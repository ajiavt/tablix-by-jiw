#!/usr/bin/env python3
from app import app

# Tambahkan endpoint source_file_count jika belum ada
import os
from flask import jsonify

@app.route('/source_file_count')
def source_file_count():
    try:
        files = [f for f in os.listdir(app.config['SOURCE_FOLDER']) if f.endswith(".DAT")]
        return jsonify({
            "status": "success", 
            "count": len(files)
        })
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000) 