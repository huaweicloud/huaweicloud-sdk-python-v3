# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowResourcesJobDetailResponse(SdkResponse):

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
        'begin_time': 'str',
        'end_time': 'str',
        'status': 'str',
        'error_code': 'str',
        'fail_reason': 'str',
        'entities': 'SubJobsInfo'
    }

    attribute_map = {
        'job_id': 'job_id',
        'job_type': 'job_type',
        'begin_time': 'begin_time',
        'end_time': 'end_time',
        'status': 'status',
        'error_code': 'error_code',
        'fail_reason': 'fail_reason',
        'entities': 'entities'
    }

    def __init__(self, job_id=None, job_type=None, begin_time=None, end_time=None, status=None, error_code=None, fail_reason=None, entities=None):
        """ShowResourcesJobDetailResponse

        The model defined in huaweicloud sdk

        :param job_id: job id
        :type job_id: str
        :param job_type: job类型
        :type job_type: str
        :param begin_time: 创建时间
        :type begin_time: str
        :param end_time: 创建完成时间
        :type end_time: str
        :param status: job状态
        :type status: str
        :param error_code: 错误码
        :type error_code: str
        :param fail_reason: 错误信息
        :type fail_reason: str
        :param entities: 
        :type entities: :class:`huaweicloudsdkeip.v2.SubJobsInfo`
        """
        
        super(ShowResourcesJobDetailResponse, self).__init__()

        self._job_id = None
        self._job_type = None
        self._begin_time = None
        self._end_time = None
        self._status = None
        self._error_code = None
        self._fail_reason = None
        self._entities = None
        self.discriminator = None

        if job_id is not None:
            self.job_id = job_id
        if job_type is not None:
            self.job_type = job_type
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
        if entities is not None:
            self.entities = entities

    @property
    def job_id(self):
        """Gets the job_id of this ShowResourcesJobDetailResponse.

        job id

        :return: The job_id of this ShowResourcesJobDetailResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this ShowResourcesJobDetailResponse.

        job id

        :param job_id: The job_id of this ShowResourcesJobDetailResponse.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def job_type(self):
        """Gets the job_type of this ShowResourcesJobDetailResponse.

        job类型

        :return: The job_type of this ShowResourcesJobDetailResponse.
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        """Sets the job_type of this ShowResourcesJobDetailResponse.

        job类型

        :param job_type: The job_type of this ShowResourcesJobDetailResponse.
        :type job_type: str
        """
        self._job_type = job_type

    @property
    def begin_time(self):
        """Gets the begin_time of this ShowResourcesJobDetailResponse.

        创建时间

        :return: The begin_time of this ShowResourcesJobDetailResponse.
        :rtype: str
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        """Sets the begin_time of this ShowResourcesJobDetailResponse.

        创建时间

        :param begin_time: The begin_time of this ShowResourcesJobDetailResponse.
        :type begin_time: str
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        """Gets the end_time of this ShowResourcesJobDetailResponse.

        创建完成时间

        :return: The end_time of this ShowResourcesJobDetailResponse.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ShowResourcesJobDetailResponse.

        创建完成时间

        :param end_time: The end_time of this ShowResourcesJobDetailResponse.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def status(self):
        """Gets the status of this ShowResourcesJobDetailResponse.

        job状态

        :return: The status of this ShowResourcesJobDetailResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShowResourcesJobDetailResponse.

        job状态

        :param status: The status of this ShowResourcesJobDetailResponse.
        :type status: str
        """
        self._status = status

    @property
    def error_code(self):
        """Gets the error_code of this ShowResourcesJobDetailResponse.

        错误码

        :return: The error_code of this ShowResourcesJobDetailResponse.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this ShowResourcesJobDetailResponse.

        错误码

        :param error_code: The error_code of this ShowResourcesJobDetailResponse.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def fail_reason(self):
        """Gets the fail_reason of this ShowResourcesJobDetailResponse.

        错误信息

        :return: The fail_reason of this ShowResourcesJobDetailResponse.
        :rtype: str
        """
        return self._fail_reason

    @fail_reason.setter
    def fail_reason(self, fail_reason):
        """Sets the fail_reason of this ShowResourcesJobDetailResponse.

        错误信息

        :param fail_reason: The fail_reason of this ShowResourcesJobDetailResponse.
        :type fail_reason: str
        """
        self._fail_reason = fail_reason

    @property
    def entities(self):
        """Gets the entities of this ShowResourcesJobDetailResponse.

        :return: The entities of this ShowResourcesJobDetailResponse.
        :rtype: :class:`huaweicloudsdkeip.v2.SubJobsInfo`
        """
        return self._entities

    @entities.setter
    def entities(self, entities):
        """Sets the entities of this ShowResourcesJobDetailResponse.

        :param entities: The entities of this ShowResourcesJobDetailResponse.
        :type entities: :class:`huaweicloudsdkeip.v2.SubJobsInfo`
        """
        self._entities = entities

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
        if not isinstance(other, ShowResourcesJobDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
