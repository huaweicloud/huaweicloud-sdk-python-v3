# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResetPasswordRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'new_password': 'str'
    }

    attribute_map = {
        'new_password': 'new_password'
    }

    def __init__(self, new_password=None):
        """ResetPasswordRequestBody

        The model defined in huaweicloud sdk

        :param new_password: GaussDB(DWS) 集群管理员新密码。 新密码复杂度要求如下：  - 密码字符长度为12~32位。 - 不能与用户名或倒序的用户名相同。 - 至少包含以下4种类型的3种：    - 小写字母   - 大写字母   - 数字   - 特殊字符（~!?,.:;-_&#39;\&quot;(){}[]/&lt;&gt;@#%^&amp;*+|\\&#x3D;）。 - 不能与历史密码相同。 - 不能为弱密码。
        :type new_password: str
        """
        
        

        self._new_password = None
        self.discriminator = None

        self.new_password = new_password

    @property
    def new_password(self):
        """Gets the new_password of this ResetPasswordRequestBody.

        GaussDB(DWS) 集群管理员新密码。 新密码复杂度要求如下：  - 密码字符长度为12~32位。 - 不能与用户名或倒序的用户名相同。 - 至少包含以下4种类型的3种：    - 小写字母   - 大写字母   - 数字   - 特殊字符（~!?,.:;-_'\"(){}[]/<>@#%^&*+|\\=）。 - 不能与历史密码相同。 - 不能为弱密码。

        :return: The new_password of this ResetPasswordRequestBody.
        :rtype: str
        """
        return self._new_password

    @new_password.setter
    def new_password(self, new_password):
        """Sets the new_password of this ResetPasswordRequestBody.

        GaussDB(DWS) 集群管理员新密码。 新密码复杂度要求如下：  - 密码字符长度为12~32位。 - 不能与用户名或倒序的用户名相同。 - 至少包含以下4种类型的3种：    - 小写字母   - 大写字母   - 数字   - 特殊字符（~!?,.:;-_'\"(){}[]/<>@#%^&*+|\\=）。 - 不能与历史密码相同。 - 不能为弱密码。

        :param new_password: The new_password of this ResetPasswordRequestBody.
        :type new_password: str
        """
        self._new_password = new_password

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
        if not isinstance(other, ResetPasswordRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
