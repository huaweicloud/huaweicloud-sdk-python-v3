# coding: utf-8

import pprint
import re

import six





class TaxiInvoiceResultBody:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'location': 'str',
        'code': 'str',
        'number': 'str',
        'phone_number': 'str',
        'company': 'str',
        'taxi_number': 'str',
        'certificate_number': 'str',
        'identification_number': 'str',
        'date': 'str',
        'boarding_time': 'str',
        'alighting_time': 'str',
        'time': 'str',
        'unit_price': 'str',
        'distance': 'str',
        'waiting_time': 'str',
        'fare': 'str',
        'fuel_oil_surcharge': 'str',
        'call_service_surcharge': 'str',
        'total': 'str',
        'confidence': 'object'
    }

    attribute_map = {
        'location': 'location',
        'code': 'code',
        'number': 'number',
        'phone_number': 'phone_number',
        'company': 'company',
        'taxi_number': 'taxi_number',
        'certificate_number': 'certificate_number',
        'identification_number': 'identification_number',
        'date': 'date',
        'boarding_time': 'boarding_time',
        'alighting_time': 'alighting_time',
        'time': 'time',
        'unit_price': 'unit_price',
        'distance': 'distance',
        'waiting_time': 'waiting_time',
        'fare': 'fare',
        'fuel_oil_surcharge': 'fuel_oil_surcharge',
        'call_service_surcharge': 'call_service_surcharge',
        'total': 'total',
        'confidence': 'confidence'
    }

    def __init__(self, location=None, code=None, number=None, phone_number=None, company=None, taxi_number=None, certificate_number=None, identification_number=None, date=None, boarding_time=None, alighting_time=None, time=None, unit_price=None, distance=None, waiting_time=None, fare=None, fuel_oil_surcharge=None, call_service_surcharge=None, total=None, confidence=None):
        """TaxiInvoiceResultBody - a model defined in huaweicloud sdk"""
        
        

        self._location = None
        self._code = None
        self._number = None
        self._phone_number = None
        self._company = None
        self._taxi_number = None
        self._certificate_number = None
        self._identification_number = None
        self._date = None
        self._boarding_time = None
        self._alighting_time = None
        self._time = None
        self._unit_price = None
        self._distance = None
        self._waiting_time = None
        self._fare = None
        self._fuel_oil_surcharge = None
        self._call_service_surcharge = None
        self._total = None
        self._confidence = None
        self.discriminator = None

        if location is not None:
            self.location = location
        if code is not None:
            self.code = code
        if number is not None:
            self.number = number
        if phone_number is not None:
            self.phone_number = phone_number
        if company is not None:
            self.company = company
        if taxi_number is not None:
            self.taxi_number = taxi_number
        if certificate_number is not None:
            self.certificate_number = certificate_number
        if identification_number is not None:
            self.identification_number = identification_number
        if date is not None:
            self.date = date
        if boarding_time is not None:
            self.boarding_time = boarding_time
        if alighting_time is not None:
            self.alighting_time = alighting_time
        if time is not None:
            self.time = time
        if unit_price is not None:
            self.unit_price = unit_price
        if distance is not None:
            self.distance = distance
        if waiting_time is not None:
            self.waiting_time = waiting_time
        if fare is not None:
            self.fare = fare
        if fuel_oil_surcharge is not None:
            self.fuel_oil_surcharge = fuel_oil_surcharge
        if call_service_surcharge is not None:
            self.call_service_surcharge = call_service_surcharge
        if total is not None:
            self.total = total
        if confidence is not None:
            self.confidence = confidence

    @property
    def location(self):
        """Gets the location of this TaxiInvoiceResultBody.

        归属地区。 

        :return: The location of this TaxiInvoiceResultBody.
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this TaxiInvoiceResultBody.

        归属地区。 

        :param location: The location of this TaxiInvoiceResultBody.
        :type: str
        """
        self._location = location

    @property
    def code(self):
        """Gets the code of this TaxiInvoiceResultBody.

        发票代码。 

        :return: The code of this TaxiInvoiceResultBody.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this TaxiInvoiceResultBody.

        发票代码。 

        :param code: The code of this TaxiInvoiceResultBody.
        :type: str
        """
        self._code = code

    @property
    def number(self):
        """Gets the number of this TaxiInvoiceResultBody.

        发票号码。 

        :return: The number of this TaxiInvoiceResultBody.
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this TaxiInvoiceResultBody.

        发票号码。 

        :param number: The number of this TaxiInvoiceResultBody.
        :type: str
        """
        self._number = number

    @property
    def phone_number(self):
        """Gets the phone_number of this TaxiInvoiceResultBody.

        电话（包括电话、监督电话）。 

        :return: The phone_number of this TaxiInvoiceResultBody.
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """Sets the phone_number of this TaxiInvoiceResultBody.

        电话（包括电话、监督电话）。 

        :param phone_number: The phone_number of this TaxiInvoiceResultBody.
        :type: str
        """
        self._phone_number = phone_number

    @property
    def company(self):
        """Gets the company of this TaxiInvoiceResultBody.

        单位。 

        :return: The company of this TaxiInvoiceResultBody.
        :rtype: str
        """
        return self._company

    @company.setter
    def company(self, company):
        """Sets the company of this TaxiInvoiceResultBody.

        单位。 

        :param company: The company of this TaxiInvoiceResultBody.
        :type: str
        """
        self._company = company

    @property
    def taxi_number(self):
        """Gets the taxi_number of this TaxiInvoiceResultBody.

        车号。 

        :return: The taxi_number of this TaxiInvoiceResultBody.
        :rtype: str
        """
        return self._taxi_number

    @taxi_number.setter
    def taxi_number(self, taxi_number):
        """Sets the taxi_number of this TaxiInvoiceResultBody.

        车号。 

        :param taxi_number: The taxi_number of this TaxiInvoiceResultBody.
        :type: str
        """
        self._taxi_number = taxi_number

    @property
    def certificate_number(self):
        """Gets the certificate_number of this TaxiInvoiceResultBody.

        证号。 

        :return: The certificate_number of this TaxiInvoiceResultBody.
        :rtype: str
        """
        return self._certificate_number

    @certificate_number.setter
    def certificate_number(self, certificate_number):
        """Sets the certificate_number of this TaxiInvoiceResultBody.

        证号。 

        :param certificate_number: The certificate_number of this TaxiInvoiceResultBody.
        :type: str
        """
        self._certificate_number = certificate_number

    @property
    def identification_number(self):
        """Gets the identification_number of this TaxiInvoiceResultBody.

        识别编号。 

        :return: The identification_number of this TaxiInvoiceResultBody.
        :rtype: str
        """
        return self._identification_number

    @identification_number.setter
    def identification_number(self, identification_number):
        """Sets the identification_number of this TaxiInvoiceResultBody.

        识别编号。 

        :param identification_number: The identification_number of this TaxiInvoiceResultBody.
        :type: str
        """
        self._identification_number = identification_number

    @property
    def date(self):
        """Gets the date of this TaxiInvoiceResultBody.

        开票日期。 

        :return: The date of this TaxiInvoiceResultBody.
        :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this TaxiInvoiceResultBody.

        开票日期。 

        :param date: The date of this TaxiInvoiceResultBody.
        :type: str
        """
        self._date = date

    @property
    def boarding_time(self):
        """Gets the boarding_time of this TaxiInvoiceResultBody.

        上车时间。 

        :return: The boarding_time of this TaxiInvoiceResultBody.
        :rtype: str
        """
        return self._boarding_time

    @boarding_time.setter
    def boarding_time(self, boarding_time):
        """Sets the boarding_time of this TaxiInvoiceResultBody.

        上车时间。 

        :param boarding_time: The boarding_time of this TaxiInvoiceResultBody.
        :type: str
        """
        self._boarding_time = boarding_time

    @property
    def alighting_time(self):
        """Gets the alighting_time of this TaxiInvoiceResultBody.

        下车时间。 

        :return: The alighting_time of this TaxiInvoiceResultBody.
        :rtype: str
        """
        return self._alighting_time

    @alighting_time.setter
    def alighting_time(self, alighting_time):
        """Sets the alighting_time of this TaxiInvoiceResultBody.

        下车时间。 

        :param alighting_time: The alighting_time of this TaxiInvoiceResultBody.
        :type: str
        """
        self._alighting_time = alighting_time

    @property
    def time(self):
        """Gets the time of this TaxiInvoiceResultBody.

        时间(起止时间、上下车时间)。 

        :return: The time of this TaxiInvoiceResultBody.
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this TaxiInvoiceResultBody.

        时间(起止时间、上下车时间)。 

        :param time: The time of this TaxiInvoiceResultBody.
        :type: str
        """
        self._time = time

    @property
    def unit_price(self):
        """Gets the unit_price of this TaxiInvoiceResultBody.

        单价。 

        :return: The unit_price of this TaxiInvoiceResultBody.
        :rtype: str
        """
        return self._unit_price

    @unit_price.setter
    def unit_price(self, unit_price):
        """Sets the unit_price of this TaxiInvoiceResultBody.

        单价。 

        :param unit_price: The unit_price of this TaxiInvoiceResultBody.
        :type: str
        """
        self._unit_price = unit_price

    @property
    def distance(self):
        """Gets the distance of this TaxiInvoiceResultBody.

        总里程。 

        :return: The distance of this TaxiInvoiceResultBody.
        :rtype: str
        """
        return self._distance

    @distance.setter
    def distance(self, distance):
        """Sets the distance of this TaxiInvoiceResultBody.

        总里程。 

        :param distance: The distance of this TaxiInvoiceResultBody.
        :type: str
        """
        self._distance = distance

    @property
    def waiting_time(self):
        """Gets the waiting_time of this TaxiInvoiceResultBody.

        等候时间。 

        :return: The waiting_time of this TaxiInvoiceResultBody.
        :rtype: str
        """
        return self._waiting_time

    @waiting_time.setter
    def waiting_time(self, waiting_time):
        """Sets the waiting_time of this TaxiInvoiceResultBody.

        等候时间。 

        :param waiting_time: The waiting_time of this TaxiInvoiceResultBody.
        :type: str
        """
        self._waiting_time = waiting_time

    @property
    def fare(self):
        """Gets the fare of this TaxiInvoiceResultBody.

        金额。 

        :return: The fare of this TaxiInvoiceResultBody.
        :rtype: str
        """
        return self._fare

    @fare.setter
    def fare(self, fare):
        """Sets the fare of this TaxiInvoiceResultBody.

        金额。 

        :param fare: The fare of this TaxiInvoiceResultBody.
        :type: str
        """
        self._fare = fare

    @property
    def fuel_oil_surcharge(self):
        """Gets the fuel_oil_surcharge of this TaxiInvoiceResultBody.

        燃油附加费。 

        :return: The fuel_oil_surcharge of this TaxiInvoiceResultBody.
        :rtype: str
        """
        return self._fuel_oil_surcharge

    @fuel_oil_surcharge.setter
    def fuel_oil_surcharge(self, fuel_oil_surcharge):
        """Sets the fuel_oil_surcharge of this TaxiInvoiceResultBody.

        燃油附加费。 

        :param fuel_oil_surcharge: The fuel_oil_surcharge of this TaxiInvoiceResultBody.
        :type: str
        """
        self._fuel_oil_surcharge = fuel_oil_surcharge

    @property
    def call_service_surcharge(self):
        """Gets the call_service_surcharge of this TaxiInvoiceResultBody.

        电调费（预约费）。 

        :return: The call_service_surcharge of this TaxiInvoiceResultBody.
        :rtype: str
        """
        return self._call_service_surcharge

    @call_service_surcharge.setter
    def call_service_surcharge(self, call_service_surcharge):
        """Sets the call_service_surcharge of this TaxiInvoiceResultBody.

        电调费（预约费）。 

        :param call_service_surcharge: The call_service_surcharge of this TaxiInvoiceResultBody.
        :type: str
        """
        self._call_service_surcharge = call_service_surcharge

    @property
    def total(self):
        """Gets the total of this TaxiInvoiceResultBody.

        实收金额。 

        :return: The total of this TaxiInvoiceResultBody.
        :rtype: str
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this TaxiInvoiceResultBody.

        实收金额。 

        :param total: The total of this TaxiInvoiceResultBody.
        :type: str
        """
        self._total = total

    @property
    def confidence(self):
        """Gets the confidence of this TaxiInvoiceResultBody.

        相关字段的置信度信息，置信度越大，表示本次识别的对应字段的可靠性越高，在统计意义上，置信度越大，准确率越高。 置信度由算法给出，不直接等价于对应字段的准确率。 

        :return: The confidence of this TaxiInvoiceResultBody.
        :rtype: object
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        """Sets the confidence of this TaxiInvoiceResultBody.

        相关字段的置信度信息，置信度越大，表示本次识别的对应字段的可靠性越高，在统计意义上，置信度越大，准确率越高。 置信度由算法给出，不直接等价于对应字段的准确率。 

        :param confidence: The confidence of this TaxiInvoiceResultBody.
        :type: object
        """
        self._confidence = confidence

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                if attr in self.sensitive_list:
                    result[attr] = "****"
                else:
                    result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TaxiInvoiceResultBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
