# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowResJobResponse(SdkResponse):

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
        'jobs': 'list[Jobs]',
        'message': 'str',
        'error_code': 'str'
    }

    attribute_map = {
        'is_success': 'is_success',
        'jobs': 'jobs',
        'message': 'message',
        'error_code': 'error_code'
    }

    def __init__(self, is_success=None, jobs=None, message=None, error_code=None):
        r"""ShowResJobResponse

        The model defined in huaweicloud sdk

        :param is_success: 是否成功
        :type is_success: bool
        :param jobs: 作业详情
        :type jobs: list[:class:`huaweicloudsdkres.v1.Jobs`]
        :param message: 返回消息（请求成功时，不返回此字段）
        :type message: str
        :param error_code: 错误码（请求成功时，不返回此字段）
        :type error_code: str
        """
        
        super(ShowResJobResponse, self).__init__()

        self._is_success = None
        self._jobs = None
        self._message = None
        self._error_code = None
        self.discriminator = None

        if is_success is not None:
            self.is_success = is_success
        if jobs is not None:
            self.jobs = jobs
        if message is not None:
            self.message = message
        if error_code is not None:
            self.error_code = error_code

    @property
    def is_success(self):
        r"""Gets the is_success of this ShowResJobResponse.

        是否成功

        :return: The is_success of this ShowResJobResponse.
        :rtype: bool
        """
        return self._is_success

    @is_success.setter
    def is_success(self, is_success):
        r"""Sets the is_success of this ShowResJobResponse.

        是否成功

        :param is_success: The is_success of this ShowResJobResponse.
        :type is_success: bool
        """
        self._is_success = is_success

    @property
    def jobs(self):
        r"""Gets the jobs of this ShowResJobResponse.

        作业详情

        :return: The jobs of this ShowResJobResponse.
        :rtype: list[:class:`huaweicloudsdkres.v1.Jobs`]
        """
        return self._jobs

    @jobs.setter
    def jobs(self, jobs):
        r"""Sets the jobs of this ShowResJobResponse.

        作业详情

        :param jobs: The jobs of this ShowResJobResponse.
        :type jobs: list[:class:`huaweicloudsdkres.v1.Jobs`]
        """
        self._jobs = jobs

    @property
    def message(self):
        r"""Gets the message of this ShowResJobResponse.

        返回消息（请求成功时，不返回此字段）

        :return: The message of this ShowResJobResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this ShowResJobResponse.

        返回消息（请求成功时，不返回此字段）

        :param message: The message of this ShowResJobResponse.
        :type message: str
        """
        self._message = message

    @property
    def error_code(self):
        r"""Gets the error_code of this ShowResJobResponse.

        错误码（请求成功时，不返回此字段）

        :return: The error_code of this ShowResJobResponse.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        r"""Sets the error_code of this ShowResJobResponse.

        错误码（请求成功时，不返回此字段）

        :param error_code: The error_code of this ShowResJobResponse.
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
        if not isinstance(other, ShowResJobResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
