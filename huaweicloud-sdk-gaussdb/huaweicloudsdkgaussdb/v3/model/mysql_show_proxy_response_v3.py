# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MysqlShowProxyResponseV3:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'proxy': 'MysqlProxyV3',
        'master_node': 'MysqlProxyNodeV3',
        'readonly_nodes': 'list[MysqlProxyNodeV3]'
    }

    attribute_map = {
        'proxy': 'proxy',
        'master_node': 'master_node',
        'readonly_nodes': 'readonly_nodes'
    }

    def __init__(self, proxy=None, master_node=None, readonly_nodes=None):
        """MysqlShowProxyResponseV3

        The model defined in huaweicloud sdk

        :param proxy: 
        :type proxy: :class:`huaweicloudsdkgaussdb.v3.MysqlProxyV3`
        :param master_node: 
        :type master_node: :class:`huaweicloudsdkgaussdb.v3.MysqlProxyNodeV3`
        :param readonly_nodes: 只读节点信息。
        :type readonly_nodes: list[:class:`huaweicloudsdkgaussdb.v3.MysqlProxyNodeV3`]
        """
        
        

        self._proxy = None
        self._master_node = None
        self._readonly_nodes = None
        self.discriminator = None

        if proxy is not None:
            self.proxy = proxy
        if master_node is not None:
            self.master_node = master_node
        if readonly_nodes is not None:
            self.readonly_nodes = readonly_nodes

    @property
    def proxy(self):
        """Gets the proxy of this MysqlShowProxyResponseV3.


        :return: The proxy of this MysqlShowProxyResponseV3.
        :rtype: :class:`huaweicloudsdkgaussdb.v3.MysqlProxyV3`
        """
        return self._proxy

    @proxy.setter
    def proxy(self, proxy):
        """Sets the proxy of this MysqlShowProxyResponseV3.


        :param proxy: The proxy of this MysqlShowProxyResponseV3.
        :type proxy: :class:`huaweicloudsdkgaussdb.v3.MysqlProxyV3`
        """
        self._proxy = proxy

    @property
    def master_node(self):
        """Gets the master_node of this MysqlShowProxyResponseV3.


        :return: The master_node of this MysqlShowProxyResponseV3.
        :rtype: :class:`huaweicloudsdkgaussdb.v3.MysqlProxyNodeV3`
        """
        return self._master_node

    @master_node.setter
    def master_node(self, master_node):
        """Sets the master_node of this MysqlShowProxyResponseV3.


        :param master_node: The master_node of this MysqlShowProxyResponseV3.
        :type master_node: :class:`huaweicloudsdkgaussdb.v3.MysqlProxyNodeV3`
        """
        self._master_node = master_node

    @property
    def readonly_nodes(self):
        """Gets the readonly_nodes of this MysqlShowProxyResponseV3.

        只读节点信息。

        :return: The readonly_nodes of this MysqlShowProxyResponseV3.
        :rtype: list[:class:`huaweicloudsdkgaussdb.v3.MysqlProxyNodeV3`]
        """
        return self._readonly_nodes

    @readonly_nodes.setter
    def readonly_nodes(self, readonly_nodes):
        """Sets the readonly_nodes of this MysqlShowProxyResponseV3.

        只读节点信息。

        :param readonly_nodes: The readonly_nodes of this MysqlShowProxyResponseV3.
        :type readonly_nodes: list[:class:`huaweicloudsdkgaussdb.v3.MysqlProxyNodeV3`]
        """
        self._readonly_nodes = readonly_nodes

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
        if not isinstance(other, MysqlShowProxyResponseV3):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
