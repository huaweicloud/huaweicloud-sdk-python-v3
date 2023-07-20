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
        'type': 'list[str]',
        'er_id': 'list[str]',
        'route_table_id': 'list[str]',
        'vpc_id': 'list[str]'
    }

    attribute_map = {
        'type': 'type',
        'er_id': 'erId',
        'route_table_id': 'routeTableId',
        'vpc_id': 'vpcId'
    }

    def __init__(self, type=None, er_id=None, route_table_id=None, vpc_id=None):
        """ShowQuotasRequest

        The model defined in huaweicloud sdk

        :param type: 支持过滤的配额类型： - er_instance: 企业路由器实例的配额和使用量 - dc_attachment: 云专线网关连接的配额和使用量 - vpc_attachment: VPC连接的配额和使用量 - vpn_attachment: VPN网关连接的配额和使用量 - peering_attachment：云连接实例连接的配额和使用量 - can_attachment: 智能接入网关连接的配额和使用量 - route_table: 路由表的配额和使用量 - static_route: 静态路由的配额和使用量 - vpc_er: 每个vpc可以接入的企业路由器数量和当前使用量 - flow_log: 每个连接可以创建的流日志数量
        :type type: list[str]
        :param er_id: 
        :type er_id: list[str]
        :param route_table_id: 
        :type route_table_id: list[str]
        :param vpc_id: 
        :type vpc_id: list[str]
        """
        
        

        self._type = None
        self._er_id = None
        self._route_table_id = None
        self._vpc_id = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if er_id is not None:
            self.er_id = er_id
        if route_table_id is not None:
            self.route_table_id = route_table_id
        if vpc_id is not None:
            self.vpc_id = vpc_id

    @property
    def type(self):
        """Gets the type of this ShowQuotasRequest.

        支持过滤的配额类型： - er_instance: 企业路由器实例的配额和使用量 - dc_attachment: 云专线网关连接的配额和使用量 - vpc_attachment: VPC连接的配额和使用量 - vpn_attachment: VPN网关连接的配额和使用量 - peering_attachment：云连接实例连接的配额和使用量 - can_attachment: 智能接入网关连接的配额和使用量 - route_table: 路由表的配额和使用量 - static_route: 静态路由的配额和使用量 - vpc_er: 每个vpc可以接入的企业路由器数量和当前使用量 - flow_log: 每个连接可以创建的流日志数量

        :return: The type of this ShowQuotasRequest.
        :rtype: list[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ShowQuotasRequest.

        支持过滤的配额类型： - er_instance: 企业路由器实例的配额和使用量 - dc_attachment: 云专线网关连接的配额和使用量 - vpc_attachment: VPC连接的配额和使用量 - vpn_attachment: VPN网关连接的配额和使用量 - peering_attachment：云连接实例连接的配额和使用量 - can_attachment: 智能接入网关连接的配额和使用量 - route_table: 路由表的配额和使用量 - static_route: 静态路由的配额和使用量 - vpc_er: 每个vpc可以接入的企业路由器数量和当前使用量 - flow_log: 每个连接可以创建的流日志数量

        :param type: The type of this ShowQuotasRequest.
        :type type: list[str]
        """
        self._type = type

    @property
    def er_id(self):
        """Gets the er_id of this ShowQuotasRequest.

        :return: The er_id of this ShowQuotasRequest.
        :rtype: list[str]
        """
        return self._er_id

    @er_id.setter
    def er_id(self, er_id):
        """Sets the er_id of this ShowQuotasRequest.

        :param er_id: The er_id of this ShowQuotasRequest.
        :type er_id: list[str]
        """
        self._er_id = er_id

    @property
    def route_table_id(self):
        """Gets the route_table_id of this ShowQuotasRequest.

        :return: The route_table_id of this ShowQuotasRequest.
        :rtype: list[str]
        """
        return self._route_table_id

    @route_table_id.setter
    def route_table_id(self, route_table_id):
        """Sets the route_table_id of this ShowQuotasRequest.

        :param route_table_id: The route_table_id of this ShowQuotasRequest.
        :type route_table_id: list[str]
        """
        self._route_table_id = route_table_id

    @property
    def vpc_id(self):
        """Gets the vpc_id of this ShowQuotasRequest.

        :return: The vpc_id of this ShowQuotasRequest.
        :rtype: list[str]
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this ShowQuotasRequest.

        :param vpc_id: The vpc_id of this ShowQuotasRequest.
        :type vpc_id: list[str]
        """
        self._vpc_id = vpc_id

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
