# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AccessConfigurationHttpPath:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'hostname': 'str',
        'path': 'str',
        'url_match_mode': 'str'
    }

    attribute_map = {
        'hostname': 'hostname',
        'path': 'path',
        'url_match_mode': 'url_match_mode'
    }

    def __init__(self, hostname=None, path=None, url_match_mode=None):
        r"""AccessConfigurationHttpPath

        The model defined in huaweicloud sdk

        :param hostname: 域名/不填，不填时表示使用IP。
        :type hostname: str
        :param path: URL路径。
        :type path: str
        :param url_match_mode: URL路径匹配模式，支持前缀匹配、正则匹配、精准匹配。
        :type url_match_mode: str
        """
        
        

        self._hostname = None
        self._path = None
        self._url_match_mode = None
        self.discriminator = None

        if hostname is not None:
            self.hostname = hostname
        if path is not None:
            self.path = path
        if url_match_mode is not None:
            self.url_match_mode = url_match_mode

    @property
    def hostname(self):
        r"""Gets the hostname of this AccessConfigurationHttpPath.

        域名/不填，不填时表示使用IP。

        :return: The hostname of this AccessConfigurationHttpPath.
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        r"""Sets the hostname of this AccessConfigurationHttpPath.

        域名/不填，不填时表示使用IP。

        :param hostname: The hostname of this AccessConfigurationHttpPath.
        :type hostname: str
        """
        self._hostname = hostname

    @property
    def path(self):
        r"""Gets the path of this AccessConfigurationHttpPath.

        URL路径。

        :return: The path of this AccessConfigurationHttpPath.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        r"""Sets the path of this AccessConfigurationHttpPath.

        URL路径。

        :param path: The path of this AccessConfigurationHttpPath.
        :type path: str
        """
        self._path = path

    @property
    def url_match_mode(self):
        r"""Gets the url_match_mode of this AccessConfigurationHttpPath.

        URL路径匹配模式，支持前缀匹配、正则匹配、精准匹配。

        :return: The url_match_mode of this AccessConfigurationHttpPath.
        :rtype: str
        """
        return self._url_match_mode

    @url_match_mode.setter
    def url_match_mode(self, url_match_mode):
        r"""Sets the url_match_mode of this AccessConfigurationHttpPath.

        URL路径匹配模式，支持前缀匹配、正则匹配、精准匹配。

        :param url_match_mode: The url_match_mode of this AccessConfigurationHttpPath.
        :type url_match_mode: str
        """
        self._url_match_mode = url_match_mode

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
        if not isinstance(other, AccessConfigurationHttpPath):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
