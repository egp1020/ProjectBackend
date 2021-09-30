import base64
import os, flask
import sys
from app import app, db
from app.taxDetails.model import TaxDetails

class TaxDetailsController:
    def getTaxDetailsAll(self):
        taxDetails = TaxDetails.query.all()
        taxDetail = []

        for element in taxDetails:
            taxDetail.append({
                'id':element.id,
                'taxType':element.taxType,
                'amountBuy':element.amountBuy,
                'baseBuy':element.baseBuy,
                'valueTax':element.valueTax
            })
        return tax

    def getTaxDetails(self, id):
        taxDetails = []
        taxDetail = TaxDetails.query.filter_by(id=id).first()

        if taxDetail is not None:
            taxDetails.append({
                'id':taxDetail.id,
                'taxType':taxDetail.taxType,
                'amountBuy':taxDetail.amountBuy,
                'baseBuy':taxDetail.baseBuy,
                'valueTax':taxDetail.valueTax
            })
        else:
            taxDetails.append({
                'messages':'no se encontro id.',
            })
        return taxDetails

    def insertTaxDetails(self, taxDetail):
        taxType = taxDetail["taxType"]
        amountBuy = taxDetail["amountBuy"]
        baseBuy = taxDetail["baseBuy"]
        valueTax = taxDetail["valueTax"]
        taxDetail = TaxDetails.query.filter_by(id = id).first()
        if taxDetail is not None:
            data = TaxDetails(taxType, amountBuy, baseBuy, valueTax)
            db.session.add(data)
            db.session.commit()

            message = "El registro se hizo con éxito"
        else:
            message = "El registro no se logro."
        return message

    def updateTax(self, taxDetail):
        taxType = taxDetail["taxType"]
        amountBuy = taxDetail["amountBuy"]
        baseBuy = taxDetail["baseBuy"]
        valueTax = taxDetail["valueTax"]
        taxDetail = TaxDetails.query.filter_by(id = id).first()
        if taxDetail is not None:
            taxDetail.taxType = taxType
            taxDetail.amountBuy = amountBuy
            taxDetail.baseBuy = baseBuy
            taxDetail.valueTax = valueTax
            db.session.add(taxDetail)
            db.session.commit()
            message = "El detalle de impuesto se actualizo correctamente"
        else:
            message = "La actualización no se pudo realizar con éxito"
        return message


    def deleteTax(self, id):
        taxDetail = TaxDetails.query.filter_by(id=id).first()
        if taxDetail is not None:
            db.session.delete(taxDetail)
            db.session.commit()
            message = "El detalle del impuesto ha sido eliminado con éxito."
        else:
            message = "El detalle del impuesto no se pudo eliminar."
        
        return message