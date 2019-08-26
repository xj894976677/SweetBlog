from flask import Flask
app = Flask(__name__)
print('谁在使用我', __name__)

from app import routes
