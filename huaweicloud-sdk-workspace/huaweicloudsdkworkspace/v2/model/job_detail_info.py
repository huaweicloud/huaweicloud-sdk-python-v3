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
        'message': 'str',
        'job_id': 'str',
        'desktop_name': 'str',
        'ip_address': 'str',
        'mac_address': 'str'
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
        'message': 'message',
        'job_id': 'job_id',
        'desktop_name': 'desktop_name',
        'ip_address': 'ip_address',
        'mac_address': 'mac_address'
    }

    def __init__(self, id=None, job_type=None, entities=None, begin_time=None, end_time=None, status=None, error_code=None, fail_reason=None, message=None, job_id=None, desktop_name=None, ip_address=None, mac_address=None):
        """JobDetailInfo

        The model defined in huaweicloud sdk

        :param id: 任务id。
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
        :param message: 任务失败原因信息。
        :type message: str
        :param job_id: 任务ID。
        :type job_id: str
        :param desktop_name: 桌面名称。
        :type desktop_name: str
        :param ip_address: ip地址。
        :type ip_address: str
        :param mac_address: mac地址。
        :type mac_address: str
        """
        
        

        self._id = None
        self._job_type = None
        self._entities = None
        self._begin_time = None
        self._end_time = None
        self._status = None
        self._error_code = None
        self._fail_reason = None
        self._message = None
        self._job_id = None
        self._desktop_name = None
        self._ip_address = None
        self._mac_address = None
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
        if message is not None:
            self.message = message
        if job_id is not None:
            self.job_id = job_id
        if desktop_name is not None:
            self.desktop_name = desktop_name
        if ip_address is not None:
            self.ip_address = ip_address
        if mac_address is not None:
            self.mac_address = mac_address

    @property
    def id(self):
        """Gets the id of this JobDetailInfo.

        任务id。

        :return: The id of this JobDetailInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this JobDetailInfo.

        任务id。

        :param id: The id of this JobDetailInfo.
        :type id: str
        """
        self._id = id

    @property
    def job_type(self):
        """Gets the job_type of this JobDetailInfo.

        任务类型。

        :return: The job_type of this JobDetailInfo.
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        """Sets the job_type of this JobDetailInfo.

        任务类型。

        :param job_type: The job_type of this JobDetailInfo.
        :type job_type: str
        """
        self._job_type = job_type

    @property
    def entities(self):
        """Gets the entities of this JobDetailInfo.

        :return: The entities of this JobDetailInfo.
        :rtype: :class:`huaweicloudsdkworkspace.v2.JobEntities`
        """
        return self._entities

    @entities.setter
    def entities(self, entities):
        """Sets the entities of this JobDetailInfo.

        :param entities: The entities of this JobDetailInfo.
        :type entities: :class:`huaweicloudsdkworkspace.v2.JobEntities`
        """
        self._entities = entities

    @property
    def begin_time(self):
        """Gets the begin_time of this JobDetailInfo.

        任务创建时间。

        :return: The begin_time of this JobDetailInfo.
        :rtype: str
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        """Sets the begin_time of this JobDetailInfo.

        任务创建时间。

        :param begin_time: The begin_time of this JobDetailInfo.
        :type begin_time: str
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        """Gets the end_time of this JobDetailInfo.

        任务结束时间。

        :return: The end_time of this JobDetailInfo.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this JobDetailInfo.

        任务结束时间。

        :param end_time: The end_time of this JobDetailInfo.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def status(self):
        """Gets the status of this JobDetailInfo.

        任务状态。

        :return: The status of this JobDetailInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this JobDetailInfo.

        任务状态。

        :param status: The status of this JobDetailInfo.
        :type status: str
        """
        self._status = status

    @property
    def error_code(self):
        """Gets the error_code of this JobDetailInfo.

        任务执行失败时的错误码。

        :return: The error_code of this JobDetailInfo.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this JobDetailInfo.

        任务执行失败时的错误码。

        :param error_code: The error_code of this JobDetailInfo.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def fail_reason(self):
        """Gets the fail_reason of this JobDetailInfo.

        任务失败原因。

        :return: The fail_reason of this JobDetailInfo.
        :rtype: str
        """
        return self._fail_reason

    @fail_reason.setter
    def fail_reason(self, fail_reason):
        """Sets the fail_reason of this JobDetailInfo.

        任务失败原因。

        :param fail_reason: The fail_reason of this JobDetailInfo.
        :type fail_reason: str
        """
        self._fail_reason = fail_reason

    @property
    def message(self):
        """Gets the message of this JobDetailInfo.

        任务失败原因信息。

        :return: The message of this JobDetailInfo.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this JobDetailInfo.

        任务失败原因信息。

        :param message: The message of this JobDetailInfo.
        :type message: str
        """
        self._message = message

    @property
    def job_id(self):
        """Gets the job_id of this JobDetailInfo.

        任务ID。

        :return: The job_id of this JobDetailInfo.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this JobDetailInfo.

        任务ID。

        :param job_id: The job_id of this JobDetailInfo.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def desktop_name(self):
        """Gets the desktop_name of this JobDetailInfo.

        桌面名称。

        :return: The desktop_name of this JobDetailInfo.
        :rtype: str
        """
        return self._desktop_name

    @desktop_name.setter
    def desktop_name(self, desktop_name):
        """Sets the desktop_name of this JobDetailInfo.

        桌面名称。

        :param desktop_name: The desktop_name of this JobDetailInfo.
        :type desktop_name: str
        """
        self._desktop_name = desktop_name

    @property
    def ip_address(self):
        """Gets the ip_address of this JobDetailInfo.

        ip地址。

        :return: The ip_address of this JobDetailInfo.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """Sets the ip_address of this JobDetailInfo.

        ip地址。

        :param ip_address: The ip_address of this JobDetailInfo.
        :type ip_address: str
        """
        self._ip_address = ip_address

    @property
    def mac_address(self):
        """Gets the mac_address of this JobDetailInfo.

        mac地址。

        :return: The mac_address of this JobDetailInfo.
        :rtype: str
        """
        return self._mac_address

    @mac_address.setter
    def mac_address(self, mac_address):
        """Sets the mac_address of this JobDetailInfo.

        mac地址。

        :param mac_address: The mac_address of this JobDetailInfo.
        :type mac_address: str
        """
        self._mac_address = mac_address

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
