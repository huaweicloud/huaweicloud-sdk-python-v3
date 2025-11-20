# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Flavor:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'id': 'str',
        'connections': 'int',
        'bandwidth': 'int',
        'pps': 'int',
        'available_zones': 'list[str]'
    }

    attribute_map = {
        'name': 'name',
        'id': 'id',
        'connections': 'connections',
        'bandwidth': 'bandwidth',
        'pps': 'pps',
        'available_zones': 'available_zones'
    }

    def __init__(self, name=None, id=None, connections=None, bandwidth=None, pps=None, available_zones=None):
        r"""Flavor

        The model defined in huaweicloud sdk

        :param name: - 参数解释：ESW实例规格名称。 - 约束限制：不涉及。 - 取值范围：  - l2cg.small.ha  - l2cg.medium.ha  - l2cg.large.ha - 默认取值：不涉及。
        :type name: str
        :param id: - 参数解释：ESW实例规格的唯一标识。 - 约束限制：不涉及。 - 取值范围：1-3。 - 默认取值：不涉及。
        :type id: str
        :param connections: - 参数解释：该规格ESW实例可承载的二层连接数量。 - 约束限制：不涉及。 - 取值范围：1、3、6。 - 默认取值：不涉及。
        :type connections: int
        :param bandwidth: - 参数解释：该规格ESW实例可承载的最大带宽。 - 约束限制：单位:Gbit/s。 - 取值范围：3、5、10。 - 默认取值：不涉及。
        :type bandwidth: int
        :param pps: - 参数解释：该规格ESW实例可承载的最大发包数。 - 约束限制：不涉及。 - 取值范围：500000、1000000、2000000。 - 默认取值：不涉及。
        :type pps: int
        :param available_zones: - 参数解释：可选用该规格的可用区列表。 - 约束限制：不涉及。 - 取值范围：不涉及。 - 默认取值：不涉及。
        :type available_zones: list[str]
        """
        
        

        self._name = None
        self._id = None
        self._connections = None
        self._bandwidth = None
        self._pps = None
        self._available_zones = None
        self.discriminator = None

        self.name = name
        self.id = id
        self.connections = connections
        self.bandwidth = bandwidth
        self.pps = pps
        self.available_zones = available_zones

    @property
    def name(self):
        r"""Gets the name of this Flavor.

        - 参数解释：ESW实例规格名称。 - 约束限制：不涉及。 - 取值范围：  - l2cg.small.ha  - l2cg.medium.ha  - l2cg.large.ha - 默认取值：不涉及。

        :return: The name of this Flavor.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this Flavor.

        - 参数解释：ESW实例规格名称。 - 约束限制：不涉及。 - 取值范围：  - l2cg.small.ha  - l2cg.medium.ha  - l2cg.large.ha - 默认取值：不涉及。

        :param name: The name of this Flavor.
        :type name: str
        """
        self._name = name

    @property
    def id(self):
        r"""Gets the id of this Flavor.

        - 参数解释：ESW实例规格的唯一标识。 - 约束限制：不涉及。 - 取值范围：1-3。 - 默认取值：不涉及。

        :return: The id of this Flavor.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this Flavor.

        - 参数解释：ESW实例规格的唯一标识。 - 约束限制：不涉及。 - 取值范围：1-3。 - 默认取值：不涉及。

        :param id: The id of this Flavor.
        :type id: str
        """
        self._id = id

    @property
    def connections(self):
        r"""Gets the connections of this Flavor.

        - 参数解释：该规格ESW实例可承载的二层连接数量。 - 约束限制：不涉及。 - 取值范围：1、3、6。 - 默认取值：不涉及。

        :return: The connections of this Flavor.
        :rtype: int
        """
        return self._connections

    @connections.setter
    def connections(self, connections):
        r"""Sets the connections of this Flavor.

        - 参数解释：该规格ESW实例可承载的二层连接数量。 - 约束限制：不涉及。 - 取值范围：1、3、6。 - 默认取值：不涉及。

        :param connections: The connections of this Flavor.
        :type connections: int
        """
        self._connections = connections

    @property
    def bandwidth(self):
        r"""Gets the bandwidth of this Flavor.

        - 参数解释：该规格ESW实例可承载的最大带宽。 - 约束限制：单位:Gbit/s。 - 取值范围：3、5、10。 - 默认取值：不涉及。

        :return: The bandwidth of this Flavor.
        :rtype: int
        """
        return self._bandwidth

    @bandwidth.setter
    def bandwidth(self, bandwidth):
        r"""Sets the bandwidth of this Flavor.

        - 参数解释：该规格ESW实例可承载的最大带宽。 - 约束限制：单位:Gbit/s。 - 取值范围：3、5、10。 - 默认取值：不涉及。

        :param bandwidth: The bandwidth of this Flavor.
        :type bandwidth: int
        """
        self._bandwidth = bandwidth

    @property
    def pps(self):
        r"""Gets the pps of this Flavor.

        - 参数解释：该规格ESW实例可承载的最大发包数。 - 约束限制：不涉及。 - 取值范围：500000、1000000、2000000。 - 默认取值：不涉及。

        :return: The pps of this Flavor.
        :rtype: int
        """
        return self._pps

    @pps.setter
    def pps(self, pps):
        r"""Sets the pps of this Flavor.

        - 参数解释：该规格ESW实例可承载的最大发包数。 - 约束限制：不涉及。 - 取值范围：500000、1000000、2000000。 - 默认取值：不涉及。

        :param pps: The pps of this Flavor.
        :type pps: int
        """
        self._pps = pps

    @property
    def available_zones(self):
        r"""Gets the available_zones of this Flavor.

        - 参数解释：可选用该规格的可用区列表。 - 约束限制：不涉及。 - 取值范围：不涉及。 - 默认取值：不涉及。

        :return: The available_zones of this Flavor.
        :rtype: list[str]
        """
        return self._available_zones

    @available_zones.setter
    def available_zones(self, available_zones):
        r"""Sets the available_zones of this Flavor.

        - 参数解释：可选用该规格的可用区列表。 - 约束限制：不涉及。 - 取值范围：不涉及。 - 默认取值：不涉及。

        :param available_zones: The available_zones of this Flavor.
        :type available_zones: list[str]
        """
        self._available_zones = available_zones

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
        if not isinstance(other, Flavor):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
