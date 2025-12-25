# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ColumnDisplaySetting:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'mapping_required': 'bool',
        'group_sequence_number': 'int',
        'intra_group_sequence_number': 'int',
        'value_type': 'str',
        'value_qualified': 'str',
        'display_name': 'str',
        'display_description': 'str',
        'group_name': 'str'
    }

    attribute_map = {
        'mapping_required': 'mapping_required',
        'group_sequence_number': 'group_sequence_number',
        'intra_group_sequence_number': 'intra_group_sequence_number',
        'value_type': 'value_type',
        'value_qualified': 'value_qualified',
        'display_name': 'display_name',
        'display_description': 'display_description',
        'group_name': 'group_name'
    }

    def __init__(self, mapping_required=None, group_sequence_number=None, intra_group_sequence_number=None, value_type=None, value_qualified=None, display_name=None, display_description=None, group_name=None):
        r"""ColumnDisplaySetting

        The model defined in huaweicloud sdk

        :param mapping_required: 映射是否必填
        :type mapping_required: bool
        :param group_sequence_number: 组顺序编号
        :type group_sequence_number: int
        :param intra_group_sequence_number: 组内顺序编号
        :type intra_group_sequence_number: int
        :param value_type: 值类型
        :type value_type: str
        :param value_qualified: 合法值
        :type value_qualified: str
        :param display_name: 显示名称
        :type display_name: str
        :param display_description: 显示描述
        :type display_description: str
        :param group_name: 组名
        :type group_name: str
        """
        
        

        self._mapping_required = None
        self._group_sequence_number = None
        self._intra_group_sequence_number = None
        self._value_type = None
        self._value_qualified = None
        self._display_name = None
        self._display_description = None
        self._group_name = None
        self.discriminator = None

        if mapping_required is not None:
            self.mapping_required = mapping_required
        if group_sequence_number is not None:
            self.group_sequence_number = group_sequence_number
        if intra_group_sequence_number is not None:
            self.intra_group_sequence_number = intra_group_sequence_number
        if value_type is not None:
            self.value_type = value_type
        if value_qualified is not None:
            self.value_qualified = value_qualified
        if display_name is not None:
            self.display_name = display_name
        if display_description is not None:
            self.display_description = display_description
        if group_name is not None:
            self.group_name = group_name

    @property
    def mapping_required(self):
        r"""Gets the mapping_required of this ColumnDisplaySetting.

        映射是否必填

        :return: The mapping_required of this ColumnDisplaySetting.
        :rtype: bool
        """
        return self._mapping_required

    @mapping_required.setter
    def mapping_required(self, mapping_required):
        r"""Sets the mapping_required of this ColumnDisplaySetting.

        映射是否必填

        :param mapping_required: The mapping_required of this ColumnDisplaySetting.
        :type mapping_required: bool
        """
        self._mapping_required = mapping_required

    @property
    def group_sequence_number(self):
        r"""Gets the group_sequence_number of this ColumnDisplaySetting.

        组顺序编号

        :return: The group_sequence_number of this ColumnDisplaySetting.
        :rtype: int
        """
        return self._group_sequence_number

    @group_sequence_number.setter
    def group_sequence_number(self, group_sequence_number):
        r"""Sets the group_sequence_number of this ColumnDisplaySetting.

        组顺序编号

        :param group_sequence_number: The group_sequence_number of this ColumnDisplaySetting.
        :type group_sequence_number: int
        """
        self._group_sequence_number = group_sequence_number

    @property
    def intra_group_sequence_number(self):
        r"""Gets the intra_group_sequence_number of this ColumnDisplaySetting.

        组内顺序编号

        :return: The intra_group_sequence_number of this ColumnDisplaySetting.
        :rtype: int
        """
        return self._intra_group_sequence_number

    @intra_group_sequence_number.setter
    def intra_group_sequence_number(self, intra_group_sequence_number):
        r"""Sets the intra_group_sequence_number of this ColumnDisplaySetting.

        组内顺序编号

        :param intra_group_sequence_number: The intra_group_sequence_number of this ColumnDisplaySetting.
        :type intra_group_sequence_number: int
        """
        self._intra_group_sequence_number = intra_group_sequence_number

    @property
    def value_type(self):
        r"""Gets the value_type of this ColumnDisplaySetting.

        值类型

        :return: The value_type of this ColumnDisplaySetting.
        :rtype: str
        """
        return self._value_type

    @value_type.setter
    def value_type(self, value_type):
        r"""Sets the value_type of this ColumnDisplaySetting.

        值类型

        :param value_type: The value_type of this ColumnDisplaySetting.
        :type value_type: str
        """
        self._value_type = value_type

    @property
    def value_qualified(self):
        r"""Gets the value_qualified of this ColumnDisplaySetting.

        合法值

        :return: The value_qualified of this ColumnDisplaySetting.
        :rtype: str
        """
        return self._value_qualified

    @value_qualified.setter
    def value_qualified(self, value_qualified):
        r"""Sets the value_qualified of this ColumnDisplaySetting.

        合法值

        :param value_qualified: The value_qualified of this ColumnDisplaySetting.
        :type value_qualified: str
        """
        self._value_qualified = value_qualified

    @property
    def display_name(self):
        r"""Gets the display_name of this ColumnDisplaySetting.

        显示名称

        :return: The display_name of this ColumnDisplaySetting.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        r"""Sets the display_name of this ColumnDisplaySetting.

        显示名称

        :param display_name: The display_name of this ColumnDisplaySetting.
        :type display_name: str
        """
        self._display_name = display_name

    @property
    def display_description(self):
        r"""Gets the display_description of this ColumnDisplaySetting.

        显示描述

        :return: The display_description of this ColumnDisplaySetting.
        :rtype: str
        """
        return self._display_description

    @display_description.setter
    def display_description(self, display_description):
        r"""Sets the display_description of this ColumnDisplaySetting.

        显示描述

        :param display_description: The display_description of this ColumnDisplaySetting.
        :type display_description: str
        """
        self._display_description = display_description

    @property
    def group_name(self):
        r"""Gets the group_name of this ColumnDisplaySetting.

        组名

        :return: The group_name of this ColumnDisplaySetting.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        r"""Sets the group_name of this ColumnDisplaySetting.

        组名

        :param group_name: The group_name of this ColumnDisplaySetting.
        :type group_name: str
        """
        self._group_name = group_name

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ColumnDisplaySetting):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
