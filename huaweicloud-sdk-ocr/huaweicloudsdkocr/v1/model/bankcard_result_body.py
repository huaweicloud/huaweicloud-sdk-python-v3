# coding: utf-8

import pprint
import re

import six





class BankcardResultBody:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'bank_name': 'str',
        'card_number': 'str',
        'issue_date': 'str',
        'expiry_date': 'str',
        'type': 'str',
        'confidence': 'object'
    }

    attribute_map = {
        'bank_name': 'bank_name',
        'card_number': 'card_number',
        'issue_date': 'issue_date',
        'expiry_date': 'expiry_date',
        'type': 'type',
        'confidence': 'confidence'
    }

    def __init__(self, bank_name=None, card_number=None, issue_date=None, expiry_date=None, type=None, confidence=None):
        """BankcardResultBody - a model defined in huaweicloud sdk"""
        
        

        self._bank_name = None
        self._card_number = None
        self._issue_date = None
        self._expiry_date = None
        self._type = None
        self._confidence = None
        self.discriminator = None

        if bank_name is not None:
            self.bank_name = bank_name
        if card_number is not None:
            self.card_number = card_number
        if issue_date is not None:
            self.issue_date = issue_date
        if expiry_date is not None:
            self.expiry_date = expiry_date
        if type is not None:
            self.type = type
        if confidence is not None:
            self.confidence = confidence

    @property
    def bank_name(self):
        """Gets the bank_name of this BankcardResultBody.

        发卡行。 

        :return: The bank_name of this BankcardResultBody.
        :rtype: str
        """
        return self._bank_name

    @bank_name.setter
    def bank_name(self, bank_name):
        """Sets the bank_name of this BankcardResultBody.

        发卡行。 

        :param bank_name: The bank_name of this BankcardResultBody.
        :type: str
        """
        self._bank_name = bank_name

    @property
    def card_number(self):
        """Gets the card_number of this BankcardResultBody.

        银行卡号。 

        :return: The card_number of this BankcardResultBody.
        :rtype: str
        """
        return self._card_number

    @card_number.setter
    def card_number(self, card_number):
        """Sets the card_number of this BankcardResultBody.

        银行卡号。 

        :param card_number: The card_number of this BankcardResultBody.
        :type: str
        """
        self._card_number = card_number

    @property
    def issue_date(self):
        """Gets the issue_date of this BankcardResultBody.

        有效期开始日期。 

        :return: The issue_date of this BankcardResultBody.
        :rtype: str
        """
        return self._issue_date

    @issue_date.setter
    def issue_date(self, issue_date):
        """Sets the issue_date of this BankcardResultBody.

        有效期开始日期。 

        :param issue_date: The issue_date of this BankcardResultBody.
        :type: str
        """
        self._issue_date = issue_date

    @property
    def expiry_date(self):
        """Gets the expiry_date of this BankcardResultBody.

        有效期截止日期。 

        :return: The expiry_date of this BankcardResultBody.
        :rtype: str
        """
        return self._expiry_date

    @expiry_date.setter
    def expiry_date(self, expiry_date):
        """Sets the expiry_date of this BankcardResultBody.

        有效期截止日期。 

        :param expiry_date: The expiry_date of this BankcardResultBody.
        :type: str
        """
        self._expiry_date = expiry_date

    @property
    def type(self):
        """Gets the type of this BankcardResultBody.

        银行卡类别，如：储蓄卡，信用卡。 

        :return: The type of this BankcardResultBody.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this BankcardResultBody.

        银行卡类别，如：储蓄卡，信用卡。 

        :param type: The type of this BankcardResultBody.
        :type: str
        """
        self._type = type

    @property
    def confidence(self):
        """Gets the confidence of this BankcardResultBody.

        相关字段的置信度信息，置信度越大，表示本次识别的对应字段的可靠性越高，在统计意义上，置信度越大，准确率越高。 置信度由算法给出，不直接等价于对应字段的准确率。 

        :return: The confidence of this BankcardResultBody.
        :rtype: object
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        """Sets the confidence of this BankcardResultBody.

        相关字段的置信度信息，置信度越大，表示本次识别的对应字段的可靠性越高，在统计意义上，置信度越大，准确率越高。 置信度由算法给出，不直接等价于对应字段的准确率。 

        :param confidence: The confidence of this BankcardResultBody.
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
        if not isinstance(other, BankcardResultBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
