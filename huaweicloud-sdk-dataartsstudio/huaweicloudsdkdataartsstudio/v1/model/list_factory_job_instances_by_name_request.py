# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListFactoryJobInstancesByNameRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'workspace': 'str',
        'limit': 'int',
        'offset': 'int',
        'min_plan_time': 'int',
        'max_plan_time': 'int',
        'status': 'str',
        'job_name': 'str',
        'force_success': 'bool',
        'ignore_success': 'bool',
        'instance_type': 'str'
    }

    attribute_map = {
        'workspace': 'workspace',
        'limit': 'limit',
        'offset': 'offset',
        'min_plan_time': 'min_plan_time',
        'max_plan_time': 'max_plan_time',
        'status': 'status',
        'job_name': 'job_name',
        'force_success': 'force_success',
        'ignore_success': 'ignore_success',
        'instance_type': 'instance_type'
    }

    def __init__(self, workspace=None, limit=None, offset=None, min_plan_time=None, max_plan_time=None, status=None, job_name=None, force_success=None, ignore_success=None, instance_type=None):
        """ListFactoryJobInstancesByNameRequest

        The model defined in huaweicloud sdk

        :param workspace: 工作空间ID
        :type workspace: str
        :param limit: 分页返回结果，指定每页最大记录数。 范围[1,1000] 默认值：10
        :type limit: int
        :param offset: 分页的起始页，默认值为0。取值范围大于等于0。
        :type offset: int
        :param min_plan_time: 返回作业实例开始时间大于min_plain_time的作业实例，单位为毫秒ms，默认设置为查询当天0点，最大可支持查询一个月。
        :type min_plan_time: int
        :param max_plan_time: 返回作业实例开始时间小于max_plain_time的作业实例，单位为毫秒ms，默认设置为当前时间。
        :type max_plan_time: int
        :param status: 实例运行状态: - waiting：等待运行 - running：运行中 - success：运行成功 - fail： 运行失败 - running-exception：运行异常 - pause： 暂停 - manual-stop：取消 - skip-by-depend：跳过 - freeze：冻结 默认查全部
        :type status: str
        :param job_name: 作业名称
        :type job_name: str
        :param force_success: status为success的时候使用，true则筛选出强制成功的作业实例默认值：false
        :type force_success: bool
        :param ignore_success: status为success的时候使用，true则筛选出忽略失败的作业实例默认值：false
        :type ignore_success: bool
        :param instance_type: 作业调度方式: -0:正常调度 -2:手工调度 -5:补数据 -6:子作业调度 -7:单次调度
        :type instance_type: str
        """
        
        

        self._workspace = None
        self._limit = None
        self._offset = None
        self._min_plan_time = None
        self._max_plan_time = None
        self._status = None
        self._job_name = None
        self._force_success = None
        self._ignore_success = None
        self._instance_type = None
        self.discriminator = None

        if workspace is not None:
            self.workspace = workspace
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if min_plan_time is not None:
            self.min_plan_time = min_plan_time
        if max_plan_time is not None:
            self.max_plan_time = max_plan_time
        if status is not None:
            self.status = status
        self.job_name = job_name
        if force_success is not None:
            self.force_success = force_success
        if ignore_success is not None:
            self.ignore_success = ignore_success
        if instance_type is not None:
            self.instance_type = instance_type

    @property
    def workspace(self):
        """Gets the workspace of this ListFactoryJobInstancesByNameRequest.

        工作空间ID

        :return: The workspace of this ListFactoryJobInstancesByNameRequest.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        """Sets the workspace of this ListFactoryJobInstancesByNameRequest.

        工作空间ID

        :param workspace: The workspace of this ListFactoryJobInstancesByNameRequest.
        :type workspace: str
        """
        self._workspace = workspace

    @property
    def limit(self):
        """Gets the limit of this ListFactoryJobInstancesByNameRequest.

        分页返回结果，指定每页最大记录数。 范围[1,1000] 默认值：10

        :return: The limit of this ListFactoryJobInstancesByNameRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListFactoryJobInstancesByNameRequest.

        分页返回结果，指定每页最大记录数。 范围[1,1000] 默认值：10

        :param limit: The limit of this ListFactoryJobInstancesByNameRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListFactoryJobInstancesByNameRequest.

        分页的起始页，默认值为0。取值范围大于等于0。

        :return: The offset of this ListFactoryJobInstancesByNameRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListFactoryJobInstancesByNameRequest.

        分页的起始页，默认值为0。取值范围大于等于0。

        :param offset: The offset of this ListFactoryJobInstancesByNameRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def min_plan_time(self):
        """Gets the min_plan_time of this ListFactoryJobInstancesByNameRequest.

        返回作业实例开始时间大于min_plain_time的作业实例，单位为毫秒ms，默认设置为查询当天0点，最大可支持查询一个月。

        :return: The min_plan_time of this ListFactoryJobInstancesByNameRequest.
        :rtype: int
        """
        return self._min_plan_time

    @min_plan_time.setter
    def min_plan_time(self, min_plan_time):
        """Sets the min_plan_time of this ListFactoryJobInstancesByNameRequest.

        返回作业实例开始时间大于min_plain_time的作业实例，单位为毫秒ms，默认设置为查询当天0点，最大可支持查询一个月。

        :param min_plan_time: The min_plan_time of this ListFactoryJobInstancesByNameRequest.
        :type min_plan_time: int
        """
        self._min_plan_time = min_plan_time

    @property
    def max_plan_time(self):
        """Gets the max_plan_time of this ListFactoryJobInstancesByNameRequest.

        返回作业实例开始时间小于max_plain_time的作业实例，单位为毫秒ms，默认设置为当前时间。

        :return: The max_plan_time of this ListFactoryJobInstancesByNameRequest.
        :rtype: int
        """
        return self._max_plan_time

    @max_plan_time.setter
    def max_plan_time(self, max_plan_time):
        """Sets the max_plan_time of this ListFactoryJobInstancesByNameRequest.

        返回作业实例开始时间小于max_plain_time的作业实例，单位为毫秒ms，默认设置为当前时间。

        :param max_plan_time: The max_plan_time of this ListFactoryJobInstancesByNameRequest.
        :type max_plan_time: int
        """
        self._max_plan_time = max_plan_time

    @property
    def status(self):
        """Gets the status of this ListFactoryJobInstancesByNameRequest.

        实例运行状态: - waiting：等待运行 - running：运行中 - success：运行成功 - fail： 运行失败 - running-exception：运行异常 - pause： 暂停 - manual-stop：取消 - skip-by-depend：跳过 - freeze：冻结 默认查全部

        :return: The status of this ListFactoryJobInstancesByNameRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListFactoryJobInstancesByNameRequest.

        实例运行状态: - waiting：等待运行 - running：运行中 - success：运行成功 - fail： 运行失败 - running-exception：运行异常 - pause： 暂停 - manual-stop：取消 - skip-by-depend：跳过 - freeze：冻结 默认查全部

        :param status: The status of this ListFactoryJobInstancesByNameRequest.
        :type status: str
        """
        self._status = status

    @property
    def job_name(self):
        """Gets the job_name of this ListFactoryJobInstancesByNameRequest.

        作业名称

        :return: The job_name of this ListFactoryJobInstancesByNameRequest.
        :rtype: str
        """
        return self._job_name

    @job_name.setter
    def job_name(self, job_name):
        """Sets the job_name of this ListFactoryJobInstancesByNameRequest.

        作业名称

        :param job_name: The job_name of this ListFactoryJobInstancesByNameRequest.
        :type job_name: str
        """
        self._job_name = job_name

    @property
    def force_success(self):
        """Gets the force_success of this ListFactoryJobInstancesByNameRequest.

        status为success的时候使用，true则筛选出强制成功的作业实例默认值：false

        :return: The force_success of this ListFactoryJobInstancesByNameRequest.
        :rtype: bool
        """
        return self._force_success

    @force_success.setter
    def force_success(self, force_success):
        """Sets the force_success of this ListFactoryJobInstancesByNameRequest.

        status为success的时候使用，true则筛选出强制成功的作业实例默认值：false

        :param force_success: The force_success of this ListFactoryJobInstancesByNameRequest.
        :type force_success: bool
        """
        self._force_success = force_success

    @property
    def ignore_success(self):
        """Gets the ignore_success of this ListFactoryJobInstancesByNameRequest.

        status为success的时候使用，true则筛选出忽略失败的作业实例默认值：false

        :return: The ignore_success of this ListFactoryJobInstancesByNameRequest.
        :rtype: bool
        """
        return self._ignore_success

    @ignore_success.setter
    def ignore_success(self, ignore_success):
        """Sets the ignore_success of this ListFactoryJobInstancesByNameRequest.

        status为success的时候使用，true则筛选出忽略失败的作业实例默认值：false

        :param ignore_success: The ignore_success of this ListFactoryJobInstancesByNameRequest.
        :type ignore_success: bool
        """
        self._ignore_success = ignore_success

    @property
    def instance_type(self):
        """Gets the instance_type of this ListFactoryJobInstancesByNameRequest.

        作业调度方式: -0:正常调度 -2:手工调度 -5:补数据 -6:子作业调度 -7:单次调度

        :return: The instance_type of this ListFactoryJobInstancesByNameRequest.
        :rtype: str
        """
        return self._instance_type

    @instance_type.setter
    def instance_type(self, instance_type):
        """Sets the instance_type of this ListFactoryJobInstancesByNameRequest.

        作业调度方式: -0:正常调度 -2:手工调度 -5:补数据 -6:子作业调度 -7:单次调度

        :param instance_type: The instance_type of this ListFactoryJobInstancesByNameRequest.
        :type instance_type: str
        """
        self._instance_type = instance_type

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
        if not isinstance(other, ListFactoryJobInstancesByNameRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
