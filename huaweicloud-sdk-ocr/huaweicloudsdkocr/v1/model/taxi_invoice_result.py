# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TaxiInvoiceResult:

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
        'confidence': 'object',
        'text_location': 'object'
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
        'confidence': 'confidence',
        'text_location': 'text_location'
    }

    def __init__(self, location=None, code=None, number=None, phone_number=None, company=None, taxi_number=None, certificate_number=None, identification_number=None, date=None, boarding_time=None, alighting_time=None, time=None, unit_price=None, distance=None, waiting_time=None, fare=None, fuel_oil_surcharge=None, call_service_surcharge=None, total=None, confidence=None, text_location=None):
        """TaxiInvoiceResult

        The model defined in huaweicloud sdk

        :param location: 归属地区。 
        :type location: str
        :param code: 发票代码。 
        :type code: str
        :param number: 发票号码。 
        :type number: str
        :param phone_number: 电话（包括电话、监督电话）。 
        :type phone_number: str
        :param company: 单位。 
        :type company: str
        :param taxi_number: 车号。 
        :type taxi_number: str
        :param certificate_number: 证号。 
        :type certificate_number: str
        :param identification_number: 识别编号。 
        :type identification_number: str
        :param date: 开票日期。 
        :type date: str
        :param boarding_time: 上车时间。 
        :type boarding_time: str
        :param alighting_time: 下车时间。 
        :type alighting_time: str
        :param time: 时间(起止时间、上下车时间)。 
        :type time: str
        :param unit_price: 单价。 
        :type unit_price: str
        :param distance: 总里程。 
        :type distance: str
        :param waiting_time: 等候时间。 
        :type waiting_time: str
        :param fare: 金额。 
        :type fare: str
        :param fuel_oil_surcharge: 燃油附加费。 
        :type fuel_oil_surcharge: str
        :param call_service_surcharge: 电调费（预约费）。 
        :type call_service_surcharge: str
        :param total: 实收金额。 
        :type total: str
        :param confidence: 相关字段的置信度信息，置信度越大，表示本次识别的对应字段的可靠性越高，在统计意义上，置信度越大，准确率越高。 置信度由算法给出，不直接等价于对应字段的准确率。 
        :type confidence: object
        :param text_location: 对应所有在原图上识别到的字段位置信息，包含所有文字区域四个顶点的二维坐标（x,y）。采用图像坐标系，坐标原点为图片左上角，x轴沿水平方向，y轴沿竖直方向。 
        :type text_location: object
        """
        
        

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
        self._text_location = None
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
        if text_location is not None:
            self.text_location = text_location

    @property
    def location(self):
        """Gets the location of this TaxiInvoiceResult.

        归属地区。 

        :return: The location of this TaxiInvoiceResult.
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this TaxiInvoiceResult.

        归属地区。 

        :param location: The location of this TaxiInvoiceResult.
        :type location: str
        """
        self._location = location

    @property
    def code(self):
        """Gets the code of this TaxiInvoiceResult.

        发票代码。 

        :return: The code of this TaxiInvoiceResult.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this TaxiInvoiceResult.

        发票代码。 

        :param code: The code of this TaxiInvoiceResult.
        :type code: str
        """
        self._code = code

    @property
    def number(self):
        """Gets the number of this TaxiInvoiceResult.

        发票号码。 

        :return: The number of this TaxiInvoiceResult.
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this TaxiInvoiceResult.

        发票号码。 

        :param number: The number of this TaxiInvoiceResult.
        :type number: str
        """
        self._number = number

    @property
    def phone_number(self):
        """Gets the phone_number of this TaxiInvoiceResult.

        电话（包括电话、监督电话）。 

        :return: The phone_number of this TaxiInvoiceResult.
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """Sets the phone_number of this TaxiInvoiceResult.

        电话（包括电话、监督电话）。 

        :param phone_number: The phone_number of this TaxiInvoiceResult.
        :type phone_number: str
        """
        self._phone_number = phone_number

    @property
    def company(self):
        """Gets the company of this TaxiInvoiceResult.

        单位。 

        :return: The company of this TaxiInvoiceResult.
        :rtype: str
        """
        return self._company

    @company.setter
    def company(self, company):
        """Sets the company of this TaxiInvoiceResult.

        单位。 

        :param company: The company of this TaxiInvoiceResult.
        :type company: str
        """
        self._company = company

    @property
    def taxi_number(self):
        """Gets the taxi_number of this TaxiInvoiceResult.

        车号。 

        :return: The taxi_number of this TaxiInvoiceResult.
        :rtype: str
        """
        return self._taxi_number

    @taxi_number.setter
    def taxi_number(self, taxi_number):
        """Sets the taxi_number of this TaxiInvoiceResult.

        车号。 

        :param taxi_number: The taxi_number of this TaxiInvoiceResult.
        :type taxi_number: str
        """
        self._taxi_number = taxi_number

    @property
    def certificate_number(self):
        """Gets the certificate_number of this TaxiInvoiceResult.

        证号。 

        :return: The certificate_number of this TaxiInvoiceResult.
        :rtype: str
        """
        return self._certificate_number

    @certificate_number.setter
    def certificate_number(self, certificate_number):
        """Sets the certificate_number of this TaxiInvoiceResult.

        证号。 

        :param certificate_number: The certificate_number of this TaxiInvoiceResult.
        :type certificate_number: str
        """
        self._certificate_number = certificate_number

    @property
    def identification_number(self):
        """Gets the identification_number of this TaxiInvoiceResult.

        识别编号。 

        :return: The identification_number of this TaxiInvoiceResult.
        :rtype: str
        """
        return self._identification_number

    @identification_number.setter
    def identification_number(self, identification_number):
        """Sets the identification_number of this TaxiInvoiceResult.

        识别编号。 

        :param identification_number: The identification_number of this TaxiInvoiceResult.
        :type identification_number: str
        """
        self._identification_number = identification_number

    @property
    def date(self):
        """Gets the date of this TaxiInvoiceResult.

        开票日期。 

        :return: The date of this TaxiInvoiceResult.
        :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this TaxiInvoiceResult.

        开票日期。 

        :param date: The date of this TaxiInvoiceResult.
        :type date: str
        """
        self._date = date

    @property
    def boarding_time(self):
        """Gets the boarding_time of this TaxiInvoiceResult.

        上车时间。 

        :return: The boarding_time of this TaxiInvoiceResult.
        :rtype: str
        """
        return self._boarding_time

    @boarding_time.setter
    def boarding_time(self, boarding_time):
        """Sets the boarding_time of this TaxiInvoiceResult.

        上车时间。 

        :param boarding_time: The boarding_time of this TaxiInvoiceResult.
        :type boarding_time: str
        """
        self._boarding_time = boarding_time

    @property
    def alighting_time(self):
        """Gets the alighting_time of this TaxiInvoiceResult.

        下车时间。 

        :return: The alighting_time of this TaxiInvoiceResult.
        :rtype: str
        """
        return self._alighting_time

    @alighting_time.setter
    def alighting_time(self, alighting_time):
        """Sets the alighting_time of this TaxiInvoiceResult.

        下车时间。 

        :param alighting_time: The alighting_time of this TaxiInvoiceResult.
        :type alighting_time: str
        """
        self._alighting_time = alighting_time

    @property
    def time(self):
        """Gets the time of this TaxiInvoiceResult.

        时间(起止时间、上下车时间)。 

        :return: The time of this TaxiInvoiceResult.
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this TaxiInvoiceResult.

        时间(起止时间、上下车时间)。 

        :param time: The time of this TaxiInvoiceResult.
        :type time: str
        """
        self._time = time

    @property
    def unit_price(self):
        """Gets the unit_price of this TaxiInvoiceResult.

        单价。 

        :return: The unit_price of this TaxiInvoiceResult.
        :rtype: str
        """
        return self._unit_price

    @unit_price.setter
    def unit_price(self, unit_price):
        """Sets the unit_price of this TaxiInvoiceResult.

        单价。 

        :param unit_price: The unit_price of this TaxiInvoiceResult.
        :type unit_price: str
        """
        self._unit_price = unit_price

    @property
    def distance(self):
        """Gets the distance of this TaxiInvoiceResult.

        总里程。 

        :return: The distance of this TaxiInvoiceResult.
        :rtype: str
        """
        return self._distance

    @distance.setter
    def distance(self, distance):
        """Sets the distance of this TaxiInvoiceResult.

        总里程。 

        :param distance: The distance of this TaxiInvoiceResult.
        :type distance: str
        """
        self._distance = distance

    @property
    def waiting_time(self):
        """Gets the waiting_time of this TaxiInvoiceResult.

        等候时间。 

        :return: The waiting_time of this TaxiInvoiceResult.
        :rtype: str
        """
        return self._waiting_time

    @waiting_time.setter
    def waiting_time(self, waiting_time):
        """Sets the waiting_time of this TaxiInvoiceResult.

        等候时间。 

        :param waiting_time: The waiting_time of this TaxiInvoiceResult.
        :type waiting_time: str
        """
        self._waiting_time = waiting_time

    @property
    def fare(self):
        """Gets the fare of this TaxiInvoiceResult.

        金额。 

        :return: The fare of this TaxiInvoiceResult.
        :rtype: str
        """
        return self._fare

    @fare.setter
    def fare(self, fare):
        """Sets the fare of this TaxiInvoiceResult.

        金额。 

        :param fare: The fare of this TaxiInvoiceResult.
        :type fare: str
        """
        self._fare = fare

    @property
    def fuel_oil_surcharge(self):
        """Gets the fuel_oil_surcharge of this TaxiInvoiceResult.

        燃油附加费。 

        :return: The fuel_oil_surcharge of this TaxiInvoiceResult.
        :rtype: str
        """
        return self._fuel_oil_surcharge

    @fuel_oil_surcharge.setter
    def fuel_oil_surcharge(self, fuel_oil_surcharge):
        """Sets the fuel_oil_surcharge of this TaxiInvoiceResult.

        燃油附加费。 

        :param fuel_oil_surcharge: The fuel_oil_surcharge of this TaxiInvoiceResult.
        :type fuel_oil_surcharge: str
        """
        self._fuel_oil_surcharge = fuel_oil_surcharge

    @property
    def call_service_surcharge(self):
        """Gets the call_service_surcharge of this TaxiInvoiceResult.

        电调费（预约费）。 

        :return: The call_service_surcharge of this TaxiInvoiceResult.
        :rtype: str
        """
        return self._call_service_surcharge

    @call_service_surcharge.setter
    def call_service_surcharge(self, call_service_surcharge):
        """Sets the call_service_surcharge of this TaxiInvoiceResult.

        电调费（预约费）。 

        :param call_service_surcharge: The call_service_surcharge of this TaxiInvoiceResult.
        :type call_service_surcharge: str
        """
        self._call_service_surcharge = call_service_surcharge

    @property
    def total(self):
        """Gets the total of this TaxiInvoiceResult.

        实收金额。 

        :return: The total of this TaxiInvoiceResult.
        :rtype: str
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this TaxiInvoiceResult.

        实收金额。 

        :param total: The total of this TaxiInvoiceResult.
        :type total: str
        """
        self._total = total

    @property
    def confidence(self):
        """Gets the confidence of this TaxiInvoiceResult.

        相关字段的置信度信息，置信度越大，表示本次识别的对应字段的可靠性越高，在统计意义上，置信度越大，准确率越高。 置信度由算法给出，不直接等价于对应字段的准确率。 

        :return: The confidence of this TaxiInvoiceResult.
        :rtype: object
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        """Sets the confidence of this TaxiInvoiceResult.

        相关字段的置信度信息，置信度越大，表示本次识别的对应字段的可靠性越高，在统计意义上，置信度越大，准确率越高。 置信度由算法给出，不直接等价于对应字段的准确率。 

        :param confidence: The confidence of this TaxiInvoiceResult.
        :type confidence: object
        """
        self._confidence = confidence

    @property
    def text_location(self):
        """Gets the text_location of this TaxiInvoiceResult.

        对应所有在原图上识别到的字段位置信息，包含所有文字区域四个顶点的二维坐标（x,y）。采用图像坐标系，坐标原点为图片左上角，x轴沿水平方向，y轴沿竖直方向。 

        :return: The text_location of this TaxiInvoiceResult.
        :rtype: object
        """
        return self._text_location

    @text_location.setter
    def text_location(self, text_location):
        """Sets the text_location of this TaxiInvoiceResult.

        对应所有在原图上识别到的字段位置信息，包含所有文字区域四个顶点的二维坐标（x,y）。采用图像坐标系，坐标原点为图片左上角，x轴沿水平方向，y轴沿竖直方向。 

        :param text_location: The text_location of this TaxiInvoiceResult.
        :type text_location: object
        """
        self._text_location = text_location

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
        import simplejson as json
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TaxiInvoiceResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
