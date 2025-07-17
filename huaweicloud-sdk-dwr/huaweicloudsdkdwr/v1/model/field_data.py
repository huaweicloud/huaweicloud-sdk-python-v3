# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FieldData:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'field_name': 'str',
        'data_type': 'str',
        'primary_key': 'bool',
        'partition_key': 'bool',
        'dim': 'str',
        'max_length': 'str',
        'max_capacity': 'str'
    }

    attribute_map = {
        'field_name': 'field_name',
        'data_type': 'data_type',
        'primary_key': 'primary_key',
        'partition_key': 'partition_key',
        'dim': 'dim',
        'max_length': 'max_length',
        'max_capacity': 'max_capacity'
    }

    def __init__(self, field_name=None, data_type=None, primary_key=None, partition_key=None, dim=None, max_length=None, max_capacity=None):
        r"""FieldData

        The model defined in huaweicloud sdk

        :param field_name: **参数解释：** 要在集合中创建的字段名称。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值:** 不涉及。
        :type field_name: str
        :param data_type: **参数解释：** 字段的数据类型。 **约束限制：** 不涉及。 **取值范围：** “Bool”,“Int8”,“Int16”,“Int32”,“Int64”,“Float”,“String”,“Array”,“JSON”,\&quot;FloatVector\&quot;, \&quot;SparseFloatVector\&quot;。 **默认取值:** 不涉及。
        :type data_type: str
        :param primary_key: **参数解释：** 是否是主键字段。 **约束限制：** 不涉及。 **取值范围：** true，false。 **默认取值:** 不涉及。
        :type primary_key: bool
        :param partition_key: **参数解释：** 是否是partition key。 **约束限制：** 不涉及。 **取值范围：** true，false。 **默认取值:** 不涉及。
        :type partition_key: bool
        :param dim: **参数解释：** 向量列的维度值。 **约束限制：** field的数据类型是FloatVector, SparseFloatVector时生效。 **取值范围：** 不涉及。 **默认取值:** 不涉及。
        :type dim: str
        :param max_length: **参数解释：** 字符串列设置的最大长度值。 **约束限制：** field的数据类型是String或者 Array 元素类型为String类型时生效。 **取值范围：** 不涉及。 **默认取值:** 不涉及。
        :type max_length: str
        :param max_capacity: **参数解释：** 数组列设置的最大容量值。 **约束限制：** field的数据类型是 Array 类型时生效。 **取值范围：** 不涉及。 **默认取值:** 不涉及。
        :type max_capacity: str
        """
        
        

        self._field_name = None
        self._data_type = None
        self._primary_key = None
        self._partition_key = None
        self._dim = None
        self._max_length = None
        self._max_capacity = None
        self.discriminator = None

        self.field_name = field_name
        self.data_type = data_type
        self.primary_key = primary_key
        self.partition_key = partition_key
        if dim is not None:
            self.dim = dim
        if max_length is not None:
            self.max_length = max_length
        if max_capacity is not None:
            self.max_capacity = max_capacity

    @property
    def field_name(self):
        r"""Gets the field_name of this FieldData.

        **参数解释：** 要在集合中创建的字段名称。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值:** 不涉及。

        :return: The field_name of this FieldData.
        :rtype: str
        """
        return self._field_name

    @field_name.setter
    def field_name(self, field_name):
        r"""Sets the field_name of this FieldData.

        **参数解释：** 要在集合中创建的字段名称。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值:** 不涉及。

        :param field_name: The field_name of this FieldData.
        :type field_name: str
        """
        self._field_name = field_name

    @property
    def data_type(self):
        r"""Gets the data_type of this FieldData.

        **参数解释：** 字段的数据类型。 **约束限制：** 不涉及。 **取值范围：** “Bool”,“Int8”,“Int16”,“Int32”,“Int64”,“Float”,“String”,“Array”,“JSON”,\"FloatVector\", \"SparseFloatVector\"。 **默认取值:** 不涉及。

        :return: The data_type of this FieldData.
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        r"""Sets the data_type of this FieldData.

        **参数解释：** 字段的数据类型。 **约束限制：** 不涉及。 **取值范围：** “Bool”,“Int8”,“Int16”,“Int32”,“Int64”,“Float”,“String”,“Array”,“JSON”,\"FloatVector\", \"SparseFloatVector\"。 **默认取值:** 不涉及。

        :param data_type: The data_type of this FieldData.
        :type data_type: str
        """
        self._data_type = data_type

    @property
    def primary_key(self):
        r"""Gets the primary_key of this FieldData.

        **参数解释：** 是否是主键字段。 **约束限制：** 不涉及。 **取值范围：** true，false。 **默认取值:** 不涉及。

        :return: The primary_key of this FieldData.
        :rtype: bool
        """
        return self._primary_key

    @primary_key.setter
    def primary_key(self, primary_key):
        r"""Sets the primary_key of this FieldData.

        **参数解释：** 是否是主键字段。 **约束限制：** 不涉及。 **取值范围：** true，false。 **默认取值:** 不涉及。

        :param primary_key: The primary_key of this FieldData.
        :type primary_key: bool
        """
        self._primary_key = primary_key

    @property
    def partition_key(self):
        r"""Gets the partition_key of this FieldData.

        **参数解释：** 是否是partition key。 **约束限制：** 不涉及。 **取值范围：** true，false。 **默认取值:** 不涉及。

        :return: The partition_key of this FieldData.
        :rtype: bool
        """
        return self._partition_key

    @partition_key.setter
    def partition_key(self, partition_key):
        r"""Sets the partition_key of this FieldData.

        **参数解释：** 是否是partition key。 **约束限制：** 不涉及。 **取值范围：** true，false。 **默认取值:** 不涉及。

        :param partition_key: The partition_key of this FieldData.
        :type partition_key: bool
        """
        self._partition_key = partition_key

    @property
    def dim(self):
        r"""Gets the dim of this FieldData.

        **参数解释：** 向量列的维度值。 **约束限制：** field的数据类型是FloatVector, SparseFloatVector时生效。 **取值范围：** 不涉及。 **默认取值:** 不涉及。

        :return: The dim of this FieldData.
        :rtype: str
        """
        return self._dim

    @dim.setter
    def dim(self, dim):
        r"""Sets the dim of this FieldData.

        **参数解释：** 向量列的维度值。 **约束限制：** field的数据类型是FloatVector, SparseFloatVector时生效。 **取值范围：** 不涉及。 **默认取值:** 不涉及。

        :param dim: The dim of this FieldData.
        :type dim: str
        """
        self._dim = dim

    @property
    def max_length(self):
        r"""Gets the max_length of this FieldData.

        **参数解释：** 字符串列设置的最大长度值。 **约束限制：** field的数据类型是String或者 Array 元素类型为String类型时生效。 **取值范围：** 不涉及。 **默认取值:** 不涉及。

        :return: The max_length of this FieldData.
        :rtype: str
        """
        return self._max_length

    @max_length.setter
    def max_length(self, max_length):
        r"""Sets the max_length of this FieldData.

        **参数解释：** 字符串列设置的最大长度值。 **约束限制：** field的数据类型是String或者 Array 元素类型为String类型时生效。 **取值范围：** 不涉及。 **默认取值:** 不涉及。

        :param max_length: The max_length of this FieldData.
        :type max_length: str
        """
        self._max_length = max_length

    @property
    def max_capacity(self):
        r"""Gets the max_capacity of this FieldData.

        **参数解释：** 数组列设置的最大容量值。 **约束限制：** field的数据类型是 Array 类型时生效。 **取值范围：** 不涉及。 **默认取值:** 不涉及。

        :return: The max_capacity of this FieldData.
        :rtype: str
        """
        return self._max_capacity

    @max_capacity.setter
    def max_capacity(self, max_capacity):
        r"""Sets the max_capacity of this FieldData.

        **参数解释：** 数组列设置的最大容量值。 **约束限制：** field的数据类型是 Array 类型时生效。 **取值范围：** 不涉及。 **默认取值:** 不涉及。

        :param max_capacity: The max_capacity of this FieldData.
        :type max_capacity: str
        """
        self._max_capacity = max_capacity

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
        if not isinstance(other, FieldData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
