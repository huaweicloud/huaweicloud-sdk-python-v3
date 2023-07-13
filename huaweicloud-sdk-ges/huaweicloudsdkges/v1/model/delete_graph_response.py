# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteGraphResponse(SdkResponse):

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
        'error_message': 'str',
        'error_code': 'str'
    }

    attribute_map = {
        'job_id': 'jobId',
        'error_message': 'errorMessage',
        'error_code': 'errorCode'
    }

    def __init__(self, job_id=None, error_message=None, error_code=None):
        """DeleteGraphResponse

        The model defined in huaweicloud sdk

        :param job_id: 删除图任务ID。请求失败时字段为空。 &gt;可以查询jobId查看任务执行状态、获取返回结果
        :type job_id: str
        :param error_message: 系统提示信息，执行成功时，字段可能为空。执行失败时，用于显示错误信息。
        :type error_message: str
        :param error_code: 系统提示信息，执行成功时，字段可能为空。执行失败时，用于显示错误码。
        :type error_code: str
        """
        
        super(DeleteGraphResponse, self).__init__()

        self._job_id = None
        self._error_message = None
        self._error_code = None
        self.discriminator = None

        if job_id is not None:
            self.job_id = job_id
        if error_message is not None:
            self.error_message = error_message
        if error_code is not None:
            self.error_code = error_code

    @property
    def job_id(self):
        """Gets the job_id of this DeleteGraphResponse.

        删除图任务ID。请求失败时字段为空。 >可以查询jobId查看任务执行状态、获取返回结果

        :return: The job_id of this DeleteGraphResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this DeleteGraphResponse.

        删除图任务ID。请求失败时字段为空。 >可以查询jobId查看任务执行状态、获取返回结果

        :param job_id: The job_id of this DeleteGraphResponse.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def error_message(self):
        """Gets the error_message of this DeleteGraphResponse.

        系统提示信息，执行成功时，字段可能为空。执行失败时，用于显示错误信息。

        :return: The error_message of this DeleteGraphResponse.
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """Sets the error_message of this DeleteGraphResponse.

        系统提示信息，执行成功时，字段可能为空。执行失败时，用于显示错误信息。

        :param error_message: The error_message of this DeleteGraphResponse.
        :type error_message: str
        """
        self._error_message = error_message

    @property
    def error_code(self):
        """Gets the error_code of this DeleteGraphResponse.

        系统提示信息，执行成功时，字段可能为空。执行失败时，用于显示错误码。

        :return: The error_code of this DeleteGraphResponse.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this DeleteGraphResponse.

        系统提示信息，执行成功时，字段可能为空。执行失败时，用于显示错误码。

        :param error_code: The error_code of this DeleteGraphResponse.
        :type error_code: str
        """
        self._error_code = error_code

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
        if not isinstance(other, DeleteGraphResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
