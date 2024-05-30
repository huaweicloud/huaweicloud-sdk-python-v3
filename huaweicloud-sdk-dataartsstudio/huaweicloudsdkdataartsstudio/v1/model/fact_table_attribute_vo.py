# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FactTableAttributeVO:

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
        'fact_logic_table_id': 'str',
        'ordinal': 'int',
        'dimension_id': 'str',
        'role': 'str',
        'dimension': 'DimensionVO',
        'is_primary_key': 'bool',
        'is_partition_key': 'bool',
        'is_foreign_key': 'bool',
        'secrecy_levels': 'list[SecrecyLevelRecordVO]',
        'description': 'str',
        'data_type': 'str',
        'domain_type': 'DataTypeDomainEnum',
        'data_type_extend': 'str',
        'name_en': 'str',
        'name_ch': 'str',
        'not_null': 'bool',
        'attribute_type': 'BizTypeEnum',
        'stand_row_id': 'str',
        'stand_row_name': 'str',
        'quality_infos': 'list[QualityInfoVO]',
        'alias': 'str',
        'self_defined_fields': 'list[SelfDefinedFieldVO]'
    }

    attribute_map = {
        'id': 'id',
        'fact_logic_table_id': 'fact_logic_table_id',
        'ordinal': 'ordinal',
        'dimension_id': 'dimension_id',
        'role': 'role',
        'dimension': 'dimension',
        'is_primary_key': 'is_primary_key',
        'is_partition_key': 'is_partition_key',
        'is_foreign_key': 'is_foreign_key',
        'secrecy_levels': 'secrecy_levels',
        'description': 'description',
        'data_type': 'data_type',
        'domain_type': 'domain_type',
        'data_type_extend': 'data_type_extend',
        'name_en': 'name_en',
        'name_ch': 'name_ch',
        'not_null': 'not_null',
        'attribute_type': 'attribute_type',
        'stand_row_id': 'stand_row_id',
        'stand_row_name': 'stand_row_name',
        'quality_infos': 'quality_infos',
        'alias': 'alias',
        'self_defined_fields': 'self_defined_fields'
    }

    def __init__(self, id=None, fact_logic_table_id=None, ordinal=None, dimension_id=None, role=None, dimension=None, is_primary_key=None, is_partition_key=None, is_foreign_key=None, secrecy_levels=None, description=None, data_type=None, domain_type=None, data_type_extend=None, name_en=None, name_ch=None, not_null=None, attribute_type=None, stand_row_id=None, stand_row_name=None, quality_infos=None, alias=None, self_defined_fields=None):
        """FactTableAttributeVO

        The model defined in huaweicloud sdk

        :param id: 编码，填写String类型替代Long类型。
        :type id: str
        :param fact_logic_table_id: 所属事实表ID，只读，填写String类型替代Long类型。
        :type fact_logic_table_id: str
        :param ordinal: 序号。
        :type ordinal: int
        :param dimension_id: 维度ID，填写String类型替代Long类型。
        :type dimension_id: str
        :param role: 维度角色。
        :type role: str
        :param dimension: 
        :type dimension: :class:`huaweicloudsdkdataartsstudio.v1.DimensionVO`
        :param is_primary_key: 是否主键。
        :type is_primary_key: bool
        :param is_partition_key: 是否分区键。
        :type is_partition_key: bool
        :param is_foreign_key: 是否外键，只读。
        :type is_foreign_key: bool
        :param secrecy_levels: 密级
        :type secrecy_levels: list[:class:`huaweicloudsdkdataartsstudio.v1.SecrecyLevelRecordVO`]
        :param description: 描述。
        :type description: str
        :param data_type: 字段类型。
        :type data_type: str
        :param domain_type: 
        :type domain_type: :class:`huaweicloudsdkdataartsstudio.v1.DataTypeDomainEnum`
        :param data_type_extend: 数据类型扩展字段。
        :type data_type_extend: str
        :param name_en: 英文名。
        :type name_en: str
        :param name_ch: 中文名。
        :type name_ch: str
        :param not_null: 是否不为空。
        :type not_null: bool
        :param attribute_type: 
        :type attribute_type: :class:`huaweicloudsdkdataartsstudio.v1.BizTypeEnum`
        :param stand_row_id: 关联的数据标准的ID，填写String类型替代Long类型。
        :type stand_row_id: str
        :param stand_row_name: 关联的数据标准名称，只读。
        :type stand_row_name: str
        :param quality_infos: 质量信息，只读。
        :type quality_infos: list[:class:`huaweicloudsdkdataartsstudio.v1.QualityInfoVO`]
        :param alias: 别名。
        :type alias: str
        :param self_defined_fields: 自定义项。
        :type self_defined_fields: list[:class:`huaweicloudsdkdataartsstudio.v1.SelfDefinedFieldVO`]
        """
        
        

        self._id = None
        self._fact_logic_table_id = None
        self._ordinal = None
        self._dimension_id = None
        self._role = None
        self._dimension = None
        self._is_primary_key = None
        self._is_partition_key = None
        self._is_foreign_key = None
        self._secrecy_levels = None
        self._description = None
        self._data_type = None
        self._domain_type = None
        self._data_type_extend = None
        self._name_en = None
        self._name_ch = None
        self._not_null = None
        self._attribute_type = None
        self._stand_row_id = None
        self._stand_row_name = None
        self._quality_infos = None
        self._alias = None
        self._self_defined_fields = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if fact_logic_table_id is not None:
            self.fact_logic_table_id = fact_logic_table_id
        self.ordinal = ordinal
        if dimension_id is not None:
            self.dimension_id = dimension_id
        if role is not None:
            self.role = role
        if dimension is not None:
            self.dimension = dimension
        self.is_primary_key = is_primary_key
        self.is_partition_key = is_partition_key
        if is_foreign_key is not None:
            self.is_foreign_key = is_foreign_key
        if secrecy_levels is not None:
            self.secrecy_levels = secrecy_levels
        if description is not None:
            self.description = description
        self.data_type = data_type
        if domain_type is not None:
            self.domain_type = domain_type
        if data_type_extend is not None:
            self.data_type_extend = data_type_extend
        self.name_en = name_en
        self.name_ch = name_ch
        if not_null is not None:
            self.not_null = not_null
        if attribute_type is not None:
            self.attribute_type = attribute_type
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

    @property
    def id(self):
        """Gets the id of this FactTableAttributeVO.

        编码，填写String类型替代Long类型。

        :return: The id of this FactTableAttributeVO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FactTableAttributeVO.

        编码，填写String类型替代Long类型。

        :param id: The id of this FactTableAttributeVO.
        :type id: str
        """
        self._id = id

    @property
    def fact_logic_table_id(self):
        """Gets the fact_logic_table_id of this FactTableAttributeVO.

        所属事实表ID，只读，填写String类型替代Long类型。

        :return: The fact_logic_table_id of this FactTableAttributeVO.
        :rtype: str
        """
        return self._fact_logic_table_id

    @fact_logic_table_id.setter
    def fact_logic_table_id(self, fact_logic_table_id):
        """Sets the fact_logic_table_id of this FactTableAttributeVO.

        所属事实表ID，只读，填写String类型替代Long类型。

        :param fact_logic_table_id: The fact_logic_table_id of this FactTableAttributeVO.
        :type fact_logic_table_id: str
        """
        self._fact_logic_table_id = fact_logic_table_id

    @property
    def ordinal(self):
        """Gets the ordinal of this FactTableAttributeVO.

        序号。

        :return: The ordinal of this FactTableAttributeVO.
        :rtype: int
        """
        return self._ordinal

    @ordinal.setter
    def ordinal(self, ordinal):
        """Sets the ordinal of this FactTableAttributeVO.

        序号。

        :param ordinal: The ordinal of this FactTableAttributeVO.
        :type ordinal: int
        """
        self._ordinal = ordinal

    @property
    def dimension_id(self):
        """Gets the dimension_id of this FactTableAttributeVO.

        维度ID，填写String类型替代Long类型。

        :return: The dimension_id of this FactTableAttributeVO.
        :rtype: str
        """
        return self._dimension_id

    @dimension_id.setter
    def dimension_id(self, dimension_id):
        """Sets the dimension_id of this FactTableAttributeVO.

        维度ID，填写String类型替代Long类型。

        :param dimension_id: The dimension_id of this FactTableAttributeVO.
        :type dimension_id: str
        """
        self._dimension_id = dimension_id

    @property
    def role(self):
        """Gets the role of this FactTableAttributeVO.

        维度角色。

        :return: The role of this FactTableAttributeVO.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this FactTableAttributeVO.

        维度角色。

        :param role: The role of this FactTableAttributeVO.
        :type role: str
        """
        self._role = role

    @property
    def dimension(self):
        """Gets the dimension of this FactTableAttributeVO.

        :return: The dimension of this FactTableAttributeVO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.DimensionVO`
        """
        return self._dimension

    @dimension.setter
    def dimension(self, dimension):
        """Sets the dimension of this FactTableAttributeVO.

        :param dimension: The dimension of this FactTableAttributeVO.
        :type dimension: :class:`huaweicloudsdkdataartsstudio.v1.DimensionVO`
        """
        self._dimension = dimension

    @property
    def is_primary_key(self):
        """Gets the is_primary_key of this FactTableAttributeVO.

        是否主键。

        :return: The is_primary_key of this FactTableAttributeVO.
        :rtype: bool
        """
        return self._is_primary_key

    @is_primary_key.setter
    def is_primary_key(self, is_primary_key):
        """Sets the is_primary_key of this FactTableAttributeVO.

        是否主键。

        :param is_primary_key: The is_primary_key of this FactTableAttributeVO.
        :type is_primary_key: bool
        """
        self._is_primary_key = is_primary_key

    @property
    def is_partition_key(self):
        """Gets the is_partition_key of this FactTableAttributeVO.

        是否分区键。

        :return: The is_partition_key of this FactTableAttributeVO.
        :rtype: bool
        """
        return self._is_partition_key

    @is_partition_key.setter
    def is_partition_key(self, is_partition_key):
        """Sets the is_partition_key of this FactTableAttributeVO.

        是否分区键。

        :param is_partition_key: The is_partition_key of this FactTableAttributeVO.
        :type is_partition_key: bool
        """
        self._is_partition_key = is_partition_key

    @property
    def is_foreign_key(self):
        """Gets the is_foreign_key of this FactTableAttributeVO.

        是否外键，只读。

        :return: The is_foreign_key of this FactTableAttributeVO.
        :rtype: bool
        """
        return self._is_foreign_key

    @is_foreign_key.setter
    def is_foreign_key(self, is_foreign_key):
        """Sets the is_foreign_key of this FactTableAttributeVO.

        是否外键，只读。

        :param is_foreign_key: The is_foreign_key of this FactTableAttributeVO.
        :type is_foreign_key: bool
        """
        self._is_foreign_key = is_foreign_key

    @property
    def secrecy_levels(self):
        """Gets the secrecy_levels of this FactTableAttributeVO.

        密级

        :return: The secrecy_levels of this FactTableAttributeVO.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.SecrecyLevelRecordVO`]
        """
        return self._secrecy_levels

    @secrecy_levels.setter
    def secrecy_levels(self, secrecy_levels):
        """Sets the secrecy_levels of this FactTableAttributeVO.

        密级

        :param secrecy_levels: The secrecy_levels of this FactTableAttributeVO.
        :type secrecy_levels: list[:class:`huaweicloudsdkdataartsstudio.v1.SecrecyLevelRecordVO`]
        """
        self._secrecy_levels = secrecy_levels

    @property
    def description(self):
        """Gets the description of this FactTableAttributeVO.

        描述。

        :return: The description of this FactTableAttributeVO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this FactTableAttributeVO.

        描述。

        :param description: The description of this FactTableAttributeVO.
        :type description: str
        """
        self._description = description

    @property
    def data_type(self):
        """Gets the data_type of this FactTableAttributeVO.

        字段类型。

        :return: The data_type of this FactTableAttributeVO.
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """Sets the data_type of this FactTableAttributeVO.

        字段类型。

        :param data_type: The data_type of this FactTableAttributeVO.
        :type data_type: str
        """
        self._data_type = data_type

    @property
    def domain_type(self):
        """Gets the domain_type of this FactTableAttributeVO.

        :return: The domain_type of this FactTableAttributeVO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.DataTypeDomainEnum`
        """
        return self._domain_type

    @domain_type.setter
    def domain_type(self, domain_type):
        """Sets the domain_type of this FactTableAttributeVO.

        :param domain_type: The domain_type of this FactTableAttributeVO.
        :type domain_type: :class:`huaweicloudsdkdataartsstudio.v1.DataTypeDomainEnum`
        """
        self._domain_type = domain_type

    @property
    def data_type_extend(self):
        """Gets the data_type_extend of this FactTableAttributeVO.

        数据类型扩展字段。

        :return: The data_type_extend of this FactTableAttributeVO.
        :rtype: str
        """
        return self._data_type_extend

    @data_type_extend.setter
    def data_type_extend(self, data_type_extend):
        """Sets the data_type_extend of this FactTableAttributeVO.

        数据类型扩展字段。

        :param data_type_extend: The data_type_extend of this FactTableAttributeVO.
        :type data_type_extend: str
        """
        self._data_type_extend = data_type_extend

    @property
    def name_en(self):
        """Gets the name_en of this FactTableAttributeVO.

        英文名。

        :return: The name_en of this FactTableAttributeVO.
        :rtype: str
        """
        return self._name_en

    @name_en.setter
    def name_en(self, name_en):
        """Sets the name_en of this FactTableAttributeVO.

        英文名。

        :param name_en: The name_en of this FactTableAttributeVO.
        :type name_en: str
        """
        self._name_en = name_en

    @property
    def name_ch(self):
        """Gets the name_ch of this FactTableAttributeVO.

        中文名。

        :return: The name_ch of this FactTableAttributeVO.
        :rtype: str
        """
        return self._name_ch

    @name_ch.setter
    def name_ch(self, name_ch):
        """Sets the name_ch of this FactTableAttributeVO.

        中文名。

        :param name_ch: The name_ch of this FactTableAttributeVO.
        :type name_ch: str
        """
        self._name_ch = name_ch

    @property
    def not_null(self):
        """Gets the not_null of this FactTableAttributeVO.

        是否不为空。

        :return: The not_null of this FactTableAttributeVO.
        :rtype: bool
        """
        return self._not_null

    @not_null.setter
    def not_null(self, not_null):
        """Sets the not_null of this FactTableAttributeVO.

        是否不为空。

        :param not_null: The not_null of this FactTableAttributeVO.
        :type not_null: bool
        """
        self._not_null = not_null

    @property
    def attribute_type(self):
        """Gets the attribute_type of this FactTableAttributeVO.

        :return: The attribute_type of this FactTableAttributeVO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.BizTypeEnum`
        """
        return self._attribute_type

    @attribute_type.setter
    def attribute_type(self, attribute_type):
        """Sets the attribute_type of this FactTableAttributeVO.

        :param attribute_type: The attribute_type of this FactTableAttributeVO.
        :type attribute_type: :class:`huaweicloudsdkdataartsstudio.v1.BizTypeEnum`
        """
        self._attribute_type = attribute_type

    @property
    def stand_row_id(self):
        """Gets the stand_row_id of this FactTableAttributeVO.

        关联的数据标准的ID，填写String类型替代Long类型。

        :return: The stand_row_id of this FactTableAttributeVO.
        :rtype: str
        """
        return self._stand_row_id

    @stand_row_id.setter
    def stand_row_id(self, stand_row_id):
        """Sets the stand_row_id of this FactTableAttributeVO.

        关联的数据标准的ID，填写String类型替代Long类型。

        :param stand_row_id: The stand_row_id of this FactTableAttributeVO.
        :type stand_row_id: str
        """
        self._stand_row_id = stand_row_id

    @property
    def stand_row_name(self):
        """Gets the stand_row_name of this FactTableAttributeVO.

        关联的数据标准名称，只读。

        :return: The stand_row_name of this FactTableAttributeVO.
        :rtype: str
        """
        return self._stand_row_name

    @stand_row_name.setter
    def stand_row_name(self, stand_row_name):
        """Sets the stand_row_name of this FactTableAttributeVO.

        关联的数据标准名称，只读。

        :param stand_row_name: The stand_row_name of this FactTableAttributeVO.
        :type stand_row_name: str
        """
        self._stand_row_name = stand_row_name

    @property
    def quality_infos(self):
        """Gets the quality_infos of this FactTableAttributeVO.

        质量信息，只读。

        :return: The quality_infos of this FactTableAttributeVO.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.QualityInfoVO`]
        """
        return self._quality_infos

    @quality_infos.setter
    def quality_infos(self, quality_infos):
        """Sets the quality_infos of this FactTableAttributeVO.

        质量信息，只读。

        :param quality_infos: The quality_infos of this FactTableAttributeVO.
        :type quality_infos: list[:class:`huaweicloudsdkdataartsstudio.v1.QualityInfoVO`]
        """
        self._quality_infos = quality_infos

    @property
    def alias(self):
        """Gets the alias of this FactTableAttributeVO.

        别名。

        :return: The alias of this FactTableAttributeVO.
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """Sets the alias of this FactTableAttributeVO.

        别名。

        :param alias: The alias of this FactTableAttributeVO.
        :type alias: str
        """
        self._alias = alias

    @property
    def self_defined_fields(self):
        """Gets the self_defined_fields of this FactTableAttributeVO.

        自定义项。

        :return: The self_defined_fields of this FactTableAttributeVO.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.SelfDefinedFieldVO`]
        """
        return self._self_defined_fields

    @self_defined_fields.setter
    def self_defined_fields(self, self_defined_fields):
        """Sets the self_defined_fields of this FactTableAttributeVO.

        自定义项。

        :param self_defined_fields: The self_defined_fields of this FactTableAttributeVO.
        :type self_defined_fields: list[:class:`huaweicloudsdkdataartsstudio.v1.SelfDefinedFieldVO`]
        """
        self._self_defined_fields = self_defined_fields

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
        if not isinstance(other, FactTableAttributeVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
