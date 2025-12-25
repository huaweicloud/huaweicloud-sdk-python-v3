# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DerivativeIndexDimensionVO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'group_id': 'str',
        'role': 'str',
        'dimension_id': 'str',
        'hierarchies_id': 'str',
        'ordinal': 'int',
        'group_name': 'str',
        'group_code': 'str',
        'biz_type': 'str',
        'hierarchies': 'list[DimensionHierarchiesVO]',
        'l1': 'str',
        'l2': 'str',
        'l3': 'str',
        'l1_id': 'str',
        'l2_id': 'str',
        'l3_id': 'str',
        'dw_type': 'str',
        'id': 'str'
    }

    attribute_map = {
        'group_id': 'group_id',
        'role': 'role',
        'dimension_id': 'dimension_id',
        'hierarchies_id': 'hierarchies_id',
        'ordinal': 'ordinal',
        'group_name': 'group_name',
        'group_code': 'group_code',
        'biz_type': 'biz_type',
        'hierarchies': 'hierarchies',
        'l1': 'l1',
        'l2': 'l2',
        'l3': 'l3',
        'l1_id': 'l1_id',
        'l2_id': 'l2_id',
        'l3_id': 'l3_id',
        'dw_type': 'dw_type',
        'id': 'id'
    }

    def __init__(self, group_id=None, role=None, dimension_id=None, hierarchies_id=None, ordinal=None, group_name=None, group_code=None, biz_type=None, hierarchies=None, l1=None, l2=None, l3=None, l1_id=None, l2_id=None, l3_id=None, dw_type=None, id=None):
        r"""DerivativeIndexDimensionVO

        The model defined in huaweicloud sdk

        :param group_id: 维度分组ID。
        :type group_id: str
        :param role: 维度角色。
        :type role: str
        :param dimension_id: 维度ID，ID字符串。
        :type dimension_id: str
        :param hierarchies_id: 维度层级ID，ID字符串。
        :type hierarchies_id: str
        :param ordinal: 序号，只读。
        :type ordinal: int
        :param group_name: 维度分组名称。
        :type group_name: str
        :param group_code: 维度分组编码。
        :type group_code: str
        :param biz_type: 业务实体类型。 枚举值：  - AGGREGATION_LOGIC_TABLE: 汇总表  - ATOMIC_INDEX: 原子指标  - ATOMIC_METRIC: 原子指标（新）  - BIZ_CATALOG: 流程架构目录  - BIZ_METRIC: 业务指标  - CODE_TABLE: 码表  - COMMON_CONDITION: 通用限定  - COMPOSITE_METRIC: 复合指标（新）  - COMPOUND_METRIC: 复合指标  - CONDITION_GROUP: 限定分组  - DEGENERATE_DIMENSION: 退化维度  - DERIVATIVE_INDEX: 衍生指标  - DERIVED_METRIC: 衍生指标（新）  - DIMENSION: 维度  - DIMENSION_ATTRIBUTE: 维度属性  - DIMENSION_HIERARCHIES: 维度层级  - DIMENSION_LOGIC_TABLE: 维度表  - DIMENSION_TABLE_ATTRIBUTE: 维度属性  - DIRECTORY: 目录  - FACT_ATTRIBUTE: 事实表属性  - FACT_DIMENSION: 事实表维度  - FACT_LOGIC_TABLE: 事实表  - FACT_MEASURE: 事实表度量  - FUNCTION: 函数  - INFO_ARCH: 信息架构（批量修改主题使用）  - MODEL: 模型  - QUALITY_RULE: 质量规则  - SECRECY_LEVEL: 密级  - STANDARD_ELEMENT: 数据标准  - STANDARD_ELEMENT_TEMPLATE: 数据标准模板  - SUBJECT: 主题  - SUMMARY_DIMENSION_ATTRIBUTE: 汇总表维度属性  - SUMMARY_INDEX: 汇总表指标属性  - SUMMARY_TIME: 汇总表时间周期属性  - TABLE_MODEL: 关系模型（逻辑模型/物理模型）  - TABLE_MODEL_ATTRIBUTE: 关系模型属性（逻辑模型/物理模型）  - TABLE_MODEL_LOGIC: 逻辑实体  - TABLE_TYPE: 表类型  - TAG: 标签  - TIME_CONDITION: 时间限定 
        :type biz_type: str
        :param hierarchies: 层级属性，只读。
        :type hierarchies: list[:class:`huaweicloudsdkdataartsstudio.v1.DimensionHierarchiesVO`]
        :param l1: 主题域分组中文名，只读，创建和更新时无需填写。
        :type l1: str
        :param l2: 主题域中文名，只读，创建和更新时无需填写。
        :type l2: str
        :param l3: 业务对象中文名，只读，创建和更新时无需填写。
        :type l3: str
        :param l1_id: 主题域分组ID，只读，ID字符串。
        :type l1_id: str
        :param l2_id: 主题域ID，只读，创建和更新时无需填写。
        :type l2_id: str
        :param l3_id: 业务对象ID，只读，ID字符串。
        :type l3_id: str
        :param dw_type: 数据连接类型。
        :type dw_type: str
        :param id: 层级的ID，只读，ID字符串。
        :type id: str
        """
        
        

        self._group_id = None
        self._role = None
        self._dimension_id = None
        self._hierarchies_id = None
        self._ordinal = None
        self._group_name = None
        self._group_code = None
        self._biz_type = None
        self._hierarchies = None
        self._l1 = None
        self._l2 = None
        self._l3 = None
        self._l1_id = None
        self._l2_id = None
        self._l3_id = None
        self._dw_type = None
        self._id = None
        self.discriminator = None

        self.group_id = group_id
        if role is not None:
            self.role = role
        if dimension_id is not None:
            self.dimension_id = dimension_id
        if hierarchies_id is not None:
            self.hierarchies_id = hierarchies_id
        if ordinal is not None:
            self.ordinal = ordinal
        if group_name is not None:
            self.group_name = group_name
        if group_code is not None:
            self.group_code = group_code
        self.biz_type = biz_type
        if hierarchies is not None:
            self.hierarchies = hierarchies
        if l1 is not None:
            self.l1 = l1
        if l2 is not None:
            self.l2 = l2
        if l3 is not None:
            self.l3 = l3
        if l1_id is not None:
            self.l1_id = l1_id
        if l2_id is not None:
            self.l2_id = l2_id
        if l3_id is not None:
            self.l3_id = l3_id
        if dw_type is not None:
            self.dw_type = dw_type
        if id is not None:
            self.id = id

    @property
    def group_id(self):
        r"""Gets the group_id of this DerivativeIndexDimensionVO.

        维度分组ID。

        :return: The group_id of this DerivativeIndexDimensionVO.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this DerivativeIndexDimensionVO.

        维度分组ID。

        :param group_id: The group_id of this DerivativeIndexDimensionVO.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def role(self):
        r"""Gets the role of this DerivativeIndexDimensionVO.

        维度角色。

        :return: The role of this DerivativeIndexDimensionVO.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        r"""Sets the role of this DerivativeIndexDimensionVO.

        维度角色。

        :param role: The role of this DerivativeIndexDimensionVO.
        :type role: str
        """
        self._role = role

    @property
    def dimension_id(self):
        r"""Gets the dimension_id of this DerivativeIndexDimensionVO.

        维度ID，ID字符串。

        :return: The dimension_id of this DerivativeIndexDimensionVO.
        :rtype: str
        """
        return self._dimension_id

    @dimension_id.setter
    def dimension_id(self, dimension_id):
        r"""Sets the dimension_id of this DerivativeIndexDimensionVO.

        维度ID，ID字符串。

        :param dimension_id: The dimension_id of this DerivativeIndexDimensionVO.
        :type dimension_id: str
        """
        self._dimension_id = dimension_id

    @property
    def hierarchies_id(self):
        r"""Gets the hierarchies_id of this DerivativeIndexDimensionVO.

        维度层级ID，ID字符串。

        :return: The hierarchies_id of this DerivativeIndexDimensionVO.
        :rtype: str
        """
        return self._hierarchies_id

    @hierarchies_id.setter
    def hierarchies_id(self, hierarchies_id):
        r"""Sets the hierarchies_id of this DerivativeIndexDimensionVO.

        维度层级ID，ID字符串。

        :param hierarchies_id: The hierarchies_id of this DerivativeIndexDimensionVO.
        :type hierarchies_id: str
        """
        self._hierarchies_id = hierarchies_id

    @property
    def ordinal(self):
        r"""Gets the ordinal of this DerivativeIndexDimensionVO.

        序号，只读。

        :return: The ordinal of this DerivativeIndexDimensionVO.
        :rtype: int
        """
        return self._ordinal

    @ordinal.setter
    def ordinal(self, ordinal):
        r"""Sets the ordinal of this DerivativeIndexDimensionVO.

        序号，只读。

        :param ordinal: The ordinal of this DerivativeIndexDimensionVO.
        :type ordinal: int
        """
        self._ordinal = ordinal

    @property
    def group_name(self):
        r"""Gets the group_name of this DerivativeIndexDimensionVO.

        维度分组名称。

        :return: The group_name of this DerivativeIndexDimensionVO.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        r"""Sets the group_name of this DerivativeIndexDimensionVO.

        维度分组名称。

        :param group_name: The group_name of this DerivativeIndexDimensionVO.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def group_code(self):
        r"""Gets the group_code of this DerivativeIndexDimensionVO.

        维度分组编码。

        :return: The group_code of this DerivativeIndexDimensionVO.
        :rtype: str
        """
        return self._group_code

    @group_code.setter
    def group_code(self, group_code):
        r"""Sets the group_code of this DerivativeIndexDimensionVO.

        维度分组编码。

        :param group_code: The group_code of this DerivativeIndexDimensionVO.
        :type group_code: str
        """
        self._group_code = group_code

    @property
    def biz_type(self):
        r"""Gets the biz_type of this DerivativeIndexDimensionVO.

        业务实体类型。 枚举值：  - AGGREGATION_LOGIC_TABLE: 汇总表  - ATOMIC_INDEX: 原子指标  - ATOMIC_METRIC: 原子指标（新）  - BIZ_CATALOG: 流程架构目录  - BIZ_METRIC: 业务指标  - CODE_TABLE: 码表  - COMMON_CONDITION: 通用限定  - COMPOSITE_METRIC: 复合指标（新）  - COMPOUND_METRIC: 复合指标  - CONDITION_GROUP: 限定分组  - DEGENERATE_DIMENSION: 退化维度  - DERIVATIVE_INDEX: 衍生指标  - DERIVED_METRIC: 衍生指标（新）  - DIMENSION: 维度  - DIMENSION_ATTRIBUTE: 维度属性  - DIMENSION_HIERARCHIES: 维度层级  - DIMENSION_LOGIC_TABLE: 维度表  - DIMENSION_TABLE_ATTRIBUTE: 维度属性  - DIRECTORY: 目录  - FACT_ATTRIBUTE: 事实表属性  - FACT_DIMENSION: 事实表维度  - FACT_LOGIC_TABLE: 事实表  - FACT_MEASURE: 事实表度量  - FUNCTION: 函数  - INFO_ARCH: 信息架构（批量修改主题使用）  - MODEL: 模型  - QUALITY_RULE: 质量规则  - SECRECY_LEVEL: 密级  - STANDARD_ELEMENT: 数据标准  - STANDARD_ELEMENT_TEMPLATE: 数据标准模板  - SUBJECT: 主题  - SUMMARY_DIMENSION_ATTRIBUTE: 汇总表维度属性  - SUMMARY_INDEX: 汇总表指标属性  - SUMMARY_TIME: 汇总表时间周期属性  - TABLE_MODEL: 关系模型（逻辑模型/物理模型）  - TABLE_MODEL_ATTRIBUTE: 关系模型属性（逻辑模型/物理模型）  - TABLE_MODEL_LOGIC: 逻辑实体  - TABLE_TYPE: 表类型  - TAG: 标签  - TIME_CONDITION: 时间限定 

        :return: The biz_type of this DerivativeIndexDimensionVO.
        :rtype: str
        """
        return self._biz_type

    @biz_type.setter
    def biz_type(self, biz_type):
        r"""Sets the biz_type of this DerivativeIndexDimensionVO.

        业务实体类型。 枚举值：  - AGGREGATION_LOGIC_TABLE: 汇总表  - ATOMIC_INDEX: 原子指标  - ATOMIC_METRIC: 原子指标（新）  - BIZ_CATALOG: 流程架构目录  - BIZ_METRIC: 业务指标  - CODE_TABLE: 码表  - COMMON_CONDITION: 通用限定  - COMPOSITE_METRIC: 复合指标（新）  - COMPOUND_METRIC: 复合指标  - CONDITION_GROUP: 限定分组  - DEGENERATE_DIMENSION: 退化维度  - DERIVATIVE_INDEX: 衍生指标  - DERIVED_METRIC: 衍生指标（新）  - DIMENSION: 维度  - DIMENSION_ATTRIBUTE: 维度属性  - DIMENSION_HIERARCHIES: 维度层级  - DIMENSION_LOGIC_TABLE: 维度表  - DIMENSION_TABLE_ATTRIBUTE: 维度属性  - DIRECTORY: 目录  - FACT_ATTRIBUTE: 事实表属性  - FACT_DIMENSION: 事实表维度  - FACT_LOGIC_TABLE: 事实表  - FACT_MEASURE: 事实表度量  - FUNCTION: 函数  - INFO_ARCH: 信息架构（批量修改主题使用）  - MODEL: 模型  - QUALITY_RULE: 质量规则  - SECRECY_LEVEL: 密级  - STANDARD_ELEMENT: 数据标准  - STANDARD_ELEMENT_TEMPLATE: 数据标准模板  - SUBJECT: 主题  - SUMMARY_DIMENSION_ATTRIBUTE: 汇总表维度属性  - SUMMARY_INDEX: 汇总表指标属性  - SUMMARY_TIME: 汇总表时间周期属性  - TABLE_MODEL: 关系模型（逻辑模型/物理模型）  - TABLE_MODEL_ATTRIBUTE: 关系模型属性（逻辑模型/物理模型）  - TABLE_MODEL_LOGIC: 逻辑实体  - TABLE_TYPE: 表类型  - TAG: 标签  - TIME_CONDITION: 时间限定 

        :param biz_type: The biz_type of this DerivativeIndexDimensionVO.
        :type biz_type: str
        """
        self._biz_type = biz_type

    @property
    def hierarchies(self):
        r"""Gets the hierarchies of this DerivativeIndexDimensionVO.

        层级属性，只读。

        :return: The hierarchies of this DerivativeIndexDimensionVO.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.DimensionHierarchiesVO`]
        """
        return self._hierarchies

    @hierarchies.setter
    def hierarchies(self, hierarchies):
        r"""Sets the hierarchies of this DerivativeIndexDimensionVO.

        层级属性，只读。

        :param hierarchies: The hierarchies of this DerivativeIndexDimensionVO.
        :type hierarchies: list[:class:`huaweicloudsdkdataartsstudio.v1.DimensionHierarchiesVO`]
        """
        self._hierarchies = hierarchies

    @property
    def l1(self):
        r"""Gets the l1 of this DerivativeIndexDimensionVO.

        主题域分组中文名，只读，创建和更新时无需填写。

        :return: The l1 of this DerivativeIndexDimensionVO.
        :rtype: str
        """
        return self._l1

    @l1.setter
    def l1(self, l1):
        r"""Sets the l1 of this DerivativeIndexDimensionVO.

        主题域分组中文名，只读，创建和更新时无需填写。

        :param l1: The l1 of this DerivativeIndexDimensionVO.
        :type l1: str
        """
        self._l1 = l1

    @property
    def l2(self):
        r"""Gets the l2 of this DerivativeIndexDimensionVO.

        主题域中文名，只读，创建和更新时无需填写。

        :return: The l2 of this DerivativeIndexDimensionVO.
        :rtype: str
        """
        return self._l2

    @l2.setter
    def l2(self, l2):
        r"""Sets the l2 of this DerivativeIndexDimensionVO.

        主题域中文名，只读，创建和更新时无需填写。

        :param l2: The l2 of this DerivativeIndexDimensionVO.
        :type l2: str
        """
        self._l2 = l2

    @property
    def l3(self):
        r"""Gets the l3 of this DerivativeIndexDimensionVO.

        业务对象中文名，只读，创建和更新时无需填写。

        :return: The l3 of this DerivativeIndexDimensionVO.
        :rtype: str
        """
        return self._l3

    @l3.setter
    def l3(self, l3):
        r"""Sets the l3 of this DerivativeIndexDimensionVO.

        业务对象中文名，只读，创建和更新时无需填写。

        :param l3: The l3 of this DerivativeIndexDimensionVO.
        :type l3: str
        """
        self._l3 = l3

    @property
    def l1_id(self):
        r"""Gets the l1_id of this DerivativeIndexDimensionVO.

        主题域分组ID，只读，ID字符串。

        :return: The l1_id of this DerivativeIndexDimensionVO.
        :rtype: str
        """
        return self._l1_id

    @l1_id.setter
    def l1_id(self, l1_id):
        r"""Sets the l1_id of this DerivativeIndexDimensionVO.

        主题域分组ID，只读，ID字符串。

        :param l1_id: The l1_id of this DerivativeIndexDimensionVO.
        :type l1_id: str
        """
        self._l1_id = l1_id

    @property
    def l2_id(self):
        r"""Gets the l2_id of this DerivativeIndexDimensionVO.

        主题域ID，只读，创建和更新时无需填写。

        :return: The l2_id of this DerivativeIndexDimensionVO.
        :rtype: str
        """
        return self._l2_id

    @l2_id.setter
    def l2_id(self, l2_id):
        r"""Sets the l2_id of this DerivativeIndexDimensionVO.

        主题域ID，只读，创建和更新时无需填写。

        :param l2_id: The l2_id of this DerivativeIndexDimensionVO.
        :type l2_id: str
        """
        self._l2_id = l2_id

    @property
    def l3_id(self):
        r"""Gets the l3_id of this DerivativeIndexDimensionVO.

        业务对象ID，只读，ID字符串。

        :return: The l3_id of this DerivativeIndexDimensionVO.
        :rtype: str
        """
        return self._l3_id

    @l3_id.setter
    def l3_id(self, l3_id):
        r"""Sets the l3_id of this DerivativeIndexDimensionVO.

        业务对象ID，只读，ID字符串。

        :param l3_id: The l3_id of this DerivativeIndexDimensionVO.
        :type l3_id: str
        """
        self._l3_id = l3_id

    @property
    def dw_type(self):
        r"""Gets the dw_type of this DerivativeIndexDimensionVO.

        数据连接类型。

        :return: The dw_type of this DerivativeIndexDimensionVO.
        :rtype: str
        """
        return self._dw_type

    @dw_type.setter
    def dw_type(self, dw_type):
        r"""Sets the dw_type of this DerivativeIndexDimensionVO.

        数据连接类型。

        :param dw_type: The dw_type of this DerivativeIndexDimensionVO.
        :type dw_type: str
        """
        self._dw_type = dw_type

    @property
    def id(self):
        r"""Gets the id of this DerivativeIndexDimensionVO.

        层级的ID，只读，ID字符串。

        :return: The id of this DerivativeIndexDimensionVO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this DerivativeIndexDimensionVO.

        层级的ID，只读，ID字符串。

        :param id: The id of this DerivativeIndexDimensionVO.
        :type id: str
        """
        self._id = id

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
        if not isinstance(other, DerivativeIndexDimensionVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
