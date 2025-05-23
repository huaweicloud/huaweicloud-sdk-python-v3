# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImportFlinkJobsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'is_success': 'str',
        'message': 'str',
        'job_mapping': 'list[JobMap]'
    }

    attribute_map = {
        'is_success': 'is_success',
        'message': 'message',
        'job_mapping': 'job_mapping'
    }

    def __init__(self, is_success=None, message=None, job_mapping=None):
        r"""ImportFlinkJobsResponse

        The model defined in huaweicloud sdk

        :param is_success: 执行请求是否成功。“true”表示请求执行成功。
        :type is_success: str
        :param message: 消息内容。
        :type message: str
        :param job_mapping: 作业导入结果。
        :type job_mapping: list[:class:`huaweicloudsdkdli.v1.JobMap`]
        """
        
        super(ImportFlinkJobsResponse, self).__init__()

        self._is_success = None
        self._message = None
        self._job_mapping = None
        self.discriminator = None

        if is_success is not None:
            self.is_success = is_success
        if message is not None:
            self.message = message
        if job_mapping is not None:
            self.job_mapping = job_mapping

    @property
    def is_success(self):
        r"""Gets the is_success of this ImportFlinkJobsResponse.

        执行请求是否成功。“true”表示请求执行成功。

        :return: The is_success of this ImportFlinkJobsResponse.
        :rtype: str
        """
        return self._is_success

    @is_success.setter
    def is_success(self, is_success):
        r"""Sets the is_success of this ImportFlinkJobsResponse.

        执行请求是否成功。“true”表示请求执行成功。

        :param is_success: The is_success of this ImportFlinkJobsResponse.
        :type is_success: str
        """
        self._is_success = is_success

    @property
    def message(self):
        r"""Gets the message of this ImportFlinkJobsResponse.

        消息内容。

        :return: The message of this ImportFlinkJobsResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this ImportFlinkJobsResponse.

        消息内容。

        :param message: The message of this ImportFlinkJobsResponse.
        :type message: str
        """
        self._message = message

    @property
    def job_mapping(self):
        r"""Gets the job_mapping of this ImportFlinkJobsResponse.

        作业导入结果。

        :return: The job_mapping of this ImportFlinkJobsResponse.
        :rtype: list[:class:`huaweicloudsdkdli.v1.JobMap`]
        """
        return self._job_mapping

    @job_mapping.setter
    def job_mapping(self, job_mapping):
        r"""Sets the job_mapping of this ImportFlinkJobsResponse.

        作业导入结果。

        :param job_mapping: The job_mapping of this ImportFlinkJobsResponse.
        :type job_mapping: list[:class:`huaweicloudsdkdli.v1.JobMap`]
        """
        self._job_mapping = job_mapping

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
        if not isinstance(other, ImportFlinkJobsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
