# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DimChild:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'dim_name': 'str',
        'dim_route': 'str'
    }

    attribute_map = {
        'dim_name': 'dim_name',
        'dim_route': 'dim_route'
    }

    def __init__(self, dim_name=None, dim_route=None):
        """DimChild

        The model defined in huaweicloud sdk

        :param dim_name: 维度名称，当前支持维度有dcs_instance_id、dcs_cluster_redis_node、 dcs_cluster_proxy_node和dcs_memcached_instance_id。
        :type dim_name: str
        :param dim_route: 维度的路由，结构为主维度名称,当前维度名称，比如： dim_name字段为dcs_cluster_redis_node时，这个字段的值为dcs_instance_id,dcs_cluster_redis_node。
        :type dim_route: str
        """
        
        

        self._dim_name = None
        self._dim_route = None
        self.discriminator = None

        if dim_name is not None:
            self.dim_name = dim_name
        if dim_route is not None:
            self.dim_route = dim_route

    @property
    def dim_name(self):
        """Gets the dim_name of this DimChild.

        维度名称，当前支持维度有dcs_instance_id、dcs_cluster_redis_node、 dcs_cluster_proxy_node和dcs_memcached_instance_id。

        :return: The dim_name of this DimChild.
        :rtype: str
        """
        return self._dim_name

    @dim_name.setter
    def dim_name(self, dim_name):
        """Sets the dim_name of this DimChild.

        维度名称，当前支持维度有dcs_instance_id、dcs_cluster_redis_node、 dcs_cluster_proxy_node和dcs_memcached_instance_id。

        :param dim_name: The dim_name of this DimChild.
        :type dim_name: str
        """
        self._dim_name = dim_name

    @property
    def dim_route(self):
        """Gets the dim_route of this DimChild.

        维度的路由，结构为主维度名称,当前维度名称，比如： dim_name字段为dcs_cluster_redis_node时，这个字段的值为dcs_instance_id,dcs_cluster_redis_node。

        :return: The dim_route of this DimChild.
        :rtype: str
        """
        return self._dim_route

    @dim_route.setter
    def dim_route(self, dim_route):
        """Sets the dim_route of this DimChild.

        维度的路由，结构为主维度名称,当前维度名称，比如： dim_name字段为dcs_cluster_redis_node时，这个字段的值为dcs_instance_id,dcs_cluster_redis_node。

        :param dim_route: The dim_route of this DimChild.
        :type dim_route: str
        """
        self._dim_route = dim_route

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
        if not isinstance(other, DimChild):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
