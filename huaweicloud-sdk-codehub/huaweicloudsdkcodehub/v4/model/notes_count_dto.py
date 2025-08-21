# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NotesCountDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'notes_count': 'int',
        'unresolved_notes_count': 'int',
        'already_resolved_count': 'int',
        'need_resolved_count': 'int'
    }

    attribute_map = {
        'notes_count': 'notes_count',
        'unresolved_notes_count': 'unresolved_notes_count',
        'already_resolved_count': 'already_resolved_count',
        'need_resolved_count': 'need_resolved_count'
    }

    def __init__(self, notes_count=None, unresolved_notes_count=None, already_resolved_count=None, need_resolved_count=None):
        r"""NotesCountDto

        The model defined in huaweicloud sdk

        :param notes_count: 检视意见总数
        :type notes_count: int
        :param unresolved_notes_count: 未解决的检视意见数量
        :type unresolved_notes_count: int
        :param already_resolved_count: 已解决的检视意见数量
        :type already_resolved_count: int
        :param need_resolved_count: 需要解决的检视意见总数
        :type need_resolved_count: int
        """
        
        

        self._notes_count = None
        self._unresolved_notes_count = None
        self._already_resolved_count = None
        self._need_resolved_count = None
        self.discriminator = None

        if notes_count is not None:
            self.notes_count = notes_count
        if unresolved_notes_count is not None:
            self.unresolved_notes_count = unresolved_notes_count
        if already_resolved_count is not None:
            self.already_resolved_count = already_resolved_count
        if need_resolved_count is not None:
            self.need_resolved_count = need_resolved_count

    @property
    def notes_count(self):
        r"""Gets the notes_count of this NotesCountDto.

        检视意见总数

        :return: The notes_count of this NotesCountDto.
        :rtype: int
        """
        return self._notes_count

    @notes_count.setter
    def notes_count(self, notes_count):
        r"""Sets the notes_count of this NotesCountDto.

        检视意见总数

        :param notes_count: The notes_count of this NotesCountDto.
        :type notes_count: int
        """
        self._notes_count = notes_count

    @property
    def unresolved_notes_count(self):
        r"""Gets the unresolved_notes_count of this NotesCountDto.

        未解决的检视意见数量

        :return: The unresolved_notes_count of this NotesCountDto.
        :rtype: int
        """
        return self._unresolved_notes_count

    @unresolved_notes_count.setter
    def unresolved_notes_count(self, unresolved_notes_count):
        r"""Sets the unresolved_notes_count of this NotesCountDto.

        未解决的检视意见数量

        :param unresolved_notes_count: The unresolved_notes_count of this NotesCountDto.
        :type unresolved_notes_count: int
        """
        self._unresolved_notes_count = unresolved_notes_count

    @property
    def already_resolved_count(self):
        r"""Gets the already_resolved_count of this NotesCountDto.

        已解决的检视意见数量

        :return: The already_resolved_count of this NotesCountDto.
        :rtype: int
        """
        return self._already_resolved_count

    @already_resolved_count.setter
    def already_resolved_count(self, already_resolved_count):
        r"""Sets the already_resolved_count of this NotesCountDto.

        已解决的检视意见数量

        :param already_resolved_count: The already_resolved_count of this NotesCountDto.
        :type already_resolved_count: int
        """
        self._already_resolved_count = already_resolved_count

    @property
    def need_resolved_count(self):
        r"""Gets the need_resolved_count of this NotesCountDto.

        需要解决的检视意见总数

        :return: The need_resolved_count of this NotesCountDto.
        :rtype: int
        """
        return self._need_resolved_count

    @need_resolved_count.setter
    def need_resolved_count(self, need_resolved_count):
        r"""Sets the need_resolved_count of this NotesCountDto.

        需要解决的检视意见总数

        :param need_resolved_count: The need_resolved_count of this NotesCountDto.
        :type need_resolved_count: int
        """
        self._need_resolved_count = need_resolved_count

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
        if not isinstance(other, NotesCountDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
