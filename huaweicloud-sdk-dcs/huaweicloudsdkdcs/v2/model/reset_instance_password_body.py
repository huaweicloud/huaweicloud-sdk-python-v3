# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResetInstancePasswordBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'new_password': 'str',
        'no_password_access': 'bool'
    }

    attribute_map = {
        'new_password': 'new_password',
        'no_password_access': 'no_password_access'
    }

    def __init__(self, new_password=None, no_password_access=None):
        r"""ResetInstancePasswordBody

        The model defined in huaweicloud sdk

        :param new_password: 重置的新密码
        :type new_password: str
        :param no_password_access: 是否重置为免密码访问缓存实例
        :type no_password_access: bool
        """
        
        

        self._new_password = None
        self._no_password_access = None
        self.discriminator = None

        if new_password is not None:
            self.new_password = new_password
        if no_password_access is not None:
            self.no_password_access = no_password_access

    @property
    def new_password(self):
        r"""Gets the new_password of this ResetInstancePasswordBody.

        重置的新密码

        :return: The new_password of this ResetInstancePasswordBody.
        :rtype: str
        """
        return self._new_password

    @new_password.setter
    def new_password(self, new_password):
        r"""Sets the new_password of this ResetInstancePasswordBody.

        重置的新密码

        :param new_password: The new_password of this ResetInstancePasswordBody.
        :type new_password: str
        """
        self._new_password = new_password

    @property
    def no_password_access(self):
        r"""Gets the no_password_access of this ResetInstancePasswordBody.

        是否重置为免密码访问缓存实例

        :return: The no_password_access of this ResetInstancePasswordBody.
        :rtype: bool
        """
        return self._no_password_access

    @no_password_access.setter
    def no_password_access(self, no_password_access):
        r"""Sets the no_password_access of this ResetInstancePasswordBody.

        是否重置为免密码访问缓存实例

        :param no_password_access: The no_password_access of this ResetInstancePasswordBody.
        :type no_password_access: bool
        """
        self._no_password_access = no_password_access

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
        if not isinstance(other, ResetInstancePasswordBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
