# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DebugApiV2Response(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'request': 'str',
        'response': 'str',
        'latency': 'int',
        'log': 'str'
    }

    attribute_map = {
        'request': 'request',
        'response': 'response',
        'latency': 'latency',
        'log': 'log'
    }

    def __init__(self, request=None, response=None, latency=None, log=None):
        """DebugApiV2Response

        The model defined in huaweicloud sdk

        :param request: 调试请求报文内容
        :type request: str
        :param response: 调试响应报文内容，响应消息体最大支持2097152字节，超过部分会被截断 &gt; 响应消息体超过限制长度时，超过部分会被截断，并追加\&quot;[TRUNCATED]\&quot;信息。
        :type response: str
        :param latency: 调试耗时，单位：毫秒
        :type latency: int
        :param log: 调试过程日志
        :type log: str
        """
        
        super(DebugApiV2Response, self).__init__()

        self._request = None
        self._response = None
        self._latency = None
        self._log = None
        self.discriminator = None

        if request is not None:
            self.request = request
        if response is not None:
            self.response = response
        if latency is not None:
            self.latency = latency
        if log is not None:
            self.log = log

    @property
    def request(self):
        """Gets the request of this DebugApiV2Response.

        调试请求报文内容

        :return: The request of this DebugApiV2Response.
        :rtype: str
        """
        return self._request

    @request.setter
    def request(self, request):
        """Sets the request of this DebugApiV2Response.

        调试请求报文内容

        :param request: The request of this DebugApiV2Response.
        :type request: str
        """
        self._request = request

    @property
    def response(self):
        """Gets the response of this DebugApiV2Response.

        调试响应报文内容，响应消息体最大支持2097152字节，超过部分会被截断 > 响应消息体超过限制长度时，超过部分会被截断，并追加\"[TRUNCATED]\"信息。

        :return: The response of this DebugApiV2Response.
        :rtype: str
        """
        return self._response

    @response.setter
    def response(self, response):
        """Sets the response of this DebugApiV2Response.

        调试响应报文内容，响应消息体最大支持2097152字节，超过部分会被截断 > 响应消息体超过限制长度时，超过部分会被截断，并追加\"[TRUNCATED]\"信息。

        :param response: The response of this DebugApiV2Response.
        :type response: str
        """
        self._response = response

    @property
    def latency(self):
        """Gets the latency of this DebugApiV2Response.

        调试耗时，单位：毫秒

        :return: The latency of this DebugApiV2Response.
        :rtype: int
        """
        return self._latency

    @latency.setter
    def latency(self, latency):
        """Sets the latency of this DebugApiV2Response.

        调试耗时，单位：毫秒

        :param latency: The latency of this DebugApiV2Response.
        :type latency: int
        """
        self._latency = latency

    @property
    def log(self):
        """Gets the log of this DebugApiV2Response.

        调试过程日志

        :return: The log of this DebugApiV2Response.
        :rtype: str
        """
        return self._log

    @log.setter
    def log(self, log):
        """Sets the log of this DebugApiV2Response.

        调试过程日志

        :param log: The log of this DebugApiV2Response.
        :type log: str
        """
        self._log = log

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
        if not isinstance(other, DebugApiV2Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
