# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TableModelAttributeVO:

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
        'name_en': 'str',
        'name_ch': 'str',
        'description': 'str',
        'obs_location': 'str',
        'create_by': 'str',
        'update_by': 'str',
        'data_type': 'str',
        'domain_type': 'DataTypeDomainEnum',
        'data_type_extend': 'str',
        'is_primary_key': 'bool',
        'is_partition_key': 'bool',
        'is_foreign_key': 'bool',
        'extend_field': 'bool',
        'not_null': 'bool',
        'ordinal': 'int',
        'table_model_id': 'str',
        'create_time': 'datetime',
        'update_time': 'datetime',
        'tags': 'list[TagVO]',
        'secrecy_levels': 'list[SecrecyLevelVO]',
        'stand_row_id': 'str',
        'stand_row_name': 'str',
        'quality_infos': 'list[QualityInfoVO]',
        'alias': 'str',
        'self_defined_fields': 'list[SelfDefinedFieldVO]',
        'code': 'str',
        'related_logic_attr_id': 'str',
        'related_logic_attr_name': 'str',
        'related_logic_attr_name_en': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name_en': 'name_en',
        'name_ch': 'name_ch',
        'description': 'description',
        'obs_location': 'obs_location',
        'create_by': 'create_by',
        'update_by': 'update_by',
        'data_type': 'data_type',
        'domain_type': 'domain_type',
        'data_type_extend': 'data_type_extend',
        'is_primary_key': 'is_primary_key',
        'is_partition_key': 'is_partition_key',
        'is_foreign_key': 'is_foreign_key',
        'extend_field': 'extend_field',
        'not_null': 'not_null',
        'ordinal': 'ordinal',
        'table_model_id': 'table_model_id',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'tags': 'tags',
        'secrecy_levels': 'secrecy_levels',
        'stand_row_id': 'stand_row_id',
        'stand_row_name': 'stand_row_name',
        'quality_infos': 'quality_infos',
        'alias': 'alias',
        'self_defined_fields': 'self_defined_fields',
        'code': 'code',
        'related_logic_attr_id': 'related_logic_attr_id',
        'related_logic_attr_name': 'related_logic_attr_name',
        'related_logic_attr_name_en': 'related_logic_attr_name_en'
    }

    def __init__(self, id=None, name_en=None, name_ch=None, description=None, obs_location=None, create_by=None, update_by=None, data_type=None, domain_type=None, data_type_extend=None, is_primary_key=None, is_partition_key=None, is_foreign_key=None, extend_field=None, not_null=None, ordinal=None, table_model_id=None, create_time=None, update_time=None, tags=None, secrecy_levels=None, stand_row_id=None, stand_row_name=None, quality_infos=None, alias=None, self_defined_fields=None, code=None, related_logic_attr_id=None, related_logic_attr_name=None, related_logic_attr_name_en=None):
        """TableModelAttributeVO

        The model defined in huaweicloud sdk

        :param id: 编码，填写String类型替代Long类型。
        :type id: str
        :param name_en: 字段名。
        :type name_en: str
        :param name_ch: 业务属性。
        :type name_ch: str
        :param description: 描述。
        :type description: str
        :param obs_location: obs路径，子路径。
        :type obs_location: str
        :param create_by: 创建人。
        :type create_by: str
        :param update_by: 更新人。
        :type update_by: str
        :param data_type: 字段类型。
        :type data_type: str
        :param domain_type: 
        :type domain_type: :class:`huaweicloudsdkdataartsstudio.v1.DataTypeDomainEnum`
        :param data_type_extend: 数据类型扩展字段。
        :type data_type_extend: str
        :param is_primary_key: 是否主键。
        :type is_primary_key: bool
        :param is_partition_key: 是否分区键。
        :type is_partition_key: bool
        :param is_foreign_key: 是否外键。
        :type is_foreign_key: bool
        :param extend_field: 是否继承的属性。
        :type extend_field: bool
        :param not_null: 是否不为空。
        :type not_null: bool
        :param ordinal: 序号。
        :type ordinal: int
        :param table_model_id: 所属关系建模的模型ID，填写String类型替代Long类型。
        :type table_model_id: str
        :param create_time: 创建时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。
        :type create_time: datetime
        :param update_time: 更新时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。
        :type update_time: datetime
        :param tags: 表标签，只读。
        :type tags: list[:class:`huaweicloudsdkdataartsstudio.v1.TagVO`]
        :param secrecy_levels: 密级
        :type secrecy_levels: list[:class:`huaweicloudsdkdataartsstudio.v1.SecrecyLevelVO`]
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
        :param code: 逻辑属性编码
        :type code: str
        :param related_logic_attr_id: 关联逻辑属性ID，填写String类型替代Long类型。
        :type related_logic_attr_id: str
        :param related_logic_attr_name: 关联逻辑实体属性中文名称
        :type related_logic_attr_name: str
        :param related_logic_attr_name_en: 关联逻辑实体属性英文名称
        :type related_logic_attr_name_en: str
        """
        
        

        self._id = None
        self._name_en = None
        self._name_ch = None
        self._description = None
        self._obs_location = None
        self._create_by = None
        self._update_by = None
        self._data_type = None
        self._domain_type = None
        self._data_type_extend = None
        self._is_primary_key = None
        self._is_partition_key = None
        self._is_foreign_key = None
        self._extend_field = None
        self._not_null = None
        self._ordinal = None
        self._table_model_id = None
        self._create_time = None
        self._update_time = None
        self._tags = None
        self._secrecy_levels = None
        self._stand_row_id = None
        self._stand_row_name = None
        self._quality_infos = None
        self._alias = None
        self._self_defined_fields = None
        self._code = None
        self._related_logic_attr_id = None
        self._related_logic_attr_name = None
        self._related_logic_attr_name_en = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.name_en = name_en
        self.name_ch = name_ch
        if description is not None:
            self.description = description
        if obs_location is not None:
            self.obs_location = obs_location
        if create_by is not None:
            self.create_by = create_by
        if update_by is not None:
            self.update_by = update_by
        self.data_type = data_type
        if domain_type is not None:
            self.domain_type = domain_type
        if data_type_extend is not None:
            self.data_type_extend = data_type_extend
        self.is_primary_key = is_primary_key
        if is_partition_key is not None:
            self.is_partition_key = is_partition_key
        if is_foreign_key is not None:
            self.is_foreign_key = is_foreign_key
        if extend_field is not None:
            self.extend_field = extend_field
        if not_null is not None:
            self.not_null = not_null
        if ordinal is not None:
            self.ordinal = ordinal
        if table_model_id is not None:
            self.table_model_id = table_model_id
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if tags is not None:
            self.tags = tags
        if secrecy_levels is not None:
            self.secrecy_levels = secrecy_levels
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
        if code is not None:
            self.code = code
        if related_logic_attr_id is not None:
            self.related_logic_attr_id = related_logic_attr_id
        if related_logic_attr_name is not None:
            self.related_logic_attr_name = related_logic_attr_name
        if related_logic_attr_name_en is not None:
            self.related_logic_attr_name_en = related_logic_attr_name_en

    @property
    def id(self):
        """Gets the id of this TableModelAttributeVO.

        编码，填写String类型替代Long类型。

        :return: The id of this TableModelAttributeVO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TableModelAttributeVO.

        编码，填写String类型替代Long类型。

        :param id: The id of this TableModelAttributeVO.
        :type id: str
        """
        self._id = id

    @property
    def name_en(self):
        """Gets the name_en of this TableModelAttributeVO.

        字段名。

        :return: The name_en of this TableModelAttributeVO.
        :rtype: str
        """
        return self._name_en

    @name_en.setter
    def name_en(self, name_en):
        """Sets the name_en of this TableModelAttributeVO.

        字段名。

        :param name_en: The name_en of this TableModelAttributeVO.
        :type name_en: str
        """
        self._name_en = name_en

    @property
    def name_ch(self):
        """Gets the name_ch of this TableModelAttributeVO.

        业务属性。

        :return: The name_ch of this TableModelAttributeVO.
        :rtype: str
        """
        return self._name_ch

    @name_ch.setter
    def name_ch(self, name_ch):
        """Sets the name_ch of this TableModelAttributeVO.

        业务属性。

        :param name_ch: The name_ch of this TableModelAttributeVO.
        :type name_ch: str
        """
        self._name_ch = name_ch

    @property
    def description(self):
        """Gets the description of this TableModelAttributeVO.

        描述。

        :return: The description of this TableModelAttributeVO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TableModelAttributeVO.

        描述。

        :param description: The description of this TableModelAttributeVO.
        :type description: str
        """
        self._description = description

    @property
    def obs_location(self):
        """Gets the obs_location of this TableModelAttributeVO.

        obs路径，子路径。

        :return: The obs_location of this TableModelAttributeVO.
        :rtype: str
        """
        return self._obs_location

    @obs_location.setter
    def obs_location(self, obs_location):
        """Sets the obs_location of this TableModelAttributeVO.

        obs路径，子路径。

        :param obs_location: The obs_location of this TableModelAttributeVO.
        :type obs_location: str
        """
        self._obs_location = obs_location

    @property
    def create_by(self):
        """Gets the create_by of this TableModelAttributeVO.

        创建人。

        :return: The create_by of this TableModelAttributeVO.
        :rtype: str
        """
        return self._create_by

    @create_by.setter
    def create_by(self, create_by):
        """Sets the create_by of this TableModelAttributeVO.

        创建人。

        :param create_by: The create_by of this TableModelAttributeVO.
        :type create_by: str
        """
        self._create_by = create_by

    @property
    def update_by(self):
        """Gets the update_by of this TableModelAttributeVO.

        更新人。

        :return: The update_by of this TableModelAttributeVO.
        :rtype: str
        """
        return self._update_by

    @update_by.setter
    def update_by(self, update_by):
        """Sets the update_by of this TableModelAttributeVO.

        更新人。

        :param update_by: The update_by of this TableModelAttributeVO.
        :type update_by: str
        """
        self._update_by = update_by

    @property
    def data_type(self):
        """Gets the data_type of this TableModelAttributeVO.

        字段类型。

        :return: The data_type of this TableModelAttributeVO.
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """Sets the data_type of this TableModelAttributeVO.

        字段类型。

        :param data_type: The data_type of this TableModelAttributeVO.
        :type data_type: str
        """
        self._data_type = data_type

    @property
    def domain_type(self):
        """Gets the domain_type of this TableModelAttributeVO.

        :return: The domain_type of this TableModelAttributeVO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.DataTypeDomainEnum`
        """
        return self._domain_type

    @domain_type.setter
    def domain_type(self, domain_type):
        """Sets the domain_type of this TableModelAttributeVO.

        :param domain_type: The domain_type of this TableModelAttributeVO.
        :type domain_type: :class:`huaweicloudsdkdataartsstudio.v1.DataTypeDomainEnum`
        """
        self._domain_type = domain_type

    @property
    def data_type_extend(self):
        """Gets the data_type_extend of this TableModelAttributeVO.

        数据类型扩展字段。

        :return: The data_type_extend of this TableModelAttributeVO.
        :rtype: str
        """
        return self._data_type_extend

    @data_type_extend.setter
    def data_type_extend(self, data_type_extend):
        """Sets the data_type_extend of this TableModelAttributeVO.

        数据类型扩展字段。

        :param data_type_extend: The data_type_extend of this TableModelAttributeVO.
        :type data_type_extend: str
        """
        self._data_type_extend = data_type_extend

    @property
    def is_primary_key(self):
        """Gets the is_primary_key of this TableModelAttributeVO.

        是否主键。

        :return: The is_primary_key of this TableModelAttributeVO.
        :rtype: bool
        """
        return self._is_primary_key

    @is_primary_key.setter
    def is_primary_key(self, is_primary_key):
        """Sets the is_primary_key of this TableModelAttributeVO.

        是否主键。

        :param is_primary_key: The is_primary_key of this TableModelAttributeVO.
        :type is_primary_key: bool
        """
        self._is_primary_key = is_primary_key

    @property
    def is_partition_key(self):
        """Gets the is_partition_key of this TableModelAttributeVO.

        是否分区键。

        :return: The is_partition_key of this TableModelAttributeVO.
        :rtype: bool
        """
        return self._is_partition_key

    @is_partition_key.setter
    def is_partition_key(self, is_partition_key):
        """Sets the is_partition_key of this TableModelAttributeVO.

        是否分区键。

        :param is_partition_key: The is_partition_key of this TableModelAttributeVO.
        :type is_partition_key: bool
        """
        self._is_partition_key = is_partition_key

    @property
    def is_foreign_key(self):
        """Gets the is_foreign_key of this TableModelAttributeVO.

        是否外键。

        :return: The is_foreign_key of this TableModelAttributeVO.
        :rtype: bool
        """
        return self._is_foreign_key

    @is_foreign_key.setter
    def is_foreign_key(self, is_foreign_key):
        """Sets the is_foreign_key of this TableModelAttributeVO.

        是否外键。

        :param is_foreign_key: The is_foreign_key of this TableModelAttributeVO.
        :type is_foreign_key: bool
        """
        self._is_foreign_key = is_foreign_key

    @property
    def extend_field(self):
        """Gets the extend_field of this TableModelAttributeVO.

        是否继承的属性。

        :return: The extend_field of this TableModelAttributeVO.
        :rtype: bool
        """
        return self._extend_field

    @extend_field.setter
    def extend_field(self, extend_field):
        """Sets the extend_field of this TableModelAttributeVO.

        是否继承的属性。

        :param extend_field: The extend_field of this TableModelAttributeVO.
        :type extend_field: bool
        """
        self._extend_field = extend_field

    @property
    def not_null(self):
        """Gets the not_null of this TableModelAttributeVO.

        是否不为空。

        :return: The not_null of this TableModelAttributeVO.
        :rtype: bool
        """
        return self._not_null

    @not_null.setter
    def not_null(self, not_null):
        """Sets the not_null of this TableModelAttributeVO.

        是否不为空。

        :param not_null: The not_null of this TableModelAttributeVO.
        :type not_null: bool
        """
        self._not_null = not_null

    @property
    def ordinal(self):
        """Gets the ordinal of this TableModelAttributeVO.

        序号。

        :return: The ordinal of this TableModelAttributeVO.
        :rtype: int
        """
        return self._ordinal

    @ordinal.setter
    def ordinal(self, ordinal):
        """Sets the ordinal of this TableModelAttributeVO.

        序号。

        :param ordinal: The ordinal of this TableModelAttributeVO.
        :type ordinal: int
        """
        self._ordinal = ordinal

    @property
    def table_model_id(self):
        """Gets the table_model_id of this TableModelAttributeVO.

        所属关系建模的模型ID，填写String类型替代Long类型。

        :return: The table_model_id of this TableModelAttributeVO.
        :rtype: str
        """
        return self._table_model_id

    @table_model_id.setter
    def table_model_id(self, table_model_id):
        """Sets the table_model_id of this TableModelAttributeVO.

        所属关系建模的模型ID，填写String类型替代Long类型。

        :param table_model_id: The table_model_id of this TableModelAttributeVO.
        :type table_model_id: str
        """
        self._table_model_id = table_model_id

    @property
    def create_time(self):
        """Gets the create_time of this TableModelAttributeVO.

        创建时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。

        :return: The create_time of this TableModelAttributeVO.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this TableModelAttributeVO.

        创建时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。

        :param create_time: The create_time of this TableModelAttributeVO.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this TableModelAttributeVO.

        更新时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。

        :return: The update_time of this TableModelAttributeVO.
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this TableModelAttributeVO.

        更新时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。

        :param update_time: The update_time of this TableModelAttributeVO.
        :type update_time: datetime
        """
        self._update_time = update_time

    @property
    def tags(self):
        """Gets the tags of this TableModelAttributeVO.

        表标签，只读。

        :return: The tags of this TableModelAttributeVO.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.TagVO`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this TableModelAttributeVO.

        表标签，只读。

        :param tags: The tags of this TableModelAttributeVO.
        :type tags: list[:class:`huaweicloudsdkdataartsstudio.v1.TagVO`]
        """
        self._tags = tags

    @property
    def secrecy_levels(self):
        """Gets the secrecy_levels of this TableModelAttributeVO.

        密级

        :return: The secrecy_levels of this TableModelAttributeVO.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.SecrecyLevelVO`]
        """
        return self._secrecy_levels

    @secrecy_levels.setter
    def secrecy_levels(self, secrecy_levels):
        """Sets the secrecy_levels of this TableModelAttributeVO.

        密级

        :param secrecy_levels: The secrecy_levels of this TableModelAttributeVO.
        :type secrecy_levels: list[:class:`huaweicloudsdkdataartsstudio.v1.SecrecyLevelVO`]
        """
        self._secrecy_levels = secrecy_levels

    @property
    def stand_row_id(self):
        """Gets the stand_row_id of this TableModelAttributeVO.

        关联的数据标准的ID，填写String类型替代Long类型。

        :return: The stand_row_id of this TableModelAttributeVO.
        :rtype: str
        """
        return self._stand_row_id

    @stand_row_id.setter
    def stand_row_id(self, stand_row_id):
        """Sets the stand_row_id of this TableModelAttributeVO.

        关联的数据标准的ID，填写String类型替代Long类型。

        :param stand_row_id: The stand_row_id of this TableModelAttributeVO.
        :type stand_row_id: str
        """
        self._stand_row_id = stand_row_id

    @property
    def stand_row_name(self):
        """Gets the stand_row_name of this TableModelAttributeVO.

        关联的数据标准名称，只读。

        :return: The stand_row_name of this TableModelAttributeVO.
        :rtype: str
        """
        return self._stand_row_name

    @stand_row_name.setter
    def stand_row_name(self, stand_row_name):
        """Sets the stand_row_name of this TableModelAttributeVO.

        关联的数据标准名称，只读。

        :param stand_row_name: The stand_row_name of this TableModelAttributeVO.
        :type stand_row_name: str
        """
        self._stand_row_name = stand_row_name

    @property
    def quality_infos(self):
        """Gets the quality_infos of this TableModelAttributeVO.

        质量信息，只读。

        :return: The quality_infos of this TableModelAttributeVO.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.QualityInfoVO`]
        """
        return self._quality_infos

    @quality_infos.setter
    def quality_infos(self, quality_infos):
        """Sets the quality_infos of this TableModelAttributeVO.

        质量信息，只读。

        :param quality_infos: The quality_infos of this TableModelAttributeVO.
        :type quality_infos: list[:class:`huaweicloudsdkdataartsstudio.v1.QualityInfoVO`]
        """
        self._quality_infos = quality_infos

    @property
    def alias(self):
        """Gets the alias of this TableModelAttributeVO.

        别名。

        :return: The alias of this TableModelAttributeVO.
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """Sets the alias of this TableModelAttributeVO.

        别名。

        :param alias: The alias of this TableModelAttributeVO.
        :type alias: str
        """
        self._alias = alias

    @property
    def self_defined_fields(self):
        """Gets the self_defined_fields of this TableModelAttributeVO.

        自定义项。

        :return: The self_defined_fields of this TableModelAttributeVO.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.SelfDefinedFieldVO`]
        """
        return self._self_defined_fields

    @self_defined_fields.setter
    def self_defined_fields(self, self_defined_fields):
        """Sets the self_defined_fields of this TableModelAttributeVO.

        自定义项。

        :param self_defined_fields: The self_defined_fields of this TableModelAttributeVO.
        :type self_defined_fields: list[:class:`huaweicloudsdkdataartsstudio.v1.SelfDefinedFieldVO`]
        """
        self._self_defined_fields = self_defined_fields

    @property
    def code(self):
        """Gets the code of this TableModelAttributeVO.

        逻辑属性编码

        :return: The code of this TableModelAttributeVO.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this TableModelAttributeVO.

        逻辑属性编码

        :param code: The code of this TableModelAttributeVO.
        :type code: str
        """
        self._code = code

    @property
    def related_logic_attr_id(self):
        """Gets the related_logic_attr_id of this TableModelAttributeVO.

        关联逻辑属性ID，填写String类型替代Long类型。

        :return: The related_logic_attr_id of this TableModelAttributeVO.
        :rtype: str
        """
        return self._related_logic_attr_id

    @related_logic_attr_id.setter
    def related_logic_attr_id(self, related_logic_attr_id):
        """Sets the related_logic_attr_id of this TableModelAttributeVO.

        关联逻辑属性ID，填写String类型替代Long类型。

        :param related_logic_attr_id: The related_logic_attr_id of this TableModelAttributeVO.
        :type related_logic_attr_id: str
        """
        self._related_logic_attr_id = related_logic_attr_id

    @property
    def related_logic_attr_name(self):
        """Gets the related_logic_attr_name of this TableModelAttributeVO.

        关联逻辑实体属性中文名称

        :return: The related_logic_attr_name of this TableModelAttributeVO.
        :rtype: str
        """
        return self._related_logic_attr_name

    @related_logic_attr_name.setter
    def related_logic_attr_name(self, related_logic_attr_name):
        """Sets the related_logic_attr_name of this TableModelAttributeVO.

        关联逻辑实体属性中文名称

        :param related_logic_attr_name: The related_logic_attr_name of this TableModelAttributeVO.
        :type related_logic_attr_name: str
        """
        self._related_logic_attr_name = related_logic_attr_name

    @property
    def related_logic_attr_name_en(self):
        """Gets the related_logic_attr_name_en of this TableModelAttributeVO.

        关联逻辑实体属性英文名称

        :return: The related_logic_attr_name_en of this TableModelAttributeVO.
        :rtype: str
        """
        return self._related_logic_attr_name_en

    @related_logic_attr_name_en.setter
    def related_logic_attr_name_en(self, related_logic_attr_name_en):
        """Sets the related_logic_attr_name_en of this TableModelAttributeVO.

        关联逻辑实体属性英文名称

        :param related_logic_attr_name_en: The related_logic_attr_name_en of this TableModelAttributeVO.
        :type related_logic_attr_name_en: str
        """
        self._related_logic_attr_name_en = related_logic_attr_name_en

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
        if not isinstance(other, TableModelAttributeVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
