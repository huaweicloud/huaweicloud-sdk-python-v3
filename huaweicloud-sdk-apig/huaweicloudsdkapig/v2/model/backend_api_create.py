# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BackendApiCreate:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'authorizer_id': 'str',
        'url_domain': 'str',
        'req_protocol': 'str',
        'remark': 'str',
        'req_method': 'str',
        'version': 'str',
        'req_uri': 'str',
        'timeout': 'int',
        'enable_client_ssl': 'bool',
        'retry_count': 'str',
        'vpc_channel_info': 'ApiBackendVpcReq',
        'vpc_channel_status': 'int'
    }

    attribute_map = {
        'authorizer_id': 'authorizer_id',
        'url_domain': 'url_domain',
        'req_protocol': 'req_protocol',
        'remark': 'remark',
        'req_method': 'req_method',
        'version': 'version',
        'req_uri': 'req_uri',
        'timeout': 'timeout',
        'enable_client_ssl': 'enable_client_ssl',
        'retry_count': 'retry_count',
        'vpc_channel_info': 'vpc_channel_info',
        'vpc_channel_status': 'vpc_channel_status'
    }

    def __init__(self, authorizer_id=None, url_domain=None, req_protocol=None, remark=None, req_method=None, version=None, req_uri=None, timeout=None, enable_client_ssl=None, retry_count=None, vpc_channel_info=None, vpc_channel_status=None):
        """BackendApiCreate

        The model defined in huaweicloud sdk

        :param authorizer_id: 后端自定义认证对象的ID
        :type authorizer_id: str
        :param url_domain: 后端服务的地址。   由主机（IP或域名）和端口号组成，总长度不超过255。格式为主机:端口（如：apig.example.com:7443）。如果不写端口，则HTTPS默认端口号为443，HTTP默认端口号为80。   支持环境变量，使用环境变量时，每个变量名的长度为3 ~ 32位的字符串，字符串由英文字母、数字、下划线、中划线组成，且只能以英文开头
        :type url_domain: str
        :param req_protocol: 请求协议，后端类型为GRPC时请求协议可选GRPC、GRPCS
        :type req_protocol: str
        :param remark: 描述。字符长度不超过255 &gt; 中文字符必须为UTF-8或者unicode编码。
        :type remark: str
        :param req_method: 请求方式，后端类型为GRPC时请求方式固定为POST
        :type req_method: str
        :param version: web后端版本，字符长度不超过16
        :type version: str
        :param req_uri: 请求地址。可以包含请求参数，用{}标识，比如/getUserInfo/{userId}，支持 * % - _ . 等特殊字符，总长度不超过512，且满足URI规范。   支持环境变量，使用环境变量时，每个变量名的长度为3 ~ 32位的字符串，字符串由英文字母、数字、中划线、下划线组成，且只能以英文开头。  &gt; 需要服从URI规范。  后端类型为GRPC时请求地址固定为/
        :type req_uri: str
        :param timeout: API网关请求后端服务的超时时间。最大超时时间可通过实例特性backend_timeout配置修改，可修改的上限为600000。  单位：毫秒。
        :type timeout: int
        :param enable_client_ssl: 是否开启双向认证
        :type enable_client_ssl: bool
        :param retry_count: 请求后端服务的重试次数，默认为-1，范围[-1,10]。  当该值为-1时，幂等的接口会重试1次，非幂等的不会重试。POST，PATCH方法为非幂等；GET，HEAD，PUT，OPTIONS和DELETE等方法为幂等的。
        :type retry_count: str
        :param vpc_channel_info: 
        :type vpc_channel_info: :class:`huaweicloudsdkapig.v2.ApiBackendVpcReq`
        :param vpc_channel_status: 是否使用VPC通道 - 1：使用VPC通道 - 2：不使用VPC通道
        :type vpc_channel_status: int
        """
        
        

        self._authorizer_id = None
        self._url_domain = None
        self._req_protocol = None
        self._remark = None
        self._req_method = None
        self._version = None
        self._req_uri = None
        self._timeout = None
        self._enable_client_ssl = None
        self._retry_count = None
        self._vpc_channel_info = None
        self._vpc_channel_status = None
        self.discriminator = None

        if authorizer_id is not None:
            self.authorizer_id = authorizer_id
        if url_domain is not None:
            self.url_domain = url_domain
        self.req_protocol = req_protocol
        if remark is not None:
            self.remark = remark
        self.req_method = req_method
        if version is not None:
            self.version = version
        self.req_uri = req_uri
        self.timeout = timeout
        if enable_client_ssl is not None:
            self.enable_client_ssl = enable_client_ssl
        if retry_count is not None:
            self.retry_count = retry_count
        if vpc_channel_info is not None:
            self.vpc_channel_info = vpc_channel_info
        if vpc_channel_status is not None:
            self.vpc_channel_status = vpc_channel_status

    @property
    def authorizer_id(self):
        """Gets the authorizer_id of this BackendApiCreate.

        后端自定义认证对象的ID

        :return: The authorizer_id of this BackendApiCreate.
        :rtype: str
        """
        return self._authorizer_id

    @authorizer_id.setter
    def authorizer_id(self, authorizer_id):
        """Sets the authorizer_id of this BackendApiCreate.

        后端自定义认证对象的ID

        :param authorizer_id: The authorizer_id of this BackendApiCreate.
        :type authorizer_id: str
        """
        self._authorizer_id = authorizer_id

    @property
    def url_domain(self):
        """Gets the url_domain of this BackendApiCreate.

        后端服务的地址。   由主机（IP或域名）和端口号组成，总长度不超过255。格式为主机:端口（如：apig.example.com:7443）。如果不写端口，则HTTPS默认端口号为443，HTTP默认端口号为80。   支持环境变量，使用环境变量时，每个变量名的长度为3 ~ 32位的字符串，字符串由英文字母、数字、下划线、中划线组成，且只能以英文开头

        :return: The url_domain of this BackendApiCreate.
        :rtype: str
        """
        return self._url_domain

    @url_domain.setter
    def url_domain(self, url_domain):
        """Sets the url_domain of this BackendApiCreate.

        后端服务的地址。   由主机（IP或域名）和端口号组成，总长度不超过255。格式为主机:端口（如：apig.example.com:7443）。如果不写端口，则HTTPS默认端口号为443，HTTP默认端口号为80。   支持环境变量，使用环境变量时，每个变量名的长度为3 ~ 32位的字符串，字符串由英文字母、数字、下划线、中划线组成，且只能以英文开头

        :param url_domain: The url_domain of this BackendApiCreate.
        :type url_domain: str
        """
        self._url_domain = url_domain

    @property
    def req_protocol(self):
        """Gets the req_protocol of this BackendApiCreate.

        请求协议，后端类型为GRPC时请求协议可选GRPC、GRPCS

        :return: The req_protocol of this BackendApiCreate.
        :rtype: str
        """
        return self._req_protocol

    @req_protocol.setter
    def req_protocol(self, req_protocol):
        """Sets the req_protocol of this BackendApiCreate.

        请求协议，后端类型为GRPC时请求协议可选GRPC、GRPCS

        :param req_protocol: The req_protocol of this BackendApiCreate.
        :type req_protocol: str
        """
        self._req_protocol = req_protocol

    @property
    def remark(self):
        """Gets the remark of this BackendApiCreate.

        描述。字符长度不超过255 > 中文字符必须为UTF-8或者unicode编码。

        :return: The remark of this BackendApiCreate.
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        """Sets the remark of this BackendApiCreate.

        描述。字符长度不超过255 > 中文字符必须为UTF-8或者unicode编码。

        :param remark: The remark of this BackendApiCreate.
        :type remark: str
        """
        self._remark = remark

    @property
    def req_method(self):
        """Gets the req_method of this BackendApiCreate.

        请求方式，后端类型为GRPC时请求方式固定为POST

        :return: The req_method of this BackendApiCreate.
        :rtype: str
        """
        return self._req_method

    @req_method.setter
    def req_method(self, req_method):
        """Sets the req_method of this BackendApiCreate.

        请求方式，后端类型为GRPC时请求方式固定为POST

        :param req_method: The req_method of this BackendApiCreate.
        :type req_method: str
        """
        self._req_method = req_method

    @property
    def version(self):
        """Gets the version of this BackendApiCreate.

        web后端版本，字符长度不超过16

        :return: The version of this BackendApiCreate.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this BackendApiCreate.

        web后端版本，字符长度不超过16

        :param version: The version of this BackendApiCreate.
        :type version: str
        """
        self._version = version

    @property
    def req_uri(self):
        """Gets the req_uri of this BackendApiCreate.

        请求地址。可以包含请求参数，用{}标识，比如/getUserInfo/{userId}，支持 * % - _ . 等特殊字符，总长度不超过512，且满足URI规范。   支持环境变量，使用环境变量时，每个变量名的长度为3 ~ 32位的字符串，字符串由英文字母、数字、中划线、下划线组成，且只能以英文开头。  > 需要服从URI规范。  后端类型为GRPC时请求地址固定为/

        :return: The req_uri of this BackendApiCreate.
        :rtype: str
        """
        return self._req_uri

    @req_uri.setter
    def req_uri(self, req_uri):
        """Sets the req_uri of this BackendApiCreate.

        请求地址。可以包含请求参数，用{}标识，比如/getUserInfo/{userId}，支持 * % - _ . 等特殊字符，总长度不超过512，且满足URI规范。   支持环境变量，使用环境变量时，每个变量名的长度为3 ~ 32位的字符串，字符串由英文字母、数字、中划线、下划线组成，且只能以英文开头。  > 需要服从URI规范。  后端类型为GRPC时请求地址固定为/

        :param req_uri: The req_uri of this BackendApiCreate.
        :type req_uri: str
        """
        self._req_uri = req_uri

    @property
    def timeout(self):
        """Gets the timeout of this BackendApiCreate.

        API网关请求后端服务的超时时间。最大超时时间可通过实例特性backend_timeout配置修改，可修改的上限为600000。  单位：毫秒。

        :return: The timeout of this BackendApiCreate.
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """Sets the timeout of this BackendApiCreate.

        API网关请求后端服务的超时时间。最大超时时间可通过实例特性backend_timeout配置修改，可修改的上限为600000。  单位：毫秒。

        :param timeout: The timeout of this BackendApiCreate.
        :type timeout: int
        """
        self._timeout = timeout

    @property
    def enable_client_ssl(self):
        """Gets the enable_client_ssl of this BackendApiCreate.

        是否开启双向认证

        :return: The enable_client_ssl of this BackendApiCreate.
        :rtype: bool
        """
        return self._enable_client_ssl

    @enable_client_ssl.setter
    def enable_client_ssl(self, enable_client_ssl):
        """Sets the enable_client_ssl of this BackendApiCreate.

        是否开启双向认证

        :param enable_client_ssl: The enable_client_ssl of this BackendApiCreate.
        :type enable_client_ssl: bool
        """
        self._enable_client_ssl = enable_client_ssl

    @property
    def retry_count(self):
        """Gets the retry_count of this BackendApiCreate.

        请求后端服务的重试次数，默认为-1，范围[-1,10]。  当该值为-1时，幂等的接口会重试1次，非幂等的不会重试。POST，PATCH方法为非幂等；GET，HEAD，PUT，OPTIONS和DELETE等方法为幂等的。

        :return: The retry_count of this BackendApiCreate.
        :rtype: str
        """
        return self._retry_count

    @retry_count.setter
    def retry_count(self, retry_count):
        """Sets the retry_count of this BackendApiCreate.

        请求后端服务的重试次数，默认为-1，范围[-1,10]。  当该值为-1时，幂等的接口会重试1次，非幂等的不会重试。POST，PATCH方法为非幂等；GET，HEAD，PUT，OPTIONS和DELETE等方法为幂等的。

        :param retry_count: The retry_count of this BackendApiCreate.
        :type retry_count: str
        """
        self._retry_count = retry_count

    @property
    def vpc_channel_info(self):
        """Gets the vpc_channel_info of this BackendApiCreate.

        :return: The vpc_channel_info of this BackendApiCreate.
        :rtype: :class:`huaweicloudsdkapig.v2.ApiBackendVpcReq`
        """
        return self._vpc_channel_info

    @vpc_channel_info.setter
    def vpc_channel_info(self, vpc_channel_info):
        """Sets the vpc_channel_info of this BackendApiCreate.

        :param vpc_channel_info: The vpc_channel_info of this BackendApiCreate.
        :type vpc_channel_info: :class:`huaweicloudsdkapig.v2.ApiBackendVpcReq`
        """
        self._vpc_channel_info = vpc_channel_info

    @property
    def vpc_channel_status(self):
        """Gets the vpc_channel_status of this BackendApiCreate.

        是否使用VPC通道 - 1：使用VPC通道 - 2：不使用VPC通道

        :return: The vpc_channel_status of this BackendApiCreate.
        :rtype: int
        """
        return self._vpc_channel_status

    @vpc_channel_status.setter
    def vpc_channel_status(self, vpc_channel_status):
        """Sets the vpc_channel_status of this BackendApiCreate.

        是否使用VPC通道 - 1：使用VPC通道 - 2：不使用VPC通道

        :param vpc_channel_status: The vpc_channel_status of this BackendApiCreate.
        :type vpc_channel_status: int
        """
        self._vpc_channel_status = vpc_channel_status

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
        if not isinstance(other, BackendApiCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
