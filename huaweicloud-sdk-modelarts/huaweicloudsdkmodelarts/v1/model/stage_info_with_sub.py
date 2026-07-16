# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StageInfoWithSub:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'job_id': 'str',
        'name': 'str',
        'en_message': 'str',
        'zh_message': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'stage_order': 'int',
        'sub_stages': 'list[SubStage]'
    }

    attribute_map = {
        'job_id': 'job_id',
        'name': 'name',
        'en_message': 'en_message',
        'zh_message': 'zh_message',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'stage_order': 'stage_order',
        'sub_stages': 'sub_stages'
    }

    def __init__(self, job_id=None, name=None, en_message=None, zh_message=None, start_time=None, end_time=None, stage_order=None, sub_stages=None):
        r"""StageInfoWithSub

        The model defined in huaweicloud sdk

        :param job_id: **参数解释**：作业ID。 **取值范围**：不涉及。
        :type job_id: str
        :param name: **参数解释**：主阶段名称。  **取值范围**： - scheduling：作业调度 - preparing：环境准备 - running：作业运行 - end：作业结束
        :type name: str
        :param en_message: **参数解释**：主阶段英文描述信息。  **取值范围**：不涉及。
        :type en_message: str
        :param zh_message: **参数解释**：主阶段中文描述信息。  **取值范围**：不涉及。
        :type zh_message: str
        :param start_time: **参数解释**：主阶段开始时间。  **取值范围**：不涉及。
        :type start_time: str
        :param end_time: **参数解释**：主阶段结束时间。  **取值范围**：不涉及。
        :type end_time: str
        :param stage_order: **参数解释**：主阶段序号。 **取值范围**：[1,4]。
        :type stage_order: int
        :param sub_stages: **参数解释**：子阶段信息列表。
        :type sub_stages: list[:class:`huaweicloudsdkmodelarts.v1.SubStage`]
        """
        
        

        self._job_id = None
        self._name = None
        self._en_message = None
        self._zh_message = None
        self._start_time = None
        self._end_time = None
        self._stage_order = None
        self._sub_stages = None
        self.discriminator = None

        if job_id is not None:
            self.job_id = job_id
        if name is not None:
            self.name = name
        if en_message is not None:
            self.en_message = en_message
        if zh_message is not None:
            self.zh_message = zh_message
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if stage_order is not None:
            self.stage_order = stage_order
        if sub_stages is not None:
            self.sub_stages = sub_stages

    @property
    def job_id(self):
        r"""Gets the job_id of this StageInfoWithSub.

        **参数解释**：作业ID。 **取值范围**：不涉及。

        :return: The job_id of this StageInfoWithSub.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this StageInfoWithSub.

        **参数解释**：作业ID。 **取值范围**：不涉及。

        :param job_id: The job_id of this StageInfoWithSub.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def name(self):
        r"""Gets the name of this StageInfoWithSub.

        **参数解释**：主阶段名称。  **取值范围**： - scheduling：作业调度 - preparing：环境准备 - running：作业运行 - end：作业结束

        :return: The name of this StageInfoWithSub.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this StageInfoWithSub.

        **参数解释**：主阶段名称。  **取值范围**： - scheduling：作业调度 - preparing：环境准备 - running：作业运行 - end：作业结束

        :param name: The name of this StageInfoWithSub.
        :type name: str
        """
        self._name = name

    @property
    def en_message(self):
        r"""Gets the en_message of this StageInfoWithSub.

        **参数解释**：主阶段英文描述信息。  **取值范围**：不涉及。

        :return: The en_message of this StageInfoWithSub.
        :rtype: str
        """
        return self._en_message

    @en_message.setter
    def en_message(self, en_message):
        r"""Sets the en_message of this StageInfoWithSub.

        **参数解释**：主阶段英文描述信息。  **取值范围**：不涉及。

        :param en_message: The en_message of this StageInfoWithSub.
        :type en_message: str
        """
        self._en_message = en_message

    @property
    def zh_message(self):
        r"""Gets the zh_message of this StageInfoWithSub.

        **参数解释**：主阶段中文描述信息。  **取值范围**：不涉及。

        :return: The zh_message of this StageInfoWithSub.
        :rtype: str
        """
        return self._zh_message

    @zh_message.setter
    def zh_message(self, zh_message):
        r"""Sets the zh_message of this StageInfoWithSub.

        **参数解释**：主阶段中文描述信息。  **取值范围**：不涉及。

        :param zh_message: The zh_message of this StageInfoWithSub.
        :type zh_message: str
        """
        self._zh_message = zh_message

    @property
    def start_time(self):
        r"""Gets the start_time of this StageInfoWithSub.

        **参数解释**：主阶段开始时间。  **取值范围**：不涉及。

        :return: The start_time of this StageInfoWithSub.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this StageInfoWithSub.

        **参数解释**：主阶段开始时间。  **取值范围**：不涉及。

        :param start_time: The start_time of this StageInfoWithSub.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this StageInfoWithSub.

        **参数解释**：主阶段结束时间。  **取值范围**：不涉及。

        :return: The end_time of this StageInfoWithSub.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this StageInfoWithSub.

        **参数解释**：主阶段结束时间。  **取值范围**：不涉及。

        :param end_time: The end_time of this StageInfoWithSub.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def stage_order(self):
        r"""Gets the stage_order of this StageInfoWithSub.

        **参数解释**：主阶段序号。 **取值范围**：[1,4]。

        :return: The stage_order of this StageInfoWithSub.
        :rtype: int
        """
        return self._stage_order

    @stage_order.setter
    def stage_order(self, stage_order):
        r"""Sets the stage_order of this StageInfoWithSub.

        **参数解释**：主阶段序号。 **取值范围**：[1,4]。

        :param stage_order: The stage_order of this StageInfoWithSub.
        :type stage_order: int
        """
        self._stage_order = stage_order

    @property
    def sub_stages(self):
        r"""Gets the sub_stages of this StageInfoWithSub.

        **参数解释**：子阶段信息列表。

        :return: The sub_stages of this StageInfoWithSub.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.SubStage`]
        """
        return self._sub_stages

    @sub_stages.setter
    def sub_stages(self, sub_stages):
        r"""Sets the sub_stages of this StageInfoWithSub.

        **参数解释**：子阶段信息列表。

        :param sub_stages: The sub_stages of this StageInfoWithSub.
        :type sub_stages: list[:class:`huaweicloudsdkmodelarts.v1.SubStage`]
        """
        self._sub_stages = sub_stages

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
        if not isinstance(other, StageInfoWithSub):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
