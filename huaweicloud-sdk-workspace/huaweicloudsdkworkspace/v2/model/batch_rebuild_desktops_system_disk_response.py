# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchRebuildDesktopsSystemDiskResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'error_code': 'str',
        'error_msg': 'str',
        'encoded_authorization_message': 'str',
        'job_id': 'str'
    }

    attribute_map = {
        'error_code': 'error_code',
        'error_msg': 'error_msg',
        'encoded_authorization_message': 'encoded_authorization_message',
        'job_id': 'job_id'
    }

    def __init__(self, error_code=None, error_msg=None, encoded_authorization_message=None, job_id=None):
        r"""BatchRebuildDesktopsSystemDiskResponse

        The model defined in huaweicloud sdk

        :param error_code: 错误码。
        :type error_code: str
        :param error_msg: 错误描述。
        :type error_msg: str
        :param encoded_authorization_message: 加密后的详细拒绝原因，用户可以自行调用STS服务的decode-authorization-message接口进行解密。
        :type encoded_authorization_message: str
        :param job_id: 重建系统盘总任务id。
        :type job_id: str
        """
        
        super(BatchRebuildDesktopsSystemDiskResponse, self).__init__()

        self._error_code = None
        self._error_msg = None
        self._encoded_authorization_message = None
        self._job_id = None
        self.discriminator = None

        if error_code is not None:
            self.error_code = error_code
        if error_msg is not None:
            self.error_msg = error_msg
        if encoded_authorization_message is not None:
            self.encoded_authorization_message = encoded_authorization_message
        if job_id is not None:
            self.job_id = job_id

    @property
    def error_code(self):
        r"""Gets the error_code of this BatchRebuildDesktopsSystemDiskResponse.

        错误码。

        :return: The error_code of this BatchRebuildDesktopsSystemDiskResponse.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        r"""Sets the error_code of this BatchRebuildDesktopsSystemDiskResponse.

        错误码。

        :param error_code: The error_code of this BatchRebuildDesktopsSystemDiskResponse.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def error_msg(self):
        r"""Gets the error_msg of this BatchRebuildDesktopsSystemDiskResponse.

        错误描述。

        :return: The error_msg of this BatchRebuildDesktopsSystemDiskResponse.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        r"""Sets the error_msg of this BatchRebuildDesktopsSystemDiskResponse.

        错误描述。

        :param error_msg: The error_msg of this BatchRebuildDesktopsSystemDiskResponse.
        :type error_msg: str
        """
        self._error_msg = error_msg

    @property
    def encoded_authorization_message(self):
        r"""Gets the encoded_authorization_message of this BatchRebuildDesktopsSystemDiskResponse.

        加密后的详细拒绝原因，用户可以自行调用STS服务的decode-authorization-message接口进行解密。

        :return: The encoded_authorization_message of this BatchRebuildDesktopsSystemDiskResponse.
        :rtype: str
        """
        return self._encoded_authorization_message

    @encoded_authorization_message.setter
    def encoded_authorization_message(self, encoded_authorization_message):
        r"""Sets the encoded_authorization_message of this BatchRebuildDesktopsSystemDiskResponse.

        加密后的详细拒绝原因，用户可以自行调用STS服务的decode-authorization-message接口进行解密。

        :param encoded_authorization_message: The encoded_authorization_message of this BatchRebuildDesktopsSystemDiskResponse.
        :type encoded_authorization_message: str
        """
        self._encoded_authorization_message = encoded_authorization_message

    @property
    def job_id(self):
        r"""Gets the job_id of this BatchRebuildDesktopsSystemDiskResponse.

        重建系统盘总任务id。

        :return: The job_id of this BatchRebuildDesktopsSystemDiskResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this BatchRebuildDesktopsSystemDiskResponse.

        重建系统盘总任务id。

        :param job_id: The job_id of this BatchRebuildDesktopsSystemDiskResponse.
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
        if not isinstance(other, BatchRebuildDesktopsSystemDiskResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
