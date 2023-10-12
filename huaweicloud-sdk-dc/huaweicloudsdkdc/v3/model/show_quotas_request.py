# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowQuotasRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'list[str]'
    }

    attribute_map = {
        'type': 'type'
    }

    def __init__(self, type=None):
        """ShowQuotasRequest

        The model defined in huaweicloud sdk

        :param type: 支持过滤的配额类型： - [physicalConnect:  物理连接direct_connect实例的配额和使用量](tag:hws) - [virtualInterface: 虚拟接口virtual-interface的配额和使用量](tag:hws) - [connectGateway: 连接网关（用于关联GEIP）的配额和使用量](tag:hws) - [geip: 每租户可以关联GEIP的配额和使用量](tag:hws) - [globalDcGateway 专线全球接入网关的配额和使用量](tag:hws) - [peerLinkPerGdgw: 接入网关的关联连接的配额和使用量](tag:hws)
        :type type: list[str]
        """
        
        

        self._type = None
        self.discriminator = None

        if type is not None:
            self.type = type

    @property
    def type(self):
        """Gets the type of this ShowQuotasRequest.

        支持过滤的配额类型： - [physicalConnect:  物理连接direct_connect实例的配额和使用量](tag:hws) - [virtualInterface: 虚拟接口virtual-interface的配额和使用量](tag:hws) - [connectGateway: 连接网关（用于关联GEIP）的配额和使用量](tag:hws) - [geip: 每租户可以关联GEIP的配额和使用量](tag:hws) - [globalDcGateway 专线全球接入网关的配额和使用量](tag:hws) - [peerLinkPerGdgw: 接入网关的关联连接的配额和使用量](tag:hws)

        :return: The type of this ShowQuotasRequest.
        :rtype: list[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ShowQuotasRequest.

        支持过滤的配额类型： - [physicalConnect:  物理连接direct_connect实例的配额和使用量](tag:hws) - [virtualInterface: 虚拟接口virtual-interface的配额和使用量](tag:hws) - [connectGateway: 连接网关（用于关联GEIP）的配额和使用量](tag:hws) - [geip: 每租户可以关联GEIP的配额和使用量](tag:hws) - [globalDcGateway 专线全球接入网关的配额和使用量](tag:hws) - [peerLinkPerGdgw: 接入网关的关联连接的配额和使用量](tag:hws)

        :param type: The type of this ShowQuotasRequest.
        :type type: list[str]
        """
        self._type = type

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
        if not isinstance(other, ShowQuotasRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
