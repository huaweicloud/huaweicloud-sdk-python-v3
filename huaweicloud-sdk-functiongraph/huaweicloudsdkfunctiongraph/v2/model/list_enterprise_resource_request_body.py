# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListEnterpriseResourceRequestBody:

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
        'limit': 'str',
        'offset': 'str',
        'action': 'str',
        'matches': 'list[KvItem]',
        'sys_tags': 'list[TagItem]'
    }

    attribute_map = {
        'without_any_tag': 'without_any_tag',
        'limit': 'limit',
        'offset': 'offset',
        'action': 'action',
        'matches': 'matches',
        'sys_tags': 'sys_tags'
    }

    def __init__(self, without_any_tag=None, limit=None, offset=None, action=None, matches=None, sys_tags=None):
        r"""ListEnterpriseResourceRequestBody

        The model defined in huaweicloud sdk

        :param without_any_tag: 是否通过标签过滤
        :type without_any_tag: bool
        :param limit: 每页显示条数
        :type limit: str
        :param offset: 查询偏移量
        :type offset: str
        :param action: 查询指定action
        :type action: str
        :param matches: 查询指定键值对
        :type matches: list[:class:`huaweicloudsdkfunctiongraph.v2.KvItem`]
        :param sys_tags: 查询指定系统标签列表
        :type sys_tags: list[:class:`huaweicloudsdkfunctiongraph.v2.TagItem`]
        """
        
        

        self._without_any_tag = None
        self._limit = None
        self._offset = None
        self._action = None
        self._matches = None
        self._sys_tags = None
        self.discriminator = None

        if without_any_tag is not None:
            self.without_any_tag = without_any_tag
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if action is not None:
            self.action = action
        if matches is not None:
            self.matches = matches
        if sys_tags is not None:
            self.sys_tags = sys_tags

    @property
    def without_any_tag(self):
        r"""Gets the without_any_tag of this ListEnterpriseResourceRequestBody.

        是否通过标签过滤

        :return: The without_any_tag of this ListEnterpriseResourceRequestBody.
        :rtype: bool
        """
        return self._without_any_tag

    @without_any_tag.setter
    def without_any_tag(self, without_any_tag):
        r"""Sets the without_any_tag of this ListEnterpriseResourceRequestBody.

        是否通过标签过滤

        :param without_any_tag: The without_any_tag of this ListEnterpriseResourceRequestBody.
        :type without_any_tag: bool
        """
        self._without_any_tag = without_any_tag

    @property
    def limit(self):
        r"""Gets the limit of this ListEnterpriseResourceRequestBody.

        每页显示条数

        :return: The limit of this ListEnterpriseResourceRequestBody.
        :rtype: str
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListEnterpriseResourceRequestBody.

        每页显示条数

        :param limit: The limit of this ListEnterpriseResourceRequestBody.
        :type limit: str
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListEnterpriseResourceRequestBody.

        查询偏移量

        :return: The offset of this ListEnterpriseResourceRequestBody.
        :rtype: str
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListEnterpriseResourceRequestBody.

        查询偏移量

        :param offset: The offset of this ListEnterpriseResourceRequestBody.
        :type offset: str
        """
        self._offset = offset

    @property
    def action(self):
        r"""Gets the action of this ListEnterpriseResourceRequestBody.

        查询指定action

        :return: The action of this ListEnterpriseResourceRequestBody.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this ListEnterpriseResourceRequestBody.

        查询指定action

        :param action: The action of this ListEnterpriseResourceRequestBody.
        :type action: str
        """
        self._action = action

    @property
    def matches(self):
        r"""Gets the matches of this ListEnterpriseResourceRequestBody.

        查询指定键值对

        :return: The matches of this ListEnterpriseResourceRequestBody.
        :rtype: list[:class:`huaweicloudsdkfunctiongraph.v2.KvItem`]
        """
        return self._matches

    @matches.setter
    def matches(self, matches):
        r"""Sets the matches of this ListEnterpriseResourceRequestBody.

        查询指定键值对

        :param matches: The matches of this ListEnterpriseResourceRequestBody.
        :type matches: list[:class:`huaweicloudsdkfunctiongraph.v2.KvItem`]
        """
        self._matches = matches

    @property
    def sys_tags(self):
        r"""Gets the sys_tags of this ListEnterpriseResourceRequestBody.

        查询指定系统标签列表

        :return: The sys_tags of this ListEnterpriseResourceRequestBody.
        :rtype: list[:class:`huaweicloudsdkfunctiongraph.v2.TagItem`]
        """
        return self._sys_tags

    @sys_tags.setter
    def sys_tags(self, sys_tags):
        r"""Sets the sys_tags of this ListEnterpriseResourceRequestBody.

        查询指定系统标签列表

        :param sys_tags: The sys_tags of this ListEnterpriseResourceRequestBody.
        :type sys_tags: list[:class:`huaweicloudsdkfunctiongraph.v2.TagItem`]
        """
        self._sys_tags = sys_tags

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
        if not isinstance(other, ListEnterpriseResourceRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
