from datetime import datetime
from app import app
from models import db, Menu, Category

# faker

#
with app.app_context():
    print("Start seeding...........")

    # 1. Delete the initial data if any
    Category.query.delete()
    Menu.query.delete()

    # 2. Start adding data to our models and persist to db
    category = Category(name="Lunch")
    db.session.add(category)
    db.session.commit()

    print("Category seeded")

    menus = []
    menu1 = Menu(name = "Smocha", price=60, quantity=10, category=category, created_at=datetime.now())
    menus.append(menu1)
    rnb = Menu(name="Rice n Beans", price=150, quantity=10, category=category, created_at=datetime.now())
    menus.append(rnb)
    shawarma = Menu(name="Shawarma", price=300, quantity=10, category=category, created_at=datetime.now())
    menus.append(shawarma)
    hotdog = Menu(name="Hotdog", price=150, quantity=10, category=category, created_at=datetime.now())
    menus.append(hotdog)
    pilau = Menu(name="Pilau", price=200, quantity=10, category=category, created_at=datetime.now())
    menus.append(pilau)
    burgers = Menu(name="Burgers", price=350, quantity=10, category=category, created_at=datetime.now())
    menus.append(burgers)

    db.session.add_all(menus)
    db.session.commit()

    print("Menus seeded")
