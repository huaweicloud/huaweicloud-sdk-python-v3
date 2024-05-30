# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DimensionAttributeVO:

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
        'dimension_id': 'str',
        'code_table_field_id': 'str',
        'name_en': 'str',
        'name_ch': 'str',
        'description': 'str',
        'create_by': 'str',
        'data_type': 'str',
        'domain_type': 'DataTypeDomainEnum',
        'data_type_extend': 'str',
        'is_primary_key': 'bool',
        'is_biz_primary': 'bool',
        'is_partition_key': 'bool',
        'ordinal': 'int',
        'not_null': 'bool',
        'stand_row_id': 'str',
        'stand_row_name': 'str',
        'quality_infos': 'list[QualityInfoVO]',
        'secrecy_levels': 'list[SecrecyLevelVO]',
        'status': 'BizStatusEnum',
        'create_time': 'datetime',
        'update_time': 'datetime',
        'alias': 'str',
        'self_defined_fields': 'list[SelfDefinedFieldVO]'
    }

    attribute_map = {
        'id': 'id',
        'dimension_id': 'dimension_id',
        'code_table_field_id': 'code_table_field_id',
        'name_en': 'name_en',
        'name_ch': 'name_ch',
        'description': 'description',
        'create_by': 'create_by',
        'data_type': 'data_type',
        'domain_type': 'domain_type',
        'data_type_extend': 'data_type_extend',
        'is_primary_key': 'is_primary_key',
        'is_biz_primary': 'is_biz_primary',
        'is_partition_key': 'is_partition_key',
        'ordinal': 'ordinal',
        'not_null': 'not_null',
        'stand_row_id': 'stand_row_id',
        'stand_row_name': 'stand_row_name',
        'quality_infos': 'quality_infos',
        'secrecy_levels': 'secrecy_levels',
        'status': 'status',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'alias': 'alias',
        'self_defined_fields': 'self_defined_fields'
    }

    def __init__(self, id=None, dimension_id=None, code_table_field_id=None, name_en=None, name_ch=None, description=None, create_by=None, data_type=None, domain_type=None, data_type_extend=None, is_primary_key=None, is_biz_primary=None, is_partition_key=None, ordinal=None, not_null=None, stand_row_id=None, stand_row_name=None, quality_infos=None, secrecy_levels=None, status=None, create_time=None, update_time=None, alias=None, self_defined_fields=None):
        """DimensionAttributeVO

        The model defined in huaweicloud sdk

        :param id: 编码，填写String类型替代Long类型。
        :type id: str
        :param dimension_id: 维度ID，只读，填写String类型替代Long类型。
        :type dimension_id: str
        :param code_table_field_id: 码表属性ID，填写String类型替代Long类型。
        :type code_table_field_id: str
        :param name_en: 字段名。
        :type name_en: str
        :param name_ch: 业务属性。
        :type name_ch: str
        :param description: 描述。
        :type description: str
        :param create_by: 创建人。
        :type create_by: str
        :param data_type: 字段类型。
        :type data_type: str
        :param domain_type: 
        :type domain_type: :class:`huaweicloudsdkdataartsstudio.v1.DataTypeDomainEnum`
        :param data_type_extend: 数据类型扩展字段。
        :type data_type_extend: str
        :param is_primary_key: 是否主键。
        :type is_primary_key: bool
        :param is_biz_primary: 是否业务主键。
        :type is_biz_primary: bool
        :param is_partition_key: 是否分区。
        :type is_partition_key: bool
        :param ordinal: 序号。
        :type ordinal: int
        :param not_null: 是否不为空。
        :type not_null: bool
        :param stand_row_id: 关联的数据标准的ID，填写String类型替代Long类型。
        :type stand_row_id: str
        :param stand_row_name: 关联的数据标准名称，只读。
        :type stand_row_name: str
        :param quality_infos: 质量信息，只读。
        :type quality_infos: list[:class:`huaweicloudsdkdataartsstudio.v1.QualityInfoVO`]
        :param secrecy_levels: 密级
        :type secrecy_levels: list[:class:`huaweicloudsdkdataartsstudio.v1.SecrecyLevelVO`]
        :param status: 
        :type status: :class:`huaweicloudsdkdataartsstudio.v1.BizStatusEnum`
        :param create_time: 创建时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。
        :type create_time: datetime
        :param update_time: 更新时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。
        :type update_time: datetime
        :param alias: 别名
        :type alias: str
        :param self_defined_fields: 自定义项。
        :type self_defined_fields: list[:class:`huaweicloudsdkdataartsstudio.v1.SelfDefinedFieldVO`]
        """
        
        

        self._id = None
        self._dimension_id = None
        self._code_table_field_id = None
        self._name_en = None
        self._name_ch = None
        self._description = None
        self._create_by = None
        self._data_type = None
        self._domain_type = None
        self._data_type_extend = None
        self._is_primary_key = None
        self._is_biz_primary = None
        self._is_partition_key = None
        self._ordinal = None
        self._not_null = None
        self._stand_row_id = None
        self._stand_row_name = None
        self._quality_infos = None
        self._secrecy_levels = None
        self._status = None
        self._create_time = None
        self._update_time = None
        self._alias = None
        self._self_defined_fields = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if dimension_id is not None:
            self.dimension_id = dimension_id
        if code_table_field_id is not None:
            self.code_table_field_id = code_table_field_id
        self.name_en = name_en
        self.name_ch = name_ch
        if description is not None:
            self.description = description
        if create_by is not None:
            self.create_by = create_by
        self.data_type = data_type
        if domain_type is not None:
            self.domain_type = domain_type
        if data_type_extend is not None:
            self.data_type_extend = data_type_extend
        self.is_primary_key = is_primary_key
        if is_biz_primary is not None:
            self.is_biz_primary = is_biz_primary
        if is_partition_key is not None:
            self.is_partition_key = is_partition_key
        self.ordinal = ordinal
        if not_null is not None:
            self.not_null = not_null
        if stand_row_id is not None:
            self.stand_row_id = stand_row_id
        if stand_row_name is not None:
            self.stand_row_name = stand_row_name
        if quality_infos is not None:
            self.quality_infos = quality_infos
        if secrecy_levels is not None:
            self.secrecy_levels = secrecy_levels
        if status is not None:
            self.status = status
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if alias is not None:
            self.alias = alias
        if self_defined_fields is not None:
            self.self_defined_fields = self_defined_fields

    @property
    def id(self):
        """Gets the id of this DimensionAttributeVO.

        编码，填写String类型替代Long类型。

        :return: The id of this DimensionAttributeVO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DimensionAttributeVO.

        编码，填写String类型替代Long类型。

        :param id: The id of this DimensionAttributeVO.
        :type id: str
        """
        self._id = id

    @property
    def dimension_id(self):
        """Gets the dimension_id of this DimensionAttributeVO.

        维度ID，只读，填写String类型替代Long类型。

        :return: The dimension_id of this DimensionAttributeVO.
        :rtype: str
        """
        return self._dimension_id

    @dimension_id.setter
    def dimension_id(self, dimension_id):
        """Sets the dimension_id of this DimensionAttributeVO.

        维度ID，只读，填写String类型替代Long类型。

        :param dimension_id: The dimension_id of this DimensionAttributeVO.
        :type dimension_id: str
        """
        self._dimension_id = dimension_id

    @property
    def code_table_field_id(self):
        """Gets the code_table_field_id of this DimensionAttributeVO.

        码表属性ID，填写String类型替代Long类型。

        :return: The code_table_field_id of this DimensionAttributeVO.
        :rtype: str
        """
        return self._code_table_field_id

    @code_table_field_id.setter
    def code_table_field_id(self, code_table_field_id):
        """Sets the code_table_field_id of this DimensionAttributeVO.

        码表属性ID，填写String类型替代Long类型。

        :param code_table_field_id: The code_table_field_id of this DimensionAttributeVO.
        :type code_table_field_id: str
        """
        self._code_table_field_id = code_table_field_id

    @property
    def name_en(self):
        """Gets the name_en of this DimensionAttributeVO.

        字段名。

        :return: The name_en of this DimensionAttributeVO.
        :rtype: str
        """
        return self._name_en

    @name_en.setter
    def name_en(self, name_en):
        """Sets the name_en of this DimensionAttributeVO.

        字段名。

        :param name_en: The name_en of this DimensionAttributeVO.
        :type name_en: str
        """
        self._name_en = name_en

    @property
    def name_ch(self):
        """Gets the name_ch of this DimensionAttributeVO.

        业务属性。

        :return: The name_ch of this DimensionAttributeVO.
        :rtype: str
        """
        return self._name_ch

    @name_ch.setter
    def name_ch(self, name_ch):
        """Sets the name_ch of this DimensionAttributeVO.

        业务属性。

        :param name_ch: The name_ch of this DimensionAttributeVO.
        :type name_ch: str
        """
        self._name_ch = name_ch

    @property
    def description(self):
        """Gets the description of this DimensionAttributeVO.

        描述。

        :return: The description of this DimensionAttributeVO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DimensionAttributeVO.

        描述。

        :param description: The description of this DimensionAttributeVO.
        :type description: str
        """
        self._description = description

    @property
    def create_by(self):
        """Gets the create_by of this DimensionAttributeVO.

        创建人。

        :return: The create_by of this DimensionAttributeVO.
        :rtype: str
        """
        return self._create_by

    @create_by.setter
    def create_by(self, create_by):
        """Sets the create_by of this DimensionAttributeVO.

        创建人。

        :param create_by: The create_by of this DimensionAttributeVO.
        :type create_by: str
        """
        self._create_by = create_by

    @property
    def data_type(self):
        """Gets the data_type of this DimensionAttributeVO.

        字段类型。

        :return: The data_type of this DimensionAttributeVO.
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """Sets the data_type of this DimensionAttributeVO.

        字段类型。

        :param data_type: The data_type of this DimensionAttributeVO.
        :type data_type: str
        """
        self._data_type = data_type

    @property
    def domain_type(self):
        """Gets the domain_type of this DimensionAttributeVO.

        :return: The domain_type of this DimensionAttributeVO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.DataTypeDomainEnum`
        """
        return self._domain_type

    @domain_type.setter
    def domain_type(self, domain_type):
        """Sets the domain_type of this DimensionAttributeVO.

        :param domain_type: The domain_type of this DimensionAttributeVO.
        :type domain_type: :class:`huaweicloudsdkdataartsstudio.v1.DataTypeDomainEnum`
        """
        self._domain_type = domain_type

    @property
    def data_type_extend(self):
        """Gets the data_type_extend of this DimensionAttributeVO.

        数据类型扩展字段。

        :return: The data_type_extend of this DimensionAttributeVO.
        :rtype: str
        """
        return self._data_type_extend

    @data_type_extend.setter
    def data_type_extend(self, data_type_extend):
        """Sets the data_type_extend of this DimensionAttributeVO.

        数据类型扩展字段。

        :param data_type_extend: The data_type_extend of this DimensionAttributeVO.
        :type data_type_extend: str
        """
        self._data_type_extend = data_type_extend

    @property
    def is_primary_key(self):
        """Gets the is_primary_key of this DimensionAttributeVO.

        是否主键。

        :return: The is_primary_key of this DimensionAttributeVO.
        :rtype: bool
        """
        return self._is_primary_key

    @is_primary_key.setter
    def is_primary_key(self, is_primary_key):
        """Sets the is_primary_key of this DimensionAttributeVO.

        是否主键。

        :param is_primary_key: The is_primary_key of this DimensionAttributeVO.
        :type is_primary_key: bool
        """
        self._is_primary_key = is_primary_key

    @property
    def is_biz_primary(self):
        """Gets the is_biz_primary of this DimensionAttributeVO.

        是否业务主键。

        :return: The is_biz_primary of this DimensionAttributeVO.
        :rtype: bool
        """
        return self._is_biz_primary

    @is_biz_primary.setter
    def is_biz_primary(self, is_biz_primary):
        """Sets the is_biz_primary of this DimensionAttributeVO.

        是否业务主键。

        :param is_biz_primary: The is_biz_primary of this DimensionAttributeVO.
        :type is_biz_primary: bool
        """
        self._is_biz_primary = is_biz_primary

    @property
    def is_partition_key(self):
        """Gets the is_partition_key of this DimensionAttributeVO.

        是否分区。

        :return: The is_partition_key of this DimensionAttributeVO.
        :rtype: bool
        """
        return self._is_partition_key

    @is_partition_key.setter
    def is_partition_key(self, is_partition_key):
        """Sets the is_partition_key of this DimensionAttributeVO.

        是否分区。

        :param is_partition_key: The is_partition_key of this DimensionAttributeVO.
        :type is_partition_key: bool
        """
        self._is_partition_key = is_partition_key

    @property
    def ordinal(self):
        """Gets the ordinal of this DimensionAttributeVO.

        序号。

        :return: The ordinal of this DimensionAttributeVO.
        :rtype: int
        """
        return self._ordinal

    @ordinal.setter
    def ordinal(self, ordinal):
        """Sets the ordinal of this DimensionAttributeVO.

        序号。

        :param ordinal: The ordinal of this DimensionAttributeVO.
        :type ordinal: int
        """
        self._ordinal = ordinal

    @property
    def not_null(self):
        """Gets the not_null of this DimensionAttributeVO.

        是否不为空。

        :return: The not_null of this DimensionAttributeVO.
        :rtype: bool
        """
        return self._not_null

    @not_null.setter
    def not_null(self, not_null):
        """Sets the not_null of this DimensionAttributeVO.

        是否不为空。

        :param not_null: The not_null of this DimensionAttributeVO.
        :type not_null: bool
        """
        self._not_null = not_null

    @property
    def stand_row_id(self):
        """Gets the stand_row_id of this DimensionAttributeVO.

        关联的数据标准的ID，填写String类型替代Long类型。

        :return: The stand_row_id of this DimensionAttributeVO.
        :rtype: str
        """
        return self._stand_row_id

    @stand_row_id.setter
    def stand_row_id(self, stand_row_id):
        """Sets the stand_row_id of this DimensionAttributeVO.

        关联的数据标准的ID，填写String类型替代Long类型。

        :param stand_row_id: The stand_row_id of this DimensionAttributeVO.
        :type stand_row_id: str
        """
        self._stand_row_id = stand_row_id

    @property
    def stand_row_name(self):
        """Gets the stand_row_name of this DimensionAttributeVO.

        关联的数据标准名称，只读。

        :return: The stand_row_name of this DimensionAttributeVO.
        :rtype: str
        """
        return self._stand_row_name

    @stand_row_name.setter
    def stand_row_name(self, stand_row_name):
        """Sets the stand_row_name of this DimensionAttributeVO.

        关联的数据标准名称，只读。

        :param stand_row_name: The stand_row_name of this DimensionAttributeVO.
        :type stand_row_name: str
        """
        self._stand_row_name = stand_row_name

    @property
    def quality_infos(self):
        """Gets the quality_infos of this DimensionAttributeVO.

        质量信息，只读。

        :return: The quality_infos of this DimensionAttributeVO.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.QualityInfoVO`]
        """
        return self._quality_infos

    @quality_infos.setter
    def quality_infos(self, quality_infos):
        """Sets the quality_infos of this DimensionAttributeVO.

        质量信息，只读。

        :param quality_infos: The quality_infos of this DimensionAttributeVO.
        :type quality_infos: list[:class:`huaweicloudsdkdataartsstudio.v1.QualityInfoVO`]
        """
        self._quality_infos = quality_infos

    @property
    def secrecy_levels(self):
        """Gets the secrecy_levels of this DimensionAttributeVO.

        密级

        :return: The secrecy_levels of this DimensionAttributeVO.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.SecrecyLevelVO`]
        """
        return self._secrecy_levels

    @secrecy_levels.setter
    def secrecy_levels(self, secrecy_levels):
        """Sets the secrecy_levels of this DimensionAttributeVO.

        密级

        :param secrecy_levels: The secrecy_levels of this DimensionAttributeVO.
        :type secrecy_levels: list[:class:`huaweicloudsdkdataartsstudio.v1.SecrecyLevelVO`]
        """
        self._secrecy_levels = secrecy_levels

    @property
    def status(self):
        """Gets the status of this DimensionAttributeVO.

        :return: The status of this DimensionAttributeVO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.BizStatusEnum`
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DimensionAttributeVO.

        :param status: The status of this DimensionAttributeVO.
        :type status: :class:`huaweicloudsdkdataartsstudio.v1.BizStatusEnum`
        """
        self._status = status

    @property
    def create_time(self):
        """Gets the create_time of this DimensionAttributeVO.

        创建时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。

        :return: The create_time of this DimensionAttributeVO.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this DimensionAttributeVO.

        创建时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。

        :param create_time: The create_time of this DimensionAttributeVO.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this DimensionAttributeVO.

        更新时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。

        :return: The update_time of this DimensionAttributeVO.
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this DimensionAttributeVO.

        更新时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。

        :param update_time: The update_time of this DimensionAttributeVO.
        :type update_time: datetime
        """
        self._update_time = update_time

    @property
    def alias(self):
        """Gets the alias of this DimensionAttributeVO.

        别名

        :return: The alias of this DimensionAttributeVO.
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """Sets the alias of this DimensionAttributeVO.

        别名

        :param alias: The alias of this DimensionAttributeVO.
        :type alias: str
        """
        self._alias = alias

    @property
    def self_defined_fields(self):
        """Gets the self_defined_fields of this DimensionAttributeVO.

        自定义项。

        :return: The self_defined_fields of this DimensionAttributeVO.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.SelfDefinedFieldVO`]
        """
        return self._self_defined_fields

    @self_defined_fields.setter
    def self_defined_fields(self, self_defined_fields):
        """Sets the self_defined_fields of this DimensionAttributeVO.

        自定义项。

        :param self_defined_fields: The self_defined_fields of this DimensionAttributeVO.
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
        if not isinstance(other, DimensionAttributeVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
