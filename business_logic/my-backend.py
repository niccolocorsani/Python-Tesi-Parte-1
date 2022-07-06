from flask import Flask, request
import os
import time


from flask_cors import cross_origin, CORS


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

def format_server_time():
    server_time = time.localtime()
    return time.strftime("%I:%M:%S %p", server_time)


@app.route('/data/')
@cross_origin()
def index():


    # here we want to get the value of user (i.e. ?user=some-value)

    # http://127.0.0.1:8080/data/?user=mail%20del%2022giugno*corsani.niccolo.94@gmail.com     * che delimita il contenuto da l'indirizzo
    values = request.args.get('user')
    splitted = values.split('*')
    print('values: ' + splitted[0] + ' ' + splitted[1])
    return values




if __name__ == '__main__':


    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
