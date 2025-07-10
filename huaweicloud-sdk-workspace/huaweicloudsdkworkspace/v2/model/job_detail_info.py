# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class JobDetailInfo:

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
        'job_type': 'str',
        'entities': 'JobEntities',
        'begin_time': 'str',
        'end_time': 'str',
        'status': 'str',
        'error_code': 'str',
        'fail_reason': 'str',
        'host': 'str',
        'project_id': 'str',
        'job_id': 'str',
        'process': 'int',
        'attach_user': 'str',
        'entity': 'str',
        'ip_address': 'str'
    }

    attribute_map = {
        'id': 'id',
        'job_type': 'job_type',
        'entities': 'entities',
        'begin_time': 'begin_time',
        'end_time': 'end_time',
        'status': 'status',
        'error_code': 'error_code',
        'fail_reason': 'fail_reason',
        'host': 'host',
        'project_id': 'project_id',
        'job_id': 'job_id',
        'process': 'process',
        'attach_user': 'attach_user',
        'entity': 'entity',
        'ip_address': 'ip_address'
    }

    def __init__(self, id=None, job_type=None, entities=None, begin_time=None, end_time=None, status=None, error_code=None, fail_reason=None, host=None, project_id=None, job_id=None, process=None, attach_user=None, entity=None, ip_address=None):
        r"""JobDetailInfo

        The model defined in huaweicloud sdk

        :param id: 子任务ID。
        :type id: str
        :param job_type: 任务类型。
        :type job_type: str
        :param entities: 
        :type entities: :class:`huaweicloudsdkworkspace.v2.JobEntities`
        :param begin_time: 任务创建时间。
        :type begin_time: str
        :param end_time: 任务结束时间。
        :type end_time: str
        :param status: 任务状态。
        :type status: str
        :param error_code: 任务执行失败时的错误码。
        :type error_code: str
        :param fail_reason: 任务失败原因。
        :type fail_reason: str
        :param host: 任务执行的服务器IP。
        :type host: str
        :param project_id: 项目ID。
        :type project_id: str
        :param job_id: 任务ID。
        :type job_id: str
        :param process: 任务进度。
        :type process: int
        :param attach_user: 关联用户。
        :type attach_user: str
        :param entity: 操作对象。
        :type entity: str
        :param ip_address: ip地址。
        :type ip_address: str
        """
        
        

        self._id = None
        self._job_type = None
        self._entities = None
        self._begin_time = None
        self._end_time = None
        self._status = None
        self._error_code = None
        self._fail_reason = None
        self._host = None
        self._project_id = None
        self._job_id = None
        self._process = None
        self._attach_user = None
        self._entity = None
        self._ip_address = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if job_type is not None:
            self.job_type = job_type
        if entities is not None:
            self.entities = entities
        if begin_time is not None:
            self.begin_time = begin_time
        if end_time is not None:
            self.end_time = end_time
        if status is not None:
            self.status = status
        if error_code is not None:
            self.error_code = error_code
        if fail_reason is not None:
            self.fail_reason = fail_reason
        if host is not None:
            self.host = host
        if project_id is not None:
            self.project_id = project_id
        if job_id is not None:
            self.job_id = job_id
        if process is not None:
            self.process = process
        if attach_user is not None:
            self.attach_user = attach_user
        if entity is not None:
            self.entity = entity
        if ip_address is not None:
            self.ip_address = ip_address

    @property
    def id(self):
        r"""Gets the id of this JobDetailInfo.

        子任务ID。

        :return: The id of this JobDetailInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this JobDetailInfo.

        子任务ID。

        :param id: The id of this JobDetailInfo.
        :type id: str
        """
        self._id = id

    @property
    def job_type(self):
        r"""Gets the job_type of this JobDetailInfo.

        任务类型。

        :return: The job_type of this JobDetailInfo.
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        r"""Sets the job_type of this JobDetailInfo.

        任务类型。

        :param job_type: The job_type of this JobDetailInfo.
        :type job_type: str
        """
        self._job_type = job_type

    @property
    def entities(self):
        r"""Gets the entities of this JobDetailInfo.

        :return: The entities of this JobDetailInfo.
        :rtype: :class:`huaweicloudsdkworkspace.v2.JobEntities`
        """
        return self._entities

    @entities.setter
    def entities(self, entities):
        r"""Sets the entities of this JobDetailInfo.

        :param entities: The entities of this JobDetailInfo.
        :type entities: :class:`huaweicloudsdkworkspace.v2.JobEntities`
        """
        self._entities = entities

    @property
    def begin_time(self):
        r"""Gets the begin_time of this JobDetailInfo.

        任务创建时间。

        :return: The begin_time of this JobDetailInfo.
        :rtype: str
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        r"""Sets the begin_time of this JobDetailInfo.

        任务创建时间。

        :param begin_time: The begin_time of this JobDetailInfo.
        :type begin_time: str
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        r"""Gets the end_time of this JobDetailInfo.

        任务结束时间。

        :return: The end_time of this JobDetailInfo.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this JobDetailInfo.

        任务结束时间。

        :param end_time: The end_time of this JobDetailInfo.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def status(self):
        r"""Gets the status of this JobDetailInfo.

        任务状态。

        :return: The status of this JobDetailInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this JobDetailInfo.

        任务状态。

        :param status: The status of this JobDetailInfo.
        :type status: str
        """
        self._status = status

    @property
    def error_code(self):
        r"""Gets the error_code of this JobDetailInfo.

        任务执行失败时的错误码。

        :return: The error_code of this JobDetailInfo.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        r"""Sets the error_code of this JobDetailInfo.

        任务执行失败时的错误码。

        :param error_code: The error_code of this JobDetailInfo.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def fail_reason(self):
        r"""Gets the fail_reason of this JobDetailInfo.

        任务失败原因。

        :return: The fail_reason of this JobDetailInfo.
        :rtype: str
        """
        return self._fail_reason

    @fail_reason.setter
    def fail_reason(self, fail_reason):
        r"""Sets the fail_reason of this JobDetailInfo.

        任务失败原因。

        :param fail_reason: The fail_reason of this JobDetailInfo.
        :type fail_reason: str
        """
        self._fail_reason = fail_reason

    @property
    def host(self):
        r"""Gets the host of this JobDetailInfo.

        任务执行的服务器IP。

        :return: The host of this JobDetailInfo.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        r"""Sets the host of this JobDetailInfo.

        任务执行的服务器IP。

        :param host: The host of this JobDetailInfo.
        :type host: str
        """
        self._host = host

    @property
    def project_id(self):
        r"""Gets the project_id of this JobDetailInfo.

        项目ID。

        :return: The project_id of this JobDetailInfo.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this JobDetailInfo.

        项目ID。

        :param project_id: The project_id of this JobDetailInfo.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def job_id(self):
        r"""Gets the job_id of this JobDetailInfo.

        任务ID。

        :return: The job_id of this JobDetailInfo.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this JobDetailInfo.

        任务ID。

        :param job_id: The job_id of this JobDetailInfo.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def process(self):
        r"""Gets the process of this JobDetailInfo.

        任务进度。

        :return: The process of this JobDetailInfo.
        :rtype: int
        """
        return self._process

    @process.setter
    def process(self, process):
        r"""Sets the process of this JobDetailInfo.

        任务进度。

        :param process: The process of this JobDetailInfo.
        :type process: int
        """
        self._process = process

    @property
    def attach_user(self):
        r"""Gets the attach_user of this JobDetailInfo.

        关联用户。

        :return: The attach_user of this JobDetailInfo.
        :rtype: str
        """
        return self._attach_user

    @attach_user.setter
    def attach_user(self, attach_user):
        r"""Sets the attach_user of this JobDetailInfo.

        关联用户。

        :param attach_user: The attach_user of this JobDetailInfo.
        :type attach_user: str
        """
        self._attach_user = attach_user

    @property
    def entity(self):
        r"""Gets the entity of this JobDetailInfo.

        操作对象。

        :return: The entity of this JobDetailInfo.
        :rtype: str
        """
        return self._entity

    @entity.setter
    def entity(self, entity):
        r"""Sets the entity of this JobDetailInfo.

        操作对象。

        :param entity: The entity of this JobDetailInfo.
        :type entity: str
        """
        self._entity = entity

    @property
    def ip_address(self):
        r"""Gets the ip_address of this JobDetailInfo.

        ip地址。

        :return: The ip_address of this JobDetailInfo.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        r"""Sets the ip_address of this JobDetailInfo.

        ip地址。

        :param ip_address: The ip_address of this JobDetailInfo.
        :type ip_address: str
        """
        self._ip_address = ip_address

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
        if not isinstance(other, JobDetailInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
