# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueryDesktopByTagReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'offset': 'str',
        'limit': 'str',
        'action': 'str',
        'without_any_tag': 'bool',
        'matches': 'list[Match]',
        'tags': 'list[Tags]',
        'tags_any': 'list[Tags]',
        'not_tags': 'list[Tags]',
        'not_tags_any': 'list[Tags]'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'action': 'action',
        'without_any_tag': 'without_any_tag',
        'matches': 'matches',
        'tags': 'tags',
        'tags_any': 'tags_any',
        'not_tags': 'not_tags',
        'not_tags_any': 'not_tags_any'
    }

    def __init__(self, offset=None, limit=None, action=None, without_any_tag=None, matches=None, tags=None, tags_any=None, not_tags=None, not_tags_any=None):
        """QueryDesktopByTagReq

        The model defined in huaweicloud sdk

        :param offset: 默认为0
        :type offset: str
        :param limit: 默认为1000
        :type limit: str
        :param action: 如果是filter就是分页查询，如果是count只需按照条件将总条数返回即可
        :type action: str
        :param without_any_tag: 包含任意一个标签,该字段为true时查询所有不带标签的资源
        :type without_any_tag: bool
        :param matches: match对象
        :type matches: list[:class:`huaweicloudsdkworkspace.v2.Match`]
        :param tags: 包含的标签对象，只要有一个不包含，就不符合，一个key对应多个value
        :type tags: list[:class:`huaweicloudsdkworkspace.v2.Tags`]
        :param tags_any: 包含任意标签，若全都不包含，不符合，一个key对应多个value
        :type tags_any: list[:class:`huaweicloudsdkworkspace.v2.Tags`]
        :param not_tags: 不包含标签，只要有一个不包含，就符合了，一个key对应多个value
        :type not_tags: list[:class:`huaweicloudsdkworkspace.v2.Tags`]
        :param not_tags_any: 不包含任意标签，只要包含其中一个，就不符合，一个key对应多个value
        :type not_tags_any: list[:class:`huaweicloudsdkworkspace.v2.Tags`]
        """
        
        

        self._offset = None
        self._limit = None
        self._action = None
        self._without_any_tag = None
        self._matches = None
        self._tags = None
        self._tags_any = None
        self._not_tags = None
        self._not_tags_any = None
        self.discriminator = None

        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if action is not None:
            self.action = action
        if without_any_tag is not None:
            self.without_any_tag = without_any_tag
        if matches is not None:
            self.matches = matches
        if tags is not None:
            self.tags = tags
        if tags_any is not None:
            self.tags_any = tags_any
        if not_tags is not None:
            self.not_tags = not_tags
        if not_tags_any is not None:
            self.not_tags_any = not_tags_any

    @property
    def offset(self):
        """Gets the offset of this QueryDesktopByTagReq.

        默认为0

        :return: The offset of this QueryDesktopByTagReq.
        :rtype: str
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this QueryDesktopByTagReq.

        默认为0

        :param offset: The offset of this QueryDesktopByTagReq.
        :type offset: str
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this QueryDesktopByTagReq.

        默认为1000

        :return: The limit of this QueryDesktopByTagReq.
        :rtype: str
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this QueryDesktopByTagReq.

        默认为1000

        :param limit: The limit of this QueryDesktopByTagReq.
        :type limit: str
        """
        self._limit = limit

    @property
    def action(self):
        """Gets the action of this QueryDesktopByTagReq.

        如果是filter就是分页查询，如果是count只需按照条件将总条数返回即可

        :return: The action of this QueryDesktopByTagReq.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this QueryDesktopByTagReq.

        如果是filter就是分页查询，如果是count只需按照条件将总条数返回即可

        :param action: The action of this QueryDesktopByTagReq.
        :type action: str
        """
        self._action = action

    @property
    def without_any_tag(self):
        """Gets the without_any_tag of this QueryDesktopByTagReq.

        包含任意一个标签,该字段为true时查询所有不带标签的资源

        :return: The without_any_tag of this QueryDesktopByTagReq.
        :rtype: bool
        """
        return self._without_any_tag

    @without_any_tag.setter
    def without_any_tag(self, without_any_tag):
        """Sets the without_any_tag of this QueryDesktopByTagReq.

        包含任意一个标签,该字段为true时查询所有不带标签的资源

        :param without_any_tag: The without_any_tag of this QueryDesktopByTagReq.
        :type without_any_tag: bool
        """
        self._without_any_tag = without_any_tag

    @property
    def matches(self):
        """Gets the matches of this QueryDesktopByTagReq.

        match对象

        :return: The matches of this QueryDesktopByTagReq.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.Match`]
        """
        return self._matches

    @matches.setter
    def matches(self, matches):
        """Sets the matches of this QueryDesktopByTagReq.

        match对象

        :param matches: The matches of this QueryDesktopByTagReq.
        :type matches: list[:class:`huaweicloudsdkworkspace.v2.Match`]
        """
        self._matches = matches

    @property
    def tags(self):
        """Gets the tags of this QueryDesktopByTagReq.

        包含的标签对象，只要有一个不包含，就不符合，一个key对应多个value

        :return: The tags of this QueryDesktopByTagReq.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.Tags`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this QueryDesktopByTagReq.

        包含的标签对象，只要有一个不包含，就不符合，一个key对应多个value

        :param tags: The tags of this QueryDesktopByTagReq.
        :type tags: list[:class:`huaweicloudsdkworkspace.v2.Tags`]
        """
        self._tags = tags

    @property
    def tags_any(self):
        """Gets the tags_any of this QueryDesktopByTagReq.

        包含任意标签，若全都不包含，不符合，一个key对应多个value

        :return: The tags_any of this QueryDesktopByTagReq.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.Tags`]
        """
        return self._tags_any

    @tags_any.setter
    def tags_any(self, tags_any):
        """Sets the tags_any of this QueryDesktopByTagReq.

        包含任意标签，若全都不包含，不符合，一个key对应多个value

        :param tags_any: The tags_any of this QueryDesktopByTagReq.
        :type tags_any: list[:class:`huaweicloudsdkworkspace.v2.Tags`]
        """
        self._tags_any = tags_any

    @property
    def not_tags(self):
        """Gets the not_tags of this QueryDesktopByTagReq.

        不包含标签，只要有一个不包含，就符合了，一个key对应多个value

        :return: The not_tags of this QueryDesktopByTagReq.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.Tags`]
        """
        return self._not_tags

    @not_tags.setter
    def not_tags(self, not_tags):
        """Sets the not_tags of this QueryDesktopByTagReq.

        不包含标签，只要有一个不包含，就符合了，一个key对应多个value

        :param not_tags: The not_tags of this QueryDesktopByTagReq.
        :type not_tags: list[:class:`huaweicloudsdkworkspace.v2.Tags`]
        """
        self._not_tags = not_tags

    @property
    def not_tags_any(self):
        """Gets the not_tags_any of this QueryDesktopByTagReq.

        不包含任意标签，只要包含其中一个，就不符合，一个key对应多个value

        :return: The not_tags_any of this QueryDesktopByTagReq.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.Tags`]
        """
        return self._not_tags_any

    @not_tags_any.setter
    def not_tags_any(self, not_tags_any):
        """Sets the not_tags_any of this QueryDesktopByTagReq.

        不包含任意标签，只要包含其中一个，就不符合，一个key对应多个value

        :param not_tags_any: The not_tags_any of this QueryDesktopByTagReq.
        :type not_tags_any: list[:class:`huaweicloudsdkworkspace.v2.Tags`]
        """
        self._not_tags_any = not_tags_any

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
        if not isinstance(other, QueryDesktopByTagReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
