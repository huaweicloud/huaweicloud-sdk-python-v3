# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApiPolicyMockBase:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'result_content': 'str',
        'status_code': 'int',
        'header': 'str'
    }

    attribute_map = {
        'result_content': 'result_content',
        'status_code': 'status_code',
        'header': 'header'
    }

    def __init__(self, result_content=None, status_code=None, header=None):
        """ApiPolicyMockBase

        The model defined in huaweicloud sdk

        :param result_content: 返回结果
        :type result_content: str
        :param status_code: mock后端自定义状态码： \&quot;200\&quot;: \&quot;OK\&quot;, \&quot;201\&quot;: \&quot;Created\&quot;, \&quot;202\&quot;: \&quot;Accepted\&quot;, \&quot;203\&quot;: \&quot;NonAuthoritativeInformation\&quot;, \&quot;204\&quot;: \&quot;NoContent\&quot;, \&quot;205\&quot;: \&quot;ResetContent\&quot;, \&quot;206\&quot;: \&quot;PartialContent\&quot;, \&quot;300\&quot;: \&quot;MultipleChoices\&quot;, \&quot;301\&quot;: \&quot;MovedPermanently\&quot;, \&quot;302\&quot;: \&quot;Found\&quot;, \&quot;303\&quot;: \&quot;SeeOther\&quot;, \&quot;304\&quot;: \&quot;NotModified\&quot;, \&quot;305\&quot;: \&quot;UseProxy\&quot;, \&quot;306\&quot;: \&quot;Unused\&quot;, \&quot;307\&quot;: \&quot;TemporaryRedirect\&quot;, \&quot;400\&quot;: \&quot;BadRequest\&quot;, \&quot;401\&quot;: \&quot;Unauthorized\&quot;, \&quot;402\&quot;: \&quot;PaymentRequired\&quot;, \&quot;403\&quot;: \&quot;Forbidden\&quot;, \&quot;404\&quot;: \&quot;NotFound\&quot;, \&quot;405\&quot;: \&quot;MethodNotAllowed\&quot;, \&quot;406\&quot;: \&quot;NotAcceptable\&quot;, \&quot;407\&quot;: \&quot;ProxyAuthenticationRequired\&quot;, \&quot;408\&quot;: \&quot;RequestTimeout\&quot;, \&quot;409\&quot;: \&quot;Conflict\&quot;, \&quot;410\&quot;: \&quot;Gone\&quot;, \&quot;411\&quot;: \&quot;LengthRequired\&quot;, \&quot;412\&quot;: \&quot;PreconditionFailed\&quot;, \&quot;413\&quot;: \&quot;RequestEntityTooLarge\&quot;, \&quot;414\&quot;: \&quot;RequestURITooLong\&quot;, \&quot;415\&quot;: \&quot;UnsupportedMediaType\&quot;, \&quot;416\&quot;: \&quot;RequestedRangeNotSatisfiable\&quot;, \&quot;417\&quot;: \&quot;ExpectationFailed\&quot;, \&quot;450\&quot;: \&quot;ParameterRequried\&quot;, \&quot;451\&quot;: \&quot;MethodConnectException\&quot;, \&quot;500\&quot;: \&quot;InternalServerError\&quot;, \&quot;501\&quot;: \&quot;NotImplemented\&quot;, \&quot;502\&quot;: \&quot;BadGateway\&quot;, \&quot;503\&quot;: \&quot;ServiceUnavailable\&quot;, \&quot;504\&quot;: \&quot;GatewayTimeout\&quot;, \&quot;505\&quot;: \&quot;HTTPVersionNotSupported\&quot;,
        :type status_code: int
        :param header: mock后端自定义响应头header  格式：[{\&quot;key\&quot;:\&quot;\&quot;,\&quot;value\&quot;: \&quot;\&quot;, \&quot;remark:\&quot;\&quot;}, {\&quot;key2\&quot;:\&quot;\&quot;,\&quot;value2\&quot;: \&quot;\&quot;,\&quot;remark2:\&quot;\&quot;}]  参数说明：  key：mock后端自定义响应头header key, 支持英文，数字，中划线，且只能以英文字母或数字开头，1 ~ 64字符  value： mock后端自定义响应头header value，中文字符必须为UTF-8或者unicode编码, 不能为空，最大长度为10240  remark：mock后端自定义响应头header remark，中文字符必须为UTF-8 或者unicode编码，可以为空，最大长度为2048
        :type header: str
        """
        
        

        self._result_content = None
        self._status_code = None
        self._header = None
        self.discriminator = None

        if result_content is not None:
            self.result_content = result_content
        if status_code is not None:
            self.status_code = status_code
        if header is not None:
            self.header = header

    @property
    def result_content(self):
        """Gets the result_content of this ApiPolicyMockBase.

        返回结果

        :return: The result_content of this ApiPolicyMockBase.
        :rtype: str
        """
        return self._result_content

    @result_content.setter
    def result_content(self, result_content):
        """Sets the result_content of this ApiPolicyMockBase.

        返回结果

        :param result_content: The result_content of this ApiPolicyMockBase.
        :type result_content: str
        """
        self._result_content = result_content

    @property
    def status_code(self):
        """Gets the status_code of this ApiPolicyMockBase.

        mock后端自定义状态码： \"200\": \"OK\", \"201\": \"Created\", \"202\": \"Accepted\", \"203\": \"NonAuthoritativeInformation\", \"204\": \"NoContent\", \"205\": \"ResetContent\", \"206\": \"PartialContent\", \"300\": \"MultipleChoices\", \"301\": \"MovedPermanently\", \"302\": \"Found\", \"303\": \"SeeOther\", \"304\": \"NotModified\", \"305\": \"UseProxy\", \"306\": \"Unused\", \"307\": \"TemporaryRedirect\", \"400\": \"BadRequest\", \"401\": \"Unauthorized\", \"402\": \"PaymentRequired\", \"403\": \"Forbidden\", \"404\": \"NotFound\", \"405\": \"MethodNotAllowed\", \"406\": \"NotAcceptable\", \"407\": \"ProxyAuthenticationRequired\", \"408\": \"RequestTimeout\", \"409\": \"Conflict\", \"410\": \"Gone\", \"411\": \"LengthRequired\", \"412\": \"PreconditionFailed\", \"413\": \"RequestEntityTooLarge\", \"414\": \"RequestURITooLong\", \"415\": \"UnsupportedMediaType\", \"416\": \"RequestedRangeNotSatisfiable\", \"417\": \"ExpectationFailed\", \"450\": \"ParameterRequried\", \"451\": \"MethodConnectException\", \"500\": \"InternalServerError\", \"501\": \"NotImplemented\", \"502\": \"BadGateway\", \"503\": \"ServiceUnavailable\", \"504\": \"GatewayTimeout\", \"505\": \"HTTPVersionNotSupported\",

        :return: The status_code of this ApiPolicyMockBase.
        :rtype: int
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code):
        """Sets the status_code of this ApiPolicyMockBase.

        mock后端自定义状态码： \"200\": \"OK\", \"201\": \"Created\", \"202\": \"Accepted\", \"203\": \"NonAuthoritativeInformation\", \"204\": \"NoContent\", \"205\": \"ResetContent\", \"206\": \"PartialContent\", \"300\": \"MultipleChoices\", \"301\": \"MovedPermanently\", \"302\": \"Found\", \"303\": \"SeeOther\", \"304\": \"NotModified\", \"305\": \"UseProxy\", \"306\": \"Unused\", \"307\": \"TemporaryRedirect\", \"400\": \"BadRequest\", \"401\": \"Unauthorized\", \"402\": \"PaymentRequired\", \"403\": \"Forbidden\", \"404\": \"NotFound\", \"405\": \"MethodNotAllowed\", \"406\": \"NotAcceptable\", \"407\": \"ProxyAuthenticationRequired\", \"408\": \"RequestTimeout\", \"409\": \"Conflict\", \"410\": \"Gone\", \"411\": \"LengthRequired\", \"412\": \"PreconditionFailed\", \"413\": \"RequestEntityTooLarge\", \"414\": \"RequestURITooLong\", \"415\": \"UnsupportedMediaType\", \"416\": \"RequestedRangeNotSatisfiable\", \"417\": \"ExpectationFailed\", \"450\": \"ParameterRequried\", \"451\": \"MethodConnectException\", \"500\": \"InternalServerError\", \"501\": \"NotImplemented\", \"502\": \"BadGateway\", \"503\": \"ServiceUnavailable\", \"504\": \"GatewayTimeout\", \"505\": \"HTTPVersionNotSupported\",

        :param status_code: The status_code of this ApiPolicyMockBase.
        :type status_code: int
        """
        self._status_code = status_code

    @property
    def header(self):
        """Gets the header of this ApiPolicyMockBase.

        mock后端自定义响应头header  格式：[{\"key\":\"\",\"value\": \"\", \"remark:\"\"}, {\"key2\":\"\",\"value2\": \"\",\"remark2:\"\"}]  参数说明：  key：mock后端自定义响应头header key, 支持英文，数字，中划线，且只能以英文字母或数字开头，1 ~ 64字符  value： mock后端自定义响应头header value，中文字符必须为UTF-8或者unicode编码, 不能为空，最大长度为10240  remark：mock后端自定义响应头header remark，中文字符必须为UTF-8 或者unicode编码，可以为空，最大长度为2048

        :return: The header of this ApiPolicyMockBase.
        :rtype: str
        """
        return self._header

    @header.setter
    def header(self, header):
        """Sets the header of this ApiPolicyMockBase.

        mock后端自定义响应头header  格式：[{\"key\":\"\",\"value\": \"\", \"remark:\"\"}, {\"key2\":\"\",\"value2\": \"\",\"remark2:\"\"}]  参数说明：  key：mock后端自定义响应头header key, 支持英文，数字，中划线，且只能以英文字母或数字开头，1 ~ 64字符  value： mock后端自定义响应头header value，中文字符必须为UTF-8或者unicode编码, 不能为空，最大长度为10240  remark：mock后端自定义响应头header remark，中文字符必须为UTF-8 或者unicode编码，可以为空，最大长度为2048

        :param header: The header of this ApiPolicyMockBase.
        :type header: str
        """
        self._header = header

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
        if not isinstance(other, ApiPolicyMockBase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
