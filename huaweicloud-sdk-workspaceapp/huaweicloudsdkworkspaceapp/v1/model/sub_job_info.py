# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SubJobInfo:

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
        'job_type': 'int',
        'job_status': 'int',
        'entities': 'list[JobResourceInfo]',
        'begin_time': 'datetime',
        'end_time': 'datetime',
        'expected_end_time': 'datetime',
        'execute_code': 'str',
        'execute_message': 'str'
    }

    attribute_map = {
        'job_id': 'job_id',
        'job_type': 'job_type',
        'job_status': 'job_status',
        'entities': 'entities',
        'begin_time': 'begin_time',
        'end_time': 'end_time',
        'expected_end_time': 'expected_end_time',
        'execute_code': 'execute_code',
        'execute_message': 'execute_message'
    }

    def __init__(self, job_id=None, job_type=None, job_status=None, entities=None, begin_time=None, end_time=None, expected_end_time=None, execute_code=None, execute_message=None):
        """SubJobInfo

        The model defined in huaweicloud sdk

        :param job_id: 子job标识
        :type job_id: str
        :param job_type: 任务类型，固定值2：子Job
        :type job_type: int
        :param job_status: job状态 - 0：失败。 - 1：成功。 - 2：处理中。 - 3：正在初始化。
        :type job_status: int
        :param entities: SubJob中处理的云服务/云资源对象。 创建、规格变更等场景是必填；冻结、解冻、删除等场景可空。
        :type entities: list[:class:`huaweicloudsdkworkspaceapp.v1.JobResourceInfo`]
        :param begin_time: 任务开始时间
        :type begin_time: datetime
        :param end_time: 任务结束时间
        :type end_time: datetime
        :param expected_end_time: 云服务预估的Job处理结束时间，只针对job有效，针对子job无效。
        :type expected_end_time: datetime
        :param execute_code: Job执行结果码
        :type execute_code: str
        :param execute_message: Job执行结果描述，以及每个SubJob的执行结果描述
        :type execute_message: str
        """
        
        

        self._job_id = None
        self._job_type = None
        self._job_status = None
        self._entities = None
        self._begin_time = None
        self._end_time = None
        self._expected_end_time = None
        self._execute_code = None
        self._execute_message = None
        self.discriminator = None

        if job_id is not None:
            self.job_id = job_id
        if job_type is not None:
            self.job_type = job_type
        if job_status is not None:
            self.job_status = job_status
        if entities is not None:
            self.entities = entities
        if begin_time is not None:
            self.begin_time = begin_time
        if end_time is not None:
            self.end_time = end_time
        if expected_end_time is not None:
            self.expected_end_time = expected_end_time
        if execute_code is not None:
            self.execute_code = execute_code
        if execute_message is not None:
            self.execute_message = execute_message

    @property
    def job_id(self):
        """Gets the job_id of this SubJobInfo.

        子job标识

        :return: The job_id of this SubJobInfo.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this SubJobInfo.

        子job标识

        :param job_id: The job_id of this SubJobInfo.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def job_type(self):
        """Gets the job_type of this SubJobInfo.

        任务类型，固定值2：子Job

        :return: The job_type of this SubJobInfo.
        :rtype: int
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        """Sets the job_type of this SubJobInfo.

        任务类型，固定值2：子Job

        :param job_type: The job_type of this SubJobInfo.
        :type job_type: int
        """
        self._job_type = job_type

    @property
    def job_status(self):
        """Gets the job_status of this SubJobInfo.

        job状态 - 0：失败。 - 1：成功。 - 2：处理中。 - 3：正在初始化。

        :return: The job_status of this SubJobInfo.
        :rtype: int
        """
        return self._job_status

    @job_status.setter
    def job_status(self, job_status):
        """Sets the job_status of this SubJobInfo.

        job状态 - 0：失败。 - 1：成功。 - 2：处理中。 - 3：正在初始化。

        :param job_status: The job_status of this SubJobInfo.
        :type job_status: int
        """
        self._job_status = job_status

    @property
    def entities(self):
        """Gets the entities of this SubJobInfo.

        SubJob中处理的云服务/云资源对象。 创建、规格变更等场景是必填；冻结、解冻、删除等场景可空。

        :return: The entities of this SubJobInfo.
        :rtype: list[:class:`huaweicloudsdkworkspaceapp.v1.JobResourceInfo`]
        """
        return self._entities

    @entities.setter
    def entities(self, entities):
        """Sets the entities of this SubJobInfo.

        SubJob中处理的云服务/云资源对象。 创建、规格变更等场景是必填；冻结、解冻、删除等场景可空。

        :param entities: The entities of this SubJobInfo.
        :type entities: list[:class:`huaweicloudsdkworkspaceapp.v1.JobResourceInfo`]
        """
        self._entities = entities

    @property
    def begin_time(self):
        """Gets the begin_time of this SubJobInfo.

        任务开始时间

        :return: The begin_time of this SubJobInfo.
        :rtype: datetime
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        """Sets the begin_time of this SubJobInfo.

        任务开始时间

        :param begin_time: The begin_time of this SubJobInfo.
        :type begin_time: datetime
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        """Gets the end_time of this SubJobInfo.

        任务结束时间

        :return: The end_time of this SubJobInfo.
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this SubJobInfo.

        任务结束时间

        :param end_time: The end_time of this SubJobInfo.
        :type end_time: datetime
        """
        self._end_time = end_time

    @property
    def expected_end_time(self):
        """Gets the expected_end_time of this SubJobInfo.

        云服务预估的Job处理结束时间，只针对job有效，针对子job无效。

        :return: The expected_end_time of this SubJobInfo.
        :rtype: datetime
        """
        return self._expected_end_time

    @expected_end_time.setter
    def expected_end_time(self, expected_end_time):
        """Sets the expected_end_time of this SubJobInfo.

        云服务预估的Job处理结束时间，只针对job有效，针对子job无效。

        :param expected_end_time: The expected_end_time of this SubJobInfo.
        :type expected_end_time: datetime
        """
        self._expected_end_time = expected_end_time

    @property
    def execute_code(self):
        """Gets the execute_code of this SubJobInfo.

        Job执行结果码

        :return: The execute_code of this SubJobInfo.
        :rtype: str
        """
        return self._execute_code

    @execute_code.setter
    def execute_code(self, execute_code):
        """Sets the execute_code of this SubJobInfo.

        Job执行结果码

        :param execute_code: The execute_code of this SubJobInfo.
        :type execute_code: str
        """
        self._execute_code = execute_code

    @property
    def execute_message(self):
        """Gets the execute_message of this SubJobInfo.

        Job执行结果描述，以及每个SubJob的执行结果描述

        :return: The execute_message of this SubJobInfo.
        :rtype: str
        """
        return self._execute_message

    @execute_message.setter
    def execute_message(self, execute_message):
        """Sets the execute_message of this SubJobInfo.

        Job执行结果描述，以及每个SubJob的执行结果描述

        :param execute_message: The execute_message of this SubJobInfo.
        :type execute_message: str
        """
        self._execute_message = execute_message

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
        if not isinstance(other, SubJobInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
