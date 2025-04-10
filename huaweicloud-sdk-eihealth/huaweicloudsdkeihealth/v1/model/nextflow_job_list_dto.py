# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NextflowJobListDto:

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
        'description': 'str',
        'labels': 'list[str]',
        'status': 'str',
        'has_ignore_failed_tasks': 'bool',
        'create_time': 'str',
        'finish_time': 'str',
        'failed_message': 'str',
        'failed_reason': 'str',
        'user_name': 'str',
        'workflow_name': 'str',
        'workflow_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'labels': 'labels',
        'status': 'status',
        'has_ignore_failed_tasks': 'has_ignore_failed_tasks',
        'create_time': 'create_time',
        'finish_time': 'finish_time',
        'failed_message': 'failed_message',
        'failed_reason': 'failed_reason',
        'user_name': 'user_name',
        'workflow_name': 'workflow_name',
        'workflow_id': 'workflow_id'
    }

    def __init__(self, id=None, name=None, description=None, labels=None, status=None, has_ignore_failed_tasks=None, create_time=None, finish_time=None, failed_message=None, failed_reason=None, user_name=None, workflow_name=None, workflow_id=None):
        r"""NextflowJobListDto

        The model defined in huaweicloud sdk

        :param id: 作业id
        :type id: str
        :param name: 作业的名称，取值范围：[1,63]，允许大小写字母、数字、以及特殊字符中划线(-)
        :type name: str
        :param description: 作业的描述,取值范围：输入字符最大长度为255
        :type description: str
        :param labels: 作业标签
        :type labels: list[str]
        :param status: 作业状态
        :type status: str
        :param has_ignore_failed_tasks: 是否包含已被忽略的失败tasks
        :type has_ignore_failed_tasks: bool
        :param create_time: 作业创建时间
        :type create_time: str
        :param finish_time: 作业结束时间
        :type finish_time: str
        :param failed_message: 失败提示，当作业执行失败时会返回
        :type failed_message: str
        :param failed_reason: 失败原因，当作业执行失败时会返回
        :type failed_reason: str
        :param user_name: 创建任务的用户名称
        :type user_name: str
        :param workflow_name: 流程名称
        :type workflow_name: str
        :param workflow_id: 流程id
        :type workflow_id: str
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._labels = None
        self._status = None
        self._has_ignore_failed_tasks = None
        self._create_time = None
        self._finish_time = None
        self._failed_message = None
        self._failed_reason = None
        self._user_name = None
        self._workflow_name = None
        self._workflow_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if labels is not None:
            self.labels = labels
        if status is not None:
            self.status = status
        if has_ignore_failed_tasks is not None:
            self.has_ignore_failed_tasks = has_ignore_failed_tasks
        if create_time is not None:
            self.create_time = create_time
        if finish_time is not None:
            self.finish_time = finish_time
        if failed_message is not None:
            self.failed_message = failed_message
        if failed_reason is not None:
            self.failed_reason = failed_reason
        if user_name is not None:
            self.user_name = user_name
        if workflow_name is not None:
            self.workflow_name = workflow_name
        if workflow_id is not None:
            self.workflow_id = workflow_id

    @property
    def id(self):
        r"""Gets the id of this NextflowJobListDto.

        作业id

        :return: The id of this NextflowJobListDto.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this NextflowJobListDto.

        作业id

        :param id: The id of this NextflowJobListDto.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this NextflowJobListDto.

        作业的名称，取值范围：[1,63]，允许大小写字母、数字、以及特殊字符中划线(-)

        :return: The name of this NextflowJobListDto.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this NextflowJobListDto.

        作业的名称，取值范围：[1,63]，允许大小写字母、数字、以及特殊字符中划线(-)

        :param name: The name of this NextflowJobListDto.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this NextflowJobListDto.

        作业的描述,取值范围：输入字符最大长度为255

        :return: The description of this NextflowJobListDto.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this NextflowJobListDto.

        作业的描述,取值范围：输入字符最大长度为255

        :param description: The description of this NextflowJobListDto.
        :type description: str
        """
        self._description = description

    @property
    def labels(self):
        r"""Gets the labels of this NextflowJobListDto.

        作业标签

        :return: The labels of this NextflowJobListDto.
        :rtype: list[str]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        r"""Sets the labels of this NextflowJobListDto.

        作业标签

        :param labels: The labels of this NextflowJobListDto.
        :type labels: list[str]
        """
        self._labels = labels

    @property
    def status(self):
        r"""Gets the status of this NextflowJobListDto.

        作业状态

        :return: The status of this NextflowJobListDto.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this NextflowJobListDto.

        作业状态

        :param status: The status of this NextflowJobListDto.
        :type status: str
        """
        self._status = status

    @property
    def has_ignore_failed_tasks(self):
        r"""Gets the has_ignore_failed_tasks of this NextflowJobListDto.

        是否包含已被忽略的失败tasks

        :return: The has_ignore_failed_tasks of this NextflowJobListDto.
        :rtype: bool
        """
        return self._has_ignore_failed_tasks

    @has_ignore_failed_tasks.setter
    def has_ignore_failed_tasks(self, has_ignore_failed_tasks):
        r"""Sets the has_ignore_failed_tasks of this NextflowJobListDto.

        是否包含已被忽略的失败tasks

        :param has_ignore_failed_tasks: The has_ignore_failed_tasks of this NextflowJobListDto.
        :type has_ignore_failed_tasks: bool
        """
        self._has_ignore_failed_tasks = has_ignore_failed_tasks

    @property
    def create_time(self):
        r"""Gets the create_time of this NextflowJobListDto.

        作业创建时间

        :return: The create_time of this NextflowJobListDto.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this NextflowJobListDto.

        作业创建时间

        :param create_time: The create_time of this NextflowJobListDto.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def finish_time(self):
        r"""Gets the finish_time of this NextflowJobListDto.

        作业结束时间

        :return: The finish_time of this NextflowJobListDto.
        :rtype: str
        """
        return self._finish_time

    @finish_time.setter
    def finish_time(self, finish_time):
        r"""Sets the finish_time of this NextflowJobListDto.

        作业结束时间

        :param finish_time: The finish_time of this NextflowJobListDto.
        :type finish_time: str
        """
        self._finish_time = finish_time

    @property
    def failed_message(self):
        r"""Gets the failed_message of this NextflowJobListDto.

        失败提示，当作业执行失败时会返回

        :return: The failed_message of this NextflowJobListDto.
        :rtype: str
        """
        return self._failed_message

    @failed_message.setter
    def failed_message(self, failed_message):
        r"""Sets the failed_message of this NextflowJobListDto.

        失败提示，当作业执行失败时会返回

        :param failed_message: The failed_message of this NextflowJobListDto.
        :type failed_message: str
        """
        self._failed_message = failed_message

    @property
    def failed_reason(self):
        r"""Gets the failed_reason of this NextflowJobListDto.

        失败原因，当作业执行失败时会返回

        :return: The failed_reason of this NextflowJobListDto.
        :rtype: str
        """
        return self._failed_reason

    @failed_reason.setter
    def failed_reason(self, failed_reason):
        r"""Sets the failed_reason of this NextflowJobListDto.

        失败原因，当作业执行失败时会返回

        :param failed_reason: The failed_reason of this NextflowJobListDto.
        :type failed_reason: str
        """
        self._failed_reason = failed_reason

    @property
    def user_name(self):
        r"""Gets the user_name of this NextflowJobListDto.

        创建任务的用户名称

        :return: The user_name of this NextflowJobListDto.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this NextflowJobListDto.

        创建任务的用户名称

        :param user_name: The user_name of this NextflowJobListDto.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def workflow_name(self):
        r"""Gets the workflow_name of this NextflowJobListDto.

        流程名称

        :return: The workflow_name of this NextflowJobListDto.
        :rtype: str
        """
        return self._workflow_name

    @workflow_name.setter
    def workflow_name(self, workflow_name):
        r"""Sets the workflow_name of this NextflowJobListDto.

        流程名称

        :param workflow_name: The workflow_name of this NextflowJobListDto.
        :type workflow_name: str
        """
        self._workflow_name = workflow_name

    @property
    def workflow_id(self):
        r"""Gets the workflow_id of this NextflowJobListDto.

        流程id

        :return: The workflow_id of this NextflowJobListDto.
        :rtype: str
        """
        return self._workflow_id

    @workflow_id.setter
    def workflow_id(self, workflow_id):
        r"""Sets the workflow_id of this NextflowJobListDto.

        流程id

        :param workflow_id: The workflow_id of this NextflowJobListDto.
        :type workflow_id: str
        """
        self._workflow_id = workflow_id

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
        if not isinstance(other, NextflowJobListDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
