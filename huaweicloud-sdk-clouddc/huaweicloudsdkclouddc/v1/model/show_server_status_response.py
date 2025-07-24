# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowServerStatusResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'server_status': 'ServerStatus',
        'server_power_status': 'ServerPowerStatus'
    }

    attribute_map = {
        'server_status': 'server_status',
        'server_power_status': 'server_power_status'
    }

    def __init__(self, server_status=None, server_power_status=None):
        r"""ShowServerStatusResponse

        The model defined in huaweicloud sdk

        :param server_status: 
        :type server_status: :class:`huaweicloudsdkclouddc.v1.ServerStatus`
        :param server_power_status: 
        :type server_power_status: :class:`huaweicloudsdkclouddc.v1.ServerPowerStatus`
        """
        
        super(ShowServerStatusResponse, self).__init__()

        self._server_status = None
        self._server_power_status = None
        self.discriminator = None

        if server_status is not None:
            self.server_status = server_status
        if server_power_status is not None:
            self.server_power_status = server_power_status

    @property
    def server_status(self):
        r"""Gets the server_status of this ShowServerStatusResponse.

        :return: The server_status of this ShowServerStatusResponse.
        :rtype: :class:`huaweicloudsdkclouddc.v1.ServerStatus`
        """
        return self._server_status

    @server_status.setter
    def server_status(self, server_status):
        r"""Sets the server_status of this ShowServerStatusResponse.

        :param server_status: The server_status of this ShowServerStatusResponse.
        :type server_status: :class:`huaweicloudsdkclouddc.v1.ServerStatus`
        """
        self._server_status = server_status

    @property
    def server_power_status(self):
        r"""Gets the server_power_status of this ShowServerStatusResponse.

        :return: The server_power_status of this ShowServerStatusResponse.
        :rtype: :class:`huaweicloudsdkclouddc.v1.ServerPowerStatus`
        """
        return self._server_power_status

    @server_power_status.setter
    def server_power_status(self, server_power_status):
        r"""Sets the server_power_status of this ShowServerStatusResponse.

        :param server_power_status: The server_power_status of this ShowServerStatusResponse.
        :type server_power_status: :class:`huaweicloudsdkclouddc.v1.ServerPowerStatus`
        """
        self._server_power_status = server_power_status

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
        if not isinstance(other, ShowServerStatusResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
