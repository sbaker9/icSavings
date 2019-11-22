from app import app, db
from flask import flash


@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"


@app.route('/reset_db')
def reset_db():
    flash("Resetting database: deleting old data and repopulating with dummy data")
    # clear all data from all tables
    meta = db.metadata
    for table in reversed(meta.sorted_tables):
        print('Clear table {}'.format(table))
        db.session.execute(table.delete())
    db.session.commit()

    # adding dummy data--

    a1 = Product(name="", info="", url="", favorite=False, category="")
    a2 = Product(name="=", info="", url="", favorite=True, category="")
    a3 = Product(name="", info="", url="", favorite=False, category="")
    a4 = Product(name="", info="", url="", favorite=True, category="")
    a5 = Product(name="", info="", url="", favorite=False, category="")

    db.session.add(a1)
    db.session.add(a2)
    db.session.add(a3)
    db.session.add(a4)
    db.session.add(a5)

    v1 = Price(price=0.01, streetAddress="4 Pennsylvania Plaza", city="New York City", state="NY", capacity=20789)
    v2 = Price(price="", streetAddress="1 MetLife Stadium Dr", city="East Rutherford", state="NJ", capacity=82500)
    v3 = Price(price="", streetAddress="200 Main St", city="Portland", state="ME", capacity=6500)

    db.session.add(v1)
    db.session.add(v2)
    db.session.add(v3)

    e1 = Event(name="Country Music Festival", datetime=datetime(2019, 10, 14), venue=v1)
    e2 = Event(name="Jimmy Hendrix Final Concert", datetime=datetime(1970, 9, 6), venue=v1)
    e3 = Event(name="Comedy Music Festival", datetime=datetime(2017, 6, 18), venue=v2)
    e4 = Event(name="Phillip Phillips Live in Concert", datetime=datetime(2017, 4, 21), venue=v3)
    e5 = Event(name="Bo Burnham's Jimmy Hendrix Seance", datetime=datetime(2015, 9, 6), venue=v2)
    e6 = Event(name="Jack Black's Back in Black", datetime=datetime(2010, 8, 12), venue=v2)
    e7 = Event(name="Bo Burnham's Make Happy", datetime=datetime(2016, 6, 3), venue=v3)

    db.session.add(e1)
    db.session.add(e2)
    db.session.add(e3)
    db.session.add(e4)
    db.session.add(e5)
    db.session.add(e6)
    db.session.add(e7)

    ae1 = ArtistToEvent(artistID=1, eventID=1)
    ae2 = ArtistToEvent(artistID=1, eventID=4)
    ae3 = ArtistToEvent(artistID=2, eventID=2)
    ae4 = ArtistToEvent(artistID=2, eventID=5)
    ae5 = ArtistToEvent(artistID=3, eventID=6)
    ae6 = ArtistToEvent(artistID=3, eventID=3)
    ae7 = ArtistToEvent(artistID=4, eventID=3)
    ae8 = ArtistToEvent(artistID=4, eventID=5)
    ae9 = ArtistToEvent(artistID=4, eventID=7)

    db.session.add(ae1)
    db.session.add(ae2)
    db.session.add(ae3)
    db.session.add(ae4)
    db.session.add(ae5)
    db.session.add(ae6)
    db.session.add(ae7)
    db.session.add(ae8)
    db.session.add(ae9)

    db.session.commit()

    return redirect(url_for('index'))