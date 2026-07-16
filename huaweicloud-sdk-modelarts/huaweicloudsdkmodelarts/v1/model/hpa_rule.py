# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HpaRule:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'hpa_id': 'str',
        'name': 'str',
        'type': 'str',
        'schedule': 'str',
        'target_replicas': 'int',
        'disable': 'str',
        'status': 'str'
    }

    attribute_map = {
        'id': 'id',
        'hpa_id': 'hpa_id',
        'name': 'name',
        'type': 'type',
        'schedule': 'schedule',
        'target_replicas': 'target_replicas',
        'disable': 'disable',
        'status': 'status'
    }

    def __init__(self, id=None, hpa_id=None, name=None, type=None, schedule=None, target_replicas=None, disable=None, status=None):
        r"""HpaRule

        The model defined in huaweicloud sdk

        :param id: **参数解释：** 自动扩缩容规则ID **取值范围：** 不涉及。
        :type id: str
        :param hpa_id: **参数解释：** 自动扩缩容规则关联的策略ID **取值范围：** 不涉及。
        :type hpa_id: str
        :param name: **参数解释：** 自动扩缩容规则名 **取值范围：** 支持4-64个字符，可以包含字母、汉字、数字、中划线和下划线。
        :type name: str
        :param type: **参数解释：** 自动扩缩容类型。 **取值范围：** - CRON_HPA：定时扩缩容策略 - METRIC_HPA：指标扩缩容策略
        :type type: str
        :param schedule: **参数解释：** 定时自动扩缩容执行的cron表达式，不支持秒，从分钟开始设定 **取值范围：** 不涉及。
        :type schedule: str
        :param target_replicas: **参数解释：** 自动扩缩容目标实例数。 **取值范围：** 1-128
        :type target_replicas: int
        :param disable: **参数解释：** 自动扩缩容规则是否启用。 **取值范围：** - false - true
        :type disable: str
        :param status: **参数解释：** 自动扩缩容规则状态。 **取值范围：** - CREATING：创建中 - CONFIG_SUCCESS：配置成功 - EXECUTE_SUCCESS：执行成功 - DELETED：已删除 - FAILED: 执行失败
        :type status: str
        """
        
        

        self._id = None
        self._hpa_id = None
        self._name = None
        self._type = None
        self._schedule = None
        self._target_replicas = None
        self._disable = None
        self._status = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if hpa_id is not None:
            self.hpa_id = hpa_id
        self.name = name
        if type is not None:
            self.type = type
        if schedule is not None:
            self.schedule = schedule
        if target_replicas is not None:
            self.target_replicas = target_replicas
        if disable is not None:
            self.disable = disable
        if status is not None:
            self.status = status

    @property
    def id(self):
        r"""Gets the id of this HpaRule.

        **参数解释：** 自动扩缩容规则ID **取值范围：** 不涉及。

        :return: The id of this HpaRule.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this HpaRule.

        **参数解释：** 自动扩缩容规则ID **取值范围：** 不涉及。

        :param id: The id of this HpaRule.
        :type id: str
        """
        self._id = id

    @property
    def hpa_id(self):
        r"""Gets the hpa_id of this HpaRule.

        **参数解释：** 自动扩缩容规则关联的策略ID **取值范围：** 不涉及。

        :return: The hpa_id of this HpaRule.
        :rtype: str
        """
        return self._hpa_id

    @hpa_id.setter
    def hpa_id(self, hpa_id):
        r"""Sets the hpa_id of this HpaRule.

        **参数解释：** 自动扩缩容规则关联的策略ID **取值范围：** 不涉及。

        :param hpa_id: The hpa_id of this HpaRule.
        :type hpa_id: str
        """
        self._hpa_id = hpa_id

    @property
    def name(self):
        r"""Gets the name of this HpaRule.

        **参数解释：** 自动扩缩容规则名 **取值范围：** 支持4-64个字符，可以包含字母、汉字、数字、中划线和下划线。

        :return: The name of this HpaRule.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this HpaRule.

        **参数解释：** 自动扩缩容规则名 **取值范围：** 支持4-64个字符，可以包含字母、汉字、数字、中划线和下划线。

        :param name: The name of this HpaRule.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        r"""Gets the type of this HpaRule.

        **参数解释：** 自动扩缩容类型。 **取值范围：** - CRON_HPA：定时扩缩容策略 - METRIC_HPA：指标扩缩容策略

        :return: The type of this HpaRule.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this HpaRule.

        **参数解释：** 自动扩缩容类型。 **取值范围：** - CRON_HPA：定时扩缩容策略 - METRIC_HPA：指标扩缩容策略

        :param type: The type of this HpaRule.
        :type type: str
        """
        self._type = type

    @property
    def schedule(self):
        r"""Gets the schedule of this HpaRule.

        **参数解释：** 定时自动扩缩容执行的cron表达式，不支持秒，从分钟开始设定 **取值范围：** 不涉及。

        :return: The schedule of this HpaRule.
        :rtype: str
        """
        return self._schedule

    @schedule.setter
    def schedule(self, schedule):
        r"""Sets the schedule of this HpaRule.

        **参数解释：** 定时自动扩缩容执行的cron表达式，不支持秒，从分钟开始设定 **取值范围：** 不涉及。

        :param schedule: The schedule of this HpaRule.
        :type schedule: str
        """
        self._schedule = schedule

    @property
    def target_replicas(self):
        r"""Gets the target_replicas of this HpaRule.

        **参数解释：** 自动扩缩容目标实例数。 **取值范围：** 1-128

        :return: The target_replicas of this HpaRule.
        :rtype: int
        """
        return self._target_replicas

    @target_replicas.setter
    def target_replicas(self, target_replicas):
        r"""Sets the target_replicas of this HpaRule.

        **参数解释：** 自动扩缩容目标实例数。 **取值范围：** 1-128

        :param target_replicas: The target_replicas of this HpaRule.
        :type target_replicas: int
        """
        self._target_replicas = target_replicas

    @property
    def disable(self):
        r"""Gets the disable of this HpaRule.

        **参数解释：** 自动扩缩容规则是否启用。 **取值范围：** - false - true

        :return: The disable of this HpaRule.
        :rtype: str
        """
        return self._disable

    @disable.setter
    def disable(self, disable):
        r"""Sets the disable of this HpaRule.

        **参数解释：** 自动扩缩容规则是否启用。 **取值范围：** - false - true

        :param disable: The disable of this HpaRule.
        :type disable: str
        """
        self._disable = disable

    @property
    def status(self):
        r"""Gets the status of this HpaRule.

        **参数解释：** 自动扩缩容规则状态。 **取值范围：** - CREATING：创建中 - CONFIG_SUCCESS：配置成功 - EXECUTE_SUCCESS：执行成功 - DELETED：已删除 - FAILED: 执行失败

        :return: The status of this HpaRule.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this HpaRule.

        **参数解释：** 自动扩缩容规则状态。 **取值范围：** - CREATING：创建中 - CONFIG_SUCCESS：配置成功 - EXECUTE_SUCCESS：执行成功 - DELETED：已删除 - FAILED: 执行失败

        :param status: The status of this HpaRule.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, HpaRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
