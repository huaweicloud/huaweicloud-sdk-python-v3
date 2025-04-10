# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class JobBean:

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
        'status': 'str',
        'job_type': 'str',
        'server_id': 'str',
        'server_name': 'str',
        'resource_id': 'str',
        'begin_time': 'int',
        'end_time': 'int',
        'charge_mode': 'str',
        'error_code': 'str',
        'fail_reason': 'str',
        'ha_id': 'str',
        'ha_name': 'str'
    }

    attribute_map = {
        'job_id': 'job_id',
        'status': 'status',
        'job_type': 'job_type',
        'server_id': 'server_id',
        'server_name': 'server_name',
        'resource_id': 'resource_id',
        'begin_time': 'begin_time',
        'end_time': 'end_time',
        'charge_mode': 'charge_mode',
        'error_code': 'error_code',
        'fail_reason': 'fail_reason',
        'ha_id': 'ha_id',
        'ha_name': 'ha_name'
    }

    def __init__(self, job_id=None, status=None, job_type=None, server_id=None, server_name=None, resource_id=None, begin_time=None, end_time=None, charge_mode=None, error_code=None, fail_reason=None, ha_id=None, ha_name=None):
        r"""JobBean

        The model defined in huaweicloud sdk

        :param job_id: 任务ID。
        :type job_id: str
        :param status: 任务状态 - SUCCESS - RUNNING - FAIL - INIT - READY
        :type status: str
        :param job_type: 类型
        :type job_type: str
        :param server_id: 虚拟机ID
        :type server_id: str
        :param server_name: 虚拟机名称
        :type server_name: str
        :param resource_id: 资源ID
        :type resource_id: str
        :param begin_time: 开始时间
        :type begin_time: int
        :param end_time: 结束时间
        :type end_time: int
        :param charge_mode: 计费模式 - Period:包周期计费 - Demand:按需计费
        :type charge_mode: str
        :param error_code: 错误码
        :type error_code: str
        :param fail_reason: 失败原因
        :type fail_reason: str
        :param ha_id: 防护实例ID,该字段已废弃
        :type ha_id: str
        :param ha_name: 防护实例名称，该字段已废弃
        :type ha_name: str
        """
        
        

        self._job_id = None
        self._status = None
        self._job_type = None
        self._server_id = None
        self._server_name = None
        self._resource_id = None
        self._begin_time = None
        self._end_time = None
        self._charge_mode = None
        self._error_code = None
        self._fail_reason = None
        self._ha_id = None
        self._ha_name = None
        self.discriminator = None

        self.job_id = job_id
        self.status = status
        self.job_type = job_type
        self.server_id = server_id
        self.server_name = server_name
        self.resource_id = resource_id
        self.begin_time = begin_time
        self.end_time = end_time
        self.charge_mode = charge_mode
        if error_code is not None:
            self.error_code = error_code
        if fail_reason is not None:
            self.fail_reason = fail_reason
        if ha_id is not None:
            self.ha_id = ha_id
        if ha_name is not None:
            self.ha_name = ha_name

    @property
    def job_id(self):
        r"""Gets the job_id of this JobBean.

        任务ID。

        :return: The job_id of this JobBean.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this JobBean.

        任务ID。

        :param job_id: The job_id of this JobBean.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def status(self):
        r"""Gets the status of this JobBean.

        任务状态 - SUCCESS - RUNNING - FAIL - INIT - READY

        :return: The status of this JobBean.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this JobBean.

        任务状态 - SUCCESS - RUNNING - FAIL - INIT - READY

        :param status: The status of this JobBean.
        :type status: str
        """
        self._status = status

    @property
    def job_type(self):
        r"""Gets the job_type of this JobBean.

        类型

        :return: The job_type of this JobBean.
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        r"""Sets the job_type of this JobBean.

        类型

        :param job_type: The job_type of this JobBean.
        :type job_type: str
        """
        self._job_type = job_type

    @property
    def server_id(self):
        r"""Gets the server_id of this JobBean.

        虚拟机ID

        :return: The server_id of this JobBean.
        :rtype: str
        """
        return self._server_id

    @server_id.setter
    def server_id(self, server_id):
        r"""Sets the server_id of this JobBean.

        虚拟机ID

        :param server_id: The server_id of this JobBean.
        :type server_id: str
        """
        self._server_id = server_id

    @property
    def server_name(self):
        r"""Gets the server_name of this JobBean.

        虚拟机名称

        :return: The server_name of this JobBean.
        :rtype: str
        """
        return self._server_name

    @server_name.setter
    def server_name(self, server_name):
        r"""Sets the server_name of this JobBean.

        虚拟机名称

        :param server_name: The server_name of this JobBean.
        :type server_name: str
        """
        self._server_name = server_name

    @property
    def resource_id(self):
        r"""Gets the resource_id of this JobBean.

        资源ID

        :return: The resource_id of this JobBean.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this JobBean.

        资源ID

        :param resource_id: The resource_id of this JobBean.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def begin_time(self):
        r"""Gets the begin_time of this JobBean.

        开始时间

        :return: The begin_time of this JobBean.
        :rtype: int
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        r"""Sets the begin_time of this JobBean.

        开始时间

        :param begin_time: The begin_time of this JobBean.
        :type begin_time: int
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        r"""Gets the end_time of this JobBean.

        结束时间

        :return: The end_time of this JobBean.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this JobBean.

        结束时间

        :param end_time: The end_time of this JobBean.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def charge_mode(self):
        r"""Gets the charge_mode of this JobBean.

        计费模式 - Period:包周期计费 - Demand:按需计费

        :return: The charge_mode of this JobBean.
        :rtype: str
        """
        return self._charge_mode

    @charge_mode.setter
    def charge_mode(self, charge_mode):
        r"""Sets the charge_mode of this JobBean.

        计费模式 - Period:包周期计费 - Demand:按需计费

        :param charge_mode: The charge_mode of this JobBean.
        :type charge_mode: str
        """
        self._charge_mode = charge_mode

    @property
    def error_code(self):
        r"""Gets the error_code of this JobBean.

        错误码

        :return: The error_code of this JobBean.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        r"""Sets the error_code of this JobBean.

        错误码

        :param error_code: The error_code of this JobBean.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def fail_reason(self):
        r"""Gets the fail_reason of this JobBean.

        失败原因

        :return: The fail_reason of this JobBean.
        :rtype: str
        """
        return self._fail_reason

    @fail_reason.setter
    def fail_reason(self, fail_reason):
        r"""Sets the fail_reason of this JobBean.

        失败原因

        :param fail_reason: The fail_reason of this JobBean.
        :type fail_reason: str
        """
        self._fail_reason = fail_reason

    @property
    def ha_id(self):
        r"""Gets the ha_id of this JobBean.

        防护实例ID,该字段已废弃

        :return: The ha_id of this JobBean.
        :rtype: str
        """
        return self._ha_id

    @ha_id.setter
    def ha_id(self, ha_id):
        r"""Sets the ha_id of this JobBean.

        防护实例ID,该字段已废弃

        :param ha_id: The ha_id of this JobBean.
        :type ha_id: str
        """
        self._ha_id = ha_id

    @property
    def ha_name(self):
        r"""Gets the ha_name of this JobBean.

        防护实例名称，该字段已废弃

        :return: The ha_name of this JobBean.
        :rtype: str
        """
        return self._ha_name

    @ha_name.setter
    def ha_name(self, ha_name):
        r"""Sets the ha_name of this JobBean.

        防护实例名称，该字段已废弃

        :param ha_name: The ha_name of this JobBean.
        :type ha_name: str
        """
        self._ha_name = ha_name

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
        if not isinstance(other, JobBean):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
