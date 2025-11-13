# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TmsResourceInstancesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'offset': 'int',
        'limit': 'int',
        'action': 'str',
        'tags': 'list[TmsResourceInstancesTag]',
        'sys_tags': 'list[TmsResourceInstancesTag]',
        'matches': 'list[TmsResourceTag]',
        'without_any_tag': 'str',
        'tags_any': 'list[TmsResourceInstancesTag]',
        'not_tags_any': 'list[TmsResourceInstancesTag]',
        'not_tags': 'list[TmsResourceInstancesTag]'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'action': 'action',
        'tags': 'tags',
        'sys_tags': 'sys_tags',
        'matches': 'matches',
        'without_any_tag': 'without_any_tag',
        'tags_any': 'tags_any',
        'not_tags_any': 'not_tags_any',
        'not_tags': 'not_tags'
    }

    def __init__(self, offset=None, limit=None, action=None, tags=None, sys_tags=None, matches=None, without_any_tag=None, tags_any=None, not_tags_any=None, not_tags=None):
        r"""TmsResourceInstancesRequest

        The model defined in huaweicloud sdk

        :param offset: 索引位置，默认为0
        :type offset: int
        :param limit: 查询记录数，默认为1000
        :type limit: int
        :param action: 操作标识
        :type action: str
        :param tags: 标签
        :type tags: list[:class:`huaweicloudsdkwaf.v1.TmsResourceInstancesTag`]
        :param sys_tags: 系统标签
        :type sys_tags: list[:class:`huaweicloudsdkwaf.v1.TmsResourceInstancesTag`]
        :param matches: tms资源标签
        :type matches: list[:class:`huaweicloudsdkwaf.v1.TmsResourceTag`]
        :param without_any_tag: 无任何标签的资源筛选标识
        :type without_any_tag: str
        :param tags_any: 任意标签的资源筛选标识
        :type tags_any: list[:class:`huaweicloudsdkwaf.v1.TmsResourceInstancesTag`]
        :param not_tags_any: 不标识于标签
        :type not_tags_any: list[:class:`huaweicloudsdkwaf.v1.TmsResourceInstancesTag`]
        :param not_tags: 不标识于标签
        :type not_tags: list[:class:`huaweicloudsdkwaf.v1.TmsResourceInstancesTag`]
        """
        
        

        self._offset = None
        self._limit = None
        self._action = None
        self._tags = None
        self._sys_tags = None
        self._matches = None
        self._without_any_tag = None
        self._tags_any = None
        self._not_tags_any = None
        self._not_tags = None
        self.discriminator = None

        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if action is not None:
            self.action = action
        if tags is not None:
            self.tags = tags
        if sys_tags is not None:
            self.sys_tags = sys_tags
        if matches is not None:
            self.matches = matches
        if without_any_tag is not None:
            self.without_any_tag = without_any_tag
        if tags_any is not None:
            self.tags_any = tags_any
        if not_tags_any is not None:
            self.not_tags_any = not_tags_any
        if not_tags is not None:
            self.not_tags = not_tags

    @property
    def offset(self):
        r"""Gets the offset of this TmsResourceInstancesRequest.

        索引位置，默认为0

        :return: The offset of this TmsResourceInstancesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this TmsResourceInstancesRequest.

        索引位置，默认为0

        :param offset: The offset of this TmsResourceInstancesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this TmsResourceInstancesRequest.

        查询记录数，默认为1000

        :return: The limit of this TmsResourceInstancesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this TmsResourceInstancesRequest.

        查询记录数，默认为1000

        :param limit: The limit of this TmsResourceInstancesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def action(self):
        r"""Gets the action of this TmsResourceInstancesRequest.

        操作标识

        :return: The action of this TmsResourceInstancesRequest.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this TmsResourceInstancesRequest.

        操作标识

        :param action: The action of this TmsResourceInstancesRequest.
        :type action: str
        """
        self._action = action

    @property
    def tags(self):
        r"""Gets the tags of this TmsResourceInstancesRequest.

        标签

        :return: The tags of this TmsResourceInstancesRequest.
        :rtype: list[:class:`huaweicloudsdkwaf.v1.TmsResourceInstancesTag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this TmsResourceInstancesRequest.

        标签

        :param tags: The tags of this TmsResourceInstancesRequest.
        :type tags: list[:class:`huaweicloudsdkwaf.v1.TmsResourceInstancesTag`]
        """
        self._tags = tags

    @property
    def sys_tags(self):
        r"""Gets the sys_tags of this TmsResourceInstancesRequest.

        系统标签

        :return: The sys_tags of this TmsResourceInstancesRequest.
        :rtype: list[:class:`huaweicloudsdkwaf.v1.TmsResourceInstancesTag`]
        """
        return self._sys_tags

    @sys_tags.setter
    def sys_tags(self, sys_tags):
        r"""Sets the sys_tags of this TmsResourceInstancesRequest.

        系统标签

        :param sys_tags: The sys_tags of this TmsResourceInstancesRequest.
        :type sys_tags: list[:class:`huaweicloudsdkwaf.v1.TmsResourceInstancesTag`]
        """
        self._sys_tags = sys_tags

    @property
    def matches(self):
        r"""Gets the matches of this TmsResourceInstancesRequest.

        tms资源标签

        :return: The matches of this TmsResourceInstancesRequest.
        :rtype: list[:class:`huaweicloudsdkwaf.v1.TmsResourceTag`]
        """
        return self._matches

    @matches.setter
    def matches(self, matches):
        r"""Sets the matches of this TmsResourceInstancesRequest.

        tms资源标签

        :param matches: The matches of this TmsResourceInstancesRequest.
        :type matches: list[:class:`huaweicloudsdkwaf.v1.TmsResourceTag`]
        """
        self._matches = matches

    @property
    def without_any_tag(self):
        r"""Gets the without_any_tag of this TmsResourceInstancesRequest.

        无任何标签的资源筛选标识

        :return: The without_any_tag of this TmsResourceInstancesRequest.
        :rtype: str
        """
        return self._without_any_tag

    @without_any_tag.setter
    def without_any_tag(self, without_any_tag):
        r"""Sets the without_any_tag of this TmsResourceInstancesRequest.

        无任何标签的资源筛选标识

        :param without_any_tag: The without_any_tag of this TmsResourceInstancesRequest.
        :type without_any_tag: str
        """
        self._without_any_tag = without_any_tag

    @property
    def tags_any(self):
        r"""Gets the tags_any of this TmsResourceInstancesRequest.

        任意标签的资源筛选标识

        :return: The tags_any of this TmsResourceInstancesRequest.
        :rtype: list[:class:`huaweicloudsdkwaf.v1.TmsResourceInstancesTag`]
        """
        return self._tags_any

    @tags_any.setter
    def tags_any(self, tags_any):
        r"""Sets the tags_any of this TmsResourceInstancesRequest.

        任意标签的资源筛选标识

        :param tags_any: The tags_any of this TmsResourceInstancesRequest.
        :type tags_any: list[:class:`huaweicloudsdkwaf.v1.TmsResourceInstancesTag`]
        """
        self._tags_any = tags_any

    @property
    def not_tags_any(self):
        r"""Gets the not_tags_any of this TmsResourceInstancesRequest.

        不标识于标签

        :return: The not_tags_any of this TmsResourceInstancesRequest.
        :rtype: list[:class:`huaweicloudsdkwaf.v1.TmsResourceInstancesTag`]
        """
        return self._not_tags_any

    @not_tags_any.setter
    def not_tags_any(self, not_tags_any):
        r"""Sets the not_tags_any of this TmsResourceInstancesRequest.

        不标识于标签

        :param not_tags_any: The not_tags_any of this TmsResourceInstancesRequest.
        :type not_tags_any: list[:class:`huaweicloudsdkwaf.v1.TmsResourceInstancesTag`]
        """
        self._not_tags_any = not_tags_any

    @property
    def not_tags(self):
        r"""Gets the not_tags of this TmsResourceInstancesRequest.

        不标识于标签

        :return: The not_tags of this TmsResourceInstancesRequest.
        :rtype: list[:class:`huaweicloudsdkwaf.v1.TmsResourceInstancesTag`]
        """
        return self._not_tags

    @not_tags.setter
    def not_tags(self, not_tags):
        r"""Sets the not_tags of this TmsResourceInstancesRequest.

        不标识于标签

        :param not_tags: The not_tags of this TmsResourceInstancesRequest.
        :type not_tags: list[:class:`huaweicloudsdkwaf.v1.TmsResourceInstancesTag`]
        """
        self._not_tags = not_tags

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TmsResourceInstancesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
