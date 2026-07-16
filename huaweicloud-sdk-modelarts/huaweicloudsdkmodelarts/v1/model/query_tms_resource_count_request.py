# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueryTmsResourceCountRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'matches': 'list[TmsMatch]',
        'tags': 'list[CombineInferTmsTags]',
        'without_any_tag': 'bool'
    }

    attribute_map = {
        'matches': 'matches',
        'tags': 'tags',
        'without_any_tag': 'without_any_tag'
    }

    def __init__(self, matches=None, tags=None, without_any_tag=None):
        r"""QueryTmsResourceCountRequest

        The model defined in huaweicloud sdk

        :param matches: **参数解释：** 匹配项，目前只支持资源名称的模糊匹配。 **约束限制：** 不涉及。
        :type matches: list[:class:`huaweicloudsdkmodelarts.v1.TmsMatch`]
        :param tags: **参数解释：** 标签匹配项，只支持多个标签与操作，不携带表示查询所有资源。 **约束限制：** 不涉及。
        :type tags: list[:class:`huaweicloudsdkmodelarts.v1.CombineInferTmsTags`]
        :param without_any_tag: **参数解释：** 是否只查询没有打标签的资源。 **约束限制：** 不涉及。 **取值范围：** true：只查询没有打标签的资源。 false：查询所有资源。 **默认取值：** 不涉及。
        :type without_any_tag: bool
        """
        
        

        self._matches = None
        self._tags = None
        self._without_any_tag = None
        self.discriminator = None

        if matches is not None:
            self.matches = matches
        if tags is not None:
            self.tags = tags
        if without_any_tag is not None:
            self.without_any_tag = without_any_tag

    @property
    def matches(self):
        r"""Gets the matches of this QueryTmsResourceCountRequest.

        **参数解释：** 匹配项，目前只支持资源名称的模糊匹配。 **约束限制：** 不涉及。

        :return: The matches of this QueryTmsResourceCountRequest.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.TmsMatch`]
        """
        return self._matches

    @matches.setter
    def matches(self, matches):
        r"""Sets the matches of this QueryTmsResourceCountRequest.

        **参数解释：** 匹配项，目前只支持资源名称的模糊匹配。 **约束限制：** 不涉及。

        :param matches: The matches of this QueryTmsResourceCountRequest.
        :type matches: list[:class:`huaweicloudsdkmodelarts.v1.TmsMatch`]
        """
        self._matches = matches

    @property
    def tags(self):
        r"""Gets the tags of this QueryTmsResourceCountRequest.

        **参数解释：** 标签匹配项，只支持多个标签与操作，不携带表示查询所有资源。 **约束限制：** 不涉及。

        :return: The tags of this QueryTmsResourceCountRequest.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.CombineInferTmsTags`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this QueryTmsResourceCountRequest.

        **参数解释：** 标签匹配项，只支持多个标签与操作，不携带表示查询所有资源。 **约束限制：** 不涉及。

        :param tags: The tags of this QueryTmsResourceCountRequest.
        :type tags: list[:class:`huaweicloudsdkmodelarts.v1.CombineInferTmsTags`]
        """
        self._tags = tags

    @property
    def without_any_tag(self):
        r"""Gets the without_any_tag of this QueryTmsResourceCountRequest.

        **参数解释：** 是否只查询没有打标签的资源。 **约束限制：** 不涉及。 **取值范围：** true：只查询没有打标签的资源。 false：查询所有资源。 **默认取值：** 不涉及。

        :return: The without_any_tag of this QueryTmsResourceCountRequest.
        :rtype: bool
        """
        return self._without_any_tag

    @without_any_tag.setter
    def without_any_tag(self, without_any_tag):
        r"""Sets the without_any_tag of this QueryTmsResourceCountRequest.

        **参数解释：** 是否只查询没有打标签的资源。 **约束限制：** 不涉及。 **取值范围：** true：只查询没有打标签的资源。 false：查询所有资源。 **默认取值：** 不涉及。

        :param without_any_tag: The without_any_tag of this QueryTmsResourceCountRequest.
        :type without_any_tag: bool
        """
        self._without_any_tag = without_any_tag

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
        if not isinstance(other, QueryTmsResourceCountRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
