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
    menus = []
    menu1 = Menu(name = "Smocha", price=60)
    menus.append(menu1)
    rnb = Menu(name="Rice n Beans", price=150)
    menus.append(rnb)
    shawarma = Menu(name="Shawarma", price=300)
    menus.append(shawarma)
    hotdog = Menu(name="Hotdog", price=150)
    menus.append(hotdog)
    pilau = Menu(name="Pilau", price=200)
    menus.append(pilau)
    burgers = Menu(name="Burgers", price=350)
    menus.append(burgers)

    db.session.add_all(menus)
    db.session.commit()

    print("Menus seeded")
