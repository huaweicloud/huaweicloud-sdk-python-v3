# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LoginTokenAuth:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'securitytoken': 'LoginTokenSecurityToken'
    }

    attribute_map = {
        'securitytoken': 'securitytoken'
    }

    def __init__(self, securitytoken=None):
        r"""LoginTokenAuth

        The model defined in huaweicloud sdk

        :param securitytoken: 
        :type securitytoken: :class:`huaweicloudsdkiam.v3.LoginTokenSecurityToken`
        """
        
        

        self._securitytoken = None
        self.discriminator = None

        self.securitytoken = securitytoken

    @property
    def securitytoken(self):
        r"""Gets the securitytoken of this LoginTokenAuth.

        :return: The securitytoken of this LoginTokenAuth.
        :rtype: :class:`huaweicloudsdkiam.v3.LoginTokenSecurityToken`
        """
        return self._securitytoken

    @securitytoken.setter
    def securitytoken(self, securitytoken):
        r"""Sets the securitytoken of this LoginTokenAuth.

        :param securitytoken: The securitytoken of this LoginTokenAuth.
        :type securitytoken: :class:`huaweicloudsdkiam.v3.LoginTokenSecurityToken`
        """
        self._securitytoken = securitytoken

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
        if not isinstance(other, LoginTokenAuth):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
