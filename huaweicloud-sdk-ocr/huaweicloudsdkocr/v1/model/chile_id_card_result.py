# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChileIdCardResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'surname': 'list[str]',
        'given_name': 'str',
        'nationality': 'str',
        'sex': 'str',
        'birth': 'str',
        'issue_date': 'str',
        'expiry_date': 'str',
        'document_number': 'str',
        'number': 'str',
        'confidence': 'ChileIdCardConfidence'
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
        'number': 'number',
        'confidence': 'confidence'
    }

    def __init__(self, surname=None, given_name=None, nationality=None, sex=None, birth=None, issue_date=None, expiry_date=None, document_number=None, number=None, confidence=None):
        r"""ChileIdCardResult

        The model defined in huaweicloud sdk

        :param surname: 姓氏。 
        :type surname: list[str]
        :param given_name: 名。 
        :type given_name: str
        :param nationality: 国籍。 
        :type nationality: str
        :param sex: 性别。 
        :type sex: str
        :param birth: 出生日。 
        :type birth: str
        :param issue_date: 发行日。 
        :type issue_date: str
        :param expiry_date: 有效期。 
        :type expiry_date: str
        :param document_number: 文档编号。 
        :type document_number: str
        :param number: 身份证号。 
        :type number: str
        :param confidence: 
        :type confidence: :class:`huaweicloudsdkocr.v1.ChileIdCardConfidence`
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
        self._confidence = None
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
        if confidence is not None:
            self.confidence = confidence

    @property
    def surname(self):
        r"""Gets the surname of this ChileIdCardResult.

        姓氏。 

        :return: The surname of this ChileIdCardResult.
        :rtype: list[str]
        """
        return self._surname

    @surname.setter
    def surname(self, surname):
        r"""Sets the surname of this ChileIdCardResult.

        姓氏。 

        :param surname: The surname of this ChileIdCardResult.
        :type surname: list[str]
        """
        self._surname = surname

    @property
    def given_name(self):
        r"""Gets the given_name of this ChileIdCardResult.

        名。 

        :return: The given_name of this ChileIdCardResult.
        :rtype: str
        """
        return self._given_name

    @given_name.setter
    def given_name(self, given_name):
        r"""Sets the given_name of this ChileIdCardResult.

        名。 

        :param given_name: The given_name of this ChileIdCardResult.
        :type given_name: str
        """
        self._given_name = given_name

    @property
    def nationality(self):
        r"""Gets the nationality of this ChileIdCardResult.

        国籍。 

        :return: The nationality of this ChileIdCardResult.
        :rtype: str
        """
        return self._nationality

    @nationality.setter
    def nationality(self, nationality):
        r"""Sets the nationality of this ChileIdCardResult.

        国籍。 

        :param nationality: The nationality of this ChileIdCardResult.
        :type nationality: str
        """
        self._nationality = nationality

    @property
    def sex(self):
        r"""Gets the sex of this ChileIdCardResult.

        性别。 

        :return: The sex of this ChileIdCardResult.
        :rtype: str
        """
        return self._sex

    @sex.setter
    def sex(self, sex):
        r"""Sets the sex of this ChileIdCardResult.

        性别。 

        :param sex: The sex of this ChileIdCardResult.
        :type sex: str
        """
        self._sex = sex

    @property
    def birth(self):
        r"""Gets the birth of this ChileIdCardResult.

        出生日。 

        :return: The birth of this ChileIdCardResult.
        :rtype: str
        """
        return self._birth

    @birth.setter
    def birth(self, birth):
        r"""Sets the birth of this ChileIdCardResult.

        出生日。 

        :param birth: The birth of this ChileIdCardResult.
        :type birth: str
        """
        self._birth = birth

    @property
    def issue_date(self):
        r"""Gets the issue_date of this ChileIdCardResult.

        发行日。 

        :return: The issue_date of this ChileIdCardResult.
        :rtype: str
        """
        return self._issue_date

    @issue_date.setter
    def issue_date(self, issue_date):
        r"""Sets the issue_date of this ChileIdCardResult.

        发行日。 

        :param issue_date: The issue_date of this ChileIdCardResult.
        :type issue_date: str
        """
        self._issue_date = issue_date

    @property
    def expiry_date(self):
        r"""Gets the expiry_date of this ChileIdCardResult.

        有效期。 

        :return: The expiry_date of this ChileIdCardResult.
        :rtype: str
        """
        return self._expiry_date

    @expiry_date.setter
    def expiry_date(self, expiry_date):
        r"""Sets the expiry_date of this ChileIdCardResult.

        有效期。 

        :param expiry_date: The expiry_date of this ChileIdCardResult.
        :type expiry_date: str
        """
        self._expiry_date = expiry_date

    @property
    def document_number(self):
        r"""Gets the document_number of this ChileIdCardResult.

        文档编号。 

        :return: The document_number of this ChileIdCardResult.
        :rtype: str
        """
        return self._document_number

    @document_number.setter
    def document_number(self, document_number):
        r"""Sets the document_number of this ChileIdCardResult.

        文档编号。 

        :param document_number: The document_number of this ChileIdCardResult.
        :type document_number: str
        """
        self._document_number = document_number

    @property
    def number(self):
        r"""Gets the number of this ChileIdCardResult.

        身份证号。 

        :return: The number of this ChileIdCardResult.
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        r"""Sets the number of this ChileIdCardResult.

        身份证号。 

        :param number: The number of this ChileIdCardResult.
        :type number: str
        """
        self._number = number

    @property
    def confidence(self):
        r"""Gets the confidence of this ChileIdCardResult.

        :return: The confidence of this ChileIdCardResult.
        :rtype: :class:`huaweicloudsdkocr.v1.ChileIdCardConfidence`
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        r"""Sets the confidence of this ChileIdCardResult.

        :param confidence: The confidence of this ChileIdCardResult.
        :type confidence: :class:`huaweicloudsdkocr.v1.ChileIdCardConfidence`
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
        if not isinstance(other, ChileIdCardResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
