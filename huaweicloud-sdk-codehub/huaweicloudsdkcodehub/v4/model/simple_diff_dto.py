# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SimpleDiffDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'added_line': 'int',
        'deleted_line': 'int',
        'path': 'str'
    }

    attribute_map = {
        'added_line': 'added_line',
        'deleted_line': 'deleted_line',
        'path': 'path'
    }

    def __init__(self, added_line=None, deleted_line=None, path=None):
        r"""SimpleDiffDto

        The model defined in huaweicloud sdk

        :param added_line: **参数解释：** 增加行数。 **取值范围：** 不涉及。
        :type added_line: int
        :param deleted_line: **参数解释：** 删除行数。 **取值范围：** 不涉及。
        :type deleted_line: int
        :param path: **参数解释：** 路径。 **取值范围：** 不涉及。
        :type path: str
        """
        
        

        self._added_line = None
        self._deleted_line = None
        self._path = None
        self.discriminator = None

        if added_line is not None:
            self.added_line = added_line
        if deleted_line is not None:
            self.deleted_line = deleted_line
        if path is not None:
            self.path = path

    @property
    def added_line(self):
        r"""Gets the added_line of this SimpleDiffDto.

        **参数解释：** 增加行数。 **取值范围：** 不涉及。

        :return: The added_line of this SimpleDiffDto.
        :rtype: int
        """
        return self._added_line

    @added_line.setter
    def added_line(self, added_line):
        r"""Sets the added_line of this SimpleDiffDto.

        **参数解释：** 增加行数。 **取值范围：** 不涉及。

        :param added_line: The added_line of this SimpleDiffDto.
        :type added_line: int
        """
        self._added_line = added_line

    @property
    def deleted_line(self):
        r"""Gets the deleted_line of this SimpleDiffDto.

        **参数解释：** 删除行数。 **取值范围：** 不涉及。

        :return: The deleted_line of this SimpleDiffDto.
        :rtype: int
        """
        return self._deleted_line

    @deleted_line.setter
    def deleted_line(self, deleted_line):
        r"""Sets the deleted_line of this SimpleDiffDto.

        **参数解释：** 删除行数。 **取值范围：** 不涉及。

        :param deleted_line: The deleted_line of this SimpleDiffDto.
        :type deleted_line: int
        """
        self._deleted_line = deleted_line

    @property
    def path(self):
        r"""Gets the path of this SimpleDiffDto.

        **参数解释：** 路径。 **取值范围：** 不涉及。

        :return: The path of this SimpleDiffDto.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        r"""Sets the path of this SimpleDiffDto.

        **参数解释：** 路径。 **取值范围：** 不涉及。

        :param path: The path of this SimpleDiffDto.
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
        if not isinstance(other, SimpleDiffDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
