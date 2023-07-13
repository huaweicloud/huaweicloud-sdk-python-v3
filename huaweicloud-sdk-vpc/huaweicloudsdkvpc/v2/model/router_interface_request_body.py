# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RouterInterfaceRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'port_id': 'str',
        'subnet_id': 'str'
    }

    attribute_map = {
        'port_id': 'port_id',
        'subnet_id': 'subnet_id'
    }

    def __init__(self, port_id=None, subnet_id=None):
        """RouterInterfaceRequestBody

        The model defined in huaweicloud sdk

        :param port_id: 功能说明：路由器添加（或删除）接口请求参数port对应的id 约束：  - 使用端口的时候，端口上有且只有一个IP地址  - subnet_id与port_id其中之一必须指定
        :type port_id: str
        :param subnet_id: 功能说明：路由器添加（或删除）接口请求参数subnet对应的id 约束：  - 使用子网的时候，子网上必须配置gatewayIP地址  - \&quot;provider:network_type\&quot;为\&quot;geneve\&quot;的网络不可以添加路由器  - subnet_id与port_id其中之一必须指定。
        :type subnet_id: str
        """
        
        

        self._port_id = None
        self._subnet_id = None
        self.discriminator = None

        if port_id is not None:
            self.port_id = port_id
        if subnet_id is not None:
            self.subnet_id = subnet_id

    @property
    def port_id(self):
        """Gets the port_id of this RouterInterfaceRequestBody.

        功能说明：路由器添加（或删除）接口请求参数port对应的id 约束：  - 使用端口的时候，端口上有且只有一个IP地址  - subnet_id与port_id其中之一必须指定

        :return: The port_id of this RouterInterfaceRequestBody.
        :rtype: str
        """
        return self._port_id

    @port_id.setter
    def port_id(self, port_id):
        """Sets the port_id of this RouterInterfaceRequestBody.

        功能说明：路由器添加（或删除）接口请求参数port对应的id 约束：  - 使用端口的时候，端口上有且只有一个IP地址  - subnet_id与port_id其中之一必须指定

        :param port_id: The port_id of this RouterInterfaceRequestBody.
        :type port_id: str
        """
        self._port_id = port_id

    @property
    def subnet_id(self):
        """Gets the subnet_id of this RouterInterfaceRequestBody.

        功能说明：路由器添加（或删除）接口请求参数subnet对应的id 约束：  - 使用子网的时候，子网上必须配置gatewayIP地址  - \"provider:network_type\"为\"geneve\"的网络不可以添加路由器  - subnet_id与port_id其中之一必须指定。

        :return: The subnet_id of this RouterInterfaceRequestBody.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this RouterInterfaceRequestBody.

        功能说明：路由器添加（或删除）接口请求参数subnet对应的id 约束：  - 使用子网的时候，子网上必须配置gatewayIP地址  - \"provider:network_type\"为\"geneve\"的网络不可以添加路由器  - subnet_id与port_id其中之一必须指定。

        :param subnet_id: The subnet_id of this RouterInterfaceRequestBody.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

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
        if not isinstance(other, RouterInterfaceRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
