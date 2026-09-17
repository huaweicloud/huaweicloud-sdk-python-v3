# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CommentResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total': 'int',
        'comment_list': 'list[CommentEntity]'
    }

    attribute_map = {
        'total': 'total',
        'comment_list': 'comment_list'
    }

    def __init__(self, total=None, comment_list=None):
        r"""CommentResult

        The model defined in huaweicloud sdk

        :param total: **参数解释**： 符合过滤条件的工作项评论总数。 **取值范围**： 不涉及。
        :type total: int
        :param comment_list: **参数解释**： 工作项评论列表。 **取值范围**： 不涉及。
        :type comment_list: list[:class:`huaweicloudsdkprojectman.v4.CommentEntity`]
        """
        
        

        self._total = None
        self._comment_list = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if comment_list is not None:
            self.comment_list = comment_list

    @property
    def total(self):
        r"""Gets the total of this CommentResult.

        **参数解释**： 符合过滤条件的工作项评论总数。 **取值范围**： 不涉及。

        :return: The total of this CommentResult.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this CommentResult.

        **参数解释**： 符合过滤条件的工作项评论总数。 **取值范围**： 不涉及。

        :param total: The total of this CommentResult.
        :type total: int
        """
        self._total = total

    @property
    def comment_list(self):
        r"""Gets the comment_list of this CommentResult.

        **参数解释**： 工作项评论列表。 **取值范围**： 不涉及。

        :return: The comment_list of this CommentResult.
        :rtype: list[:class:`huaweicloudsdkprojectman.v4.CommentEntity`]
        """
        return self._comment_list

    @comment_list.setter
    def comment_list(self, comment_list):
        r"""Sets the comment_list of this CommentResult.

        **参数解释**： 工作项评论列表。 **取值范围**： 不涉及。

        :param comment_list: The comment_list of this CommentResult.
        :type comment_list: list[:class:`huaweicloudsdkprojectman.v4.CommentEntity`]
        """
        self._comment_list = comment_list

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
        if not isinstance(other, CommentResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
