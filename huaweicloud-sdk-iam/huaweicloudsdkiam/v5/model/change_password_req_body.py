# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChangePasswordReqBody:

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
        'old_password': 'str'
    }

    attribute_map = {
        'new_password': 'new_password',
        'old_password': 'old_password'
    }

    def __init__(self, new_password=None, old_password=None):
        r"""ChangePasswordReqBody

        The model defined in huaweicloud sdk

        :param new_password: IAM用户的新密码。
        :type new_password: str
        :param old_password: IAM用户的旧密码。
        :type old_password: str
        """
        
        

        self._new_password = None
        self._old_password = None
        self.discriminator = None

        self.new_password = new_password
        self.old_password = old_password

    @property
    def new_password(self):
        r"""Gets the new_password of this ChangePasswordReqBody.

        IAM用户的新密码。

        :return: The new_password of this ChangePasswordReqBody.
        :rtype: str
        """
        return self._new_password

    @new_password.setter
    def new_password(self, new_password):
        r"""Sets the new_password of this ChangePasswordReqBody.

        IAM用户的新密码。

        :param new_password: The new_password of this ChangePasswordReqBody.
        :type new_password: str
        """
        self._new_password = new_password

    @property
    def old_password(self):
        r"""Gets the old_password of this ChangePasswordReqBody.

        IAM用户的旧密码。

        :return: The old_password of this ChangePasswordReqBody.
        :rtype: str
        """
        return self._old_password

    @old_password.setter
    def old_password(self, old_password):
        r"""Sets the old_password of this ChangePasswordReqBody.

        IAM用户的旧密码。

        :param old_password: The old_password of this ChangePasswordReqBody.
        :type old_password: str
        """
        self._old_password = old_password

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
        if not isinstance(other, ChangePasswordReqBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
