# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Encryption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'key_rotation_interval_seconds': 'int',
        'encryption_method': 'str',
        'level': 'str',
        'resource_id': 'str',
        'system_ids': 'list[str]',
        'url': 'str',
        'speke_version': 'str',
        'request_mode': 'str',
        'http_headers': 'list[HttpHeader]',
        'urn': 'str'
    }

    attribute_map = {
        'key_rotation_interval_seconds': 'key_rotation_interval_seconds',
        'encryption_method': 'encryption_method',
        'level': 'level',
        'resource_id': 'resource_id',
        'system_ids': 'system_ids',
        'url': 'url',
        'speke_version': 'speke_version',
        'request_mode': 'request_mode',
        'http_headers': 'http_headers',
        'urn': 'urn'
    }

    def __init__(self, key_rotation_interval_seconds=None, encryption_method=None, level=None, resource_id=None, system_ids=None, url=None, speke_version=None, request_mode=None, http_headers=None, urn=None):
        r"""Encryption

        The model defined in huaweicloud sdk

        :param key_rotation_interval_seconds: 密钥缓存时间。如果密钥不变，默认缓存七天。  请注意：目前为保留字段，不支持配置。 
        :type key_rotation_interval_seconds: int
        :param encryption_method: 加密方式。  请注意：目前为保留字段，不支持配置。 
        :type encryption_method: str
        :param level: 取值如下： - content：一个频道对应一个密钥 - profile：一个码率对应一个密钥  默认值：content
        :type level: str
        :param resource_id: 客户生成的DRM内容ID
        :type resource_id: str
        :param system_ids: system_id枚举值。  取值如下： * HLS：FairPlay * DASH：Widevine、PlayReady * MSS：PlayReady 
        :type system_ids: list[str]
        :param url: 获取密钥的DRM地址
        :type url: str
        :param speke_version: drm speke 版本号 当前只支持1.0
        :type speke_version: str
        :param request_mode: 请求模式。  取值如下： * direct_http：HTTP(S)直接访问DRM。 * functiongraph_proxy：FunctionGraph代理访问DRM。 
        :type request_mode: str
        :param http_headers: 需要添加在drm请求头中的鉴权信息。最多支持配置5个。  仅direct_http请求模式支持配置http_headers。 
        :type http_headers: list[:class:`huaweicloudsdklive.v1.HttpHeader`]
        :param urn: functiongraph_proxy请求模式需要提供functiongraph的urn。
        :type urn: str
        """
        
        

        self._key_rotation_interval_seconds = None
        self._encryption_method = None
        self._level = None
        self._resource_id = None
        self._system_ids = None
        self._url = None
        self._speke_version = None
        self._request_mode = None
        self._http_headers = None
        self._urn = None
        self.discriminator = None

        if key_rotation_interval_seconds is not None:
            self.key_rotation_interval_seconds = key_rotation_interval_seconds
        if encryption_method is not None:
            self.encryption_method = encryption_method
        if level is not None:
            self.level = level
        self.resource_id = resource_id
        self.system_ids = system_ids
        self.url = url
        self.speke_version = speke_version
        self.request_mode = request_mode
        if http_headers is not None:
            self.http_headers = http_headers
        if urn is not None:
            self.urn = urn

    @property
    def key_rotation_interval_seconds(self):
        r"""Gets the key_rotation_interval_seconds of this Encryption.

        密钥缓存时间。如果密钥不变，默认缓存七天。  请注意：目前为保留字段，不支持配置。 

        :return: The key_rotation_interval_seconds of this Encryption.
        :rtype: int
        """
        return self._key_rotation_interval_seconds

    @key_rotation_interval_seconds.setter
    def key_rotation_interval_seconds(self, key_rotation_interval_seconds):
        r"""Sets the key_rotation_interval_seconds of this Encryption.

        密钥缓存时间。如果密钥不变，默认缓存七天。  请注意：目前为保留字段，不支持配置。 

        :param key_rotation_interval_seconds: The key_rotation_interval_seconds of this Encryption.
        :type key_rotation_interval_seconds: int
        """
        self._key_rotation_interval_seconds = key_rotation_interval_seconds

    @property
    def encryption_method(self):
        r"""Gets the encryption_method of this Encryption.

        加密方式。  请注意：目前为保留字段，不支持配置。 

        :return: The encryption_method of this Encryption.
        :rtype: str
        """
        return self._encryption_method

    @encryption_method.setter
    def encryption_method(self, encryption_method):
        r"""Sets the encryption_method of this Encryption.

        加密方式。  请注意：目前为保留字段，不支持配置。 

        :param encryption_method: The encryption_method of this Encryption.
        :type encryption_method: str
        """
        self._encryption_method = encryption_method

    @property
    def level(self):
        r"""Gets the level of this Encryption.

        取值如下： - content：一个频道对应一个密钥 - profile：一个码率对应一个密钥  默认值：content

        :return: The level of this Encryption.
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level):
        r"""Sets the level of this Encryption.

        取值如下： - content：一个频道对应一个密钥 - profile：一个码率对应一个密钥  默认值：content

        :param level: The level of this Encryption.
        :type level: str
        """
        self._level = level

    @property
    def resource_id(self):
        r"""Gets the resource_id of this Encryption.

        客户生成的DRM内容ID

        :return: The resource_id of this Encryption.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this Encryption.

        客户生成的DRM内容ID

        :param resource_id: The resource_id of this Encryption.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def system_ids(self):
        r"""Gets the system_ids of this Encryption.

        system_id枚举值。  取值如下： * HLS：FairPlay * DASH：Widevine、PlayReady * MSS：PlayReady 

        :return: The system_ids of this Encryption.
        :rtype: list[str]
        """
        return self._system_ids

    @system_ids.setter
    def system_ids(self, system_ids):
        r"""Sets the system_ids of this Encryption.

        system_id枚举值。  取值如下： * HLS：FairPlay * DASH：Widevine、PlayReady * MSS：PlayReady 

        :param system_ids: The system_ids of this Encryption.
        :type system_ids: list[str]
        """
        self._system_ids = system_ids

    @property
    def url(self):
        r"""Gets the url of this Encryption.

        获取密钥的DRM地址

        :return: The url of this Encryption.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this Encryption.

        获取密钥的DRM地址

        :param url: The url of this Encryption.
        :type url: str
        """
        self._url = url

    @property
    def speke_version(self):
        r"""Gets the speke_version of this Encryption.

        drm speke 版本号 当前只支持1.0

        :return: The speke_version of this Encryption.
        :rtype: str
        """
        return self._speke_version

    @speke_version.setter
    def speke_version(self, speke_version):
        r"""Sets the speke_version of this Encryption.

        drm speke 版本号 当前只支持1.0

        :param speke_version: The speke_version of this Encryption.
        :type speke_version: str
        """
        self._speke_version = speke_version

    @property
    def request_mode(self):
        r"""Gets the request_mode of this Encryption.

        请求模式。  取值如下： * direct_http：HTTP(S)直接访问DRM。 * functiongraph_proxy：FunctionGraph代理访问DRM。 

        :return: The request_mode of this Encryption.
        :rtype: str
        """
        return self._request_mode

    @request_mode.setter
    def request_mode(self, request_mode):
        r"""Sets the request_mode of this Encryption.

        请求模式。  取值如下： * direct_http：HTTP(S)直接访问DRM。 * functiongraph_proxy：FunctionGraph代理访问DRM。 

        :param request_mode: The request_mode of this Encryption.
        :type request_mode: str
        """
        self._request_mode = request_mode

    @property
    def http_headers(self):
        r"""Gets the http_headers of this Encryption.

        需要添加在drm请求头中的鉴权信息。最多支持配置5个。  仅direct_http请求模式支持配置http_headers。 

        :return: The http_headers of this Encryption.
        :rtype: list[:class:`huaweicloudsdklive.v1.HttpHeader`]
        """
        return self._http_headers

    @http_headers.setter
    def http_headers(self, http_headers):
        r"""Sets the http_headers of this Encryption.

        需要添加在drm请求头中的鉴权信息。最多支持配置5个。  仅direct_http请求模式支持配置http_headers。 

        :param http_headers: The http_headers of this Encryption.
        :type http_headers: list[:class:`huaweicloudsdklive.v1.HttpHeader`]
        """
        self._http_headers = http_headers

    @property
    def urn(self):
        r"""Gets the urn of this Encryption.

        functiongraph_proxy请求模式需要提供functiongraph的urn。

        :return: The urn of this Encryption.
        :rtype: str
        """
        return self._urn

    @urn.setter
    def urn(self, urn):
        r"""Sets the urn of this Encryption.

        functiongraph_proxy请求模式需要提供functiongraph的urn。

        :param urn: The urn of this Encryption.
        :type urn: str
        """
        self._urn = urn

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
        if not isinstance(other, Encryption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
