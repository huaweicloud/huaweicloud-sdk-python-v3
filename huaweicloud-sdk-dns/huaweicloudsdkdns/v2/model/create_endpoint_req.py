# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateEndpointReq:

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
        'ipaddresses': 'list[Ipaddresses]'
    }

    attribute_map = {
        'name': 'name',
        'direction': 'direction',
        'region': 'region',
        'ipaddresses': 'ipaddresses'
    }

    def __init__(self, name=None, direction=None, region=None, ipaddresses=None):
        """CreateEndpointReq

        The model defined in huaweicloud sdk

        :param name: 待终端节点名称。 取值范围：1-64个字符，支持数字、字母、中文、_（下划线）、-（中划线）、.（点）。
        :type name: str
        :param direction: 终端节点方向。 取值： inbound，表示入站规则。 outbound，表示出站规则。
        :type direction: str
        :param region: 当前子网所在的region。
        :type region: str
        :param ipaddresses: 终端节点的ip地址和子网信息。
        :type ipaddresses: list[:class:`huaweicloudsdkdns.v2.Ipaddresses`]
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
        """Gets the name of this CreateEndpointReq.

        待终端节点名称。 取值范围：1-64个字符，支持数字、字母、中文、_（下划线）、-（中划线）、.（点）。

        :return: The name of this CreateEndpointReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateEndpointReq.

        待终端节点名称。 取值范围：1-64个字符，支持数字、字母、中文、_（下划线）、-（中划线）、.（点）。

        :param name: The name of this CreateEndpointReq.
        :type name: str
        """
        self._name = name

    @property
    def direction(self):
        """Gets the direction of this CreateEndpointReq.

        终端节点方向。 取值： inbound，表示入站规则。 outbound，表示出站规则。

        :return: The direction of this CreateEndpointReq.
        :rtype: str
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        """Sets the direction of this CreateEndpointReq.

        终端节点方向。 取值： inbound，表示入站规则。 outbound，表示出站规则。

        :param direction: The direction of this CreateEndpointReq.
        :type direction: str
        """
        self._direction = direction

    @property
    def region(self):
        """Gets the region of this CreateEndpointReq.

        当前子网所在的region。

        :return: The region of this CreateEndpointReq.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this CreateEndpointReq.

        当前子网所在的region。

        :param region: The region of this CreateEndpointReq.
        :type region: str
        """
        self._region = region

    @property
    def ipaddresses(self):
        """Gets the ipaddresses of this CreateEndpointReq.

        终端节点的ip地址和子网信息。

        :return: The ipaddresses of this CreateEndpointReq.
        :rtype: list[:class:`huaweicloudsdkdns.v2.Ipaddresses`]
        """
        return self._ipaddresses

    @ipaddresses.setter
    def ipaddresses(self, ipaddresses):
        """Sets the ipaddresses of this CreateEndpointReq.

        终端节点的ip地址和子网信息。

        :param ipaddresses: The ipaddresses of this CreateEndpointReq.
        :type ipaddresses: list[:class:`huaweicloudsdkdns.v2.Ipaddresses`]
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
        if not isinstance(other, CreateEndpointReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
