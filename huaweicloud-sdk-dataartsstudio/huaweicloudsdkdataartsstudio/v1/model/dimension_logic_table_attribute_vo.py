# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DimensionLogicTableAttributeVO:

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
        'dimension_logic_table_id': 'str',
        'ordinal': 'int',
        'dimension_attribute_id': 'str',
        'name_en': 'str',
        'name_ch': 'str',
        'description': 'str',
        'data_type': 'str',
        'domain_type': 'DataTypeDomainEnum',
        'data_type_extend': 'str',
        'is_primary_key': 'bool',
        'is_biz_primary': 'bool',
        'is_partition_key': 'bool',
        'not_null': 'bool',
        'stand_row_id': 'str',
        'stand_row_name': 'str',
        'quality_infos': 'list[QualityInfoVO]',
        'alias': 'str',
        'self_defined_fields': 'list[SelfDefinedFieldVO]',
        'secrecy_levels': 'list[SecrecyLevelVO]'
    }

    attribute_map = {
        'id': 'id',
        'dimension_logic_table_id': 'dimension_logic_table_id',
        'ordinal': 'ordinal',
        'dimension_attribute_id': 'dimension_attribute_id',
        'name_en': 'name_en',
        'name_ch': 'name_ch',
        'description': 'description',
        'data_type': 'data_type',
        'domain_type': 'domain_type',
        'data_type_extend': 'data_type_extend',
        'is_primary_key': 'is_primary_key',
        'is_biz_primary': 'is_biz_primary',
        'is_partition_key': 'is_partition_key',
        'not_null': 'not_null',
        'stand_row_id': 'stand_row_id',
        'stand_row_name': 'stand_row_name',
        'quality_infos': 'quality_infos',
        'alias': 'alias',
        'self_defined_fields': 'self_defined_fields',
        'secrecy_levels': 'secrecy_levels'
    }

    def __init__(self, id=None, dimension_logic_table_id=None, ordinal=None, dimension_attribute_id=None, name_en=None, name_ch=None, description=None, data_type=None, domain_type=None, data_type_extend=None, is_primary_key=None, is_biz_primary=None, is_partition_key=None, not_null=None, stand_row_id=None, stand_row_name=None, quality_infos=None, alias=None, self_defined_fields=None, secrecy_levels=None):
        r"""DimensionLogicTableAttributeVO

        The model defined in huaweicloud sdk

        :param id: 维度表ID，ID字符串。
        :type id: str
        :param dimension_logic_table_id: 所属维表ID。
        :type dimension_logic_table_id: str
        :param ordinal: 序号
        :type ordinal: int
        :param dimension_attribute_id: 维度属性ID，ID字符串。
        :type dimension_attribute_id: str
        :param name_en: 字段名，只读。
        :type name_en: str
        :param name_ch: 业务属性，只读。
        :type name_ch: str
        :param description: 描述，只读。
        :type description: str
        :param data_type: 字段类型。
        :type data_type: str
        :param domain_type: 
        :type domain_type: :class:`huaweicloudsdkdataartsstudio.v1.DataTypeDomainEnum`
        :param data_type_extend: 数据类型扩展字段。
        :type data_type_extend: str
        :param is_primary_key: 是否主键，只读。
        :type is_primary_key: bool
        :param is_biz_primary: 是否业务主键。
        :type is_biz_primary: bool
        :param is_partition_key: 是否主键分区，只读。
        :type is_partition_key: bool
        :param not_null: 是否不为空。
        :type not_null: bool
        :param stand_row_id: 关联的数据标准的ID，ID字符串。
        :type stand_row_id: str
        :param stand_row_name: 关联的数据标准名称，只读。
        :type stand_row_name: str
        :param quality_infos: 质量信息，只读。
        :type quality_infos: list[:class:`huaweicloudsdkdataartsstudio.v1.QualityInfoVO`]
        :param alias: 别名。
        :type alias: str
        :param self_defined_fields: 自定义项。
        :type self_defined_fields: list[:class:`huaweicloudsdkdataartsstudio.v1.SelfDefinedFieldVO`]
        :param secrecy_levels: 密级
        :type secrecy_levels: list[:class:`huaweicloudsdkdataartsstudio.v1.SecrecyLevelVO`]
        """
        
        

        self._id = None
        self._dimension_logic_table_id = None
        self._ordinal = None
        self._dimension_attribute_id = None
        self._name_en = None
        self._name_ch = None
        self._description = None
        self._data_type = None
        self._domain_type = None
        self._data_type_extend = None
        self._is_primary_key = None
        self._is_biz_primary = None
        self._is_partition_key = None
        self._not_null = None
        self._stand_row_id = None
        self._stand_row_name = None
        self._quality_infos = None
        self._alias = None
        self._self_defined_fields = None
        self._secrecy_levels = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if dimension_logic_table_id is not None:
            self.dimension_logic_table_id = dimension_logic_table_id
        self.ordinal = ordinal
        self.dimension_attribute_id = dimension_attribute_id
        if name_en is not None:
            self.name_en = name_en
        if name_ch is not None:
            self.name_ch = name_ch
        if description is not None:
            self.description = description
        if data_type is not None:
            self.data_type = data_type
        if domain_type is not None:
            self.domain_type = domain_type
        if data_type_extend is not None:
            self.data_type_extend = data_type_extend
        if is_primary_key is not None:
            self.is_primary_key = is_primary_key
        if is_biz_primary is not None:
            self.is_biz_primary = is_biz_primary
        if is_partition_key is not None:
            self.is_partition_key = is_partition_key
        if not_null is not None:
            self.not_null = not_null
        if stand_row_id is not None:
            self.stand_row_id = stand_row_id
        if stand_row_name is not None:
            self.stand_row_name = stand_row_name
        if quality_infos is not None:
            self.quality_infos = quality_infos
        if alias is not None:
            self.alias = alias
        if self_defined_fields is not None:
            self.self_defined_fields = self_defined_fields
        if secrecy_levels is not None:
            self.secrecy_levels = secrecy_levels

    @property
    def id(self):
        r"""Gets the id of this DimensionLogicTableAttributeVO.

        维度表ID，ID字符串。

        :return: The id of this DimensionLogicTableAttributeVO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this DimensionLogicTableAttributeVO.

        维度表ID，ID字符串。

        :param id: The id of this DimensionLogicTableAttributeVO.
        :type id: str
        """
        self._id = id

    @property
    def dimension_logic_table_id(self):
        r"""Gets the dimension_logic_table_id of this DimensionLogicTableAttributeVO.

        所属维表ID。

        :return: The dimension_logic_table_id of this DimensionLogicTableAttributeVO.
        :rtype: str
        """
        return self._dimension_logic_table_id

    @dimension_logic_table_id.setter
    def dimension_logic_table_id(self, dimension_logic_table_id):
        r"""Sets the dimension_logic_table_id of this DimensionLogicTableAttributeVO.

        所属维表ID。

        :param dimension_logic_table_id: The dimension_logic_table_id of this DimensionLogicTableAttributeVO.
        :type dimension_logic_table_id: str
        """
        self._dimension_logic_table_id = dimension_logic_table_id

    @property
    def ordinal(self):
        r"""Gets the ordinal of this DimensionLogicTableAttributeVO.

        序号

        :return: The ordinal of this DimensionLogicTableAttributeVO.
        :rtype: int
        """
        return self._ordinal

    @ordinal.setter
    def ordinal(self, ordinal):
        r"""Sets the ordinal of this DimensionLogicTableAttributeVO.

        序号

        :param ordinal: The ordinal of this DimensionLogicTableAttributeVO.
        :type ordinal: int
        """
        self._ordinal = ordinal

    @property
    def dimension_attribute_id(self):
        r"""Gets the dimension_attribute_id of this DimensionLogicTableAttributeVO.

        维度属性ID，ID字符串。

        :return: The dimension_attribute_id of this DimensionLogicTableAttributeVO.
        :rtype: str
        """
        return self._dimension_attribute_id

    @dimension_attribute_id.setter
    def dimension_attribute_id(self, dimension_attribute_id):
        r"""Sets the dimension_attribute_id of this DimensionLogicTableAttributeVO.

        维度属性ID，ID字符串。

        :param dimension_attribute_id: The dimension_attribute_id of this DimensionLogicTableAttributeVO.
        :type dimension_attribute_id: str
        """
        self._dimension_attribute_id = dimension_attribute_id

    @property
    def name_en(self):
        r"""Gets the name_en of this DimensionLogicTableAttributeVO.

        字段名，只读。

        :return: The name_en of this DimensionLogicTableAttributeVO.
        :rtype: str
        """
        return self._name_en

    @name_en.setter
    def name_en(self, name_en):
        r"""Sets the name_en of this DimensionLogicTableAttributeVO.

        字段名，只读。

        :param name_en: The name_en of this DimensionLogicTableAttributeVO.
        :type name_en: str
        """
        self._name_en = name_en

    @property
    def name_ch(self):
        r"""Gets the name_ch of this DimensionLogicTableAttributeVO.

        业务属性，只读。

        :return: The name_ch of this DimensionLogicTableAttributeVO.
        :rtype: str
        """
        return self._name_ch

    @name_ch.setter
    def name_ch(self, name_ch):
        r"""Sets the name_ch of this DimensionLogicTableAttributeVO.

        业务属性，只读。

        :param name_ch: The name_ch of this DimensionLogicTableAttributeVO.
        :type name_ch: str
        """
        self._name_ch = name_ch

    @property
    def description(self):
        r"""Gets the description of this DimensionLogicTableAttributeVO.

        描述，只读。

        :return: The description of this DimensionLogicTableAttributeVO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this DimensionLogicTableAttributeVO.

        描述，只读。

        :param description: The description of this DimensionLogicTableAttributeVO.
        :type description: str
        """
        self._description = description

    @property
    def data_type(self):
        r"""Gets the data_type of this DimensionLogicTableAttributeVO.

        字段类型。

        :return: The data_type of this DimensionLogicTableAttributeVO.
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        r"""Sets the data_type of this DimensionLogicTableAttributeVO.

        字段类型。

        :param data_type: The data_type of this DimensionLogicTableAttributeVO.
        :type data_type: str
        """
        self._data_type = data_type

    @property
    def domain_type(self):
        r"""Gets the domain_type of this DimensionLogicTableAttributeVO.

        :return: The domain_type of this DimensionLogicTableAttributeVO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.DataTypeDomainEnum`
        """
        return self._domain_type

    @domain_type.setter
    def domain_type(self, domain_type):
        r"""Sets the domain_type of this DimensionLogicTableAttributeVO.

        :param domain_type: The domain_type of this DimensionLogicTableAttributeVO.
        :type domain_type: :class:`huaweicloudsdkdataartsstudio.v1.DataTypeDomainEnum`
        """
        self._domain_type = domain_type

    @property
    def data_type_extend(self):
        r"""Gets the data_type_extend of this DimensionLogicTableAttributeVO.

        数据类型扩展字段。

        :return: The data_type_extend of this DimensionLogicTableAttributeVO.
        :rtype: str
        """
        return self._data_type_extend

    @data_type_extend.setter
    def data_type_extend(self, data_type_extend):
        r"""Sets the data_type_extend of this DimensionLogicTableAttributeVO.

        数据类型扩展字段。

        :param data_type_extend: The data_type_extend of this DimensionLogicTableAttributeVO.
        :type data_type_extend: str
        """
        self._data_type_extend = data_type_extend

    @property
    def is_primary_key(self):
        r"""Gets the is_primary_key of this DimensionLogicTableAttributeVO.

        是否主键，只读。

        :return: The is_primary_key of this DimensionLogicTableAttributeVO.
        :rtype: bool
        """
        return self._is_primary_key

    @is_primary_key.setter
    def is_primary_key(self, is_primary_key):
        r"""Sets the is_primary_key of this DimensionLogicTableAttributeVO.

        是否主键，只读。

        :param is_primary_key: The is_primary_key of this DimensionLogicTableAttributeVO.
        :type is_primary_key: bool
        """
        self._is_primary_key = is_primary_key

    @property
    def is_biz_primary(self):
        r"""Gets the is_biz_primary of this DimensionLogicTableAttributeVO.

        是否业务主键。

        :return: The is_biz_primary of this DimensionLogicTableAttributeVO.
        :rtype: bool
        """
        return self._is_biz_primary

    @is_biz_primary.setter
    def is_biz_primary(self, is_biz_primary):
        r"""Sets the is_biz_primary of this DimensionLogicTableAttributeVO.

        是否业务主键。

        :param is_biz_primary: The is_biz_primary of this DimensionLogicTableAttributeVO.
        :type is_biz_primary: bool
        """
        self._is_biz_primary = is_biz_primary

    @property
    def is_partition_key(self):
        r"""Gets the is_partition_key of this DimensionLogicTableAttributeVO.

        是否主键分区，只读。

        :return: The is_partition_key of this DimensionLogicTableAttributeVO.
        :rtype: bool
        """
        return self._is_partition_key

    @is_partition_key.setter
    def is_partition_key(self, is_partition_key):
        r"""Sets the is_partition_key of this DimensionLogicTableAttributeVO.

        是否主键分区，只读。

        :param is_partition_key: The is_partition_key of this DimensionLogicTableAttributeVO.
        :type is_partition_key: bool
        """
        self._is_partition_key = is_partition_key

    @property
    def not_null(self):
        r"""Gets the not_null of this DimensionLogicTableAttributeVO.

        是否不为空。

        :return: The not_null of this DimensionLogicTableAttributeVO.
        :rtype: bool
        """
        return self._not_null

    @not_null.setter
    def not_null(self, not_null):
        r"""Sets the not_null of this DimensionLogicTableAttributeVO.

        是否不为空。

        :param not_null: The not_null of this DimensionLogicTableAttributeVO.
        :type not_null: bool
        """
        self._not_null = not_null

    @property
    def stand_row_id(self):
        r"""Gets the stand_row_id of this DimensionLogicTableAttributeVO.

        关联的数据标准的ID，ID字符串。

        :return: The stand_row_id of this DimensionLogicTableAttributeVO.
        :rtype: str
        """
        return self._stand_row_id

    @stand_row_id.setter
    def stand_row_id(self, stand_row_id):
        r"""Sets the stand_row_id of this DimensionLogicTableAttributeVO.

        关联的数据标准的ID，ID字符串。

        :param stand_row_id: The stand_row_id of this DimensionLogicTableAttributeVO.
        :type stand_row_id: str
        """
        self._stand_row_id = stand_row_id

    @property
    def stand_row_name(self):
        r"""Gets the stand_row_name of this DimensionLogicTableAttributeVO.

        关联的数据标准名称，只读。

        :return: The stand_row_name of this DimensionLogicTableAttributeVO.
        :rtype: str
        """
        return self._stand_row_name

    @stand_row_name.setter
    def stand_row_name(self, stand_row_name):
        r"""Sets the stand_row_name of this DimensionLogicTableAttributeVO.

        关联的数据标准名称，只读。

        :param stand_row_name: The stand_row_name of this DimensionLogicTableAttributeVO.
        :type stand_row_name: str
        """
        self._stand_row_name = stand_row_name

    @property
    def quality_infos(self):
        r"""Gets the quality_infos of this DimensionLogicTableAttributeVO.

        质量信息，只读。

        :return: The quality_infos of this DimensionLogicTableAttributeVO.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.QualityInfoVO`]
        """
        return self._quality_infos

    @quality_infos.setter
    def quality_infos(self, quality_infos):
        r"""Sets the quality_infos of this DimensionLogicTableAttributeVO.

        质量信息，只读。

        :param quality_infos: The quality_infos of this DimensionLogicTableAttributeVO.
        :type quality_infos: list[:class:`huaweicloudsdkdataartsstudio.v1.QualityInfoVO`]
        """
        self._quality_infos = quality_infos

    @property
    def alias(self):
        r"""Gets the alias of this DimensionLogicTableAttributeVO.

        别名。

        :return: The alias of this DimensionLogicTableAttributeVO.
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        r"""Sets the alias of this DimensionLogicTableAttributeVO.

        别名。

        :param alias: The alias of this DimensionLogicTableAttributeVO.
        :type alias: str
        """
        self._alias = alias

    @property
    def self_defined_fields(self):
        r"""Gets the self_defined_fields of this DimensionLogicTableAttributeVO.

        自定义项。

        :return: The self_defined_fields of this DimensionLogicTableAttributeVO.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.SelfDefinedFieldVO`]
        """
        return self._self_defined_fields

    @self_defined_fields.setter
    def self_defined_fields(self, self_defined_fields):
        r"""Sets the self_defined_fields of this DimensionLogicTableAttributeVO.

        自定义项。

        :param self_defined_fields: The self_defined_fields of this DimensionLogicTableAttributeVO.
        :type self_defined_fields: list[:class:`huaweicloudsdkdataartsstudio.v1.SelfDefinedFieldVO`]
        """
        self._self_defined_fields = self_defined_fields

    @property
    def secrecy_levels(self):
        r"""Gets the secrecy_levels of this DimensionLogicTableAttributeVO.

        密级

        :return: The secrecy_levels of this DimensionLogicTableAttributeVO.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.SecrecyLevelVO`]
        """
        return self._secrecy_levels

    @secrecy_levels.setter
    def secrecy_levels(self, secrecy_levels):
        r"""Sets the secrecy_levels of this DimensionLogicTableAttributeVO.

        密级

        :param secrecy_levels: The secrecy_levels of this DimensionLogicTableAttributeVO.
        :type secrecy_levels: list[:class:`huaweicloudsdkdataartsstudio.v1.SecrecyLevelVO`]
        """
        self._secrecy_levels = secrecy_levels

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
        if not isinstance(other, DimensionLogicTableAttributeVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
