# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ThailandIdcardConfidence:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id_number': 'float',
        'name_th': 'float',
        'name_en': 'float',
        'ref_number': 'float',
        'first_name_en': 'float',
        'last_name_en': 'float',
        'date_of_birth_th': 'float',
        'date_of_birth_en': 'float',
        'religion_th': 'float',
        'address_th': 'float',
        'date_of_issue_th': 'float',
        'date_of_issue_en': 'float',
        'date_of_expiry_th': 'float',
        'date_of_expiry_en': 'float',
        'serial_number': 'float',
        'card_number': 'float',
        'laser_number': 'float'
    }

    attribute_map = {
        'id_number': 'id_number',
        'name_th': 'name_th',
        'name_en': 'name_en',
        'ref_number': 'ref_number',
        'first_name_en': 'first_name_en',
        'last_name_en': 'last_name_en',
        'date_of_birth_th': 'date_of_birth_th',
        'date_of_birth_en': 'date_of_birth_en',
        'religion_th': 'religion_th',
        'address_th': 'address_th',
        'date_of_issue_th': 'date_of_issue_th',
        'date_of_issue_en': 'date_of_issue_en',
        'date_of_expiry_th': 'date_of_expiry_th',
        'date_of_expiry_en': 'date_of_expiry_en',
        'serial_number': 'serial_number',
        'card_number': 'card_number',
        'laser_number': 'laser_number'
    }

    def __init__(self, id_number=None, name_th=None, name_en=None, ref_number=None, first_name_en=None, last_name_en=None, date_of_birth_th=None, date_of_birth_en=None, religion_th=None, address_th=None, date_of_issue_th=None, date_of_issue_en=None, date_of_expiry_th=None, date_of_expiry_en=None, serial_number=None, card_number=None, laser_number=None):
        """ThailandIdcardConfidence

        The model defined in huaweicloud sdk

        :param id_number: 身份证号置信度。 
        :type id_number: float
        :param name_th: 泰文名字置信度。 
        :type name_th: float
        :param name_en: 英文名置信度。 
        :type name_en: float
        :param ref_number: 参考编码置信度。 
        :type ref_number: float
        :param first_name_en: 英文名字置信度。 
        :type first_name_en: float
        :param last_name_en: 英文姓氏置信度。 
        :type last_name_en: float
        :param date_of_birth_th: 泰文出生日期置信度。 
        :type date_of_birth_th: float
        :param date_of_birth_en: 英文出生日期置信度。 
        :type date_of_birth_en: float
        :param religion_th: 宗教置信度。 
        :type religion_th: float
        :param address_th: 地址置信度。 
        :type address_th: float
        :param date_of_issue_th: 泰文签发日期置信度。 
        :type date_of_issue_th: float
        :param date_of_issue_en: 英文签发日期置信度。 
        :type date_of_issue_en: float
        :param date_of_expiry_th: 泰文有效期置信度。 
        :type date_of_expiry_th: float
        :param date_of_expiry_en: 英文有效期置信度。 
        :type date_of_expiry_en: float
        :param serial_number: 序列号置信度。 
        :type serial_number: float
        :param card_number: 身份证反面卡号置信度。 
        :type card_number: float
        :param laser_number: 激光码置信度。 
        :type laser_number: float
        """
        
        

        self._id_number = None
        self._name_th = None
        self._name_en = None
        self._ref_number = None
        self._first_name_en = None
        self._last_name_en = None
        self._date_of_birth_th = None
        self._date_of_birth_en = None
        self._religion_th = None
        self._address_th = None
        self._date_of_issue_th = None
        self._date_of_issue_en = None
        self._date_of_expiry_th = None
        self._date_of_expiry_en = None
        self._serial_number = None
        self._card_number = None
        self._laser_number = None
        self.discriminator = None

        if id_number is not None:
            self.id_number = id_number
        if name_th is not None:
            self.name_th = name_th
        if name_en is not None:
            self.name_en = name_en
        if ref_number is not None:
            self.ref_number = ref_number
        if first_name_en is not None:
            self.first_name_en = first_name_en
        if last_name_en is not None:
            self.last_name_en = last_name_en
        if date_of_birth_th is not None:
            self.date_of_birth_th = date_of_birth_th
        if date_of_birth_en is not None:
            self.date_of_birth_en = date_of_birth_en
        if religion_th is not None:
            self.religion_th = religion_th
        if address_th is not None:
            self.address_th = address_th
        if date_of_issue_th is not None:
            self.date_of_issue_th = date_of_issue_th
        if date_of_issue_en is not None:
            self.date_of_issue_en = date_of_issue_en
        if date_of_expiry_th is not None:
            self.date_of_expiry_th = date_of_expiry_th
        if date_of_expiry_en is not None:
            self.date_of_expiry_en = date_of_expiry_en
        if serial_number is not None:
            self.serial_number = serial_number
        if card_number is not None:
            self.card_number = card_number
        if laser_number is not None:
            self.laser_number = laser_number

    @property
    def id_number(self):
        """Gets the id_number of this ThailandIdcardConfidence.

        身份证号置信度。 

        :return: The id_number of this ThailandIdcardConfidence.
        :rtype: float
        """
        return self._id_number

    @id_number.setter
    def id_number(self, id_number):
        """Sets the id_number of this ThailandIdcardConfidence.

        身份证号置信度。 

        :param id_number: The id_number of this ThailandIdcardConfidence.
        :type id_number: float
        """
        self._id_number = id_number

    @property
    def name_th(self):
        """Gets the name_th of this ThailandIdcardConfidence.

        泰文名字置信度。 

        :return: The name_th of this ThailandIdcardConfidence.
        :rtype: float
        """
        return self._name_th

    @name_th.setter
    def name_th(self, name_th):
        """Sets the name_th of this ThailandIdcardConfidence.

        泰文名字置信度。 

        :param name_th: The name_th of this ThailandIdcardConfidence.
        :type name_th: float
        """
        self._name_th = name_th

    @property
    def name_en(self):
        """Gets the name_en of this ThailandIdcardConfidence.

        英文名置信度。 

        :return: The name_en of this ThailandIdcardConfidence.
        :rtype: float
        """
        return self._name_en

    @name_en.setter
    def name_en(self, name_en):
        """Sets the name_en of this ThailandIdcardConfidence.

        英文名置信度。 

        :param name_en: The name_en of this ThailandIdcardConfidence.
        :type name_en: float
        """
        self._name_en = name_en

    @property
    def ref_number(self):
        """Gets the ref_number of this ThailandIdcardConfidence.

        参考编码置信度。 

        :return: The ref_number of this ThailandIdcardConfidence.
        :rtype: float
        """
        return self._ref_number

    @ref_number.setter
    def ref_number(self, ref_number):
        """Sets the ref_number of this ThailandIdcardConfidence.

        参考编码置信度。 

        :param ref_number: The ref_number of this ThailandIdcardConfidence.
        :type ref_number: float
        """
        self._ref_number = ref_number

    @property
    def first_name_en(self):
        """Gets the first_name_en of this ThailandIdcardConfidence.

        英文名字置信度。 

        :return: The first_name_en of this ThailandIdcardConfidence.
        :rtype: float
        """
        return self._first_name_en

    @first_name_en.setter
    def first_name_en(self, first_name_en):
        """Sets the first_name_en of this ThailandIdcardConfidence.

        英文名字置信度。 

        :param first_name_en: The first_name_en of this ThailandIdcardConfidence.
        :type first_name_en: float
        """
        self._first_name_en = first_name_en

    @property
    def last_name_en(self):
        """Gets the last_name_en of this ThailandIdcardConfidence.

        英文姓氏置信度。 

        :return: The last_name_en of this ThailandIdcardConfidence.
        :rtype: float
        """
        return self._last_name_en

    @last_name_en.setter
    def last_name_en(self, last_name_en):
        """Sets the last_name_en of this ThailandIdcardConfidence.

        英文姓氏置信度。 

        :param last_name_en: The last_name_en of this ThailandIdcardConfidence.
        :type last_name_en: float
        """
        self._last_name_en = last_name_en

    @property
    def date_of_birth_th(self):
        """Gets the date_of_birth_th of this ThailandIdcardConfidence.

        泰文出生日期置信度。 

        :return: The date_of_birth_th of this ThailandIdcardConfidence.
        :rtype: float
        """
        return self._date_of_birth_th

    @date_of_birth_th.setter
    def date_of_birth_th(self, date_of_birth_th):
        """Sets the date_of_birth_th of this ThailandIdcardConfidence.

        泰文出生日期置信度。 

        :param date_of_birth_th: The date_of_birth_th of this ThailandIdcardConfidence.
        :type date_of_birth_th: float
        """
        self._date_of_birth_th = date_of_birth_th

    @property
    def date_of_birth_en(self):
        """Gets the date_of_birth_en of this ThailandIdcardConfidence.

        英文出生日期置信度。 

        :return: The date_of_birth_en of this ThailandIdcardConfidence.
        :rtype: float
        """
        return self._date_of_birth_en

    @date_of_birth_en.setter
    def date_of_birth_en(self, date_of_birth_en):
        """Sets the date_of_birth_en of this ThailandIdcardConfidence.

        英文出生日期置信度。 

        :param date_of_birth_en: The date_of_birth_en of this ThailandIdcardConfidence.
        :type date_of_birth_en: float
        """
        self._date_of_birth_en = date_of_birth_en

    @property
    def religion_th(self):
        """Gets the religion_th of this ThailandIdcardConfidence.

        宗教置信度。 

        :return: The religion_th of this ThailandIdcardConfidence.
        :rtype: float
        """
        return self._religion_th

    @religion_th.setter
    def religion_th(self, religion_th):
        """Sets the religion_th of this ThailandIdcardConfidence.

        宗教置信度。 

        :param religion_th: The religion_th of this ThailandIdcardConfidence.
        :type religion_th: float
        """
        self._religion_th = religion_th

    @property
    def address_th(self):
        """Gets the address_th of this ThailandIdcardConfidence.

        地址置信度。 

        :return: The address_th of this ThailandIdcardConfidence.
        :rtype: float
        """
        return self._address_th

    @address_th.setter
    def address_th(self, address_th):
        """Sets the address_th of this ThailandIdcardConfidence.

        地址置信度。 

        :param address_th: The address_th of this ThailandIdcardConfidence.
        :type address_th: float
        """
        self._address_th = address_th

    @property
    def date_of_issue_th(self):
        """Gets the date_of_issue_th of this ThailandIdcardConfidence.

        泰文签发日期置信度。 

        :return: The date_of_issue_th of this ThailandIdcardConfidence.
        :rtype: float
        """
        return self._date_of_issue_th

    @date_of_issue_th.setter
    def date_of_issue_th(self, date_of_issue_th):
        """Sets the date_of_issue_th of this ThailandIdcardConfidence.

        泰文签发日期置信度。 

        :param date_of_issue_th: The date_of_issue_th of this ThailandIdcardConfidence.
        :type date_of_issue_th: float
        """
        self._date_of_issue_th = date_of_issue_th

    @property
    def date_of_issue_en(self):
        """Gets the date_of_issue_en of this ThailandIdcardConfidence.

        英文签发日期置信度。 

        :return: The date_of_issue_en of this ThailandIdcardConfidence.
        :rtype: float
        """
        return self._date_of_issue_en

    @date_of_issue_en.setter
    def date_of_issue_en(self, date_of_issue_en):
        """Sets the date_of_issue_en of this ThailandIdcardConfidence.

        英文签发日期置信度。 

        :param date_of_issue_en: The date_of_issue_en of this ThailandIdcardConfidence.
        :type date_of_issue_en: float
        """
        self._date_of_issue_en = date_of_issue_en

    @property
    def date_of_expiry_th(self):
        """Gets the date_of_expiry_th of this ThailandIdcardConfidence.

        泰文有效期置信度。 

        :return: The date_of_expiry_th of this ThailandIdcardConfidence.
        :rtype: float
        """
        return self._date_of_expiry_th

    @date_of_expiry_th.setter
    def date_of_expiry_th(self, date_of_expiry_th):
        """Sets the date_of_expiry_th of this ThailandIdcardConfidence.

        泰文有效期置信度。 

        :param date_of_expiry_th: The date_of_expiry_th of this ThailandIdcardConfidence.
        :type date_of_expiry_th: float
        """
        self._date_of_expiry_th = date_of_expiry_th

    @property
    def date_of_expiry_en(self):
        """Gets the date_of_expiry_en of this ThailandIdcardConfidence.

        英文有效期置信度。 

        :return: The date_of_expiry_en of this ThailandIdcardConfidence.
        :rtype: float
        """
        return self._date_of_expiry_en

    @date_of_expiry_en.setter
    def date_of_expiry_en(self, date_of_expiry_en):
        """Sets the date_of_expiry_en of this ThailandIdcardConfidence.

        英文有效期置信度。 

        :param date_of_expiry_en: The date_of_expiry_en of this ThailandIdcardConfidence.
        :type date_of_expiry_en: float
        """
        self._date_of_expiry_en = date_of_expiry_en

    @property
    def serial_number(self):
        """Gets the serial_number of this ThailandIdcardConfidence.

        序列号置信度。 

        :return: The serial_number of this ThailandIdcardConfidence.
        :rtype: float
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        """Sets the serial_number of this ThailandIdcardConfidence.

        序列号置信度。 

        :param serial_number: The serial_number of this ThailandIdcardConfidence.
        :type serial_number: float
        """
        self._serial_number = serial_number

    @property
    def card_number(self):
        """Gets the card_number of this ThailandIdcardConfidence.

        身份证反面卡号置信度。 

        :return: The card_number of this ThailandIdcardConfidence.
        :rtype: float
        """
        return self._card_number

    @card_number.setter
    def card_number(self, card_number):
        """Sets the card_number of this ThailandIdcardConfidence.

        身份证反面卡号置信度。 

        :param card_number: The card_number of this ThailandIdcardConfidence.
        :type card_number: float
        """
        self._card_number = card_number

    @property
    def laser_number(self):
        """Gets the laser_number of this ThailandIdcardConfidence.

        激光码置信度。 

        :return: The laser_number of this ThailandIdcardConfidence.
        :rtype: float
        """
        return self._laser_number

    @laser_number.setter
    def laser_number(self, laser_number):
        """Sets the laser_number of this ThailandIdcardConfidence.

        激光码置信度。 

        :param laser_number: The laser_number of this ThailandIdcardConfidence.
        :type laser_number: float
        """
        self._laser_number = laser_number

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
        if not isinstance(other, ThailandIdcardConfidence):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
