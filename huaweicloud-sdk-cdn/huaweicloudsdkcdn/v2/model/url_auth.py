# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UrlAuth:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'str',
        'type': 'str',
        'expire_time': 'int',
        'sign_method': 'str',
        'match_type': 'str',
        'inherit_config': 'InheritConfig',
        'key': 'str',
        'backup_key': 'str',
        'sign_arg': 'str',
        'time_format': 'str'
    }

    attribute_map = {
        'status': 'status',
        'type': 'type',
        'expire_time': 'expire_time',
        'sign_method': 'sign_method',
        'match_type': 'match_type',
        'inherit_config': 'inherit_config',
        'key': 'key',
        'backup_key': 'backup_key',
        'sign_arg': 'sign_arg',
        'time_format': 'time_format'
    }

    def __init__(self, status=None, type=None, expire_time=None, sign_method=None, match_type=None, inherit_config=None, key=None, backup_key=None, sign_arg=None, time_format=None):
        """UrlAuth

        The model defined in huaweicloud sdk

        :param status: 是否开启URL鉴权，on：开启,off：关闭。
        :type status: str
        :param type: 鉴权方式 type_a：鉴权方式A type_b：鉴权方式B type_c1：鉴权方式C1 type_c2：鉴权方式C2
        :type type: str
        :param expire_time: 过期时间：范围：0-31536000单位为秒。
        :type expire_time: int
        :param sign_method: 加密的算法 可选择md5或sha256。
        :type sign_method: str
        :param match_type: 鉴权范围，目前仅支持配置所有文件参与鉴权，all：所有文件。
        :type match_type: str
        :param inherit_config: 
        :type inherit_config: :class:`huaweicloudsdkcdn.v2.InheritConfig`
        :param key: 鉴权KEY 由6-32位大小写字母、数字构成。
        :type key: str
        :param backup_key: 鉴权KEY（备） 由6-32位大小写字母、数字构成。
        :type backup_key: str
        :param sign_arg: 鉴权参数：1-100位可以由大小写字母、数字、下划线构成（不能以数字开头）。
        :type sign_arg: str
        :param time_format: 时间格式 dec：十进制 hex：十六进制 鉴权方式A：只支持十进制 鉴权方式B：只支持十进制 鉴权方式C1：只支持十六进制鉴权方式 鉴权方式C2：支持十进制/十六进制
        :type time_format: str
        """
        
        

        self._status = None
        self._type = None
        self._expire_time = None
        self._sign_method = None
        self._match_type = None
        self._inherit_config = None
        self._key = None
        self._backup_key = None
        self._sign_arg = None
        self._time_format = None
        self.discriminator = None

        self.status = status
        self.type = type
        self.expire_time = expire_time
        if sign_method is not None:
            self.sign_method = sign_method
        if match_type is not None:
            self.match_type = match_type
        if inherit_config is not None:
            self.inherit_config = inherit_config
        if key is not None:
            self.key = key
        if backup_key is not None:
            self.backup_key = backup_key
        if sign_arg is not None:
            self.sign_arg = sign_arg
        self.time_format = time_format

    @property
    def status(self):
        """Gets the status of this UrlAuth.

        是否开启URL鉴权，on：开启,off：关闭。

        :return: The status of this UrlAuth.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this UrlAuth.

        是否开启URL鉴权，on：开启,off：关闭。

        :param status: The status of this UrlAuth.
        :type status: str
        """
        self._status = status

    @property
    def type(self):
        """Gets the type of this UrlAuth.

        鉴权方式 type_a：鉴权方式A type_b：鉴权方式B type_c1：鉴权方式C1 type_c2：鉴权方式C2

        :return: The type of this UrlAuth.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this UrlAuth.

        鉴权方式 type_a：鉴权方式A type_b：鉴权方式B type_c1：鉴权方式C1 type_c2：鉴权方式C2

        :param type: The type of this UrlAuth.
        :type type: str
        """
        self._type = type

    @property
    def expire_time(self):
        """Gets the expire_time of this UrlAuth.

        过期时间：范围：0-31536000单位为秒。

        :return: The expire_time of this UrlAuth.
        :rtype: int
        """
        return self._expire_time

    @expire_time.setter
    def expire_time(self, expire_time):
        """Sets the expire_time of this UrlAuth.

        过期时间：范围：0-31536000单位为秒。

        :param expire_time: The expire_time of this UrlAuth.
        :type expire_time: int
        """
        self._expire_time = expire_time

    @property
    def sign_method(self):
        """Gets the sign_method of this UrlAuth.

        加密的算法 可选择md5或sha256。

        :return: The sign_method of this UrlAuth.
        :rtype: str
        """
        return self._sign_method

    @sign_method.setter
    def sign_method(self, sign_method):
        """Sets the sign_method of this UrlAuth.

        加密的算法 可选择md5或sha256。

        :param sign_method: The sign_method of this UrlAuth.
        :type sign_method: str
        """
        self._sign_method = sign_method

    @property
    def match_type(self):
        """Gets the match_type of this UrlAuth.

        鉴权范围，目前仅支持配置所有文件参与鉴权，all：所有文件。

        :return: The match_type of this UrlAuth.
        :rtype: str
        """
        return self._match_type

    @match_type.setter
    def match_type(self, match_type):
        """Sets the match_type of this UrlAuth.

        鉴权范围，目前仅支持配置所有文件参与鉴权，all：所有文件。

        :param match_type: The match_type of this UrlAuth.
        :type match_type: str
        """
        self._match_type = match_type

    @property
    def inherit_config(self):
        """Gets the inherit_config of this UrlAuth.

        :return: The inherit_config of this UrlAuth.
        :rtype: :class:`huaweicloudsdkcdn.v2.InheritConfig`
        """
        return self._inherit_config

    @inherit_config.setter
    def inherit_config(self, inherit_config):
        """Sets the inherit_config of this UrlAuth.

        :param inherit_config: The inherit_config of this UrlAuth.
        :type inherit_config: :class:`huaweicloudsdkcdn.v2.InheritConfig`
        """
        self._inherit_config = inherit_config

    @property
    def key(self):
        """Gets the key of this UrlAuth.

        鉴权KEY 由6-32位大小写字母、数字构成。

        :return: The key of this UrlAuth.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this UrlAuth.

        鉴权KEY 由6-32位大小写字母、数字构成。

        :param key: The key of this UrlAuth.
        :type key: str
        """
        self._key = key

    @property
    def backup_key(self):
        """Gets the backup_key of this UrlAuth.

        鉴权KEY（备） 由6-32位大小写字母、数字构成。

        :return: The backup_key of this UrlAuth.
        :rtype: str
        """
        return self._backup_key

    @backup_key.setter
    def backup_key(self, backup_key):
        """Sets the backup_key of this UrlAuth.

        鉴权KEY（备） 由6-32位大小写字母、数字构成。

        :param backup_key: The backup_key of this UrlAuth.
        :type backup_key: str
        """
        self._backup_key = backup_key

    @property
    def sign_arg(self):
        """Gets the sign_arg of this UrlAuth.

        鉴权参数：1-100位可以由大小写字母、数字、下划线构成（不能以数字开头）。

        :return: The sign_arg of this UrlAuth.
        :rtype: str
        """
        return self._sign_arg

    @sign_arg.setter
    def sign_arg(self, sign_arg):
        """Sets the sign_arg of this UrlAuth.

        鉴权参数：1-100位可以由大小写字母、数字、下划线构成（不能以数字开头）。

        :param sign_arg: The sign_arg of this UrlAuth.
        :type sign_arg: str
        """
        self._sign_arg = sign_arg

    @property
    def time_format(self):
        """Gets the time_format of this UrlAuth.

        时间格式 dec：十进制 hex：十六进制 鉴权方式A：只支持十进制 鉴权方式B：只支持十进制 鉴权方式C1：只支持十六进制鉴权方式 鉴权方式C2：支持十进制/十六进制

        :return: The time_format of this UrlAuth.
        :rtype: str
        """
        return self._time_format

    @time_format.setter
    def time_format(self, time_format):
        """Sets the time_format of this UrlAuth.

        时间格式 dec：十进制 hex：十六进制 鉴权方式A：只支持十进制 鉴权方式B：只支持十进制 鉴权方式C1：只支持十六进制鉴权方式 鉴权方式C2：支持十进制/十六进制

        :param time_format: The time_format of this UrlAuth.
        :type time_format: str
        """
        self._time_format = time_format

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
        if not isinstance(other, UrlAuth):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
