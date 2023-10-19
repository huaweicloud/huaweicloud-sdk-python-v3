# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListFirewallListResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'user_support_eps': 'bool',
        'data': 'HttpFirewallInstanceListResponseData'
    }

    attribute_map = {
        'user_support_eps': 'user_support_eps',
        'data': 'data'
    }

    def __init__(self, user_support_eps=None, data=None):
        """ListFirewallListResponse

        The model defined in huaweicloud sdk

        :param user_support_eps: 是否支持eps
        :type user_support_eps: bool
        :param data: 
        :type data: :class:`huaweicloudsdkcfw.v1.HttpFirewallInstanceListResponseData`
        """
        
        super(ListFirewallListResponse, self).__init__()

        self._user_support_eps = None
        self._data = None
        self.discriminator = None

        if user_support_eps is not None:
            self.user_support_eps = user_support_eps
        if data is not None:
            self.data = data

    @property
    def user_support_eps(self):
        """Gets the user_support_eps of this ListFirewallListResponse.

        是否支持eps

        :return: The user_support_eps of this ListFirewallListResponse.
        :rtype: bool
        """
        return self._user_support_eps

    @user_support_eps.setter
    def user_support_eps(self, user_support_eps):
        """Sets the user_support_eps of this ListFirewallListResponse.

        是否支持eps

        :param user_support_eps: The user_support_eps of this ListFirewallListResponse.
        :type user_support_eps: bool
        """
        self._user_support_eps = user_support_eps

    @property
    def data(self):
        """Gets the data of this ListFirewallListResponse.

        :return: The data of this ListFirewallListResponse.
        :rtype: :class:`huaweicloudsdkcfw.v1.HttpFirewallInstanceListResponseData`
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this ListFirewallListResponse.

        :param data: The data of this ListFirewallListResponse.
        :type data: :class:`huaweicloudsdkcfw.v1.HttpFirewallInstanceListResponseData`
        """
        self._data = data

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
        if not isinstance(other, ListFirewallListResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
