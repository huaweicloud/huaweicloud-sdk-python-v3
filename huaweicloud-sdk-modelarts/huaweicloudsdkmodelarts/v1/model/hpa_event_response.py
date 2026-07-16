# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HpaEventResponse:

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
        'status': 'str',
        'message': 'str',
        'current_replicas': 'int',
        'target_replicas': 'int',
        'final_replicas': 'int',
        'record_time': 'str'
    }

    attribute_map = {
        'id': 'id',
        'hpa_id': 'hpa_id',
        'status': 'status',
        'message': 'message',
        'current_replicas': 'current_replicas',
        'target_replicas': 'target_replicas',
        'final_replicas': 'final_replicas',
        'record_time': 'record_time'
    }

    def __init__(self, id=None, hpa_id=None, status=None, message=None, current_replicas=None, target_replicas=None, final_replicas=None, record_time=None):
        r"""HpaEventResponse

        The model defined in huaweicloud sdk

        :param id: **参数解释：** 自动扩缩容策略事件ID **取值范围：** 事件ID
        :type id: str
        :param hpa_id: **参数解释：** 自动扩缩容策略ID **取值范围：** 策略ID
        :type hpa_id: str
        :param status: **参数解释：** 自动扩缩容事件状态。 **取值范围：** - SUCCESS: 成功 - FAILED: 失败
        :type status: str
        :param message: **参数解释：** 自动扩缩容规则执行信息。 **取值范围：** 不涉及
        :type message: str
        :param current_replicas: **参数解释：** 扩缩容前实例数。 **取值范围：** 不涉及。
        :type current_replicas: int
        :param target_replicas: **参数解释：** 预设目标实例数。 **取值范围：** 不涉及。
        :type target_replicas: int
        :param final_replicas: **参数解释：** 扩缩容后实例数。 **取值范围：** 不涉及。
        :type final_replicas: int
        :param record_time: **参数解释：** 执行记录时间。 **取值范围：** 2025-05-20 10:05:55
        :type record_time: str
        """
        
        

        self._id = None
        self._hpa_id = None
        self._status = None
        self._message = None
        self._current_replicas = None
        self._target_replicas = None
        self._final_replicas = None
        self._record_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if hpa_id is not None:
            self.hpa_id = hpa_id
        if status is not None:
            self.status = status
        if message is not None:
            self.message = message
        if current_replicas is not None:
            self.current_replicas = current_replicas
        if target_replicas is not None:
            self.target_replicas = target_replicas
        if final_replicas is not None:
            self.final_replicas = final_replicas
        if record_time is not None:
            self.record_time = record_time

    @property
    def id(self):
        r"""Gets the id of this HpaEventResponse.

        **参数解释：** 自动扩缩容策略事件ID **取值范围：** 事件ID

        :return: The id of this HpaEventResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this HpaEventResponse.

        **参数解释：** 自动扩缩容策略事件ID **取值范围：** 事件ID

        :param id: The id of this HpaEventResponse.
        :type id: str
        """
        self._id = id

    @property
    def hpa_id(self):
        r"""Gets the hpa_id of this HpaEventResponse.

        **参数解释：** 自动扩缩容策略ID **取值范围：** 策略ID

        :return: The hpa_id of this HpaEventResponse.
        :rtype: str
        """
        return self._hpa_id

    @hpa_id.setter
    def hpa_id(self, hpa_id):
        r"""Sets the hpa_id of this HpaEventResponse.

        **参数解释：** 自动扩缩容策略ID **取值范围：** 策略ID

        :param hpa_id: The hpa_id of this HpaEventResponse.
        :type hpa_id: str
        """
        self._hpa_id = hpa_id

    @property
    def status(self):
        r"""Gets the status of this HpaEventResponse.

        **参数解释：** 自动扩缩容事件状态。 **取值范围：** - SUCCESS: 成功 - FAILED: 失败

        :return: The status of this HpaEventResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this HpaEventResponse.

        **参数解释：** 自动扩缩容事件状态。 **取值范围：** - SUCCESS: 成功 - FAILED: 失败

        :param status: The status of this HpaEventResponse.
        :type status: str
        """
        self._status = status

    @property
    def message(self):
        r"""Gets the message of this HpaEventResponse.

        **参数解释：** 自动扩缩容规则执行信息。 **取值范围：** 不涉及

        :return: The message of this HpaEventResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this HpaEventResponse.

        **参数解释：** 自动扩缩容规则执行信息。 **取值范围：** 不涉及

        :param message: The message of this HpaEventResponse.
        :type message: str
        """
        self._message = message

    @property
    def current_replicas(self):
        r"""Gets the current_replicas of this HpaEventResponse.

        **参数解释：** 扩缩容前实例数。 **取值范围：** 不涉及。

        :return: The current_replicas of this HpaEventResponse.
        :rtype: int
        """
        return self._current_replicas

    @current_replicas.setter
    def current_replicas(self, current_replicas):
        r"""Sets the current_replicas of this HpaEventResponse.

        **参数解释：** 扩缩容前实例数。 **取值范围：** 不涉及。

        :param current_replicas: The current_replicas of this HpaEventResponse.
        :type current_replicas: int
        """
        self._current_replicas = current_replicas

    @property
    def target_replicas(self):
        r"""Gets the target_replicas of this HpaEventResponse.

        **参数解释：** 预设目标实例数。 **取值范围：** 不涉及。

        :return: The target_replicas of this HpaEventResponse.
        :rtype: int
        """
        return self._target_replicas

    @target_replicas.setter
    def target_replicas(self, target_replicas):
        r"""Sets the target_replicas of this HpaEventResponse.

        **参数解释：** 预设目标实例数。 **取值范围：** 不涉及。

        :param target_replicas: The target_replicas of this HpaEventResponse.
        :type target_replicas: int
        """
        self._target_replicas = target_replicas

    @property
    def final_replicas(self):
        r"""Gets the final_replicas of this HpaEventResponse.

        **参数解释：** 扩缩容后实例数。 **取值范围：** 不涉及。

        :return: The final_replicas of this HpaEventResponse.
        :rtype: int
        """
        return self._final_replicas

    @final_replicas.setter
    def final_replicas(self, final_replicas):
        r"""Sets the final_replicas of this HpaEventResponse.

        **参数解释：** 扩缩容后实例数。 **取值范围：** 不涉及。

        :param final_replicas: The final_replicas of this HpaEventResponse.
        :type final_replicas: int
        """
        self._final_replicas = final_replicas

    @property
    def record_time(self):
        r"""Gets the record_time of this HpaEventResponse.

        **参数解释：** 执行记录时间。 **取值范围：** 2025-05-20 10:05:55

        :return: The record_time of this HpaEventResponse.
        :rtype: str
        """
        return self._record_time

    @record_time.setter
    def record_time(self, record_time):
        r"""Sets the record_time of this HpaEventResponse.

        **参数解释：** 执行记录时间。 **取值范围：** 2025-05-20 10:05:55

        :param record_time: The record_time of this HpaEventResponse.
        :type record_time: str
        """
        self._record_time = record_time

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
        if not isinstance(other, HpaEventResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
