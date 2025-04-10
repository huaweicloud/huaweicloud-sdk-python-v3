# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CallBackConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'callback_url': 'str',
        'auth_type': 'str',
        'key': 'str'
    }

    attribute_map = {
        'callback_url': 'callback_url',
        'auth_type': 'auth_type',
        'key': 'key'
    }

    def __init__(self, callback_url=None, auth_type=None, key=None):
        r"""CallBackConfig

        The model defined in huaweicloud sdk

        :param callback_url: 回调URL。  回调请求body为json格式，带参数如下：  result: SUCCEED或FAILED  asset_id: 资产ID  job_id: 任务
        :type callback_url: str
        :param auth_type: 认证类型。 * NONE。URL中自带认证。 * MSS_A。HMACSHA256签名模式，在URL中追加参数:secret,time_stamp。取值方式：secret&#x3D;hmac_sha256(key, URI（callback_url）+ time_stamp)&amp;time_stamp&#x3D;hex(timestamp)
        :type auth_type: str
        :param key: 密钥Key
        :type key: str
        """
        
        

        self._callback_url = None
        self._auth_type = None
        self._key = None
        self.discriminator = None

        self.callback_url = callback_url
        if auth_type is not None:
            self.auth_type = auth_type
        if key is not None:
            self.key = key

    @property
    def callback_url(self):
        r"""Gets the callback_url of this CallBackConfig.

        回调URL。  回调请求body为json格式，带参数如下：  result: SUCCEED或FAILED  asset_id: 资产ID  job_id: 任务

        :return: The callback_url of this CallBackConfig.
        :rtype: str
        """
        return self._callback_url

    @callback_url.setter
    def callback_url(self, callback_url):
        r"""Sets the callback_url of this CallBackConfig.

        回调URL。  回调请求body为json格式，带参数如下：  result: SUCCEED或FAILED  asset_id: 资产ID  job_id: 任务

        :param callback_url: The callback_url of this CallBackConfig.
        :type callback_url: str
        """
        self._callback_url = callback_url

    @property
    def auth_type(self):
        r"""Gets the auth_type of this CallBackConfig.

        认证类型。 * NONE。URL中自带认证。 * MSS_A。HMACSHA256签名模式，在URL中追加参数:secret,time_stamp。取值方式：secret=hmac_sha256(key, URI（callback_url）+ time_stamp)&time_stamp=hex(timestamp)

        :return: The auth_type of this CallBackConfig.
        :rtype: str
        """
        return self._auth_type

    @auth_type.setter
    def auth_type(self, auth_type):
        r"""Sets the auth_type of this CallBackConfig.

        认证类型。 * NONE。URL中自带认证。 * MSS_A。HMACSHA256签名模式，在URL中追加参数:secret,time_stamp。取值方式：secret=hmac_sha256(key, URI（callback_url）+ time_stamp)&time_stamp=hex(timestamp)

        :param auth_type: The auth_type of this CallBackConfig.
        :type auth_type: str
        """
        self._auth_type = auth_type

    @property
    def key(self):
        r"""Gets the key of this CallBackConfig.

        密钥Key

        :return: The key of this CallBackConfig.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        r"""Sets the key of this CallBackConfig.

        密钥Key

        :param key: The key of this CallBackConfig.
        :type key: str
        """
        self._key = key

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
        if not isinstance(other, CallBackConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
