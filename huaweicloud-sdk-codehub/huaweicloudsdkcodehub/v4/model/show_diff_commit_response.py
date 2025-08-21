# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDiffCommitResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'diffs': 'list[DiffNoLineDto]',
        'diff_refs': 'DiffRefsDto',
        'added_lines': 'int',
        'removed_lines': 'int',
        'change_file_count': 'int',
        'change_line_count': 'int',
        'too_large': 'bool'
    }

    attribute_map = {
        'diffs': 'diffs',
        'diff_refs': 'diff_refs',
        'added_lines': 'added_lines',
        'removed_lines': 'removed_lines',
        'change_file_count': 'change_file_count',
        'change_line_count': 'change_line_count',
        'too_large': 'too_large'
    }

    def __init__(self, diffs=None, diff_refs=None, added_lines=None, removed_lines=None, change_file_count=None, change_line_count=None, too_large=None):
        r"""ShowDiffCommitResponse

        The model defined in huaweicloud sdk

        :param diffs: **参数解释：** 差异信息。 **取值范围：** 不涉及。
        :type diffs: list[:class:`huaweicloudsdkcodehub.v4.DiffNoLineDto`]
        :param diff_refs: 
        :type diff_refs: :class:`huaweicloudsdkcodehub.v4.DiffRefsDto`
        :param added_lines: **参数解释：** 增加行数。 **取值范围：** 不涉及。
        :type added_lines: int
        :param removed_lines: **参数解释：** 删除行数。 **取值范围：** 不涉及。
        :type removed_lines: int
        :param change_file_count: **参数解释：** 更改文件数目。 **取值范围：** 不涉及。
        :type change_file_count: int
        :param change_line_count: **参数解释：** 更改行数。 **取值范围：** 不涉及。
        :type change_line_count: int
        :param too_large: **参数解释：** 是否过大。 **取值范围：** - true，大文件。 - false，非大文件
        :type too_large: bool
        """
        
        super(ShowDiffCommitResponse, self).__init__()

        self._diffs = None
        self._diff_refs = None
        self._added_lines = None
        self._removed_lines = None
        self._change_file_count = None
        self._change_line_count = None
        self._too_large = None
        self.discriminator = None

        if diffs is not None:
            self.diffs = diffs
        if diff_refs is not None:
            self.diff_refs = diff_refs
        if added_lines is not None:
            self.added_lines = added_lines
        if removed_lines is not None:
            self.removed_lines = removed_lines
        if change_file_count is not None:
            self.change_file_count = change_file_count
        if change_line_count is not None:
            self.change_line_count = change_line_count
        if too_large is not None:
            self.too_large = too_large

    @property
    def diffs(self):
        r"""Gets the diffs of this ShowDiffCommitResponse.

        **参数解释：** 差异信息。 **取值范围：** 不涉及。

        :return: The diffs of this ShowDiffCommitResponse.
        :rtype: list[:class:`huaweicloudsdkcodehub.v4.DiffNoLineDto`]
        """
        return self._diffs

    @diffs.setter
    def diffs(self, diffs):
        r"""Sets the diffs of this ShowDiffCommitResponse.

        **参数解释：** 差异信息。 **取值范围：** 不涉及。

        :param diffs: The diffs of this ShowDiffCommitResponse.
        :type diffs: list[:class:`huaweicloudsdkcodehub.v4.DiffNoLineDto`]
        """
        self._diffs = diffs

    @property
    def diff_refs(self):
        r"""Gets the diff_refs of this ShowDiffCommitResponse.

        :return: The diff_refs of this ShowDiffCommitResponse.
        :rtype: :class:`huaweicloudsdkcodehub.v4.DiffRefsDto`
        """
        return self._diff_refs

    @diff_refs.setter
    def diff_refs(self, diff_refs):
        r"""Sets the diff_refs of this ShowDiffCommitResponse.

        :param diff_refs: The diff_refs of this ShowDiffCommitResponse.
        :type diff_refs: :class:`huaweicloudsdkcodehub.v4.DiffRefsDto`
        """
        self._diff_refs = diff_refs

    @property
    def added_lines(self):
        r"""Gets the added_lines of this ShowDiffCommitResponse.

        **参数解释：** 增加行数。 **取值范围：** 不涉及。

        :return: The added_lines of this ShowDiffCommitResponse.
        :rtype: int
        """
        return self._added_lines

    @added_lines.setter
    def added_lines(self, added_lines):
        r"""Sets the added_lines of this ShowDiffCommitResponse.

        **参数解释：** 增加行数。 **取值范围：** 不涉及。

        :param added_lines: The added_lines of this ShowDiffCommitResponse.
        :type added_lines: int
        """
        self._added_lines = added_lines

    @property
    def removed_lines(self):
        r"""Gets the removed_lines of this ShowDiffCommitResponse.

        **参数解释：** 删除行数。 **取值范围：** 不涉及。

        :return: The removed_lines of this ShowDiffCommitResponse.
        :rtype: int
        """
        return self._removed_lines

    @removed_lines.setter
    def removed_lines(self, removed_lines):
        r"""Sets the removed_lines of this ShowDiffCommitResponse.

        **参数解释：** 删除行数。 **取值范围：** 不涉及。

        :param removed_lines: The removed_lines of this ShowDiffCommitResponse.
        :type removed_lines: int
        """
        self._removed_lines = removed_lines

    @property
    def change_file_count(self):
        r"""Gets the change_file_count of this ShowDiffCommitResponse.

        **参数解释：** 更改文件数目。 **取值范围：** 不涉及。

        :return: The change_file_count of this ShowDiffCommitResponse.
        :rtype: int
        """
        return self._change_file_count

    @change_file_count.setter
    def change_file_count(self, change_file_count):
        r"""Sets the change_file_count of this ShowDiffCommitResponse.

        **参数解释：** 更改文件数目。 **取值范围：** 不涉及。

        :param change_file_count: The change_file_count of this ShowDiffCommitResponse.
        :type change_file_count: int
        """
        self._change_file_count = change_file_count

    @property
    def change_line_count(self):
        r"""Gets the change_line_count of this ShowDiffCommitResponse.

        **参数解释：** 更改行数。 **取值范围：** 不涉及。

        :return: The change_line_count of this ShowDiffCommitResponse.
        :rtype: int
        """
        return self._change_line_count

    @change_line_count.setter
    def change_line_count(self, change_line_count):
        r"""Sets the change_line_count of this ShowDiffCommitResponse.

        **参数解释：** 更改行数。 **取值范围：** 不涉及。

        :param change_line_count: The change_line_count of this ShowDiffCommitResponse.
        :type change_line_count: int
        """
        self._change_line_count = change_line_count

    @property
    def too_large(self):
        r"""Gets the too_large of this ShowDiffCommitResponse.

        **参数解释：** 是否过大。 **取值范围：** - true，大文件。 - false，非大文件

        :return: The too_large of this ShowDiffCommitResponse.
        :rtype: bool
        """
        return self._too_large

    @too_large.setter
    def too_large(self, too_large):
        r"""Sets the too_large of this ShowDiffCommitResponse.

        **参数解释：** 是否过大。 **取值范围：** - true，大文件。 - false，非大文件

        :param too_large: The too_large of this ShowDiffCommitResponse.
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
        if not isinstance(other, ShowDiffCommitResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
