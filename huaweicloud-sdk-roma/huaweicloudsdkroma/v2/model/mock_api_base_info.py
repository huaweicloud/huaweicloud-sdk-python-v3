# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MockApiBaseInfo:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'remark': 'str',
        'result_content': 'str',
        'version': 'str',
        'authorizer_id': 'str',
        'status_code': 'int',
        'header': 'list[MockApiBaseInfoHeader]'
    }

    attribute_map = {
        'remark': 'remark',
        'result_content': 'result_content',
        'version': 'version',
        'authorizer_id': 'authorizer_id',
        'status_code': 'status_code',
        'header': 'header'
    }

    def __init__(self, remark=None, result_content=None, version=None, authorizer_id=None, status_code=None, header=None):
        """MockApiBaseInfo - a model defined in huaweicloud sdk"""
        
        

        self._remark = None
        self._result_content = None
        self._version = None
        self._authorizer_id = None
        self._status_code = None
        self._header = None
        self.discriminator = None

        if remark is not None:
            self.remark = remark
        if result_content is not None:
            self.result_content = result_content
        if version is not None:
            self.version = version
        if authorizer_id is not None:
            self.authorizer_id = authorizer_id
        if status_code is not None:
            self.status_code = status_code
        if header is not None:
            self.header = header

    @property
    def remark(self):
        """Gets the remark of this MockApiBaseInfo.

        描述信息。 > 中文字符必须为UTF-8或者unicode编码。

        :return: The remark of this MockApiBaseInfo.
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        """Sets the remark of this MockApiBaseInfo.

        描述信息。 > 中文字符必须为UTF-8或者unicode编码。

        :param remark: The remark of this MockApiBaseInfo.
        :type: str
        """
        self._remark = remark

    @property
    def result_content(self):
        """Gets the result_content of this MockApiBaseInfo.

        返回结果

        :return: The result_content of this MockApiBaseInfo.
        :rtype: str
        """
        return self._result_content

    @result_content.setter
    def result_content(self, result_content):
        """Sets the result_content of this MockApiBaseInfo.

        返回结果

        :param result_content: The result_content of this MockApiBaseInfo.
        :type: str
        """
        self._result_content = result_content

    @property
    def version(self):
        """Gets the version of this MockApiBaseInfo.

        版本。字符长度不超过64

        :return: The version of this MockApiBaseInfo.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this MockApiBaseInfo.

        版本。字符长度不超过64

        :param version: The version of this MockApiBaseInfo.
        :type: str
        """
        self._version = version

    @property
    def authorizer_id(self):
        """Gets the authorizer_id of this MockApiBaseInfo.

        后端自定义认证ID

        :return: The authorizer_id of this MockApiBaseInfo.
        :rtype: str
        """
        return self._authorizer_id

    @authorizer_id.setter
    def authorizer_id(self, authorizer_id):
        """Sets the authorizer_id of this MockApiBaseInfo.

        后端自定义认证ID

        :param authorizer_id: The authorizer_id of this MockApiBaseInfo.
        :type: str
        """
        self._authorizer_id = authorizer_id

    @property
    def status_code(self):
        """Gets the status_code of this MockApiBaseInfo.

        mock后端自定义状态码： \"200\": \"OK\", \"201\": \"Created\", \"202\": \"Accepted\", \"203\": \"NonAuthoritativeInformation\", \"204\": \"NoContent\", \"205\": \"ResetContent\", \"206\": \"PartialContent\", \"300\": \"MultipleChoices\", \"301\": \"MovedPermanently\", \"302\": \"Found\", \"303\": \"SeeOther\", \"304\": \"NotModified\", \"305\": \"UseProxy\", \"306\": \"Unused\", \"307\": \"TemporaryRedirect\", \"400\": \"BadRequest\", \"401\": \"Unauthorized\", \"402\": \"PaymentRequired\", \"403\": \"Forbidden\", \"404\": \"NotFound\", \"405\": \"MethodNotAllowed\", \"406\": \"NotAcceptable\", \"407\": \"ProxyAuthenticationRequired\", \"408\": \"RequestTimeout\", \"409\": \"Conflict\", \"410\": \"Gone\", \"411\": \"LengthRequired\", \"412\": \"PreconditionFailed\", \"413\": \"RequestEntityTooLarge\", \"414\": \"RequestURITooLong\", \"415\": \"UnsupportedMediaType\", \"416\": \"RequestedRangeNotSatisfiable\", \"417\": \"ExpectationFailed\", \"450\": \"ParameterRequried\", \"451\": \"MethodConnectException\", \"500\": \"InternalServerError\", \"501\": \"NotImplemented\", \"502\": \"BadGateway\", \"503\": \"ServiceUnavailable\", \"504\": \"GatewayTimeout\", \"505\": \"HTTPVersionNotSupported\",

        :return: The status_code of this MockApiBaseInfo.
        :rtype: int
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code):
        """Sets the status_code of this MockApiBaseInfo.

        mock后端自定义状态码： \"200\": \"OK\", \"201\": \"Created\", \"202\": \"Accepted\", \"203\": \"NonAuthoritativeInformation\", \"204\": \"NoContent\", \"205\": \"ResetContent\", \"206\": \"PartialContent\", \"300\": \"MultipleChoices\", \"301\": \"MovedPermanently\", \"302\": \"Found\", \"303\": \"SeeOther\", \"304\": \"NotModified\", \"305\": \"UseProxy\", \"306\": \"Unused\", \"307\": \"TemporaryRedirect\", \"400\": \"BadRequest\", \"401\": \"Unauthorized\", \"402\": \"PaymentRequired\", \"403\": \"Forbidden\", \"404\": \"NotFound\", \"405\": \"MethodNotAllowed\", \"406\": \"NotAcceptable\", \"407\": \"ProxyAuthenticationRequired\", \"408\": \"RequestTimeout\", \"409\": \"Conflict\", \"410\": \"Gone\", \"411\": \"LengthRequired\", \"412\": \"PreconditionFailed\", \"413\": \"RequestEntityTooLarge\", \"414\": \"RequestURITooLong\", \"415\": \"UnsupportedMediaType\", \"416\": \"RequestedRangeNotSatisfiable\", \"417\": \"ExpectationFailed\", \"450\": \"ParameterRequried\", \"451\": \"MethodConnectException\", \"500\": \"InternalServerError\", \"501\": \"NotImplemented\", \"502\": \"BadGateway\", \"503\": \"ServiceUnavailable\", \"504\": \"GatewayTimeout\", \"505\": \"HTTPVersionNotSupported\",

        :param status_code: The status_code of this MockApiBaseInfo.
        :type: int
        """
        self._status_code = status_code

    @property
    def header(self):
        """Gets the header of this MockApiBaseInfo.

        mock后端自定义响应头header

        :return: The header of this MockApiBaseInfo.
        :rtype: list[MockApiBaseInfoHeader]
        """
        return self._header

    @header.setter
    def header(self, header):
        """Sets the header of this MockApiBaseInfo.

        mock后端自定义响应头header

        :param header: The header of this MockApiBaseInfo.
        :type: list[MockApiBaseInfoHeader]
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
        if not isinstance(other, MockApiBaseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
