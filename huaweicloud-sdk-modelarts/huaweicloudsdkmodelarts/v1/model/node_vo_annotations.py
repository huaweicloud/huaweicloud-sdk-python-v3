# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NodeVOAnnotations:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'os_modelarts_npu_topology_placement': 'str'
    }

    attribute_map = {
        'os_modelarts_npu_topology_placement': 'os.modelarts/npu-topology-placement'
    }

    def __init__(self, os_modelarts_npu_topology_placement=None):
        r"""NodeVOAnnotations

        The model defined in huaweicloud sdk

        :param os_modelarts_npu_topology_placement: **参数解释**：NPU卡的资源使用拓扑信息，长度为16的二进制编码，右起第一位编码代表卡1。其中，1表示占用，0表示空闲。例如，16卡的机型中卡1和卡15被占用，值为0100000000000001；8卡的机型中卡1和卡7被占用，返回值为0000000001000001。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type os_modelarts_npu_topology_placement: str
        """
        
        

        self._os_modelarts_npu_topology_placement = None
        self.discriminator = None

        if os_modelarts_npu_topology_placement is not None:
            self.os_modelarts_npu_topology_placement = os_modelarts_npu_topology_placement

    @property
    def os_modelarts_npu_topology_placement(self):
        r"""Gets the os_modelarts_npu_topology_placement of this NodeVOAnnotations.

        **参数解释**：NPU卡的资源使用拓扑信息，长度为16的二进制编码，右起第一位编码代表卡1。其中，1表示占用，0表示空闲。例如，16卡的机型中卡1和卡15被占用，值为0100000000000001；8卡的机型中卡1和卡7被占用，返回值为0000000001000001。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The os_modelarts_npu_topology_placement of this NodeVOAnnotations.
        :rtype: str
        """
        return self._os_modelarts_npu_topology_placement

    @os_modelarts_npu_topology_placement.setter
    def os_modelarts_npu_topology_placement(self, os_modelarts_npu_topology_placement):
        r"""Sets the os_modelarts_npu_topology_placement of this NodeVOAnnotations.

        **参数解释**：NPU卡的资源使用拓扑信息，长度为16的二进制编码，右起第一位编码代表卡1。其中，1表示占用，0表示空闲。例如，16卡的机型中卡1和卡15被占用，值为0100000000000001；8卡的机型中卡1和卡7被占用，返回值为0000000001000001。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param os_modelarts_npu_topology_placement: The os_modelarts_npu_topology_placement of this NodeVOAnnotations.
        :type os_modelarts_npu_topology_placement: str
        """
        self._os_modelarts_npu_topology_placement = os_modelarts_npu_topology_placement

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
        if not isinstance(other, NodeVOAnnotations):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
