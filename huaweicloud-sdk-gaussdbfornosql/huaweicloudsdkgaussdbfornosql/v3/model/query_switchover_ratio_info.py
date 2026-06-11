# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QuerySwitchoverRatioInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'switchover_ratio': 'int',
        'sync_delay': 'int'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'switchover_ratio': 'switchover_ratio',
        'sync_delay': 'sync_delay'
    }

    def __init__(self, instance_id=None, switchover_ratio=None, sync_delay=None):
        r"""QuerySwitchoverRatioInfo

        The model defined in huaweicloud sdk

        :param instance_id: **参数解释：** 实例ID，可以调用“查询实例列表”接口获取。如果未申请实例，可以调用“创建实例”接口创建。 **取值范围：** 不涉及。
        :type instance_id: str
        :param switchover_ratio: **参数解释：** 容灾切换的故障节点比例。 **取值范围：** - 50 - 60 - 70 - 80 - 90 - 100
        :type switchover_ratio: int
        :param sync_delay: **参数解释：** 容灾实例数据同步时延，单位s。备实例和主实例同步时延超过该值时，不进行容灾倒换。默认不判断时延。 **取值范围：** 不涉及。
        :type sync_delay: int
        """
        
        

        self._instance_id = None
        self._switchover_ratio = None
        self._sync_delay = None
        self.discriminator = None

        self.instance_id = instance_id
        if switchover_ratio is not None:
            self.switchover_ratio = switchover_ratio
        if sync_delay is not None:
            self.sync_delay = sync_delay

    @property
    def instance_id(self):
        r"""Gets the instance_id of this QuerySwitchoverRatioInfo.

        **参数解释：** 实例ID，可以调用“查询实例列表”接口获取。如果未申请实例，可以调用“创建实例”接口创建。 **取值范围：** 不涉及。

        :return: The instance_id of this QuerySwitchoverRatioInfo.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this QuerySwitchoverRatioInfo.

        **参数解释：** 实例ID，可以调用“查询实例列表”接口获取。如果未申请实例，可以调用“创建实例”接口创建。 **取值范围：** 不涉及。

        :param instance_id: The instance_id of this QuerySwitchoverRatioInfo.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def switchover_ratio(self):
        r"""Gets the switchover_ratio of this QuerySwitchoverRatioInfo.

        **参数解释：** 容灾切换的故障节点比例。 **取值范围：** - 50 - 60 - 70 - 80 - 90 - 100

        :return: The switchover_ratio of this QuerySwitchoverRatioInfo.
        :rtype: int
        """
        return self._switchover_ratio

    @switchover_ratio.setter
    def switchover_ratio(self, switchover_ratio):
        r"""Sets the switchover_ratio of this QuerySwitchoverRatioInfo.

        **参数解释：** 容灾切换的故障节点比例。 **取值范围：** - 50 - 60 - 70 - 80 - 90 - 100

        :param switchover_ratio: The switchover_ratio of this QuerySwitchoverRatioInfo.
        :type switchover_ratio: int
        """
        self._switchover_ratio = switchover_ratio

    @property
    def sync_delay(self):
        r"""Gets the sync_delay of this QuerySwitchoverRatioInfo.

        **参数解释：** 容灾实例数据同步时延，单位s。备实例和主实例同步时延超过该值时，不进行容灾倒换。默认不判断时延。 **取值范围：** 不涉及。

        :return: The sync_delay of this QuerySwitchoverRatioInfo.
        :rtype: int
        """
        return self._sync_delay

    @sync_delay.setter
    def sync_delay(self, sync_delay):
        r"""Sets the sync_delay of this QuerySwitchoverRatioInfo.

        **参数解释：** 容灾实例数据同步时延，单位s。备实例和主实例同步时延超过该值时，不进行容灾倒换。默认不判断时延。 **取值范围：** 不涉及。

        :param sync_delay: The sync_delay of this QuerySwitchoverRatioInfo.
        :type sync_delay: int
        """
        self._sync_delay = sync_delay

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
        if not isinstance(other, QuerySwitchoverRatioInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
