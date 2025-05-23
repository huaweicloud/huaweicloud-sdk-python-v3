# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SupplementDataResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'end_date': 'int',
        'job_list': 'list[str]',
        'name': 'str',
        'parallel': 'int',
        'start_date': 'int',
        'status': 'str',
        'submitted_date': 'int',
        'supplement_data_instance_time': 'SupplementDataRespSupplementDataInstanceTime',
        'supplement_data_run_time': 'SupplementDataRespSupplementDataRunTime',
        'type': 'int',
        'user_name': 'str'
    }

    attribute_map = {
        'end_date': 'endDate',
        'job_list': 'jobList',
        'name': 'name',
        'parallel': 'parallel',
        'start_date': 'startDate',
        'status': 'status',
        'submitted_date': 'submittedDate',
        'supplement_data_instance_time': 'supplement_data_instance_time',
        'supplement_data_run_time': 'supplement_data_run_time',
        'type': 'type',
        'user_name': 'userName'
    }

    def __init__(self, end_date=None, job_list=None, name=None, parallel=None, start_date=None, status=None, submitted_date=None, supplement_data_instance_time=None, supplement_data_run_time=None, type=None, user_name=None):
        r"""SupplementDataResp

        The model defined in huaweicloud sdk

        :param end_date: 作业的开始日期 13位时间戳
        :type end_date: int
        :param job_list: 补数据作业名称，可能有依赖的作业，故会有多个作业的情况。
        :type job_list: list[str]
        :param name: 补数据名称
        :type name: str
        :param parallel: 并行周期数，取值范围[1,5]
        :type parallel: int
        :param start_date: 作业的结束日期 13位时间戳
        :type start_date: int
        :param status: 实例状态：SUCCESS：成功RUNNING ：运行中CANCLE：取消
        :type status: str
        :param submitted_date: 作业提交时间，13位时间戳
        :type submitted_date: int
        :param supplement_data_instance_time: 
        :type supplement_data_instance_time: :class:`huaweicloudsdkdgc.v1.SupplementDataRespSupplementDataInstanceTime`
        :param supplement_data_run_time: 
        :type supplement_data_run_time: :class:`huaweicloudsdkdgc.v1.SupplementDataRespSupplementDataRunTime`
        :param type: 触发补数据的类型，取值范围[0, 1]。0代表作业监控界面触发的补数据，1代表恢复动作触发的补数据
        :type type: int
        :param user_name: 用户名称
        :type user_name: str
        """
        
        

        self._end_date = None
        self._job_list = None
        self._name = None
        self._parallel = None
        self._start_date = None
        self._status = None
        self._submitted_date = None
        self._supplement_data_instance_time = None
        self._supplement_data_run_time = None
        self._type = None
        self._user_name = None
        self.discriminator = None

        if end_date is not None:
            self.end_date = end_date
        if job_list is not None:
            self.job_list = job_list
        if name is not None:
            self.name = name
        if parallel is not None:
            self.parallel = parallel
        if start_date is not None:
            self.start_date = start_date
        if status is not None:
            self.status = status
        if submitted_date is not None:
            self.submitted_date = submitted_date
        if supplement_data_instance_time is not None:
            self.supplement_data_instance_time = supplement_data_instance_time
        if supplement_data_run_time is not None:
            self.supplement_data_run_time = supplement_data_run_time
        if type is not None:
            self.type = type
        if user_name is not None:
            self.user_name = user_name

    @property
    def end_date(self):
        r"""Gets the end_date of this SupplementDataResp.

        作业的开始日期 13位时间戳

        :return: The end_date of this SupplementDataResp.
        :rtype: int
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        r"""Sets the end_date of this SupplementDataResp.

        作业的开始日期 13位时间戳

        :param end_date: The end_date of this SupplementDataResp.
        :type end_date: int
        """
        self._end_date = end_date

    @property
    def job_list(self):
        r"""Gets the job_list of this SupplementDataResp.

        补数据作业名称，可能有依赖的作业，故会有多个作业的情况。

        :return: The job_list of this SupplementDataResp.
        :rtype: list[str]
        """
        return self._job_list

    @job_list.setter
    def job_list(self, job_list):
        r"""Sets the job_list of this SupplementDataResp.

        补数据作业名称，可能有依赖的作业，故会有多个作业的情况。

        :param job_list: The job_list of this SupplementDataResp.
        :type job_list: list[str]
        """
        self._job_list = job_list

    @property
    def name(self):
        r"""Gets the name of this SupplementDataResp.

        补数据名称

        :return: The name of this SupplementDataResp.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this SupplementDataResp.

        补数据名称

        :param name: The name of this SupplementDataResp.
        :type name: str
        """
        self._name = name

    @property
    def parallel(self):
        r"""Gets the parallel of this SupplementDataResp.

        并行周期数，取值范围[1,5]

        :return: The parallel of this SupplementDataResp.
        :rtype: int
        """
        return self._parallel

    @parallel.setter
    def parallel(self, parallel):
        r"""Sets the parallel of this SupplementDataResp.

        并行周期数，取值范围[1,5]

        :param parallel: The parallel of this SupplementDataResp.
        :type parallel: int
        """
        self._parallel = parallel

    @property
    def start_date(self):
        r"""Gets the start_date of this SupplementDataResp.

        作业的结束日期 13位时间戳

        :return: The start_date of this SupplementDataResp.
        :rtype: int
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        r"""Sets the start_date of this SupplementDataResp.

        作业的结束日期 13位时间戳

        :param start_date: The start_date of this SupplementDataResp.
        :type start_date: int
        """
        self._start_date = start_date

    @property
    def status(self):
        r"""Gets the status of this SupplementDataResp.

        实例状态：SUCCESS：成功RUNNING ：运行中CANCLE：取消

        :return: The status of this SupplementDataResp.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this SupplementDataResp.

        实例状态：SUCCESS：成功RUNNING ：运行中CANCLE：取消

        :param status: The status of this SupplementDataResp.
        :type status: str
        """
        self._status = status

    @property
    def submitted_date(self):
        r"""Gets the submitted_date of this SupplementDataResp.

        作业提交时间，13位时间戳

        :return: The submitted_date of this SupplementDataResp.
        :rtype: int
        """
        return self._submitted_date

    @submitted_date.setter
    def submitted_date(self, submitted_date):
        r"""Sets the submitted_date of this SupplementDataResp.

        作业提交时间，13位时间戳

        :param submitted_date: The submitted_date of this SupplementDataResp.
        :type submitted_date: int
        """
        self._submitted_date = submitted_date

    @property
    def supplement_data_instance_time(self):
        r"""Gets the supplement_data_instance_time of this SupplementDataResp.

        :return: The supplement_data_instance_time of this SupplementDataResp.
        :rtype: :class:`huaweicloudsdkdgc.v1.SupplementDataRespSupplementDataInstanceTime`
        """
        return self._supplement_data_instance_time

    @supplement_data_instance_time.setter
    def supplement_data_instance_time(self, supplement_data_instance_time):
        r"""Sets the supplement_data_instance_time of this SupplementDataResp.

        :param supplement_data_instance_time: The supplement_data_instance_time of this SupplementDataResp.
        :type supplement_data_instance_time: :class:`huaweicloudsdkdgc.v1.SupplementDataRespSupplementDataInstanceTime`
        """
        self._supplement_data_instance_time = supplement_data_instance_time

    @property
    def supplement_data_run_time(self):
        r"""Gets the supplement_data_run_time of this SupplementDataResp.

        :return: The supplement_data_run_time of this SupplementDataResp.
        :rtype: :class:`huaweicloudsdkdgc.v1.SupplementDataRespSupplementDataRunTime`
        """
        return self._supplement_data_run_time

    @supplement_data_run_time.setter
    def supplement_data_run_time(self, supplement_data_run_time):
        r"""Sets the supplement_data_run_time of this SupplementDataResp.

        :param supplement_data_run_time: The supplement_data_run_time of this SupplementDataResp.
        :type supplement_data_run_time: :class:`huaweicloudsdkdgc.v1.SupplementDataRespSupplementDataRunTime`
        """
        self._supplement_data_run_time = supplement_data_run_time

    @property
    def type(self):
        r"""Gets the type of this SupplementDataResp.

        触发补数据的类型，取值范围[0, 1]。0代表作业监控界面触发的补数据，1代表恢复动作触发的补数据

        :return: The type of this SupplementDataResp.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this SupplementDataResp.

        触发补数据的类型，取值范围[0, 1]。0代表作业监控界面触发的补数据，1代表恢复动作触发的补数据

        :param type: The type of this SupplementDataResp.
        :type type: int
        """
        self._type = type

    @property
    def user_name(self):
        r"""Gets the user_name of this SupplementDataResp.

        用户名称

        :return: The user_name of this SupplementDataResp.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this SupplementDataResp.

        用户名称

        :param user_name: The user_name of this SupplementDataResp.
        :type user_name: str
        """
        self._user_name = user_name

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
        if not isinstance(other, SupplementDataResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
