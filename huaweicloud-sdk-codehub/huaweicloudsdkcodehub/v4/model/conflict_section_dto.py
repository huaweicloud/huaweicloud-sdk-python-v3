# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConflictSectionDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'conflict': 'bool',
        'lines': 'list[ConflictSectionLineDto]',
        'id': 'str'
    }

    attribute_map = {
        'conflict': 'conflict',
        'lines': 'lines',
        'id': 'id'
    }

    def __init__(self, conflict=None, lines=None, id=None):
        r"""ConflictSectionDto

        The model defined in huaweicloud sdk

        :param conflict: 是否冲突
        :type conflict: bool
        :param lines: 冲突行列表
        :type lines: list[:class:`huaweicloudsdkcodehub.v4.ConflictSectionLineDto`]
        :param id: 编号
        :type id: str
        """
        
        

        self._conflict = None
        self._lines = None
        self._id = None
        self.discriminator = None

        if conflict is not None:
            self.conflict = conflict
        if lines is not None:
            self.lines = lines
        if id is not None:
            self.id = id

    @property
    def conflict(self):
        r"""Gets the conflict of this ConflictSectionDto.

        是否冲突

        :return: The conflict of this ConflictSectionDto.
        :rtype: bool
        """
        return self._conflict

    @conflict.setter
    def conflict(self, conflict):
        r"""Sets the conflict of this ConflictSectionDto.

        是否冲突

        :param conflict: The conflict of this ConflictSectionDto.
        :type conflict: bool
        """
        self._conflict = conflict

    @property
    def lines(self):
        r"""Gets the lines of this ConflictSectionDto.

        冲突行列表

        :return: The lines of this ConflictSectionDto.
        :rtype: list[:class:`huaweicloudsdkcodehub.v4.ConflictSectionLineDto`]
        """
        return self._lines

    @lines.setter
    def lines(self, lines):
        r"""Sets the lines of this ConflictSectionDto.

        冲突行列表

        :param lines: The lines of this ConflictSectionDto.
        :type lines: list[:class:`huaweicloudsdkcodehub.v4.ConflictSectionLineDto`]
        """
        self._lines = lines

    @property
    def id(self):
        r"""Gets the id of this ConflictSectionDto.

        编号

        :return: The id of this ConflictSectionDto.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ConflictSectionDto.

        编号

        :param id: The id of this ConflictSectionDto.
        :type id: str
        """
        self._id = id

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
        if not isinstance(other, ConflictSectionDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
