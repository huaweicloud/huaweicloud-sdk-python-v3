# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApiDebugInfo:

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
        'header': 'dict(str, str)',
        'method': 'str',
        'mode': 'str',
        'path': 'str',
        'query': 'dict(str, str)',
        'scheme': 'str',
        'app_key': 'str',
        'app_secret': 'str',
        'domain': 'str',
        'stage': 'str'
    }

    attribute_map = {
        'body': 'body',
        'header': 'header',
        'method': 'method',
        'mode': 'mode',
        'path': 'path',
        'query': 'query',
        'scheme': 'scheme',
        'app_key': 'app_key',
        'app_secret': 'app_secret',
        'domain': 'domain',
        'stage': 'stage'
    }

    def __init__(self, body=None, header=None, method=None, mode=None, path=None, query=None, scheme=None, app_key=None, app_secret=None, domain=None, stage=None):
        """ApiDebugInfo

        The model defined in huaweicloud sdk

        :param body: 请求消息体，最长2097152字节
        :type body: str
        :param header: 头域参数，每个参数值为字符串数组，每个参数名称有如下约束： - 英文字母、数字、点、中连线组成 - 必须以英文字母开头，最长32字节 - 不支持以\&quot;X-Apig-\&quot;或\&quot;X-Sdk-\&quot;开头，不区分大小写 - 不支持取值为\&quot;X-Stage\&quot;，不区分大小写 - mode为MARKET或CONSUMER时，不支持取值为\&quot;X-Auth-Token\&quot;和\&quot;Authorization\&quot;，不区分大小写 &gt; 头域名称在使用前会被规范化，如：\&quot;x-MY-hEaDer\&quot;会被规范化为\&quot;X-My-Header\&quot;
        :type header: dict(str, str)
        :param method: API的请求方法
        :type method: str
        :param mode: 调试模式 - DEVELOPER 调试尚未发布的API定义 - MARKET [调试云商店已购买的API](tag:hws)[暂未使用](tag:cmcc,ctc,DT,g42,hk_g42,hk_sbc,hk_tm,hws_eu,hws_ocb,OCB,sbc,tm,hws_hk) - CONSUMER 调试指定运行环境下的API定义 &gt; DEVELOPER模式，接口调用者必须是API拥有者。    [MARKET模式，接口调用者必须是API购买者或拥有者。](tag:hws)    CONSUMER模式，接口调用者必须有API在指定环境上的授权信息或是API拥有者。
        :type mode: str
        :param path: API的请求路径，需以\&quot;/\&quot;开头，最大长度1024 &gt; 须符合路径规范，百分号编码格式可被正确解码
        :type path: str
        :param query: 查询参数，每个参数值为字符串数组，每个参数名称有如下约束： - 英文字母、数字、点、下划线、中连线组成 - 必须以英文字母开头，最长32字节 - 不支持以\&quot;X-Apig-\&quot;或\&quot;X-Sdk-\&quot;开头，不区分大小写 - 不支持取值为\&quot;X-Stage\&quot;，不区分大小写
        :type query: dict(str, str)
        :param scheme: API的请求协议 - HTTP - HTTPS
        :type scheme: str
        :param app_key: 调试请求使用的APP的key
        :type app_key: str
        :param app_secret: 调试请求使用的APP的密钥
        :type app_secret: str
        :param domain: API的访问域名，未提供时根据mode的取值使用如下默认值： - DEVELOPER API分组的子域名 - MARKET [云商店为API分组分配的域名](tag:hws)[暂未使用](tag:cmcc,ctc,DT,g42,hk_g42,hk_sbc,hk_tm,hws_eu,hws_ocb,OCB,sbc,tm,hws_hk) - CONSUMER API分组的子域名
        :type domain: str
        :param stage: 调试请求指定的运行环境，仅在mode为CONSUMER时有效，未提供时有如下默认值: - CONSUMER RELEASE
        :type stage: str
        """
        
        

        self._body = None
        self._header = None
        self._method = None
        self._mode = None
        self._path = None
        self._query = None
        self._scheme = None
        self._app_key = None
        self._app_secret = None
        self._domain = None
        self._stage = None
        self.discriminator = None

        if body is not None:
            self.body = body
        if header is not None:
            self.header = header
        self.method = method
        self.mode = mode
        self.path = path
        if query is not None:
            self.query = query
        self.scheme = scheme
        if app_key is not None:
            self.app_key = app_key
        if app_secret is not None:
            self.app_secret = app_secret
        if domain is not None:
            self.domain = domain
        if stage is not None:
            self.stage = stage

    @property
    def body(self):
        """Gets the body of this ApiDebugInfo.

        请求消息体，最长2097152字节

        :return: The body of this ApiDebugInfo.
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this ApiDebugInfo.

        请求消息体，最长2097152字节

        :param body: The body of this ApiDebugInfo.
        :type body: str
        """
        self._body = body

    @property
    def header(self):
        """Gets the header of this ApiDebugInfo.

        头域参数，每个参数值为字符串数组，每个参数名称有如下约束： - 英文字母、数字、点、中连线组成 - 必须以英文字母开头，最长32字节 - 不支持以\"X-Apig-\"或\"X-Sdk-\"开头，不区分大小写 - 不支持取值为\"X-Stage\"，不区分大小写 - mode为MARKET或CONSUMER时，不支持取值为\"X-Auth-Token\"和\"Authorization\"，不区分大小写 > 头域名称在使用前会被规范化，如：\"x-MY-hEaDer\"会被规范化为\"X-My-Header\"

        :return: The header of this ApiDebugInfo.
        :rtype: dict(str, str)
        """
        return self._header

    @header.setter
    def header(self, header):
        """Sets the header of this ApiDebugInfo.

        头域参数，每个参数值为字符串数组，每个参数名称有如下约束： - 英文字母、数字、点、中连线组成 - 必须以英文字母开头，最长32字节 - 不支持以\"X-Apig-\"或\"X-Sdk-\"开头，不区分大小写 - 不支持取值为\"X-Stage\"，不区分大小写 - mode为MARKET或CONSUMER时，不支持取值为\"X-Auth-Token\"和\"Authorization\"，不区分大小写 > 头域名称在使用前会被规范化，如：\"x-MY-hEaDer\"会被规范化为\"X-My-Header\"

        :param header: The header of this ApiDebugInfo.
        :type header: dict(str, str)
        """
        self._header = header

    @property
    def method(self):
        """Gets the method of this ApiDebugInfo.

        API的请求方法

        :return: The method of this ApiDebugInfo.
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        """Sets the method of this ApiDebugInfo.

        API的请求方法

        :param method: The method of this ApiDebugInfo.
        :type method: str
        """
        self._method = method

    @property
    def mode(self):
        """Gets the mode of this ApiDebugInfo.

        调试模式 - DEVELOPER 调试尚未发布的API定义 - MARKET [调试云商店已购买的API](tag:hws)[暂未使用](tag:cmcc,ctc,DT,g42,hk_g42,hk_sbc,hk_tm,hws_eu,hws_ocb,OCB,sbc,tm,hws_hk) - CONSUMER 调试指定运行环境下的API定义 > DEVELOPER模式，接口调用者必须是API拥有者。    [MARKET模式，接口调用者必须是API购买者或拥有者。](tag:hws)    CONSUMER模式，接口调用者必须有API在指定环境上的授权信息或是API拥有者。

        :return: The mode of this ApiDebugInfo.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this ApiDebugInfo.

        调试模式 - DEVELOPER 调试尚未发布的API定义 - MARKET [调试云商店已购买的API](tag:hws)[暂未使用](tag:cmcc,ctc,DT,g42,hk_g42,hk_sbc,hk_tm,hws_eu,hws_ocb,OCB,sbc,tm,hws_hk) - CONSUMER 调试指定运行环境下的API定义 > DEVELOPER模式，接口调用者必须是API拥有者。    [MARKET模式，接口调用者必须是API购买者或拥有者。](tag:hws)    CONSUMER模式，接口调用者必须有API在指定环境上的授权信息或是API拥有者。

        :param mode: The mode of this ApiDebugInfo.
        :type mode: str
        """
        self._mode = mode

    @property
    def path(self):
        """Gets the path of this ApiDebugInfo.

        API的请求路径，需以\"/\"开头，最大长度1024 > 须符合路径规范，百分号编码格式可被正确解码

        :return: The path of this ApiDebugInfo.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this ApiDebugInfo.

        API的请求路径，需以\"/\"开头，最大长度1024 > 须符合路径规范，百分号编码格式可被正确解码

        :param path: The path of this ApiDebugInfo.
        :type path: str
        """
        self._path = path

    @property
    def query(self):
        """Gets the query of this ApiDebugInfo.

        查询参数，每个参数值为字符串数组，每个参数名称有如下约束： - 英文字母、数字、点、下划线、中连线组成 - 必须以英文字母开头，最长32字节 - 不支持以\"X-Apig-\"或\"X-Sdk-\"开头，不区分大小写 - 不支持取值为\"X-Stage\"，不区分大小写

        :return: The query of this ApiDebugInfo.
        :rtype: dict(str, str)
        """
        return self._query

    @query.setter
    def query(self, query):
        """Sets the query of this ApiDebugInfo.

        查询参数，每个参数值为字符串数组，每个参数名称有如下约束： - 英文字母、数字、点、下划线、中连线组成 - 必须以英文字母开头，最长32字节 - 不支持以\"X-Apig-\"或\"X-Sdk-\"开头，不区分大小写 - 不支持取值为\"X-Stage\"，不区分大小写

        :param query: The query of this ApiDebugInfo.
        :type query: dict(str, str)
        """
        self._query = query

    @property
    def scheme(self):
        """Gets the scheme of this ApiDebugInfo.

        API的请求协议 - HTTP - HTTPS

        :return: The scheme of this ApiDebugInfo.
        :rtype: str
        """
        return self._scheme

    @scheme.setter
    def scheme(self, scheme):
        """Sets the scheme of this ApiDebugInfo.

        API的请求协议 - HTTP - HTTPS

        :param scheme: The scheme of this ApiDebugInfo.
        :type scheme: str
        """
        self._scheme = scheme

    @property
    def app_key(self):
        """Gets the app_key of this ApiDebugInfo.

        调试请求使用的APP的key

        :return: The app_key of this ApiDebugInfo.
        :rtype: str
        """
        return self._app_key

    @app_key.setter
    def app_key(self, app_key):
        """Sets the app_key of this ApiDebugInfo.

        调试请求使用的APP的key

        :param app_key: The app_key of this ApiDebugInfo.
        :type app_key: str
        """
        self._app_key = app_key

    @property
    def app_secret(self):
        """Gets the app_secret of this ApiDebugInfo.

        调试请求使用的APP的密钥

        :return: The app_secret of this ApiDebugInfo.
        :rtype: str
        """
        return self._app_secret

    @app_secret.setter
    def app_secret(self, app_secret):
        """Sets the app_secret of this ApiDebugInfo.

        调试请求使用的APP的密钥

        :param app_secret: The app_secret of this ApiDebugInfo.
        :type app_secret: str
        """
        self._app_secret = app_secret

    @property
    def domain(self):
        """Gets the domain of this ApiDebugInfo.

        API的访问域名，未提供时根据mode的取值使用如下默认值： - DEVELOPER API分组的子域名 - MARKET [云商店为API分组分配的域名](tag:hws)[暂未使用](tag:cmcc,ctc,DT,g42,hk_g42,hk_sbc,hk_tm,hws_eu,hws_ocb,OCB,sbc,tm,hws_hk) - CONSUMER API分组的子域名

        :return: The domain of this ApiDebugInfo.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this ApiDebugInfo.

        API的访问域名，未提供时根据mode的取值使用如下默认值： - DEVELOPER API分组的子域名 - MARKET [云商店为API分组分配的域名](tag:hws)[暂未使用](tag:cmcc,ctc,DT,g42,hk_g42,hk_sbc,hk_tm,hws_eu,hws_ocb,OCB,sbc,tm,hws_hk) - CONSUMER API分组的子域名

        :param domain: The domain of this ApiDebugInfo.
        :type domain: str
        """
        self._domain = domain

    @property
    def stage(self):
        """Gets the stage of this ApiDebugInfo.

        调试请求指定的运行环境，仅在mode为CONSUMER时有效，未提供时有如下默认值: - CONSUMER RELEASE

        :return: The stage of this ApiDebugInfo.
        :rtype: str
        """
        return self._stage

    @stage.setter
    def stage(self, stage):
        """Sets the stage of this ApiDebugInfo.

        调试请求指定的运行环境，仅在mode为CONSUMER时有效，未提供时有如下默认值: - CONSUMER RELEASE

        :param stage: The stage of this ApiDebugInfo.
        :type stage: str
        """
        self._stage = stage

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
        if not isinstance(other, ApiDebugInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
