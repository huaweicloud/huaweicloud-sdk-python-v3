# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAiOpsRequestBodyAiopsList:

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
        'name': 'str',
        'desc': 'str',
        'status': 'int',
        'summary': 'ListAiOpsRequestBodySummary',
        'create_time': 'str',
        'smn_status': 'str',
        'smn_fail_reason': 'str',
        'task_risks': 'list[AIOpsRiskInfo]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'desc': 'desc',
        'status': 'status',
        'summary': 'summary',
        'create_time': 'create_time',
        'smn_status': 'smn_status',
        'smn_fail_reason': 'smn_fail_reason',
        'task_risks': 'task_risks'
    }

    def __init__(self, id=None, name=None, desc=None, status=None, summary=None, create_time=None, smn_status=None, smn_fail_reason=None, task_risks=None):
        """ListAiOpsRequestBodyAiopsList

        The model defined in huaweicloud sdk

        :param id: 检测任务id。
        :type id: str
        :param name: 检测任务名称。
        :type name: str
        :param desc: 检测任务描述。
        :type desc: str
        :param status: 任务执行状态。 - 150：未开启。 - 200：已开启。 - 300：已发送。
        :type status: int
        :param summary: 
        :type summary: :class:`huaweicloudsdkcss.v1.ListAiOpsRequestBodySummary`
        :param create_time: 检测任务创建时间戳。
        :type create_time: str
        :param smn_status: 检测任务SMN告警任务发送状态。 - not_open：未开启。 - not_trigger：未触发。 - sent：已发送。 - send_fail： 发送失败。
        :type smn_status: str
        :param smn_fail_reason: 发送失败原因。
        :type smn_fail_reason: str
        :param task_risks: 风险项详情。
        :type task_risks: list[:class:`huaweicloudsdkcss.v1.AIOpsRiskInfo`]
        """
        
        

        self._id = None
        self._name = None
        self._desc = None
        self._status = None
        self._summary = None
        self._create_time = None
        self._smn_status = None
        self._smn_fail_reason = None
        self._task_risks = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if desc is not None:
            self.desc = desc
        if status is not None:
            self.status = status
        if summary is not None:
            self.summary = summary
        if create_time is not None:
            self.create_time = create_time
        if smn_status is not None:
            self.smn_status = smn_status
        if smn_fail_reason is not None:
            self.smn_fail_reason = smn_fail_reason
        if task_risks is not None:
            self.task_risks = task_risks

    @property
    def id(self):
        """Gets the id of this ListAiOpsRequestBodyAiopsList.

        检测任务id。

        :return: The id of this ListAiOpsRequestBodyAiopsList.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListAiOpsRequestBodyAiopsList.

        检测任务id。

        :param id: The id of this ListAiOpsRequestBodyAiopsList.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ListAiOpsRequestBodyAiopsList.

        检测任务名称。

        :return: The name of this ListAiOpsRequestBodyAiopsList.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListAiOpsRequestBodyAiopsList.

        检测任务名称。

        :param name: The name of this ListAiOpsRequestBodyAiopsList.
        :type name: str
        """
        self._name = name

    @property
    def desc(self):
        """Gets the desc of this ListAiOpsRequestBodyAiopsList.

        检测任务描述。

        :return: The desc of this ListAiOpsRequestBodyAiopsList.
        :rtype: str
        """
        return self._desc

    @desc.setter
    def desc(self, desc):
        """Sets the desc of this ListAiOpsRequestBodyAiopsList.

        检测任务描述。

        :param desc: The desc of this ListAiOpsRequestBodyAiopsList.
        :type desc: str
        """
        self._desc = desc

    @property
    def status(self):
        """Gets the status of this ListAiOpsRequestBodyAiopsList.

        任务执行状态。 - 150：未开启。 - 200：已开启。 - 300：已发送。

        :return: The status of this ListAiOpsRequestBodyAiopsList.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListAiOpsRequestBodyAiopsList.

        任务执行状态。 - 150：未开启。 - 200：已开启。 - 300：已发送。

        :param status: The status of this ListAiOpsRequestBodyAiopsList.
        :type status: int
        """
        self._status = status

    @property
    def summary(self):
        """Gets the summary of this ListAiOpsRequestBodyAiopsList.

        :return: The summary of this ListAiOpsRequestBodyAiopsList.
        :rtype: :class:`huaweicloudsdkcss.v1.ListAiOpsRequestBodySummary`
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """Sets the summary of this ListAiOpsRequestBodyAiopsList.

        :param summary: The summary of this ListAiOpsRequestBodyAiopsList.
        :type summary: :class:`huaweicloudsdkcss.v1.ListAiOpsRequestBodySummary`
        """
        self._summary = summary

    @property
    def create_time(self):
        """Gets the create_time of this ListAiOpsRequestBodyAiopsList.

        检测任务创建时间戳。

        :return: The create_time of this ListAiOpsRequestBodyAiopsList.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ListAiOpsRequestBodyAiopsList.

        检测任务创建时间戳。

        :param create_time: The create_time of this ListAiOpsRequestBodyAiopsList.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def smn_status(self):
        """Gets the smn_status of this ListAiOpsRequestBodyAiopsList.

        检测任务SMN告警任务发送状态。 - not_open：未开启。 - not_trigger：未触发。 - sent：已发送。 - send_fail： 发送失败。

        :return: The smn_status of this ListAiOpsRequestBodyAiopsList.
        :rtype: str
        """
        return self._smn_status

    @smn_status.setter
    def smn_status(self, smn_status):
        """Sets the smn_status of this ListAiOpsRequestBodyAiopsList.

        检测任务SMN告警任务发送状态。 - not_open：未开启。 - not_trigger：未触发。 - sent：已发送。 - send_fail： 发送失败。

        :param smn_status: The smn_status of this ListAiOpsRequestBodyAiopsList.
        :type smn_status: str
        """
        self._smn_status = smn_status

    @property
    def smn_fail_reason(self):
        """Gets the smn_fail_reason of this ListAiOpsRequestBodyAiopsList.

        发送失败原因。

        :return: The smn_fail_reason of this ListAiOpsRequestBodyAiopsList.
        :rtype: str
        """
        return self._smn_fail_reason

    @smn_fail_reason.setter
    def smn_fail_reason(self, smn_fail_reason):
        """Sets the smn_fail_reason of this ListAiOpsRequestBodyAiopsList.

        发送失败原因。

        :param smn_fail_reason: The smn_fail_reason of this ListAiOpsRequestBodyAiopsList.
        :type smn_fail_reason: str
        """
        self._smn_fail_reason = smn_fail_reason

    @property
    def task_risks(self):
        """Gets the task_risks of this ListAiOpsRequestBodyAiopsList.

        风险项详情。

        :return: The task_risks of this ListAiOpsRequestBodyAiopsList.
        :rtype: list[:class:`huaweicloudsdkcss.v1.AIOpsRiskInfo`]
        """
        return self._task_risks

    @task_risks.setter
    def task_risks(self, task_risks):
        """Sets the task_risks of this ListAiOpsRequestBodyAiopsList.

        风险项详情。

        :param task_risks: The task_risks of this ListAiOpsRequestBodyAiopsList.
        :type task_risks: list[:class:`huaweicloudsdkcss.v1.AIOpsRiskInfo`]
        """
        self._task_risks = task_risks

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListAiOpsRequestBodyAiopsList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
