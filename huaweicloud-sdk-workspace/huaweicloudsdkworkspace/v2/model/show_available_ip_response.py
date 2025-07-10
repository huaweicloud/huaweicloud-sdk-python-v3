# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAvailableIpResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'available_ip': 'int'
    }

    attribute_map = {
        'available_ip': 'available_ip'
    }

    def __init__(self, available_ip=None):
        r"""ShowAvailableIpResponse

        The model defined in huaweicloud sdk

        :param available_ip: 可用ip数。
        :type available_ip: int
        """
        
        super(ShowAvailableIpResponse, self).__init__()

        self._available_ip = None
        self.discriminator = None

        if available_ip is not None:
            self.available_ip = available_ip

    @property
    def available_ip(self):
        r"""Gets the available_ip of this ShowAvailableIpResponse.

        可用ip数。

        :return: The available_ip of this ShowAvailableIpResponse.
        :rtype: int
        """
        return self._available_ip

    @available_ip.setter
    def available_ip(self, available_ip):
        r"""Sets the available_ip of this ShowAvailableIpResponse.

        可用ip数。

        :param available_ip: The available_ip of this ShowAvailableIpResponse.
        :type available_ip: int
        """
        self._available_ip = available_ip

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
        if not isinstance(other, ShowAvailableIpResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
