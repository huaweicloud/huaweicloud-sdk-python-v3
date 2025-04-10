# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListUserDnsMappingResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'error': 'CommonResponseErrorOfAPITest',
        'reason': 'str',
        'result': 'DnsMapping',
        'status': 'str',
        'code': 'str'
    }

    attribute_map = {
        'error': 'error',
        'reason': 'reason',
        'result': 'result',
        'status': 'status',
        'code': 'code'
    }

    def __init__(self, error=None, reason=None, result=None, status=None, code=None):
        r"""ListUserDnsMappingResponse

        The model defined in huaweicloud sdk

        :param error: 
        :type error: :class:`huaweicloudsdkcloudtest.v1.CommonResponseErrorOfAPITest`
        :param reason: 错误原因
        :type reason: str
        :param result: 
        :type result: :class:`huaweicloudsdkcloudtest.v1.DnsMapping`
        :param status: 状态值，如success、error
        :type status: str
        :param code: 错误码
        :type code: str
        """
        
        super(ListUserDnsMappingResponse, self).__init__()

        self._error = None
        self._reason = None
        self._result = None
        self._status = None
        self._code = None
        self.discriminator = None

        if error is not None:
            self.error = error
        if reason is not None:
            self.reason = reason
        if result is not None:
            self.result = result
        if status is not None:
            self.status = status
        if code is not None:
            self.code = code

    @property
    def error(self):
        r"""Gets the error of this ListUserDnsMappingResponse.

        :return: The error of this ListUserDnsMappingResponse.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.CommonResponseErrorOfAPITest`
        """
        return self._error

    @error.setter
    def error(self, error):
        r"""Sets the error of this ListUserDnsMappingResponse.

        :param error: The error of this ListUserDnsMappingResponse.
        :type error: :class:`huaweicloudsdkcloudtest.v1.CommonResponseErrorOfAPITest`
        """
        self._error = error

    @property
    def reason(self):
        r"""Gets the reason of this ListUserDnsMappingResponse.

        错误原因

        :return: The reason of this ListUserDnsMappingResponse.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        r"""Sets the reason of this ListUserDnsMappingResponse.

        错误原因

        :param reason: The reason of this ListUserDnsMappingResponse.
        :type reason: str
        """
        self._reason = reason

    @property
    def result(self):
        r"""Gets the result of this ListUserDnsMappingResponse.

        :return: The result of this ListUserDnsMappingResponse.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.DnsMapping`
        """
        return self._result

    @result.setter
    def result(self, result):
        r"""Sets the result of this ListUserDnsMappingResponse.

        :param result: The result of this ListUserDnsMappingResponse.
        :type result: :class:`huaweicloudsdkcloudtest.v1.DnsMapping`
        """
        self._result = result

    @property
    def status(self):
        r"""Gets the status of this ListUserDnsMappingResponse.

        状态值，如success、error

        :return: The status of this ListUserDnsMappingResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListUserDnsMappingResponse.

        状态值，如success、error

        :param status: The status of this ListUserDnsMappingResponse.
        :type status: str
        """
        self._status = status

    @property
    def code(self):
        r"""Gets the code of this ListUserDnsMappingResponse.

        错误码

        :return: The code of this ListUserDnsMappingResponse.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        r"""Sets the code of this ListUserDnsMappingResponse.

        错误码

        :param code: The code of this ListUserDnsMappingResponse.
        :type code: str
        """
        self._code = code

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
        if not isinstance(other, ListUserDnsMappingResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
