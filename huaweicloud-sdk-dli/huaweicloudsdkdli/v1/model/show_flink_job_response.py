# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowFlinkJobResponse(SdkResponse):

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
        'job_detail': 'FlinkJob'
    }

    attribute_map = {
        'is_success': 'is_success',
        'message': 'message',
        'job_detail': 'job_detail'
    }

    def __init__(self, is_success=None, message=None, job_detail=None):
        r"""ShowFlinkJobResponse

        The model defined in huaweicloud sdk

        :param is_success: 执行请求是否成功。“true”表示请求执行成功。
        :type is_success: str
        :param message: 系统提示信息，执行成功时，信息可能为空。
        :type message: str
        :param job_detail: 
        :type job_detail: :class:`huaweicloudsdkdli.v1.FlinkJob`
        """
        
        super(ShowFlinkJobResponse, self).__init__()

        self._is_success = None
        self._message = None
        self._job_detail = None
        self.discriminator = None

        if is_success is not None:
            self.is_success = is_success
        if message is not None:
            self.message = message
        if job_detail is not None:
            self.job_detail = job_detail

    @property
    def is_success(self):
        r"""Gets the is_success of this ShowFlinkJobResponse.

        执行请求是否成功。“true”表示请求执行成功。

        :return: The is_success of this ShowFlinkJobResponse.
        :rtype: str
        """
        return self._is_success

    @is_success.setter
    def is_success(self, is_success):
        r"""Sets the is_success of this ShowFlinkJobResponse.

        执行请求是否成功。“true”表示请求执行成功。

        :param is_success: The is_success of this ShowFlinkJobResponse.
        :type is_success: str
        """
        self._is_success = is_success

    @property
    def message(self):
        r"""Gets the message of this ShowFlinkJobResponse.

        系统提示信息，执行成功时，信息可能为空。

        :return: The message of this ShowFlinkJobResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this ShowFlinkJobResponse.

        系统提示信息，执行成功时，信息可能为空。

        :param message: The message of this ShowFlinkJobResponse.
        :type message: str
        """
        self._message = message

    @property
    def job_detail(self):
        r"""Gets the job_detail of this ShowFlinkJobResponse.

        :return: The job_detail of this ShowFlinkJobResponse.
        :rtype: :class:`huaweicloudsdkdli.v1.FlinkJob`
        """
        return self._job_detail

    @job_detail.setter
    def job_detail(self, job_detail):
        r"""Sets the job_detail of this ShowFlinkJobResponse.

        :param job_detail: The job_detail of this ShowFlinkJobResponse.
        :type job_detail: :class:`huaweicloudsdkdli.v1.FlinkJob`
        """
        self._job_detail = job_detail

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
        if not isinstance(other, ShowFlinkJobResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
