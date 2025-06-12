# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListResourcesByTagsRequestBody:

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
        'tags': 'list[TagWithValues]',
        'matches': 'list[Match]'
    }

    attribute_map = {
        'without_any_tag': 'without_any_tag',
        'tags': 'tags',
        'matches': 'matches'
    }

    def __init__(self, without_any_tag=None, tags=None, matches=None):
        r"""ListResourcesByTagsRequestBody

        The model defined in huaweicloud sdk

        :param without_any_tag: 是否不包含任意一个标签
        :type without_any_tag: bool
        :param tags: 标签列表
        :type tags: list[:class:`huaweicloudsdkdli.v1.TagWithValues`]
        :param matches: 搜索字段列表
        :type matches: list[:class:`huaweicloudsdkdli.v1.Match`]
        """
        
        

        self._without_any_tag = None
        self._tags = None
        self._matches = None
        self.discriminator = None

        if without_any_tag is not None:
            self.without_any_tag = without_any_tag
        if tags is not None:
            self.tags = tags
        if matches is not None:
            self.matches = matches

    @property
    def without_any_tag(self):
        r"""Gets the without_any_tag of this ListResourcesByTagsRequestBody.

        是否不包含任意一个标签

        :return: The without_any_tag of this ListResourcesByTagsRequestBody.
        :rtype: bool
        """
        return self._without_any_tag

    @without_any_tag.setter
    def without_any_tag(self, without_any_tag):
        r"""Sets the without_any_tag of this ListResourcesByTagsRequestBody.

        是否不包含任意一个标签

        :param without_any_tag: The without_any_tag of this ListResourcesByTagsRequestBody.
        :type without_any_tag: bool
        """
        self._without_any_tag = without_any_tag

    @property
    def tags(self):
        r"""Gets the tags of this ListResourcesByTagsRequestBody.

        标签列表

        :return: The tags of this ListResourcesByTagsRequestBody.
        :rtype: list[:class:`huaweicloudsdkdli.v1.TagWithValues`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this ListResourcesByTagsRequestBody.

        标签列表

        :param tags: The tags of this ListResourcesByTagsRequestBody.
        :type tags: list[:class:`huaweicloudsdkdli.v1.TagWithValues`]
        """
        self._tags = tags

    @property
    def matches(self):
        r"""Gets the matches of this ListResourcesByTagsRequestBody.

        搜索字段列表

        :return: The matches of this ListResourcesByTagsRequestBody.
        :rtype: list[:class:`huaweicloudsdkdli.v1.Match`]
        """
        return self._matches

    @matches.setter
    def matches(self, matches):
        r"""Sets the matches of this ListResourcesByTagsRequestBody.

        搜索字段列表

        :param matches: The matches of this ListResourcesByTagsRequestBody.
        :type matches: list[:class:`huaweicloudsdkdli.v1.Match`]
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
        if not isinstance(other, ListResourcesByTagsRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
