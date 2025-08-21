# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DiffDto:

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
        'new_path': 'str',
        'a_mode': 'str',
        'b_mode': 'str',
        'file_path': 'str',
        'new_file': 'bool',
        'file_type': 'str',
        'renamed_file': 'bool',
        'deleted_file': 'bool',
        'diff': 'str',
        'binary': 'bool',
        'too_large': 'bool',
        'collapsed': 'bool',
        'line_count': 'list[int]',
        'added_lines': 'int',
        'removed_lines': 'int'
    }

    attribute_map = {
        'old_path': 'old_path',
        'new_path': 'new_path',
        'a_mode': 'a_mode',
        'b_mode': 'b_mode',
        'file_path': 'file_path',
        'new_file': 'new_file',
        'file_type': 'file_type',
        'renamed_file': 'renamed_file',
        'deleted_file': 'deleted_file',
        'diff': 'diff',
        'binary': 'binary',
        'too_large': 'too_large',
        'collapsed': 'collapsed',
        'line_count': 'line_count',
        'added_lines': 'added_lines',
        'removed_lines': 'removed_lines'
    }

    def __init__(self, old_path=None, new_path=None, a_mode=None, b_mode=None, file_path=None, new_file=None, file_type=None, renamed_file=None, deleted_file=None, diff=None, binary=None, too_large=None, collapsed=None, line_count=None, added_lines=None, removed_lines=None):
        r"""DiffDto

        The model defined in huaweicloud sdk

        :param old_path: 旧文件
        :type old_path: str
        :param new_path: 新文件
        :type new_path: str
        :param a_mode: 旧文件类型
        :type a_mode: str
        :param b_mode: 新文件类型
        :type b_mode: str
        :param file_path: 文件路径
        :type file_path: str
        :param new_file: 是否新增
        :type new_file: bool
        :param file_type: 文件类型
        :type file_type: str
        :param renamed_file: 是否重命名
        :type renamed_file: bool
        :param deleted_file: 是否删除文件
        :type deleted_file: bool
        :param diff: 比较结果
        :type diff: str
        :param binary: 是否二进制
        :type binary: bool
        :param too_large: 是否过大
        :type too_large: bool
        :param collapsed: 是否折叠
        :type collapsed: bool
        :param line_count: 
        :type line_count: list[int]
        :param added_lines: 增加行数
        :type added_lines: int
        :param removed_lines: 删除行数
        :type removed_lines: int
        """
        
        

        self._old_path = None
        self._new_path = None
        self._a_mode = None
        self._b_mode = None
        self._file_path = None
        self._new_file = None
        self._file_type = None
        self._renamed_file = None
        self._deleted_file = None
        self._diff = None
        self._binary = None
        self._too_large = None
        self._collapsed = None
        self._line_count = None
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
        if file_path is not None:
            self.file_path = file_path
        if new_file is not None:
            self.new_file = new_file
        if file_type is not None:
            self.file_type = file_type
        if renamed_file is not None:
            self.renamed_file = renamed_file
        if deleted_file is not None:
            self.deleted_file = deleted_file
        if diff is not None:
            self.diff = diff
        if binary is not None:
            self.binary = binary
        if too_large is not None:
            self.too_large = too_large
        if collapsed is not None:
            self.collapsed = collapsed
        if line_count is not None:
            self.line_count = line_count
        if added_lines is not None:
            self.added_lines = added_lines
        if removed_lines is not None:
            self.removed_lines = removed_lines

    @property
    def old_path(self):
        r"""Gets the old_path of this DiffDto.

        旧文件

        :return: The old_path of this DiffDto.
        :rtype: str
        """
        return self._old_path

    @old_path.setter
    def old_path(self, old_path):
        r"""Sets the old_path of this DiffDto.

        旧文件

        :param old_path: The old_path of this DiffDto.
        :type old_path: str
        """
        self._old_path = old_path

    @property
    def new_path(self):
        r"""Gets the new_path of this DiffDto.

        新文件

        :return: The new_path of this DiffDto.
        :rtype: str
        """
        return self._new_path

    @new_path.setter
    def new_path(self, new_path):
        r"""Sets the new_path of this DiffDto.

        新文件

        :param new_path: The new_path of this DiffDto.
        :type new_path: str
        """
        self._new_path = new_path

    @property
    def a_mode(self):
        r"""Gets the a_mode of this DiffDto.

        旧文件类型

        :return: The a_mode of this DiffDto.
        :rtype: str
        """
        return self._a_mode

    @a_mode.setter
    def a_mode(self, a_mode):
        r"""Sets the a_mode of this DiffDto.

        旧文件类型

        :param a_mode: The a_mode of this DiffDto.
        :type a_mode: str
        """
        self._a_mode = a_mode

    @property
    def b_mode(self):
        r"""Gets the b_mode of this DiffDto.

        新文件类型

        :return: The b_mode of this DiffDto.
        :rtype: str
        """
        return self._b_mode

    @b_mode.setter
    def b_mode(self, b_mode):
        r"""Sets the b_mode of this DiffDto.

        新文件类型

        :param b_mode: The b_mode of this DiffDto.
        :type b_mode: str
        """
        self._b_mode = b_mode

    @property
    def file_path(self):
        r"""Gets the file_path of this DiffDto.

        文件路径

        :return: The file_path of this DiffDto.
        :rtype: str
        """
        return self._file_path

    @file_path.setter
    def file_path(self, file_path):
        r"""Sets the file_path of this DiffDto.

        文件路径

        :param file_path: The file_path of this DiffDto.
        :type file_path: str
        """
        self._file_path = file_path

    @property
    def new_file(self):
        r"""Gets the new_file of this DiffDto.

        是否新增

        :return: The new_file of this DiffDto.
        :rtype: bool
        """
        return self._new_file

    @new_file.setter
    def new_file(self, new_file):
        r"""Sets the new_file of this DiffDto.

        是否新增

        :param new_file: The new_file of this DiffDto.
        :type new_file: bool
        """
        self._new_file = new_file

    @property
    def file_type(self):
        r"""Gets the file_type of this DiffDto.

        文件类型

        :return: The file_type of this DiffDto.
        :rtype: str
        """
        return self._file_type

    @file_type.setter
    def file_type(self, file_type):
        r"""Sets the file_type of this DiffDto.

        文件类型

        :param file_type: The file_type of this DiffDto.
        :type file_type: str
        """
        self._file_type = file_type

    @property
    def renamed_file(self):
        r"""Gets the renamed_file of this DiffDto.

        是否重命名

        :return: The renamed_file of this DiffDto.
        :rtype: bool
        """
        return self._renamed_file

    @renamed_file.setter
    def renamed_file(self, renamed_file):
        r"""Sets the renamed_file of this DiffDto.

        是否重命名

        :param renamed_file: The renamed_file of this DiffDto.
        :type renamed_file: bool
        """
        self._renamed_file = renamed_file

    @property
    def deleted_file(self):
        r"""Gets the deleted_file of this DiffDto.

        是否删除文件

        :return: The deleted_file of this DiffDto.
        :rtype: bool
        """
        return self._deleted_file

    @deleted_file.setter
    def deleted_file(self, deleted_file):
        r"""Sets the deleted_file of this DiffDto.

        是否删除文件

        :param deleted_file: The deleted_file of this DiffDto.
        :type deleted_file: bool
        """
        self._deleted_file = deleted_file

    @property
    def diff(self):
        r"""Gets the diff of this DiffDto.

        比较结果

        :return: The diff of this DiffDto.
        :rtype: str
        """
        return self._diff

    @diff.setter
    def diff(self, diff):
        r"""Sets the diff of this DiffDto.

        比较结果

        :param diff: The diff of this DiffDto.
        :type diff: str
        """
        self._diff = diff

    @property
    def binary(self):
        r"""Gets the binary of this DiffDto.

        是否二进制

        :return: The binary of this DiffDto.
        :rtype: bool
        """
        return self._binary

    @binary.setter
    def binary(self, binary):
        r"""Sets the binary of this DiffDto.

        是否二进制

        :param binary: The binary of this DiffDto.
        :type binary: bool
        """
        self._binary = binary

    @property
    def too_large(self):
        r"""Gets the too_large of this DiffDto.

        是否过大

        :return: The too_large of this DiffDto.
        :rtype: bool
        """
        return self._too_large

    @too_large.setter
    def too_large(self, too_large):
        r"""Sets the too_large of this DiffDto.

        是否过大

        :param too_large: The too_large of this DiffDto.
        :type too_large: bool
        """
        self._too_large = too_large

    @property
    def collapsed(self):
        r"""Gets the collapsed of this DiffDto.

        是否折叠

        :return: The collapsed of this DiffDto.
        :rtype: bool
        """
        return self._collapsed

    @collapsed.setter
    def collapsed(self, collapsed):
        r"""Sets the collapsed of this DiffDto.

        是否折叠

        :param collapsed: The collapsed of this DiffDto.
        :type collapsed: bool
        """
        self._collapsed = collapsed

    @property
    def line_count(self):
        r"""Gets the line_count of this DiffDto.

        :return: The line_count of this DiffDto.
        :rtype: list[int]
        """
        return self._line_count

    @line_count.setter
    def line_count(self, line_count):
        r"""Sets the line_count of this DiffDto.

        :param line_count: The line_count of this DiffDto.
        :type line_count: list[int]
        """
        self._line_count = line_count

    @property
    def added_lines(self):
        r"""Gets the added_lines of this DiffDto.

        增加行数

        :return: The added_lines of this DiffDto.
        :rtype: int
        """
        return self._added_lines

    @added_lines.setter
    def added_lines(self, added_lines):
        r"""Sets the added_lines of this DiffDto.

        增加行数

        :param added_lines: The added_lines of this DiffDto.
        :type added_lines: int
        """
        self._added_lines = added_lines

    @property
    def removed_lines(self):
        r"""Gets the removed_lines of this DiffDto.

        删除行数

        :return: The removed_lines of this DiffDto.
        :rtype: int
        """
        return self._removed_lines

    @removed_lines.setter
    def removed_lines(self, removed_lines):
        r"""Sets the removed_lines of this DiffDto.

        删除行数

        :param removed_lines: The removed_lines of this DiffDto.
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
        if not isinstance(other, DiffDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
