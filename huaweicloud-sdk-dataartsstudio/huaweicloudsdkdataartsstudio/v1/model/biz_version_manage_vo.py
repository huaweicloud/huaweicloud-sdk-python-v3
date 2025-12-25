# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BizVersionManageVO:

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
        'biz_type': 'str',
        'biz_id': 'str',
        'biz_info': 'str',
        'status': 'str',
        'biz_version': 'int',
        'create_time': 'datetime',
        'update_time': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'biz_type': 'biz_type',
        'biz_id': 'biz_id',
        'biz_info': 'biz_info',
        'status': 'status',
        'biz_version': 'biz_version',
        'create_time': 'create_time',
        'update_time': 'update_time'
    }

    def __init__(self, id=None, biz_type=None, biz_id=None, biz_info=None, status=None, biz_version=None, create_time=None, update_time=None):
        r"""BizVersionManageVO

        The model defined in huaweicloud sdk

        :param id: ID信息，ID字符串。
        :type id: str
        :param biz_type: 业务实体类型。 枚举值：  - AGGREGATION_LOGIC_TABLE: 汇总表  - ATOMIC_INDEX: 原子指标  - ATOMIC_METRIC: 原子指标（新）  - BIZ_CATALOG: 流程架构目录  - BIZ_METRIC: 业务指标  - CODE_TABLE: 码表  - COMMON_CONDITION: 通用限定  - COMPOSITE_METRIC: 复合指标（新）  - COMPOUND_METRIC: 复合指标  - CONDITION_GROUP: 限定分组  - DEGENERATE_DIMENSION: 退化维度  - DERIVATIVE_INDEX: 衍生指标  - DERIVED_METRIC: 衍生指标（新）  - DIMENSION: 维度  - DIMENSION_ATTRIBUTE: 维度属性  - DIMENSION_HIERARCHIES: 维度层级  - DIMENSION_LOGIC_TABLE: 维度表  - DIMENSION_TABLE_ATTRIBUTE: 维度属性  - DIRECTORY: 目录  - FACT_ATTRIBUTE: 事实表属性  - FACT_DIMENSION: 事实表维度  - FACT_LOGIC_TABLE: 事实表  - FACT_MEASURE: 事实表度量  - FUNCTION: 函数  - INFO_ARCH: 信息架构（批量修改主题使用）  - MODEL: 模型  - QUALITY_RULE: 质量规则  - SECRECY_LEVEL: 密级  - STANDARD_ELEMENT: 数据标准  - STANDARD_ELEMENT_TEMPLATE: 数据标准模板  - SUBJECT: 主题  - SUMMARY_DIMENSION_ATTRIBUTE: 汇总表维度属性  - SUMMARY_INDEX: 汇总表指标属性  - SUMMARY_TIME: 汇总表时间周期属性  - TABLE_MODEL: 关系模型（逻辑模型/物理模型）  - TABLE_MODEL_ATTRIBUTE: 关系模型属性（逻辑模型/物理模型）  - TABLE_MODEL_LOGIC: 逻辑实体  - TABLE_TYPE: 表类型  - TAG: 标签  - TIME_CONDITION: 时间限定 
        :type biz_type: str
        :param biz_id: 业务ID，ID字符串。
        :type biz_id: str
        :param biz_info: 业务对象信息。
        :type biz_info: str
        :param status: 实体的发布状态，只读，创建和更新时无需填写。 枚举值：   - DRAFT: 草稿   - PUBLISH_DEVELOPING: 发布待审核   - PUBLISHED: 已发布   - OFFLINE_DEVELOPING: 下线待审核   - OFFLINE: 已下线   - REJECT: 已驳回 
        :type status: str
        :param biz_version: 业务版本，只读。
        :type biz_version: int
        :param create_time: 创建时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。
        :type create_time: datetime
        :param update_time: 更新时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。
        :type update_time: datetime
        """
        
        

        self._id = None
        self._biz_type = None
        self._biz_id = None
        self._biz_info = None
        self._status = None
        self._biz_version = None
        self._create_time = None
        self._update_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if biz_type is not None:
            self.biz_type = biz_type
        if biz_id is not None:
            self.biz_id = biz_id
        if biz_info is not None:
            self.biz_info = biz_info
        if status is not None:
            self.status = status
        if biz_version is not None:
            self.biz_version = biz_version
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def id(self):
        r"""Gets the id of this BizVersionManageVO.

        ID信息，ID字符串。

        :return: The id of this BizVersionManageVO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this BizVersionManageVO.

        ID信息，ID字符串。

        :param id: The id of this BizVersionManageVO.
        :type id: str
        """
        self._id = id

    @property
    def biz_type(self):
        r"""Gets the biz_type of this BizVersionManageVO.

        业务实体类型。 枚举值：  - AGGREGATION_LOGIC_TABLE: 汇总表  - ATOMIC_INDEX: 原子指标  - ATOMIC_METRIC: 原子指标（新）  - BIZ_CATALOG: 流程架构目录  - BIZ_METRIC: 业务指标  - CODE_TABLE: 码表  - COMMON_CONDITION: 通用限定  - COMPOSITE_METRIC: 复合指标（新）  - COMPOUND_METRIC: 复合指标  - CONDITION_GROUP: 限定分组  - DEGENERATE_DIMENSION: 退化维度  - DERIVATIVE_INDEX: 衍生指标  - DERIVED_METRIC: 衍生指标（新）  - DIMENSION: 维度  - DIMENSION_ATTRIBUTE: 维度属性  - DIMENSION_HIERARCHIES: 维度层级  - DIMENSION_LOGIC_TABLE: 维度表  - DIMENSION_TABLE_ATTRIBUTE: 维度属性  - DIRECTORY: 目录  - FACT_ATTRIBUTE: 事实表属性  - FACT_DIMENSION: 事实表维度  - FACT_LOGIC_TABLE: 事实表  - FACT_MEASURE: 事实表度量  - FUNCTION: 函数  - INFO_ARCH: 信息架构（批量修改主题使用）  - MODEL: 模型  - QUALITY_RULE: 质量规则  - SECRECY_LEVEL: 密级  - STANDARD_ELEMENT: 数据标准  - STANDARD_ELEMENT_TEMPLATE: 数据标准模板  - SUBJECT: 主题  - SUMMARY_DIMENSION_ATTRIBUTE: 汇总表维度属性  - SUMMARY_INDEX: 汇总表指标属性  - SUMMARY_TIME: 汇总表时间周期属性  - TABLE_MODEL: 关系模型（逻辑模型/物理模型）  - TABLE_MODEL_ATTRIBUTE: 关系模型属性（逻辑模型/物理模型）  - TABLE_MODEL_LOGIC: 逻辑实体  - TABLE_TYPE: 表类型  - TAG: 标签  - TIME_CONDITION: 时间限定 

        :return: The biz_type of this BizVersionManageVO.
        :rtype: str
        """
        return self._biz_type

    @biz_type.setter
    def biz_type(self, biz_type):
        r"""Sets the biz_type of this BizVersionManageVO.

        业务实体类型。 枚举值：  - AGGREGATION_LOGIC_TABLE: 汇总表  - ATOMIC_INDEX: 原子指标  - ATOMIC_METRIC: 原子指标（新）  - BIZ_CATALOG: 流程架构目录  - BIZ_METRIC: 业务指标  - CODE_TABLE: 码表  - COMMON_CONDITION: 通用限定  - COMPOSITE_METRIC: 复合指标（新）  - COMPOUND_METRIC: 复合指标  - CONDITION_GROUP: 限定分组  - DEGENERATE_DIMENSION: 退化维度  - DERIVATIVE_INDEX: 衍生指标  - DERIVED_METRIC: 衍生指标（新）  - DIMENSION: 维度  - DIMENSION_ATTRIBUTE: 维度属性  - DIMENSION_HIERARCHIES: 维度层级  - DIMENSION_LOGIC_TABLE: 维度表  - DIMENSION_TABLE_ATTRIBUTE: 维度属性  - DIRECTORY: 目录  - FACT_ATTRIBUTE: 事实表属性  - FACT_DIMENSION: 事实表维度  - FACT_LOGIC_TABLE: 事实表  - FACT_MEASURE: 事实表度量  - FUNCTION: 函数  - INFO_ARCH: 信息架构（批量修改主题使用）  - MODEL: 模型  - QUALITY_RULE: 质量规则  - SECRECY_LEVEL: 密级  - STANDARD_ELEMENT: 数据标准  - STANDARD_ELEMENT_TEMPLATE: 数据标准模板  - SUBJECT: 主题  - SUMMARY_DIMENSION_ATTRIBUTE: 汇总表维度属性  - SUMMARY_INDEX: 汇总表指标属性  - SUMMARY_TIME: 汇总表时间周期属性  - TABLE_MODEL: 关系模型（逻辑模型/物理模型）  - TABLE_MODEL_ATTRIBUTE: 关系模型属性（逻辑模型/物理模型）  - TABLE_MODEL_LOGIC: 逻辑实体  - TABLE_TYPE: 表类型  - TAG: 标签  - TIME_CONDITION: 时间限定 

        :param biz_type: The biz_type of this BizVersionManageVO.
        :type biz_type: str
        """
        self._biz_type = biz_type

    @property
    def biz_id(self):
        r"""Gets the biz_id of this BizVersionManageVO.

        业务ID，ID字符串。

        :return: The biz_id of this BizVersionManageVO.
        :rtype: str
        """
        return self._biz_id

    @biz_id.setter
    def biz_id(self, biz_id):
        r"""Sets the biz_id of this BizVersionManageVO.

        业务ID，ID字符串。

        :param biz_id: The biz_id of this BizVersionManageVO.
        :type biz_id: str
        """
        self._biz_id = biz_id

    @property
    def biz_info(self):
        r"""Gets the biz_info of this BizVersionManageVO.

        业务对象信息。

        :return: The biz_info of this BizVersionManageVO.
        :rtype: str
        """
        return self._biz_info

    @biz_info.setter
    def biz_info(self, biz_info):
        r"""Sets the biz_info of this BizVersionManageVO.

        业务对象信息。

        :param biz_info: The biz_info of this BizVersionManageVO.
        :type biz_info: str
        """
        self._biz_info = biz_info

    @property
    def status(self):
        r"""Gets the status of this BizVersionManageVO.

        实体的发布状态，只读，创建和更新时无需填写。 枚举值：   - DRAFT: 草稿   - PUBLISH_DEVELOPING: 发布待审核   - PUBLISHED: 已发布   - OFFLINE_DEVELOPING: 下线待审核   - OFFLINE: 已下线   - REJECT: 已驳回 

        :return: The status of this BizVersionManageVO.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this BizVersionManageVO.

        实体的发布状态，只读，创建和更新时无需填写。 枚举值：   - DRAFT: 草稿   - PUBLISH_DEVELOPING: 发布待审核   - PUBLISHED: 已发布   - OFFLINE_DEVELOPING: 下线待审核   - OFFLINE: 已下线   - REJECT: 已驳回 

        :param status: The status of this BizVersionManageVO.
        :type status: str
        """
        self._status = status

    @property
    def biz_version(self):
        r"""Gets the biz_version of this BizVersionManageVO.

        业务版本，只读。

        :return: The biz_version of this BizVersionManageVO.
        :rtype: int
        """
        return self._biz_version

    @biz_version.setter
    def biz_version(self, biz_version):
        r"""Sets the biz_version of this BizVersionManageVO.

        业务版本，只读。

        :param biz_version: The biz_version of this BizVersionManageVO.
        :type biz_version: int
        """
        self._biz_version = biz_version

    @property
    def create_time(self):
        r"""Gets the create_time of this BizVersionManageVO.

        创建时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。

        :return: The create_time of this BizVersionManageVO.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this BizVersionManageVO.

        创建时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。

        :param create_time: The create_time of this BizVersionManageVO.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this BizVersionManageVO.

        更新时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。

        :return: The update_time of this BizVersionManageVO.
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this BizVersionManageVO.

        更新时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。

        :param update_time: The update_time of this BizVersionManageVO.
        :type update_time: datetime
        """
        self._update_time = update_time

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
        if not isinstance(other, BizVersionManageVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
