# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTaskDetailsResponse(SdkResponse):

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
        'instance_name': 'str',
        'job_id': 'str',
        'job_name': 'str',
        'status': 'str',
        'sub_task_list': 'list[SubTaskInfo]'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'instance_name': 'instance_name',
        'job_id': 'job_id',
        'job_name': 'job_name',
        'status': 'status',
        'sub_task_list': 'sub_task_list'
    }

    def __init__(self, instance_id=None, instance_name=None, job_id=None, job_name=None, status=None, sub_task_list=None):
        r"""ShowTaskDetailsResponse

        The model defined in huaweicloud sdk

        :param instance_id: **参数解释**：  实例ID。  **取值范围**：  不涉及。
        :type instance_id: str
        :param instance_name: **参数解释**：  实例名称。  **取值范围**：  不涉及。
        :type instance_name: str
        :param job_id: **参数解释**：  任务ID。  **取值范围**：  不涉及。
        :type job_id: str
        :param job_name: **参数解释**：  任务名称。  **取值范围**：  不涉及。
        :type job_name: str
        :param status: **参数解释**：  任务状态。  **取值范围**：    - Pending：表示待执行。   - Running：表示运行中。   - Completed：表示已完成。
        :type status: str
        :param sub_task_list: **参数解释**：  任务详情列表。  **取值范围**：  不涉及。
        :type sub_task_list: list[:class:`huaweicloudsdkgaussdb.v3.SubTaskInfo`]
        """
        
        super().__init__()

        self._instance_id = None
        self._instance_name = None
        self._job_id = None
        self._job_name = None
        self._status = None
        self._sub_task_list = None
        self.discriminator = None

        if instance_id is not None:
            self.instance_id = instance_id
        if instance_name is not None:
            self.instance_name = instance_name
        if job_id is not None:
            self.job_id = job_id
        if job_name is not None:
            self.job_name = job_name
        if status is not None:
            self.status = status
        if sub_task_list is not None:
            self.sub_task_list = sub_task_list

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ShowTaskDetailsResponse.

        **参数解释**：  实例ID。  **取值范围**：  不涉及。

        :return: The instance_id of this ShowTaskDetailsResponse.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ShowTaskDetailsResponse.

        **参数解释**：  实例ID。  **取值范围**：  不涉及。

        :param instance_id: The instance_id of this ShowTaskDetailsResponse.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def instance_name(self):
        r"""Gets the instance_name of this ShowTaskDetailsResponse.

        **参数解释**：  实例名称。  **取值范围**：  不涉及。

        :return: The instance_name of this ShowTaskDetailsResponse.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        r"""Sets the instance_name of this ShowTaskDetailsResponse.

        **参数解释**：  实例名称。  **取值范围**：  不涉及。

        :param instance_name: The instance_name of this ShowTaskDetailsResponse.
        :type instance_name: str
        """
        self._instance_name = instance_name

    @property
    def job_id(self):
        r"""Gets the job_id of this ShowTaskDetailsResponse.

        **参数解释**：  任务ID。  **取值范围**：  不涉及。

        :return: The job_id of this ShowTaskDetailsResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this ShowTaskDetailsResponse.

        **参数解释**：  任务ID。  **取值范围**：  不涉及。

        :param job_id: The job_id of this ShowTaskDetailsResponse.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def job_name(self):
        r"""Gets the job_name of this ShowTaskDetailsResponse.

        **参数解释**：  任务名称。  **取值范围**：  不涉及。

        :return: The job_name of this ShowTaskDetailsResponse.
        :rtype: str
        """
        return self._job_name

    @job_name.setter
    def job_name(self, job_name):
        r"""Sets the job_name of this ShowTaskDetailsResponse.

        **参数解释**：  任务名称。  **取值范围**：  不涉及。

        :param job_name: The job_name of this ShowTaskDetailsResponse.
        :type job_name: str
        """
        self._job_name = job_name

    @property
    def status(self):
        r"""Gets the status of this ShowTaskDetailsResponse.

        **参数解释**：  任务状态。  **取值范围**：    - Pending：表示待执行。   - Running：表示运行中。   - Completed：表示已完成。

        :return: The status of this ShowTaskDetailsResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowTaskDetailsResponse.

        **参数解释**：  任务状态。  **取值范围**：    - Pending：表示待执行。   - Running：表示运行中。   - Completed：表示已完成。

        :param status: The status of this ShowTaskDetailsResponse.
        :type status: str
        """
        self._status = status

    @property
    def sub_task_list(self):
        r"""Gets the sub_task_list of this ShowTaskDetailsResponse.

        **参数解释**：  任务详情列表。  **取值范围**：  不涉及。

        :return: The sub_task_list of this ShowTaskDetailsResponse.
        :rtype: list[:class:`huaweicloudsdkgaussdb.v3.SubTaskInfo`]
        """
        return self._sub_task_list

    @sub_task_list.setter
    def sub_task_list(self, sub_task_list):
        r"""Sets the sub_task_list of this ShowTaskDetailsResponse.

        **参数解释**：  任务详情列表。  **取值范围**：  不涉及。

        :param sub_task_list: The sub_task_list of this ShowTaskDetailsResponse.
        :type sub_task_list: list[:class:`huaweicloudsdkgaussdb.v3.SubTaskInfo`]
        """
        self._sub_task_list = sub_task_list

    def to_dict(self):
        import warnings
        warnings.warn("ShowTaskDetailsResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ShowTaskDetailsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
