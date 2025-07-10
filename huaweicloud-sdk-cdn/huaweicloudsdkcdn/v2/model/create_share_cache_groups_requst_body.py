# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateShareCacheGroupsRequstBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'group_name': 'str',
        'primary_domain': 'str',
        'share_cache_records': 'list[ShareCacheGroupsRecord]'
    }

    attribute_map = {
        'group_name': 'group_name',
        'primary_domain': 'primary_domain',
        'share_cache_records': 'share_cache_records'
    }

    def __init__(self, group_name=None, primary_domain=None, share_cache_records=None):
        r"""CreateShareCacheGroupsRequstBody

        The model defined in huaweicloud sdk

        :param group_name: **参数解释：** 共享缓存组名称 **约束限制：** 不涉及 **取值范围：** - 1-128个字符 - 不支持特殊字符“%”、“&amp;”、“&#x3D;”、“?”、“$”\&quot;、“\&quot;”、“&lt;”、“&gt;” **默认取值：** 不涉及
        :type group_name: str
        :param primary_domain: **参数解释：** 主域名 **约束限制：** 只能有一个主域名 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type primary_domain: str
        :param share_cache_records: **参数解释：** 关联域名 **约束限制：** - 必须传入主域名 - 最多可包含50个关联域名
        :type share_cache_records: list[:class:`huaweicloudsdkcdn.v2.ShareCacheGroupsRecord`]
        """
        
        

        self._group_name = None
        self._primary_domain = None
        self._share_cache_records = None
        self.discriminator = None

        if group_name is not None:
            self.group_name = group_name
        if primary_domain is not None:
            self.primary_domain = primary_domain
        if share_cache_records is not None:
            self.share_cache_records = share_cache_records

    @property
    def group_name(self):
        r"""Gets the group_name of this CreateShareCacheGroupsRequstBody.

        **参数解释：** 共享缓存组名称 **约束限制：** 不涉及 **取值范围：** - 1-128个字符 - 不支持特殊字符“%”、“&”、“=”、“?”、“$”\"、“\"”、“<”、“>” **默认取值：** 不涉及

        :return: The group_name of this CreateShareCacheGroupsRequstBody.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        r"""Sets the group_name of this CreateShareCacheGroupsRequstBody.

        **参数解释：** 共享缓存组名称 **约束限制：** 不涉及 **取值范围：** - 1-128个字符 - 不支持特殊字符“%”、“&”、“=”、“?”、“$”\"、“\"”、“<”、“>” **默认取值：** 不涉及

        :param group_name: The group_name of this CreateShareCacheGroupsRequstBody.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def primary_domain(self):
        r"""Gets the primary_domain of this CreateShareCacheGroupsRequstBody.

        **参数解释：** 主域名 **约束限制：** 只能有一个主域名 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The primary_domain of this CreateShareCacheGroupsRequstBody.
        :rtype: str
        """
        return self._primary_domain

    @primary_domain.setter
    def primary_domain(self, primary_domain):
        r"""Sets the primary_domain of this CreateShareCacheGroupsRequstBody.

        **参数解释：** 主域名 **约束限制：** 只能有一个主域名 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param primary_domain: The primary_domain of this CreateShareCacheGroupsRequstBody.
        :type primary_domain: str
        """
        self._primary_domain = primary_domain

    @property
    def share_cache_records(self):
        r"""Gets the share_cache_records of this CreateShareCacheGroupsRequstBody.

        **参数解释：** 关联域名 **约束限制：** - 必须传入主域名 - 最多可包含50个关联域名

        :return: The share_cache_records of this CreateShareCacheGroupsRequstBody.
        :rtype: list[:class:`huaweicloudsdkcdn.v2.ShareCacheGroupsRecord`]
        """
        return self._share_cache_records

    @share_cache_records.setter
    def share_cache_records(self, share_cache_records):
        r"""Sets the share_cache_records of this CreateShareCacheGroupsRequstBody.

        **参数解释：** 关联域名 **约束限制：** - 必须传入主域名 - 最多可包含50个关联域名

        :param share_cache_records: The share_cache_records of this CreateShareCacheGroupsRequstBody.
        :type share_cache_records: list[:class:`huaweicloudsdkcdn.v2.ShareCacheGroupsRecord`]
        """
        self._share_cache_records = share_cache_records

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
        if not isinstance(other, CreateShareCacheGroupsRequstBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
