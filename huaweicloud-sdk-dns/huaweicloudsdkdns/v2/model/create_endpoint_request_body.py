# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateEndpointRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'direction': 'str',
        'region': 'str',
        'ipaddresses': 'list[IpaddressInfo]'
    }

    attribute_map = {
        'name': 'name',
        'direction': 'direction',
        'region': 'region',
        'ipaddresses': 'ipaddresses'
    }

    def __init__(self, name=None, direction=None, region=None, ipaddresses=None):
        r"""CreateEndpointRequestBody

        The model defined in huaweicloud sdk

        :param name: 待创建的终端节点名称。 取值范围：1-64个字符，支持数字、字母、中文、_（下划线）、-（中划线）、.（点）。
        :type name: str
        :param direction: 终端节点方向。 取值： inbound，表示入站终端节点。 outbound，表示出站终端节点。
        :type direction: str
        :param region: 当前子网所在的region。
        :type region: str
        :param ipaddresses: 终端节点的IP地址和子网信息。最少需要添加2个IP地址，最多可以添加6个IP地址。
        :type ipaddresses: list[:class:`huaweicloudsdkdns.v2.IpaddressInfo`]
        """
        
        

        self._name = None
        self._direction = None
        self._region = None
        self._ipaddresses = None
        self.discriminator = None

        self.name = name
        self.direction = direction
        self.region = region
        self.ipaddresses = ipaddresses

    @property
    def name(self):
        r"""Gets the name of this CreateEndpointRequestBody.

        待创建的终端节点名称。 取值范围：1-64个字符，支持数字、字母、中文、_（下划线）、-（中划线）、.（点）。

        :return: The name of this CreateEndpointRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateEndpointRequestBody.

        待创建的终端节点名称。 取值范围：1-64个字符，支持数字、字母、中文、_（下划线）、-（中划线）、.（点）。

        :param name: The name of this CreateEndpointRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def direction(self):
        r"""Gets the direction of this CreateEndpointRequestBody.

        终端节点方向。 取值： inbound，表示入站终端节点。 outbound，表示出站终端节点。

        :return: The direction of this CreateEndpointRequestBody.
        :rtype: str
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        r"""Sets the direction of this CreateEndpointRequestBody.

        终端节点方向。 取值： inbound，表示入站终端节点。 outbound，表示出站终端节点。

        :param direction: The direction of this CreateEndpointRequestBody.
        :type direction: str
        """
        self._direction = direction

    @property
    def region(self):
        r"""Gets the region of this CreateEndpointRequestBody.

        当前子网所在的region。

        :return: The region of this CreateEndpointRequestBody.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this CreateEndpointRequestBody.

        当前子网所在的region。

        :param region: The region of this CreateEndpointRequestBody.
        :type region: str
        """
        self._region = region

    @property
    def ipaddresses(self):
        r"""Gets the ipaddresses of this CreateEndpointRequestBody.

        终端节点的IP地址和子网信息。最少需要添加2个IP地址，最多可以添加6个IP地址。

        :return: The ipaddresses of this CreateEndpointRequestBody.
        :rtype: list[:class:`huaweicloudsdkdns.v2.IpaddressInfo`]
        """
        return self._ipaddresses

    @ipaddresses.setter
    def ipaddresses(self, ipaddresses):
        r"""Sets the ipaddresses of this CreateEndpointRequestBody.

        终端节点的IP地址和子网信息。最少需要添加2个IP地址，最多可以添加6个IP地址。

        :param ipaddresses: The ipaddresses of this CreateEndpointRequestBody.
        :type ipaddresses: list[:class:`huaweicloudsdkdns.v2.IpaddressInfo`]
        """
        self._ipaddresses = ipaddresses

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
        if not isinstance(other, CreateEndpointRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
