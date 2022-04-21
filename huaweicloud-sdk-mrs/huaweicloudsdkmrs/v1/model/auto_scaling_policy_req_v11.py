# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AutoScalingPolicyReqV11:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'node_group': 'str',
        'auto_scaling_policy': 'AutoScalingPolicy'
    }

    attribute_map = {
        'node_group': 'node_group',
        'auto_scaling_policy': 'auto_scaling_policy'
    }

    def __init__(self, node_group=None, auto_scaling_policy=None):
        """AutoScalingPolicyReqV11

        The model defined in huaweicloud sdk

        :param node_group: 弹性伸缩规则适用的节点类型，当前只支持task节点。
        :type node_group: str
        :param auto_scaling_policy: 
        :type auto_scaling_policy: :class:`huaweicloudsdkmrs.v1.AutoScalingPolicy`
        """
        
        

        self._node_group = None
        self._auto_scaling_policy = None
        self.discriminator = None

        self.node_group = node_group
        self.auto_scaling_policy = auto_scaling_policy

    @property
    def node_group(self):
        """Gets the node_group of this AutoScalingPolicyReqV11.

        弹性伸缩规则适用的节点类型，当前只支持task节点。

        :return: The node_group of this AutoScalingPolicyReqV11.
        :rtype: str
        """
        return self._node_group

    @node_group.setter
    def node_group(self, node_group):
        """Sets the node_group of this AutoScalingPolicyReqV11.

        弹性伸缩规则适用的节点类型，当前只支持task节点。

        :param node_group: The node_group of this AutoScalingPolicyReqV11.
        :type node_group: str
        """
        self._node_group = node_group

    @property
    def auto_scaling_policy(self):
        """Gets the auto_scaling_policy of this AutoScalingPolicyReqV11.


        :return: The auto_scaling_policy of this AutoScalingPolicyReqV11.
        :rtype: :class:`huaweicloudsdkmrs.v1.AutoScalingPolicy`
        """
        return self._auto_scaling_policy

    @auto_scaling_policy.setter
    def auto_scaling_policy(self, auto_scaling_policy):
        """Sets the auto_scaling_policy of this AutoScalingPolicyReqV11.


        :param auto_scaling_policy: The auto_scaling_policy of this AutoScalingPolicyReqV11.
        :type auto_scaling_policy: :class:`huaweicloudsdkmrs.v1.AutoScalingPolicy`
        """
        self._auto_scaling_policy = auto_scaling_policy

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
        if not isinstance(other, AutoScalingPolicyReqV11):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
