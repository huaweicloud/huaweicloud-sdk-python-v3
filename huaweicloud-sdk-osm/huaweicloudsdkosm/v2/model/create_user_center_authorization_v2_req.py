# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateUserCenterAuthorizationV2Req:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'is_authorized': 'int',
        'authorization_content': 'str'
    }

    attribute_map = {
        'is_authorized': 'is_authorized',
        'authorization_content': 'authorization_content'
    }

    def __init__(self, is_authorized=None, authorization_content=None):
        """CreateUserCenterAuthorizationV2Req

        The model defined in huaweicloud sdk

        :param is_authorized: 是否同意 0不同意 1同意
        :type is_authorized: int
        :param authorization_content: 机密信息内容
        :type authorization_content: str
        """
        
        

        self._is_authorized = None
        self._authorization_content = None
        self.discriminator = None

        if is_authorized is not None:
            self.is_authorized = is_authorized
        if authorization_content is not None:
            self.authorization_content = authorization_content

    @property
    def is_authorized(self):
        """Gets the is_authorized of this CreateUserCenterAuthorizationV2Req.

        是否同意 0不同意 1同意

        :return: The is_authorized of this CreateUserCenterAuthorizationV2Req.
        :rtype: int
        """
        return self._is_authorized

    @is_authorized.setter
    def is_authorized(self, is_authorized):
        """Sets the is_authorized of this CreateUserCenterAuthorizationV2Req.

        是否同意 0不同意 1同意

        :param is_authorized: The is_authorized of this CreateUserCenterAuthorizationV2Req.
        :type is_authorized: int
        """
        self._is_authorized = is_authorized

    @property
    def authorization_content(self):
        """Gets the authorization_content of this CreateUserCenterAuthorizationV2Req.

        机密信息内容

        :return: The authorization_content of this CreateUserCenterAuthorizationV2Req.
        :rtype: str
        """
        return self._authorization_content

    @authorization_content.setter
    def authorization_content(self, authorization_content):
        """Sets the authorization_content of this CreateUserCenterAuthorizationV2Req.

        机密信息内容

        :param authorization_content: The authorization_content of this CreateUserCenterAuthorizationV2Req.
        :type authorization_content: str
        """
        self._authorization_content = authorization_content

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
        if not isinstance(other, CreateUserCenterAuthorizationV2Req):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
