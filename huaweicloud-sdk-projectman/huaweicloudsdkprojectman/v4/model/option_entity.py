# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OptionEntity:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'code': 'str',
        'display_value': 'str',
        'value': 'str',
        'level': 'int',
        'sequence': 'int',
        'parent_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'code': 'code',
        'display_value': 'display_value',
        'value': 'value',
        'level': 'level',
        'sequence': 'sequence',
        'parent_id': 'parent_id'
    }

    def __init__(self, id=None, code=None, display_value=None, value=None, level=None, sequence=None, parent_id=None):
        r"""OptionEntity

        The model defined in huaweicloud sdk

        :param id: 选项id
        :type id: str
        :param code: 选项code值
        :type code: str
        :param display_value: 选项显示名称
        :type display_value: str
        :param value: 选项唯一标识
        :type value: str
        :param level: 选项层级。用于区分层级字段的层级
        :type level: int
        :param sequence: 选项顺序
        :type sequence: int
        :param parent_id: 父选项id
        :type parent_id: str
        """
        
        

        self._id = None
        self._code = None
        self._display_value = None
        self._value = None
        self._level = None
        self._sequence = None
        self._parent_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if code is not None:
            self.code = code
        if display_value is not None:
            self.display_value = display_value
        if value is not None:
            self.value = value
        if level is not None:
            self.level = level
        if sequence is not None:
            self.sequence = sequence
        if parent_id is not None:
            self.parent_id = parent_id

    @property
    def id(self):
        r"""Gets the id of this OptionEntity.

        选项id

        :return: The id of this OptionEntity.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this OptionEntity.

        选项id

        :param id: The id of this OptionEntity.
        :type id: str
        """
        self._id = id

    @property
    def code(self):
        r"""Gets the code of this OptionEntity.

        选项code值

        :return: The code of this OptionEntity.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        r"""Sets the code of this OptionEntity.

        选项code值

        :param code: The code of this OptionEntity.
        :type code: str
        """
        self._code = code

    @property
    def display_value(self):
        r"""Gets the display_value of this OptionEntity.

        选项显示名称

        :return: The display_value of this OptionEntity.
        :rtype: str
        """
        return self._display_value

    @display_value.setter
    def display_value(self, display_value):
        r"""Sets the display_value of this OptionEntity.

        选项显示名称

        :param display_value: The display_value of this OptionEntity.
        :type display_value: str
        """
        self._display_value = display_value

    @property
    def value(self):
        r"""Gets the value of this OptionEntity.

        选项唯一标识

        :return: The value of this OptionEntity.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this OptionEntity.

        选项唯一标识

        :param value: The value of this OptionEntity.
        :type value: str
        """
        self._value = value

    @property
    def level(self):
        r"""Gets the level of this OptionEntity.

        选项层级。用于区分层级字段的层级

        :return: The level of this OptionEntity.
        :rtype: int
        """
        return self._level

    @level.setter
    def level(self, level):
        r"""Sets the level of this OptionEntity.

        选项层级。用于区分层级字段的层级

        :param level: The level of this OptionEntity.
        :type level: int
        """
        self._level = level

    @property
    def sequence(self):
        r"""Gets the sequence of this OptionEntity.

        选项顺序

        :return: The sequence of this OptionEntity.
        :rtype: int
        """
        return self._sequence

    @sequence.setter
    def sequence(self, sequence):
        r"""Sets the sequence of this OptionEntity.

        选项顺序

        :param sequence: The sequence of this OptionEntity.
        :type sequence: int
        """
        self._sequence = sequence

    @property
    def parent_id(self):
        r"""Gets the parent_id of this OptionEntity.

        父选项id

        :return: The parent_id of this OptionEntity.
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        r"""Sets the parent_id of this OptionEntity.

        父选项id

        :param parent_id: The parent_id of this OptionEntity.
        :type parent_id: str
        """
        self._parent_id = parent_id

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
        if not isinstance(other, OptionEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
