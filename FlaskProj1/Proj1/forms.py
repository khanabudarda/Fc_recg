from typing import Dict

from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, SubmitField
from wtforms.validators import Length, DataRequired
from wtforms.widgets.html5 import NumberInput
from wtforms.fields.html5 import TelField


class PhoneRecharge(FlaskForm):
    prvlst: Dict[str, str] = {'Airtel': 'AT',
                              'BSNL': 'BS',
                              'Idea': 'ID',
                              'Vodafone': 'VF',
                              'Tata Docomo GSM': 'TD',
                              'Tata Docomo CDMA': 'TA',
                              'Jio': 'JP'}
    phoneno = TelField('Phone Number', widget=NumberInput(), validators=[DataRequired()])
    prvdr = SelectField('Select Operator',
                        choices=[('AT', 'Airtel'), ('BS', 'BSNL'), ('ID', 'Idea'), ('VF', 'Vodafone'),
                                 ('TD', 'Tata Docomo GSM'), ('TA', 'Tata Docomo CDMA'), ('JP', 'Jio')],
                        validators=[DataRequired()])
    amtrec = StringField('Amount', widget=NumberInput(), validators=[DataRequired()])
    rechg = SubmitField('Recharge')


class MetroRecharge(FlaskForm):
    phoneno = TelField('Phone Number', widget=NumberInput(), validators=[DataRequired()])
    prvdr = SelectField('Select Operator',
                        choices=[('AT', 'Airtel'), ('BS', 'BSNL'), ('ID', 'Idea'), ('VF', 'Vodafone'),
                                 ('TD', 'Tata Docomo GSM'), ('TA', 'Tata Docomo CDMA'), ('JP', 'Jio')],
                        validators=[DataRequired()])
    amtrec = StringField('Amount', widget=NumberInput(), validators=[DataRequired()])
    rechg = SubmitField('Recharge')


class DTHRecharge(FlaskForm):
    phoneno = TelField('Phone Number', widget=NumberInput(), validators=[DataRequired()])
    prvdr = SelectField('Select Operator',
                        choices=[('AD', 'Airtel Digital TV'), ('DS', 'Dish TV'), ('BT', 'Reliance Big TV'), ('SD', 'Sun Direct TV'),
                                 ('TS', 'Tata Sky'), ('VD', 'Videocon D2H')],
                        validators=[DataRequired()])
    amtrec = StringField('Amount', widget=NumberInput(), validators=[DataRequired()])
    rechg = SubmitField('Recharge')


class WaterRecharge(FlaskForm):
    phoneno = TelField('Phone Number', widget=NumberInput(), validators=[DataRequired()])
    prvdr = SelectField('Select Operator',
                        choices=[('NMW', 'NDMC Water'), ('DJW', 'Delhi Jal Board'), ('MGW', 'Municipal Corporation Of Gurugram')],
                        validators=[DataRequired()])
    amtrec = StringField('Amount', widget=NumberInput(), validators=[DataRequired()])
    rechg = SubmitField('Recharge')


class ElectRecharge(FlaskForm):
    phoneno = TelField('Phone Number', widget=NumberInput(), validators=[DataRequired()])
    prvdr = SelectField('Select Operator',
                        choices=[('DNE', 'Dnh Power Distribution Company Limited'), ('DHB', 'Dakshin Haryana Bijli Vitran Nigam (dhbvn)'),
                                 ('BRE', 'Bses Rajdhani - Delhi Electricity'), ('BSY', 'Bses Yamuna - Delhi Electricity'),
                                 ('UHB', 'Uttar Haryana Bijli Vitran Nigam (uhbvn)'), ('URE', 'Uttar Pradesh Power Corp Ltd (uppcl) - Rural'),
                                 ('UBE', 'Uttar Pradesh Power Corp Ltd (uppcl) - Urban') ,('NDE', 'Tata Power - Delhi Electricity'),
                                 ('NUE', 'Noida Power - Noida Electricity')],
                        validators=[DataRequired()])
    amtrec = StringField('Amount', widget=NumberInput(), validators=[DataRequired()])
    rechg = SubmitField('Recharge')