# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RunCreateVideoModerationJobResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'request_id': 'str',
        'job_id': 'str'
    }

    attribute_map = {
        'request_id': 'request_id',
        'job_id': 'job_id'
    }

    def __init__(self, request_id=None, job_id=None):
        """RunCreateVideoModerationJobResponse

        The model defined in huaweicloud sdk

        :param request_id: 本次请求的唯⼀标识，⽤于问题排查，建议保存。
        :type request_id: str
        :param job_id: 作业唯一标识。
        :type job_id: str
        """
        
        super(RunCreateVideoModerationJobResponse, self).__init__()

        self._request_id = None
        self._job_id = None
        self.discriminator = None

        if request_id is not None:
            self.request_id = request_id
        if job_id is not None:
            self.job_id = job_id

    @property
    def request_id(self):
        """Gets the request_id of this RunCreateVideoModerationJobResponse.

        本次请求的唯⼀标识，⽤于问题排查，建议保存。

        :return: The request_id of this RunCreateVideoModerationJobResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this RunCreateVideoModerationJobResponse.

        本次请求的唯⼀标识，⽤于问题排查，建议保存。

        :param request_id: The request_id of this RunCreateVideoModerationJobResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def job_id(self):
        """Gets the job_id of this RunCreateVideoModerationJobResponse.

        作业唯一标识。

        :return: The job_id of this RunCreateVideoModerationJobResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this RunCreateVideoModerationJobResponse.

        作业唯一标识。

        :param job_id: The job_id of this RunCreateVideoModerationJobResponse.
        :type job_id: str
        """
        self._job_id = job_id

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
        if not isinstance(other, RunCreateVideoModerationJobResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
