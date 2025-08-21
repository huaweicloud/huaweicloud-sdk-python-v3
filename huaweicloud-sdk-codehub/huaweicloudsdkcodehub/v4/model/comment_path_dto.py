# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CommentPathDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'new': 'list[LineDiscussionDto]',
        'old': 'list[LineDiscussionDto]',
        'path': 'str'
    }

    attribute_map = {
        'new': 'new',
        'old': 'old',
        'path': 'path'
    }

    def __init__(self, new=None, old=None, path=None):
        r"""CommentPathDto

        The model defined in huaweicloud sdk

        :param new: **参数解释：** 位于文件对比结果右侧的检视意见集合。
        :type new: list[:class:`huaweicloudsdkcodehub.v4.LineDiscussionDto`]
        :param old: **参数解释：** 位于文件对比结果左侧的检视意见集合。
        :type old: list[:class:`huaweicloudsdkcodehub.v4.LineDiscussionDto`]
        :param path: **参数解释：** 文件名。
        :type path: str
        """
        
        

        self._new = None
        self._old = None
        self._path = None
        self.discriminator = None

        if new is not None:
            self.new = new
        if old is not None:
            self.old = old
        if path is not None:
            self.path = path

    @property
    def new(self):
        r"""Gets the new of this CommentPathDto.

        **参数解释：** 位于文件对比结果右侧的检视意见集合。

        :return: The new of this CommentPathDto.
        :rtype: list[:class:`huaweicloudsdkcodehub.v4.LineDiscussionDto`]
        """
        return self._new

    @new.setter
    def new(self, new):
        r"""Sets the new of this CommentPathDto.

        **参数解释：** 位于文件对比结果右侧的检视意见集合。

        :param new: The new of this CommentPathDto.
        :type new: list[:class:`huaweicloudsdkcodehub.v4.LineDiscussionDto`]
        """
        self._new = new

    @property
    def old(self):
        r"""Gets the old of this CommentPathDto.

        **参数解释：** 位于文件对比结果左侧的检视意见集合。

        :return: The old of this CommentPathDto.
        :rtype: list[:class:`huaweicloudsdkcodehub.v4.LineDiscussionDto`]
        """
        return self._old

    @old.setter
    def old(self, old):
        r"""Sets the old of this CommentPathDto.

        **参数解释：** 位于文件对比结果左侧的检视意见集合。

        :param old: The old of this CommentPathDto.
        :type old: list[:class:`huaweicloudsdkcodehub.v4.LineDiscussionDto`]
        """
        self._old = old

    @property
    def path(self):
        r"""Gets the path of this CommentPathDto.

        **参数解释：** 文件名。

        :return: The path of this CommentPathDto.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        r"""Sets the path of this CommentPathDto.

        **参数解释：** 文件名。

        :param path: The path of this CommentPathDto.
        :type path: str
        """
        self._path = path

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
        if not isinstance(other, CommentPathDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
