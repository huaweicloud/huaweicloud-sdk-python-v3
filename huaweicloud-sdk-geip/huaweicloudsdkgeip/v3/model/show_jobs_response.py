# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowJobsResponse(SdkResponse):

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
        'job': 'ShowJob',
        'x_request_id': 'str'
    }

    attribute_map = {
        'request_id': 'request_id',
        'job': 'job',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, request_id=None, job=None, x_request_id=None):
        r"""ShowJobsResponse

        The model defined in huaweicloud sdk

        :param request_id: 本次请求的编号
        :type request_id: str
        :param job: 
        :type job: :class:`huaweicloudsdkgeip.v3.ShowJob`
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(ShowJobsResponse, self).__init__()

        self._request_id = None
        self._job = None
        self._x_request_id = None
        self.discriminator = None

        if request_id is not None:
            self.request_id = request_id
        if job is not None:
            self.job = job
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def request_id(self):
        r"""Gets the request_id of this ShowJobsResponse.

        本次请求的编号

        :return: The request_id of this ShowJobsResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        r"""Sets the request_id of this ShowJobsResponse.

        本次请求的编号

        :param request_id: The request_id of this ShowJobsResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def job(self):
        r"""Gets the job of this ShowJobsResponse.

        :return: The job of this ShowJobsResponse.
        :rtype: :class:`huaweicloudsdkgeip.v3.ShowJob`
        """
        return self._job

    @job.setter
    def job(self, job):
        r"""Sets the job of this ShowJobsResponse.

        :param job: The job of this ShowJobsResponse.
        :type job: :class:`huaweicloudsdkgeip.v3.ShowJob`
        """
        self._job = job

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this ShowJobsResponse.

        :return: The x_request_id of this ShowJobsResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this ShowJobsResponse.

        :param x_request_id: The x_request_id of this ShowJobsResponse.
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
        if not isinstance(other, ShowJobsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
