# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PwdIdentity:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'methods': 'list[str]',
        'password': 'PwdPassword'
    }

    attribute_map = {
        'methods': 'methods',
        'password': 'password'
    }

    def __init__(self, methods=None, password=None):
        """PwdIdentity

        The model defined in huaweicloud sdk

        :param methods: 认证方法，该字段内容为[\&quot;password\&quot;]。
        :type methods: list[str]
        :param password: 
        :type password: :class:`huaweicloudsdkiam.v3.PwdPassword`
        """
        
        

        self._methods = None
        self._password = None
        self.discriminator = None

        self.methods = methods
        self.password = password

    @property
    def methods(self):
        """Gets the methods of this PwdIdentity.

        认证方法，该字段内容为[\"password\"]。

        :return: The methods of this PwdIdentity.
        :rtype: list[str]
        """
        return self._methods

    @methods.setter
    def methods(self, methods):
        """Sets the methods of this PwdIdentity.

        认证方法，该字段内容为[\"password\"]。

        :param methods: The methods of this PwdIdentity.
        :type methods: list[str]
        """
        self._methods = methods

    @property
    def password(self):
        """Gets the password of this PwdIdentity.


        :return: The password of this PwdIdentity.
        :rtype: :class:`huaweicloudsdkiam.v3.PwdPassword`
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this PwdIdentity.


        :param password: The password of this PwdIdentity.
        :type password: :class:`huaweicloudsdkiam.v3.PwdPassword`
        """
        self._password = password

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
        if not isinstance(other, PwdIdentity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
