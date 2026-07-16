# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NodeSpec:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'flavor': 'str',
        'os': 'Os',
        'host_network': 'NodeNetwork',
        'root_volume': 'VolumeVO',
        'data_volumes': 'list[VolumeVO]',
        'extend_params': 'ResourceExtendParams'
    }

    attribute_map = {
        'flavor': 'flavor',
        'os': 'os',
        'host_network': 'hostNetwork',
        'root_volume': 'rootVolume',
        'data_volumes': 'dataVolumes',
        'extend_params': 'extendParams'
    }

    def __init__(self, flavor=None, os=None, host_network=None, root_volume=None, data_volumes=None, extend_params=None):
        r"""NodeSpec

        The model defined in huaweicloud sdk

        :param flavor: **参数解释**：节点资源规格ID。 **取值范围**：不涉及。
        :type flavor: str
        :param os: 
        :type os: :class:`huaweicloudsdkmodelarts.v1.Os`
        :param host_network: 
        :type host_network: :class:`huaweicloudsdkmodelarts.v1.NodeNetwork`
        :param root_volume: 
        :type root_volume: :class:`huaweicloudsdkmodelarts.v1.VolumeVO`
        :param data_volumes: **参数解释**：数据盘信息。
        :type data_volumes: list[:class:`huaweicloudsdkmodelarts.v1.VolumeVO`]
        :param extend_params: 
        :type extend_params: :class:`huaweicloudsdkmodelarts.v1.ResourceExtendParams`
        """
        
        

        self._flavor = None
        self._os = None
        self._host_network = None
        self._root_volume = None
        self._data_volumes = None
        self._extend_params = None
        self.discriminator = None

        self.flavor = flavor
        if os is not None:
            self.os = os
        if host_network is not None:
            self.host_network = host_network
        if root_volume is not None:
            self.root_volume = root_volume
        if data_volumes is not None:
            self.data_volumes = data_volumes
        if extend_params is not None:
            self.extend_params = extend_params

    @property
    def flavor(self):
        r"""Gets the flavor of this NodeSpec.

        **参数解释**：节点资源规格ID。 **取值范围**：不涉及。

        :return: The flavor of this NodeSpec.
        :rtype: str
        """
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        r"""Sets the flavor of this NodeSpec.

        **参数解释**：节点资源规格ID。 **取值范围**：不涉及。

        :param flavor: The flavor of this NodeSpec.
        :type flavor: str
        """
        self._flavor = flavor

    @property
    def os(self):
        r"""Gets the os of this NodeSpec.

        :return: The os of this NodeSpec.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.Os`
        """
        return self._os

    @os.setter
    def os(self, os):
        r"""Sets the os of this NodeSpec.

        :param os: The os of this NodeSpec.
        :type os: :class:`huaweicloudsdkmodelarts.v1.Os`
        """
        self._os = os

    @property
    def host_network(self):
        r"""Gets the host_network of this NodeSpec.

        :return: The host_network of this NodeSpec.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.NodeNetwork`
        """
        return self._host_network

    @host_network.setter
    def host_network(self, host_network):
        r"""Sets the host_network of this NodeSpec.

        :param host_network: The host_network of this NodeSpec.
        :type host_network: :class:`huaweicloudsdkmodelarts.v1.NodeNetwork`
        """
        self._host_network = host_network

    @property
    def root_volume(self):
        r"""Gets the root_volume of this NodeSpec.

        :return: The root_volume of this NodeSpec.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.VolumeVO`
        """
        return self._root_volume

    @root_volume.setter
    def root_volume(self, root_volume):
        r"""Sets the root_volume of this NodeSpec.

        :param root_volume: The root_volume of this NodeSpec.
        :type root_volume: :class:`huaweicloudsdkmodelarts.v1.VolumeVO`
        """
        self._root_volume = root_volume

    @property
    def data_volumes(self):
        r"""Gets the data_volumes of this NodeSpec.

        **参数解释**：数据盘信息。

        :return: The data_volumes of this NodeSpec.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.VolumeVO`]
        """
        return self._data_volumes

    @data_volumes.setter
    def data_volumes(self, data_volumes):
        r"""Sets the data_volumes of this NodeSpec.

        **参数解释**：数据盘信息。

        :param data_volumes: The data_volumes of this NodeSpec.
        :type data_volumes: list[:class:`huaweicloudsdkmodelarts.v1.VolumeVO`]
        """
        self._data_volumes = data_volumes

    @property
    def extend_params(self):
        r"""Gets the extend_params of this NodeSpec.

        :return: The extend_params of this NodeSpec.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ResourceExtendParams`
        """
        return self._extend_params

    @extend_params.setter
    def extend_params(self, extend_params):
        r"""Sets the extend_params of this NodeSpec.

        :param extend_params: The extend_params of this NodeSpec.
        :type extend_params: :class:`huaweicloudsdkmodelarts.v1.ResourceExtendParams`
        """
        self._extend_params = extend_params

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
        if not isinstance(other, NodeSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
