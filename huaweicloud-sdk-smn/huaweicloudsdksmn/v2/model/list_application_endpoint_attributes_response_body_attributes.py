# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListApplicationEndpointAttributesResponseBodyAttributes:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enabled': 'str',
        'token': 'str',
        'user_data': 'str'
    }

    attribute_map = {
        'enabled': 'enabled',
        'token': 'token',
        'user_data': 'user_data'
    }

    def __init__(self, enabled=None, token=None, user_data=None):
        r"""ListApplicationEndpointAttributesResponseBodyAttributes

        The model defined in huaweicloud sdk

        :param enabled: 设备是否可用。
        :type enabled: str
        :param token: 设备token。
        :type token: str
        :param user_data: 用户数据。
        :type user_data: str
        """
        
        

        self._enabled = None
        self._token = None
        self._user_data = None
        self.discriminator = None

        self.enabled = enabled
        self.token = token
        self.user_data = user_data

    @property
    def enabled(self):
        r"""Gets the enabled of this ListApplicationEndpointAttributesResponseBodyAttributes.

        设备是否可用。

        :return: The enabled of this ListApplicationEndpointAttributesResponseBodyAttributes.
        :rtype: str
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        r"""Sets the enabled of this ListApplicationEndpointAttributesResponseBodyAttributes.

        设备是否可用。

        :param enabled: The enabled of this ListApplicationEndpointAttributesResponseBodyAttributes.
        :type enabled: str
        """
        self._enabled = enabled

    @property
    def token(self):
        r"""Gets the token of this ListApplicationEndpointAttributesResponseBodyAttributes.

        设备token。

        :return: The token of this ListApplicationEndpointAttributesResponseBodyAttributes.
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        r"""Sets the token of this ListApplicationEndpointAttributesResponseBodyAttributes.

        设备token。

        :param token: The token of this ListApplicationEndpointAttributesResponseBodyAttributes.
        :type token: str
        """
        self._token = token

    @property
    def user_data(self):
        r"""Gets the user_data of this ListApplicationEndpointAttributesResponseBodyAttributes.

        用户数据。

        :return: The user_data of this ListApplicationEndpointAttributesResponseBodyAttributes.
        :rtype: str
        """
        return self._user_data

    @user_data.setter
    def user_data(self, user_data):
        r"""Sets the user_data of this ListApplicationEndpointAttributesResponseBodyAttributes.

        用户数据。

        :param user_data: The user_data of this ListApplicationEndpointAttributesResponseBodyAttributes.
        :type user_data: str
        """
        self._user_data = user_data

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
        if not isinstance(other, ListApplicationEndpointAttributesResponseBodyAttributes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
