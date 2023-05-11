# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IdcardResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'number': 'str',
        'sex': 'str',
        'birth': 'str',
        'ethnicity': 'str',
        'address': 'str',
        'issue': 'str',
        'valid_from': 'str',
        'valid_to': 'str'
    }

    attribute_map = {
        'name': 'name',
        'number': 'number',
        'sex': 'sex',
        'birth': 'birth',
        'ethnicity': 'ethnicity',
        'address': 'address',
        'issue': 'issue',
        'valid_from': 'valid_from',
        'valid_to': 'valid_to'
    }

    def __init__(self, name=None, number=None, sex=None, birth=None, ethnicity=None, address=None, issue=None, valid_from=None, valid_to=None):
        """IdcardResult

        The model defined in huaweicloud sdk

        :param name: 身份证上识别的名称。
        :type name: str
        :param number: 身份证号。
        :type number: str
        :param sex: 性别。
        :type sex: str
        :param birth: 出生日期。
        :type birth: str
        :param ethnicity: 民族。
        :type ethnicity: str
        :param address: 地址。
        :type address: str
        :param issue: 发证机关。
        :type issue: str
        :param valid_from: 有效起始日期。
        :type valid_from: str
        :param valid_to: 有效结束日期。
        :type valid_to: str
        """
        
        

        self._name = None
        self._number = None
        self._sex = None
        self._birth = None
        self._ethnicity = None
        self._address = None
        self._issue = None
        self._valid_from = None
        self._valid_to = None
        self.discriminator = None

        self.name = name
        self.number = number
        self.sex = sex
        self.birth = birth
        self.ethnicity = ethnicity
        self.address = address
        if issue is not None:
            self.issue = issue
        if valid_from is not None:
            self.valid_from = valid_from
        if valid_to is not None:
            self.valid_to = valid_to

    @property
    def name(self):
        """Gets the name of this IdcardResult.

        身份证上识别的名称。

        :return: The name of this IdcardResult.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this IdcardResult.

        身份证上识别的名称。

        :param name: The name of this IdcardResult.
        :type name: str
        """
        self._name = name

    @property
    def number(self):
        """Gets the number of this IdcardResult.

        身份证号。

        :return: The number of this IdcardResult.
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this IdcardResult.

        身份证号。

        :param number: The number of this IdcardResult.
        :type number: str
        """
        self._number = number

    @property
    def sex(self):
        """Gets the sex of this IdcardResult.

        性别。

        :return: The sex of this IdcardResult.
        :rtype: str
        """
        return self._sex

    @sex.setter
    def sex(self, sex):
        """Sets the sex of this IdcardResult.

        性别。

        :param sex: The sex of this IdcardResult.
        :type sex: str
        """
        self._sex = sex

    @property
    def birth(self):
        """Gets the birth of this IdcardResult.

        出生日期。

        :return: The birth of this IdcardResult.
        :rtype: str
        """
        return self._birth

    @birth.setter
    def birth(self, birth):
        """Sets the birth of this IdcardResult.

        出生日期。

        :param birth: The birth of this IdcardResult.
        :type birth: str
        """
        self._birth = birth

    @property
    def ethnicity(self):
        """Gets the ethnicity of this IdcardResult.

        民族。

        :return: The ethnicity of this IdcardResult.
        :rtype: str
        """
        return self._ethnicity

    @ethnicity.setter
    def ethnicity(self, ethnicity):
        """Sets the ethnicity of this IdcardResult.

        民族。

        :param ethnicity: The ethnicity of this IdcardResult.
        :type ethnicity: str
        """
        self._ethnicity = ethnicity

    @property
    def address(self):
        """Gets the address of this IdcardResult.

        地址。

        :return: The address of this IdcardResult.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this IdcardResult.

        地址。

        :param address: The address of this IdcardResult.
        :type address: str
        """
        self._address = address

    @property
    def issue(self):
        """Gets the issue of this IdcardResult.

        发证机关。

        :return: The issue of this IdcardResult.
        :rtype: str
        """
        return self._issue

    @issue.setter
    def issue(self, issue):
        """Sets the issue of this IdcardResult.

        发证机关。

        :param issue: The issue of this IdcardResult.
        :type issue: str
        """
        self._issue = issue

    @property
    def valid_from(self):
        """Gets the valid_from of this IdcardResult.

        有效起始日期。

        :return: The valid_from of this IdcardResult.
        :rtype: str
        """
        return self._valid_from

    @valid_from.setter
    def valid_from(self, valid_from):
        """Sets the valid_from of this IdcardResult.

        有效起始日期。

        :param valid_from: The valid_from of this IdcardResult.
        :type valid_from: str
        """
        self._valid_from = valid_from

    @property
    def valid_to(self):
        """Gets the valid_to of this IdcardResult.

        有效结束日期。

        :return: The valid_to of this IdcardResult.
        :rtype: str
        """
        return self._valid_to

    @valid_to.setter
    def valid_to(self, valid_to):
        """Sets the valid_to of this IdcardResult.

        有效结束日期。

        :param valid_to: The valid_to of this IdcardResult.
        :type valid_to: str
        """
        self._valid_to = valid_to

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
        if not isinstance(other, IdcardResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
