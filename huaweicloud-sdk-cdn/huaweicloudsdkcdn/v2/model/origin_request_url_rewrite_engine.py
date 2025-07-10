# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OriginRequestUrlRewriteEngine:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'rewrite_type': 'str',
        'source_url': 'str',
        'target_url': 'str'
    }

    attribute_map = {
        'rewrite_type': 'rewrite_type',
        'source_url': 'source_url',
        'target_url': 'target_url'
    }

    def __init__(self, rewrite_type=None, source_url=None, target_url=None):
        r"""OriginRequestUrlRewriteEngine

        The model defined in huaweicloud sdk

        :param rewrite_type: **参数解释：** 改写方式 **约束限制：** 不涉及 **取值范围：** - simple: 精确改写 - wildcard: 捕获改写 - regex: 正则改写（白名单功能，请提交工单开放该配置） **默认取值：** 不涉及
        :type rewrite_type: str
        :param source_url: **参数解释：** 需要替换的URI **约束限制：** 当rewrite_type为wildcard或regex时，该参数必填 当rewrite_type为regex时，该参数必填必须以“^/”开始，如：^/test **取值范围：** - 1-512个字符 - 支持通配符\\*匹配，如：/test/\\*/\\*.mp4 - 以正斜线（/）开头的URI，不含http(s)://头及域名 **默认取值：** 不涉及
        :type source_url: str
        :param target_url: **参数解释：** 替换后的URI **约束限制：** **取值范围：** - 1-256个字符 - 以正斜线（/）开头的URI，不含http(s)://头及域名  &gt; 通配符 * 可通过$n捕获（n&#x3D;1,2,3...，例如：/newtest/$1/$2.jpg）  **默认取值：** 不涉及
        :type target_url: str
        """
        
        

        self._rewrite_type = None
        self._source_url = None
        self._target_url = None
        self.discriminator = None

        self.rewrite_type = rewrite_type
        if source_url is not None:
            self.source_url = source_url
        self.target_url = target_url

    @property
    def rewrite_type(self):
        r"""Gets the rewrite_type of this OriginRequestUrlRewriteEngine.

        **参数解释：** 改写方式 **约束限制：** 不涉及 **取值范围：** - simple: 精确改写 - wildcard: 捕获改写 - regex: 正则改写（白名单功能，请提交工单开放该配置） **默认取值：** 不涉及

        :return: The rewrite_type of this OriginRequestUrlRewriteEngine.
        :rtype: str
        """
        return self._rewrite_type

    @rewrite_type.setter
    def rewrite_type(self, rewrite_type):
        r"""Sets the rewrite_type of this OriginRequestUrlRewriteEngine.

        **参数解释：** 改写方式 **约束限制：** 不涉及 **取值范围：** - simple: 精确改写 - wildcard: 捕获改写 - regex: 正则改写（白名单功能，请提交工单开放该配置） **默认取值：** 不涉及

        :param rewrite_type: The rewrite_type of this OriginRequestUrlRewriteEngine.
        :type rewrite_type: str
        """
        self._rewrite_type = rewrite_type

    @property
    def source_url(self):
        r"""Gets the source_url of this OriginRequestUrlRewriteEngine.

        **参数解释：** 需要替换的URI **约束限制：** 当rewrite_type为wildcard或regex时，该参数必填 当rewrite_type为regex时，该参数必填必须以“^/”开始，如：^/test **取值范围：** - 1-512个字符 - 支持通配符\\*匹配，如：/test/\\*/\\*.mp4 - 以正斜线（/）开头的URI，不含http(s)://头及域名 **默认取值：** 不涉及

        :return: The source_url of this OriginRequestUrlRewriteEngine.
        :rtype: str
        """
        return self._source_url

    @source_url.setter
    def source_url(self, source_url):
        r"""Sets the source_url of this OriginRequestUrlRewriteEngine.

        **参数解释：** 需要替换的URI **约束限制：** 当rewrite_type为wildcard或regex时，该参数必填 当rewrite_type为regex时，该参数必填必须以“^/”开始，如：^/test **取值范围：** - 1-512个字符 - 支持通配符\\*匹配，如：/test/\\*/\\*.mp4 - 以正斜线（/）开头的URI，不含http(s)://头及域名 **默认取值：** 不涉及

        :param source_url: The source_url of this OriginRequestUrlRewriteEngine.
        :type source_url: str
        """
        self._source_url = source_url

    @property
    def target_url(self):
        r"""Gets the target_url of this OriginRequestUrlRewriteEngine.

        **参数解释：** 替换后的URI **约束限制：** **取值范围：** - 1-256个字符 - 以正斜线（/）开头的URI，不含http(s)://头及域名  > 通配符 * 可通过$n捕获（n=1,2,3...，例如：/newtest/$1/$2.jpg）  **默认取值：** 不涉及

        :return: The target_url of this OriginRequestUrlRewriteEngine.
        :rtype: str
        """
        return self._target_url

    @target_url.setter
    def target_url(self, target_url):
        r"""Sets the target_url of this OriginRequestUrlRewriteEngine.

        **参数解释：** 替换后的URI **约束限制：** **取值范围：** - 1-256个字符 - 以正斜线（/）开头的URI，不含http(s)://头及域名  > 通配符 * 可通过$n捕获（n=1,2,3...，例如：/newtest/$1/$2.jpg）  **默认取值：** 不涉及

        :param target_url: The target_url of this OriginRequestUrlRewriteEngine.
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
        if not isinstance(other, OriginRequestUrlRewriteEngine):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
