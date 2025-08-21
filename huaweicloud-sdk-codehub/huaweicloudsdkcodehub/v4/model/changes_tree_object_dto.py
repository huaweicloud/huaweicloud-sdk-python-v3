# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChangesTreeObjectDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'title': 'str',
        'level': 'int',
        'file_path': 'str',
        'file_type': 'str',
        'diff': 'ChangesTreeObjectDiffDto',
        'items': 'list[ChangesTreeObjectDto]'
    }

    attribute_map = {
        'title': 'title',
        'level': 'level',
        'file_path': 'file_path',
        'file_type': 'file_type',
        'diff': 'diff',
        'items': 'items'
    }

    def __init__(self, title=None, level=None, file_path=None, file_type=None, diff=None, items=None):
        r"""ChangesTreeObjectDto

        The model defined in huaweicloud sdk

        :param title: **参数解释：** 变更文件名。
        :type title: str
        :param level: **参数解释：** 文件层级。
        :type level: int
        :param file_path: **参数解释：** 文件路径。
        :type file_path: str
        :param file_type: **参数解释：** 文件类型。
        :type file_type: str
        :param diff: 
        :type diff: :class:`huaweicloudsdkcodehub.v4.ChangesTreeObjectDiffDto`
        :param items: **参数解释：** 子文件变更。
        :type items: list[:class:`huaweicloudsdkcodehub.v4.ChangesTreeObjectDto`]
        """
        
        

        self._title = None
        self._level = None
        self._file_path = None
        self._file_type = None
        self._diff = None
        self._items = None
        self.discriminator = None

        if title is not None:
            self.title = title
        if level is not None:
            self.level = level
        if file_path is not None:
            self.file_path = file_path
        if file_type is not None:
            self.file_type = file_type
        if diff is not None:
            self.diff = diff
        if items is not None:
            self.items = items

    @property
    def title(self):
        r"""Gets the title of this ChangesTreeObjectDto.

        **参数解释：** 变更文件名。

        :return: The title of this ChangesTreeObjectDto.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        r"""Sets the title of this ChangesTreeObjectDto.

        **参数解释：** 变更文件名。

        :param title: The title of this ChangesTreeObjectDto.
        :type title: str
        """
        self._title = title

    @property
    def level(self):
        r"""Gets the level of this ChangesTreeObjectDto.

        **参数解释：** 文件层级。

        :return: The level of this ChangesTreeObjectDto.
        :rtype: int
        """
        return self._level

    @level.setter
    def level(self, level):
        r"""Sets the level of this ChangesTreeObjectDto.

        **参数解释：** 文件层级。

        :param level: The level of this ChangesTreeObjectDto.
        :type level: int
        """
        self._level = level

    @property
    def file_path(self):
        r"""Gets the file_path of this ChangesTreeObjectDto.

        **参数解释：** 文件路径。

        :return: The file_path of this ChangesTreeObjectDto.
        :rtype: str
        """
        return self._file_path

    @file_path.setter
    def file_path(self, file_path):
        r"""Sets the file_path of this ChangesTreeObjectDto.

        **参数解释：** 文件路径。

        :param file_path: The file_path of this ChangesTreeObjectDto.
        :type file_path: str
        """
        self._file_path = file_path

    @property
    def file_type(self):
        r"""Gets the file_type of this ChangesTreeObjectDto.

        **参数解释：** 文件类型。

        :return: The file_type of this ChangesTreeObjectDto.
        :rtype: str
        """
        return self._file_type

    @file_type.setter
    def file_type(self, file_type):
        r"""Sets the file_type of this ChangesTreeObjectDto.

        **参数解释：** 文件类型。

        :param file_type: The file_type of this ChangesTreeObjectDto.
        :type file_type: str
        """
        self._file_type = file_type

    @property
    def diff(self):
        r"""Gets the diff of this ChangesTreeObjectDto.

        :return: The diff of this ChangesTreeObjectDto.
        :rtype: :class:`huaweicloudsdkcodehub.v4.ChangesTreeObjectDiffDto`
        """
        return self._diff

    @diff.setter
    def diff(self, diff):
        r"""Sets the diff of this ChangesTreeObjectDto.

        :param diff: The diff of this ChangesTreeObjectDto.
        :type diff: :class:`huaweicloudsdkcodehub.v4.ChangesTreeObjectDiffDto`
        """
        self._diff = diff

    @property
    def items(self):
        r"""Gets the items of this ChangesTreeObjectDto.

        **参数解释：** 子文件变更。

        :return: The items of this ChangesTreeObjectDto.
        :rtype: list[:class:`huaweicloudsdkcodehub.v4.ChangesTreeObjectDto`]
        """
        return self._items

    @items.setter
    def items(self, items):
        r"""Sets the items of this ChangesTreeObjectDto.

        **参数解释：** 子文件变更。

        :param items: The items of this ChangesTreeObjectDto.
        :type items: list[:class:`huaweicloudsdkcodehub.v4.ChangesTreeObjectDto`]
        """
        self._items = items

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
        if not isinstance(other, ChangesTreeObjectDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
