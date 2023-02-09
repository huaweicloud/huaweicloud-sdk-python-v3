# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TollInvoiceResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'code': 'str',
        'number': 'str',
        'entry': 'str',
        'exit': 'str',
        'amount': 'str',
        'cashier': 'str',
        'vehicle_type': 'str',
        'date': 'str',
        'time': 'str',
        'confidence': 'object',
        'text_location': 'object'
    }

    attribute_map = {
        'code': 'code',
        'number': 'number',
        'entry': 'entry',
        'exit': 'exit',
        'amount': 'amount',
        'cashier': 'cashier',
        'vehicle_type': 'vehicle_type',
        'date': 'date',
        'time': 'time',
        'confidence': 'confidence',
        'text_location': 'text_location'
    }

    def __init__(self, code=None, number=None, entry=None, exit=None, amount=None, cashier=None, vehicle_type=None, date=None, time=None, confidence=None, text_location=None):
        """TollInvoiceResult

        The model defined in huaweicloud sdk

        :param code: 发票代码。 
        :type code: str
        :param number: 发票号码。 
        :type number: str
        :param entry: 入口。 
        :type entry: str
        :param exit: 出口。 
        :type exit: str
        :param amount: 收费金额。 
        :type amount: str
        :param cashier: 收费员。 
        :type cashier: str
        :param vehicle_type: 车辆类型。 
        :type vehicle_type: str
        :param date: 日期。 
        :type date: str
        :param time: 时间。 
        :type time: str
        :param confidence: 相关字段的置信度信息，置信度越大，表示本次识别的对应字段的可靠性越高，在统计意义上，置信度越大，准确率越高。 置信度由算法给出，不直接等价于对应字段的准确率。
        :type confidence: object
        :param text_location: 对应所有在原图上识别到的字段位置信息，包含所有文字区域四个顶点的二维坐标（x,y）。采用图像坐标系，坐标原点为图片左上角，x轴沿水平方向，y轴沿竖直方向。 
        :type text_location: object
        """
        
        

        self._code = None
        self._number = None
        self._entry = None
        self._exit = None
        self._amount = None
        self._cashier = None
        self._vehicle_type = None
        self._date = None
        self._time = None
        self._confidence = None
        self._text_location = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if number is not None:
            self.number = number
        if entry is not None:
            self.entry = entry
        if exit is not None:
            self.exit = exit
        if amount is not None:
            self.amount = amount
        if cashier is not None:
            self.cashier = cashier
        if vehicle_type is not None:
            self.vehicle_type = vehicle_type
        if date is not None:
            self.date = date
        if time is not None:
            self.time = time
        if confidence is not None:
            self.confidence = confidence
        if text_location is not None:
            self.text_location = text_location

    @property
    def code(self):
        """Gets the code of this TollInvoiceResult.

        发票代码。 

        :return: The code of this TollInvoiceResult.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this TollInvoiceResult.

        发票代码。 

        :param code: The code of this TollInvoiceResult.
        :type code: str
        """
        self._code = code

    @property
    def number(self):
        """Gets the number of this TollInvoiceResult.

        发票号码。 

        :return: The number of this TollInvoiceResult.
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this TollInvoiceResult.

        发票号码。 

        :param number: The number of this TollInvoiceResult.
        :type number: str
        """
        self._number = number

    @property
    def entry(self):
        """Gets the entry of this TollInvoiceResult.

        入口。 

        :return: The entry of this TollInvoiceResult.
        :rtype: str
        """
        return self._entry

    @entry.setter
    def entry(self, entry):
        """Sets the entry of this TollInvoiceResult.

        入口。 

        :param entry: The entry of this TollInvoiceResult.
        :type entry: str
        """
        self._entry = entry

    @property
    def exit(self):
        """Gets the exit of this TollInvoiceResult.

        出口。 

        :return: The exit of this TollInvoiceResult.
        :rtype: str
        """
        return self._exit

    @exit.setter
    def exit(self, exit):
        """Sets the exit of this TollInvoiceResult.

        出口。 

        :param exit: The exit of this TollInvoiceResult.
        :type exit: str
        """
        self._exit = exit

    @property
    def amount(self):
        """Gets the amount of this TollInvoiceResult.

        收费金额。 

        :return: The amount of this TollInvoiceResult.
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this TollInvoiceResult.

        收费金额。 

        :param amount: The amount of this TollInvoiceResult.
        :type amount: str
        """
        self._amount = amount

    @property
    def cashier(self):
        """Gets the cashier of this TollInvoiceResult.

        收费员。 

        :return: The cashier of this TollInvoiceResult.
        :rtype: str
        """
        return self._cashier

    @cashier.setter
    def cashier(self, cashier):
        """Sets the cashier of this TollInvoiceResult.

        收费员。 

        :param cashier: The cashier of this TollInvoiceResult.
        :type cashier: str
        """
        self._cashier = cashier

    @property
    def vehicle_type(self):
        """Gets the vehicle_type of this TollInvoiceResult.

        车辆类型。 

        :return: The vehicle_type of this TollInvoiceResult.
        :rtype: str
        """
        return self._vehicle_type

    @vehicle_type.setter
    def vehicle_type(self, vehicle_type):
        """Sets the vehicle_type of this TollInvoiceResult.

        车辆类型。 

        :param vehicle_type: The vehicle_type of this TollInvoiceResult.
        :type vehicle_type: str
        """
        self._vehicle_type = vehicle_type

    @property
    def date(self):
        """Gets the date of this TollInvoiceResult.

        日期。 

        :return: The date of this TollInvoiceResult.
        :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this TollInvoiceResult.

        日期。 

        :param date: The date of this TollInvoiceResult.
        :type date: str
        """
        self._date = date

    @property
    def time(self):
        """Gets the time of this TollInvoiceResult.

        时间。 

        :return: The time of this TollInvoiceResult.
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this TollInvoiceResult.

        时间。 

        :param time: The time of this TollInvoiceResult.
        :type time: str
        """
        self._time = time

    @property
    def confidence(self):
        """Gets the confidence of this TollInvoiceResult.

        相关字段的置信度信息，置信度越大，表示本次识别的对应字段的可靠性越高，在统计意义上，置信度越大，准确率越高。 置信度由算法给出，不直接等价于对应字段的准确率。

        :return: The confidence of this TollInvoiceResult.
        :rtype: object
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        """Sets the confidence of this TollInvoiceResult.

        相关字段的置信度信息，置信度越大，表示本次识别的对应字段的可靠性越高，在统计意义上，置信度越大，准确率越高。 置信度由算法给出，不直接等价于对应字段的准确率。

        :param confidence: The confidence of this TollInvoiceResult.
        :type confidence: object
        """
        self._confidence = confidence

    @property
    def text_location(self):
        """Gets the text_location of this TollInvoiceResult.

        对应所有在原图上识别到的字段位置信息，包含所有文字区域四个顶点的二维坐标（x,y）。采用图像坐标系，坐标原点为图片左上角，x轴沿水平方向，y轴沿竖直方向。 

        :return: The text_location of this TollInvoiceResult.
        :rtype: object
        """
        return self._text_location

    @text_location.setter
    def text_location(self, text_location):
        """Sets the text_location of this TollInvoiceResult.

        对应所有在原图上识别到的字段位置信息，包含所有文字区域四个顶点的二维坐标（x,y）。采用图像坐标系，坐标原点为图片左上角，x轴沿水平方向，y轴沿竖直方向。 

        :param text_location: The text_location of this TollInvoiceResult.
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
        if not isinstance(other, TollInvoiceResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
