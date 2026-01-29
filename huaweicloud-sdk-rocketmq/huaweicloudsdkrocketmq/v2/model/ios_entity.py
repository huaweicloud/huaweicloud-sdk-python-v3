# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IOSEntity:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'available_zones': 'list[str]',
        'unavailable_zones': 'list[str]',
        'io_spec': 'str',
        'type': 'str'
    }

    attribute_map = {
        'available_zones': 'available_zones',
        'unavailable_zones': 'unavailable_zones',
        'io_spec': 'io_spec',
        'type': 'type'
    }

    def __init__(self, available_zones=None, unavailable_zones=None, io_spec=None, type=None):
        r"""IOSEntity

        The model defined in huaweicloud sdk

        :param available_zones: **参数解释**： 可用分区列表。[RocketMQ 5.X基础版部署架构为单机时，请选择1个可用区，为集群时可选择1个或2个可用区。](tag:ctc,hws_eu,ocb,g42,hk_g42,tm,sbc,hk_sbc,hk_tm,hcs,fcs,dt,hcs_oemout,srg) **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type available_zones: list[str]
        :param unavailable_zones: **参数解释**： 不可用分区列表。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type unavailable_zones: list[str]
        :param io_spec: **参数解释**： 存储类型规格编码。 **约束限制**： 不涉及。 **取值范围**： - dms.physical.storage.high.v2：高IO类型磁盘 - dms.physical.storage.ultra.v2：超高IO类型磁盘 [- dms.physical.storage.general：使用通用型SSD的磁盘类型。](tag:hws,hws_hk,dt,ctc,ax) [- dms.physical.storage.extreme：使用极速型SSD的磁盘类型。](tag:hws,hws_hk,dt,ctc,ax) **默认取值**： 不涉及。
        :type io_spec: str
        :param type: **参数解释**： 存储所属服务类型。 **约束限制**： 不涉及。 **取值范围**： evs **默认取值**： 不涉及。
        :type type: str
        """
        
        

        self._available_zones = None
        self._unavailable_zones = None
        self._io_spec = None
        self._type = None
        self.discriminator = None

        if available_zones is not None:
            self.available_zones = available_zones
        if unavailable_zones is not None:
            self.unavailable_zones = unavailable_zones
        if io_spec is not None:
            self.io_spec = io_spec
        if type is not None:
            self.type = type

    @property
    def available_zones(self):
        r"""Gets the available_zones of this IOSEntity.

        **参数解释**： 可用分区列表。[RocketMQ 5.X基础版部署架构为单机时，请选择1个可用区，为集群时可选择1个或2个可用区。](tag:ctc,hws_eu,ocb,g42,hk_g42,tm,sbc,hk_sbc,hk_tm,hcs,fcs,dt,hcs_oemout,srg) **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The available_zones of this IOSEntity.
        :rtype: list[str]
        """
        return self._available_zones

    @available_zones.setter
    def available_zones(self, available_zones):
        r"""Sets the available_zones of this IOSEntity.

        **参数解释**： 可用分区列表。[RocketMQ 5.X基础版部署架构为单机时，请选择1个可用区，为集群时可选择1个或2个可用区。](tag:ctc,hws_eu,ocb,g42,hk_g42,tm,sbc,hk_sbc,hk_tm,hcs,fcs,dt,hcs_oemout,srg) **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param available_zones: The available_zones of this IOSEntity.
        :type available_zones: list[str]
        """
        self._available_zones = available_zones

    @property
    def unavailable_zones(self):
        r"""Gets the unavailable_zones of this IOSEntity.

        **参数解释**： 不可用分区列表。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The unavailable_zones of this IOSEntity.
        :rtype: list[str]
        """
        return self._unavailable_zones

    @unavailable_zones.setter
    def unavailable_zones(self, unavailable_zones):
        r"""Sets the unavailable_zones of this IOSEntity.

        **参数解释**： 不可用分区列表。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param unavailable_zones: The unavailable_zones of this IOSEntity.
        :type unavailable_zones: list[str]
        """
        self._unavailable_zones = unavailable_zones

    @property
    def io_spec(self):
        r"""Gets the io_spec of this IOSEntity.

        **参数解释**： 存储类型规格编码。 **约束限制**： 不涉及。 **取值范围**： - dms.physical.storage.high.v2：高IO类型磁盘 - dms.physical.storage.ultra.v2：超高IO类型磁盘 [- dms.physical.storage.general：使用通用型SSD的磁盘类型。](tag:hws,hws_hk,dt,ctc,ax) [- dms.physical.storage.extreme：使用极速型SSD的磁盘类型。](tag:hws,hws_hk,dt,ctc,ax) **默认取值**： 不涉及。

        :return: The io_spec of this IOSEntity.
        :rtype: str
        """
        return self._io_spec

    @io_spec.setter
    def io_spec(self, io_spec):
        r"""Sets the io_spec of this IOSEntity.

        **参数解释**： 存储类型规格编码。 **约束限制**： 不涉及。 **取值范围**： - dms.physical.storage.high.v2：高IO类型磁盘 - dms.physical.storage.ultra.v2：超高IO类型磁盘 [- dms.physical.storage.general：使用通用型SSD的磁盘类型。](tag:hws,hws_hk,dt,ctc,ax) [- dms.physical.storage.extreme：使用极速型SSD的磁盘类型。](tag:hws,hws_hk,dt,ctc,ax) **默认取值**： 不涉及。

        :param io_spec: The io_spec of this IOSEntity.
        :type io_spec: str
        """
        self._io_spec = io_spec

    @property
    def type(self):
        r"""Gets the type of this IOSEntity.

        **参数解释**： 存储所属服务类型。 **约束限制**： 不涉及。 **取值范围**： evs **默认取值**： 不涉及。

        :return: The type of this IOSEntity.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this IOSEntity.

        **参数解释**： 存储所属服务类型。 **约束限制**： 不涉及。 **取值范围**： evs **默认取值**： 不涉及。

        :param type: The type of this IOSEntity.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, IOSEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
