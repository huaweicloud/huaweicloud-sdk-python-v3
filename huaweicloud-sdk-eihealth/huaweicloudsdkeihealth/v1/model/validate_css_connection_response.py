# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ValidateCssConnectionResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'connected': 'bool',
        'reason': 'str'
    }

    attribute_map = {
        'connected': 'connected',
        'reason': 'reason'
    }

    def __init__(self, connected=None, reason=None):
        """ValidateCssConnectionResponse

        The model defined in huaweicloud sdk

        :param connected: 是否连通
        :type connected: bool
        :param reason: 失败原因
        :type reason: str
        """
        
        super(ValidateCssConnectionResponse, self).__init__()

        self._connected = None
        self._reason = None
        self.discriminator = None

        if connected is not None:
            self.connected = connected
        if reason is not None:
            self.reason = reason

    @property
    def connected(self):
        """Gets the connected of this ValidateCssConnectionResponse.

        是否连通

        :return: The connected of this ValidateCssConnectionResponse.
        :rtype: bool
        """
        return self._connected

    @connected.setter
    def connected(self, connected):
        """Sets the connected of this ValidateCssConnectionResponse.

        是否连通

        :param connected: The connected of this ValidateCssConnectionResponse.
        :type connected: bool
        """
        self._connected = connected

    @property
    def reason(self):
        """Gets the reason of this ValidateCssConnectionResponse.

        失败原因

        :return: The reason of this ValidateCssConnectionResponse.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this ValidateCssConnectionResponse.

        失败原因

        :param reason: The reason of this ValidateCssConnectionResponse.
        :type reason: str
        """
        self._reason = reason

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
        if not isinstance(other, ValidateCssConnectionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
