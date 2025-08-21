# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConflictSectionLineMetaDataDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'old_pos': 'int',
        'new_pos': 'int'
    }

    attribute_map = {
        'old_pos': 'old_pos',
        'new_pos': 'new_pos'
    }

    def __init__(self, old_pos=None, new_pos=None):
        r"""ConflictSectionLineMetaDataDto

        The model defined in huaweicloud sdk

        :param old_pos: 旧列位置
        :type old_pos: int
        :param new_pos: 新列位置
        :type new_pos: int
        """
        
        

        self._old_pos = None
        self._new_pos = None
        self.discriminator = None

        if old_pos is not None:
            self.old_pos = old_pos
        if new_pos is not None:
            self.new_pos = new_pos

    @property
    def old_pos(self):
        r"""Gets the old_pos of this ConflictSectionLineMetaDataDto.

        旧列位置

        :return: The old_pos of this ConflictSectionLineMetaDataDto.
        :rtype: int
        """
        return self._old_pos

    @old_pos.setter
    def old_pos(self, old_pos):
        r"""Sets the old_pos of this ConflictSectionLineMetaDataDto.

        旧列位置

        :param old_pos: The old_pos of this ConflictSectionLineMetaDataDto.
        :type old_pos: int
        """
        self._old_pos = old_pos

    @property
    def new_pos(self):
        r"""Gets the new_pos of this ConflictSectionLineMetaDataDto.

        新列位置

        :return: The new_pos of this ConflictSectionLineMetaDataDto.
        :rtype: int
        """
        return self._new_pos

    @new_pos.setter
    def new_pos(self, new_pos):
        r"""Sets the new_pos of this ConflictSectionLineMetaDataDto.

        新列位置

        :param new_pos: The new_pos of this ConflictSectionLineMetaDataDto.
        :type new_pos: int
        """
        self._new_pos = new_pos

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
        if not isinstance(other, ConflictSectionLineMetaDataDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
