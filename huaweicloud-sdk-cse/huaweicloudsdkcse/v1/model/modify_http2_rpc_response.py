# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModifyHttp2RpcResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'gateway_id': 'str',
        'plugin_config': 'object',
        'name': 'str',
        'route_name': 'str',
        'route_destination_name': 'str',
        'dubbo': 'Dubbo'
    }

    attribute_map = {
        'gateway_id': 'gatewayId',
        'plugin_config': 'pluginConfig',
        'name': 'name',
        'route_name': 'routeName',
        'route_destination_name': 'routeDestinationName',
        'dubbo': 'dubbo'
    }

    def __init__(self, gateway_id=None, plugin_config=None, name=None, route_name=None, route_destination_name=None, dubbo=None):
        """ModifyHttp2RpcResponse

        The model defined in huaweicloud sdk

        :param gateway_id: 网关的ID。
        :type gateway_id: str
        :param plugin_config: 传递给插件的配置。
        :type plugin_config: object
        :param name: 
        :type name: str
        :param route_name: 路由的名称。
        :type route_name: str
        :param route_destination_name: 目标路由的名称。
        :type route_destination_name: str
        :param dubbo: 
        :type dubbo: :class:`huaweicloudsdkcse.v1.Dubbo`
        """
        
        super(ModifyHttp2RpcResponse, self).__init__()

        self._gateway_id = None
        self._plugin_config = None
        self._name = None
        self._route_name = None
        self._route_destination_name = None
        self._dubbo = None
        self.discriminator = None

        if gateway_id is not None:
            self.gateway_id = gateway_id
        if plugin_config is not None:
            self.plugin_config = plugin_config
        if name is not None:
            self.name = name
        if route_name is not None:
            self.route_name = route_name
        if route_destination_name is not None:
            self.route_destination_name = route_destination_name
        if dubbo is not None:
            self.dubbo = dubbo

    @property
    def gateway_id(self):
        """Gets the gateway_id of this ModifyHttp2RpcResponse.

        网关的ID。

        :return: The gateway_id of this ModifyHttp2RpcResponse.
        :rtype: str
        """
        return self._gateway_id

    @gateway_id.setter
    def gateway_id(self, gateway_id):
        """Sets the gateway_id of this ModifyHttp2RpcResponse.

        网关的ID。

        :param gateway_id: The gateway_id of this ModifyHttp2RpcResponse.
        :type gateway_id: str
        """
        self._gateway_id = gateway_id

    @property
    def plugin_config(self):
        """Gets the plugin_config of this ModifyHttp2RpcResponse.

        传递给插件的配置。

        :return: The plugin_config of this ModifyHttp2RpcResponse.
        :rtype: object
        """
        return self._plugin_config

    @plugin_config.setter
    def plugin_config(self, plugin_config):
        """Sets the plugin_config of this ModifyHttp2RpcResponse.

        传递给插件的配置。

        :param plugin_config: The plugin_config of this ModifyHttp2RpcResponse.
        :type plugin_config: object
        """
        self._plugin_config = plugin_config

    @property
    def name(self):
        """Gets the name of this ModifyHttp2RpcResponse.

        :return: The name of this ModifyHttp2RpcResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ModifyHttp2RpcResponse.

        :param name: The name of this ModifyHttp2RpcResponse.
        :type name: str
        """
        self._name = name

    @property
    def route_name(self):
        """Gets the route_name of this ModifyHttp2RpcResponse.

        路由的名称。

        :return: The route_name of this ModifyHttp2RpcResponse.
        :rtype: str
        """
        return self._route_name

    @route_name.setter
    def route_name(self, route_name):
        """Sets the route_name of this ModifyHttp2RpcResponse.

        路由的名称。

        :param route_name: The route_name of this ModifyHttp2RpcResponse.
        :type route_name: str
        """
        self._route_name = route_name

    @property
    def route_destination_name(self):
        """Gets the route_destination_name of this ModifyHttp2RpcResponse.

        目标路由的名称。

        :return: The route_destination_name of this ModifyHttp2RpcResponse.
        :rtype: str
        """
        return self._route_destination_name

    @route_destination_name.setter
    def route_destination_name(self, route_destination_name):
        """Sets the route_destination_name of this ModifyHttp2RpcResponse.

        目标路由的名称。

        :param route_destination_name: The route_destination_name of this ModifyHttp2RpcResponse.
        :type route_destination_name: str
        """
        self._route_destination_name = route_destination_name

    @property
    def dubbo(self):
        """Gets the dubbo of this ModifyHttp2RpcResponse.

        :return: The dubbo of this ModifyHttp2RpcResponse.
        :rtype: :class:`huaweicloudsdkcse.v1.Dubbo`
        """
        return self._dubbo

    @dubbo.setter
    def dubbo(self, dubbo):
        """Sets the dubbo of this ModifyHttp2RpcResponse.

        :param dubbo: The dubbo of this ModifyHttp2RpcResponse.
        :type dubbo: :class:`huaweicloudsdkcse.v1.Dubbo`
        """
        self._dubbo = dubbo

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
        if not isinstance(other, ModifyHttp2RpcResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
