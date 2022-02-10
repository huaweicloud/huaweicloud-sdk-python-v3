# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResetPasswordReq:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'newpassword': 'str'
    }

    attribute_map = {
        'newpassword': 'newpassword'
    }

    def __init__(self, newpassword=None):
        """ResetPasswordReq - a model defined in huaweicloud sdk"""
        
        

        self._newpassword = None
        self.discriminator = None

        self.newpassword = newpassword

    @property
    def newpassword(self):
        """Gets the newpassword of this ResetPasswordReq.

        新密码。

        :return: The newpassword of this ResetPasswordReq.
        :rtype: str
        """
        return self._newpassword

    @newpassword.setter
    def newpassword(self, newpassword):
        """Sets the newpassword of this ResetPasswordReq.

        新密码。

        :param newpassword: The newpassword of this ResetPasswordReq.
        :type: str
        """
        self._newpassword = newpassword

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
        if not isinstance(other, ResetPasswordReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
