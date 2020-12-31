# coding: utf-8

import pprint
import re

import six





class TollInvoiceResultBody:


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
        'confidence': 'object'
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
        'confidence': 'confidence'
    }

    def __init__(self, code=None, number=None, entry=None, exit=None, amount=None, cashier=None, vehicle_type=None, date=None, time=None, confidence=None):
        """TollInvoiceResultBody - a model defined in huaweicloud sdk"""
        
        

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

    @property
    def code(self):
        """Gets the code of this TollInvoiceResultBody.

        发票代码。 

        :return: The code of this TollInvoiceResultBody.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this TollInvoiceResultBody.

        发票代码。 

        :param code: The code of this TollInvoiceResultBody.
        :type: str
        """
        self._code = code

    @property
    def number(self):
        """Gets the number of this TollInvoiceResultBody.

        发票号码。 

        :return: The number of this TollInvoiceResultBody.
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this TollInvoiceResultBody.

        发票号码。 

        :param number: The number of this TollInvoiceResultBody.
        :type: str
        """
        self._number = number

    @property
    def entry(self):
        """Gets the entry of this TollInvoiceResultBody.

        入口。 

        :return: The entry of this TollInvoiceResultBody.
        :rtype: str
        """
        return self._entry

    @entry.setter
    def entry(self, entry):
        """Sets the entry of this TollInvoiceResultBody.

        入口。 

        :param entry: The entry of this TollInvoiceResultBody.
        :type: str
        """
        self._entry = entry

    @property
    def exit(self):
        """Gets the exit of this TollInvoiceResultBody.

        出口。 

        :return: The exit of this TollInvoiceResultBody.
        :rtype: str
        """
        return self._exit

    @exit.setter
    def exit(self, exit):
        """Sets the exit of this TollInvoiceResultBody.

        出口。 

        :param exit: The exit of this TollInvoiceResultBody.
        :type: str
        """
        self._exit = exit

    @property
    def amount(self):
        """Gets the amount of this TollInvoiceResultBody.

        收费金额。 

        :return: The amount of this TollInvoiceResultBody.
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this TollInvoiceResultBody.

        收费金额。 

        :param amount: The amount of this TollInvoiceResultBody.
        :type: str
        """
        self._amount = amount

    @property
    def cashier(self):
        """Gets the cashier of this TollInvoiceResultBody.

        收费员。 

        :return: The cashier of this TollInvoiceResultBody.
        :rtype: str
        """
        return self._cashier

    @cashier.setter
    def cashier(self, cashier):
        """Sets the cashier of this TollInvoiceResultBody.

        收费员。 

        :param cashier: The cashier of this TollInvoiceResultBody.
        :type: str
        """
        self._cashier = cashier

    @property
    def vehicle_type(self):
        """Gets the vehicle_type of this TollInvoiceResultBody.

        车辆类型。 

        :return: The vehicle_type of this TollInvoiceResultBody.
        :rtype: str
        """
        return self._vehicle_type

    @vehicle_type.setter
    def vehicle_type(self, vehicle_type):
        """Sets the vehicle_type of this TollInvoiceResultBody.

        车辆类型。 

        :param vehicle_type: The vehicle_type of this TollInvoiceResultBody.
        :type: str
        """
        self._vehicle_type = vehicle_type

    @property
    def date(self):
        """Gets the date of this TollInvoiceResultBody.

        日期。 

        :return: The date of this TollInvoiceResultBody.
        :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this TollInvoiceResultBody.

        日期。 

        :param date: The date of this TollInvoiceResultBody.
        :type: str
        """
        self._date = date

    @property
    def time(self):
        """Gets the time of this TollInvoiceResultBody.

        时间。 

        :return: The time of this TollInvoiceResultBody.
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this TollInvoiceResultBody.

        时间。 

        :param time: The time of this TollInvoiceResultBody.
        :type: str
        """
        self._time = time

    @property
    def confidence(self):
        """Gets the confidence of this TollInvoiceResultBody.

        相关字段的置信度信息，置信度越大，表示本次识别的对应字段的可靠性越高，在统计意义上，置信度越大，准确率越高。 置信度由算法给出，不直接等价于对应字段的准确率。

        :return: The confidence of this TollInvoiceResultBody.
        :rtype: object
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        """Sets the confidence of this TollInvoiceResultBody.

        相关字段的置信度信息，置信度越大，表示本次识别的对应字段的可靠性越高，在统计意义上，置信度越大，准确率越高。 置信度由算法给出，不直接等价于对应字段的准确率。

        :param confidence: The confidence of this TollInvoiceResultBody.
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
        if not isinstance(other, TollInvoiceResultBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
