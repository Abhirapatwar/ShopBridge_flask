from flask import Flask,render_template,request,redirect,url_for,flash
from flask_sqlalchemy import SQLAlchemy


app=Flask(__name__)
app.config['SECRET_KEY']='SECRET123'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///Usertable.db'
app.config['SQLALCHEMY_TRACK_MODIFICATION']=True

db=SQLAlchemy(app)

#creating a model
class Usertable(db.Model):
    ID=db.Column(db.Integer,primary_key=True)
    Name=db.Column(db.String(200),nullable=False)
    Price=db.Column(db.Integer,nullable=False)
    Qty=db.Column(db.Integer,nullable=False)
    Description=db.Column(db.String(200),nullable=False)

@app.route('/insert',methods=['POST'])
def Insert():
    if request.method == 'POST':
        Name=request.form['pname']
        Price=request.form['pprice']
        Qty=request.form['pqty']
        Description=request.form['pdesc']

        my_data = Usertable(Name=Name,Price=Price,Qty=Qty,Description=Description)
        db.session.add(my_data)
        db.session.commit()

        flash("Entry Added successfully")

        return redirect(url_for('Home'))


@app.route('/')
def Home():
    all_data=Usertable.query.all()
    # return "<h1> flask started </h1>"
    return render_template('Home.html', all_data=all_data)

@app.route('/update',methods=['GET','POST'])
def update():
    new_data=Usertable.query.get(request.form.get('id'))
    print(new_data)
    new_data.Name=request.form['newname']
    new_data.Price=request.form['newprice']
    new_data.Qty=request.form['newqty']
    new_data.Description=request.form['newdesc']
    db.session.commit()

    flash("Entry Updated successfully")

    return redirect(url_for('Home'))

@app.route('/delete/<id>',methods=['GET','POST'])
def delete(id):
    to_delete=Usertable.query.get(id)
    db.session.delete(to_delete)
    db.session.commit()

    flash("Entry deleted successfully")

    return redirect(url_for('Home'))


if __name__=='__main__':
    app.run(debug=True)    