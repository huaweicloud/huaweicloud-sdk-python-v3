# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OpenMysqlProxyRequestBody:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'flavor_ref': 'str',
        'node_num': 'int'
    }

    attribute_map = {
        'flavor_ref': 'flavor_ref',
        'node_num': 'node_num'
    }

    def __init__(self, flavor_ref=None, node_num=None):
        """OpenMysqlProxyRequestBody - a model defined in huaweicloud sdk"""
        
        

        self._flavor_ref = None
        self._node_num = None
        self.discriminator = None

        if flavor_ref is not None:
            self.flavor_ref = flavor_ref
        if node_num is not None:
            self.node_num = node_num

    @property
    def flavor_ref(self):
        """Gets the flavor_ref of this OpenMysqlProxyRequestBody.

        代理规格码。

        :return: The flavor_ref of this OpenMysqlProxyRequestBody.
        :rtype: str
        """
        return self._flavor_ref

    @flavor_ref.setter
    def flavor_ref(self, flavor_ref):
        """Sets the flavor_ref of this OpenMysqlProxyRequestBody.

        代理规格码。

        :param flavor_ref: The flavor_ref of this OpenMysqlProxyRequestBody.
        :type: str
        """
        self._flavor_ref = flavor_ref

    @property
    def node_num(self):
        """Gets the node_num of this OpenMysqlProxyRequestBody.

        代理实例节点数，取值整数2-32。

        :return: The node_num of this OpenMysqlProxyRequestBody.
        :rtype: int
        """
        return self._node_num

    @node_num.setter
    def node_num(self, node_num):
        """Sets the node_num of this OpenMysqlProxyRequestBody.

        代理实例节点数，取值整数2-32。

        :param node_num: The node_num of this OpenMysqlProxyRequestBody.
        :type: int
        """
        self._node_num = node_num

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
        if not isinstance(other, OpenMysqlProxyRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
