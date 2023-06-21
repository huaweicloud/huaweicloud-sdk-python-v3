# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DebugApiResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'request_id': 'str',
        'url': 'str',
        'result': 'str',
        'timeout': 'int',
        'success': 'bool',
        'request_header': 'ApiTestRequestHeader',
        'response_header': 'ApiTestResponseHeader'
    }

    attribute_map = {
        'request_id': 'request_id',
        'url': 'url',
        'result': 'result',
        'timeout': 'timeout',
        'success': 'success',
        'request_header': 'request_header',
        'response_header': 'response_header'
    }

    def __init__(self, request_id=None, url=None, result=None, timeout=None, success=None, request_header=None, response_header=None):
        """DebugApiResponse

        The model defined in huaweicloud sdk

        :param request_id: 请求编号
        :type request_id: str
        :param url: 请求url
        :type url: str
        :param result: 调试结果
        :type result: str
        :param timeout: 调试耗时
        :type timeout: int
        :param success: 是否调试成功
        :type success: bool
        :param request_header: 
        :type request_header: :class:`huaweicloudsdkdataartsstudio.v1.ApiTestRequestHeader`
        :param response_header: 
        :type response_header: :class:`huaweicloudsdkdataartsstudio.v1.ApiTestResponseHeader`
        """
        
        super(DebugApiResponse, self).__init__()

        self._request_id = None
        self._url = None
        self._result = None
        self._timeout = None
        self._success = None
        self._request_header = None
        self._response_header = None
        self.discriminator = None

        if request_id is not None:
            self.request_id = request_id
        if url is not None:
            self.url = url
        if result is not None:
            self.result = result
        if timeout is not None:
            self.timeout = timeout
        if success is not None:
            self.success = success
        if request_header is not None:
            self.request_header = request_header
        if response_header is not None:
            self.response_header = response_header

    @property
    def request_id(self):
        """Gets the request_id of this DebugApiResponse.

        请求编号

        :return: The request_id of this DebugApiResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this DebugApiResponse.

        请求编号

        :param request_id: The request_id of this DebugApiResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def url(self):
        """Gets the url of this DebugApiResponse.

        请求url

        :return: The url of this DebugApiResponse.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this DebugApiResponse.

        请求url

        :param url: The url of this DebugApiResponse.
        :type url: str
        """
        self._url = url

    @property
    def result(self):
        """Gets the result of this DebugApiResponse.

        调试结果

        :return: The result of this DebugApiResponse.
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this DebugApiResponse.

        调试结果

        :param result: The result of this DebugApiResponse.
        :type result: str
        """
        self._result = result

    @property
    def timeout(self):
        """Gets the timeout of this DebugApiResponse.

        调试耗时

        :return: The timeout of this DebugApiResponse.
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """Sets the timeout of this DebugApiResponse.

        调试耗时

        :param timeout: The timeout of this DebugApiResponse.
        :type timeout: int
        """
        self._timeout = timeout

    @property
    def success(self):
        """Gets the success of this DebugApiResponse.

        是否调试成功

        :return: The success of this DebugApiResponse.
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this DebugApiResponse.

        是否调试成功

        :param success: The success of this DebugApiResponse.
        :type success: bool
        """
        self._success = success

    @property
    def request_header(self):
        """Gets the request_header of this DebugApiResponse.

        :return: The request_header of this DebugApiResponse.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ApiTestRequestHeader`
        """
        return self._request_header

    @request_header.setter
    def request_header(self, request_header):
        """Sets the request_header of this DebugApiResponse.

        :param request_header: The request_header of this DebugApiResponse.
        :type request_header: :class:`huaweicloudsdkdataartsstudio.v1.ApiTestRequestHeader`
        """
        self._request_header = request_header

    @property
    def response_header(self):
        """Gets the response_header of this DebugApiResponse.

        :return: The response_header of this DebugApiResponse.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ApiTestResponseHeader`
        """
        return self._response_header

    @response_header.setter
    def response_header(self, response_header):
        """Sets the response_header of this DebugApiResponse.

        :param response_header: The response_header of this DebugApiResponse.
        :type response_header: :class:`huaweicloudsdkdataartsstudio.v1.ApiTestResponseHeader`
        """
        self._response_header = response_header

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
        if not isinstance(other, DebugApiResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
