# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FileDiffDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'old_path': 'str',
        'new_path': 'object',
        'a_mode': 'str',
        'b_mode': 'str',
        'new_file': 'bool',
        'renamed_file': 'bool',
        'deleted_file': 'bool',
        'diff': 'str',
        'too_large': 'bool',
        'added_lines': 'int',
        'removed_lines': 'int'
    }

    attribute_map = {
        'old_path': 'old_path',
        'new_path': 'new_path',
        'a_mode': 'a_mode',
        'b_mode': 'b_mode',
        'new_file': 'new_file',
        'renamed_file': 'renamed_file',
        'deleted_file': 'deleted_file',
        'diff': 'diff',
        'too_large': 'too_large',
        'added_lines': 'added_lines',
        'removed_lines': 'removed_lines'
    }

    def __init__(self, old_path=None, new_path=None, a_mode=None, b_mode=None, new_file=None, renamed_file=None, deleted_file=None, diff=None, too_large=None, added_lines=None, removed_lines=None):
        r"""FileDiffDto

        The model defined in huaweicloud sdk

        :param old_path: **参数解释：** 旧文件名称。 **取值范围：** 字符串长度不少于1，不超过10000。
        :type old_path: str
        :param new_path: **参数解释：** 新文件名称。 **取值范围：** 字符串长度不少于1，不超过10000。
        :type new_path: object
        :param a_mode: **参数解释：** 旧文件权限。
        :type a_mode: str
        :param b_mode: **参数解释：** 新文件权限。
        :type b_mode: str
        :param new_file: **参数解释：** 是否为新文件。 **取值范围：** - true，新文件。 - false，非新文件
        :type new_file: bool
        :param renamed_file: **参数解释：** 是否为重命名文件。 **取值范围：** - true，重命名文件。 - false，非重命名文件
        :type renamed_file: bool
        :param deleted_file: **参数解释：** 是否为被删除文件。 **取值范围：** - true，被删除文件。 - false，非被删除文件
        :type deleted_file: bool
        :param diff: **参数解释：** 差异信息。
        :type diff: str
        :param too_large: **参数解释：** 是否为大文件。 **取值范围：** - true，大文件。 - false，非大文件
        :type too_large: bool
        :param added_lines: **参数解释：** 增加行数。
        :type added_lines: int
        :param removed_lines: **参数解释：** 删除行数。
        :type removed_lines: int
        """
        
        

        self._old_path = None
        self._new_path = None
        self._a_mode = None
        self._b_mode = None
        self._new_file = None
        self._renamed_file = None
        self._deleted_file = None
        self._diff = None
        self._too_large = None
        self._added_lines = None
        self._removed_lines = None
        self.discriminator = None

        if old_path is not None:
            self.old_path = old_path
        if new_path is not None:
            self.new_path = new_path
        if a_mode is not None:
            self.a_mode = a_mode
        if b_mode is not None:
            self.b_mode = b_mode
        if new_file is not None:
            self.new_file = new_file
        if renamed_file is not None:
            self.renamed_file = renamed_file
        if deleted_file is not None:
            self.deleted_file = deleted_file
        if diff is not None:
            self.diff = diff
        if too_large is not None:
            self.too_large = too_large
        if added_lines is not None:
            self.added_lines = added_lines
        if removed_lines is not None:
            self.removed_lines = removed_lines

    @property
    def old_path(self):
        r"""Gets the old_path of this FileDiffDto.

        **参数解释：** 旧文件名称。 **取值范围：** 字符串长度不少于1，不超过10000。

        :return: The old_path of this FileDiffDto.
        :rtype: str
        """
        return self._old_path

    @old_path.setter
    def old_path(self, old_path):
        r"""Sets the old_path of this FileDiffDto.

        **参数解释：** 旧文件名称。 **取值范围：** 字符串长度不少于1，不超过10000。

        :param old_path: The old_path of this FileDiffDto.
        :type old_path: str
        """
        self._old_path = old_path

    @property
    def new_path(self):
        r"""Gets the new_path of this FileDiffDto.

        **参数解释：** 新文件名称。 **取值范围：** 字符串长度不少于1，不超过10000。

        :return: The new_path of this FileDiffDto.
        :rtype: object
        """
        return self._new_path

    @new_path.setter
    def new_path(self, new_path):
        r"""Sets the new_path of this FileDiffDto.

        **参数解释：** 新文件名称。 **取值范围：** 字符串长度不少于1，不超过10000。

        :param new_path: The new_path of this FileDiffDto.
        :type new_path: object
        """
        self._new_path = new_path

    @property
    def a_mode(self):
        r"""Gets the a_mode of this FileDiffDto.

        **参数解释：** 旧文件权限。

        :return: The a_mode of this FileDiffDto.
        :rtype: str
        """
        return self._a_mode

    @a_mode.setter
    def a_mode(self, a_mode):
        r"""Sets the a_mode of this FileDiffDto.

        **参数解释：** 旧文件权限。

        :param a_mode: The a_mode of this FileDiffDto.
        :type a_mode: str
        """
        self._a_mode = a_mode

    @property
    def b_mode(self):
        r"""Gets the b_mode of this FileDiffDto.

        **参数解释：** 新文件权限。

        :return: The b_mode of this FileDiffDto.
        :rtype: str
        """
        return self._b_mode

    @b_mode.setter
    def b_mode(self, b_mode):
        r"""Sets the b_mode of this FileDiffDto.

        **参数解释：** 新文件权限。

        :param b_mode: The b_mode of this FileDiffDto.
        :type b_mode: str
        """
        self._b_mode = b_mode

    @property
    def new_file(self):
        r"""Gets the new_file of this FileDiffDto.

        **参数解释：** 是否为新文件。 **取值范围：** - true，新文件。 - false，非新文件

        :return: The new_file of this FileDiffDto.
        :rtype: bool
        """
        return self._new_file

    @new_file.setter
    def new_file(self, new_file):
        r"""Sets the new_file of this FileDiffDto.

        **参数解释：** 是否为新文件。 **取值范围：** - true，新文件。 - false，非新文件

        :param new_file: The new_file of this FileDiffDto.
        :type new_file: bool
        """
        self._new_file = new_file

    @property
    def renamed_file(self):
        r"""Gets the renamed_file of this FileDiffDto.

        **参数解释：** 是否为重命名文件。 **取值范围：** - true，重命名文件。 - false，非重命名文件

        :return: The renamed_file of this FileDiffDto.
        :rtype: bool
        """
        return self._renamed_file

    @renamed_file.setter
    def renamed_file(self, renamed_file):
        r"""Sets the renamed_file of this FileDiffDto.

        **参数解释：** 是否为重命名文件。 **取值范围：** - true，重命名文件。 - false，非重命名文件

        :param renamed_file: The renamed_file of this FileDiffDto.
        :type renamed_file: bool
        """
        self._renamed_file = renamed_file

    @property
    def deleted_file(self):
        r"""Gets the deleted_file of this FileDiffDto.

        **参数解释：** 是否为被删除文件。 **取值范围：** - true，被删除文件。 - false，非被删除文件

        :return: The deleted_file of this FileDiffDto.
        :rtype: bool
        """
        return self._deleted_file

    @deleted_file.setter
    def deleted_file(self, deleted_file):
        r"""Sets the deleted_file of this FileDiffDto.

        **参数解释：** 是否为被删除文件。 **取值范围：** - true，被删除文件。 - false，非被删除文件

        :param deleted_file: The deleted_file of this FileDiffDto.
        :type deleted_file: bool
        """
        self._deleted_file = deleted_file

    @property
    def diff(self):
        r"""Gets the diff of this FileDiffDto.

        **参数解释：** 差异信息。

        :return: The diff of this FileDiffDto.
        :rtype: str
        """
        return self._diff

    @diff.setter
    def diff(self, diff):
        r"""Sets the diff of this FileDiffDto.

        **参数解释：** 差异信息。

        :param diff: The diff of this FileDiffDto.
        :type diff: str
        """
        self._diff = diff

    @property
    def too_large(self):
        r"""Gets the too_large of this FileDiffDto.

        **参数解释：** 是否为大文件。 **取值范围：** - true，大文件。 - false，非大文件

        :return: The too_large of this FileDiffDto.
        :rtype: bool
        """
        return self._too_large

    @too_large.setter
    def too_large(self, too_large):
        r"""Sets the too_large of this FileDiffDto.

        **参数解释：** 是否为大文件。 **取值范围：** - true，大文件。 - false，非大文件

        :param too_large: The too_large of this FileDiffDto.
        :type too_large: bool
        """
        self._too_large = too_large

    @property
    def added_lines(self):
        r"""Gets the added_lines of this FileDiffDto.

        **参数解释：** 增加行数。

        :return: The added_lines of this FileDiffDto.
        :rtype: int
        """
        return self._added_lines

    @added_lines.setter
    def added_lines(self, added_lines):
        r"""Sets the added_lines of this FileDiffDto.

        **参数解释：** 增加行数。

        :param added_lines: The added_lines of this FileDiffDto.
        :type added_lines: int
        """
        self._added_lines = added_lines

    @property
    def removed_lines(self):
        r"""Gets the removed_lines of this FileDiffDto.

        **参数解释：** 删除行数。

        :return: The removed_lines of this FileDiffDto.
        :rtype: int
        """
        return self._removed_lines

    @removed_lines.setter
    def removed_lines(self, removed_lines):
        r"""Sets the removed_lines of this FileDiffDto.

        **参数解释：** 删除行数。

        :param removed_lines: The removed_lines of this FileDiffDto.
        :type removed_lines: int
        """
        self._removed_lines = removed_lines

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
        if not isinstance(other, FileDiffDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
