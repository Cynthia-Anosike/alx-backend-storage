from app import db

class Students(db.Model):
    """Record for Engineering Students"""
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(50), index=True)
    last_name = db.Column(db.String(50), index=True)
    department = db.Column(db.String(100), index=True)
    email = db.Column(db.String(50), index=True)
    Addr = db.Column(db.String(100))
    pin = db.Column(db.String(10), unique=True, primary_key=True)

    def __init__(self, first_name, last_name, department, email, Addr, pin):
        self.first_name = first_name
        self.last_name = last_name
        self.department = department
        self.email = email
        self.Addr = Addr
        self.pin = pin

    def __repr__(self):
        return '<Students {}>'.format(self.first_name)
