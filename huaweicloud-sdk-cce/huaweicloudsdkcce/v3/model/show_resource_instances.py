# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowResourceInstances:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'action': 'str',
        'tags': 'TagFilter',
        'tags_any': 'TagFilter',
        'not_tags': 'TagFilter',
        'not_tags_any': 'TagFilter',
        'sys_tags': 'TagFilter',
        'without_any_tag': 'bool',
        'limit': 'str',
        'offset': 'str',
        'matches': 'list[object]'
    }

    attribute_map = {
        'action': 'action',
        'tags': 'tags',
        'tags_any': 'tags_any',
        'not_tags': 'not_tags',
        'not_tags_any': 'not_tags_any',
        'sys_tags': 'sys_tags',
        'without_any_tag': 'without_any_tag',
        'limit': 'limit',
        'offset': 'offset',
        'matches': 'matches'
    }

    def __init__(self, action=None, tags=None, tags_any=None, not_tags=None, not_tags_any=None, sys_tags=None, without_any_tag=None, limit=None, offset=None, matches=None):
        """ShowResourceInstances

        The model defined in huaweicloud sdk

        :param action: action类型，\&quot;filter\&quot;或者\&quot;count\&quot;。
        :type action: str
        :param tags: 
        :type tags: :class:`huaweicloudsdkcce.v3.TagFilter`
        :param tags_any: 
        :type tags_any: :class:`huaweicloudsdkcce.v3.TagFilter`
        :param not_tags: 
        :type not_tags: :class:`huaweicloudsdkcce.v3.TagFilter`
        :param not_tags_any: 
        :type not_tags_any: :class:`huaweicloudsdkcce.v3.TagFilter`
        :param sys_tags: 
        :type sys_tags: :class:`huaweicloudsdkcce.v3.TagFilter`
        :param without_any_tag: 忽略其他标签字段，返回不带任何标签的资源。
        :type without_any_tag: bool
        :param limit: 
        :type limit: str
        :param offset: 
        :type offset: str
        :param matches: 
        :type matches: list[object]
        """
        
        

        self._action = None
        self._tags = None
        self._tags_any = None
        self._not_tags = None
        self._not_tags_any = None
        self._sys_tags = None
        self._without_any_tag = None
        self._limit = None
        self._offset = None
        self._matches = None
        self.discriminator = None

        self.action = action
        if tags is not None:
            self.tags = tags
        if tags_any is not None:
            self.tags_any = tags_any
        if not_tags is not None:
            self.not_tags = not_tags
        if not_tags_any is not None:
            self.not_tags_any = not_tags_any
        if sys_tags is not None:
            self.sys_tags = sys_tags
        if without_any_tag is not None:
            self.without_any_tag = without_any_tag
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if matches is not None:
            self.matches = matches

    @property
    def action(self):
        """Gets the action of this ShowResourceInstances.

        action类型，\"filter\"或者\"count\"。

        :return: The action of this ShowResourceInstances.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this ShowResourceInstances.

        action类型，\"filter\"或者\"count\"。

        :param action: The action of this ShowResourceInstances.
        :type action: str
        """
        self._action = action

    @property
    def tags(self):
        """Gets the tags of this ShowResourceInstances.

        :return: The tags of this ShowResourceInstances.
        :rtype: :class:`huaweicloudsdkcce.v3.TagFilter`
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ShowResourceInstances.

        :param tags: The tags of this ShowResourceInstances.
        :type tags: :class:`huaweicloudsdkcce.v3.TagFilter`
        """
        self._tags = tags

    @property
    def tags_any(self):
        """Gets the tags_any of this ShowResourceInstances.

        :return: The tags_any of this ShowResourceInstances.
        :rtype: :class:`huaweicloudsdkcce.v3.TagFilter`
        """
        return self._tags_any

    @tags_any.setter
    def tags_any(self, tags_any):
        """Sets the tags_any of this ShowResourceInstances.

        :param tags_any: The tags_any of this ShowResourceInstances.
        :type tags_any: :class:`huaweicloudsdkcce.v3.TagFilter`
        """
        self._tags_any = tags_any

    @property
    def not_tags(self):
        """Gets the not_tags of this ShowResourceInstances.

        :return: The not_tags of this ShowResourceInstances.
        :rtype: :class:`huaweicloudsdkcce.v3.TagFilter`
        """
        return self._not_tags

    @not_tags.setter
    def not_tags(self, not_tags):
        """Sets the not_tags of this ShowResourceInstances.

        :param not_tags: The not_tags of this ShowResourceInstances.
        :type not_tags: :class:`huaweicloudsdkcce.v3.TagFilter`
        """
        self._not_tags = not_tags

    @property
    def not_tags_any(self):
        """Gets the not_tags_any of this ShowResourceInstances.

        :return: The not_tags_any of this ShowResourceInstances.
        :rtype: :class:`huaweicloudsdkcce.v3.TagFilter`
        """
        return self._not_tags_any

    @not_tags_any.setter
    def not_tags_any(self, not_tags_any):
        """Sets the not_tags_any of this ShowResourceInstances.

        :param not_tags_any: The not_tags_any of this ShowResourceInstances.
        :type not_tags_any: :class:`huaweicloudsdkcce.v3.TagFilter`
        """
        self._not_tags_any = not_tags_any

    @property
    def sys_tags(self):
        """Gets the sys_tags of this ShowResourceInstances.

        :return: The sys_tags of this ShowResourceInstances.
        :rtype: :class:`huaweicloudsdkcce.v3.TagFilter`
        """
        return self._sys_tags

    @sys_tags.setter
    def sys_tags(self, sys_tags):
        """Sets the sys_tags of this ShowResourceInstances.

        :param sys_tags: The sys_tags of this ShowResourceInstances.
        :type sys_tags: :class:`huaweicloudsdkcce.v3.TagFilter`
        """
        self._sys_tags = sys_tags

    @property
    def without_any_tag(self):
        """Gets the without_any_tag of this ShowResourceInstances.

        忽略其他标签字段，返回不带任何标签的资源。

        :return: The without_any_tag of this ShowResourceInstances.
        :rtype: bool
        """
        return self._without_any_tag

    @without_any_tag.setter
    def without_any_tag(self, without_any_tag):
        """Sets the without_any_tag of this ShowResourceInstances.

        忽略其他标签字段，返回不带任何标签的资源。

        :param without_any_tag: The without_any_tag of this ShowResourceInstances.
        :type without_any_tag: bool
        """
        self._without_any_tag = without_any_tag

    @property
    def limit(self):
        """Gets the limit of this ShowResourceInstances.

        :return: The limit of this ShowResourceInstances.
        :rtype: str
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ShowResourceInstances.

        :param limit: The limit of this ShowResourceInstances.
        :type limit: str
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ShowResourceInstances.

        :return: The offset of this ShowResourceInstances.
        :rtype: str
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ShowResourceInstances.

        :param offset: The offset of this ShowResourceInstances.
        :type offset: str
        """
        self._offset = offset

    @property
    def matches(self):
        """Gets the matches of this ShowResourceInstances.

        :return: The matches of this ShowResourceInstances.
        :rtype: list[object]
        """
        return self._matches

    @matches.setter
    def matches(self, matches):
        """Sets the matches of this ShowResourceInstances.

        :param matches: The matches of this ShowResourceInstances.
        :type matches: list[object]
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
        if not isinstance(other, ShowResourceInstances):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
