# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowUserLastLoginV5Response(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'user_last_login': 'UserLastLogin'
    }

    attribute_map = {
        'user_last_login': 'user_last_login'
    }

    def __init__(self, user_last_login=None):
        r"""ShowUserLastLoginV5Response

        The model defined in huaweicloud sdk

        :param user_last_login: 
        :type user_last_login: :class:`huaweicloudsdkiam.v5.UserLastLogin`
        """
        
        super(ShowUserLastLoginV5Response, self).__init__()

        self._user_last_login = None
        self.discriminator = None

        if user_last_login is not None:
            self.user_last_login = user_last_login

    @property
    def user_last_login(self):
        r"""Gets the user_last_login of this ShowUserLastLoginV5Response.

        :return: The user_last_login of this ShowUserLastLoginV5Response.
        :rtype: :class:`huaweicloudsdkiam.v5.UserLastLogin`
        """
        return self._user_last_login

    @user_last_login.setter
    def user_last_login(self, user_last_login):
        r"""Sets the user_last_login of this ShowUserLastLoginV5Response.

        :param user_last_login: The user_last_login of this ShowUserLastLoginV5Response.
        :type user_last_login: :class:`huaweicloudsdkiam.v5.UserLastLogin`
        """
        self._user_last_login = user_last_login

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
        if not isinstance(other, ShowUserLastLoginV5Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
