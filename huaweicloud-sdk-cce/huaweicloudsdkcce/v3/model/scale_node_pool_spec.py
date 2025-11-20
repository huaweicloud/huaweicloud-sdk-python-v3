# coding: utf-8

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

        :param desired_node_count: **参数解释**： 节点池的预期总数量。执行扩容操作时，需将当前节点数与扩容数量相加；执行缩容操作时，需从当前节点数中减去缩容数量。 **约束限制**： 必填参数，如果省略则默认值为0，会导致删除节点池伸缩组下的所有节点 **取值范围**： 0或正整数 **默认取值**： 0
        :type desired_node_count: int
        :param scale_groups: **参数解释**： 要扩缩容的节点池中的伸缩组名称，通过[获取指定的节点池](cce_02_0355.xml)接口获取伸缩组名称。扩容时可选择多个伸缩组，系统将按照尽量均分或随机策略在所选伸缩组间分配扩容节点数，缩容时则仅能指定单个伸缩组进行操作。 **约束限制**： 如果要伸缩默认伸缩组填\&quot;default\&quot; **取值范围**： 不涉及 **默认取值**： 不涉及
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

        **参数解释**： 节点池的预期总数量。执行扩容操作时，需将当前节点数与扩容数量相加；执行缩容操作时，需从当前节点数中减去缩容数量。 **约束限制**： 必填参数，如果省略则默认值为0，会导致删除节点池伸缩组下的所有节点 **取值范围**： 0或正整数 **默认取值**： 0

        :return: The desired_node_count of this ScaleNodePoolSpec.
        :rtype: int
        """
        return self._desired_node_count

    @desired_node_count.setter
    def desired_node_count(self, desired_node_count):
        r"""Sets the desired_node_count of this ScaleNodePoolSpec.

        **参数解释**： 节点池的预期总数量。执行扩容操作时，需将当前节点数与扩容数量相加；执行缩容操作时，需从当前节点数中减去缩容数量。 **约束限制**： 必填参数，如果省略则默认值为0，会导致删除节点池伸缩组下的所有节点 **取值范围**： 0或正整数 **默认取值**： 0

        :param desired_node_count: The desired_node_count of this ScaleNodePoolSpec.
        :type desired_node_count: int
        """
        self._desired_node_count = desired_node_count

    @property
    def scale_groups(self):
        r"""Gets the scale_groups of this ScaleNodePoolSpec.

        **参数解释**： 要扩缩容的节点池中的伸缩组名称，通过[获取指定的节点池](cce_02_0355.xml)接口获取伸缩组名称。扩容时可选择多个伸缩组，系统将按照尽量均分或随机策略在所选伸缩组间分配扩容节点数，缩容时则仅能指定单个伸缩组进行操作。 **约束限制**： 如果要伸缩默认伸缩组填\"default\" **取值范围**： 不涉及 **默认取值**： 不涉及

        :return: The scale_groups of this ScaleNodePoolSpec.
        :rtype: list[str]
        """
        return self._scale_groups

    @scale_groups.setter
    def scale_groups(self, scale_groups):
        r"""Sets the scale_groups of this ScaleNodePoolSpec.

        **参数解释**： 要扩缩容的节点池中的伸缩组名称，通过[获取指定的节点池](cce_02_0355.xml)接口获取伸缩组名称。扩容时可选择多个伸缩组，系统将按照尽量均分或随机策略在所选伸缩组间分配扩容节点数，缩容时则仅能指定单个伸缩组进行操作。 **约束限制**： 如果要伸缩默认伸缩组填\"default\" **取值范围**： 不涉及 **默认取值**： 不涉及

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
        result = {}

        for attr, _ in self.openapi_types.items():
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
