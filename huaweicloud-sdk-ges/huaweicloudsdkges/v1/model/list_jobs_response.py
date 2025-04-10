# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListJobsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'error_message': 'str',
        'error_code': 'str',
        'job_count': 'int',
        'job_list': 'list[Job]'
    }

    attribute_map = {
        'error_message': 'errorMessage',
        'error_code': 'errorCode',
        'job_count': 'jobCount',
        'job_list': 'jobList'
    }

    def __init__(self, error_message=None, error_code=None, job_count=None, job_list=None):
        r"""ListJobsResponse

        The model defined in huaweicloud sdk

        :param error_message: 系统提示信息，执行成功时，字段可能为空。执行失败时，用于显示错误信息。
        :type error_message: str
        :param error_code: 系统提示信息，执行成功时，字段可能为空。执行失败时，用于显示错误码。
        :type error_code: str
        :param job_count: 任务总数
        :type job_count: int
        :param job_list: 任务列表
        :type job_list: list[:class:`huaweicloudsdkges.v1.Job`]
        """
        
        super(ListJobsResponse, self).__init__()

        self._error_message = None
        self._error_code = None
        self._job_count = None
        self._job_list = None
        self.discriminator = None

        if error_message is not None:
            self.error_message = error_message
        if error_code is not None:
            self.error_code = error_code
        if job_count is not None:
            self.job_count = job_count
        if job_list is not None:
            self.job_list = job_list

    @property
    def error_message(self):
        r"""Gets the error_message of this ListJobsResponse.

        系统提示信息，执行成功时，字段可能为空。执行失败时，用于显示错误信息。

        :return: The error_message of this ListJobsResponse.
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        r"""Sets the error_message of this ListJobsResponse.

        系统提示信息，执行成功时，字段可能为空。执行失败时，用于显示错误信息。

        :param error_message: The error_message of this ListJobsResponse.
        :type error_message: str
        """
        self._error_message = error_message

    @property
    def error_code(self):
        r"""Gets the error_code of this ListJobsResponse.

        系统提示信息，执行成功时，字段可能为空。执行失败时，用于显示错误码。

        :return: The error_code of this ListJobsResponse.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        r"""Sets the error_code of this ListJobsResponse.

        系统提示信息，执行成功时，字段可能为空。执行失败时，用于显示错误码。

        :param error_code: The error_code of this ListJobsResponse.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def job_count(self):
        r"""Gets the job_count of this ListJobsResponse.

        任务总数

        :return: The job_count of this ListJobsResponse.
        :rtype: int
        """
        return self._job_count

    @job_count.setter
    def job_count(self, job_count):
        r"""Sets the job_count of this ListJobsResponse.

        任务总数

        :param job_count: The job_count of this ListJobsResponse.
        :type job_count: int
        """
        self._job_count = job_count

    @property
    def job_list(self):
        r"""Gets the job_list of this ListJobsResponse.

        任务列表

        :return: The job_list of this ListJobsResponse.
        :rtype: list[:class:`huaweicloudsdkges.v1.Job`]
        """
        return self._job_list

    @job_list.setter
    def job_list(self, job_list):
        r"""Sets the job_list of this ListJobsResponse.

        任务列表

        :param job_list: The job_list of this ListJobsResponse.
        :type job_list: list[:class:`huaweicloudsdkges.v1.Job`]
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
        if not isinstance(other, ListJobsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
