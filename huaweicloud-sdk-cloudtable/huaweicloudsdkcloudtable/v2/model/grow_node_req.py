# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GrowNodeReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'component_name': 'str',
        'node_num': 'int'
    }

    attribute_map = {
        'component_name': 'component_name',
        'node_num': 'node_num'
    }

    def __init__(self, component_name=None, node_num=None):
        r"""GrowNodeReq

        The model defined in huaweicloud sdk

        :param component_name: 扩容节点类型：rs,tsdb,lemon
        :type component_name: str
        :param node_num: 扩容节点范围是 [2,10]
        :type node_num: int
        """
        
        

        self._component_name = None
        self._node_num = None
        self.discriminator = None

        self.component_name = component_name
        self.node_num = node_num

    @property
    def component_name(self):
        r"""Gets the component_name of this GrowNodeReq.

        扩容节点类型：rs,tsdb,lemon

        :return: The component_name of this GrowNodeReq.
        :rtype: str
        """
        return self._component_name

    @component_name.setter
    def component_name(self, component_name):
        r"""Sets the component_name of this GrowNodeReq.

        扩容节点类型：rs,tsdb,lemon

        :param component_name: The component_name of this GrowNodeReq.
        :type component_name: str
        """
        self._component_name = component_name

    @property
    def node_num(self):
        r"""Gets the node_num of this GrowNodeReq.

        扩容节点范围是 [2,10]

        :return: The node_num of this GrowNodeReq.
        :rtype: int
        """
        return self._node_num

    @node_num.setter
    def node_num(self, node_num):
        r"""Sets the node_num of this GrowNodeReq.

        扩容节点范围是 [2,10]

        :param node_num: The node_num of this GrowNodeReq.
        :type node_num: int
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
        if not isinstance(other, GrowNodeReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
