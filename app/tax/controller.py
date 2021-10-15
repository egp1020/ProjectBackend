from app import app, db
from app.tax.model import Tax

class TaxController:
    def getTaxAll(self):
        taxs = Tax.query.all()
        tax = []

        for element in taxs:
            tax.append({
                'id':element.id,
                'taxType':element.taxType,
                'rate':element.rate
            })
        return tax

    def getTax(self, id):
        taxs = []
        tax = Tax.query.filter_by(id=id).first()

        if tax is not None:
            taxs.append({
                'id':tax.id,
                'taxType':tax.taxType,
                'rate':tax.rate
            })
        else:
            taxs.append({
                'messages':'no se encontro id.',
            })
        return taxs

    def insertTax(self, tax):
        if tax is not None:
            taxType = tax["taxType"]
            rate = tax["rate"]
            
            newTax = Tax(taxType, rate)
            db.session.add(newTax)
            db.session.commit()

            message = "El registro se hizo con éxito"
        else:
            message = "El registro no se logro."
        return message

    def updateTax(self, tax, id):
        taxType = tax["taxType"]
        rate = tax["rate"]
        tax = Tax.query.get(id)
        if tax is not None:
            tax.taxType = taxType
            tax.rate = rate
            db.session.commit()
            message = "El impuesto se actualizo correctamente"
        else:
            message = "La actualización no se pudo realizar con éxito"
        return message


    def deleteTax(self, id):
        tax = Tax.query.filter_by(id=id).first()
        if tax is not None:
            db.session.delete(tax)
            db.session.commit()
            message = "El impuesto ha sido eliminado con éxito."
        else:
            message = "El impuesto no se pudo eliminar."

        return message