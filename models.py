from myapp import db



class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    boatname = db.Column(db.String(100))
    price = db.Column(db.String(100))
    length = db.Column(db.String(100))
    numberofguests = db.Column(db.String(100))
    numberofcabins = db.Column(db.String(100))
    bodylength = db.Column(db.String(100))
    beamlength = db.Column(db.String(100))
    draft = db.Column(db.String(100))
    crewnumber = db.Column(db.String(100))
    builtyear = db.Column(db.String(100))
    producer = db.Column(db.String(100))
    engine = db.Column(db.String(100))
    cruisespeed = db.Column(db.String(100))




    def __repr__(self):
         return f"User('{self.boatname}', '{self.price}')"


class Info(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    interestedboat = db.Column(db.String(100))
    destination = db.Column(db.String(100))
    sex = db.Column(db.String(100))
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(100))
    availabletime = db.Column(db.String(100))
    notes = db.Column(db.String(100))


    def __repr__(self):
        return f"Info('{self.interestedboat}', '{self.destination}', '{self.sex}', '{self.name}', '{self.email}', '{self.phone}', '{self.availabletime}', '{self.notes}')"