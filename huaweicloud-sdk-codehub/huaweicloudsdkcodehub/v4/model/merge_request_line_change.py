# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MergeRequestLineChange:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'added_lines': 'int',
        'removed_lines': 'int'
    }

    attribute_map = {
        'added_lines': 'added_lines',
        'removed_lines': 'removed_lines'
    }

    def __init__(self, added_lines=None, removed_lines=None):
        r"""MergeRequestLineChange

        The model defined in huaweicloud sdk

        :param added_lines: 合并请求新增代码行数
        :type added_lines: int
        :param removed_lines: 合并请求删除代码行数
        :type removed_lines: int
        """
        
        

        self._added_lines = None
        self._removed_lines = None
        self.discriminator = None

        if added_lines is not None:
            self.added_lines = added_lines
        if removed_lines is not None:
            self.removed_lines = removed_lines

    @property
    def added_lines(self):
        r"""Gets the added_lines of this MergeRequestLineChange.

        合并请求新增代码行数

        :return: The added_lines of this MergeRequestLineChange.
        :rtype: int
        """
        return self._added_lines

    @added_lines.setter
    def added_lines(self, added_lines):
        r"""Sets the added_lines of this MergeRequestLineChange.

        合并请求新增代码行数

        :param added_lines: The added_lines of this MergeRequestLineChange.
        :type added_lines: int
        """
        self._added_lines = added_lines

    @property
    def removed_lines(self):
        r"""Gets the removed_lines of this MergeRequestLineChange.

        合并请求删除代码行数

        :return: The removed_lines of this MergeRequestLineChange.
        :rtype: int
        """
        return self._removed_lines

    @removed_lines.setter
    def removed_lines(self, removed_lines):
        r"""Sets the removed_lines of this MergeRequestLineChange.

        合并请求删除代码行数

        :param removed_lines: The removed_lines of this MergeRequestLineChange.
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
        if not isinstance(other, MergeRequestLineChange):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
