# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateStreamingJobResponse(SdkResponse):

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
        'job_state': 'str',
        'status': 'str',
        'check_info': 'dict(str, object)'
    }

    attribute_map = {
        'job_id': 'job_id',
        'job_state': 'job_state',
        'status': 'status',
        'check_info': 'check_info'
    }

    def __init__(self, job_id=None, job_state=None, status=None, check_info=None):
        """UpdateStreamingJobResponse

        The model defined in huaweicloud sdk

        :param job_id: 作业ID
        :type job_id: str
        :param job_state: 作业状态
        :type job_state: str
        :param status: 操作结果
        :type status: str
        :param check_info: 作业错误详情
        :type check_info: dict(str, object)
        """
        
        super(UpdateStreamingJobResponse, self).__init__()

        self._job_id = None
        self._job_state = None
        self._status = None
        self._check_info = None
        self.discriminator = None

        if job_id is not None:
            self.job_id = job_id
        if job_state is not None:
            self.job_state = job_state
        if status is not None:
            self.status = status
        if check_info is not None:
            self.check_info = check_info

    @property
    def job_id(self):
        """Gets the job_id of this UpdateStreamingJobResponse.

        作业ID

        :return: The job_id of this UpdateStreamingJobResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this UpdateStreamingJobResponse.

        作业ID

        :param job_id: The job_id of this UpdateStreamingJobResponse.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def job_state(self):
        """Gets the job_state of this UpdateStreamingJobResponse.

        作业状态

        :return: The job_state of this UpdateStreamingJobResponse.
        :rtype: str
        """
        return self._job_state

    @job_state.setter
    def job_state(self, job_state):
        """Sets the job_state of this UpdateStreamingJobResponse.

        作业状态

        :param job_state: The job_state of this UpdateStreamingJobResponse.
        :type job_state: str
        """
        self._job_state = job_state

    @property
    def status(self):
        """Gets the status of this UpdateStreamingJobResponse.

        操作结果

        :return: The status of this UpdateStreamingJobResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this UpdateStreamingJobResponse.

        操作结果

        :param status: The status of this UpdateStreamingJobResponse.
        :type status: str
        """
        self._status = status

    @property
    def check_info(self):
        """Gets the check_info of this UpdateStreamingJobResponse.

        作业错误详情

        :return: The check_info of this UpdateStreamingJobResponse.
        :rtype: dict(str, object)
        """
        return self._check_info

    @check_info.setter
    def check_info(self, check_info):
        """Sets the check_info of this UpdateStreamingJobResponse.

        作业错误详情

        :param check_info: The check_info of this UpdateStreamingJobResponse.
        :type check_info: dict(str, object)
        """
        self._check_info = check_info

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
        if not isinstance(other, UpdateStreamingJobResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
