from Flask import Flask, request, jsonify
app=Flask(__name__)

@app.route('/hello')
def get_location_names():
    response=jsonify [{
        'Locations': util.get_location_names
    }]
    response.headers.add('Access-control-Allow-Origin, '-')
    
    return 'hi'
    
    
if __name__ =='__main__':
    print ('Starting Python Flask Server for Home Price Prediction...')
    app.run()
