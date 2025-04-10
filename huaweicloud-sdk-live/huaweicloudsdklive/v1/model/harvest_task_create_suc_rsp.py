# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HarvestTaskCreateSucRsp:

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
        'domain': 'str',
        'app_name': 'str',
        'id': 'str',
        'start_time': 'int',
        'end_time': 'int',
        'create_time': 'int',
        'event_name': 'str',
        'task_desc': 'str',
        'status': 'str',
        'max_retry_cnt': 'int',
        'package_info': 'VodPackageInfo'
    }

    attribute_map = {
        'job_id': 'job_id',
        'domain': 'domain',
        'app_name': 'app_name',
        'id': 'id',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'create_time': 'create_time',
        'event_name': 'event_name',
        'task_desc': 'task_desc',
        'status': 'status',
        'max_retry_cnt': 'max_retry_cnt',
        'package_info': 'package_info'
    }

    def __init__(self, job_id=None, domain=None, app_name=None, id=None, start_time=None, end_time=None, create_time=None, event_name=None, task_desc=None, status=None, max_retry_cnt=None, package_info=None):
        r"""HarvestTaskCreateSucRsp

        The model defined in huaweicloud sdk

        :param job_id: 任务ID
        :type job_id: str
        :param domain: 频道推流域名
        :type domain: str
        :param app_name: 组名或应用名
        :type app_name: str
        :param id: 频道ID。频道唯一标识，为必填项。
        :type id: str
        :param start_time: 开始时间。Unix时间错，单位为秒
        :type start_time: int
        :param end_time: 结束时间。Unix时间错，单位为秒
        :type end_time: int
        :param create_time: 任务创建时间。Unix时间错，单位为秒
        :type create_time: int
        :param event_name: 事件名称
        :type event_name: str
        :param task_desc: 任务描述
        :type task_desc: str
        :param status: 任务状态，取值为 [ UNSTART、IN_PROGRESS、SUCCEEDED、FAILED ]
        :type status: str
        :param max_retry_cnt: 任务状态为FAILED时，最大允许重试的次数
        :type max_retry_cnt: int
        :param package_info: 
        :type package_info: :class:`huaweicloudsdklive.v1.VodPackageInfo`
        """
        
        

        self._job_id = None
        self._domain = None
        self._app_name = None
        self._id = None
        self._start_time = None
        self._end_time = None
        self._create_time = None
        self._event_name = None
        self._task_desc = None
        self._status = None
        self._max_retry_cnt = None
        self._package_info = None
        self.discriminator = None

        self.job_id = job_id
        self.domain = domain
        self.app_name = app_name
        self.id = id
        self.start_time = start_time
        self.end_time = end_time
        if create_time is not None:
            self.create_time = create_time
        self.event_name = event_name
        self.task_desc = task_desc
        self.status = status
        self.max_retry_cnt = max_retry_cnt
        if package_info is not None:
            self.package_info = package_info

    @property
    def job_id(self):
        r"""Gets the job_id of this HarvestTaskCreateSucRsp.

        任务ID

        :return: The job_id of this HarvestTaskCreateSucRsp.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this HarvestTaskCreateSucRsp.

        任务ID

        :param job_id: The job_id of this HarvestTaskCreateSucRsp.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def domain(self):
        r"""Gets the domain of this HarvestTaskCreateSucRsp.

        频道推流域名

        :return: The domain of this HarvestTaskCreateSucRsp.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        r"""Sets the domain of this HarvestTaskCreateSucRsp.

        频道推流域名

        :param domain: The domain of this HarvestTaskCreateSucRsp.
        :type domain: str
        """
        self._domain = domain

    @property
    def app_name(self):
        r"""Gets the app_name of this HarvestTaskCreateSucRsp.

        组名或应用名

        :return: The app_name of this HarvestTaskCreateSucRsp.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        r"""Sets the app_name of this HarvestTaskCreateSucRsp.

        组名或应用名

        :param app_name: The app_name of this HarvestTaskCreateSucRsp.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def id(self):
        r"""Gets the id of this HarvestTaskCreateSucRsp.

        频道ID。频道唯一标识，为必填项。

        :return: The id of this HarvestTaskCreateSucRsp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this HarvestTaskCreateSucRsp.

        频道ID。频道唯一标识，为必填项。

        :param id: The id of this HarvestTaskCreateSucRsp.
        :type id: str
        """
        self._id = id

    @property
    def start_time(self):
        r"""Gets the start_time of this HarvestTaskCreateSucRsp.

        开始时间。Unix时间错，单位为秒

        :return: The start_time of this HarvestTaskCreateSucRsp.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this HarvestTaskCreateSucRsp.

        开始时间。Unix时间错，单位为秒

        :param start_time: The start_time of this HarvestTaskCreateSucRsp.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this HarvestTaskCreateSucRsp.

        结束时间。Unix时间错，单位为秒

        :return: The end_time of this HarvestTaskCreateSucRsp.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this HarvestTaskCreateSucRsp.

        结束时间。Unix时间错，单位为秒

        :param end_time: The end_time of this HarvestTaskCreateSucRsp.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def create_time(self):
        r"""Gets the create_time of this HarvestTaskCreateSucRsp.

        任务创建时间。Unix时间错，单位为秒

        :return: The create_time of this HarvestTaskCreateSucRsp.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this HarvestTaskCreateSucRsp.

        任务创建时间。Unix时间错，单位为秒

        :param create_time: The create_time of this HarvestTaskCreateSucRsp.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def event_name(self):
        r"""Gets the event_name of this HarvestTaskCreateSucRsp.

        事件名称

        :return: The event_name of this HarvestTaskCreateSucRsp.
        :rtype: str
        """
        return self._event_name

    @event_name.setter
    def event_name(self, event_name):
        r"""Sets the event_name of this HarvestTaskCreateSucRsp.

        事件名称

        :param event_name: The event_name of this HarvestTaskCreateSucRsp.
        :type event_name: str
        """
        self._event_name = event_name

    @property
    def task_desc(self):
        r"""Gets the task_desc of this HarvestTaskCreateSucRsp.

        任务描述

        :return: The task_desc of this HarvestTaskCreateSucRsp.
        :rtype: str
        """
        return self._task_desc

    @task_desc.setter
    def task_desc(self, task_desc):
        r"""Sets the task_desc of this HarvestTaskCreateSucRsp.

        任务描述

        :param task_desc: The task_desc of this HarvestTaskCreateSucRsp.
        :type task_desc: str
        """
        self._task_desc = task_desc

    @property
    def status(self):
        r"""Gets the status of this HarvestTaskCreateSucRsp.

        任务状态，取值为 [ UNSTART、IN_PROGRESS、SUCCEEDED、FAILED ]

        :return: The status of this HarvestTaskCreateSucRsp.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this HarvestTaskCreateSucRsp.

        任务状态，取值为 [ UNSTART、IN_PROGRESS、SUCCEEDED、FAILED ]

        :param status: The status of this HarvestTaskCreateSucRsp.
        :type status: str
        """
        self._status = status

    @property
    def max_retry_cnt(self):
        r"""Gets the max_retry_cnt of this HarvestTaskCreateSucRsp.

        任务状态为FAILED时，最大允许重试的次数

        :return: The max_retry_cnt of this HarvestTaskCreateSucRsp.
        :rtype: int
        """
        return self._max_retry_cnt

    @max_retry_cnt.setter
    def max_retry_cnt(self, max_retry_cnt):
        r"""Sets the max_retry_cnt of this HarvestTaskCreateSucRsp.

        任务状态为FAILED时，最大允许重试的次数

        :param max_retry_cnt: The max_retry_cnt of this HarvestTaskCreateSucRsp.
        :type max_retry_cnt: int
        """
        self._max_retry_cnt = max_retry_cnt

    @property
    def package_info(self):
        r"""Gets the package_info of this HarvestTaskCreateSucRsp.

        :return: The package_info of this HarvestTaskCreateSucRsp.
        :rtype: :class:`huaweicloudsdklive.v1.VodPackageInfo`
        """
        return self._package_info

    @package_info.setter
    def package_info(self, package_info):
        r"""Sets the package_info of this HarvestTaskCreateSucRsp.

        :param package_info: The package_info of this HarvestTaskCreateSucRsp.
        :type package_info: :class:`huaweicloudsdklive.v1.VodPackageInfo`
        """
        self._package_info = package_info

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
        if not isinstance(other, HarvestTaskCreateSucRsp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
