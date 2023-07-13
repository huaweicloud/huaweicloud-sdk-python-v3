# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WeightPodAffinityTermsPodAffinityTerm:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'label_selector': 'LabelSelector',
        'namespaces': 'list[str]',
        'topology_key': 'str'
    }

    attribute_map = {
        'label_selector': 'labelSelector',
        'namespaces': 'namespaces',
        'topology_key': 'topologyKey'
    }

    def __init__(self, label_selector=None, namespaces=None, topology_key=None):
        """WeightPodAffinityTermsPodAffinityTerm

        The model defined in huaweicloud sdk

        :param label_selector: 
        :type label_selector: :class:`huaweicloudsdkief.v1.LabelSelector`
        :param namespaces: 命名空间
        :type namespaces: list[str]
        :param topology_key: 拓扑标签。先圈定topologyKey指定的范围，然后再选择labelSelector定义的内容，即亲和调度只会在有topologyKey指定的标签节点上调度。
        :type topology_key: str
        """
        
        

        self._label_selector = None
        self._namespaces = None
        self._topology_key = None
        self.discriminator = None

        if label_selector is not None:
            self.label_selector = label_selector
        if namespaces is not None:
            self.namespaces = namespaces
        if topology_key is not None:
            self.topology_key = topology_key

    @property
    def label_selector(self):
        """Gets the label_selector of this WeightPodAffinityTermsPodAffinityTerm.

        :return: The label_selector of this WeightPodAffinityTermsPodAffinityTerm.
        :rtype: :class:`huaweicloudsdkief.v1.LabelSelector`
        """
        return self._label_selector

    @label_selector.setter
    def label_selector(self, label_selector):
        """Sets the label_selector of this WeightPodAffinityTermsPodAffinityTerm.

        :param label_selector: The label_selector of this WeightPodAffinityTermsPodAffinityTerm.
        :type label_selector: :class:`huaweicloudsdkief.v1.LabelSelector`
        """
        self._label_selector = label_selector

    @property
    def namespaces(self):
        """Gets the namespaces of this WeightPodAffinityTermsPodAffinityTerm.

        命名空间

        :return: The namespaces of this WeightPodAffinityTermsPodAffinityTerm.
        :rtype: list[str]
        """
        return self._namespaces

    @namespaces.setter
    def namespaces(self, namespaces):
        """Sets the namespaces of this WeightPodAffinityTermsPodAffinityTerm.

        命名空间

        :param namespaces: The namespaces of this WeightPodAffinityTermsPodAffinityTerm.
        :type namespaces: list[str]
        """
        self._namespaces = namespaces

    @property
    def topology_key(self):
        """Gets the topology_key of this WeightPodAffinityTermsPodAffinityTerm.

        拓扑标签。先圈定topologyKey指定的范围，然后再选择labelSelector定义的内容，即亲和调度只会在有topologyKey指定的标签节点上调度。

        :return: The topology_key of this WeightPodAffinityTermsPodAffinityTerm.
        :rtype: str
        """
        return self._topology_key

    @topology_key.setter
    def topology_key(self, topology_key):
        """Sets the topology_key of this WeightPodAffinityTermsPodAffinityTerm.

        拓扑标签。先圈定topologyKey指定的范围，然后再选择labelSelector定义的内容，即亲和调度只会在有topologyKey指定的标签节点上调度。

        :param topology_key: The topology_key of this WeightPodAffinityTermsPodAffinityTerm.
        :type topology_key: str
        """
        self._topology_key = topology_key

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
        if not isinstance(other, WeightPodAffinityTermsPodAffinityTerm):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
