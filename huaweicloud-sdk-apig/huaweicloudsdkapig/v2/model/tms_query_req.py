# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TmsQueryReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'without_any_tag': 'bool',
        'tags': 'list[TmsKeyValues]',
        'sys_tags': 'list[TmsKeyValues]',
        'matches': 'list[TmsMatchesKeyValue]'
    }

    attribute_map = {
        'without_any_tag': 'without_any_tag',
        'tags': 'tags',
        'sys_tags': 'sys_tags',
        'matches': 'matches'
    }

    def __init__(self, without_any_tag=None, tags=None, sys_tags=None, matches=None):
        r"""TmsQueryReq

        The model defined in huaweicloud sdk

        :param without_any_tag: 不包含任意一个标签，该字段为true时查询所有不带标签的资源，此时忽略 “tags”字段。 该字段为false或者未提供该参数时，该条件不生效。 
        :type without_any_tag: bool
        :param tags: 包含标签，最多包含20个key，每个key下面的value最多20个。无tag过滤条件时返回全量数据。
        :type tags: list[:class:`huaweicloudsdkapig.v2.TmsKeyValues`]
        :param sys_tags: 企业项目.仅op_service权限可以使用此字段做资源实例过滤条件. 无sys_tags时按照tag接口处理，无tag过滤条件时返回全量数据。
        :type sys_tags: list[:class:`huaweicloudsdkapig.v2.TmsKeyValues`]
        :param matches: 搜索字段,key为要匹配的字段,当前限定为resource_name。value为匹配的值。 根据key的值确认是否需要模糊匹配，如resource_name需要实现前缀搜索。 
        :type matches: list[:class:`huaweicloudsdkapig.v2.TmsMatchesKeyValue`]
        """
        
        

        self._without_any_tag = None
        self._tags = None
        self._sys_tags = None
        self._matches = None
        self.discriminator = None

        if without_any_tag is not None:
            self.without_any_tag = without_any_tag
        if tags is not None:
            self.tags = tags
        if sys_tags is not None:
            self.sys_tags = sys_tags
        if matches is not None:
            self.matches = matches

    @property
    def without_any_tag(self):
        r"""Gets the without_any_tag of this TmsQueryReq.

        不包含任意一个标签，该字段为true时查询所有不带标签的资源，此时忽略 “tags”字段。 该字段为false或者未提供该参数时，该条件不生效。 

        :return: The without_any_tag of this TmsQueryReq.
        :rtype: bool
        """
        return self._without_any_tag

    @without_any_tag.setter
    def without_any_tag(self, without_any_tag):
        r"""Sets the without_any_tag of this TmsQueryReq.

        不包含任意一个标签，该字段为true时查询所有不带标签的资源，此时忽略 “tags”字段。 该字段为false或者未提供该参数时，该条件不生效。 

        :param without_any_tag: The without_any_tag of this TmsQueryReq.
        :type without_any_tag: bool
        """
        self._without_any_tag = without_any_tag

    @property
    def tags(self):
        r"""Gets the tags of this TmsQueryReq.

        包含标签，最多包含20个key，每个key下面的value最多20个。无tag过滤条件时返回全量数据。

        :return: The tags of this TmsQueryReq.
        :rtype: list[:class:`huaweicloudsdkapig.v2.TmsKeyValues`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this TmsQueryReq.

        包含标签，最多包含20个key，每个key下面的value最多20个。无tag过滤条件时返回全量数据。

        :param tags: The tags of this TmsQueryReq.
        :type tags: list[:class:`huaweicloudsdkapig.v2.TmsKeyValues`]
        """
        self._tags = tags

    @property
    def sys_tags(self):
        r"""Gets the sys_tags of this TmsQueryReq.

        企业项目.仅op_service权限可以使用此字段做资源实例过滤条件. 无sys_tags时按照tag接口处理，无tag过滤条件时返回全量数据。

        :return: The sys_tags of this TmsQueryReq.
        :rtype: list[:class:`huaweicloudsdkapig.v2.TmsKeyValues`]
        """
        return self._sys_tags

    @sys_tags.setter
    def sys_tags(self, sys_tags):
        r"""Sets the sys_tags of this TmsQueryReq.

        企业项目.仅op_service权限可以使用此字段做资源实例过滤条件. 无sys_tags时按照tag接口处理，无tag过滤条件时返回全量数据。

        :param sys_tags: The sys_tags of this TmsQueryReq.
        :type sys_tags: list[:class:`huaweicloudsdkapig.v2.TmsKeyValues`]
        """
        self._sys_tags = sys_tags

    @property
    def matches(self):
        r"""Gets the matches of this TmsQueryReq.

        搜索字段,key为要匹配的字段,当前限定为resource_name。value为匹配的值。 根据key的值确认是否需要模糊匹配，如resource_name需要实现前缀搜索。 

        :return: The matches of this TmsQueryReq.
        :rtype: list[:class:`huaweicloudsdkapig.v2.TmsMatchesKeyValue`]
        """
        return self._matches

    @matches.setter
    def matches(self, matches):
        r"""Sets the matches of this TmsQueryReq.

        搜索字段,key为要匹配的字段,当前限定为resource_name。value为匹配的值。 根据key的值确认是否需要模糊匹配，如resource_name需要实现前缀搜索。 

        :param matches: The matches of this TmsQueryReq.
        :type matches: list[:class:`huaweicloudsdkapig.v2.TmsMatchesKeyValue`]
        """
        self._matches = matches

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
        if not isinstance(other, TmsQueryReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
