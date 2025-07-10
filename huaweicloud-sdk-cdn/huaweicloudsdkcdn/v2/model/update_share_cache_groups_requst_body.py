# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateShareCacheGroupsRequstBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'share_cache_records': 'list[ShareCacheGroupsRecord]'
    }

    attribute_map = {
        'share_cache_records': 'share_cache_records'
    }

    def __init__(self, share_cache_records=None):
        r"""UpdateShareCacheGroupsRequstBody

        The model defined in huaweicloud sdk

        :param share_cache_records: **参数解释：** 关联域名 **约束限制：** - 必须传入主域名 - 最多可包含50个关联域名
        :type share_cache_records: list[:class:`huaweicloudsdkcdn.v2.ShareCacheGroupsRecord`]
        """
        
        

        self._share_cache_records = None
        self.discriminator = None

        if share_cache_records is not None:
            self.share_cache_records = share_cache_records

    @property
    def share_cache_records(self):
        r"""Gets the share_cache_records of this UpdateShareCacheGroupsRequstBody.

        **参数解释：** 关联域名 **约束限制：** - 必须传入主域名 - 最多可包含50个关联域名

        :return: The share_cache_records of this UpdateShareCacheGroupsRequstBody.
        :rtype: list[:class:`huaweicloudsdkcdn.v2.ShareCacheGroupsRecord`]
        """
        return self._share_cache_records

    @share_cache_records.setter
    def share_cache_records(self, share_cache_records):
        r"""Sets the share_cache_records of this UpdateShareCacheGroupsRequstBody.

        **参数解释：** 关联域名 **约束限制：** - 必须传入主域名 - 最多可包含50个关联域名

        :param share_cache_records: The share_cache_records of this UpdateShareCacheGroupsRequstBody.
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
        if not isinstance(other, UpdateShareCacheGroupsRequstBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
