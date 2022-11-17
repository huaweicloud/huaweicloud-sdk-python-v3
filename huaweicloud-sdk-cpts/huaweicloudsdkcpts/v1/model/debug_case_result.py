# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DebugCaseResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'body': 'str',
        'error_reason': 'str',
        'header': 'DebugCaseResultHeader',
        'name': 'str',
        'response_time': 'int',
        'result': 'int',
        'return_body': 'str',
        'return_header': 'DebugCaseReturnHeader',
        'status_code': 'str',
        'url': 'str'
    }

    attribute_map = {
        'body': 'body',
        'error_reason': 'errorReason',
        'header': 'header',
        'name': 'name',
        'response_time': 'responseTime',
        'result': 'result',
        'return_body': 'returnBody',
        'return_header': 'returnHeader',
        'status_code': 'statusCode',
        'url': 'url'
    }

    def __init__(self, body=None, error_reason=None, header=None, name=None, response_time=None, result=None, return_body=None, return_header=None, status_code=None, url=None):
        """DebugCaseResult

        The model defined in huaweicloud sdk

        :param body: body
        :type body: str
        :param error_reason: errorReason
        :type error_reason: str
        :param header: 
        :type header: :class:`huaweicloudsdkcpts.v1.DebugCaseResultHeader`
        :param name: name
        :type name: str
        :param response_time: responseTime
        :type response_time: int
        :param result: result
        :type result: int
        :param return_body: returnBody
        :type return_body: str
        :param return_header: 
        :type return_header: :class:`huaweicloudsdkcpts.v1.DebugCaseReturnHeader`
        :param status_code: statusCode
        :type status_code: str
        :param url: url
        :type url: str
        """
        
        

        self._body = None
        self._error_reason = None
        self._header = None
        self._name = None
        self._response_time = None
        self._result = None
        self._return_body = None
        self._return_header = None
        self._status_code = None
        self._url = None
        self.discriminator = None

        if body is not None:
            self.body = body
        if error_reason is not None:
            self.error_reason = error_reason
        if header is not None:
            self.header = header
        if name is not None:
            self.name = name
        if response_time is not None:
            self.response_time = response_time
        if result is not None:
            self.result = result
        if return_body is not None:
            self.return_body = return_body
        if return_header is not None:
            self.return_header = return_header
        if status_code is not None:
            self.status_code = status_code
        if url is not None:
            self.url = url

    @property
    def body(self):
        """Gets the body of this DebugCaseResult.

        body

        :return: The body of this DebugCaseResult.
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this DebugCaseResult.

        body

        :param body: The body of this DebugCaseResult.
        :type body: str
        """
        self._body = body

    @property
    def error_reason(self):
        """Gets the error_reason of this DebugCaseResult.

        errorReason

        :return: The error_reason of this DebugCaseResult.
        :rtype: str
        """
        return self._error_reason

    @error_reason.setter
    def error_reason(self, error_reason):
        """Sets the error_reason of this DebugCaseResult.

        errorReason

        :param error_reason: The error_reason of this DebugCaseResult.
        :type error_reason: str
        """
        self._error_reason = error_reason

    @property
    def header(self):
        """Gets the header of this DebugCaseResult.

        :return: The header of this DebugCaseResult.
        :rtype: :class:`huaweicloudsdkcpts.v1.DebugCaseResultHeader`
        """
        return self._header

    @header.setter
    def header(self, header):
        """Sets the header of this DebugCaseResult.

        :param header: The header of this DebugCaseResult.
        :type header: :class:`huaweicloudsdkcpts.v1.DebugCaseResultHeader`
        """
        self._header = header

    @property
    def name(self):
        """Gets the name of this DebugCaseResult.

        name

        :return: The name of this DebugCaseResult.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DebugCaseResult.

        name

        :param name: The name of this DebugCaseResult.
        :type name: str
        """
        self._name = name

    @property
    def response_time(self):
        """Gets the response_time of this DebugCaseResult.

        responseTime

        :return: The response_time of this DebugCaseResult.
        :rtype: int
        """
        return self._response_time

    @response_time.setter
    def response_time(self, response_time):
        """Sets the response_time of this DebugCaseResult.

        responseTime

        :param response_time: The response_time of this DebugCaseResult.
        :type response_time: int
        """
        self._response_time = response_time

    @property
    def result(self):
        """Gets the result of this DebugCaseResult.

        result

        :return: The result of this DebugCaseResult.
        :rtype: int
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this DebugCaseResult.

        result

        :param result: The result of this DebugCaseResult.
        :type result: int
        """
        self._result = result

    @property
    def return_body(self):
        """Gets the return_body of this DebugCaseResult.

        returnBody

        :return: The return_body of this DebugCaseResult.
        :rtype: str
        """
        return self._return_body

    @return_body.setter
    def return_body(self, return_body):
        """Sets the return_body of this DebugCaseResult.

        returnBody

        :param return_body: The return_body of this DebugCaseResult.
        :type return_body: str
        """
        self._return_body = return_body

    @property
    def return_header(self):
        """Gets the return_header of this DebugCaseResult.

        :return: The return_header of this DebugCaseResult.
        :rtype: :class:`huaweicloudsdkcpts.v1.DebugCaseReturnHeader`
        """
        return self._return_header

    @return_header.setter
    def return_header(self, return_header):
        """Sets the return_header of this DebugCaseResult.

        :param return_header: The return_header of this DebugCaseResult.
        :type return_header: :class:`huaweicloudsdkcpts.v1.DebugCaseReturnHeader`
        """
        self._return_header = return_header

    @property
    def status_code(self):
        """Gets the status_code of this DebugCaseResult.

        statusCode

        :return: The status_code of this DebugCaseResult.
        :rtype: str
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code):
        """Sets the status_code of this DebugCaseResult.

        statusCode

        :param status_code: The status_code of this DebugCaseResult.
        :type status_code: str
        """
        self._status_code = status_code

    @property
    def url(self):
        """Gets the url of this DebugCaseResult.

        url

        :return: The url of this DebugCaseResult.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this DebugCaseResult.

        url

        :param url: The url of this DebugCaseResult.
        :type url: str
        """
        self._url = url

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
        if not isinstance(other, DebugCaseResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
