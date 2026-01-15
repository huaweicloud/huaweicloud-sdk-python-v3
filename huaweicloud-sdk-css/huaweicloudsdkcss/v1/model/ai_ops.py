# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AiOps:

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
        'check_type': 'str',
        'trigger_type': 'str',
        'name': 'str',
        'desc': 'str',
        'status': 'int',
        'summary': 'SummaryInfo',
        'task_risks': 'list[AiOpsRiskObject]'
    }

    attribute_map = {
        'id': 'id',
        'check_type': 'check_type',
        'trigger_type': 'trigger_type',
        'name': 'name',
        'desc': 'desc',
        'status': 'status',
        'summary': 'summary',
        'task_risks': 'task_risks'
    }

    def __init__(self, id=None, check_type=None, trigger_type=None, name=None, desc=None, status=None, summary=None, task_risks=None):
        r"""AiOps

        The model defined in huaweicloud sdk

        :param id: **参数解释**： 集群风险检测任务ID。 **取值范围**： 不涉及
        :type id: str
        :param check_type: **参数解释**： 检测范围 **取值范围**： - full_detection：全量检测 - unavailability_detection：集群不可用检测 - partial_detection：部分检测
        :type check_type: str
        :param trigger_type: **参数解释**： 触发类型 **取值范围**： - manual：手动 - auto：自动
        :type trigger_type: str
        :param name: **参数解释**： 集群风险检测任务名称。 **取值范围**： 不涉及
        :type name: str
        :param desc: **参数解释**： 集群风险检测任务描述。 **取值范围**： 不涉及
        :type desc: str
        :param status: **参数解释**： 任务执行状态。 **取值范围**： - 150：未开启。 - 200：已开启。 - 300：已发送。
        :type status: int
        :param summary: 
        :type summary: :class:`huaweicloudsdkcss.v1.SummaryInfo`
        :param task_risks: **参数解释**： 集群风险项详情。 **取值范围**： 不涉及
        :type task_risks: list[:class:`huaweicloudsdkcss.v1.AiOpsRiskObject`]
        """
        
        

        self._id = None
        self._check_type = None
        self._trigger_type = None
        self._name = None
        self._desc = None
        self._status = None
        self._summary = None
        self._task_risks = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if check_type is not None:
            self.check_type = check_type
        if trigger_type is not None:
            self.trigger_type = trigger_type
        if name is not None:
            self.name = name
        if desc is not None:
            self.desc = desc
        if status is not None:
            self.status = status
        if summary is not None:
            self.summary = summary
        if task_risks is not None:
            self.task_risks = task_risks

    @property
    def id(self):
        r"""Gets the id of this AiOps.

        **参数解释**： 集群风险检测任务ID。 **取值范围**： 不涉及

        :return: The id of this AiOps.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this AiOps.

        **参数解释**： 集群风险检测任务ID。 **取值范围**： 不涉及

        :param id: The id of this AiOps.
        :type id: str
        """
        self._id = id

    @property
    def check_type(self):
        r"""Gets the check_type of this AiOps.

        **参数解释**： 检测范围 **取值范围**： - full_detection：全量检测 - unavailability_detection：集群不可用检测 - partial_detection：部分检测

        :return: The check_type of this AiOps.
        :rtype: str
        """
        return self._check_type

    @check_type.setter
    def check_type(self, check_type):
        r"""Sets the check_type of this AiOps.

        **参数解释**： 检测范围 **取值范围**： - full_detection：全量检测 - unavailability_detection：集群不可用检测 - partial_detection：部分检测

        :param check_type: The check_type of this AiOps.
        :type check_type: str
        """
        self._check_type = check_type

    @property
    def trigger_type(self):
        r"""Gets the trigger_type of this AiOps.

        **参数解释**： 触发类型 **取值范围**： - manual：手动 - auto：自动

        :return: The trigger_type of this AiOps.
        :rtype: str
        """
        return self._trigger_type

    @trigger_type.setter
    def trigger_type(self, trigger_type):
        r"""Sets the trigger_type of this AiOps.

        **参数解释**： 触发类型 **取值范围**： - manual：手动 - auto：自动

        :param trigger_type: The trigger_type of this AiOps.
        :type trigger_type: str
        """
        self._trigger_type = trigger_type

    @property
    def name(self):
        r"""Gets the name of this AiOps.

        **参数解释**： 集群风险检测任务名称。 **取值范围**： 不涉及

        :return: The name of this AiOps.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this AiOps.

        **参数解释**： 集群风险检测任务名称。 **取值范围**： 不涉及

        :param name: The name of this AiOps.
        :type name: str
        """
        self._name = name

    @property
    def desc(self):
        r"""Gets the desc of this AiOps.

        **参数解释**： 集群风险检测任务描述。 **取值范围**： 不涉及

        :return: The desc of this AiOps.
        :rtype: str
        """
        return self._desc

    @desc.setter
    def desc(self, desc):
        r"""Sets the desc of this AiOps.

        **参数解释**： 集群风险检测任务描述。 **取值范围**： 不涉及

        :param desc: The desc of this AiOps.
        :type desc: str
        """
        self._desc = desc

    @property
    def status(self):
        r"""Gets the status of this AiOps.

        **参数解释**： 任务执行状态。 **取值范围**： - 150：未开启。 - 200：已开启。 - 300：已发送。

        :return: The status of this AiOps.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this AiOps.

        **参数解释**： 任务执行状态。 **取值范围**： - 150：未开启。 - 200：已开启。 - 300：已发送。

        :param status: The status of this AiOps.
        :type status: int
        """
        self._status = status

    @property
    def summary(self):
        r"""Gets the summary of this AiOps.

        :return: The summary of this AiOps.
        :rtype: :class:`huaweicloudsdkcss.v1.SummaryInfo`
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        r"""Sets the summary of this AiOps.

        :param summary: The summary of this AiOps.
        :type summary: :class:`huaweicloudsdkcss.v1.SummaryInfo`
        """
        self._summary = summary

    @property
    def task_risks(self):
        r"""Gets the task_risks of this AiOps.

        **参数解释**： 集群风险项详情。 **取值范围**： 不涉及

        :return: The task_risks of this AiOps.
        :rtype: list[:class:`huaweicloudsdkcss.v1.AiOpsRiskObject`]
        """
        return self._task_risks

    @task_risks.setter
    def task_risks(self, task_risks):
        r"""Sets the task_risks of this AiOps.

        **参数解释**： 集群风险项详情。 **取值范围**： 不涉及

        :param task_risks: The task_risks of this AiOps.
        :type task_risks: list[:class:`huaweicloudsdkcss.v1.AiOpsRiskObject`]
        """
        self._task_risks = task_risks

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
        if not isinstance(other, AiOps):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
