from flask import Blueprint, jsonify, request
from services.chat_service import ChatService
from services.insights_service import InsightsService
import os
import pandas as pd
from werkzeug.utils import secure_filename
import tempfile
import requests
from PyPDF2 import PdfReader
import sqlite3

chat_bp = Blueprint('chat', __name__)
chat_service = ChatService()
insights_service = InsightsService()

@chat_bp.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        table_name = data.get('tableName')
        query = data.get('query')
        
        if not table_name or not query:
            return jsonify({"error": "Missing tableName or query"}), 400
            
        result = chat_service.process_query(table_name, query)
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@chat_bp.route('/newChat', methods=['POST'])
def new_chat():
    try:
        if 'csv' not in request.files or 'pdf' not in request.files:
            return jsonify({"error": "Missing CSV or PDF file"}), 400
            
        csv_file = request.files['csv']
        pdf_file = request.files['pdf']
        table_name = request.form.get('tableName')
        
        if not table_name:
            return jsonify({"error": "Missing tableName"}), 400
            
        temp_dir = tempfile.mkdtemp()
        csv_path = os.path.join(temp_dir, secure_filename(csv_file.filename))
        pdf_path = os.path.join(temp_dir, secure_filename(pdf_file.filename))
        
        csv_file.save(csv_path)
        pdf_file.save(pdf_path)
        
        df = pd.read_csv(csv_path)
        
        pdf_reader = PdfReader(pdf_path)
        jd_text = ""
        for page in pdf_reader.pages:
            jd_text += page.extract_text()
            
        result = chat_service.process_new_chat(df, jd_text, table_name)
        
        os.remove(csv_path)
        os.remove(pdf_path)
        os.rmdir(temp_dir)
        
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@chat_bp.route('/gettables', methods=['GET'])
def get_tables():
    try:
        tables = chat_service.get_all_tables()
        return jsonify({"tables": tables})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@chat_bp.route('/getinsights', methods=['GET'])
def get_insights():
    try:
        table_name = request.args.get('tableName')
        if not table_name:
            return jsonify({"error": "Missing tableName"}), 400
            
        table_data = chat_service.get_table_insights(table_name)
        insights = insights_service.generate_insights(table_name, table_data)
        
        return jsonify(insights)
    except Exception as e:
        return jsonify({"error": str(e)}), 500 