# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowJobInfoResponse(SdkResponse):

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
        'job_type': 'str',
        'status': 'str',
        'begin_time': 'str',
        'end_time': 'str',
        'fail_reason': 'str'
    }

    attribute_map = {
        'job_id': 'job_id',
        'job_type': 'job_type',
        'status': 'status',
        'begin_time': 'begin_time',
        'end_time': 'end_time',
        'fail_reason': 'fail_reason'
    }

    def __init__(self, job_id=None, job_type=None, status=None, begin_time=None, end_time=None, fail_reason=None):
        """ShowJobInfoResponse

        The model defined in huaweicloud sdk

        :param job_id: Job任务ID
        :type job_id: str
        :param job_type: Job类型，取值范围：   masterStandbySwapJob：主备倒换任务   modifyClientIpTransJob：修改源ip透传 
        :type job_type: str
        :param status: Job状态
        :type status: str
        :param begin_time: Job开始时间戳，单位为ms，格式为:1684191545379
        :type begin_time: str
        :param end_time: Job开始时间戳，单位为ms，格式为:1684191548248
        :type end_time: str
        :param fail_reason: 失败原因
        :type fail_reason: str
        """
        
        super(ShowJobInfoResponse, self).__init__()

        self._job_id = None
        self._job_type = None
        self._status = None
        self._begin_time = None
        self._end_time = None
        self._fail_reason = None
        self.discriminator = None

        if job_id is not None:
            self.job_id = job_id
        if job_type is not None:
            self.job_type = job_type
        if status is not None:
            self.status = status
        if begin_time is not None:
            self.begin_time = begin_time
        if end_time is not None:
            self.end_time = end_time
        if fail_reason is not None:
            self.fail_reason = fail_reason

    @property
    def job_id(self):
        """Gets the job_id of this ShowJobInfoResponse.

        Job任务ID

        :return: The job_id of this ShowJobInfoResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this ShowJobInfoResponse.

        Job任务ID

        :param job_id: The job_id of this ShowJobInfoResponse.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def job_type(self):
        """Gets the job_type of this ShowJobInfoResponse.

        Job类型，取值范围：   masterStandbySwapJob：主备倒换任务   modifyClientIpTransJob：修改源ip透传 

        :return: The job_type of this ShowJobInfoResponse.
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        """Sets the job_type of this ShowJobInfoResponse.

        Job类型，取值范围：   masterStandbySwapJob：主备倒换任务   modifyClientIpTransJob：修改源ip透传 

        :param job_type: The job_type of this ShowJobInfoResponse.
        :type job_type: str
        """
        self._job_type = job_type

    @property
    def status(self):
        """Gets the status of this ShowJobInfoResponse.

        Job状态

        :return: The status of this ShowJobInfoResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShowJobInfoResponse.

        Job状态

        :param status: The status of this ShowJobInfoResponse.
        :type status: str
        """
        self._status = status

    @property
    def begin_time(self):
        """Gets the begin_time of this ShowJobInfoResponse.

        Job开始时间戳，单位为ms，格式为:1684191545379

        :return: The begin_time of this ShowJobInfoResponse.
        :rtype: str
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        """Sets the begin_time of this ShowJobInfoResponse.

        Job开始时间戳，单位为ms，格式为:1684191545379

        :param begin_time: The begin_time of this ShowJobInfoResponse.
        :type begin_time: str
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        """Gets the end_time of this ShowJobInfoResponse.

        Job开始时间戳，单位为ms，格式为:1684191548248

        :return: The end_time of this ShowJobInfoResponse.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ShowJobInfoResponse.

        Job开始时间戳，单位为ms，格式为:1684191548248

        :param end_time: The end_time of this ShowJobInfoResponse.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def fail_reason(self):
        """Gets the fail_reason of this ShowJobInfoResponse.

        失败原因

        :return: The fail_reason of this ShowJobInfoResponse.
        :rtype: str
        """
        return self._fail_reason

    @fail_reason.setter
    def fail_reason(self, fail_reason):
        """Sets the fail_reason of this ShowJobInfoResponse.

        失败原因

        :param fail_reason: The fail_reason of this ShowJobInfoResponse.
        :type fail_reason: str
        """
        self._fail_reason = fail_reason

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
        if not isinstance(other, ShowJobInfoResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
