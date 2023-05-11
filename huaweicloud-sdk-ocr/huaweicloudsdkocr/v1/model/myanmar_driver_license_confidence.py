# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MyanmarDriverLicenseConfidence:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'card_number': 'float',
        'card_number_en': 'float',
        'name': 'float',
        'name_en': 'float',
        'nrc_id': 'float',
        'nrc_id_en': 'float',
        'birth': 'float',
        'birth_en': 'float',
        'blood_group': 'float',
        'blood_group_en': 'float',
        'expiried_date': 'float',
        'expiried_date_en': 'float'
    }

    attribute_map = {
        'card_number': 'card_number',
        'card_number_en': 'card_number_en',
        'name': 'name',
        'name_en': 'name_en',
        'nrc_id': 'nrc_id',
        'nrc_id_en': 'nrc_id_en',
        'birth': 'birth',
        'birth_en': 'birth_en',
        'blood_group': 'blood_group',
        'blood_group_en': 'blood_group_en',
        'expiried_date': 'expiried_date',
        'expiried_date_en': 'expiried_date_en'
    }

    def __init__(self, card_number=None, card_number_en=None, name=None, name_en=None, nrc_id=None, nrc_id_en=None, birth=None, birth_en=None, blood_group=None, blood_group_en=None, expiried_date=None, expiried_date_en=None):
        """MyanmarDriverLicenseConfidence

        The model defined in huaweicloud sdk

        :param card_number: 缅文驾驶证号置信度。 
        :type card_number: float
        :param card_number_en: 英文驾驶证号置信度。 
        :type card_number_en: float
        :param name: 缅文名字置信度。 
        :type name: float
        :param name_en: 英文名字置信度。 
        :type name_en: float
        :param nrc_id: 缅文nrc号码置信度。 
        :type nrc_id: float
        :param nrc_id_en: 英文nrc号码置信度。 
        :type nrc_id_en: float
        :param birth: 缅文出生日期置信度。 
        :type birth: float
        :param birth_en: 英文出生日期置信度。 
        :type birth_en: float
        :param blood_group: 缅文血型置信度。 
        :type blood_group: float
        :param blood_group_en: 英文血型置信度。 
        :type blood_group_en: float
        :param expiried_date: 缅文有效期置信度。 
        :type expiried_date: float
        :param expiried_date_en: 英文有效期置信度。 
        :type expiried_date_en: float
        """
        
        

        self._card_number = None
        self._card_number_en = None
        self._name = None
        self._name_en = None
        self._nrc_id = None
        self._nrc_id_en = None
        self._birth = None
        self._birth_en = None
        self._blood_group = None
        self._blood_group_en = None
        self._expiried_date = None
        self._expiried_date_en = None
        self.discriminator = None

        if card_number is not None:
            self.card_number = card_number
        if card_number_en is not None:
            self.card_number_en = card_number_en
        if name is not None:
            self.name = name
        if name_en is not None:
            self.name_en = name_en
        if nrc_id is not None:
            self.nrc_id = nrc_id
        if nrc_id_en is not None:
            self.nrc_id_en = nrc_id_en
        if birth is not None:
            self.birth = birth
        if birth_en is not None:
            self.birth_en = birth_en
        if blood_group is not None:
            self.blood_group = blood_group
        if blood_group_en is not None:
            self.blood_group_en = blood_group_en
        if expiried_date is not None:
            self.expiried_date = expiried_date
        if expiried_date_en is not None:
            self.expiried_date_en = expiried_date_en

    @property
    def card_number(self):
        """Gets the card_number of this MyanmarDriverLicenseConfidence.

        缅文驾驶证号置信度。 

        :return: The card_number of this MyanmarDriverLicenseConfidence.
        :rtype: float
        """
        return self._card_number

    @card_number.setter
    def card_number(self, card_number):
        """Sets the card_number of this MyanmarDriverLicenseConfidence.

        缅文驾驶证号置信度。 

        :param card_number: The card_number of this MyanmarDriverLicenseConfidence.
        :type card_number: float
        """
        self._card_number = card_number

    @property
    def card_number_en(self):
        """Gets the card_number_en of this MyanmarDriverLicenseConfidence.

        英文驾驶证号置信度。 

        :return: The card_number_en of this MyanmarDriverLicenseConfidence.
        :rtype: float
        """
        return self._card_number_en

    @card_number_en.setter
    def card_number_en(self, card_number_en):
        """Sets the card_number_en of this MyanmarDriverLicenseConfidence.

        英文驾驶证号置信度。 

        :param card_number_en: The card_number_en of this MyanmarDriverLicenseConfidence.
        :type card_number_en: float
        """
        self._card_number_en = card_number_en

    @property
    def name(self):
        """Gets the name of this MyanmarDriverLicenseConfidence.

        缅文名字置信度。 

        :return: The name of this MyanmarDriverLicenseConfidence.
        :rtype: float
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MyanmarDriverLicenseConfidence.

        缅文名字置信度。 

        :param name: The name of this MyanmarDriverLicenseConfidence.
        :type name: float
        """
        self._name = name

    @property
    def name_en(self):
        """Gets the name_en of this MyanmarDriverLicenseConfidence.

        英文名字置信度。 

        :return: The name_en of this MyanmarDriverLicenseConfidence.
        :rtype: float
        """
        return self._name_en

    @name_en.setter
    def name_en(self, name_en):
        """Sets the name_en of this MyanmarDriverLicenseConfidence.

        英文名字置信度。 

        :param name_en: The name_en of this MyanmarDriverLicenseConfidence.
        :type name_en: float
        """
        self._name_en = name_en

    @property
    def nrc_id(self):
        """Gets the nrc_id of this MyanmarDriverLicenseConfidence.

        缅文nrc号码置信度。 

        :return: The nrc_id of this MyanmarDriverLicenseConfidence.
        :rtype: float
        """
        return self._nrc_id

    @nrc_id.setter
    def nrc_id(self, nrc_id):
        """Sets the nrc_id of this MyanmarDriverLicenseConfidence.

        缅文nrc号码置信度。 

        :param nrc_id: The nrc_id of this MyanmarDriverLicenseConfidence.
        :type nrc_id: float
        """
        self._nrc_id = nrc_id

    @property
    def nrc_id_en(self):
        """Gets the nrc_id_en of this MyanmarDriverLicenseConfidence.

        英文nrc号码置信度。 

        :return: The nrc_id_en of this MyanmarDriverLicenseConfidence.
        :rtype: float
        """
        return self._nrc_id_en

    @nrc_id_en.setter
    def nrc_id_en(self, nrc_id_en):
        """Sets the nrc_id_en of this MyanmarDriverLicenseConfidence.

        英文nrc号码置信度。 

        :param nrc_id_en: The nrc_id_en of this MyanmarDriverLicenseConfidence.
        :type nrc_id_en: float
        """
        self._nrc_id_en = nrc_id_en

    @property
    def birth(self):
        """Gets the birth of this MyanmarDriverLicenseConfidence.

        缅文出生日期置信度。 

        :return: The birth of this MyanmarDriverLicenseConfidence.
        :rtype: float
        """
        return self._birth

    @birth.setter
    def birth(self, birth):
        """Sets the birth of this MyanmarDriverLicenseConfidence.

        缅文出生日期置信度。 

        :param birth: The birth of this MyanmarDriverLicenseConfidence.
        :type birth: float
        """
        self._birth = birth

    @property
    def birth_en(self):
        """Gets the birth_en of this MyanmarDriverLicenseConfidence.

        英文出生日期置信度。 

        :return: The birth_en of this MyanmarDriverLicenseConfidence.
        :rtype: float
        """
        return self._birth_en

    @birth_en.setter
    def birth_en(self, birth_en):
        """Sets the birth_en of this MyanmarDriverLicenseConfidence.

        英文出生日期置信度。 

        :param birth_en: The birth_en of this MyanmarDriverLicenseConfidence.
        :type birth_en: float
        """
        self._birth_en = birth_en

    @property
    def blood_group(self):
        """Gets the blood_group of this MyanmarDriverLicenseConfidence.

        缅文血型置信度。 

        :return: The blood_group of this MyanmarDriverLicenseConfidence.
        :rtype: float
        """
        return self._blood_group

    @blood_group.setter
    def blood_group(self, blood_group):
        """Sets the blood_group of this MyanmarDriverLicenseConfidence.

        缅文血型置信度。 

        :param blood_group: The blood_group of this MyanmarDriverLicenseConfidence.
        :type blood_group: float
        """
        self._blood_group = blood_group

    @property
    def blood_group_en(self):
        """Gets the blood_group_en of this MyanmarDriverLicenseConfidence.

        英文血型置信度。 

        :return: The blood_group_en of this MyanmarDriverLicenseConfidence.
        :rtype: float
        """
        return self._blood_group_en

    @blood_group_en.setter
    def blood_group_en(self, blood_group_en):
        """Sets the blood_group_en of this MyanmarDriverLicenseConfidence.

        英文血型置信度。 

        :param blood_group_en: The blood_group_en of this MyanmarDriverLicenseConfidence.
        :type blood_group_en: float
        """
        self._blood_group_en = blood_group_en

    @property
    def expiried_date(self):
        """Gets the expiried_date of this MyanmarDriverLicenseConfidence.

        缅文有效期置信度。 

        :return: The expiried_date of this MyanmarDriverLicenseConfidence.
        :rtype: float
        """
        return self._expiried_date

    @expiried_date.setter
    def expiried_date(self, expiried_date):
        """Sets the expiried_date of this MyanmarDriverLicenseConfidence.

        缅文有效期置信度。 

        :param expiried_date: The expiried_date of this MyanmarDriverLicenseConfidence.
        :type expiried_date: float
        """
        self._expiried_date = expiried_date

    @property
    def expiried_date_en(self):
        """Gets the expiried_date_en of this MyanmarDriverLicenseConfidence.

        英文有效期置信度。 

        :return: The expiried_date_en of this MyanmarDriverLicenseConfidence.
        :rtype: float
        """
        return self._expiried_date_en

    @expiried_date_en.setter
    def expiried_date_en(self, expiried_date_en):
        """Sets the expiried_date_en of this MyanmarDriverLicenseConfidence.

        英文有效期置信度。 

        :param expiried_date_en: The expiried_date_en of this MyanmarDriverLicenseConfidence.
        :type expiried_date_en: float
        """
        self._expiried_date_en = expiried_date_en

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
        if not isinstance(other, MyanmarDriverLicenseConfidence):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
