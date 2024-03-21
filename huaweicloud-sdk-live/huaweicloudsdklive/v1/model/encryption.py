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
        'drm_content_id': 'str',
        'system_ids': 'list[str]',
        'auth_info': 'str',
        'km_url': 'str'
    }

    attribute_map = {
        'key_rotation_interval_seconds': 'key_rotation_interval_seconds',
        'encryption_method': 'encryption_method',
        'level': 'level',
        'drm_content_id': 'drm_content_id',
        'system_ids': 'system_ids',
        'auth_info': 'auth_info',
        'km_url': 'km_url'
    }

    def __init__(self, key_rotation_interval_seconds=None, encryption_method=None, level=None, drm_content_id=None, system_ids=None, auth_info=None, km_url=None):
        """Encryption

        The model defined in huaweicloud sdk

        :param key_rotation_interval_seconds: 密钥缓存时间。如果密钥不变，默认缓存七天
        :type key_rotation_interval_seconds: int
        :param encryption_method: 加密方式
        :type encryption_method: str
        :param level: 取值如下： - content：一个频道对应一个密钥 - profile：一个码率对应一个密钥  默认值：content
        :type level: str
        :param drm_content_id: 客户生成的DRM内容ID
        :type drm_content_id: str
        :param system_ids: system_id枚举值
        :type system_ids: list[str]
        :param auth_info: 增加到请求消息体header中的鉴权信息
        :type auth_info: str
        :param km_url: 获取密钥的DRM地址
        :type km_url: str
        """
        
        

        self._key_rotation_interval_seconds = None
        self._encryption_method = None
        self._level = None
        self._drm_content_id = None
        self._system_ids = None
        self._auth_info = None
        self._km_url = None
        self.discriminator = None

        if key_rotation_interval_seconds is not None:
            self.key_rotation_interval_seconds = key_rotation_interval_seconds
        if encryption_method is not None:
            self.encryption_method = encryption_method
        if level is not None:
            self.level = level
        self.drm_content_id = drm_content_id
        self.system_ids = system_ids
        self.auth_info = auth_info
        self.km_url = km_url

    @property
    def key_rotation_interval_seconds(self):
        """Gets the key_rotation_interval_seconds of this Encryption.

        密钥缓存时间。如果密钥不变，默认缓存七天

        :return: The key_rotation_interval_seconds of this Encryption.
        :rtype: int
        """
        return self._key_rotation_interval_seconds

    @key_rotation_interval_seconds.setter
    def key_rotation_interval_seconds(self, key_rotation_interval_seconds):
        """Sets the key_rotation_interval_seconds of this Encryption.

        密钥缓存时间。如果密钥不变，默认缓存七天

        :param key_rotation_interval_seconds: The key_rotation_interval_seconds of this Encryption.
        :type key_rotation_interval_seconds: int
        """
        self._key_rotation_interval_seconds = key_rotation_interval_seconds

    @property
    def encryption_method(self):
        """Gets the encryption_method of this Encryption.

        加密方式

        :return: The encryption_method of this Encryption.
        :rtype: str
        """
        return self._encryption_method

    @encryption_method.setter
    def encryption_method(self, encryption_method):
        """Sets the encryption_method of this Encryption.

        加密方式

        :param encryption_method: The encryption_method of this Encryption.
        :type encryption_method: str
        """
        self._encryption_method = encryption_method

    @property
    def level(self):
        """Gets the level of this Encryption.

        取值如下： - content：一个频道对应一个密钥 - profile：一个码率对应一个密钥  默认值：content

        :return: The level of this Encryption.
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level):
        """Sets the level of this Encryption.

        取值如下： - content：一个频道对应一个密钥 - profile：一个码率对应一个密钥  默认值：content

        :param level: The level of this Encryption.
        :type level: str
        """
        self._level = level

    @property
    def drm_content_id(self):
        """Gets the drm_content_id of this Encryption.

        客户生成的DRM内容ID

        :return: The drm_content_id of this Encryption.
        :rtype: str
        """
        return self._drm_content_id

    @drm_content_id.setter
    def drm_content_id(self, drm_content_id):
        """Sets the drm_content_id of this Encryption.

        客户生成的DRM内容ID

        :param drm_content_id: The drm_content_id of this Encryption.
        :type drm_content_id: str
        """
        self._drm_content_id = drm_content_id

    @property
    def system_ids(self):
        """Gets the system_ids of this Encryption.

        system_id枚举值

        :return: The system_ids of this Encryption.
        :rtype: list[str]
        """
        return self._system_ids

    @system_ids.setter
    def system_ids(self, system_ids):
        """Sets the system_ids of this Encryption.

        system_id枚举值

        :param system_ids: The system_ids of this Encryption.
        :type system_ids: list[str]
        """
        self._system_ids = system_ids

    @property
    def auth_info(self):
        """Gets the auth_info of this Encryption.

        增加到请求消息体header中的鉴权信息

        :return: The auth_info of this Encryption.
        :rtype: str
        """
        return self._auth_info

    @auth_info.setter
    def auth_info(self, auth_info):
        """Sets the auth_info of this Encryption.

        增加到请求消息体header中的鉴权信息

        :param auth_info: The auth_info of this Encryption.
        :type auth_info: str
        """
        self._auth_info = auth_info

    @property
    def km_url(self):
        """Gets the km_url of this Encryption.

        获取密钥的DRM地址

        :return: The km_url of this Encryption.
        :rtype: str
        """
        return self._km_url

    @km_url.setter
    def km_url(self, km_url):
        """Sets the km_url of this Encryption.

        获取密钥的DRM地址

        :param km_url: The km_url of this Encryption.
        :type km_url: str
        """
        self._km_url = km_url

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
