# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UrlAuthGetBody:

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
        'inherit_config': 'InheritConfigQuery',
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
        """UrlAuthGetBody

        The model defined in huaweicloud sdk

        :param status: 是否开启URL鉴权，on：开启,off：关闭。
        :type status: str
        :param type: 鉴权方式， type_a：鉴权方式A， type_b：鉴权方式B， type_c1：鉴权方式C1， type_c2：鉴权方式C2。
        :type type: str
        :param expire_time: 过期时间，单位：秒。
        :type expire_time: int
        :param sign_method: 加密算法。
        :type sign_method: str
        :param match_type: 鉴权范围。
        :type match_type: str
        :param inherit_config: 
        :type inherit_config: :class:`huaweicloudsdkcdn.v1.InheritConfigQuery`
        :param key: 鉴权KEY。
        :type key: str
        :param backup_key: 鉴权KEY（备）。
        :type backup_key: str
        :param sign_arg: 鉴权参数。
        :type sign_arg: str
        :param time_format: 时间格式， dec：十进制, hex：十六进制。
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
        if type is not None:
            self.type = type
        if expire_time is not None:
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
        if time_format is not None:
            self.time_format = time_format

    @property
    def status(self):
        """Gets the status of this UrlAuthGetBody.

        是否开启URL鉴权，on：开启,off：关闭。

        :return: The status of this UrlAuthGetBody.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this UrlAuthGetBody.

        是否开启URL鉴权，on：开启,off：关闭。

        :param status: The status of this UrlAuthGetBody.
        :type status: str
        """
        self._status = status

    @property
    def type(self):
        """Gets the type of this UrlAuthGetBody.

        鉴权方式， type_a：鉴权方式A， type_b：鉴权方式B， type_c1：鉴权方式C1， type_c2：鉴权方式C2。

        :return: The type of this UrlAuthGetBody.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this UrlAuthGetBody.

        鉴权方式， type_a：鉴权方式A， type_b：鉴权方式B， type_c1：鉴权方式C1， type_c2：鉴权方式C2。

        :param type: The type of this UrlAuthGetBody.
        :type type: str
        """
        self._type = type

    @property
    def expire_time(self):
        """Gets the expire_time of this UrlAuthGetBody.

        过期时间，单位：秒。

        :return: The expire_time of this UrlAuthGetBody.
        :rtype: int
        """
        return self._expire_time

    @expire_time.setter
    def expire_time(self, expire_time):
        """Sets the expire_time of this UrlAuthGetBody.

        过期时间，单位：秒。

        :param expire_time: The expire_time of this UrlAuthGetBody.
        :type expire_time: int
        """
        self._expire_time = expire_time

    @property
    def sign_method(self):
        """Gets the sign_method of this UrlAuthGetBody.

        加密算法。

        :return: The sign_method of this UrlAuthGetBody.
        :rtype: str
        """
        return self._sign_method

    @sign_method.setter
    def sign_method(self, sign_method):
        """Sets the sign_method of this UrlAuthGetBody.

        加密算法。

        :param sign_method: The sign_method of this UrlAuthGetBody.
        :type sign_method: str
        """
        self._sign_method = sign_method

    @property
    def match_type(self):
        """Gets the match_type of this UrlAuthGetBody.

        鉴权范围。

        :return: The match_type of this UrlAuthGetBody.
        :rtype: str
        """
        return self._match_type

    @match_type.setter
    def match_type(self, match_type):
        """Sets the match_type of this UrlAuthGetBody.

        鉴权范围。

        :param match_type: The match_type of this UrlAuthGetBody.
        :type match_type: str
        """
        self._match_type = match_type

    @property
    def inherit_config(self):
        """Gets the inherit_config of this UrlAuthGetBody.

        :return: The inherit_config of this UrlAuthGetBody.
        :rtype: :class:`huaweicloudsdkcdn.v1.InheritConfigQuery`
        """
        return self._inherit_config

    @inherit_config.setter
    def inherit_config(self, inherit_config):
        """Sets the inherit_config of this UrlAuthGetBody.

        :param inherit_config: The inherit_config of this UrlAuthGetBody.
        :type inherit_config: :class:`huaweicloudsdkcdn.v1.InheritConfigQuery`
        """
        self._inherit_config = inherit_config

    @property
    def key(self):
        """Gets the key of this UrlAuthGetBody.

        鉴权KEY。

        :return: The key of this UrlAuthGetBody.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this UrlAuthGetBody.

        鉴权KEY。

        :param key: The key of this UrlAuthGetBody.
        :type key: str
        """
        self._key = key

    @property
    def backup_key(self):
        """Gets the backup_key of this UrlAuthGetBody.

        鉴权KEY（备）。

        :return: The backup_key of this UrlAuthGetBody.
        :rtype: str
        """
        return self._backup_key

    @backup_key.setter
    def backup_key(self, backup_key):
        """Sets the backup_key of this UrlAuthGetBody.

        鉴权KEY（备）。

        :param backup_key: The backup_key of this UrlAuthGetBody.
        :type backup_key: str
        """
        self._backup_key = backup_key

    @property
    def sign_arg(self):
        """Gets the sign_arg of this UrlAuthGetBody.

        鉴权参数。

        :return: The sign_arg of this UrlAuthGetBody.
        :rtype: str
        """
        return self._sign_arg

    @sign_arg.setter
    def sign_arg(self, sign_arg):
        """Sets the sign_arg of this UrlAuthGetBody.

        鉴权参数。

        :param sign_arg: The sign_arg of this UrlAuthGetBody.
        :type sign_arg: str
        """
        self._sign_arg = sign_arg

    @property
    def time_format(self):
        """Gets the time_format of this UrlAuthGetBody.

        时间格式， dec：十进制, hex：十六进制。

        :return: The time_format of this UrlAuthGetBody.
        :rtype: str
        """
        return self._time_format

    @time_format.setter
    def time_format(self, time_format):
        """Sets the time_format of this UrlAuthGetBody.

        时间格式， dec：十进制, hex：十六进制。

        :param time_format: The time_format of this UrlAuthGetBody.
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
        if not isinstance(other, UrlAuthGetBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
