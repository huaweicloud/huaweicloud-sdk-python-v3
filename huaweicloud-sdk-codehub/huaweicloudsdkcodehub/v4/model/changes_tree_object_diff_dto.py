# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChangesTreeObjectDiffDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'diff': 'str',
        'new_path': 'str',
        'old_path': 'str',
        'a_mode': 'str',
        'b_mode': 'str',
        'new_file': 'bool',
        'renamed_file': 'bool',
        'deleted_file': 'bool',
        'too_large': 'bool'
    }

    attribute_map = {
        'diff': 'diff',
        'new_path': 'new_path',
        'old_path': 'old_path',
        'a_mode': 'a_mode',
        'b_mode': 'b_mode',
        'new_file': 'new_file',
        'renamed_file': 'renamed_file',
        'deleted_file': 'deleted_file',
        'too_large': 'too_large'
    }

    def __init__(self, diff=None, new_path=None, old_path=None, a_mode=None, b_mode=None, new_file=None, renamed_file=None, deleted_file=None, too_large=None):
        r"""ChangesTreeObjectDiffDto

        The model defined in huaweicloud sdk

        :param diff: **参数解释：** 变更内容。
        :type diff: str
        :param new_path: **参数解释：** 变更新路径。
        :type new_path: str
        :param old_path: **参数解释：** 变更旧。
        :type old_path: str
        :param a_mode: **参数解释：** 旧文件权限。
        :type a_mode: str
        :param b_mode: **参数解释：** 新文件权限。
        :type b_mode: str
        :param new_file: **参数解释：** 是否是新文件。
        :type new_file: bool
        :param renamed_file: **参数解释：** 是否是改名文件。
        :type renamed_file: bool
        :param deleted_file: **参数解释：** 是否是删除文件。
        :type deleted_file: bool
        :param too_large: **参数解释：** 是否内容过长。
        :type too_large: bool
        """
        
        

        self._diff = None
        self._new_path = None
        self._old_path = None
        self._a_mode = None
        self._b_mode = None
        self._new_file = None
        self._renamed_file = None
        self._deleted_file = None
        self._too_large = None
        self.discriminator = None

        if diff is not None:
            self.diff = diff
        if new_path is not None:
            self.new_path = new_path
        if old_path is not None:
            self.old_path = old_path
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
        if too_large is not None:
            self.too_large = too_large

    @property
    def diff(self):
        r"""Gets the diff of this ChangesTreeObjectDiffDto.

        **参数解释：** 变更内容。

        :return: The diff of this ChangesTreeObjectDiffDto.
        :rtype: str
        """
        return self._diff

    @diff.setter
    def diff(self, diff):
        r"""Sets the diff of this ChangesTreeObjectDiffDto.

        **参数解释：** 变更内容。

        :param diff: The diff of this ChangesTreeObjectDiffDto.
        :type diff: str
        """
        self._diff = diff

    @property
    def new_path(self):
        r"""Gets the new_path of this ChangesTreeObjectDiffDto.

        **参数解释：** 变更新路径。

        :return: The new_path of this ChangesTreeObjectDiffDto.
        :rtype: str
        """
        return self._new_path

    @new_path.setter
    def new_path(self, new_path):
        r"""Sets the new_path of this ChangesTreeObjectDiffDto.

        **参数解释：** 变更新路径。

        :param new_path: The new_path of this ChangesTreeObjectDiffDto.
        :type new_path: str
        """
        self._new_path = new_path

    @property
    def old_path(self):
        r"""Gets the old_path of this ChangesTreeObjectDiffDto.

        **参数解释：** 变更旧。

        :return: The old_path of this ChangesTreeObjectDiffDto.
        :rtype: str
        """
        return self._old_path

    @old_path.setter
    def old_path(self, old_path):
        r"""Sets the old_path of this ChangesTreeObjectDiffDto.

        **参数解释：** 变更旧。

        :param old_path: The old_path of this ChangesTreeObjectDiffDto.
        :type old_path: str
        """
        self._old_path = old_path

    @property
    def a_mode(self):
        r"""Gets the a_mode of this ChangesTreeObjectDiffDto.

        **参数解释：** 旧文件权限。

        :return: The a_mode of this ChangesTreeObjectDiffDto.
        :rtype: str
        """
        return self._a_mode

    @a_mode.setter
    def a_mode(self, a_mode):
        r"""Sets the a_mode of this ChangesTreeObjectDiffDto.

        **参数解释：** 旧文件权限。

        :param a_mode: The a_mode of this ChangesTreeObjectDiffDto.
        :type a_mode: str
        """
        self._a_mode = a_mode

    @property
    def b_mode(self):
        r"""Gets the b_mode of this ChangesTreeObjectDiffDto.

        **参数解释：** 新文件权限。

        :return: The b_mode of this ChangesTreeObjectDiffDto.
        :rtype: str
        """
        return self._b_mode

    @b_mode.setter
    def b_mode(self, b_mode):
        r"""Sets the b_mode of this ChangesTreeObjectDiffDto.

        **参数解释：** 新文件权限。

        :param b_mode: The b_mode of this ChangesTreeObjectDiffDto.
        :type b_mode: str
        """
        self._b_mode = b_mode

    @property
    def new_file(self):
        r"""Gets the new_file of this ChangesTreeObjectDiffDto.

        **参数解释：** 是否是新文件。

        :return: The new_file of this ChangesTreeObjectDiffDto.
        :rtype: bool
        """
        return self._new_file

    @new_file.setter
    def new_file(self, new_file):
        r"""Sets the new_file of this ChangesTreeObjectDiffDto.

        **参数解释：** 是否是新文件。

        :param new_file: The new_file of this ChangesTreeObjectDiffDto.
        :type new_file: bool
        """
        self._new_file = new_file

    @property
    def renamed_file(self):
        r"""Gets the renamed_file of this ChangesTreeObjectDiffDto.

        **参数解释：** 是否是改名文件。

        :return: The renamed_file of this ChangesTreeObjectDiffDto.
        :rtype: bool
        """
        return self._renamed_file

    @renamed_file.setter
    def renamed_file(self, renamed_file):
        r"""Sets the renamed_file of this ChangesTreeObjectDiffDto.

        **参数解释：** 是否是改名文件。

        :param renamed_file: The renamed_file of this ChangesTreeObjectDiffDto.
        :type renamed_file: bool
        """
        self._renamed_file = renamed_file

    @property
    def deleted_file(self):
        r"""Gets the deleted_file of this ChangesTreeObjectDiffDto.

        **参数解释：** 是否是删除文件。

        :return: The deleted_file of this ChangesTreeObjectDiffDto.
        :rtype: bool
        """
        return self._deleted_file

    @deleted_file.setter
    def deleted_file(self, deleted_file):
        r"""Sets the deleted_file of this ChangesTreeObjectDiffDto.

        **参数解释：** 是否是删除文件。

        :param deleted_file: The deleted_file of this ChangesTreeObjectDiffDto.
        :type deleted_file: bool
        """
        self._deleted_file = deleted_file

    @property
    def too_large(self):
        r"""Gets the too_large of this ChangesTreeObjectDiffDto.

        **参数解释：** 是否内容过长。

        :return: The too_large of this ChangesTreeObjectDiffDto.
        :rtype: bool
        """
        return self._too_large

    @too_large.setter
    def too_large(self, too_large):
        r"""Sets the too_large of this ChangesTreeObjectDiffDto.

        **参数解释：** 是否内容过长。

        :param too_large: The too_large of this ChangesTreeObjectDiffDto.
        :type too_large: bool
        """
        self._too_large = too_large

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
        if not isinstance(other, ChangesTreeObjectDiffDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
