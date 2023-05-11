# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DiscoveryRule:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'check_content': 'list[str]',
        'check_mode': 'str',
        'check_type': 'str'
    }

    attribute_map = {
        'check_content': 'checkContent',
        'check_mode': 'checkMode',
        'check_type': 'checkType'
    }

    def __init__(self, check_content=None, check_mode=None, check_type=None):
        """DiscoveryRule

        The model defined in huaweicloud sdk

        :param check_content: 匹配值。
        :type check_content: list[str]
        :param check_mode: 匹配条件。 contain、equals
        :type check_mode: str
        :param check_type: 匹配类型。 cmdLine、env、scope
        :type check_type: str
        """
        
        

        self._check_content = None
        self._check_mode = None
        self._check_type = None
        self.discriminator = None

        self.check_content = check_content
        self.check_mode = check_mode
        self.check_type = check_type

    @property
    def check_content(self):
        """Gets the check_content of this DiscoveryRule.

        匹配值。

        :return: The check_content of this DiscoveryRule.
        :rtype: list[str]
        """
        return self._check_content

    @check_content.setter
    def check_content(self, check_content):
        """Sets the check_content of this DiscoveryRule.

        匹配值。

        :param check_content: The check_content of this DiscoveryRule.
        :type check_content: list[str]
        """
        self._check_content = check_content

    @property
    def check_mode(self):
        """Gets the check_mode of this DiscoveryRule.

        匹配条件。 contain、equals

        :return: The check_mode of this DiscoveryRule.
        :rtype: str
        """
        return self._check_mode

    @check_mode.setter
    def check_mode(self, check_mode):
        """Sets the check_mode of this DiscoveryRule.

        匹配条件。 contain、equals

        :param check_mode: The check_mode of this DiscoveryRule.
        :type check_mode: str
        """
        self._check_mode = check_mode

    @property
    def check_type(self):
        """Gets the check_type of this DiscoveryRule.

        匹配类型。 cmdLine、env、scope

        :return: The check_type of this DiscoveryRule.
        :rtype: str
        """
        return self._check_type

    @check_type.setter
    def check_type(self, check_type):
        """Sets the check_type of this DiscoveryRule.

        匹配类型。 cmdLine、env、scope

        :param check_type: The check_type of this DiscoveryRule.
        :type check_type: str
        """
        self._check_type = check_type

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
        if not isinstance(other, DiscoveryRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
