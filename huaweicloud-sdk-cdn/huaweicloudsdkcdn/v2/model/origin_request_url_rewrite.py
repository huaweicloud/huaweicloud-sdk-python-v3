# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OriginRequestUrlRewrite:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'priority': 'int',
        'match_type': 'str',
        'source_url': 'str',
        'target_url': 'str'
    }

    attribute_map = {
        'priority': 'priority',
        'match_type': 'match_type',
        'source_url': 'source_url',
        'target_url': 'target_url'
    }

    def __init__(self, priority=None, match_type=None, source_url=None, target_url=None):
        r"""OriginRequestUrlRewrite

        The model defined in huaweicloud sdk

        :param priority: 回源URL改写规则的优先级。 优先级设置具有唯一性，不支持多条回源URL改写规则设置同一优先级，且优先级不能输入为空。 多条规则下，不同规则中的相同资源内容，CDN按照优先级高的规则执行URL改写。 取值为1-100之间的整数，数值越大优先级越高。
        :type priority: int
        :param match_type: 匹配类型， all：所有文件， file_path：URL路径， wildcard：通配符， full_path: 全路径。
        :type match_type: str
        :param source_url: 需要替换的URI。 改写后的URI以正斜线（/）开头的URI，不含http(s)://头及域名。 长度不超过512个字符。 支持通配符\\*匹配，如：/test/\\*/\\*.mp4。 匹配方式为“所有文件”时，不支持配置参数。
        :type source_url: str
        :param target_url: 以正斜线（/）开头的URI，不含http(s)://头及域名。 长度不超过256个字符。 通配符 * 可通过$n捕获（n&#x3D;1,2,3...，例如：/newtest/$1/$2.jpg）。
        :type target_url: str
        """
        
        

        self._priority = None
        self._match_type = None
        self._source_url = None
        self._target_url = None
        self.discriminator = None

        self.priority = priority
        self.match_type = match_type
        if source_url is not None:
            self.source_url = source_url
        self.target_url = target_url

    @property
    def priority(self):
        r"""Gets the priority of this OriginRequestUrlRewrite.

        回源URL改写规则的优先级。 优先级设置具有唯一性，不支持多条回源URL改写规则设置同一优先级，且优先级不能输入为空。 多条规则下，不同规则中的相同资源内容，CDN按照优先级高的规则执行URL改写。 取值为1-100之间的整数，数值越大优先级越高。

        :return: The priority of this OriginRequestUrlRewrite.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        r"""Sets the priority of this OriginRequestUrlRewrite.

        回源URL改写规则的优先级。 优先级设置具有唯一性，不支持多条回源URL改写规则设置同一优先级，且优先级不能输入为空。 多条规则下，不同规则中的相同资源内容，CDN按照优先级高的规则执行URL改写。 取值为1-100之间的整数，数值越大优先级越高。

        :param priority: The priority of this OriginRequestUrlRewrite.
        :type priority: int
        """
        self._priority = priority

    @property
    def match_type(self):
        r"""Gets the match_type of this OriginRequestUrlRewrite.

        匹配类型， all：所有文件， file_path：URL路径， wildcard：通配符， full_path: 全路径。

        :return: The match_type of this OriginRequestUrlRewrite.
        :rtype: str
        """
        return self._match_type

    @match_type.setter
    def match_type(self, match_type):
        r"""Sets the match_type of this OriginRequestUrlRewrite.

        匹配类型， all：所有文件， file_path：URL路径， wildcard：通配符， full_path: 全路径。

        :param match_type: The match_type of this OriginRequestUrlRewrite.
        :type match_type: str
        """
        self._match_type = match_type

    @property
    def source_url(self):
        r"""Gets the source_url of this OriginRequestUrlRewrite.

        需要替换的URI。 改写后的URI以正斜线（/）开头的URI，不含http(s)://头及域名。 长度不超过512个字符。 支持通配符\\*匹配，如：/test/\\*/\\*.mp4。 匹配方式为“所有文件”时，不支持配置参数。

        :return: The source_url of this OriginRequestUrlRewrite.
        :rtype: str
        """
        return self._source_url

    @source_url.setter
    def source_url(self, source_url):
        r"""Sets the source_url of this OriginRequestUrlRewrite.

        需要替换的URI。 改写后的URI以正斜线（/）开头的URI，不含http(s)://头及域名。 长度不超过512个字符。 支持通配符\\*匹配，如：/test/\\*/\\*.mp4。 匹配方式为“所有文件”时，不支持配置参数。

        :param source_url: The source_url of this OriginRequestUrlRewrite.
        :type source_url: str
        """
        self._source_url = source_url

    @property
    def target_url(self):
        r"""Gets the target_url of this OriginRequestUrlRewrite.

        以正斜线（/）开头的URI，不含http(s)://头及域名。 长度不超过256个字符。 通配符 * 可通过$n捕获（n=1,2,3...，例如：/newtest/$1/$2.jpg）。

        :return: The target_url of this OriginRequestUrlRewrite.
        :rtype: str
        """
        return self._target_url

    @target_url.setter
    def target_url(self, target_url):
        r"""Sets the target_url of this OriginRequestUrlRewrite.

        以正斜线（/）开头的URI，不含http(s)://头及域名。 长度不超过256个字符。 通配符 * 可通过$n捕获（n=1,2,3...，例如：/newtest/$1/$2.jpg）。

        :param target_url: The target_url of this OriginRequestUrlRewrite.
        :type target_url: str
        """
        self._target_url = target_url

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
        if not isinstance(other, OriginRequestUrlRewrite):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
