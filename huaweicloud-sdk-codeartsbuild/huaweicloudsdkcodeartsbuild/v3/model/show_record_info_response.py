# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowRecordInfoResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'success': 'bool',
        'message': 'str',
        'err_code': 'str',
        'result': 'RecordInfoResult'
    }

    attribute_map = {
        'success': 'success',
        'message': 'message',
        'err_code': 'err_code',
        'result': 'result'
    }

    def __init__(self, success=None, message=None, err_code=None, result=None):
        r"""ShowRecordInfoResponse

        The model defined in huaweicloud sdk

        :param success: 状态
        :type success: bool
        :param message: 消息
        :type message: str
        :param err_code: 错误码
        :type err_code: str
        :param result: 
        :type result: :class:`huaweicloudsdkcodeartsbuild.v3.RecordInfoResult`
        """
        
        super(ShowRecordInfoResponse, self).__init__()

        self._success = None
        self._message = None
        self._err_code = None
        self._result = None
        self.discriminator = None

        if success is not None:
            self.success = success
        if message is not None:
            self.message = message
        if err_code is not None:
            self.err_code = err_code
        if result is not None:
            self.result = result

    @property
    def success(self):
        r"""Gets the success of this ShowRecordInfoResponse.

        状态

        :return: The success of this ShowRecordInfoResponse.
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        r"""Sets the success of this ShowRecordInfoResponse.

        状态

        :param success: The success of this ShowRecordInfoResponse.
        :type success: bool
        """
        self._success = success

    @property
    def message(self):
        r"""Gets the message of this ShowRecordInfoResponse.

        消息

        :return: The message of this ShowRecordInfoResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this ShowRecordInfoResponse.

        消息

        :param message: The message of this ShowRecordInfoResponse.
        :type message: str
        """
        self._message = message

    @property
    def err_code(self):
        r"""Gets the err_code of this ShowRecordInfoResponse.

        错误码

        :return: The err_code of this ShowRecordInfoResponse.
        :rtype: str
        """
        return self._err_code

    @err_code.setter
    def err_code(self, err_code):
        r"""Sets the err_code of this ShowRecordInfoResponse.

        错误码

        :param err_code: The err_code of this ShowRecordInfoResponse.
        :type err_code: str
        """
        self._err_code = err_code

    @property
    def result(self):
        r"""Gets the result of this ShowRecordInfoResponse.

        :return: The result of this ShowRecordInfoResponse.
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.RecordInfoResult`
        """
        return self._result

    @result.setter
    def result(self, result):
        r"""Sets the result of this ShowRecordInfoResponse.

        :param result: The result of this ShowRecordInfoResponse.
        :type result: :class:`huaweicloudsdkcodeartsbuild.v3.RecordInfoResult`
        """
        self._result = result

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
        if not isinstance(other, ShowRecordInfoResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
