# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateBatchAsyncJobsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'async_job_id': 'str',
        'x_language': 'str',
        'body': 'BatchAsyncUpdateJobReq'
    }

    attribute_map = {
        'async_job_id': 'async_job_id',
        'x_language': 'X-Language',
        'body': 'body'
    }

    def __init__(self, async_job_id=None, x_language=None, body=None):
        r"""UpdateBatchAsyncJobsRequest

        The model defined in huaweicloud sdk

        :param async_job_id: 批量异步创建的任务ID，由创建批量异步任务接口返回。
        :type async_job_id: str
        :param x_language: 请求语言类型。
        :type x_language: str
        :param body: Body of the UpdateBatchAsyncJobsRequest
        :type body: :class:`huaweicloudsdkdrs.v5.BatchAsyncUpdateJobReq`
        """
        
        

        self._async_job_id = None
        self._x_language = None
        self._body = None
        self.discriminator = None

        self.async_job_id = async_job_id
        if x_language is not None:
            self.x_language = x_language
        if body is not None:
            self.body = body

    @property
    def async_job_id(self):
        r"""Gets the async_job_id of this UpdateBatchAsyncJobsRequest.

        批量异步创建的任务ID，由创建批量异步任务接口返回。

        :return: The async_job_id of this UpdateBatchAsyncJobsRequest.
        :rtype: str
        """
        return self._async_job_id

    @async_job_id.setter
    def async_job_id(self, async_job_id):
        r"""Sets the async_job_id of this UpdateBatchAsyncJobsRequest.

        批量异步创建的任务ID，由创建批量异步任务接口返回。

        :param async_job_id: The async_job_id of this UpdateBatchAsyncJobsRequest.
        :type async_job_id: str
        """
        self._async_job_id = async_job_id

    @property
    def x_language(self):
        r"""Gets the x_language of this UpdateBatchAsyncJobsRequest.

        请求语言类型。

        :return: The x_language of this UpdateBatchAsyncJobsRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this UpdateBatchAsyncJobsRequest.

        请求语言类型。

        :param x_language: The x_language of this UpdateBatchAsyncJobsRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def body(self):
        r"""Gets the body of this UpdateBatchAsyncJobsRequest.

        :return: The body of this UpdateBatchAsyncJobsRequest.
        :rtype: :class:`huaweicloudsdkdrs.v5.BatchAsyncUpdateJobReq`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateBatchAsyncJobsRequest.

        :param body: The body of this UpdateBatchAsyncJobsRequest.
        :type body: :class:`huaweicloudsdkdrs.v5.BatchAsyncUpdateJobReq`
        """
        self._body = body

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
        if not isinstance(other, UpdateBatchAsyncJobsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
