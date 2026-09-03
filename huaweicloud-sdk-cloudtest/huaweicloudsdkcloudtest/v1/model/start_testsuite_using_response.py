# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StartTestsuiteUsingResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'error': 'Error',
        'et_trace_id': 'str',
        'result': 'TaskBasicInfoVo',
        'status': 'str',
        'warn': 'Warn'
    }

    attribute_map = {
        'error': 'error',
        'et_trace_id': 'et_trace_id',
        'result': 'result',
        'status': 'status',
        'warn': 'warn'
    }

    def __init__(self, error=None, et_trace_id=None, result=None, status=None, warn=None):
        r"""StartTestsuiteUsingResponse

        The model defined in huaweicloud sdk

        :param error: 
        :type error: :class:`huaweicloudsdkcloudtest.v1.Error`
        :param et_trace_id: 
        :type et_trace_id: str
        :param result: 
        :type result: :class:`huaweicloudsdkcloudtest.v1.TaskBasicInfoVo`
        :param status: 
        :type status: str
        :param warn: 
        :type warn: :class:`huaweicloudsdkcloudtest.v1.Warn`
        """
        
        super().__init__()

        self._error = None
        self._et_trace_id = None
        self._result = None
        self._status = None
        self._warn = None
        self.discriminator = None

        if error is not None:
            self.error = error
        if et_trace_id is not None:
            self.et_trace_id = et_trace_id
        if result is not None:
            self.result = result
        if status is not None:
            self.status = status
        if warn is not None:
            self.warn = warn

    @property
    def error(self):
        r"""Gets the error of this StartTestsuiteUsingResponse.

        :return: The error of this StartTestsuiteUsingResponse.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.Error`
        """
        return self._error

    @error.setter
    def error(self, error):
        r"""Sets the error of this StartTestsuiteUsingResponse.

        :param error: The error of this StartTestsuiteUsingResponse.
        :type error: :class:`huaweicloudsdkcloudtest.v1.Error`
        """
        self._error = error

    @property
    def et_trace_id(self):
        r"""Gets the et_trace_id of this StartTestsuiteUsingResponse.

        :return: The et_trace_id of this StartTestsuiteUsingResponse.
        :rtype: str
        """
        return self._et_trace_id

    @et_trace_id.setter
    def et_trace_id(self, et_trace_id):
        r"""Sets the et_trace_id of this StartTestsuiteUsingResponse.

        :param et_trace_id: The et_trace_id of this StartTestsuiteUsingResponse.
        :type et_trace_id: str
        """
        self._et_trace_id = et_trace_id

    @property
    def result(self):
        r"""Gets the result of this StartTestsuiteUsingResponse.

        :return: The result of this StartTestsuiteUsingResponse.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.TaskBasicInfoVo`
        """
        return self._result

    @result.setter
    def result(self, result):
        r"""Sets the result of this StartTestsuiteUsingResponse.

        :param result: The result of this StartTestsuiteUsingResponse.
        :type result: :class:`huaweicloudsdkcloudtest.v1.TaskBasicInfoVo`
        """
        self._result = result

    @property
    def status(self):
        r"""Gets the status of this StartTestsuiteUsingResponse.

        :return: The status of this StartTestsuiteUsingResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this StartTestsuiteUsingResponse.

        :param status: The status of this StartTestsuiteUsingResponse.
        :type status: str
        """
        self._status = status

    @property
    def warn(self):
        r"""Gets the warn of this StartTestsuiteUsingResponse.

        :return: The warn of this StartTestsuiteUsingResponse.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.Warn`
        """
        return self._warn

    @warn.setter
    def warn(self, warn):
        r"""Sets the warn of this StartTestsuiteUsingResponse.

        :param warn: The warn of this StartTestsuiteUsingResponse.
        :type warn: :class:`huaweicloudsdkcloudtest.v1.Warn`
        """
        self._warn = warn

    def to_dict(self):
        import warnings
        warnings.warn("StartTestsuiteUsingResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, StartTestsuiteUsingResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
