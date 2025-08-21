# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NoteRequiredAttributeDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'note_required_attributes': 'list[RequiredAttributeDto]'
    }

    attribute_map = {
        'note_required_attributes': 'note_required_attributes'
    }

    def __init__(self, note_required_attributes=None):
        r"""NoteRequiredAttributeDto

        The model defined in huaweicloud sdk

        :param note_required_attributes: **参数解释：** 检视意见必填项。
        :type note_required_attributes: list[:class:`huaweicloudsdkcodehub.v4.RequiredAttributeDto`]
        """
        
        

        self._note_required_attributes = None
        self.discriminator = None

        if note_required_attributes is not None:
            self.note_required_attributes = note_required_attributes

    @property
    def note_required_attributes(self):
        r"""Gets the note_required_attributes of this NoteRequiredAttributeDto.

        **参数解释：** 检视意见必填项。

        :return: The note_required_attributes of this NoteRequiredAttributeDto.
        :rtype: list[:class:`huaweicloudsdkcodehub.v4.RequiredAttributeDto`]
        """
        return self._note_required_attributes

    @note_required_attributes.setter
    def note_required_attributes(self, note_required_attributes):
        r"""Sets the note_required_attributes of this NoteRequiredAttributeDto.

        **参数解释：** 检视意见必填项。

        :param note_required_attributes: The note_required_attributes of this NoteRequiredAttributeDto.
        :type note_required_attributes: list[:class:`huaweicloudsdkcodehub.v4.RequiredAttributeDto`]
        """
        self._note_required_attributes = note_required_attributes

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
        if not isinstance(other, NoteRequiredAttributeDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
