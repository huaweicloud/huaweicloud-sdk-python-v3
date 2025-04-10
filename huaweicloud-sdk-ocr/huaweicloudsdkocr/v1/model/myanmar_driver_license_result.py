# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MyanmarDriverLicenseResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'card_number': 'str',
        'card_number_en': 'str',
        'name': 'str',
        'name_en': 'str',
        'nrc_id': 'str',
        'nrc_id_en': 'str',
        'birth': 'str',
        'birth_en': 'str',
        'blood_group': 'str',
        'blood_group_en': 'str',
        'expiried_date': 'str',
        'expiried_date_en': 'str',
        'confidence': 'MyanmarDriverLicenseConfidence'
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
        'expiried_date_en': 'expiried_date_en',
        'confidence': 'confidence'
    }

    def __init__(self, card_number=None, card_number_en=None, name=None, name_en=None, nrc_id=None, nrc_id_en=None, birth=None, birth_en=None, blood_group=None, blood_group_en=None, expiried_date=None, expiried_date_en=None, confidence=None):
        r"""MyanmarDriverLicenseResult

        The model defined in huaweicloud sdk

        :param card_number: 缅文驾驶证号。 
        :type card_number: str
        :param card_number_en: 英文驾驶证号。 
        :type card_number_en: str
        :param name: 缅文名字。 
        :type name: str
        :param name_en: 英文名字。 
        :type name_en: str
        :param nrc_id: 缅文nrc号码。 
        :type nrc_id: str
        :param nrc_id_en: 英文nrc号码。 
        :type nrc_id_en: str
        :param birth: 缅文出生日期。 
        :type birth: str
        :param birth_en: 英文出生日期。 
        :type birth_en: str
        :param blood_group: 缅文血型。 
        :type blood_group: str
        :param blood_group_en: 英文血型。 
        :type blood_group_en: str
        :param expiried_date: 缅文有效期。 
        :type expiried_date: str
        :param expiried_date_en: 英文有效期。 
        :type expiried_date_en: str
        :param confidence: 
        :type confidence: :class:`huaweicloudsdkocr.v1.MyanmarDriverLicenseConfidence`
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
        self._confidence = None
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
        if confidence is not None:
            self.confidence = confidence

    @property
    def card_number(self):
        r"""Gets the card_number of this MyanmarDriverLicenseResult.

        缅文驾驶证号。 

        :return: The card_number of this MyanmarDriverLicenseResult.
        :rtype: str
        """
        return self._card_number

    @card_number.setter
    def card_number(self, card_number):
        r"""Sets the card_number of this MyanmarDriverLicenseResult.

        缅文驾驶证号。 

        :param card_number: The card_number of this MyanmarDriverLicenseResult.
        :type card_number: str
        """
        self._card_number = card_number

    @property
    def card_number_en(self):
        r"""Gets the card_number_en of this MyanmarDriverLicenseResult.

        英文驾驶证号。 

        :return: The card_number_en of this MyanmarDriverLicenseResult.
        :rtype: str
        """
        return self._card_number_en

    @card_number_en.setter
    def card_number_en(self, card_number_en):
        r"""Sets the card_number_en of this MyanmarDriverLicenseResult.

        英文驾驶证号。 

        :param card_number_en: The card_number_en of this MyanmarDriverLicenseResult.
        :type card_number_en: str
        """
        self._card_number_en = card_number_en

    @property
    def name(self):
        r"""Gets the name of this MyanmarDriverLicenseResult.

        缅文名字。 

        :return: The name of this MyanmarDriverLicenseResult.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this MyanmarDriverLicenseResult.

        缅文名字。 

        :param name: The name of this MyanmarDriverLicenseResult.
        :type name: str
        """
        self._name = name

    @property
    def name_en(self):
        r"""Gets the name_en of this MyanmarDriverLicenseResult.

        英文名字。 

        :return: The name_en of this MyanmarDriverLicenseResult.
        :rtype: str
        """
        return self._name_en

    @name_en.setter
    def name_en(self, name_en):
        r"""Sets the name_en of this MyanmarDriverLicenseResult.

        英文名字。 

        :param name_en: The name_en of this MyanmarDriverLicenseResult.
        :type name_en: str
        """
        self._name_en = name_en

    @property
    def nrc_id(self):
        r"""Gets the nrc_id of this MyanmarDriverLicenseResult.

        缅文nrc号码。 

        :return: The nrc_id of this MyanmarDriverLicenseResult.
        :rtype: str
        """
        return self._nrc_id

    @nrc_id.setter
    def nrc_id(self, nrc_id):
        r"""Sets the nrc_id of this MyanmarDriverLicenseResult.

        缅文nrc号码。 

        :param nrc_id: The nrc_id of this MyanmarDriverLicenseResult.
        :type nrc_id: str
        """
        self._nrc_id = nrc_id

    @property
    def nrc_id_en(self):
        r"""Gets the nrc_id_en of this MyanmarDriverLicenseResult.

        英文nrc号码。 

        :return: The nrc_id_en of this MyanmarDriverLicenseResult.
        :rtype: str
        """
        return self._nrc_id_en

    @nrc_id_en.setter
    def nrc_id_en(self, nrc_id_en):
        r"""Sets the nrc_id_en of this MyanmarDriverLicenseResult.

        英文nrc号码。 

        :param nrc_id_en: The nrc_id_en of this MyanmarDriverLicenseResult.
        :type nrc_id_en: str
        """
        self._nrc_id_en = nrc_id_en

    @property
    def birth(self):
        r"""Gets the birth of this MyanmarDriverLicenseResult.

        缅文出生日期。 

        :return: The birth of this MyanmarDriverLicenseResult.
        :rtype: str
        """
        return self._birth

    @birth.setter
    def birth(self, birth):
        r"""Sets the birth of this MyanmarDriverLicenseResult.

        缅文出生日期。 

        :param birth: The birth of this MyanmarDriverLicenseResult.
        :type birth: str
        """
        self._birth = birth

    @property
    def birth_en(self):
        r"""Gets the birth_en of this MyanmarDriverLicenseResult.

        英文出生日期。 

        :return: The birth_en of this MyanmarDriverLicenseResult.
        :rtype: str
        """
        return self._birth_en

    @birth_en.setter
    def birth_en(self, birth_en):
        r"""Sets the birth_en of this MyanmarDriverLicenseResult.

        英文出生日期。 

        :param birth_en: The birth_en of this MyanmarDriverLicenseResult.
        :type birth_en: str
        """
        self._birth_en = birth_en

    @property
    def blood_group(self):
        r"""Gets the blood_group of this MyanmarDriverLicenseResult.

        缅文血型。 

        :return: The blood_group of this MyanmarDriverLicenseResult.
        :rtype: str
        """
        return self._blood_group

    @blood_group.setter
    def blood_group(self, blood_group):
        r"""Sets the blood_group of this MyanmarDriverLicenseResult.

        缅文血型。 

        :param blood_group: The blood_group of this MyanmarDriverLicenseResult.
        :type blood_group: str
        """
        self._blood_group = blood_group

    @property
    def blood_group_en(self):
        r"""Gets the blood_group_en of this MyanmarDriverLicenseResult.

        英文血型。 

        :return: The blood_group_en of this MyanmarDriverLicenseResult.
        :rtype: str
        """
        return self._blood_group_en

    @blood_group_en.setter
    def blood_group_en(self, blood_group_en):
        r"""Sets the blood_group_en of this MyanmarDriverLicenseResult.

        英文血型。 

        :param blood_group_en: The blood_group_en of this MyanmarDriverLicenseResult.
        :type blood_group_en: str
        """
        self._blood_group_en = blood_group_en

    @property
    def expiried_date(self):
        r"""Gets the expiried_date of this MyanmarDriverLicenseResult.

        缅文有效期。 

        :return: The expiried_date of this MyanmarDriverLicenseResult.
        :rtype: str
        """
        return self._expiried_date

    @expiried_date.setter
    def expiried_date(self, expiried_date):
        r"""Sets the expiried_date of this MyanmarDriverLicenseResult.

        缅文有效期。 

        :param expiried_date: The expiried_date of this MyanmarDriverLicenseResult.
        :type expiried_date: str
        """
        self._expiried_date = expiried_date

    @property
    def expiried_date_en(self):
        r"""Gets the expiried_date_en of this MyanmarDriverLicenseResult.

        英文有效期。 

        :return: The expiried_date_en of this MyanmarDriverLicenseResult.
        :rtype: str
        """
        return self._expiried_date_en

    @expiried_date_en.setter
    def expiried_date_en(self, expiried_date_en):
        r"""Sets the expiried_date_en of this MyanmarDriverLicenseResult.

        英文有效期。 

        :param expiried_date_en: The expiried_date_en of this MyanmarDriverLicenseResult.
        :type expiried_date_en: str
        """
        self._expiried_date_en = expiried_date_en

    @property
    def confidence(self):
        r"""Gets the confidence of this MyanmarDriverLicenseResult.

        :return: The confidence of this MyanmarDriverLicenseResult.
        :rtype: :class:`huaweicloudsdkocr.v1.MyanmarDriverLicenseConfidence`
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        r"""Sets the confidence of this MyanmarDriverLicenseResult.

        :param confidence: The confidence of this MyanmarDriverLicenseResult.
        :type confidence: :class:`huaweicloudsdkocr.v1.MyanmarDriverLicenseConfidence`
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
        if not isinstance(other, MyanmarDriverLicenseResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
