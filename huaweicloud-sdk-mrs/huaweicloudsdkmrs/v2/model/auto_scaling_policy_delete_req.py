# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AutoScalingPolicyDeleteReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'node_group_name': 'str',
        'resource_pool_name': 'str'
    }

    attribute_map = {
        'node_group_name': 'node_group_name',
        'resource_pool_name': 'resource_pool_name'
    }

    def __init__(self, node_group_name=None, resource_pool_name=None):
        r"""AutoScalingPolicyDeleteReq

        The model defined in huaweicloud sdk

        :param node_group_name: 节点组名称。如果resource_pool_name为default，则删除节点组维度的弹性伸缩策略。如果resource_pool_name不为default，则在该节点组下删除对应资源池维度的策略。
        :type node_group_name: str
        :param resource_pool_name: 资源池名称。当集群版本不支持按指定资源池进行弹性伸缩时，需要填写为default资源池。不为default时删除指定资源池维度的弹性伸缩策略。
        :type resource_pool_name: str
        """
        
        

        self._node_group_name = None
        self._resource_pool_name = None
        self.discriminator = None

        self.node_group_name = node_group_name
        self.resource_pool_name = resource_pool_name

    @property
    def node_group_name(self):
        r"""Gets the node_group_name of this AutoScalingPolicyDeleteReq.

        节点组名称。如果resource_pool_name为default，则删除节点组维度的弹性伸缩策略。如果resource_pool_name不为default，则在该节点组下删除对应资源池维度的策略。

        :return: The node_group_name of this AutoScalingPolicyDeleteReq.
        :rtype: str
        """
        return self._node_group_name

    @node_group_name.setter
    def node_group_name(self, node_group_name):
        r"""Sets the node_group_name of this AutoScalingPolicyDeleteReq.

        节点组名称。如果resource_pool_name为default，则删除节点组维度的弹性伸缩策略。如果resource_pool_name不为default，则在该节点组下删除对应资源池维度的策略。

        :param node_group_name: The node_group_name of this AutoScalingPolicyDeleteReq.
        :type node_group_name: str
        """
        self._node_group_name = node_group_name

    @property
    def resource_pool_name(self):
        r"""Gets the resource_pool_name of this AutoScalingPolicyDeleteReq.

        资源池名称。当集群版本不支持按指定资源池进行弹性伸缩时，需要填写为default资源池。不为default时删除指定资源池维度的弹性伸缩策略。

        :return: The resource_pool_name of this AutoScalingPolicyDeleteReq.
        :rtype: str
        """
        return self._resource_pool_name

    @resource_pool_name.setter
    def resource_pool_name(self, resource_pool_name):
        r"""Sets the resource_pool_name of this AutoScalingPolicyDeleteReq.

        资源池名称。当集群版本不支持按指定资源池进行弹性伸缩时，需要填写为default资源池。不为default时删除指定资源池维度的弹性伸缩策略。

        :param resource_pool_name: The resource_pool_name of this AutoScalingPolicyDeleteReq.
        :type resource_pool_name: str
        """
        self._resource_pool_name = resource_pool_name

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
        if not isinstance(other, AutoScalingPolicyDeleteReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
