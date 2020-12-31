# coding: utf-8

import pprint
import re

import six





class QuotaInvoiceResultBody:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'number': 'str',
        'code': 'str',
        'location': 'str',
        'amount': 'str',
        'confidence': 'object'
    }

    attribute_map = {
        'number': 'number',
        'code': 'code',
        'location': 'location',
        'amount': 'amount',
        'confidence': 'confidence'
    }

    def __init__(self, number=None, code=None, location=None, amount=None, confidence=None):
        """QuotaInvoiceResultBody - a model defined in huaweicloud sdk"""
        
        

        self._number = None
        self._code = None
        self._location = None
        self._amount = None
        self._confidence = None
        self.discriminator = None

        if number is not None:
            self.number = number
        if code is not None:
            self.code = code
        if location is not None:
            self.location = location
        if amount is not None:
            self.amount = amount
        if confidence is not None:
            self.confidence = confidence

    @property
    def number(self):
        """Gets the number of this QuotaInvoiceResultBody.

        发票号码。 

        :return: The number of this QuotaInvoiceResultBody.
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this QuotaInvoiceResultBody.

        发票号码。 

        :param number: The number of this QuotaInvoiceResultBody.
        :type: str
        """
        self._number = number

    @property
    def code(self):
        """Gets the code of this QuotaInvoiceResultBody.

        发票代码。 

        :return: The code of this QuotaInvoiceResultBody.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this QuotaInvoiceResultBody.

        发票代码。 

        :param code: The code of this QuotaInvoiceResultBody.
        :type: str
        """
        self._code = code

    @property
    def location(self):
        """Gets the location of this QuotaInvoiceResultBody.

        地址。 

        :return: The location of this QuotaInvoiceResultBody.
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this QuotaInvoiceResultBody.

        地址。 

        :param location: The location of this QuotaInvoiceResultBody.
        :type: str
        """
        self._location = location

    @property
    def amount(self):
        """Gets the amount of this QuotaInvoiceResultBody.

        发票金额。 

        :return: The amount of this QuotaInvoiceResultBody.
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this QuotaInvoiceResultBody.

        发票金额。 

        :param amount: The amount of this QuotaInvoiceResultBody.
        :type: str
        """
        self._amount = amount

    @property
    def confidence(self):
        """Gets the confidence of this QuotaInvoiceResultBody.

        相关字段的置信度信息，置信度越大，表示本次识别的对应字段的可靠性越高，在统计意义上，置信度越大，准确率越高。 置信度由算法给出，不直接等价于对应字段的准确率。

        :return: The confidence of this QuotaInvoiceResultBody.
        :rtype: object
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        """Sets the confidence of this QuotaInvoiceResultBody.

        相关字段的置信度信息，置信度越大，表示本次识别的对应字段的可靠性越高，在统计意义上，置信度越大，准确率越高。 置信度由算法给出，不直接等价于对应字段的准确率。

        :param confidence: The confidence of this QuotaInvoiceResultBody.
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
        if not isinstance(other, QuotaInvoiceResultBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
