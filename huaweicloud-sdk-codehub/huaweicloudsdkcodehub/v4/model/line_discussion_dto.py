# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LineDiscussionDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'discussions': 'list[MergeRequestBasicDiscussionDto]',
        'line': 'int',
        'type': 'str'
    }

    attribute_map = {
        'discussions': 'discussions',
        'line': 'line',
        'type': 'type'
    }

    def __init__(self, discussions=None, line=None, type=None):
        r"""LineDiscussionDto

        The model defined in huaweicloud sdk

        :param discussions: **参数解释：** 位于某一侧某行的检视意见集合。
        :type discussions: list[:class:`huaweicloudsdkcodehub.v4.MergeRequestBasicDiscussionDto`]
        :param line: **参数解释：** 所在的行号。
        :type line: int
        :param type: **参数解释：** 所在的行的类型。 old: 左侧删除行。 new: 右侧新增行。 unchanged-l: 左侧不变行。 unchanged-r: 右侧不变行。
        :type type: str
        """
        
        

        self._discussions = None
        self._line = None
        self._type = None
        self.discriminator = None

        if discussions is not None:
            self.discussions = discussions
        if line is not None:
            self.line = line
        if type is not None:
            self.type = type

    @property
    def discussions(self):
        r"""Gets the discussions of this LineDiscussionDto.

        **参数解释：** 位于某一侧某行的检视意见集合。

        :return: The discussions of this LineDiscussionDto.
        :rtype: list[:class:`huaweicloudsdkcodehub.v4.MergeRequestBasicDiscussionDto`]
        """
        return self._discussions

    @discussions.setter
    def discussions(self, discussions):
        r"""Sets the discussions of this LineDiscussionDto.

        **参数解释：** 位于某一侧某行的检视意见集合。

        :param discussions: The discussions of this LineDiscussionDto.
        :type discussions: list[:class:`huaweicloudsdkcodehub.v4.MergeRequestBasicDiscussionDto`]
        """
        self._discussions = discussions

    @property
    def line(self):
        r"""Gets the line of this LineDiscussionDto.

        **参数解释：** 所在的行号。

        :return: The line of this LineDiscussionDto.
        :rtype: int
        """
        return self._line

    @line.setter
    def line(self, line):
        r"""Sets the line of this LineDiscussionDto.

        **参数解释：** 所在的行号。

        :param line: The line of this LineDiscussionDto.
        :type line: int
        """
        self._line = line

    @property
    def type(self):
        r"""Gets the type of this LineDiscussionDto.

        **参数解释：** 所在的行的类型。 old: 左侧删除行。 new: 右侧新增行。 unchanged-l: 左侧不变行。 unchanged-r: 右侧不变行。

        :return: The type of this LineDiscussionDto.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this LineDiscussionDto.

        **参数解释：** 所在的行的类型。 old: 左侧删除行。 new: 右侧新增行。 unchanged-l: 左侧不变行。 unchanged-r: 右侧不变行。

        :param type: The type of this LineDiscussionDto.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, LineDiscussionDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
