# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateFlinkSqlResponse(SdkResponse):

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
        'job': 'UpdateJobRespJob'
    }

    attribute_map = {
        'is_success': 'is_success',
        'message': 'message',
        'job': 'job'
    }

    def __init__(self, is_success=None, message=None, job=None):
        """UpdateFlinkSqlResponse

        The model defined in huaweicloud sdk

        :param is_success: 执行请求是否成功。“true”表示请求执行成功。
        :type is_success: bool
        :param message: 消息内容。
        :type message: str
        :param job: 
        :type job: :class:`huaweicloudsdkdli.v1.UpdateJobRespJob`
        """
        
        super(UpdateFlinkSqlResponse, self).__init__()

        self._is_success = None
        self._message = None
        self._job = None
        self.discriminator = None

        if is_success is not None:
            self.is_success = is_success
        if message is not None:
            self.message = message
        if job is not None:
            self.job = job

    @property
    def is_success(self):
        """Gets the is_success of this UpdateFlinkSqlResponse.

        执行请求是否成功。“true”表示请求执行成功。

        :return: The is_success of this UpdateFlinkSqlResponse.
        :rtype: bool
        """
        return self._is_success

    @is_success.setter
    def is_success(self, is_success):
        """Sets the is_success of this UpdateFlinkSqlResponse.

        执行请求是否成功。“true”表示请求执行成功。

        :param is_success: The is_success of this UpdateFlinkSqlResponse.
        :type is_success: bool
        """
        self._is_success = is_success

    @property
    def message(self):
        """Gets the message of this UpdateFlinkSqlResponse.

        消息内容。

        :return: The message of this UpdateFlinkSqlResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this UpdateFlinkSqlResponse.

        消息内容。

        :param message: The message of this UpdateFlinkSqlResponse.
        :type message: str
        """
        self._message = message

    @property
    def job(self):
        """Gets the job of this UpdateFlinkSqlResponse.


        :return: The job of this UpdateFlinkSqlResponse.
        :rtype: :class:`huaweicloudsdkdli.v1.UpdateJobRespJob`
        """
        return self._job

    @job.setter
    def job(self, job):
        """Sets the job of this UpdateFlinkSqlResponse.


        :param job: The job of this UpdateFlinkSqlResponse.
        :type job: :class:`huaweicloudsdkdli.v1.UpdateJobRespJob`
        """
        self._job = job

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
        if not isinstance(other, UpdateFlinkSqlResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
