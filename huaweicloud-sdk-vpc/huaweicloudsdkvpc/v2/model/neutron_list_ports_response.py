# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NeutronListPortsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ports': 'list[NeutronPort]',
        'ports_links': 'list[NeutronPageLink]'
    }

    attribute_map = {
        'ports': 'ports',
        'ports_links': 'ports_links'
    }

    def __init__(self, ports=None, ports_links=None):
        """NeutronListPortsResponse

        The model defined in huaweicloud sdk

        :param ports: port对象列表
        :type ports: list[:class:`huaweicloudsdkvpc.v2.NeutronPort`]
        :param ports_links: 分页信息
        :type ports_links: list[:class:`huaweicloudsdkvpc.v2.NeutronPageLink`]
        """
        
        super(NeutronListPortsResponse, self).__init__()

        self._ports = None
        self._ports_links = None
        self.discriminator = None

        if ports is not None:
            self.ports = ports
        if ports_links is not None:
            self.ports_links = ports_links

    @property
    def ports(self):
        """Gets the ports of this NeutronListPortsResponse.

        port对象列表

        :return: The ports of this NeutronListPortsResponse.
        :rtype: list[:class:`huaweicloudsdkvpc.v2.NeutronPort`]
        """
        return self._ports

    @ports.setter
    def ports(self, ports):
        """Sets the ports of this NeutronListPortsResponse.

        port对象列表

        :param ports: The ports of this NeutronListPortsResponse.
        :type ports: list[:class:`huaweicloudsdkvpc.v2.NeutronPort`]
        """
        self._ports = ports

    @property
    def ports_links(self):
        """Gets the ports_links of this NeutronListPortsResponse.

        分页信息

        :return: The ports_links of this NeutronListPortsResponse.
        :rtype: list[:class:`huaweicloudsdkvpc.v2.NeutronPageLink`]
        """
        return self._ports_links

    @ports_links.setter
    def ports_links(self, ports_links):
        """Sets the ports_links of this NeutronListPortsResponse.

        分页信息

        :param ports_links: The ports_links of this NeutronListPortsResponse.
        :type ports_links: list[:class:`huaweicloudsdkvpc.v2.NeutronPageLink`]
        """
        self._ports_links = ports_links

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
        if not isinstance(other, NeutronListPortsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
