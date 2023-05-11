# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BusinessLicenseResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'registration_number': 'str',
        'name': 'str',
        'type': 'str',
        'address': 'str',
        'legal_representative': 'str',
        'registered_capital': 'str',
        'found_date': 'str',
        'business_term': 'str',
        'business_scope': 'str',
        'issue_date': 'str',
        'confidence': 'object'
    }

    attribute_map = {
        'registration_number': 'registration_number',
        'name': 'name',
        'type': 'type',
        'address': 'address',
        'legal_representative': 'legal_representative',
        'registered_capital': 'registered_capital',
        'found_date': 'found_date',
        'business_term': 'business_term',
        'business_scope': 'business_scope',
        'issue_date': 'issue_date',
        'confidence': 'confidence'
    }

    def __init__(self, registration_number=None, name=None, type=None, address=None, legal_representative=None, registered_capital=None, found_date=None, business_term=None, business_scope=None, issue_date=None, confidence=None):
        """BusinessLicenseResult

        The model defined in huaweicloud sdk

        :param registration_number:   - 老版本营业执照对应注册号。  - 新三证合一版本营业执照对应社会保障号。 
        :type registration_number: str
        :param name: 企业名称。 
        :type name: str
        :param type: 公司/企业类型/主体类型。 
        :type type: str
        :param address: 住所/营业场所/企业住所。 
        :type address: str
        :param legal_representative: 法定代表人/负责人。 
        :type legal_representative: str
        :param registered_capital: 注册资本。 
        :type registered_capital: str
        :param found_date: 成立日期。 
        :type found_date: str
        :param business_term: 营业期限。 
        :type business_term: str
        :param business_scope: 经营范围。 
        :type business_scope: str
        :param issue_date: 发照日期。 
        :type issue_date: str
        :param confidence: 相关字段的置信度信息，置信度越大，表示本次识别的对应字段的可靠性越高，在统计意义上，置信度越大，准确率越高。 置信度由算法给出，不直接等价于对应字段的准确率。 
        :type confidence: object
        """
        
        

        self._registration_number = None
        self._name = None
        self._type = None
        self._address = None
        self._legal_representative = None
        self._registered_capital = None
        self._found_date = None
        self._business_term = None
        self._business_scope = None
        self._issue_date = None
        self._confidence = None
        self.discriminator = None

        if registration_number is not None:
            self.registration_number = registration_number
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if address is not None:
            self.address = address
        if legal_representative is not None:
            self.legal_representative = legal_representative
        if registered_capital is not None:
            self.registered_capital = registered_capital
        if found_date is not None:
            self.found_date = found_date
        if business_term is not None:
            self.business_term = business_term
        if business_scope is not None:
            self.business_scope = business_scope
        if issue_date is not None:
            self.issue_date = issue_date
        if confidence is not None:
            self.confidence = confidence

    @property
    def registration_number(self):
        """Gets the registration_number of this BusinessLicenseResult.

          - 老版本营业执照对应注册号。  - 新三证合一版本营业执照对应社会保障号。 

        :return: The registration_number of this BusinessLicenseResult.
        :rtype: str
        """
        return self._registration_number

    @registration_number.setter
    def registration_number(self, registration_number):
        """Sets the registration_number of this BusinessLicenseResult.

          - 老版本营业执照对应注册号。  - 新三证合一版本营业执照对应社会保障号。 

        :param registration_number: The registration_number of this BusinessLicenseResult.
        :type registration_number: str
        """
        self._registration_number = registration_number

    @property
    def name(self):
        """Gets the name of this BusinessLicenseResult.

        企业名称。 

        :return: The name of this BusinessLicenseResult.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BusinessLicenseResult.

        企业名称。 

        :param name: The name of this BusinessLicenseResult.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        """Gets the type of this BusinessLicenseResult.

        公司/企业类型/主体类型。 

        :return: The type of this BusinessLicenseResult.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this BusinessLicenseResult.

        公司/企业类型/主体类型。 

        :param type: The type of this BusinessLicenseResult.
        :type type: str
        """
        self._type = type

    @property
    def address(self):
        """Gets the address of this BusinessLicenseResult.

        住所/营业场所/企业住所。 

        :return: The address of this BusinessLicenseResult.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this BusinessLicenseResult.

        住所/营业场所/企业住所。 

        :param address: The address of this BusinessLicenseResult.
        :type address: str
        """
        self._address = address

    @property
    def legal_representative(self):
        """Gets the legal_representative of this BusinessLicenseResult.

        法定代表人/负责人。 

        :return: The legal_representative of this BusinessLicenseResult.
        :rtype: str
        """
        return self._legal_representative

    @legal_representative.setter
    def legal_representative(self, legal_representative):
        """Sets the legal_representative of this BusinessLicenseResult.

        法定代表人/负责人。 

        :param legal_representative: The legal_representative of this BusinessLicenseResult.
        :type legal_representative: str
        """
        self._legal_representative = legal_representative

    @property
    def registered_capital(self):
        """Gets the registered_capital of this BusinessLicenseResult.

        注册资本。 

        :return: The registered_capital of this BusinessLicenseResult.
        :rtype: str
        """
        return self._registered_capital

    @registered_capital.setter
    def registered_capital(self, registered_capital):
        """Sets the registered_capital of this BusinessLicenseResult.

        注册资本。 

        :param registered_capital: The registered_capital of this BusinessLicenseResult.
        :type registered_capital: str
        """
        self._registered_capital = registered_capital

    @property
    def found_date(self):
        """Gets the found_date of this BusinessLicenseResult.

        成立日期。 

        :return: The found_date of this BusinessLicenseResult.
        :rtype: str
        """
        return self._found_date

    @found_date.setter
    def found_date(self, found_date):
        """Sets the found_date of this BusinessLicenseResult.

        成立日期。 

        :param found_date: The found_date of this BusinessLicenseResult.
        :type found_date: str
        """
        self._found_date = found_date

    @property
    def business_term(self):
        """Gets the business_term of this BusinessLicenseResult.

        营业期限。 

        :return: The business_term of this BusinessLicenseResult.
        :rtype: str
        """
        return self._business_term

    @business_term.setter
    def business_term(self, business_term):
        """Sets the business_term of this BusinessLicenseResult.

        营业期限。 

        :param business_term: The business_term of this BusinessLicenseResult.
        :type business_term: str
        """
        self._business_term = business_term

    @property
    def business_scope(self):
        """Gets the business_scope of this BusinessLicenseResult.

        经营范围。 

        :return: The business_scope of this BusinessLicenseResult.
        :rtype: str
        """
        return self._business_scope

    @business_scope.setter
    def business_scope(self, business_scope):
        """Sets the business_scope of this BusinessLicenseResult.

        经营范围。 

        :param business_scope: The business_scope of this BusinessLicenseResult.
        :type business_scope: str
        """
        self._business_scope = business_scope

    @property
    def issue_date(self):
        """Gets the issue_date of this BusinessLicenseResult.

        发照日期。 

        :return: The issue_date of this BusinessLicenseResult.
        :rtype: str
        """
        return self._issue_date

    @issue_date.setter
    def issue_date(self, issue_date):
        """Sets the issue_date of this BusinessLicenseResult.

        发照日期。 

        :param issue_date: The issue_date of this BusinessLicenseResult.
        :type issue_date: str
        """
        self._issue_date = issue_date

    @property
    def confidence(self):
        """Gets the confidence of this BusinessLicenseResult.

        相关字段的置信度信息，置信度越大，表示本次识别的对应字段的可靠性越高，在统计意义上，置信度越大，准确率越高。 置信度由算法给出，不直接等价于对应字段的准确率。 

        :return: The confidence of this BusinessLicenseResult.
        :rtype: object
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        """Sets the confidence of this BusinessLicenseResult.

        相关字段的置信度信息，置信度越大，表示本次识别的对应字段的可靠性越高，在统计意义上，置信度越大，准确率越高。 置信度由算法给出，不直接等价于对应字段的准确率。 

        :param confidence: The confidence of this BusinessLicenseResult.
        :type confidence: object
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
        if not isinstance(other, BusinessLicenseResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
