# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PwdResetRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'password': 'str'
    }

    attribute_map = {
        'password': 'password'
    }

    def __init__(self, password=None):
        r"""PwdResetRequest

        The model defined in huaweicloud sdk

        :param password: 数据库root用户密码。  - 8~32个字符。 - 至少包含以下字符中的三种： - 大写字母、小写字母、数字和特殊字符~!@#%^*-_&#x3D;+?,  - 弱密码校验。
        :type password: str
        """
        
        

        self._password = None
        self.discriminator = None

        self.password = password

    @property
    def password(self):
        r"""Gets the password of this PwdResetRequest.

        数据库root用户密码。  - 8~32个字符。 - 至少包含以下字符中的三种： - 大写字母、小写字母、数字和特殊字符~!@#%^*-_=+?,  - 弱密码校验。

        :return: The password of this PwdResetRequest.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        r"""Sets the password of this PwdResetRequest.

        数据库root用户密码。  - 8~32个字符。 - 至少包含以下字符中的三种： - 大写字母、小写字母、数字和特殊字符~!@#%^*-_=+?,  - 弱密码校验。

        :param password: The password of this PwdResetRequest.
        :type password: str
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
        if not isinstance(other, PwdResetRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
