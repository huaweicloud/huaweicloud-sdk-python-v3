# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NameDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'formatted': 'str',
        'family_name': 'str',
        'given_name': 'str',
        'middle_name': 'str',
        'honorific_prefix': 'str',
        'honorific_suffix': 'str'
    }

    attribute_map = {
        'formatted': 'formatted',
        'family_name': 'familyName',
        'given_name': 'givenName',
        'middle_name': 'middleName',
        'honorific_prefix': 'honorificPrefix',
        'honorific_suffix': 'honorificSuffix'
    }

    def __init__(self, formatted=None, family_name=None, given_name=None, middle_name=None, honorific_prefix=None, honorific_suffix=None):
        r"""NameDto

        The model defined in huaweicloud sdk

        :param formatted: 包含要显示的名称的格式化版本的字符串
        :type formatted: str
        :param family_name: 用户的姓氏
        :type family_name: str
        :param given_name: 用户的名字
        :type given_name: str
        :param middle_name: 用户的中间名
        :type middle_name: str
        :param honorific_prefix: 用户的尊称前缀
        :type honorific_prefix: str
        :param honorific_suffix: 用户的尊称后缀
        :type honorific_suffix: str
        """
        
        

        self._formatted = None
        self._family_name = None
        self._given_name = None
        self._middle_name = None
        self._honorific_prefix = None
        self._honorific_suffix = None
        self.discriminator = None

        if formatted is not None:
            self.formatted = formatted
        self.family_name = family_name
        self.given_name = given_name
        if middle_name is not None:
            self.middle_name = middle_name
        if honorific_prefix is not None:
            self.honorific_prefix = honorific_prefix
        if honorific_suffix is not None:
            self.honorific_suffix = honorific_suffix

    @property
    def formatted(self):
        r"""Gets the formatted of this NameDto.

        包含要显示的名称的格式化版本的字符串

        :return: The formatted of this NameDto.
        :rtype: str
        """
        return self._formatted

    @formatted.setter
    def formatted(self, formatted):
        r"""Sets the formatted of this NameDto.

        包含要显示的名称的格式化版本的字符串

        :param formatted: The formatted of this NameDto.
        :type formatted: str
        """
        self._formatted = formatted

    @property
    def family_name(self):
        r"""Gets the family_name of this NameDto.

        用户的姓氏

        :return: The family_name of this NameDto.
        :rtype: str
        """
        return self._family_name

    @family_name.setter
    def family_name(self, family_name):
        r"""Sets the family_name of this NameDto.

        用户的姓氏

        :param family_name: The family_name of this NameDto.
        :type family_name: str
        """
        self._family_name = family_name

    @property
    def given_name(self):
        r"""Gets the given_name of this NameDto.

        用户的名字

        :return: The given_name of this NameDto.
        :rtype: str
        """
        return self._given_name

    @given_name.setter
    def given_name(self, given_name):
        r"""Sets the given_name of this NameDto.

        用户的名字

        :param given_name: The given_name of this NameDto.
        :type given_name: str
        """
        self._given_name = given_name

    @property
    def middle_name(self):
        r"""Gets the middle_name of this NameDto.

        用户的中间名

        :return: The middle_name of this NameDto.
        :rtype: str
        """
        return self._middle_name

    @middle_name.setter
    def middle_name(self, middle_name):
        r"""Sets the middle_name of this NameDto.

        用户的中间名

        :param middle_name: The middle_name of this NameDto.
        :type middle_name: str
        """
        self._middle_name = middle_name

    @property
    def honorific_prefix(self):
        r"""Gets the honorific_prefix of this NameDto.

        用户的尊称前缀

        :return: The honorific_prefix of this NameDto.
        :rtype: str
        """
        return self._honorific_prefix

    @honorific_prefix.setter
    def honorific_prefix(self, honorific_prefix):
        r"""Sets the honorific_prefix of this NameDto.

        用户的尊称前缀

        :param honorific_prefix: The honorific_prefix of this NameDto.
        :type honorific_prefix: str
        """
        self._honorific_prefix = honorific_prefix

    @property
    def honorific_suffix(self):
        r"""Gets the honorific_suffix of this NameDto.

        用户的尊称后缀

        :return: The honorific_suffix of this NameDto.
        :rtype: str
        """
        return self._honorific_suffix

    @honorific_suffix.setter
    def honorific_suffix(self, honorific_suffix):
        r"""Sets the honorific_suffix of this NameDto.

        用户的尊称后缀

        :param honorific_suffix: The honorific_suffix of this NameDto.
        :type honorific_suffix: str
        """
        self._honorific_suffix = honorific_suffix

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
        if not isinstance(other, NameDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
