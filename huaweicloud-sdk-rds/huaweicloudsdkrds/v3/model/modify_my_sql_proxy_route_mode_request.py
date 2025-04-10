# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModifyMySqlProxyRouteModeRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'master_weight': 'int',
        'readonly_instances': 'list[InstancesWeight]',
        'route_mode': 'int'
    }

    attribute_map = {
        'master_weight': 'master_weight',
        'readonly_instances': 'readonly_instances',
        'route_mode': 'route_mode'
    }

    def __init__(self, master_weight=None, readonly_instances=None, route_mode=None):
        r"""ModifyMySqlProxyRouteModeRequest

        The model defined in huaweicloud sdk

        :param master_weight: 数据库主实例读权重。     - 当route_mode选择0（权重负载）时，该字段取值范围为0~1000。     - 当route_mode选择1或2（负载均衡）时，该字段不生效。
        :type master_weight: int
        :param readonly_instances: 数据库节点的读权重设置。      - 只能为只读实例选择权重。     - 该列表可以为空列表。
        :type readonly_instances: list[:class:`huaweicloudsdkrds.v3.InstancesWeight`]
        :param route_mode: 数据库代理路由模式。 取值范围:     0：表示权重负载模式。     1：表示负载均衡模式（数据库主实例不接受读请求）。     2：表示负载均衡模式（数据库主实例接受读请求）。      - 如需使用负载均衡模式，请联系客服申请
        :type route_mode: int
        """
        
        

        self._master_weight = None
        self._readonly_instances = None
        self._route_mode = None
        self.discriminator = None

        self.master_weight = master_weight
        self.readonly_instances = readonly_instances
        self.route_mode = route_mode

    @property
    def master_weight(self):
        r"""Gets the master_weight of this ModifyMySqlProxyRouteModeRequest.

        数据库主实例读权重。     - 当route_mode选择0（权重负载）时，该字段取值范围为0~1000。     - 当route_mode选择1或2（负载均衡）时，该字段不生效。

        :return: The master_weight of this ModifyMySqlProxyRouteModeRequest.
        :rtype: int
        """
        return self._master_weight

    @master_weight.setter
    def master_weight(self, master_weight):
        r"""Sets the master_weight of this ModifyMySqlProxyRouteModeRequest.

        数据库主实例读权重。     - 当route_mode选择0（权重负载）时，该字段取值范围为0~1000。     - 当route_mode选择1或2（负载均衡）时，该字段不生效。

        :param master_weight: The master_weight of this ModifyMySqlProxyRouteModeRequest.
        :type master_weight: int
        """
        self._master_weight = master_weight

    @property
    def readonly_instances(self):
        r"""Gets the readonly_instances of this ModifyMySqlProxyRouteModeRequest.

        数据库节点的读权重设置。      - 只能为只读实例选择权重。     - 该列表可以为空列表。

        :return: The readonly_instances of this ModifyMySqlProxyRouteModeRequest.
        :rtype: list[:class:`huaweicloudsdkrds.v3.InstancesWeight`]
        """
        return self._readonly_instances

    @readonly_instances.setter
    def readonly_instances(self, readonly_instances):
        r"""Sets the readonly_instances of this ModifyMySqlProxyRouteModeRequest.

        数据库节点的读权重设置。      - 只能为只读实例选择权重。     - 该列表可以为空列表。

        :param readonly_instances: The readonly_instances of this ModifyMySqlProxyRouteModeRequest.
        :type readonly_instances: list[:class:`huaweicloudsdkrds.v3.InstancesWeight`]
        """
        self._readonly_instances = readonly_instances

    @property
    def route_mode(self):
        r"""Gets the route_mode of this ModifyMySqlProxyRouteModeRequest.

        数据库代理路由模式。 取值范围:     0：表示权重负载模式。     1：表示负载均衡模式（数据库主实例不接受读请求）。     2：表示负载均衡模式（数据库主实例接受读请求）。      - 如需使用负载均衡模式，请联系客服申请

        :return: The route_mode of this ModifyMySqlProxyRouteModeRequest.
        :rtype: int
        """
        return self._route_mode

    @route_mode.setter
    def route_mode(self, route_mode):
        r"""Sets the route_mode of this ModifyMySqlProxyRouteModeRequest.

        数据库代理路由模式。 取值范围:     0：表示权重负载模式。     1：表示负载均衡模式（数据库主实例不接受读请求）。     2：表示负载均衡模式（数据库主实例接受读请求）。      - 如需使用负载均衡模式，请联系客服申请

        :param route_mode: The route_mode of this ModifyMySqlProxyRouteModeRequest.
        :type route_mode: int
        """
        self._route_mode = route_mode

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
        if not isinstance(other, ModifyMySqlProxyRouteModeRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
