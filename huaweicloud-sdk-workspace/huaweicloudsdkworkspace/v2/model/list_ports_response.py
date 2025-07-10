# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPortsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ports': 'list[NeutronPort]'
    }

    attribute_map = {
        'ports': 'ports'
    }

    def __init__(self, ports=None):
        r"""ListPortsResponse

        The model defined in huaweicloud sdk

        :param ports: 端口列表。
        :type ports: list[:class:`huaweicloudsdkworkspace.v2.NeutronPort`]
        """
        
        super(ListPortsResponse, self).__init__()

        self._ports = None
        self.discriminator = None

        if ports is not None:
            self.ports = ports

    @property
    def ports(self):
        r"""Gets the ports of this ListPortsResponse.

        端口列表。

        :return: The ports of this ListPortsResponse.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.NeutronPort`]
        """
        return self._ports

    @ports.setter
    def ports(self, ports):
        r"""Sets the ports of this ListPortsResponse.

        端口列表。

        :param ports: The ports of this ListPortsResponse.
        :type ports: list[:class:`huaweicloudsdkworkspace.v2.NeutronPort`]
        """
        self._ports = ports

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
        if not isinstance(other, ListPortsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
