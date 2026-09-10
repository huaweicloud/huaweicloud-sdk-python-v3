# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OpsAnalysisTaskInstanceListInfo:

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
        'status': 'str',
        'planned_start_time': 'int',
        'instance_start_time': 'int',
        'instance_end_time': 'int',
        'data_start_time': 'int',
        'data_end_time': 'int',
        'reason': 'str'
    }

    attribute_map = {
        'id': 'id',
        'status': 'status',
        'planned_start_time': 'planned_start_time',
        'instance_start_time': 'instance_start_time',
        'instance_end_time': 'instance_end_time',
        'data_start_time': 'data_start_time',
        'data_end_time': 'data_end_time',
        'reason': 'reason'
    }

    def __init__(self, id=None, status=None, planned_start_time=None, instance_start_time=None, instance_end_time=None, data_start_time=None, data_end_time=None, reason=None):
        r"""OpsAnalysisTaskInstanceListInfo

        The model defined in huaweicloud sdk

        :param id: **参数解释：** 分析任务具体执行instance的ID。  **取值范围：** UUID格式字符串。
        :type id: str
        :param status: **参数解释：** 分析任务具体执行instance的状态。  **取值范围：** scheduled: 待运行，running：运行中，skipped：跳过，success：成功完成，fail：运行失败，stopped：已停止。
        :type status: str
        :param planned_start_time: **参数解释：** 分析任务具体执行instance的计划执行时间，单位：毫秒（13位时间戳）。  **取值范围：** 13位毫秒级时间戳。
        :type planned_start_time: int
        :param instance_start_time: **参数解释：** 分析任务具体执行instance的实际开始执行时间，单位：毫秒（13位时间戳）。instance 尚未被认领执行时为 null。  **取值范围：** 13位毫秒级时间戳或 null。
        :type instance_start_time: int
        :param instance_end_time: **参数解释：** 分析任务具体执行instance的实际完成时间，单位：毫秒（13位时间戳）。instance 尚未完成时为 null。  **取值范围：** 13位毫秒级时间戳或 null。
        :type instance_end_time: int
        :param data_start_time: **参数解释：** 分析任务具体执行instance所分析的链路数据的起始时间，单位：毫秒（13位时间戳）。 **取值范围：** 13位毫秒级时间戳。
        :type data_start_time: int
        :param data_end_time: **参数解释：** 分析任务具体执行instance所分析的链路数据的截止时间，单位：毫秒（13位时间戳）。  **取值范围：** 13位毫秒级时间戳。
        :type data_end_time: int
        :param reason: **参数解释：** instance失败或跳过的原因。success 时为 null。  **取值范围：** 不涉及
        :type reason: str
        """
        
        

        self._id = None
        self._status = None
        self._planned_start_time = None
        self._instance_start_time = None
        self._instance_end_time = None
        self._data_start_time = None
        self._data_end_time = None
        self._reason = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if status is not None:
            self.status = status
        if planned_start_time is not None:
            self.planned_start_time = planned_start_time
        if instance_start_time is not None:
            self.instance_start_time = instance_start_time
        if instance_end_time is not None:
            self.instance_end_time = instance_end_time
        if data_start_time is not None:
            self.data_start_time = data_start_time
        if data_end_time is not None:
            self.data_end_time = data_end_time
        if reason is not None:
            self.reason = reason

    @property
    def id(self):
        r"""Gets the id of this OpsAnalysisTaskInstanceListInfo.

        **参数解释：** 分析任务具体执行instance的ID。  **取值范围：** UUID格式字符串。

        :return: The id of this OpsAnalysisTaskInstanceListInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this OpsAnalysisTaskInstanceListInfo.

        **参数解释：** 分析任务具体执行instance的ID。  **取值范围：** UUID格式字符串。

        :param id: The id of this OpsAnalysisTaskInstanceListInfo.
        :type id: str
        """
        self._id = id

    @property
    def status(self):
        r"""Gets the status of this OpsAnalysisTaskInstanceListInfo.

        **参数解释：** 分析任务具体执行instance的状态。  **取值范围：** scheduled: 待运行，running：运行中，skipped：跳过，success：成功完成，fail：运行失败，stopped：已停止。

        :return: The status of this OpsAnalysisTaskInstanceListInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this OpsAnalysisTaskInstanceListInfo.

        **参数解释：** 分析任务具体执行instance的状态。  **取值范围：** scheduled: 待运行，running：运行中，skipped：跳过，success：成功完成，fail：运行失败，stopped：已停止。

        :param status: The status of this OpsAnalysisTaskInstanceListInfo.
        :type status: str
        """
        self._status = status

    @property
    def planned_start_time(self):
        r"""Gets the planned_start_time of this OpsAnalysisTaskInstanceListInfo.

        **参数解释：** 分析任务具体执行instance的计划执行时间，单位：毫秒（13位时间戳）。  **取值范围：** 13位毫秒级时间戳。

        :return: The planned_start_time of this OpsAnalysisTaskInstanceListInfo.
        :rtype: int
        """
        return self._planned_start_time

    @planned_start_time.setter
    def planned_start_time(self, planned_start_time):
        r"""Sets the planned_start_time of this OpsAnalysisTaskInstanceListInfo.

        **参数解释：** 分析任务具体执行instance的计划执行时间，单位：毫秒（13位时间戳）。  **取值范围：** 13位毫秒级时间戳。

        :param planned_start_time: The planned_start_time of this OpsAnalysisTaskInstanceListInfo.
        :type planned_start_time: int
        """
        self._planned_start_time = planned_start_time

    @property
    def instance_start_time(self):
        r"""Gets the instance_start_time of this OpsAnalysisTaskInstanceListInfo.

        **参数解释：** 分析任务具体执行instance的实际开始执行时间，单位：毫秒（13位时间戳）。instance 尚未被认领执行时为 null。  **取值范围：** 13位毫秒级时间戳或 null。

        :return: The instance_start_time of this OpsAnalysisTaskInstanceListInfo.
        :rtype: int
        """
        return self._instance_start_time

    @instance_start_time.setter
    def instance_start_time(self, instance_start_time):
        r"""Sets the instance_start_time of this OpsAnalysisTaskInstanceListInfo.

        **参数解释：** 分析任务具体执行instance的实际开始执行时间，单位：毫秒（13位时间戳）。instance 尚未被认领执行时为 null。  **取值范围：** 13位毫秒级时间戳或 null。

        :param instance_start_time: The instance_start_time of this OpsAnalysisTaskInstanceListInfo.
        :type instance_start_time: int
        """
        self._instance_start_time = instance_start_time

    @property
    def instance_end_time(self):
        r"""Gets the instance_end_time of this OpsAnalysisTaskInstanceListInfo.

        **参数解释：** 分析任务具体执行instance的实际完成时间，单位：毫秒（13位时间戳）。instance 尚未完成时为 null。  **取值范围：** 13位毫秒级时间戳或 null。

        :return: The instance_end_time of this OpsAnalysisTaskInstanceListInfo.
        :rtype: int
        """
        return self._instance_end_time

    @instance_end_time.setter
    def instance_end_time(self, instance_end_time):
        r"""Sets the instance_end_time of this OpsAnalysisTaskInstanceListInfo.

        **参数解释：** 分析任务具体执行instance的实际完成时间，单位：毫秒（13位时间戳）。instance 尚未完成时为 null。  **取值范围：** 13位毫秒级时间戳或 null。

        :param instance_end_time: The instance_end_time of this OpsAnalysisTaskInstanceListInfo.
        :type instance_end_time: int
        """
        self._instance_end_time = instance_end_time

    @property
    def data_start_time(self):
        r"""Gets the data_start_time of this OpsAnalysisTaskInstanceListInfo.

        **参数解释：** 分析任务具体执行instance所分析的链路数据的起始时间，单位：毫秒（13位时间戳）。 **取值范围：** 13位毫秒级时间戳。

        :return: The data_start_time of this OpsAnalysisTaskInstanceListInfo.
        :rtype: int
        """
        return self._data_start_time

    @data_start_time.setter
    def data_start_time(self, data_start_time):
        r"""Sets the data_start_time of this OpsAnalysisTaskInstanceListInfo.

        **参数解释：** 分析任务具体执行instance所分析的链路数据的起始时间，单位：毫秒（13位时间戳）。 **取值范围：** 13位毫秒级时间戳。

        :param data_start_time: The data_start_time of this OpsAnalysisTaskInstanceListInfo.
        :type data_start_time: int
        """
        self._data_start_time = data_start_time

    @property
    def data_end_time(self):
        r"""Gets the data_end_time of this OpsAnalysisTaskInstanceListInfo.

        **参数解释：** 分析任务具体执行instance所分析的链路数据的截止时间，单位：毫秒（13位时间戳）。  **取值范围：** 13位毫秒级时间戳。

        :return: The data_end_time of this OpsAnalysisTaskInstanceListInfo.
        :rtype: int
        """
        return self._data_end_time

    @data_end_time.setter
    def data_end_time(self, data_end_time):
        r"""Sets the data_end_time of this OpsAnalysisTaskInstanceListInfo.

        **参数解释：** 分析任务具体执行instance所分析的链路数据的截止时间，单位：毫秒（13位时间戳）。  **取值范围：** 13位毫秒级时间戳。

        :param data_end_time: The data_end_time of this OpsAnalysisTaskInstanceListInfo.
        :type data_end_time: int
        """
        self._data_end_time = data_end_time

    @property
    def reason(self):
        r"""Gets the reason of this OpsAnalysisTaskInstanceListInfo.

        **参数解释：** instance失败或跳过的原因。success 时为 null。  **取值范围：** 不涉及

        :return: The reason of this OpsAnalysisTaskInstanceListInfo.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        r"""Sets the reason of this OpsAnalysisTaskInstanceListInfo.

        **参数解释：** instance失败或跳过的原因。success 时为 null。  **取值范围：** 不涉及

        :param reason: The reason of this OpsAnalysisTaskInstanceListInfo.
        :type reason: str
        """
        self._reason = reason

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
        if not isinstance(other, OpsAnalysisTaskInstanceListInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
