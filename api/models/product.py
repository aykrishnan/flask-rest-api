from api.configuration import Configuration


db = Configuration.get_db()

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(512), unique=True, nullable=False)
    price = db.Column(db.Numeric)

    def __str__(self):
        return f'Product [id={self.id}, name={self.name}, price={self.price}]'
