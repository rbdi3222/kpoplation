from flask import Flask, request, send_from_directory
import requests
import os
app = Flask(__name__, static_folder='static')

@app.route('/robots.txt')
def robots_txt():
    return send_from_directory(os.path.dirname(os.path.abspath(__file__)), 'robots.txt')

@app.route('/sitemap.xml')
def sitemap_xml():
    return send_from_directory(os.path.dirname(os.path.abspath(__file__)), 'sitemap.xml')

# KOSIS API 프록시
@app.route('/kosis_proxy')
def kosis_proxy():
    base_url = "https://kosis.kr/openapi/Param/statisticsParameterData.do"
    params = request.args.to_dict()
    response = requests.get(base_url, params=params)
    return (response.content, response.status_code, {'Content-Type': response.headers['Content-Type']})

# 정적파일 서비스 (index.html)
@app.route('/')
def serve_index():
    return send_from_directory('static', 'index.html')

# 기타 정적파일(js, css 등)
@app.route('/static/<path:path>')
def serve_static(path):
    return send_from_directory('static', path)

if __name__ == '__main__':
    # 개발용: app.run(debug=True)
    # 운영용: waitress 등으로 실행 권장
    app.run(host='0.0.0.0', port=8080, debug=True)
