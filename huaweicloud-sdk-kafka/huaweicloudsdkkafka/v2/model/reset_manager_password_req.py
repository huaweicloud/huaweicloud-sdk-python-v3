# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResetManagerPasswordReq:

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
        r"""ResetManagerPasswordReq

        The model defined in huaweicloud sdk

        :param new_password: 8-32个字符。 至少包含以下字符中的3种：   - 大写字母   - 小写字母   - 数字   - 特殊字符&#x60;~!@#$%^&amp;*()-_&#x3D;+\\\\|[{}];:\\&#39;\\\&quot;,&lt;.&gt;/?  和空格，并且不能以-开头。
        :type new_password: str
        """
        
        

        self._new_password = None
        self.discriminator = None

        if new_password is not None:
            self.new_password = new_password

    @property
    def new_password(self):
        r"""Gets the new_password of this ResetManagerPasswordReq.

        8-32个字符。 至少包含以下字符中的3种：   - 大写字母   - 小写字母   - 数字   - 特殊字符`~!@#$%^&*()-_=+\\\\|[{}];:\\'\\\",<.>/?  和空格，并且不能以-开头。

        :return: The new_password of this ResetManagerPasswordReq.
        :rtype: str
        """
        return self._new_password

    @new_password.setter
    def new_password(self, new_password):
        r"""Sets the new_password of this ResetManagerPasswordReq.

        8-32个字符。 至少包含以下字符中的3种：   - 大写字母   - 小写字母   - 数字   - 特殊字符`~!@#$%^&*()-_=+\\\\|[{}];:\\'\\\",<.>/?  和空格，并且不能以-开头。

        :param new_password: The new_password of this ResetManagerPasswordReq.
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
        if not isinstance(other, ResetManagerPasswordReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
