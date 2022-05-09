from flask import redirect, render_template,session, request, url_for, flash
from shop import app,db, photos
from .models import Brand, Category, Addproduct
from .forms import Addproducts
import secrets

@app.route('/addbrand',methods=['GET','POST'])
def addbrand():
    if request.method=="POST":
        getbrand = request.form.get('brand')
        brand = Brand(name=getbrand)
        db.session.add(brand)
        flash(f'The Brand {getbrand} was added to your database', 'success')
        db.session.commit()
        return redirect(url_for('addbrand'))

    return render_template('products/addbrand.html', brands='brands')





@app.route('/addcat',methods=['GET','POST'])
def addcat():
    if request.method=="POST":
        getbrand = request.form.get('category')
        cat = Category(name=getbrand)
        db.session.add(cat)
        flash(f'The category {getbrand} was added to your database', 'success')
        db.session.commit()
        return redirect(url_for('addcat'))

    return render_template('products/addbrand.html')

@app.route('/addproduct', methods=['GET','POST'])
def addproduct():
    brands = Brand.query.all()
    categories = Category.query.all()
    form = Addproducts(request.form)
    if request.method=="POST":
        name = form.name.data
        price = form.price.data
        discount = form.discount.data
        stock = form.stock.data
        colors = form.colors.data
        desc = form.discription.data
        brand = request.form.get('brand')
        category = request.form.get('category')
        image_1 = photos.save(request.files.get('image_1'), name=secrets.token_hex(10) + ".")
        image_2 = photos.save(request.files.get('image_2'), name=secrets.token_hex(10) + ".")
        image_3 = photos.save(request.files.get('image_3'), name=secrets.token_hex(10) + ".")
        addproduct = Addproduct(name=name,price=price,discount=discount,stock=stock,colors=colors,desc=desc,category_id=category,brand_id=brand,image_1=image_1,image_2=image_2,image_3=image_3)
        db.session.add(addproduct)
        flash(f'The product {name} was added in database','success')
        db.session.commit()
    return render_template('products/addproduct.html', title='Add a Product', form = form, brands=brands, categories=categories)