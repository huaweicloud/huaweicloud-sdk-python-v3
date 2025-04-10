# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConfigByOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'password_regex': 'str',
        'password_regex_description': 'str'
    }

    attribute_map = {
        'password_regex': 'password_regex',
        'password_regex_description': 'password_regex_description'
    }

    def __init__(self, password_regex=None, password_regex_description=None):
        r"""ConfigByOption

        The model defined in huaweicloud sdk

        :param password_regex: 密码强度策略的正则表达式。(当option为password_regex时返回)
        :type password_regex: str
        :param password_regex_description: 密码强度策略的描述。(当option为password_regex_description时返回)
        :type password_regex_description: str
        """
        
        

        self._password_regex = None
        self._password_regex_description = None
        self.discriminator = None

        if password_regex is not None:
            self.password_regex = password_regex
        if password_regex_description is not None:
            self.password_regex_description = password_regex_description

    @property
    def password_regex(self):
        r"""Gets the password_regex of this ConfigByOption.

        密码强度策略的正则表达式。(当option为password_regex时返回)

        :return: The password_regex of this ConfigByOption.
        :rtype: str
        """
        return self._password_regex

    @password_regex.setter
    def password_regex(self, password_regex):
        r"""Sets the password_regex of this ConfigByOption.

        密码强度策略的正则表达式。(当option为password_regex时返回)

        :param password_regex: The password_regex of this ConfigByOption.
        :type password_regex: str
        """
        self._password_regex = password_regex

    @property
    def password_regex_description(self):
        r"""Gets the password_regex_description of this ConfigByOption.

        密码强度策略的描述。(当option为password_regex_description时返回)

        :return: The password_regex_description of this ConfigByOption.
        :rtype: str
        """
        return self._password_regex_description

    @password_regex_description.setter
    def password_regex_description(self, password_regex_description):
        r"""Sets the password_regex_description of this ConfigByOption.

        密码强度策略的描述。(当option为password_regex_description时返回)

        :param password_regex_description: The password_regex_description of this ConfigByOption.
        :type password_regex_description: str
        """
        self._password_regex_description = password_regex_description

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
        if not isinstance(other, ConfigByOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
