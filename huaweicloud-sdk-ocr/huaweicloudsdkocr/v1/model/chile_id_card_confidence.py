# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChileIdCardConfidence:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'surname': 'float',
        'given_name': 'float',
        'nationality': 'float',
        'sex': 'float',
        'birth': 'float',
        'issue_date': 'float',
        'expiry_date': 'float',
        'document_number': 'float',
        'number': 'float'
    }

    attribute_map = {
        'surname': 'surname',
        'given_name': 'given_name',
        'nationality': 'nationality',
        'sex': 'sex',
        'birth': 'birth',
        'issue_date': 'issue_date',
        'expiry_date': 'expiry_date',
        'document_number': 'document_number',
        'number': 'number'
    }

    def __init__(self, surname=None, given_name=None, nationality=None, sex=None, birth=None, issue_date=None, expiry_date=None, document_number=None, number=None):
        """ChileIdCardConfidence

        The model defined in huaweicloud sdk

        :param surname: 姓氏置信度。 
        :type surname: float
        :param given_name: 名置信度。 
        :type given_name: float
        :param nationality: 国籍置信度。 
        :type nationality: float
        :param sex: 性别置信度。 
        :type sex: float
        :param birth: 出生日置信度。 
        :type birth: float
        :param issue_date: 发行日置信度。 
        :type issue_date: float
        :param expiry_date: 有效期置信度。 
        :type expiry_date: float
        :param document_number: 文档编号置信度。 
        :type document_number: float
        :param number: 身份证号置信度。 
        :type number: float
        """
        
        

        self._surname = None
        self._given_name = None
        self._nationality = None
        self._sex = None
        self._birth = None
        self._issue_date = None
        self._expiry_date = None
        self._document_number = None
        self._number = None
        self.discriminator = None

        if surname is not None:
            self.surname = surname
        if given_name is not None:
            self.given_name = given_name
        if nationality is not None:
            self.nationality = nationality
        if sex is not None:
            self.sex = sex
        if birth is not None:
            self.birth = birth
        if issue_date is not None:
            self.issue_date = issue_date
        if expiry_date is not None:
            self.expiry_date = expiry_date
        if document_number is not None:
            self.document_number = document_number
        if number is not None:
            self.number = number

    @property
    def surname(self):
        """Gets the surname of this ChileIdCardConfidence.

        姓氏置信度。 

        :return: The surname of this ChileIdCardConfidence.
        :rtype: float
        """
        return self._surname

    @surname.setter
    def surname(self, surname):
        """Sets the surname of this ChileIdCardConfidence.

        姓氏置信度。 

        :param surname: The surname of this ChileIdCardConfidence.
        :type surname: float
        """
        self._surname = surname

    @property
    def given_name(self):
        """Gets the given_name of this ChileIdCardConfidence.

        名置信度。 

        :return: The given_name of this ChileIdCardConfidence.
        :rtype: float
        """
        return self._given_name

    @given_name.setter
    def given_name(self, given_name):
        """Sets the given_name of this ChileIdCardConfidence.

        名置信度。 

        :param given_name: The given_name of this ChileIdCardConfidence.
        :type given_name: float
        """
        self._given_name = given_name

    @property
    def nationality(self):
        """Gets the nationality of this ChileIdCardConfidence.

        国籍置信度。 

        :return: The nationality of this ChileIdCardConfidence.
        :rtype: float
        """
        return self._nationality

    @nationality.setter
    def nationality(self, nationality):
        """Sets the nationality of this ChileIdCardConfidence.

        国籍置信度。 

        :param nationality: The nationality of this ChileIdCardConfidence.
        :type nationality: float
        """
        self._nationality = nationality

    @property
    def sex(self):
        """Gets the sex of this ChileIdCardConfidence.

        性别置信度。 

        :return: The sex of this ChileIdCardConfidence.
        :rtype: float
        """
        return self._sex

    @sex.setter
    def sex(self, sex):
        """Sets the sex of this ChileIdCardConfidence.

        性别置信度。 

        :param sex: The sex of this ChileIdCardConfidence.
        :type sex: float
        """
        self._sex = sex

    @property
    def birth(self):
        """Gets the birth of this ChileIdCardConfidence.

        出生日置信度。 

        :return: The birth of this ChileIdCardConfidence.
        :rtype: float
        """
        return self._birth

    @birth.setter
    def birth(self, birth):
        """Sets the birth of this ChileIdCardConfidence.

        出生日置信度。 

        :param birth: The birth of this ChileIdCardConfidence.
        :type birth: float
        """
        self._birth = birth

    @property
    def issue_date(self):
        """Gets the issue_date of this ChileIdCardConfidence.

        发行日置信度。 

        :return: The issue_date of this ChileIdCardConfidence.
        :rtype: float
        """
        return self._issue_date

    @issue_date.setter
    def issue_date(self, issue_date):
        """Sets the issue_date of this ChileIdCardConfidence.

        发行日置信度。 

        :param issue_date: The issue_date of this ChileIdCardConfidence.
        :type issue_date: float
        """
        self._issue_date = issue_date

    @property
    def expiry_date(self):
        """Gets the expiry_date of this ChileIdCardConfidence.

        有效期置信度。 

        :return: The expiry_date of this ChileIdCardConfidence.
        :rtype: float
        """
        return self._expiry_date

    @expiry_date.setter
    def expiry_date(self, expiry_date):
        """Sets the expiry_date of this ChileIdCardConfidence.

        有效期置信度。 

        :param expiry_date: The expiry_date of this ChileIdCardConfidence.
        :type expiry_date: float
        """
        self._expiry_date = expiry_date

    @property
    def document_number(self):
        """Gets the document_number of this ChileIdCardConfidence.

        文档编号置信度。 

        :return: The document_number of this ChileIdCardConfidence.
        :rtype: float
        """
        return self._document_number

    @document_number.setter
    def document_number(self, document_number):
        """Sets the document_number of this ChileIdCardConfidence.

        文档编号置信度。 

        :param document_number: The document_number of this ChileIdCardConfidence.
        :type document_number: float
        """
        self._document_number = document_number

    @property
    def number(self):
        """Gets the number of this ChileIdCardConfidence.

        身份证号置信度。 

        :return: The number of this ChileIdCardConfidence.
        :rtype: float
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this ChileIdCardConfidence.

        身份证号置信度。 

        :param number: The number of this ChileIdCardConfidence.
        :type number: float
        """
        self._number = number

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
        if not isinstance(other, ChileIdCardConfidence):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
