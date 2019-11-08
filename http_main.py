# -*- coding: utf-8 -*-
# @Author: JinHua
# @Date:   2019-11-08 10:30:37
# @Last Modified by:   JinHua
# @Last Modified time: 2019-11-08 10:48:30


import os
import log
import flask



logger = log.get_logger('http_main', filePath='file/http_main.log')

base_folder = os.path.dirname(os.path.abspath(__file__))
static_folder = os.path.join(base_folder, 'file')
logger.info('Static folder is {}'.format(static_folder))

app = flask.Flask('http_server', static_url_path='/static', static_folder=static_folder)


def send_file(filename):
    logger.info('Start to download file {}'.format(filename))
    with open(os.path.join(static_folder,filename), 'rb') as f:
        while 1:
            data = f.read(10 * 1024 * 1024)
            if not data:
                break
            yield data


@app.route('/status')
def check_server_status():
    logger.info('Statr to check server status')
    return '200'

@app.route('/download', methods=['GET'])
def download_file():
    filename = flask.request.args.get('filename')
    logger.info('Filename is {}'.format(filename))
    response = flask.Response(send_file(filename), content_type='application/octet-stream')
    response.headers["Content-disposition"] = 'attachment; filename={}'.format(filename)
    return  response

app.run(host="0.0.0.0", port=5678)