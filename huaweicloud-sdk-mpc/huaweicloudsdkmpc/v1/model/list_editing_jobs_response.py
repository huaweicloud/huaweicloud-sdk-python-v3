# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListEditingJobsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'job_array': 'list[QueryEditingJob]',
        'x_request_id': 'str'
    }

    attribute_map = {
        'job_array': 'job_array',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, job_array=None, x_request_id=None):
        """ListEditingJobsResponse

        The model defined in huaweicloud sdk

        :param job_array: 任务列表
        :type job_array: list[:class:`huaweicloudsdkmpc.v1.QueryEditingJob`]
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(ListEditingJobsResponse, self).__init__()

        self._job_array = None
        self._x_request_id = None
        self.discriminator = None

        if job_array is not None:
            self.job_array = job_array
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def job_array(self):
        """Gets the job_array of this ListEditingJobsResponse.

        任务列表

        :return: The job_array of this ListEditingJobsResponse.
        :rtype: list[:class:`huaweicloudsdkmpc.v1.QueryEditingJob`]
        """
        return self._job_array

    @job_array.setter
    def job_array(self, job_array):
        """Sets the job_array of this ListEditingJobsResponse.

        任务列表

        :param job_array: The job_array of this ListEditingJobsResponse.
        :type job_array: list[:class:`huaweicloudsdkmpc.v1.QueryEditingJob`]
        """
        self._job_array = job_array

    @property
    def x_request_id(self):
        """Gets the x_request_id of this ListEditingJobsResponse.

        :return: The x_request_id of this ListEditingJobsResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        """Sets the x_request_id of this ListEditingJobsResponse.

        :param x_request_id: The x_request_id of this ListEditingJobsResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

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
        if not isinstance(other, ListEditingJobsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
