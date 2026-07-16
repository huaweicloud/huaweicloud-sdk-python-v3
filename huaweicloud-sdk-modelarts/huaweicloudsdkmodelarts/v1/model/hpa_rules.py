# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HpaRules:

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
        'disable': 'bool',
        'type': 'str',
        'status': 'str',
        'operate': 'str',
        'schedule': 'str',
        'target_replicas': 'int',
        'min_replicas': 'int',
        'max_replicas': 'int',
        'downscale_window': 'int',
        'upscale_window': 'int'
    }

    attribute_map = {
        'name': 'name',
        'id': 'id',
        'disable': 'disable',
        'type': 'type',
        'status': 'status',
        'operate': 'operate',
        'schedule': 'schedule',
        'target_replicas': 'target_replicas',
        'min_replicas': 'min_replicas',
        'max_replicas': 'max_replicas',
        'downscale_window': 'downscale_window',
        'upscale_window': 'upscale_window'
    }

    def __init__(self, name=None, id=None, disable=None, type=None, status=None, operate=None, schedule=None, target_replicas=None, min_replicas=None, max_replicas=None, downscale_window=None, upscale_window=None):
        r"""HpaRules

        The model defined in huaweicloud sdk

        :param name: **参数解释：** 自动扩缩容规则名。 **取值范围：** 支持4-64个字符，可以包含小写字母、数字和中划线，必须以小写字母开头，不能以中划线结尾。 **约束限制：** 不涉及。 **默认取值：** 不涉及。
        :type name: str
        :param id: **参数解释：** 自动扩缩容id **取值范围：** 支持4-64个字符，可以包含字母、汉字、数字、中划线和下划线。 **约束限制：** 不涉及。 **默认取值：** 不涉及。
        :type id: str
        :param disable: **参数解释：** 自动扩缩容规则是否启用。 **取值范围：** - false：启动 - true：不启动 **约束限制：** 不涉及。 **默认取值：** 不涉及。
        :type disable: bool
        :param type: **参数解释：** 自动扩缩容类型。 **取值范围：** - CRON_HPA：定时扩缩容策略 - METRIC_HPA：指标扩缩容策略 **约束限制：** 不涉及。 **默认取值：** 不涉及。
        :type type: str
        :param status: **参数解释：** 自动扩缩容类型。 **取值范围：** - CREATING：创建扩缩容策略 - CONFIG_SUCCESS：配置成功扩缩容策略 - EXECUTE_SUCCESS：执行成功扩缩容策略 - DELETED：删除扩缩容策略 - FAILED：失败扩缩容策略 **约束限制：** 不涉及。 **默认取值：** 不涉及。
        :type status: str
        :param operate: **参数解释：** 自动扩缩容类型。 **取值范围：** - ADD：添加扩缩容策略规则 - UPDATE：修改扩缩容策略规则 - DELETE：删除扩缩容策略规则 **约束限制：** 不涉及。 **默认取值：** 不涉及。
        :type operate: str
        :param schedule: **参数解释：** 定时自动扩缩容执行的cron表达式，不支持秒，从分钟开始设定 **取值范围：** 不涉及。 **约束限制：** 不涉及。 **默认取值：** 不涉及。
        :type schedule: str
        :param target_replicas: **参数解释：** 自动扩缩容目标实例数。 **取值范围：** 1-128，接口能接受浮点类型，后端会自动向下取整 **约束限制：** 不涉及。 **默认取值：** 不涉及。
        :type target_replicas: int
        :param min_replicas: **参数解释：** 自动扩缩容最小实例数。 **取值范围：** 1-128，接口能接受浮点类型，后端会自动向下取整 **约束限制：** 不涉及。 **默认取值：** 不涉及。
        :type min_replicas: int
        :param max_replicas: **参数解释：** 自动扩缩容最大实例数。 **取值范围：** 1-128，接口能接受浮点类型，后端会自动向下取整 **约束限制：** 不涉及。 **默认取值：** 不涉及。
        :type max_replicas: int
        :param downscale_window: **参数解释：** 自动扩缩容扩容冷却时间。 **取值范围：** 1-128，接口能接受浮点类型，后端会自动向下取整 **约束限制：** 不涉及。 **默认取值：** 不涉及。
        :type downscale_window: int
        :param upscale_window: **参数解释：** 自动扩缩容缩容冷却时间。 **取值范围：** 1-128，接口能接受浮点类型，后端会自动向下取整 **约束限制：** 不涉及。 **默认取值：** 不涉及。
        :type upscale_window: int
        """
        
        

        self._name = None
        self._id = None
        self._disable = None
        self._type = None
        self._status = None
        self._operate = None
        self._schedule = None
        self._target_replicas = None
        self._min_replicas = None
        self._max_replicas = None
        self._downscale_window = None
        self._upscale_window = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if disable is not None:
            self.disable = disable
        self.type = type
        if status is not None:
            self.status = status
        if operate is not None:
            self.operate = operate
        self.schedule = schedule
        self.target_replicas = target_replicas
        if min_replicas is not None:
            self.min_replicas = min_replicas
        if max_replicas is not None:
            self.max_replicas = max_replicas
        if downscale_window is not None:
            self.downscale_window = downscale_window
        if upscale_window is not None:
            self.upscale_window = upscale_window

    @property
    def name(self):
        r"""Gets the name of this HpaRules.

        **参数解释：** 自动扩缩容规则名。 **取值范围：** 支持4-64个字符，可以包含小写字母、数字和中划线，必须以小写字母开头，不能以中划线结尾。 **约束限制：** 不涉及。 **默认取值：** 不涉及。

        :return: The name of this HpaRules.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this HpaRules.

        **参数解释：** 自动扩缩容规则名。 **取值范围：** 支持4-64个字符，可以包含小写字母、数字和中划线，必须以小写字母开头，不能以中划线结尾。 **约束限制：** 不涉及。 **默认取值：** 不涉及。

        :param name: The name of this HpaRules.
        :type name: str
        """
        self._name = name

    @property
    def id(self):
        r"""Gets the id of this HpaRules.

        **参数解释：** 自动扩缩容id **取值范围：** 支持4-64个字符，可以包含字母、汉字、数字、中划线和下划线。 **约束限制：** 不涉及。 **默认取值：** 不涉及。

        :return: The id of this HpaRules.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this HpaRules.

        **参数解释：** 自动扩缩容id **取值范围：** 支持4-64个字符，可以包含字母、汉字、数字、中划线和下划线。 **约束限制：** 不涉及。 **默认取值：** 不涉及。

        :param id: The id of this HpaRules.
        :type id: str
        """
        self._id = id

    @property
    def disable(self):
        r"""Gets the disable of this HpaRules.

        **参数解释：** 自动扩缩容规则是否启用。 **取值范围：** - false：启动 - true：不启动 **约束限制：** 不涉及。 **默认取值：** 不涉及。

        :return: The disable of this HpaRules.
        :rtype: bool
        """
        return self._disable

    @disable.setter
    def disable(self, disable):
        r"""Sets the disable of this HpaRules.

        **参数解释：** 自动扩缩容规则是否启用。 **取值范围：** - false：启动 - true：不启动 **约束限制：** 不涉及。 **默认取值：** 不涉及。

        :param disable: The disable of this HpaRules.
        :type disable: bool
        """
        self._disable = disable

    @property
    def type(self):
        r"""Gets the type of this HpaRules.

        **参数解释：** 自动扩缩容类型。 **取值范围：** - CRON_HPA：定时扩缩容策略 - METRIC_HPA：指标扩缩容策略 **约束限制：** 不涉及。 **默认取值：** 不涉及。

        :return: The type of this HpaRules.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this HpaRules.

        **参数解释：** 自动扩缩容类型。 **取值范围：** - CRON_HPA：定时扩缩容策略 - METRIC_HPA：指标扩缩容策略 **约束限制：** 不涉及。 **默认取值：** 不涉及。

        :param type: The type of this HpaRules.
        :type type: str
        """
        self._type = type

    @property
    def status(self):
        r"""Gets the status of this HpaRules.

        **参数解释：** 自动扩缩容类型。 **取值范围：** - CREATING：创建扩缩容策略 - CONFIG_SUCCESS：配置成功扩缩容策略 - EXECUTE_SUCCESS：执行成功扩缩容策略 - DELETED：删除扩缩容策略 - FAILED：失败扩缩容策略 **约束限制：** 不涉及。 **默认取值：** 不涉及。

        :return: The status of this HpaRules.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this HpaRules.

        **参数解释：** 自动扩缩容类型。 **取值范围：** - CREATING：创建扩缩容策略 - CONFIG_SUCCESS：配置成功扩缩容策略 - EXECUTE_SUCCESS：执行成功扩缩容策略 - DELETED：删除扩缩容策略 - FAILED：失败扩缩容策略 **约束限制：** 不涉及。 **默认取值：** 不涉及。

        :param status: The status of this HpaRules.
        :type status: str
        """
        self._status = status

    @property
    def operate(self):
        r"""Gets the operate of this HpaRules.

        **参数解释：** 自动扩缩容类型。 **取值范围：** - ADD：添加扩缩容策略规则 - UPDATE：修改扩缩容策略规则 - DELETE：删除扩缩容策略规则 **约束限制：** 不涉及。 **默认取值：** 不涉及。

        :return: The operate of this HpaRules.
        :rtype: str
        """
        return self._operate

    @operate.setter
    def operate(self, operate):
        r"""Sets the operate of this HpaRules.

        **参数解释：** 自动扩缩容类型。 **取值范围：** - ADD：添加扩缩容策略规则 - UPDATE：修改扩缩容策略规则 - DELETE：删除扩缩容策略规则 **约束限制：** 不涉及。 **默认取值：** 不涉及。

        :param operate: The operate of this HpaRules.
        :type operate: str
        """
        self._operate = operate

    @property
    def schedule(self):
        r"""Gets the schedule of this HpaRules.

        **参数解释：** 定时自动扩缩容执行的cron表达式，不支持秒，从分钟开始设定 **取值范围：** 不涉及。 **约束限制：** 不涉及。 **默认取值：** 不涉及。

        :return: The schedule of this HpaRules.
        :rtype: str
        """
        return self._schedule

    @schedule.setter
    def schedule(self, schedule):
        r"""Sets the schedule of this HpaRules.

        **参数解释：** 定时自动扩缩容执行的cron表达式，不支持秒，从分钟开始设定 **取值范围：** 不涉及。 **约束限制：** 不涉及。 **默认取值：** 不涉及。

        :param schedule: The schedule of this HpaRules.
        :type schedule: str
        """
        self._schedule = schedule

    @property
    def target_replicas(self):
        r"""Gets the target_replicas of this HpaRules.

        **参数解释：** 自动扩缩容目标实例数。 **取值范围：** 1-128，接口能接受浮点类型，后端会自动向下取整 **约束限制：** 不涉及。 **默认取值：** 不涉及。

        :return: The target_replicas of this HpaRules.
        :rtype: int
        """
        return self._target_replicas

    @target_replicas.setter
    def target_replicas(self, target_replicas):
        r"""Sets the target_replicas of this HpaRules.

        **参数解释：** 自动扩缩容目标实例数。 **取值范围：** 1-128，接口能接受浮点类型，后端会自动向下取整 **约束限制：** 不涉及。 **默认取值：** 不涉及。

        :param target_replicas: The target_replicas of this HpaRules.
        :type target_replicas: int
        """
        self._target_replicas = target_replicas

    @property
    def min_replicas(self):
        r"""Gets the min_replicas of this HpaRules.

        **参数解释：** 自动扩缩容最小实例数。 **取值范围：** 1-128，接口能接受浮点类型，后端会自动向下取整 **约束限制：** 不涉及。 **默认取值：** 不涉及。

        :return: The min_replicas of this HpaRules.
        :rtype: int
        """
        return self._min_replicas

    @min_replicas.setter
    def min_replicas(self, min_replicas):
        r"""Sets the min_replicas of this HpaRules.

        **参数解释：** 自动扩缩容最小实例数。 **取值范围：** 1-128，接口能接受浮点类型，后端会自动向下取整 **约束限制：** 不涉及。 **默认取值：** 不涉及。

        :param min_replicas: The min_replicas of this HpaRules.
        :type min_replicas: int
        """
        self._min_replicas = min_replicas

    @property
    def max_replicas(self):
        r"""Gets the max_replicas of this HpaRules.

        **参数解释：** 自动扩缩容最大实例数。 **取值范围：** 1-128，接口能接受浮点类型，后端会自动向下取整 **约束限制：** 不涉及。 **默认取值：** 不涉及。

        :return: The max_replicas of this HpaRules.
        :rtype: int
        """
        return self._max_replicas

    @max_replicas.setter
    def max_replicas(self, max_replicas):
        r"""Sets the max_replicas of this HpaRules.

        **参数解释：** 自动扩缩容最大实例数。 **取值范围：** 1-128，接口能接受浮点类型，后端会自动向下取整 **约束限制：** 不涉及。 **默认取值：** 不涉及。

        :param max_replicas: The max_replicas of this HpaRules.
        :type max_replicas: int
        """
        self._max_replicas = max_replicas

    @property
    def downscale_window(self):
        r"""Gets the downscale_window of this HpaRules.

        **参数解释：** 自动扩缩容扩容冷却时间。 **取值范围：** 1-128，接口能接受浮点类型，后端会自动向下取整 **约束限制：** 不涉及。 **默认取值：** 不涉及。

        :return: The downscale_window of this HpaRules.
        :rtype: int
        """
        return self._downscale_window

    @downscale_window.setter
    def downscale_window(self, downscale_window):
        r"""Sets the downscale_window of this HpaRules.

        **参数解释：** 自动扩缩容扩容冷却时间。 **取值范围：** 1-128，接口能接受浮点类型，后端会自动向下取整 **约束限制：** 不涉及。 **默认取值：** 不涉及。

        :param downscale_window: The downscale_window of this HpaRules.
        :type downscale_window: int
        """
        self._downscale_window = downscale_window

    @property
    def upscale_window(self):
        r"""Gets the upscale_window of this HpaRules.

        **参数解释：** 自动扩缩容缩容冷却时间。 **取值范围：** 1-128，接口能接受浮点类型，后端会自动向下取整 **约束限制：** 不涉及。 **默认取值：** 不涉及。

        :return: The upscale_window of this HpaRules.
        :rtype: int
        """
        return self._upscale_window

    @upscale_window.setter
    def upscale_window(self, upscale_window):
        r"""Sets the upscale_window of this HpaRules.

        **参数解释：** 自动扩缩容缩容冷却时间。 **取值范围：** 1-128，接口能接受浮点类型，后端会自动向下取整 **约束限制：** 不涉及。 **默认取值：** 不涉及。

        :param upscale_window: The upscale_window of this HpaRules.
        :type upscale_window: int
        """
        self._upscale_window = upscale_window

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
        if not isinstance(other, HpaRules):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
