# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NotifyTrainingJobInformationRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'training_job_id': 'str',
        'task_id': 'str',
        'report_type': 'str',
        'body': 'ReportEventBody'
    }

    attribute_map = {
        'training_job_id': 'training_job_id',
        'task_id': 'task_id',
        'report_type': 'report_type',
        'body': 'body'
    }

    def __init__(self, training_job_id=None, task_id=None, report_type=None, body=None):
        r"""NotifyTrainingJobInformationRequest

        The model defined in huaweicloud sdk

        :param training_job_id: **参数解释**：训练作业ID。获取方法请参见[查询训练作业列表](ListTrainingJobs.xml)。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type training_job_id: str
        :param task_id: **参数解释**：训练作业的任务名称。可从训练作业详情中的status.tasks字段中获取。 **约束限制**：单节点默认为\&quot;worker-0\&quot;，多节点则为\&quot;worker-0\&quot;、\&quot;worker-1\&quot;，依次类推。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type task_id: str
        :param report_type: **参数解释**：事件上报类型。 **约束限制**：不涉及。 **取值范围**：取\&quot;training-event\&quot;。 **默认取值**：不涉及。
        :type report_type: str
        :param body: Body of the NotifyTrainingJobInformationRequest
        :type body: :class:`huaweicloudsdkmodelarts.v1.ReportEventBody`
        """
        
        

        self._training_job_id = None
        self._task_id = None
        self._report_type = None
        self._body = None
        self.discriminator = None

        self.training_job_id = training_job_id
        self.task_id = task_id
        self.report_type = report_type
        if body is not None:
            self.body = body

    @property
    def training_job_id(self):
        r"""Gets the training_job_id of this NotifyTrainingJobInformationRequest.

        **参数解释**：训练作业ID。获取方法请参见[查询训练作业列表](ListTrainingJobs.xml)。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The training_job_id of this NotifyTrainingJobInformationRequest.
        :rtype: str
        """
        return self._training_job_id

    @training_job_id.setter
    def training_job_id(self, training_job_id):
        r"""Sets the training_job_id of this NotifyTrainingJobInformationRequest.

        **参数解释**：训练作业ID。获取方法请参见[查询训练作业列表](ListTrainingJobs.xml)。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param training_job_id: The training_job_id of this NotifyTrainingJobInformationRequest.
        :type training_job_id: str
        """
        self._training_job_id = training_job_id

    @property
    def task_id(self):
        r"""Gets the task_id of this NotifyTrainingJobInformationRequest.

        **参数解释**：训练作业的任务名称。可从训练作业详情中的status.tasks字段中获取。 **约束限制**：单节点默认为\"worker-0\"，多节点则为\"worker-0\"、\"worker-1\"，依次类推。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The task_id of this NotifyTrainingJobInformationRequest.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this NotifyTrainingJobInformationRequest.

        **参数解释**：训练作业的任务名称。可从训练作业详情中的status.tasks字段中获取。 **约束限制**：单节点默认为\"worker-0\"，多节点则为\"worker-0\"、\"worker-1\"，依次类推。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param task_id: The task_id of this NotifyTrainingJobInformationRequest.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def report_type(self):
        r"""Gets the report_type of this NotifyTrainingJobInformationRequest.

        **参数解释**：事件上报类型。 **约束限制**：不涉及。 **取值范围**：取\"training-event\"。 **默认取值**：不涉及。

        :return: The report_type of this NotifyTrainingJobInformationRequest.
        :rtype: str
        """
        return self._report_type

    @report_type.setter
    def report_type(self, report_type):
        r"""Sets the report_type of this NotifyTrainingJobInformationRequest.

        **参数解释**：事件上报类型。 **约束限制**：不涉及。 **取值范围**：取\"training-event\"。 **默认取值**：不涉及。

        :param report_type: The report_type of this NotifyTrainingJobInformationRequest.
        :type report_type: str
        """
        self._report_type = report_type

    @property
    def body(self):
        r"""Gets the body of this NotifyTrainingJobInformationRequest.

        :return: The body of this NotifyTrainingJobInformationRequest.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ReportEventBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this NotifyTrainingJobInformationRequest.

        :param body: The body of this NotifyTrainingJobInformationRequest.
        :type body: :class:`huaweicloudsdkmodelarts.v1.ReportEventBody`
        """
        self._body = body

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
        if not isinstance(other, NotifyTrainingJobInformationRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
