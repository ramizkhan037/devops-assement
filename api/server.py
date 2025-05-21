from flask import Flask, request, jsonify
import os, mysql.connector

app = Flask(__name__)

DB_HOST = os.getenv('DB_HOST')
DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')
DB_NAME = os.getenv('DB_NAME')

def get_db():
    return mysql.connector.connect(
        host=DB_HOST, user=DB_USER, password=DB_PASS, database=DB_NAME
    )

@app.route('/log-ip', methods=['POST'])
def log_ip():
     client_ip = (
        request.headers.get("X-Forwarded-For", request.remote_addr)
        .split(",")[0]
        .strip()
    )

    conn = get_db(); cur = conn.cursor()
    cur.execute("""
      CREATE TABLE IF NOT EXISTS ip_logs (
        id INT AUTO_INCREMENT PRIMARY KEY,
        ip VARCHAR(45),
        logged_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
      )
    """)
    cur.execute("INSERT INTO ip_logs (ip) VALUES (%s)", (ip,))
    conn.commit(); cur.close(); conn.close()
    return jsonify(status="ok", ip=ip), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
