# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CoreSpaceJobSummary:

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
        'job_name': 'str',
        'status': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'job_name': 'job_name',
        'status': 'status',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, id=None, job_name=None, status=None, created_at=None, updated_at=None):
        r"""CoreSpaceJobSummary

        The model defined in huaweicloud sdk

        :param id: **参数解释：** 异步任务 ID，唯一标识一个异步任务，可通过创建异步任务的接口返回获取。 **取值范围：** 不涉及。 
        :type id: str
        :param job_name: **参数解释：** 异步任务名称，标识任务的类型。 **取值范围：** - create_space: 创建记忆库 - update_network: 更新网络配置 - [待补充]: 其他任务类型 
        :type job_name: str
        :param status: **参数解释：** 异步任务的当前执行状态。 **取值范围：** - running: 执行中 - success: 成功 - failed: 失败 
        :type status: str
        :param created_at: **参数解释：** 记录的创建时间，由系统自动生成，格式为 ISO 8601（YYYY-MM-DDTHH:mm:ssZ）。 **取值范围：** 不涉及。 
        :type created_at: datetime
        :param updated_at: **参数解释：** 记录的最近更新时间，由系统自动更新，格式为 ISO 8601（YYYY-MM-DDTHH:mm:ssZ）。 **取值范围：** 不涉及。 
        :type updated_at: datetime
        """
        
        

        self._id = None
        self._job_name = None
        self._status = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        self.id = id
        self.job_name = job_name
        self.status = status
        self.created_at = created_at
        self.updated_at = updated_at

    @property
    def id(self):
        r"""Gets the id of this CoreSpaceJobSummary.

        **参数解释：** 异步任务 ID，唯一标识一个异步任务，可通过创建异步任务的接口返回获取。 **取值范围：** 不涉及。 

        :return: The id of this CoreSpaceJobSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CoreSpaceJobSummary.

        **参数解释：** 异步任务 ID，唯一标识一个异步任务，可通过创建异步任务的接口返回获取。 **取值范围：** 不涉及。 

        :param id: The id of this CoreSpaceJobSummary.
        :type id: str
        """
        self._id = id

    @property
    def job_name(self):
        r"""Gets the job_name of this CoreSpaceJobSummary.

        **参数解释：** 异步任务名称，标识任务的类型。 **取值范围：** - create_space: 创建记忆库 - update_network: 更新网络配置 - [待补充]: 其他任务类型 

        :return: The job_name of this CoreSpaceJobSummary.
        :rtype: str
        """
        return self._job_name

    @job_name.setter
    def job_name(self, job_name):
        r"""Sets the job_name of this CoreSpaceJobSummary.

        **参数解释：** 异步任务名称，标识任务的类型。 **取值范围：** - create_space: 创建记忆库 - update_network: 更新网络配置 - [待补充]: 其他任务类型 

        :param job_name: The job_name of this CoreSpaceJobSummary.
        :type job_name: str
        """
        self._job_name = job_name

    @property
    def status(self):
        r"""Gets the status of this CoreSpaceJobSummary.

        **参数解释：** 异步任务的当前执行状态。 **取值范围：** - running: 执行中 - success: 成功 - failed: 失败 

        :return: The status of this CoreSpaceJobSummary.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this CoreSpaceJobSummary.

        **参数解释：** 异步任务的当前执行状态。 **取值范围：** - running: 执行中 - success: 成功 - failed: 失败 

        :param status: The status of this CoreSpaceJobSummary.
        :type status: str
        """
        self._status = status

    @property
    def created_at(self):
        r"""Gets the created_at of this CoreSpaceJobSummary.

        **参数解释：** 记录的创建时间，由系统自动生成，格式为 ISO 8601（YYYY-MM-DDTHH:mm:ssZ）。 **取值范围：** 不涉及。 

        :return: The created_at of this CoreSpaceJobSummary.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this CoreSpaceJobSummary.

        **参数解释：** 记录的创建时间，由系统自动生成，格式为 ISO 8601（YYYY-MM-DDTHH:mm:ssZ）。 **取值范围：** 不涉及。 

        :param created_at: The created_at of this CoreSpaceJobSummary.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this CoreSpaceJobSummary.

        **参数解释：** 记录的最近更新时间，由系统自动更新，格式为 ISO 8601（YYYY-MM-DDTHH:mm:ssZ）。 **取值范围：** 不涉及。 

        :return: The updated_at of this CoreSpaceJobSummary.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this CoreSpaceJobSummary.

        **参数解释：** 记录的最近更新时间，由系统自动更新，格式为 ISO 8601（YYYY-MM-DDTHH:mm:ssZ）。 **取值范围：** 不涉及。 

        :param updated_at: The updated_at of this CoreSpaceJobSummary.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

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
        if not isinstance(other, CoreSpaceJobSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
