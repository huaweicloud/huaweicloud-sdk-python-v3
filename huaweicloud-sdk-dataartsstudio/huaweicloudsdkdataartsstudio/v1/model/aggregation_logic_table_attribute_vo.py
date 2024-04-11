# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AggregationLogicTableAttributeVO:

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
        'aggregation_logic_table_id': 'str',
        'ordinal': 'int',
        'name_en': 'str',
        'name_ch': 'str',
        'attribute_type': 'BizTypeEnum',
        'is_primary_key': 'bool',
        'is_partition_key': 'bool',
        'not_null': 'bool',
        'description': 'str',
        'data_type': 'str',
        'domain_type': 'DataTypeDomainEnum',
        'data_type_extend': 'str',
        'ref_id': 'str',
        'stand_row_id': 'str',
        'stand_row_name': 'str',
        'quality_infos': 'list[QualityInfoVO]',
        'alias': 'str'
    }

    attribute_map = {
        'id': 'id',
        'aggregation_logic_table_id': 'aggregation_logic_table_id',
        'ordinal': 'ordinal',
        'name_en': 'name_en',
        'name_ch': 'name_ch',
        'attribute_type': 'attribute_type',
        'is_primary_key': 'is_primary_key',
        'is_partition_key': 'is_partition_key',
        'not_null': 'not_null',
        'description': 'description',
        'data_type': 'data_type',
        'domain_type': 'domain_type',
        'data_type_extend': 'data_type_extend',
        'ref_id': 'ref_id',
        'stand_row_id': 'stand_row_id',
        'stand_row_name': 'stand_row_name',
        'quality_infos': 'quality_infos',
        'alias': 'alias'
    }

    def __init__(self, id=None, aggregation_logic_table_id=None, ordinal=None, name_en=None, name_ch=None, attribute_type=None, is_primary_key=None, is_partition_key=None, not_null=None, description=None, data_type=None, domain_type=None, data_type_extend=None, ref_id=None, stand_row_id=None, stand_row_name=None, quality_infos=None, alias=None):
        """AggregationLogicTableAttributeVO

        The model defined in huaweicloud sdk

        :param id: 编码。
        :type id: str
        :param aggregation_logic_table_id: 所属汇总表ID。
        :type aggregation_logic_table_id: str
        :param ordinal: 序号。
        :type ordinal: int
        :param name_en: 字段名。
        :type name_en: str
        :param name_ch: 业务属性。
        :type name_ch: str
        :param attribute_type: 
        :type attribute_type: :class:`huaweicloudsdkdataartsstudio.v1.BizTypeEnum`
        :param is_primary_key: 是否主键。
        :type is_primary_key: bool
        :param is_partition_key: 是否分区键。
        :type is_partition_key: bool
        :param not_null: 是否不为空。
        :type not_null: bool
        :param description: 描述。
        :type description: str
        :param data_type: 字段类型。
        :type data_type: str
        :param domain_type: 
        :type domain_type: :class:`huaweicloudsdkdataartsstudio.v1.DataTypeDomainEnum`
        :param data_type_extend: 数据类型扩展字段。
        :type data_type_extend: str
        :param ref_id: 关联ID。
        :type ref_id: str
        :param stand_row_id: 关联的数据标准的ID。
        :type stand_row_id: str
        :param stand_row_name: 关联的数据标准名称。
        :type stand_row_name: str
        :param quality_infos: 质量信息。
        :type quality_infos: list[:class:`huaweicloudsdkdataartsstudio.v1.QualityInfoVO`]
        :param alias: 别名。
        :type alias: str
        """
        
        

        self._id = None
        self._aggregation_logic_table_id = None
        self._ordinal = None
        self._name_en = None
        self._name_ch = None
        self._attribute_type = None
        self._is_primary_key = None
        self._is_partition_key = None
        self._not_null = None
        self._description = None
        self._data_type = None
        self._domain_type = None
        self._data_type_extend = None
        self._ref_id = None
        self._stand_row_id = None
        self._stand_row_name = None
        self._quality_infos = None
        self._alias = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if aggregation_logic_table_id is not None:
            self.aggregation_logic_table_id = aggregation_logic_table_id
        if ordinal is not None:
            self.ordinal = ordinal
        self.name_en = name_en
        self.name_ch = name_ch
        if attribute_type is not None:
            self.attribute_type = attribute_type
        self.is_primary_key = is_primary_key
        self.is_partition_key = is_partition_key
        if not_null is not None:
            self.not_null = not_null
        if description is not None:
            self.description = description
        self.data_type = data_type
        if domain_type is not None:
            self.domain_type = domain_type
        if data_type_extend is not None:
            self.data_type_extend = data_type_extend
        if ref_id is not None:
            self.ref_id = ref_id
        if stand_row_id is not None:
            self.stand_row_id = stand_row_id
        if stand_row_name is not None:
            self.stand_row_name = stand_row_name
        if quality_infos is not None:
            self.quality_infos = quality_infos
        if alias is not None:
            self.alias = alias

    @property
    def id(self):
        """Gets the id of this AggregationLogicTableAttributeVO.

        编码。

        :return: The id of this AggregationLogicTableAttributeVO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AggregationLogicTableAttributeVO.

        编码。

        :param id: The id of this AggregationLogicTableAttributeVO.
        :type id: str
        """
        self._id = id

    @property
    def aggregation_logic_table_id(self):
        """Gets the aggregation_logic_table_id of this AggregationLogicTableAttributeVO.

        所属汇总表ID。

        :return: The aggregation_logic_table_id of this AggregationLogicTableAttributeVO.
        :rtype: str
        """
        return self._aggregation_logic_table_id

    @aggregation_logic_table_id.setter
    def aggregation_logic_table_id(self, aggregation_logic_table_id):
        """Sets the aggregation_logic_table_id of this AggregationLogicTableAttributeVO.

        所属汇总表ID。

        :param aggregation_logic_table_id: The aggregation_logic_table_id of this AggregationLogicTableAttributeVO.
        :type aggregation_logic_table_id: str
        """
        self._aggregation_logic_table_id = aggregation_logic_table_id

    @property
    def ordinal(self):
        """Gets the ordinal of this AggregationLogicTableAttributeVO.

        序号。

        :return: The ordinal of this AggregationLogicTableAttributeVO.
        :rtype: int
        """
        return self._ordinal

    @ordinal.setter
    def ordinal(self, ordinal):
        """Sets the ordinal of this AggregationLogicTableAttributeVO.

        序号。

        :param ordinal: The ordinal of this AggregationLogicTableAttributeVO.
        :type ordinal: int
        """
        self._ordinal = ordinal

    @property
    def name_en(self):
        """Gets the name_en of this AggregationLogicTableAttributeVO.

        字段名。

        :return: The name_en of this AggregationLogicTableAttributeVO.
        :rtype: str
        """
        return self._name_en

    @name_en.setter
    def name_en(self, name_en):
        """Sets the name_en of this AggregationLogicTableAttributeVO.

        字段名。

        :param name_en: The name_en of this AggregationLogicTableAttributeVO.
        :type name_en: str
        """
        self._name_en = name_en

    @property
    def name_ch(self):
        """Gets the name_ch of this AggregationLogicTableAttributeVO.

        业务属性。

        :return: The name_ch of this AggregationLogicTableAttributeVO.
        :rtype: str
        """
        return self._name_ch

    @name_ch.setter
    def name_ch(self, name_ch):
        """Sets the name_ch of this AggregationLogicTableAttributeVO.

        业务属性。

        :param name_ch: The name_ch of this AggregationLogicTableAttributeVO.
        :type name_ch: str
        """
        self._name_ch = name_ch

    @property
    def attribute_type(self):
        """Gets the attribute_type of this AggregationLogicTableAttributeVO.

        :return: The attribute_type of this AggregationLogicTableAttributeVO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.BizTypeEnum`
        """
        return self._attribute_type

    @attribute_type.setter
    def attribute_type(self, attribute_type):
        """Sets the attribute_type of this AggregationLogicTableAttributeVO.

        :param attribute_type: The attribute_type of this AggregationLogicTableAttributeVO.
        :type attribute_type: :class:`huaweicloudsdkdataartsstudio.v1.BizTypeEnum`
        """
        self._attribute_type = attribute_type

    @property
    def is_primary_key(self):
        """Gets the is_primary_key of this AggregationLogicTableAttributeVO.

        是否主键。

        :return: The is_primary_key of this AggregationLogicTableAttributeVO.
        :rtype: bool
        """
        return self._is_primary_key

    @is_primary_key.setter
    def is_primary_key(self, is_primary_key):
        """Sets the is_primary_key of this AggregationLogicTableAttributeVO.

        是否主键。

        :param is_primary_key: The is_primary_key of this AggregationLogicTableAttributeVO.
        :type is_primary_key: bool
        """
        self._is_primary_key = is_primary_key

    @property
    def is_partition_key(self):
        """Gets the is_partition_key of this AggregationLogicTableAttributeVO.

        是否分区键。

        :return: The is_partition_key of this AggregationLogicTableAttributeVO.
        :rtype: bool
        """
        return self._is_partition_key

    @is_partition_key.setter
    def is_partition_key(self, is_partition_key):
        """Sets the is_partition_key of this AggregationLogicTableAttributeVO.

        是否分区键。

        :param is_partition_key: The is_partition_key of this AggregationLogicTableAttributeVO.
        :type is_partition_key: bool
        """
        self._is_partition_key = is_partition_key

    @property
    def not_null(self):
        """Gets the not_null of this AggregationLogicTableAttributeVO.

        是否不为空。

        :return: The not_null of this AggregationLogicTableAttributeVO.
        :rtype: bool
        """
        return self._not_null

    @not_null.setter
    def not_null(self, not_null):
        """Sets the not_null of this AggregationLogicTableAttributeVO.

        是否不为空。

        :param not_null: The not_null of this AggregationLogicTableAttributeVO.
        :type not_null: bool
        """
        self._not_null = not_null

    @property
    def description(self):
        """Gets the description of this AggregationLogicTableAttributeVO.

        描述。

        :return: The description of this AggregationLogicTableAttributeVO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AggregationLogicTableAttributeVO.

        描述。

        :param description: The description of this AggregationLogicTableAttributeVO.
        :type description: str
        """
        self._description = description

    @property
    def data_type(self):
        """Gets the data_type of this AggregationLogicTableAttributeVO.

        字段类型。

        :return: The data_type of this AggregationLogicTableAttributeVO.
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """Sets the data_type of this AggregationLogicTableAttributeVO.

        字段类型。

        :param data_type: The data_type of this AggregationLogicTableAttributeVO.
        :type data_type: str
        """
        self._data_type = data_type

    @property
    def domain_type(self):
        """Gets the domain_type of this AggregationLogicTableAttributeVO.

        :return: The domain_type of this AggregationLogicTableAttributeVO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.DataTypeDomainEnum`
        """
        return self._domain_type

    @domain_type.setter
    def domain_type(self, domain_type):
        """Sets the domain_type of this AggregationLogicTableAttributeVO.

        :param domain_type: The domain_type of this AggregationLogicTableAttributeVO.
        :type domain_type: :class:`huaweicloudsdkdataartsstudio.v1.DataTypeDomainEnum`
        """
        self._domain_type = domain_type

    @property
    def data_type_extend(self):
        """Gets the data_type_extend of this AggregationLogicTableAttributeVO.

        数据类型扩展字段。

        :return: The data_type_extend of this AggregationLogicTableAttributeVO.
        :rtype: str
        """
        return self._data_type_extend

    @data_type_extend.setter
    def data_type_extend(self, data_type_extend):
        """Sets the data_type_extend of this AggregationLogicTableAttributeVO.

        数据类型扩展字段。

        :param data_type_extend: The data_type_extend of this AggregationLogicTableAttributeVO.
        :type data_type_extend: str
        """
        self._data_type_extend = data_type_extend

    @property
    def ref_id(self):
        """Gets the ref_id of this AggregationLogicTableAttributeVO.

        关联ID。

        :return: The ref_id of this AggregationLogicTableAttributeVO.
        :rtype: str
        """
        return self._ref_id

    @ref_id.setter
    def ref_id(self, ref_id):
        """Sets the ref_id of this AggregationLogicTableAttributeVO.

        关联ID。

        :param ref_id: The ref_id of this AggregationLogicTableAttributeVO.
        :type ref_id: str
        """
        self._ref_id = ref_id

    @property
    def stand_row_id(self):
        """Gets the stand_row_id of this AggregationLogicTableAttributeVO.

        关联的数据标准的ID。

        :return: The stand_row_id of this AggregationLogicTableAttributeVO.
        :rtype: str
        """
        return self._stand_row_id

    @stand_row_id.setter
    def stand_row_id(self, stand_row_id):
        """Sets the stand_row_id of this AggregationLogicTableAttributeVO.

        关联的数据标准的ID。

        :param stand_row_id: The stand_row_id of this AggregationLogicTableAttributeVO.
        :type stand_row_id: str
        """
        self._stand_row_id = stand_row_id

    @property
    def stand_row_name(self):
        """Gets the stand_row_name of this AggregationLogicTableAttributeVO.

        关联的数据标准名称。

        :return: The stand_row_name of this AggregationLogicTableAttributeVO.
        :rtype: str
        """
        return self._stand_row_name

    @stand_row_name.setter
    def stand_row_name(self, stand_row_name):
        """Sets the stand_row_name of this AggregationLogicTableAttributeVO.

        关联的数据标准名称。

        :param stand_row_name: The stand_row_name of this AggregationLogicTableAttributeVO.
        :type stand_row_name: str
        """
        self._stand_row_name = stand_row_name

    @property
    def quality_infos(self):
        """Gets the quality_infos of this AggregationLogicTableAttributeVO.

        质量信息。

        :return: The quality_infos of this AggregationLogicTableAttributeVO.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.QualityInfoVO`]
        """
        return self._quality_infos

    @quality_infos.setter
    def quality_infos(self, quality_infos):
        """Sets the quality_infos of this AggregationLogicTableAttributeVO.

        质量信息。

        :param quality_infos: The quality_infos of this AggregationLogicTableAttributeVO.
        :type quality_infos: list[:class:`huaweicloudsdkdataartsstudio.v1.QualityInfoVO`]
        """
        self._quality_infos = quality_infos

    @property
    def alias(self):
        """Gets the alias of this AggregationLogicTableAttributeVO.

        别名。

        :return: The alias of this AggregationLogicTableAttributeVO.
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """Sets the alias of this AggregationLogicTableAttributeVO.

        别名。

        :param alias: The alias of this AggregationLogicTableAttributeVO.
        :type alias: str
        """
        self._alias = alias

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
        if not isinstance(other, AggregationLogicTableAttributeVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
