# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListFlinkJobsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'is_success': 'bool',
        'message': 'str',
        'job_list': 'ListStreamJobRespJobs'
    }

    attribute_map = {
        'is_success': 'is_success',
        'message': 'message',
        'job_list': 'job_list'
    }

    def __init__(self, is_success=None, message=None, job_list=None):
        """ListFlinkJobsResponse

        The model defined in huaweicloud sdk

        :param is_success: 执行请求是否成功。“true”表示请求执行成功。
        :type is_success: bool
        :param message: 系统提示信息，执行成功时，信息可能为空。
        :type message: str
        :param job_list: 
        :type job_list: :class:`huaweicloudsdkdli.v1.ListStreamJobRespJobs`
        """
        
        super(ListFlinkJobsResponse, self).__init__()

        self._is_success = None
        self._message = None
        self._job_list = None
        self.discriminator = None

        if is_success is not None:
            self.is_success = is_success
        if message is not None:
            self.message = message
        if job_list is not None:
            self.job_list = job_list

    @property
    def is_success(self):
        """Gets the is_success of this ListFlinkJobsResponse.

        执行请求是否成功。“true”表示请求执行成功。

        :return: The is_success of this ListFlinkJobsResponse.
        :rtype: bool
        """
        return self._is_success

    @is_success.setter
    def is_success(self, is_success):
        """Sets the is_success of this ListFlinkJobsResponse.

        执行请求是否成功。“true”表示请求执行成功。

        :param is_success: The is_success of this ListFlinkJobsResponse.
        :type is_success: bool
        """
        self._is_success = is_success

    @property
    def message(self):
        """Gets the message of this ListFlinkJobsResponse.

        系统提示信息，执行成功时，信息可能为空。

        :return: The message of this ListFlinkJobsResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ListFlinkJobsResponse.

        系统提示信息，执行成功时，信息可能为空。

        :param message: The message of this ListFlinkJobsResponse.
        :type message: str
        """
        self._message = message

    @property
    def job_list(self):
        """Gets the job_list of this ListFlinkJobsResponse.


        :return: The job_list of this ListFlinkJobsResponse.
        :rtype: :class:`huaweicloudsdkdli.v1.ListStreamJobRespJobs`
        """
        return self._job_list

    @job_list.setter
    def job_list(self, job_list):
        """Sets the job_list of this ListFlinkJobsResponse.


        :param job_list: The job_list of this ListFlinkJobsResponse.
        :type job_list: :class:`huaweicloudsdkdli.v1.ListStreamJobRespJobs`
        """
        self._job_list = job_list

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
        if not isinstance(other, ListFlinkJobsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
