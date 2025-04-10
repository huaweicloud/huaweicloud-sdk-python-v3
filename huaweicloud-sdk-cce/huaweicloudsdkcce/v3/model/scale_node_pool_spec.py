# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ScaleNodePoolSpec:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'desired_node_count': 'int',
        'scale_groups': 'list[str]',
        'options': 'ScaleNodePoolOptions'
    }

    attribute_map = {
        'desired_node_count': 'desiredNodeCount',
        'scale_groups': 'scaleGroups',
        'options': 'options'
    }

    def __init__(self, desired_node_count=None, scale_groups=None, options=None):
        r"""ScaleNodePoolSpec

        The model defined in huaweicloud sdk

        :param desired_node_count: 节点池期望节点数
        :type desired_node_count: int
        :param scale_groups: 扩缩容的节点池，只能填一个伸缩组，如果要伸缩默认伸缩组填default
        :type scale_groups: list[str]
        :param options: 
        :type options: :class:`huaweicloudsdkcce.v3.ScaleNodePoolOptions`
        """
        
        

        self._desired_node_count = None
        self._scale_groups = None
        self._options = None
        self.discriminator = None

        self.desired_node_count = desired_node_count
        self.scale_groups = scale_groups
        if options is not None:
            self.options = options

    @property
    def desired_node_count(self):
        r"""Gets the desired_node_count of this ScaleNodePoolSpec.

        节点池期望节点数

        :return: The desired_node_count of this ScaleNodePoolSpec.
        :rtype: int
        """
        return self._desired_node_count

    @desired_node_count.setter
    def desired_node_count(self, desired_node_count):
        r"""Sets the desired_node_count of this ScaleNodePoolSpec.

        节点池期望节点数

        :param desired_node_count: The desired_node_count of this ScaleNodePoolSpec.
        :type desired_node_count: int
        """
        self._desired_node_count = desired_node_count

    @property
    def scale_groups(self):
        r"""Gets the scale_groups of this ScaleNodePoolSpec.

        扩缩容的节点池，只能填一个伸缩组，如果要伸缩默认伸缩组填default

        :return: The scale_groups of this ScaleNodePoolSpec.
        :rtype: list[str]
        """
        return self._scale_groups

    @scale_groups.setter
    def scale_groups(self, scale_groups):
        r"""Sets the scale_groups of this ScaleNodePoolSpec.

        扩缩容的节点池，只能填一个伸缩组，如果要伸缩默认伸缩组填default

        :param scale_groups: The scale_groups of this ScaleNodePoolSpec.
        :type scale_groups: list[str]
        """
        self._scale_groups = scale_groups

    @property
    def options(self):
        r"""Gets the options of this ScaleNodePoolSpec.

        :return: The options of this ScaleNodePoolSpec.
        :rtype: :class:`huaweicloudsdkcce.v3.ScaleNodePoolOptions`
        """
        return self._options

    @options.setter
    def options(self, options):
        r"""Sets the options of this ScaleNodePoolSpec.

        :param options: The options of this ScaleNodePoolSpec.
        :type options: :class:`huaweicloudsdkcce.v3.ScaleNodePoolOptions`
        """
        self._options = options

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
        if not isinstance(other, ScaleNodePoolSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
