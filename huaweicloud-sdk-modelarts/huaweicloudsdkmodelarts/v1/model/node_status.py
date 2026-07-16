# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NodeStatus:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'phase': 'str',
        'az': 'str',
        'private_ip': 'str',
        'resources': 'NodeResource',
        'available_resources': 'NodeResource'
    }

    attribute_map = {
        'phase': 'phase',
        'az': 'az',
        'private_ip': 'privateIp',
        'resources': 'resources',
        'available_resources': 'availableResources'
    }

    def __init__(self, phase=None, az=None, private_ip=None, resources=None, available_resources=None):
        r"""NodeStatus

        The model defined in huaweicloud sdk

        :param phase: **参数解释**：节点当前状态。 **取值范围**：可选值如下： - Available：节点可用。 - Creating：节点创建中。 - Deleting：节点删除中。 - Abnormal：节点异常。 - Checking: 节点自检中。
        :type phase: str
        :param az: **参数解释**：节点所在的az。 **取值范围**：不涉及。
        :type az: str
        :param private_ip: **参数解释**：节点的IP地址。 **取值范围**：不涉及。
        :type private_ip: str
        :param resources: 
        :type resources: :class:`huaweicloudsdkmodelarts.v1.NodeResource`
        :param available_resources: 
        :type available_resources: :class:`huaweicloudsdkmodelarts.v1.NodeResource`
        """
        
        

        self._phase = None
        self._az = None
        self._private_ip = None
        self._resources = None
        self._available_resources = None
        self.discriminator = None

        self.phase = phase
        if az is not None:
            self.az = az
        if private_ip is not None:
            self.private_ip = private_ip
        self.resources = resources
        self.available_resources = available_resources

    @property
    def phase(self):
        r"""Gets the phase of this NodeStatus.

        **参数解释**：节点当前状态。 **取值范围**：可选值如下： - Available：节点可用。 - Creating：节点创建中。 - Deleting：节点删除中。 - Abnormal：节点异常。 - Checking: 节点自检中。

        :return: The phase of this NodeStatus.
        :rtype: str
        """
        return self._phase

    @phase.setter
    def phase(self, phase):
        r"""Sets the phase of this NodeStatus.

        **参数解释**：节点当前状态。 **取值范围**：可选值如下： - Available：节点可用。 - Creating：节点创建中。 - Deleting：节点删除中。 - Abnormal：节点异常。 - Checking: 节点自检中。

        :param phase: The phase of this NodeStatus.
        :type phase: str
        """
        self._phase = phase

    @property
    def az(self):
        r"""Gets the az of this NodeStatus.

        **参数解释**：节点所在的az。 **取值范围**：不涉及。

        :return: The az of this NodeStatus.
        :rtype: str
        """
        return self._az

    @az.setter
    def az(self, az):
        r"""Sets the az of this NodeStatus.

        **参数解释**：节点所在的az。 **取值范围**：不涉及。

        :param az: The az of this NodeStatus.
        :type az: str
        """
        self._az = az

    @property
    def private_ip(self):
        r"""Gets the private_ip of this NodeStatus.

        **参数解释**：节点的IP地址。 **取值范围**：不涉及。

        :return: The private_ip of this NodeStatus.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        r"""Sets the private_ip of this NodeStatus.

        **参数解释**：节点的IP地址。 **取值范围**：不涉及。

        :param private_ip: The private_ip of this NodeStatus.
        :type private_ip: str
        """
        self._private_ip = private_ip

    @property
    def resources(self):
        r"""Gets the resources of this NodeStatus.

        :return: The resources of this NodeStatus.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.NodeResource`
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        r"""Sets the resources of this NodeStatus.

        :param resources: The resources of this NodeStatus.
        :type resources: :class:`huaweicloudsdkmodelarts.v1.NodeResource`
        """
        self._resources = resources

    @property
    def available_resources(self):
        r"""Gets the available_resources of this NodeStatus.

        :return: The available_resources of this NodeStatus.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.NodeResource`
        """
        return self._available_resources

    @available_resources.setter
    def available_resources(self, available_resources):
        r"""Sets the available_resources of this NodeStatus.

        :param available_resources: The available_resources of this NodeStatus.
        :type available_resources: :class:`huaweicloudsdkmodelarts.v1.NodeResource`
        """
        self._available_resources = available_resources

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
        if not isinstance(other, NodeStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
