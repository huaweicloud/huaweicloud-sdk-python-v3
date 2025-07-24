# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChangeServerPowerStateResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'physical_servers': 'list[ServersResponsePhysicalServers]'
    }

    attribute_map = {
        'physical_servers': 'physical_servers'
    }

    def __init__(self, physical_servers=None):
        r"""ChangeServerPowerStateResponse

        The model defined in huaweicloud sdk

        :param physical_servers: 物理服务器返回信息
        :type physical_servers: list[:class:`huaweicloudsdkclouddc.v1.ServersResponsePhysicalServers`]
        """
        
        super(ChangeServerPowerStateResponse, self).__init__()

        self._physical_servers = None
        self.discriminator = None

        if physical_servers is not None:
            self.physical_servers = physical_servers

    @property
    def physical_servers(self):
        r"""Gets the physical_servers of this ChangeServerPowerStateResponse.

        物理服务器返回信息

        :return: The physical_servers of this ChangeServerPowerStateResponse.
        :rtype: list[:class:`huaweicloudsdkclouddc.v1.ServersResponsePhysicalServers`]
        """
        return self._physical_servers

    @physical_servers.setter
    def physical_servers(self, physical_servers):
        r"""Sets the physical_servers of this ChangeServerPowerStateResponse.

        物理服务器返回信息

        :param physical_servers: The physical_servers of this ChangeServerPowerStateResponse.
        :type physical_servers: list[:class:`huaweicloudsdkclouddc.v1.ServersResponsePhysicalServers`]
        """
        self._physical_servers = physical_servers

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
        if not isinstance(other, ChangeServerPowerStateResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
