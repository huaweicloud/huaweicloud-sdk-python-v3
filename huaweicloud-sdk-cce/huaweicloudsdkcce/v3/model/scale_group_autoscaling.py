# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ScaleGroupAutoscaling:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enable': 'bool',
        'extension_priority': 'int',
        'min_node_count': 'int',
        'max_node_count': 'int'
    }

    attribute_map = {
        'enable': 'enable',
        'extension_priority': 'extensionPriority',
        'min_node_count': 'minNodeCount',
        'max_node_count': 'maxNodeCount'
    }

    def __init__(self, enable=None, extension_priority=None, min_node_count=None, max_node_count=None):
        r"""ScaleGroupAutoscaling

        The model defined in huaweicloud sdk

        :param enable: 伸缩组弹性扩缩容启用开关，默认不开启
        :type enable: bool
        :param extension_priority: 伸缩组优先级，未设置则默认为0，数值越大优先级越高
        :type extension_priority: int
        :param min_node_count: 弹性伸缩时，伸缩组最少应保持的节点数量，必须大于0
        :type min_node_count: int
        :param max_node_count: 弹性伸缩时，伸缩组最多可保持的节点数量，应大于等于 **minNodeCount**, 不可大于集群规格所允许的节点上限，不可大于节点池节点数量上限
        :type max_node_count: int
        """
        
        

        self._enable = None
        self._extension_priority = None
        self._min_node_count = None
        self._max_node_count = None
        self.discriminator = None

        if enable is not None:
            self.enable = enable
        if extension_priority is not None:
            self.extension_priority = extension_priority
        if min_node_count is not None:
            self.min_node_count = min_node_count
        if max_node_count is not None:
            self.max_node_count = max_node_count

    @property
    def enable(self):
        r"""Gets the enable of this ScaleGroupAutoscaling.

        伸缩组弹性扩缩容启用开关，默认不开启

        :return: The enable of this ScaleGroupAutoscaling.
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        r"""Sets the enable of this ScaleGroupAutoscaling.

        伸缩组弹性扩缩容启用开关，默认不开启

        :param enable: The enable of this ScaleGroupAutoscaling.
        :type enable: bool
        """
        self._enable = enable

    @property
    def extension_priority(self):
        r"""Gets the extension_priority of this ScaleGroupAutoscaling.

        伸缩组优先级，未设置则默认为0，数值越大优先级越高

        :return: The extension_priority of this ScaleGroupAutoscaling.
        :rtype: int
        """
        return self._extension_priority

    @extension_priority.setter
    def extension_priority(self, extension_priority):
        r"""Sets the extension_priority of this ScaleGroupAutoscaling.

        伸缩组优先级，未设置则默认为0，数值越大优先级越高

        :param extension_priority: The extension_priority of this ScaleGroupAutoscaling.
        :type extension_priority: int
        """
        self._extension_priority = extension_priority

    @property
    def min_node_count(self):
        r"""Gets the min_node_count of this ScaleGroupAutoscaling.

        弹性伸缩时，伸缩组最少应保持的节点数量，必须大于0

        :return: The min_node_count of this ScaleGroupAutoscaling.
        :rtype: int
        """
        return self._min_node_count

    @min_node_count.setter
    def min_node_count(self, min_node_count):
        r"""Sets the min_node_count of this ScaleGroupAutoscaling.

        弹性伸缩时，伸缩组最少应保持的节点数量，必须大于0

        :param min_node_count: The min_node_count of this ScaleGroupAutoscaling.
        :type min_node_count: int
        """
        self._min_node_count = min_node_count

    @property
    def max_node_count(self):
        r"""Gets the max_node_count of this ScaleGroupAutoscaling.

        弹性伸缩时，伸缩组最多可保持的节点数量，应大于等于 **minNodeCount**, 不可大于集群规格所允许的节点上限，不可大于节点池节点数量上限

        :return: The max_node_count of this ScaleGroupAutoscaling.
        :rtype: int
        """
        return self._max_node_count

    @max_node_count.setter
    def max_node_count(self, max_node_count):
        r"""Sets the max_node_count of this ScaleGroupAutoscaling.

        弹性伸缩时，伸缩组最多可保持的节点数量，应大于等于 **minNodeCount**, 不可大于集群规格所允许的节点上限，不可大于节点池节点数量上限

        :param max_node_count: The max_node_count of this ScaleGroupAutoscaling.
        :type max_node_count: int
        """
        self._max_node_count = max_node_count

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
        if not isinstance(other, ScaleGroupAutoscaling):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
