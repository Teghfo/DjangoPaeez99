from flask import Flask
import random

app = Flask(__name__)
 
 
@app.route('/')
def numpy_rand_num():
    x = random.randint(1,100)
    return f"{x}"
 
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
