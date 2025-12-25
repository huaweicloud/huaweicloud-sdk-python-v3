# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PublishVersionVO:

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
        'version_name': 'str',
        'version_tag': 'str',
        'description': 'str',
        'biz_id': 'str',
        'biz_type': 'str',
        'biz_info': 'str',
        'biz_info_vo': 'object',
        'effect_objs': 'str',
        'change_props': 'str',
        'sql_ddl': 'str',
        'physical_table': 'str',
        'dev_physical_table': 'str',
        'technical_asset': 'str',
        'business_asset': 'str',
        'meta_data_link': 'str',
        'data_quality': 'str',
        'dlf_task': 'str',
        'materialization': 'str',
        'publish_to_dlm': 'str',
        'biz_metric': 'str',
        'summary_status': 'str',
        'is_current_version': 'bool',
        'create_time': 'datetime',
        'create_by': 'str'
    }

    attribute_map = {
        'id': 'id',
        'version_name': 'version_name',
        'version_tag': 'version_tag',
        'description': 'description',
        'biz_id': 'biz_id',
        'biz_type': 'biz_type',
        'biz_info': 'biz_info',
        'biz_info_vo': 'biz_info_vo',
        'effect_objs': 'effect_objs',
        'change_props': 'change_props',
        'sql_ddl': 'sql_ddl',
        'physical_table': 'physical_table',
        'dev_physical_table': 'dev_physical_table',
        'technical_asset': 'technical_asset',
        'business_asset': 'business_asset',
        'meta_data_link': 'meta_data_link',
        'data_quality': 'data_quality',
        'dlf_task': 'dlf_task',
        'materialization': 'materialization',
        'publish_to_dlm': 'publish_to_dlm',
        'biz_metric': 'biz_metric',
        'summary_status': 'summary_status',
        'is_current_version': 'is_current_version',
        'create_time': 'create_time',
        'create_by': 'create_by'
    }

    def __init__(self, id=None, version_name=None, version_tag=None, description=None, biz_id=None, biz_type=None, biz_info=None, biz_info_vo=None, effect_objs=None, change_props=None, sql_ddl=None, physical_table=None, dev_physical_table=None, technical_asset=None, business_asset=None, meta_data_link=None, data_quality=None, dlf_task=None, materialization=None, publish_to_dlm=None, biz_metric=None, summary_status=None, is_current_version=None, create_time=None, create_by=None):
        r"""PublishVersionVO

        The model defined in huaweicloud sdk

        :param id: 版本ID，ID字符串。
        :type id: str
        :param version_name: 版本名称。
        :type version_name: str
        :param version_tag: 版本标记，只读。
        :type version_tag: str
        :param description: 版本描述。
        :type description: str
        :param biz_id: 业务对象ID，ID字符串。
        :type biz_id: str
        :param biz_type: 业务实体类型。 枚举值：  - AGGREGATION_LOGIC_TABLE: 汇总表  - ATOMIC_INDEX: 原子指标  - ATOMIC_METRIC: 原子指标（新）  - BIZ_CATALOG: 流程架构目录  - BIZ_METRIC: 业务指标  - CODE_TABLE: 码表  - COMMON_CONDITION: 通用限定  - COMPOSITE_METRIC: 复合指标（新）  - COMPOUND_METRIC: 复合指标  - CONDITION_GROUP: 限定分组  - DEGENERATE_DIMENSION: 退化维度  - DERIVATIVE_INDEX: 衍生指标  - DERIVED_METRIC: 衍生指标（新）  - DIMENSION: 维度  - DIMENSION_ATTRIBUTE: 维度属性  - DIMENSION_HIERARCHIES: 维度层级  - DIMENSION_LOGIC_TABLE: 维度表  - DIMENSION_TABLE_ATTRIBUTE: 维度属性  - DIRECTORY: 目录  - FACT_ATTRIBUTE: 事实表属性  - FACT_DIMENSION: 事实表维度  - FACT_LOGIC_TABLE: 事实表  - FACT_MEASURE: 事实表度量  - FUNCTION: 函数  - INFO_ARCH: 信息架构（批量修改主题使用）  - MODEL: 模型  - QUALITY_RULE: 质量规则  - SECRECY_LEVEL: 密级  - STANDARD_ELEMENT: 数据标准  - STANDARD_ELEMENT_TEMPLATE: 数据标准模板  - SUBJECT: 主题  - SUMMARY_DIMENSION_ATTRIBUTE: 汇总表维度属性  - SUMMARY_INDEX: 汇总表指标属性  - SUMMARY_TIME: 汇总表时间周期属性  - TABLE_MODEL: 关系模型（逻辑模型/物理模型）  - TABLE_MODEL_ATTRIBUTE: 关系模型属性（逻辑模型/物理模型）  - TABLE_MODEL_LOGIC: 逻辑实体  - TABLE_TYPE: 表类型  - TAG: 标签  - TIME_CONDITION: 时间限定 
        :type biz_type: str
        :param biz_info: 业务详情，只读。
        :type biz_info: str
        :param biz_info_vo: 业务对象。
        :type biz_info_vo: object
        :param effect_objs: 影响信息，只读。
        :type effect_objs: str
        :param change_props: 变化信息，只读。
        :type change_props: str
        :param sql_ddl: SQL脚本，只读。
        :type sql_ddl: str
        :param physical_table: 同步状态。 枚举值：   - NO_NEED: 未同步   - CREATE_SUCCESS: 创建成功   - CREATE_FAILED: 创建失败   - UPDATE_SUCCESS: 更新成功   - UPDATE_FAILED: 更新失败   - SUMMARY_SUCCESS: 整体成功   - SUMMARY_FAILED: 整体失败   - RUNNING: 整体运行   - OFFLINE: 已下线 
        :type physical_table: str
        :param dev_physical_table: 同步状态。 枚举值：   - NO_NEED: 未同步   - CREATE_SUCCESS: 创建成功   - CREATE_FAILED: 创建失败   - UPDATE_SUCCESS: 更新成功   - UPDATE_FAILED: 更新失败   - SUMMARY_SUCCESS: 整体成功   - SUMMARY_FAILED: 整体失败   - RUNNING: 整体运行   - OFFLINE: 已下线 
        :type dev_physical_table: str
        :param technical_asset: 同步状态。 枚举值：   - NO_NEED: 未同步   - CREATE_SUCCESS: 创建成功   - CREATE_FAILED: 创建失败   - UPDATE_SUCCESS: 更新成功   - UPDATE_FAILED: 更新失败   - SUMMARY_SUCCESS: 整体成功   - SUMMARY_FAILED: 整体失败   - RUNNING: 整体运行   - OFFLINE: 已下线 
        :type technical_asset: str
        :param business_asset: 同步状态。 枚举值：   - NO_NEED: 未同步   - CREATE_SUCCESS: 创建成功   - CREATE_FAILED: 创建失败   - UPDATE_SUCCESS: 更新成功   - UPDATE_FAILED: 更新失败   - SUMMARY_SUCCESS: 整体成功   - SUMMARY_FAILED: 整体失败   - RUNNING: 整体运行   - OFFLINE: 已下线 
        :type business_asset: str
        :param meta_data_link: 同步状态。 枚举值：   - NO_NEED: 未同步   - CREATE_SUCCESS: 创建成功   - CREATE_FAILED: 创建失败   - UPDATE_SUCCESS: 更新成功   - UPDATE_FAILED: 更新失败   - SUMMARY_SUCCESS: 整体成功   - SUMMARY_FAILED: 整体失败   - RUNNING: 整体运行   - OFFLINE: 已下线 
        :type meta_data_link: str
        :param data_quality: 同步状态。 枚举值：   - NO_NEED: 未同步   - CREATE_SUCCESS: 创建成功   - CREATE_FAILED: 创建失败   - UPDATE_SUCCESS: 更新成功   - UPDATE_FAILED: 更新失败   - SUMMARY_SUCCESS: 整体成功   - SUMMARY_FAILED: 整体失败   - RUNNING: 整体运行   - OFFLINE: 已下线 
        :type data_quality: str
        :param dlf_task: 同步状态。 枚举值：   - NO_NEED: 未同步   - CREATE_SUCCESS: 创建成功   - CREATE_FAILED: 创建失败   - UPDATE_SUCCESS: 更新成功   - UPDATE_FAILED: 更新失败   - SUMMARY_SUCCESS: 整体成功   - SUMMARY_FAILED: 整体失败   - RUNNING: 整体运行   - OFFLINE: 已下线 
        :type dlf_task: str
        :param materialization: 同步状态。 枚举值：   - NO_NEED: 未同步   - CREATE_SUCCESS: 创建成功   - CREATE_FAILED: 创建失败   - UPDATE_SUCCESS: 更新成功   - UPDATE_FAILED: 更新失败   - SUMMARY_SUCCESS: 整体成功   - SUMMARY_FAILED: 整体失败   - RUNNING: 整体运行   - OFFLINE: 已下线 
        :type materialization: str
        :param publish_to_dlm: 同步状态。 枚举值：   - NO_NEED: 未同步   - CREATE_SUCCESS: 创建成功   - CREATE_FAILED: 创建失败   - UPDATE_SUCCESS: 更新成功   - UPDATE_FAILED: 更新失败   - SUMMARY_SUCCESS: 整体成功   - SUMMARY_FAILED: 整体失败   - RUNNING: 整体运行   - OFFLINE: 已下线 
        :type publish_to_dlm: str
        :param biz_metric: 同步状态。 枚举值：   - NO_NEED: 未同步   - CREATE_SUCCESS: 创建成功   - CREATE_FAILED: 创建失败   - UPDATE_SUCCESS: 更新成功   - UPDATE_FAILED: 更新失败   - SUMMARY_SUCCESS: 整体成功   - SUMMARY_FAILED: 整体失败   - RUNNING: 整体运行   - OFFLINE: 已下线 
        :type biz_metric: str
        :param summary_status: 同步状态。 枚举值：   - NO_NEED: 未同步   - CREATE_SUCCESS: 创建成功   - CREATE_FAILED: 创建失败   - UPDATE_SUCCESS: 更新成功   - UPDATE_FAILED: 更新失败   - SUMMARY_SUCCESS: 整体成功   - SUMMARY_FAILED: 整体失败   - RUNNING: 整体运行   - OFFLINE: 已下线 
        :type summary_status: str
        :param is_current_version: 是否为当前版本，只读。
        :type is_current_version: bool
        :param create_time: 创建时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。
        :type create_time: datetime
        :param create_by: 创建人，只读。
        :type create_by: str
        """
        
        

        self._id = None
        self._version_name = None
        self._version_tag = None
        self._description = None
        self._biz_id = None
        self._biz_type = None
        self._biz_info = None
        self._biz_info_vo = None
        self._effect_objs = None
        self._change_props = None
        self._sql_ddl = None
        self._physical_table = None
        self._dev_physical_table = None
        self._technical_asset = None
        self._business_asset = None
        self._meta_data_link = None
        self._data_quality = None
        self._dlf_task = None
        self._materialization = None
        self._publish_to_dlm = None
        self._biz_metric = None
        self._summary_status = None
        self._is_current_version = None
        self._create_time = None
        self._create_by = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.version_name = version_name
        if version_tag is not None:
            self.version_tag = version_tag
        if description is not None:
            self.description = description
        if biz_id is not None:
            self.biz_id = biz_id
        if biz_type is not None:
            self.biz_type = biz_type
        if biz_info is not None:
            self.biz_info = biz_info
        if biz_info_vo is not None:
            self.biz_info_vo = biz_info_vo
        if effect_objs is not None:
            self.effect_objs = effect_objs
        if change_props is not None:
            self.change_props = change_props
        if sql_ddl is not None:
            self.sql_ddl = sql_ddl
        if physical_table is not None:
            self.physical_table = physical_table
        if dev_physical_table is not None:
            self.dev_physical_table = dev_physical_table
        if technical_asset is not None:
            self.technical_asset = technical_asset
        if business_asset is not None:
            self.business_asset = business_asset
        if meta_data_link is not None:
            self.meta_data_link = meta_data_link
        if data_quality is not None:
            self.data_quality = data_quality
        if dlf_task is not None:
            self.dlf_task = dlf_task
        if materialization is not None:
            self.materialization = materialization
        if publish_to_dlm is not None:
            self.publish_to_dlm = publish_to_dlm
        if biz_metric is not None:
            self.biz_metric = biz_metric
        if summary_status is not None:
            self.summary_status = summary_status
        if is_current_version is not None:
            self.is_current_version = is_current_version
        if create_time is not None:
            self.create_time = create_time
        if create_by is not None:
            self.create_by = create_by

    @property
    def id(self):
        r"""Gets the id of this PublishVersionVO.

        版本ID，ID字符串。

        :return: The id of this PublishVersionVO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this PublishVersionVO.

        版本ID，ID字符串。

        :param id: The id of this PublishVersionVO.
        :type id: str
        """
        self._id = id

    @property
    def version_name(self):
        r"""Gets the version_name of this PublishVersionVO.

        版本名称。

        :return: The version_name of this PublishVersionVO.
        :rtype: str
        """
        return self._version_name

    @version_name.setter
    def version_name(self, version_name):
        r"""Sets the version_name of this PublishVersionVO.

        版本名称。

        :param version_name: The version_name of this PublishVersionVO.
        :type version_name: str
        """
        self._version_name = version_name

    @property
    def version_tag(self):
        r"""Gets the version_tag of this PublishVersionVO.

        版本标记，只读。

        :return: The version_tag of this PublishVersionVO.
        :rtype: str
        """
        return self._version_tag

    @version_tag.setter
    def version_tag(self, version_tag):
        r"""Sets the version_tag of this PublishVersionVO.

        版本标记，只读。

        :param version_tag: The version_tag of this PublishVersionVO.
        :type version_tag: str
        """
        self._version_tag = version_tag

    @property
    def description(self):
        r"""Gets the description of this PublishVersionVO.

        版本描述。

        :return: The description of this PublishVersionVO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this PublishVersionVO.

        版本描述。

        :param description: The description of this PublishVersionVO.
        :type description: str
        """
        self._description = description

    @property
    def biz_id(self):
        r"""Gets the biz_id of this PublishVersionVO.

        业务对象ID，ID字符串。

        :return: The biz_id of this PublishVersionVO.
        :rtype: str
        """
        return self._biz_id

    @biz_id.setter
    def biz_id(self, biz_id):
        r"""Sets the biz_id of this PublishVersionVO.

        业务对象ID，ID字符串。

        :param biz_id: The biz_id of this PublishVersionVO.
        :type biz_id: str
        """
        self._biz_id = biz_id

    @property
    def biz_type(self):
        r"""Gets the biz_type of this PublishVersionVO.

        业务实体类型。 枚举值：  - AGGREGATION_LOGIC_TABLE: 汇总表  - ATOMIC_INDEX: 原子指标  - ATOMIC_METRIC: 原子指标（新）  - BIZ_CATALOG: 流程架构目录  - BIZ_METRIC: 业务指标  - CODE_TABLE: 码表  - COMMON_CONDITION: 通用限定  - COMPOSITE_METRIC: 复合指标（新）  - COMPOUND_METRIC: 复合指标  - CONDITION_GROUP: 限定分组  - DEGENERATE_DIMENSION: 退化维度  - DERIVATIVE_INDEX: 衍生指标  - DERIVED_METRIC: 衍生指标（新）  - DIMENSION: 维度  - DIMENSION_ATTRIBUTE: 维度属性  - DIMENSION_HIERARCHIES: 维度层级  - DIMENSION_LOGIC_TABLE: 维度表  - DIMENSION_TABLE_ATTRIBUTE: 维度属性  - DIRECTORY: 目录  - FACT_ATTRIBUTE: 事实表属性  - FACT_DIMENSION: 事实表维度  - FACT_LOGIC_TABLE: 事实表  - FACT_MEASURE: 事实表度量  - FUNCTION: 函数  - INFO_ARCH: 信息架构（批量修改主题使用）  - MODEL: 模型  - QUALITY_RULE: 质量规则  - SECRECY_LEVEL: 密级  - STANDARD_ELEMENT: 数据标准  - STANDARD_ELEMENT_TEMPLATE: 数据标准模板  - SUBJECT: 主题  - SUMMARY_DIMENSION_ATTRIBUTE: 汇总表维度属性  - SUMMARY_INDEX: 汇总表指标属性  - SUMMARY_TIME: 汇总表时间周期属性  - TABLE_MODEL: 关系模型（逻辑模型/物理模型）  - TABLE_MODEL_ATTRIBUTE: 关系模型属性（逻辑模型/物理模型）  - TABLE_MODEL_LOGIC: 逻辑实体  - TABLE_TYPE: 表类型  - TAG: 标签  - TIME_CONDITION: 时间限定 

        :return: The biz_type of this PublishVersionVO.
        :rtype: str
        """
        return self._biz_type

    @biz_type.setter
    def biz_type(self, biz_type):
        r"""Sets the biz_type of this PublishVersionVO.

        业务实体类型。 枚举值：  - AGGREGATION_LOGIC_TABLE: 汇总表  - ATOMIC_INDEX: 原子指标  - ATOMIC_METRIC: 原子指标（新）  - BIZ_CATALOG: 流程架构目录  - BIZ_METRIC: 业务指标  - CODE_TABLE: 码表  - COMMON_CONDITION: 通用限定  - COMPOSITE_METRIC: 复合指标（新）  - COMPOUND_METRIC: 复合指标  - CONDITION_GROUP: 限定分组  - DEGENERATE_DIMENSION: 退化维度  - DERIVATIVE_INDEX: 衍生指标  - DERIVED_METRIC: 衍生指标（新）  - DIMENSION: 维度  - DIMENSION_ATTRIBUTE: 维度属性  - DIMENSION_HIERARCHIES: 维度层级  - DIMENSION_LOGIC_TABLE: 维度表  - DIMENSION_TABLE_ATTRIBUTE: 维度属性  - DIRECTORY: 目录  - FACT_ATTRIBUTE: 事实表属性  - FACT_DIMENSION: 事实表维度  - FACT_LOGIC_TABLE: 事实表  - FACT_MEASURE: 事实表度量  - FUNCTION: 函数  - INFO_ARCH: 信息架构（批量修改主题使用）  - MODEL: 模型  - QUALITY_RULE: 质量规则  - SECRECY_LEVEL: 密级  - STANDARD_ELEMENT: 数据标准  - STANDARD_ELEMENT_TEMPLATE: 数据标准模板  - SUBJECT: 主题  - SUMMARY_DIMENSION_ATTRIBUTE: 汇总表维度属性  - SUMMARY_INDEX: 汇总表指标属性  - SUMMARY_TIME: 汇总表时间周期属性  - TABLE_MODEL: 关系模型（逻辑模型/物理模型）  - TABLE_MODEL_ATTRIBUTE: 关系模型属性（逻辑模型/物理模型）  - TABLE_MODEL_LOGIC: 逻辑实体  - TABLE_TYPE: 表类型  - TAG: 标签  - TIME_CONDITION: 时间限定 

        :param biz_type: The biz_type of this PublishVersionVO.
        :type biz_type: str
        """
        self._biz_type = biz_type

    @property
    def biz_info(self):
        r"""Gets the biz_info of this PublishVersionVO.

        业务详情，只读。

        :return: The biz_info of this PublishVersionVO.
        :rtype: str
        """
        return self._biz_info

    @biz_info.setter
    def biz_info(self, biz_info):
        r"""Sets the biz_info of this PublishVersionVO.

        业务详情，只读。

        :param biz_info: The biz_info of this PublishVersionVO.
        :type biz_info: str
        """
        self._biz_info = biz_info

    @property
    def biz_info_vo(self):
        r"""Gets the biz_info_vo of this PublishVersionVO.

        业务对象。

        :return: The biz_info_vo of this PublishVersionVO.
        :rtype: object
        """
        return self._biz_info_vo

    @biz_info_vo.setter
    def biz_info_vo(self, biz_info_vo):
        r"""Sets the biz_info_vo of this PublishVersionVO.

        业务对象。

        :param biz_info_vo: The biz_info_vo of this PublishVersionVO.
        :type biz_info_vo: object
        """
        self._biz_info_vo = biz_info_vo

    @property
    def effect_objs(self):
        r"""Gets the effect_objs of this PublishVersionVO.

        影响信息，只读。

        :return: The effect_objs of this PublishVersionVO.
        :rtype: str
        """
        return self._effect_objs

    @effect_objs.setter
    def effect_objs(self, effect_objs):
        r"""Sets the effect_objs of this PublishVersionVO.

        影响信息，只读。

        :param effect_objs: The effect_objs of this PublishVersionVO.
        :type effect_objs: str
        """
        self._effect_objs = effect_objs

    @property
    def change_props(self):
        r"""Gets the change_props of this PublishVersionVO.

        变化信息，只读。

        :return: The change_props of this PublishVersionVO.
        :rtype: str
        """
        return self._change_props

    @change_props.setter
    def change_props(self, change_props):
        r"""Sets the change_props of this PublishVersionVO.

        变化信息，只读。

        :param change_props: The change_props of this PublishVersionVO.
        :type change_props: str
        """
        self._change_props = change_props

    @property
    def sql_ddl(self):
        r"""Gets the sql_ddl of this PublishVersionVO.

        SQL脚本，只读。

        :return: The sql_ddl of this PublishVersionVO.
        :rtype: str
        """
        return self._sql_ddl

    @sql_ddl.setter
    def sql_ddl(self, sql_ddl):
        r"""Sets the sql_ddl of this PublishVersionVO.

        SQL脚本，只读。

        :param sql_ddl: The sql_ddl of this PublishVersionVO.
        :type sql_ddl: str
        """
        self._sql_ddl = sql_ddl

    @property
    def physical_table(self):
        r"""Gets the physical_table of this PublishVersionVO.

        同步状态。 枚举值：   - NO_NEED: 未同步   - CREATE_SUCCESS: 创建成功   - CREATE_FAILED: 创建失败   - UPDATE_SUCCESS: 更新成功   - UPDATE_FAILED: 更新失败   - SUMMARY_SUCCESS: 整体成功   - SUMMARY_FAILED: 整体失败   - RUNNING: 整体运行   - OFFLINE: 已下线 

        :return: The physical_table of this PublishVersionVO.
        :rtype: str
        """
        return self._physical_table

    @physical_table.setter
    def physical_table(self, physical_table):
        r"""Sets the physical_table of this PublishVersionVO.

        同步状态。 枚举值：   - NO_NEED: 未同步   - CREATE_SUCCESS: 创建成功   - CREATE_FAILED: 创建失败   - UPDATE_SUCCESS: 更新成功   - UPDATE_FAILED: 更新失败   - SUMMARY_SUCCESS: 整体成功   - SUMMARY_FAILED: 整体失败   - RUNNING: 整体运行   - OFFLINE: 已下线 

        :param physical_table: The physical_table of this PublishVersionVO.
        :type physical_table: str
        """
        self._physical_table = physical_table

    @property
    def dev_physical_table(self):
        r"""Gets the dev_physical_table of this PublishVersionVO.

        同步状态。 枚举值：   - NO_NEED: 未同步   - CREATE_SUCCESS: 创建成功   - CREATE_FAILED: 创建失败   - UPDATE_SUCCESS: 更新成功   - UPDATE_FAILED: 更新失败   - SUMMARY_SUCCESS: 整体成功   - SUMMARY_FAILED: 整体失败   - RUNNING: 整体运行   - OFFLINE: 已下线 

        :return: The dev_physical_table of this PublishVersionVO.
        :rtype: str
        """
        return self._dev_physical_table

    @dev_physical_table.setter
    def dev_physical_table(self, dev_physical_table):
        r"""Sets the dev_physical_table of this PublishVersionVO.

        同步状态。 枚举值：   - NO_NEED: 未同步   - CREATE_SUCCESS: 创建成功   - CREATE_FAILED: 创建失败   - UPDATE_SUCCESS: 更新成功   - UPDATE_FAILED: 更新失败   - SUMMARY_SUCCESS: 整体成功   - SUMMARY_FAILED: 整体失败   - RUNNING: 整体运行   - OFFLINE: 已下线 

        :param dev_physical_table: The dev_physical_table of this PublishVersionVO.
        :type dev_physical_table: str
        """
        self._dev_physical_table = dev_physical_table

    @property
    def technical_asset(self):
        r"""Gets the technical_asset of this PublishVersionVO.

        同步状态。 枚举值：   - NO_NEED: 未同步   - CREATE_SUCCESS: 创建成功   - CREATE_FAILED: 创建失败   - UPDATE_SUCCESS: 更新成功   - UPDATE_FAILED: 更新失败   - SUMMARY_SUCCESS: 整体成功   - SUMMARY_FAILED: 整体失败   - RUNNING: 整体运行   - OFFLINE: 已下线 

        :return: The technical_asset of this PublishVersionVO.
        :rtype: str
        """
        return self._technical_asset

    @technical_asset.setter
    def technical_asset(self, technical_asset):
        r"""Sets the technical_asset of this PublishVersionVO.

        同步状态。 枚举值：   - NO_NEED: 未同步   - CREATE_SUCCESS: 创建成功   - CREATE_FAILED: 创建失败   - UPDATE_SUCCESS: 更新成功   - UPDATE_FAILED: 更新失败   - SUMMARY_SUCCESS: 整体成功   - SUMMARY_FAILED: 整体失败   - RUNNING: 整体运行   - OFFLINE: 已下线 

        :param technical_asset: The technical_asset of this PublishVersionVO.
        :type technical_asset: str
        """
        self._technical_asset = technical_asset

    @property
    def business_asset(self):
        r"""Gets the business_asset of this PublishVersionVO.

        同步状态。 枚举值：   - NO_NEED: 未同步   - CREATE_SUCCESS: 创建成功   - CREATE_FAILED: 创建失败   - UPDATE_SUCCESS: 更新成功   - UPDATE_FAILED: 更新失败   - SUMMARY_SUCCESS: 整体成功   - SUMMARY_FAILED: 整体失败   - RUNNING: 整体运行   - OFFLINE: 已下线 

        :return: The business_asset of this PublishVersionVO.
        :rtype: str
        """
        return self._business_asset

    @business_asset.setter
    def business_asset(self, business_asset):
        r"""Sets the business_asset of this PublishVersionVO.

        同步状态。 枚举值：   - NO_NEED: 未同步   - CREATE_SUCCESS: 创建成功   - CREATE_FAILED: 创建失败   - UPDATE_SUCCESS: 更新成功   - UPDATE_FAILED: 更新失败   - SUMMARY_SUCCESS: 整体成功   - SUMMARY_FAILED: 整体失败   - RUNNING: 整体运行   - OFFLINE: 已下线 

        :param business_asset: The business_asset of this PublishVersionVO.
        :type business_asset: str
        """
        self._business_asset = business_asset

    @property
    def meta_data_link(self):
        r"""Gets the meta_data_link of this PublishVersionVO.

        同步状态。 枚举值：   - NO_NEED: 未同步   - CREATE_SUCCESS: 创建成功   - CREATE_FAILED: 创建失败   - UPDATE_SUCCESS: 更新成功   - UPDATE_FAILED: 更新失败   - SUMMARY_SUCCESS: 整体成功   - SUMMARY_FAILED: 整体失败   - RUNNING: 整体运行   - OFFLINE: 已下线 

        :return: The meta_data_link of this PublishVersionVO.
        :rtype: str
        """
        return self._meta_data_link

    @meta_data_link.setter
    def meta_data_link(self, meta_data_link):
        r"""Sets the meta_data_link of this PublishVersionVO.

        同步状态。 枚举值：   - NO_NEED: 未同步   - CREATE_SUCCESS: 创建成功   - CREATE_FAILED: 创建失败   - UPDATE_SUCCESS: 更新成功   - UPDATE_FAILED: 更新失败   - SUMMARY_SUCCESS: 整体成功   - SUMMARY_FAILED: 整体失败   - RUNNING: 整体运行   - OFFLINE: 已下线 

        :param meta_data_link: The meta_data_link of this PublishVersionVO.
        :type meta_data_link: str
        """
        self._meta_data_link = meta_data_link

    @property
    def data_quality(self):
        r"""Gets the data_quality of this PublishVersionVO.

        同步状态。 枚举值：   - NO_NEED: 未同步   - CREATE_SUCCESS: 创建成功   - CREATE_FAILED: 创建失败   - UPDATE_SUCCESS: 更新成功   - UPDATE_FAILED: 更新失败   - SUMMARY_SUCCESS: 整体成功   - SUMMARY_FAILED: 整体失败   - RUNNING: 整体运行   - OFFLINE: 已下线 

        :return: The data_quality of this PublishVersionVO.
        :rtype: str
        """
        return self._data_quality

    @data_quality.setter
    def data_quality(self, data_quality):
        r"""Sets the data_quality of this PublishVersionVO.

        同步状态。 枚举值：   - NO_NEED: 未同步   - CREATE_SUCCESS: 创建成功   - CREATE_FAILED: 创建失败   - UPDATE_SUCCESS: 更新成功   - UPDATE_FAILED: 更新失败   - SUMMARY_SUCCESS: 整体成功   - SUMMARY_FAILED: 整体失败   - RUNNING: 整体运行   - OFFLINE: 已下线 

        :param data_quality: The data_quality of this PublishVersionVO.
        :type data_quality: str
        """
        self._data_quality = data_quality

    @property
    def dlf_task(self):
        r"""Gets the dlf_task of this PublishVersionVO.

        同步状态。 枚举值：   - NO_NEED: 未同步   - CREATE_SUCCESS: 创建成功   - CREATE_FAILED: 创建失败   - UPDATE_SUCCESS: 更新成功   - UPDATE_FAILED: 更新失败   - SUMMARY_SUCCESS: 整体成功   - SUMMARY_FAILED: 整体失败   - RUNNING: 整体运行   - OFFLINE: 已下线 

        :return: The dlf_task of this PublishVersionVO.
        :rtype: str
        """
        return self._dlf_task

    @dlf_task.setter
    def dlf_task(self, dlf_task):
        r"""Sets the dlf_task of this PublishVersionVO.

        同步状态。 枚举值：   - NO_NEED: 未同步   - CREATE_SUCCESS: 创建成功   - CREATE_FAILED: 创建失败   - UPDATE_SUCCESS: 更新成功   - UPDATE_FAILED: 更新失败   - SUMMARY_SUCCESS: 整体成功   - SUMMARY_FAILED: 整体失败   - RUNNING: 整体运行   - OFFLINE: 已下线 

        :param dlf_task: The dlf_task of this PublishVersionVO.
        :type dlf_task: str
        """
        self._dlf_task = dlf_task

    @property
    def materialization(self):
        r"""Gets the materialization of this PublishVersionVO.

        同步状态。 枚举值：   - NO_NEED: 未同步   - CREATE_SUCCESS: 创建成功   - CREATE_FAILED: 创建失败   - UPDATE_SUCCESS: 更新成功   - UPDATE_FAILED: 更新失败   - SUMMARY_SUCCESS: 整体成功   - SUMMARY_FAILED: 整体失败   - RUNNING: 整体运行   - OFFLINE: 已下线 

        :return: The materialization of this PublishVersionVO.
        :rtype: str
        """
        return self._materialization

    @materialization.setter
    def materialization(self, materialization):
        r"""Sets the materialization of this PublishVersionVO.

        同步状态。 枚举值：   - NO_NEED: 未同步   - CREATE_SUCCESS: 创建成功   - CREATE_FAILED: 创建失败   - UPDATE_SUCCESS: 更新成功   - UPDATE_FAILED: 更新失败   - SUMMARY_SUCCESS: 整体成功   - SUMMARY_FAILED: 整体失败   - RUNNING: 整体运行   - OFFLINE: 已下线 

        :param materialization: The materialization of this PublishVersionVO.
        :type materialization: str
        """
        self._materialization = materialization

    @property
    def publish_to_dlm(self):
        r"""Gets the publish_to_dlm of this PublishVersionVO.

        同步状态。 枚举值：   - NO_NEED: 未同步   - CREATE_SUCCESS: 创建成功   - CREATE_FAILED: 创建失败   - UPDATE_SUCCESS: 更新成功   - UPDATE_FAILED: 更新失败   - SUMMARY_SUCCESS: 整体成功   - SUMMARY_FAILED: 整体失败   - RUNNING: 整体运行   - OFFLINE: 已下线 

        :return: The publish_to_dlm of this PublishVersionVO.
        :rtype: str
        """
        return self._publish_to_dlm

    @publish_to_dlm.setter
    def publish_to_dlm(self, publish_to_dlm):
        r"""Sets the publish_to_dlm of this PublishVersionVO.

        同步状态。 枚举值：   - NO_NEED: 未同步   - CREATE_SUCCESS: 创建成功   - CREATE_FAILED: 创建失败   - UPDATE_SUCCESS: 更新成功   - UPDATE_FAILED: 更新失败   - SUMMARY_SUCCESS: 整体成功   - SUMMARY_FAILED: 整体失败   - RUNNING: 整体运行   - OFFLINE: 已下线 

        :param publish_to_dlm: The publish_to_dlm of this PublishVersionVO.
        :type publish_to_dlm: str
        """
        self._publish_to_dlm = publish_to_dlm

    @property
    def biz_metric(self):
        r"""Gets the biz_metric of this PublishVersionVO.

        同步状态。 枚举值：   - NO_NEED: 未同步   - CREATE_SUCCESS: 创建成功   - CREATE_FAILED: 创建失败   - UPDATE_SUCCESS: 更新成功   - UPDATE_FAILED: 更新失败   - SUMMARY_SUCCESS: 整体成功   - SUMMARY_FAILED: 整体失败   - RUNNING: 整体运行   - OFFLINE: 已下线 

        :return: The biz_metric of this PublishVersionVO.
        :rtype: str
        """
        return self._biz_metric

    @biz_metric.setter
    def biz_metric(self, biz_metric):
        r"""Sets the biz_metric of this PublishVersionVO.

        同步状态。 枚举值：   - NO_NEED: 未同步   - CREATE_SUCCESS: 创建成功   - CREATE_FAILED: 创建失败   - UPDATE_SUCCESS: 更新成功   - UPDATE_FAILED: 更新失败   - SUMMARY_SUCCESS: 整体成功   - SUMMARY_FAILED: 整体失败   - RUNNING: 整体运行   - OFFLINE: 已下线 

        :param biz_metric: The biz_metric of this PublishVersionVO.
        :type biz_metric: str
        """
        self._biz_metric = biz_metric

    @property
    def summary_status(self):
        r"""Gets the summary_status of this PublishVersionVO.

        同步状态。 枚举值：   - NO_NEED: 未同步   - CREATE_SUCCESS: 创建成功   - CREATE_FAILED: 创建失败   - UPDATE_SUCCESS: 更新成功   - UPDATE_FAILED: 更新失败   - SUMMARY_SUCCESS: 整体成功   - SUMMARY_FAILED: 整体失败   - RUNNING: 整体运行   - OFFLINE: 已下线 

        :return: The summary_status of this PublishVersionVO.
        :rtype: str
        """
        return self._summary_status

    @summary_status.setter
    def summary_status(self, summary_status):
        r"""Sets the summary_status of this PublishVersionVO.

        同步状态。 枚举值：   - NO_NEED: 未同步   - CREATE_SUCCESS: 创建成功   - CREATE_FAILED: 创建失败   - UPDATE_SUCCESS: 更新成功   - UPDATE_FAILED: 更新失败   - SUMMARY_SUCCESS: 整体成功   - SUMMARY_FAILED: 整体失败   - RUNNING: 整体运行   - OFFLINE: 已下线 

        :param summary_status: The summary_status of this PublishVersionVO.
        :type summary_status: str
        """
        self._summary_status = summary_status

    @property
    def is_current_version(self):
        r"""Gets the is_current_version of this PublishVersionVO.

        是否为当前版本，只读。

        :return: The is_current_version of this PublishVersionVO.
        :rtype: bool
        """
        return self._is_current_version

    @is_current_version.setter
    def is_current_version(self, is_current_version):
        r"""Sets the is_current_version of this PublishVersionVO.

        是否为当前版本，只读。

        :param is_current_version: The is_current_version of this PublishVersionVO.
        :type is_current_version: bool
        """
        self._is_current_version = is_current_version

    @property
    def create_time(self):
        r"""Gets the create_time of this PublishVersionVO.

        创建时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。

        :return: The create_time of this PublishVersionVO.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this PublishVersionVO.

        创建时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。

        :param create_time: The create_time of this PublishVersionVO.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def create_by(self):
        r"""Gets the create_by of this PublishVersionVO.

        创建人，只读。

        :return: The create_by of this PublishVersionVO.
        :rtype: str
        """
        return self._create_by

    @create_by.setter
    def create_by(self, create_by):
        r"""Sets the create_by of this PublishVersionVO.

        创建人，只读。

        :param create_by: The create_by of this PublishVersionVO.
        :type create_by: str
        """
        self._create_by = create_by

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
        if not isinstance(other, PublishVersionVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
