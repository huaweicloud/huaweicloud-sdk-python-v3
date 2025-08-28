# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UserLastLogin:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'last_login_at': 'datetime'
    }

    attribute_map = {
        'last_login_at': 'last_login_at'
    }

    def __init__(self, last_login_at=None):
        r"""UserLastLogin

        The model defined in huaweicloud sdk

        :param last_login_at: IAM用户最后登录时间。若为null，则表示从未登录过。
        :type last_login_at: datetime
        """
        
        

        self._last_login_at = None
        self.discriminator = None

        if last_login_at is not None:
            self.last_login_at = last_login_at

    @property
    def last_login_at(self):
        r"""Gets the last_login_at of this UserLastLogin.

        IAM用户最后登录时间。若为null，则表示从未登录过。

        :return: The last_login_at of this UserLastLogin.
        :rtype: datetime
        """
        return self._last_login_at

    @last_login_at.setter
    def last_login_at(self, last_login_at):
        r"""Sets the last_login_at of this UserLastLogin.

        IAM用户最后登录时间。若为null，则表示从未登录过。

        :param last_login_at: The last_login_at of this UserLastLogin.
        :type last_login_at: datetime
        """
        self._last_login_at = last_login_at

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
        if not isinstance(other, UserLastLogin):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
