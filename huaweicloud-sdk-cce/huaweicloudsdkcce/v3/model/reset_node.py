# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResetNode:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'node_id': 'str',
        'spec': 'ReinstallNodeSpec'
    }

    attribute_map = {
        'node_id': 'nodeID',
        'spec': 'spec'
    }

    def __init__(self, node_id=None, spec=None):
        """ResetNode

        The model defined in huaweicloud sdk

        :param node_id: 节点ID，获取方式请参见[如何获取接口URI中参数](cce_02_0271.xml)。
        :type node_id: str
        :param spec: 
        :type spec: :class:`huaweicloudsdkcce.v3.ReinstallNodeSpec`
        """
        
        

        self._node_id = None
        self._spec = None
        self.discriminator = None

        self.node_id = node_id
        self.spec = spec

    @property
    def node_id(self):
        """Gets the node_id of this ResetNode.

        节点ID，获取方式请参见[如何获取接口URI中参数](cce_02_0271.xml)。

        :return: The node_id of this ResetNode.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this ResetNode.

        节点ID，获取方式请参见[如何获取接口URI中参数](cce_02_0271.xml)。

        :param node_id: The node_id of this ResetNode.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def spec(self):
        """Gets the spec of this ResetNode.

        :return: The spec of this ResetNode.
        :rtype: :class:`huaweicloudsdkcce.v3.ReinstallNodeSpec`
        """
        return self._spec

    @spec.setter
    def spec(self, spec):
        """Sets the spec of this ResetNode.

        :param spec: The spec of this ResetNode.
        :type spec: :class:`huaweicloudsdkcce.v3.ReinstallNodeSpec`
        """
        self._spec = spec

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
        if not isinstance(other, ResetNode):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
