import pandas as pd 
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
from models import *
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = r"postgresql://postgres:1@localhost:5432/guru99"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)
dataframe = pd.read_csv(r'E:\CS50\project0\webdev-training-summer-2020\Register\blog.csv',index_col=0)

def main():
    
    for i in range(0,len(dataframe.values)):
        row = dataframe.iloc[[i]].values[0]
        # print(row)
        new_blog = Blog(title=row[0],users=row[1],ratings_count=row[2],date=row[3])
        db.session.add(new_blog)
        db.session.commit()
    db.create_all()
# print(dataframe.iloc[[0]])
    
if __name__ == "__main__":
    with app.app_context():
        main()
