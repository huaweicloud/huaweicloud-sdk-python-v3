# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OAuth:

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
        'code': 'str',
        'state': 'str'
    }

    attribute_map = {
        'name': 'name',
        'code': 'code',
        'state': 'state'
    }

    def __init__(self, name=None, code=None, state=None):
        """OAuth

        The model defined in huaweicloud sdk

        :param name: 授权名称。
        :type name: str
        :param code: git仓库授权后，重定向回来的url里面的query参数。
        :type code: str
        :param state: git仓库授权后，一次性的认证编码和随机串。
        :type state: str
        """
        
        

        self._name = None
        self._code = None
        self._state = None
        self.discriminator = None

        self.name = name
        self.code = code
        self.state = state

    @property
    def name(self):
        """Gets the name of this OAuth.

        授权名称。

        :return: The name of this OAuth.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this OAuth.

        授权名称。

        :param name: The name of this OAuth.
        :type name: str
        """
        self._name = name

    @property
    def code(self):
        """Gets the code of this OAuth.

        git仓库授权后，重定向回来的url里面的query参数。

        :return: The code of this OAuth.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this OAuth.

        git仓库授权后，重定向回来的url里面的query参数。

        :param code: The code of this OAuth.
        :type code: str
        """
        self._code = code

    @property
    def state(self):
        """Gets the state of this OAuth.

        git仓库授权后，一次性的认证编码和随机串。

        :return: The state of this OAuth.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this OAuth.

        git仓库授权后，一次性的认证编码和随机串。

        :param state: The state of this OAuth.
        :type state: str
        """
        self._state = state

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
        if not isinstance(other, OAuth):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
