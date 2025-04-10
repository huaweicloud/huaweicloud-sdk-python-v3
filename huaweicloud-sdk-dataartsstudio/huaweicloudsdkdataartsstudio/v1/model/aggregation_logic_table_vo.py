# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AggregationLogicTableVO:

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
        'tb_name': 'str',
        'tb_logic_name': 'str',
        'l1_id': 'str',
        'l2_id': 'str',
        'l3_id': 'str',
        'description': 'str',
        'owner': 'str',
        'secret_type': 'SecretTypeEnum',
        'apply_bg': 'ApplyBgEnum',
        'create_by': 'str',
        'queue_name': 'str',
        'dw_id': 'str',
        'db_name': 'str',
        'tb_id': 'str',
        'schema': 'str',
        'dw_name': 'str',
        'status': 'BizStatusEnum',
        'tb_guid': 'str',
        'tb_logic_guid': 'str',
        'dw_type': 'str',
        'l1': 'str',
        'l2': 'str',
        'l3': 'str',
        'create_time': 'datetime',
        'update_time': 'datetime',
        'approval_info': 'ApprovalVO',
        'new_biz': 'BizVersionManageVO',
        'dimension_group': 'str',
        'group_name': 'str',
        'group_code': 'str',
        'time_period': 'AggregationLogicTableAttributeVO',
        'table_attributes': 'list[AggregationLogicTableAttributeVO]',
        'physical_table': 'SyncStatusEnum',
        'dev_physical_table': 'SyncStatusEnum',
        'technical_asset': 'SyncStatusEnum',
        'business_asset': 'SyncStatusEnum',
        'meta_data_link': 'SyncStatusEnum',
        'data_quality': 'SyncStatusEnum',
        'dlf_task': 'SyncStatusEnum',
        'publish_to_dlm': 'SyncStatusEnum',
        'summary_status': 'SyncStatusEnum',
        'distribute': 'str',
        'distribute_column': 'str',
        'compression': 'str',
        'obs_location': 'str',
        'pre_combine_field': 'str',
        'table_type': 'str',
        'dlf_task_id': 'str',
        'quality_id': 'str',
        'reversed': 'bool',
        'table_version': 'int',
        'partition_conf': 'str',
        'dirty_out_switch': 'bool',
        'dirty_out_database': 'str',
        'dirty_out_prefix': 'str',
        'dirty_out_suffix': 'str',
        'alias': 'str',
        'configs': 'str',
        'self_defined_fields': 'list[SelfDefinedFieldVO]',
        'api_id': 'str',
        'sql': 'str',
        'dev_version': 'str',
        'prod_version': 'str',
        'dev_version_name': 'str',
        'prod_version_name': 'str',
        'env_type': 'EnvTypeEnum',
        'model_id': 'str',
        'model': 'WorkspaceVO'
    }

    attribute_map = {
        'id': 'id',
        'tb_name': 'tb_name',
        'tb_logic_name': 'tb_logic_name',
        'l1_id': 'l1_id',
        'l2_id': 'l2_id',
        'l3_id': 'l3_id',
        'description': 'description',
        'owner': 'owner',
        'secret_type': 'secret_type',
        'apply_bg': 'apply_bg',
        'create_by': 'create_by',
        'queue_name': 'queue_name',
        'dw_id': 'dw_id',
        'db_name': 'db_name',
        'tb_id': 'tb_id',
        'schema': 'schema',
        'dw_name': 'dw_name',
        'status': 'status',
        'tb_guid': 'tb_guid',
        'tb_logic_guid': 'tb_logic_guid',
        'dw_type': 'dw_type',
        'l1': 'l1',
        'l2': 'l2',
        'l3': 'l3',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'approval_info': 'approval_info',
        'new_biz': 'new_biz',
        'dimension_group': 'dimension_group',
        'group_name': 'group_name',
        'group_code': 'group_code',
        'time_period': 'time_period',
        'table_attributes': 'table_attributes',
        'physical_table': 'physical_table',
        'dev_physical_table': 'dev_physical_table',
        'technical_asset': 'technical_asset',
        'business_asset': 'business_asset',
        'meta_data_link': 'meta_data_link',
        'data_quality': 'data_quality',
        'dlf_task': 'dlf_task',
        'publish_to_dlm': 'publish_to_dlm',
        'summary_status': 'summary_status',
        'distribute': 'distribute',
        'distribute_column': 'distribute_column',
        'compression': 'compression',
        'obs_location': 'obs_location',
        'pre_combine_field': 'pre_combine_field',
        'table_type': 'table_type',
        'dlf_task_id': 'dlf_task_id',
        'quality_id': 'quality_id',
        'reversed': 'reversed',
        'table_version': 'table_version',
        'partition_conf': 'partition_conf',
        'dirty_out_switch': 'dirty_out_switch',
        'dirty_out_database': 'dirty_out_database',
        'dirty_out_prefix': 'dirty_out_prefix',
        'dirty_out_suffix': 'dirty_out_suffix',
        'alias': 'alias',
        'configs': 'configs',
        'self_defined_fields': 'self_defined_fields',
        'api_id': 'api_id',
        'sql': 'sql',
        'dev_version': 'dev_version',
        'prod_version': 'prod_version',
        'dev_version_name': 'dev_version_name',
        'prod_version_name': 'prod_version_name',
        'env_type': 'env_type',
        'model_id': 'model_id',
        'model': 'model'
    }

    def __init__(self, id=None, tb_name=None, tb_logic_name=None, l1_id=None, l2_id=None, l3_id=None, description=None, owner=None, secret_type=None, apply_bg=None, create_by=None, queue_name=None, dw_id=None, db_name=None, tb_id=None, schema=None, dw_name=None, status=None, tb_guid=None, tb_logic_guid=None, dw_type=None, l1=None, l2=None, l3=None, create_time=None, update_time=None, approval_info=None, new_biz=None, dimension_group=None, group_name=None, group_code=None, time_period=None, table_attributes=None, physical_table=None, dev_physical_table=None, technical_asset=None, business_asset=None, meta_data_link=None, data_quality=None, dlf_task=None, publish_to_dlm=None, summary_status=None, distribute=None, distribute_column=None, compression=None, obs_location=None, pre_combine_field=None, table_type=None, dlf_task_id=None, quality_id=None, reversed=None, table_version=None, partition_conf=None, dirty_out_switch=None, dirty_out_database=None, dirty_out_prefix=None, dirty_out_suffix=None, alias=None, configs=None, self_defined_fields=None, api_id=None, sql=None, dev_version=None, prod_version=None, dev_version_name=None, prod_version_name=None, env_type=None, model_id=None, model=None):
        r"""AggregationLogicTableVO

        The model defined in huaweicloud sdk

        :param id: 汇总表的唯一系统ID，更新时必填，创建时不须填写，ID字符串。
        :type id: str
        :param tb_name: 汇总表英文名称，对应实际的物理表名。
        :type tb_name: str
        :param tb_logic_name: 汇总表的中文名，用于展示使用。
        :type tb_logic_name: str
        :param l1_id: 主题域分组ID，只读，创建和更新时无需填写，ID字符串。
        :type l1_id: str
        :param l2_id: 主题域ID，只读，创建和更新时无需填写。
        :type l2_id: str
        :param l3_id: 汇总表所属主题的ID，必填，ID字符串。
        :type l3_id: str
        :param description: 汇总表描述信息。
        :type description: str
        :param owner: 汇总表的资产责任人。
        :type owner: str
        :param secret_type: 
        :type secret_type: :class:`huaweicloudsdkdataartsstudio.v1.SecretTypeEnum`
        :param apply_bg: 
        :type apply_bg: :class:`huaweicloudsdkdataartsstudio.v1.ApplyBgEnum`
        :param create_by: 汇总表的创建人，只读，创建和更新时无需填写。
        :type create_by: str
        :param queue_name: dli数据连接执行sql所需的队列，数据连接类型为DLI时必须填写。
        :type queue_name: str
        :param dw_id: 汇总表所在的数据连接ID，为32位十六进制数字。
        :type dw_id: str
        :param db_name: 汇总表所在的数据库名。
        :type db_name: str
        :param tb_id: 汇总表创建的表ID，是服务内部ID，只读，创建和更新时无需填写
        :type tb_id: str
        :param schema: 汇总表所在的Schema名，DWS类型必须填写。
        :type schema: str
        :param dw_name: 数据连接名称，只读，创建和更新时无需填写。
        :type dw_name: str
        :param status: 
        :type status: :class:`huaweicloudsdkdataartsstudio.v1.BizStatusEnum`
        :param tb_guid: 表发布后，创建的数据目录技术资产guid，只读，创建和更新时无需填写。
        :type tb_guid: str
        :param tb_logic_guid: 表发布后，创建的数据目录业务资产guid，只读，创建和更新时无需填写。
        :type tb_logic_guid: str
        :param dw_type: 数据连接类型，对应表所在的数仓类型，取值可以为DLI、DWS、MRS_HIVE、POSTGRESQL、MRS_SPARK、CLICKHOUSE、MYSQL、ORACLE和DORIS等。
        :type dw_type: str
        :param l1: 主题域分组中文名，只读，创建和更新时无需填写。
        :type l1: str
        :param l2: 主题域中文名，只读，创建和更新时无需填写。
        :type l2: str
        :param l3: 业务对象中文名，只读，创建和更新时无需填写。
        :type l3: str
        :param create_time: 创建时间，只读，创建和更新时无需填写。
        :type create_time: datetime
        :param update_time: 更新时间，只读，创建和更新时无需填写。
        :type update_time: datetime
        :param approval_info: 
        :type approval_info: :class:`huaweicloudsdkdataartsstudio.v1.ApprovalVO`
        :param new_biz: 
        :type new_biz: :class:`huaweicloudsdkdataartsstudio.v1.BizVersionManageVO`
        :param dimension_group: 颗粒度ID。
        :type dimension_group: str
        :param group_name: 颗粒度名称，只读。
        :type group_name: str
        :param group_code: 颗粒度编码，只读。
        :type group_code: str
        :param time_period: 
        :type time_period: :class:`huaweicloudsdkdataartsstudio.v1.AggregationLogicTableAttributeVO`
        :param table_attributes: 汇总表属性信息，依据attribute_type判断类型。
        :type table_attributes: list[:class:`huaweicloudsdkdataartsstudio.v1.AggregationLogicTableAttributeVO`]
        :param physical_table: 
        :type physical_table: :class:`huaweicloudsdkdataartsstudio.v1.SyncStatusEnum`
        :param dev_physical_table: 
        :type dev_physical_table: :class:`huaweicloudsdkdataartsstudio.v1.SyncStatusEnum`
        :param technical_asset: 
        :type technical_asset: :class:`huaweicloudsdkdataartsstudio.v1.SyncStatusEnum`
        :param business_asset: 
        :type business_asset: :class:`huaweicloudsdkdataartsstudio.v1.SyncStatusEnum`
        :param meta_data_link: 
        :type meta_data_link: :class:`huaweicloudsdkdataartsstudio.v1.SyncStatusEnum`
        :param data_quality: 
        :type data_quality: :class:`huaweicloudsdkdataartsstudio.v1.SyncStatusEnum`
        :param dlf_task: 
        :type dlf_task: :class:`huaweicloudsdkdataartsstudio.v1.SyncStatusEnum`
        :param publish_to_dlm: 
        :type publish_to_dlm: :class:`huaweicloudsdkdataartsstudio.v1.SyncStatusEnum`
        :param summary_status: 
        :type summary_status: :class:`huaweicloudsdkdataartsstudio.v1.SyncStatusEnum`
        :param distribute: DISTRIBUTE BY [HASH(column)|REPLICATION]。 枚举值：   - HASH: 对指定的列进行Hash，通过映射，把数据分布到指定DN   - REPLICATION: 表的每一行存在所有数据节点（DN）中，即每个数据节点都有完整的表数据 
        :type distribute: str
        :param distribute_column: DISTRIBUTE BY HASH column.
        :type distribute_column: str
        :param compression: DWS数据压缩等级，列压缩等级为no/low/middle/high，行压缩等级为no/yes。 枚举值：   - \&quot;NO\&quot;: 不压缩   - \&quot;YES\&quot;: 压缩   - \&quot;LOW\&quot;: 低等级压缩   - \&quot;MIDDLE\&quot;: 中等级压缩   - \&quot;HIGH\&quot;: 高等级压缩 
        :type compression: str
        :param obs_location: 外表路径。
        :type obs_location: str
        :param pre_combine_field: 版本字段。
        :type pre_combine_field: str
        :param table_type: 表类型。
        :type table_type: str
        :param dlf_task_id: DLF作业ID。
        :type dlf_task_id: str
        :param quality_id: 质量ID，ID字符串。
        :type quality_id: str
        :param reversed: 是否是逆向的，只读。
        :type reversed: bool
        :param table_version: 为2时，表示汇总表是汇总生成的，只读。
        :type table_version: int
        :param partition_conf: 分区表达式。
        :type partition_conf: str
        :param dirty_out_switch: 异常数据输出开关。
        :type dirty_out_switch: bool
        :param dirty_out_database: 异常数据输出库。
        :type dirty_out_database: str
        :param dirty_out_prefix: 异常表前缀。
        :type dirty_out_prefix: str
        :param dirty_out_suffix: 异常表后缀。
        :type dirty_out_suffix: str
        :param alias: 别名。
        :type alias: str
        :param configs: 其他配置。
        :type configs: str
        :param self_defined_fields: 自定义项。
        :type self_defined_fields: list[:class:`huaweicloudsdkdataartsstudio.v1.SelfDefinedFieldVO`]
        :param api_id: API ID。
        :type api_id: str
        :param sql: 汇总表绑定的SQL。
        :type sql: str
        :param dev_version: 开发环境版本，ID字符串。
        :type dev_version: str
        :param prod_version: 生产环境版本，ID字符串。
        :type prod_version: str
        :param dev_version_name: 开发环境版本名称
        :type dev_version_name: str
        :param prod_version_name: 生产环境版本名称
        :type prod_version_name: str
        :param env_type: 
        :type env_type: :class:`huaweicloudsdkdataartsstudio.v1.EnvTypeEnum`
        :param model_id: 所属模型ID，ID字符串。
        :type model_id: str
        :param model: 
        :type model: :class:`huaweicloudsdkdataartsstudio.v1.WorkspaceVO`
        """
        
        

        self._id = None
        self._tb_name = None
        self._tb_logic_name = None
        self._l1_id = None
        self._l2_id = None
        self._l3_id = None
        self._description = None
        self._owner = None
        self._secret_type = None
        self._apply_bg = None
        self._create_by = None
        self._queue_name = None
        self._dw_id = None
        self._db_name = None
        self._tb_id = None
        self._schema = None
        self._dw_name = None
        self._status = None
        self._tb_guid = None
        self._tb_logic_guid = None
        self._dw_type = None
        self._l1 = None
        self._l2 = None
        self._l3 = None
        self._create_time = None
        self._update_time = None
        self._approval_info = None
        self._new_biz = None
        self._dimension_group = None
        self._group_name = None
        self._group_code = None
        self._time_period = None
        self._table_attributes = None
        self._physical_table = None
        self._dev_physical_table = None
        self._technical_asset = None
        self._business_asset = None
        self._meta_data_link = None
        self._data_quality = None
        self._dlf_task = None
        self._publish_to_dlm = None
        self._summary_status = None
        self._distribute = None
        self._distribute_column = None
        self._compression = None
        self._obs_location = None
        self._pre_combine_field = None
        self._table_type = None
        self._dlf_task_id = None
        self._quality_id = None
        self._reversed = None
        self._table_version = None
        self._partition_conf = None
        self._dirty_out_switch = None
        self._dirty_out_database = None
        self._dirty_out_prefix = None
        self._dirty_out_suffix = None
        self._alias = None
        self._configs = None
        self._self_defined_fields = None
        self._api_id = None
        self._sql = None
        self._dev_version = None
        self._prod_version = None
        self._dev_version_name = None
        self._prod_version_name = None
        self._env_type = None
        self._model_id = None
        self._model = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.tb_name = tb_name
        self.tb_logic_name = tb_logic_name
        if l1_id is not None:
            self.l1_id = l1_id
        if l2_id is not None:
            self.l2_id = l2_id
        self.l3_id = l3_id
        if description is not None:
            self.description = description
        self.owner = owner
        if secret_type is not None:
            self.secret_type = secret_type
        if apply_bg is not None:
            self.apply_bg = apply_bg
        if create_by is not None:
            self.create_by = create_by
        if queue_name is not None:
            self.queue_name = queue_name
        self.dw_id = dw_id
        self.db_name = db_name
        if tb_id is not None:
            self.tb_id = tb_id
        if schema is not None:
            self.schema = schema
        if dw_name is not None:
            self.dw_name = dw_name
        if status is not None:
            self.status = status
        if tb_guid is not None:
            self.tb_guid = tb_guid
        if tb_logic_guid is not None:
            self.tb_logic_guid = tb_logic_guid
        self.dw_type = dw_type
        if l1 is not None:
            self.l1 = l1
        if l2 is not None:
            self.l2 = l2
        if l3 is not None:
            self.l3 = l3
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if approval_info is not None:
            self.approval_info = approval_info
        if new_biz is not None:
            self.new_biz = new_biz
        if dimension_group is not None:
            self.dimension_group = dimension_group
        if group_name is not None:
            self.group_name = group_name
        if group_code is not None:
            self.group_code = group_code
        if time_period is not None:
            self.time_period = time_period
        if table_attributes is not None:
            self.table_attributes = table_attributes
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
        if publish_to_dlm is not None:
            self.publish_to_dlm = publish_to_dlm
        if summary_status is not None:
            self.summary_status = summary_status
        if distribute is not None:
            self.distribute = distribute
        if distribute_column is not None:
            self.distribute_column = distribute_column
        if compression is not None:
            self.compression = compression
        if obs_location is not None:
            self.obs_location = obs_location
        if pre_combine_field is not None:
            self.pre_combine_field = pre_combine_field
        if table_type is not None:
            self.table_type = table_type
        if dlf_task_id is not None:
            self.dlf_task_id = dlf_task_id
        if quality_id is not None:
            self.quality_id = quality_id
        if reversed is not None:
            self.reversed = reversed
        if table_version is not None:
            self.table_version = table_version
        if partition_conf is not None:
            self.partition_conf = partition_conf
        if dirty_out_switch is not None:
            self.dirty_out_switch = dirty_out_switch
        if dirty_out_database is not None:
            self.dirty_out_database = dirty_out_database
        if dirty_out_prefix is not None:
            self.dirty_out_prefix = dirty_out_prefix
        if dirty_out_suffix is not None:
            self.dirty_out_suffix = dirty_out_suffix
        if alias is not None:
            self.alias = alias
        if configs is not None:
            self.configs = configs
        if self_defined_fields is not None:
            self.self_defined_fields = self_defined_fields
        if api_id is not None:
            self.api_id = api_id
        if sql is not None:
            self.sql = sql
        if dev_version is not None:
            self.dev_version = dev_version
        if prod_version is not None:
            self.prod_version = prod_version
        if dev_version_name is not None:
            self.dev_version_name = dev_version_name
        if prod_version_name is not None:
            self.prod_version_name = prod_version_name
        if env_type is not None:
            self.env_type = env_type
        if model_id is not None:
            self.model_id = model_id
        if model is not None:
            self.model = model

    @property
    def id(self):
        r"""Gets the id of this AggregationLogicTableVO.

        汇总表的唯一系统ID，更新时必填，创建时不须填写，ID字符串。

        :return: The id of this AggregationLogicTableVO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this AggregationLogicTableVO.

        汇总表的唯一系统ID，更新时必填，创建时不须填写，ID字符串。

        :param id: The id of this AggregationLogicTableVO.
        :type id: str
        """
        self._id = id

    @property
    def tb_name(self):
        r"""Gets the tb_name of this AggregationLogicTableVO.

        汇总表英文名称，对应实际的物理表名。

        :return: The tb_name of this AggregationLogicTableVO.
        :rtype: str
        """
        return self._tb_name

    @tb_name.setter
    def tb_name(self, tb_name):
        r"""Sets the tb_name of this AggregationLogicTableVO.

        汇总表英文名称，对应实际的物理表名。

        :param tb_name: The tb_name of this AggregationLogicTableVO.
        :type tb_name: str
        """
        self._tb_name = tb_name

    @property
    def tb_logic_name(self):
        r"""Gets the tb_logic_name of this AggregationLogicTableVO.

        汇总表的中文名，用于展示使用。

        :return: The tb_logic_name of this AggregationLogicTableVO.
        :rtype: str
        """
        return self._tb_logic_name

    @tb_logic_name.setter
    def tb_logic_name(self, tb_logic_name):
        r"""Sets the tb_logic_name of this AggregationLogicTableVO.

        汇总表的中文名，用于展示使用。

        :param tb_logic_name: The tb_logic_name of this AggregationLogicTableVO.
        :type tb_logic_name: str
        """
        self._tb_logic_name = tb_logic_name

    @property
    def l1_id(self):
        r"""Gets the l1_id of this AggregationLogicTableVO.

        主题域分组ID，只读，创建和更新时无需填写，ID字符串。

        :return: The l1_id of this AggregationLogicTableVO.
        :rtype: str
        """
        return self._l1_id

    @l1_id.setter
    def l1_id(self, l1_id):
        r"""Sets the l1_id of this AggregationLogicTableVO.

        主题域分组ID，只读，创建和更新时无需填写，ID字符串。

        :param l1_id: The l1_id of this AggregationLogicTableVO.
        :type l1_id: str
        """
        self._l1_id = l1_id

    @property
    def l2_id(self):
        r"""Gets the l2_id of this AggregationLogicTableVO.

        主题域ID，只读，创建和更新时无需填写。

        :return: The l2_id of this AggregationLogicTableVO.
        :rtype: str
        """
        return self._l2_id

    @l2_id.setter
    def l2_id(self, l2_id):
        r"""Sets the l2_id of this AggregationLogicTableVO.

        主题域ID，只读，创建和更新时无需填写。

        :param l2_id: The l2_id of this AggregationLogicTableVO.
        :type l2_id: str
        """
        self._l2_id = l2_id

    @property
    def l3_id(self):
        r"""Gets the l3_id of this AggregationLogicTableVO.

        汇总表所属主题的ID，必填，ID字符串。

        :return: The l3_id of this AggregationLogicTableVO.
        :rtype: str
        """
        return self._l3_id

    @l3_id.setter
    def l3_id(self, l3_id):
        r"""Sets the l3_id of this AggregationLogicTableVO.

        汇总表所属主题的ID，必填，ID字符串。

        :param l3_id: The l3_id of this AggregationLogicTableVO.
        :type l3_id: str
        """
        self._l3_id = l3_id

    @property
    def description(self):
        r"""Gets the description of this AggregationLogicTableVO.

        汇总表描述信息。

        :return: The description of this AggregationLogicTableVO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this AggregationLogicTableVO.

        汇总表描述信息。

        :param description: The description of this AggregationLogicTableVO.
        :type description: str
        """
        self._description = description

    @property
    def owner(self):
        r"""Gets the owner of this AggregationLogicTableVO.

        汇总表的资产责任人。

        :return: The owner of this AggregationLogicTableVO.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        r"""Sets the owner of this AggregationLogicTableVO.

        汇总表的资产责任人。

        :param owner: The owner of this AggregationLogicTableVO.
        :type owner: str
        """
        self._owner = owner

    @property
    def secret_type(self):
        r"""Gets the secret_type of this AggregationLogicTableVO.

        :return: The secret_type of this AggregationLogicTableVO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.SecretTypeEnum`
        """
        return self._secret_type

    @secret_type.setter
    def secret_type(self, secret_type):
        r"""Sets the secret_type of this AggregationLogicTableVO.

        :param secret_type: The secret_type of this AggregationLogicTableVO.
        :type secret_type: :class:`huaweicloudsdkdataartsstudio.v1.SecretTypeEnum`
        """
        self._secret_type = secret_type

    @property
    def apply_bg(self):
        r"""Gets the apply_bg of this AggregationLogicTableVO.

        :return: The apply_bg of this AggregationLogicTableVO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ApplyBgEnum`
        """
        return self._apply_bg

    @apply_bg.setter
    def apply_bg(self, apply_bg):
        r"""Sets the apply_bg of this AggregationLogicTableVO.

        :param apply_bg: The apply_bg of this AggregationLogicTableVO.
        :type apply_bg: :class:`huaweicloudsdkdataartsstudio.v1.ApplyBgEnum`
        """
        self._apply_bg = apply_bg

    @property
    def create_by(self):
        r"""Gets the create_by of this AggregationLogicTableVO.

        汇总表的创建人，只读，创建和更新时无需填写。

        :return: The create_by of this AggregationLogicTableVO.
        :rtype: str
        """
        return self._create_by

    @create_by.setter
    def create_by(self, create_by):
        r"""Sets the create_by of this AggregationLogicTableVO.

        汇总表的创建人，只读，创建和更新时无需填写。

        :param create_by: The create_by of this AggregationLogicTableVO.
        :type create_by: str
        """
        self._create_by = create_by

    @property
    def queue_name(self):
        r"""Gets the queue_name of this AggregationLogicTableVO.

        dli数据连接执行sql所需的队列，数据连接类型为DLI时必须填写。

        :return: The queue_name of this AggregationLogicTableVO.
        :rtype: str
        """
        return self._queue_name

    @queue_name.setter
    def queue_name(self, queue_name):
        r"""Sets the queue_name of this AggregationLogicTableVO.

        dli数据连接执行sql所需的队列，数据连接类型为DLI时必须填写。

        :param queue_name: The queue_name of this AggregationLogicTableVO.
        :type queue_name: str
        """
        self._queue_name = queue_name

    @property
    def dw_id(self):
        r"""Gets the dw_id of this AggregationLogicTableVO.

        汇总表所在的数据连接ID，为32位十六进制数字。

        :return: The dw_id of this AggregationLogicTableVO.
        :rtype: str
        """
        return self._dw_id

    @dw_id.setter
    def dw_id(self, dw_id):
        r"""Sets the dw_id of this AggregationLogicTableVO.

        汇总表所在的数据连接ID，为32位十六进制数字。

        :param dw_id: The dw_id of this AggregationLogicTableVO.
        :type dw_id: str
        """
        self._dw_id = dw_id

    @property
    def db_name(self):
        r"""Gets the db_name of this AggregationLogicTableVO.

        汇总表所在的数据库名。

        :return: The db_name of this AggregationLogicTableVO.
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        r"""Sets the db_name of this AggregationLogicTableVO.

        汇总表所在的数据库名。

        :param db_name: The db_name of this AggregationLogicTableVO.
        :type db_name: str
        """
        self._db_name = db_name

    @property
    def tb_id(self):
        r"""Gets the tb_id of this AggregationLogicTableVO.

        汇总表创建的表ID，是服务内部ID，只读，创建和更新时无需填写

        :return: The tb_id of this AggregationLogicTableVO.
        :rtype: str
        """
        return self._tb_id

    @tb_id.setter
    def tb_id(self, tb_id):
        r"""Sets the tb_id of this AggregationLogicTableVO.

        汇总表创建的表ID，是服务内部ID，只读，创建和更新时无需填写

        :param tb_id: The tb_id of this AggregationLogicTableVO.
        :type tb_id: str
        """
        self._tb_id = tb_id

    @property
    def schema(self):
        r"""Gets the schema of this AggregationLogicTableVO.

        汇总表所在的Schema名，DWS类型必须填写。

        :return: The schema of this AggregationLogicTableVO.
        :rtype: str
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        r"""Sets the schema of this AggregationLogicTableVO.

        汇总表所在的Schema名，DWS类型必须填写。

        :param schema: The schema of this AggregationLogicTableVO.
        :type schema: str
        """
        self._schema = schema

    @property
    def dw_name(self):
        r"""Gets the dw_name of this AggregationLogicTableVO.

        数据连接名称，只读，创建和更新时无需填写。

        :return: The dw_name of this AggregationLogicTableVO.
        :rtype: str
        """
        return self._dw_name

    @dw_name.setter
    def dw_name(self, dw_name):
        r"""Sets the dw_name of this AggregationLogicTableVO.

        数据连接名称，只读，创建和更新时无需填写。

        :param dw_name: The dw_name of this AggregationLogicTableVO.
        :type dw_name: str
        """
        self._dw_name = dw_name

    @property
    def status(self):
        r"""Gets the status of this AggregationLogicTableVO.

        :return: The status of this AggregationLogicTableVO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.BizStatusEnum`
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this AggregationLogicTableVO.

        :param status: The status of this AggregationLogicTableVO.
        :type status: :class:`huaweicloudsdkdataartsstudio.v1.BizStatusEnum`
        """
        self._status = status

    @property
    def tb_guid(self):
        r"""Gets the tb_guid of this AggregationLogicTableVO.

        表发布后，创建的数据目录技术资产guid，只读，创建和更新时无需填写。

        :return: The tb_guid of this AggregationLogicTableVO.
        :rtype: str
        """
        return self._tb_guid

    @tb_guid.setter
    def tb_guid(self, tb_guid):
        r"""Sets the tb_guid of this AggregationLogicTableVO.

        表发布后，创建的数据目录技术资产guid，只读，创建和更新时无需填写。

        :param tb_guid: The tb_guid of this AggregationLogicTableVO.
        :type tb_guid: str
        """
        self._tb_guid = tb_guid

    @property
    def tb_logic_guid(self):
        r"""Gets the tb_logic_guid of this AggregationLogicTableVO.

        表发布后，创建的数据目录业务资产guid，只读，创建和更新时无需填写。

        :return: The tb_logic_guid of this AggregationLogicTableVO.
        :rtype: str
        """
        return self._tb_logic_guid

    @tb_logic_guid.setter
    def tb_logic_guid(self, tb_logic_guid):
        r"""Sets the tb_logic_guid of this AggregationLogicTableVO.

        表发布后，创建的数据目录业务资产guid，只读，创建和更新时无需填写。

        :param tb_logic_guid: The tb_logic_guid of this AggregationLogicTableVO.
        :type tb_logic_guid: str
        """
        self._tb_logic_guid = tb_logic_guid

    @property
    def dw_type(self):
        r"""Gets the dw_type of this AggregationLogicTableVO.

        数据连接类型，对应表所在的数仓类型，取值可以为DLI、DWS、MRS_HIVE、POSTGRESQL、MRS_SPARK、CLICKHOUSE、MYSQL、ORACLE和DORIS等。

        :return: The dw_type of this AggregationLogicTableVO.
        :rtype: str
        """
        return self._dw_type

    @dw_type.setter
    def dw_type(self, dw_type):
        r"""Sets the dw_type of this AggregationLogicTableVO.

        数据连接类型，对应表所在的数仓类型，取值可以为DLI、DWS、MRS_HIVE、POSTGRESQL、MRS_SPARK、CLICKHOUSE、MYSQL、ORACLE和DORIS等。

        :param dw_type: The dw_type of this AggregationLogicTableVO.
        :type dw_type: str
        """
        self._dw_type = dw_type

    @property
    def l1(self):
        r"""Gets the l1 of this AggregationLogicTableVO.

        主题域分组中文名，只读，创建和更新时无需填写。

        :return: The l1 of this AggregationLogicTableVO.
        :rtype: str
        """
        return self._l1

    @l1.setter
    def l1(self, l1):
        r"""Sets the l1 of this AggregationLogicTableVO.

        主题域分组中文名，只读，创建和更新时无需填写。

        :param l1: The l1 of this AggregationLogicTableVO.
        :type l1: str
        """
        self._l1 = l1

    @property
    def l2(self):
        r"""Gets the l2 of this AggregationLogicTableVO.

        主题域中文名，只读，创建和更新时无需填写。

        :return: The l2 of this AggregationLogicTableVO.
        :rtype: str
        """
        return self._l2

    @l2.setter
    def l2(self, l2):
        r"""Sets the l2 of this AggregationLogicTableVO.

        主题域中文名，只读，创建和更新时无需填写。

        :param l2: The l2 of this AggregationLogicTableVO.
        :type l2: str
        """
        self._l2 = l2

    @property
    def l3(self):
        r"""Gets the l3 of this AggregationLogicTableVO.

        业务对象中文名，只读，创建和更新时无需填写。

        :return: The l3 of this AggregationLogicTableVO.
        :rtype: str
        """
        return self._l3

    @l3.setter
    def l3(self, l3):
        r"""Sets the l3 of this AggregationLogicTableVO.

        业务对象中文名，只读，创建和更新时无需填写。

        :param l3: The l3 of this AggregationLogicTableVO.
        :type l3: str
        """
        self._l3 = l3

    @property
    def create_time(self):
        r"""Gets the create_time of this AggregationLogicTableVO.

        创建时间，只读，创建和更新时无需填写。

        :return: The create_time of this AggregationLogicTableVO.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this AggregationLogicTableVO.

        创建时间，只读，创建和更新时无需填写。

        :param create_time: The create_time of this AggregationLogicTableVO.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this AggregationLogicTableVO.

        更新时间，只读，创建和更新时无需填写。

        :return: The update_time of this AggregationLogicTableVO.
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this AggregationLogicTableVO.

        更新时间，只读，创建和更新时无需填写。

        :param update_time: The update_time of this AggregationLogicTableVO.
        :type update_time: datetime
        """
        self._update_time = update_time

    @property
    def approval_info(self):
        r"""Gets the approval_info of this AggregationLogicTableVO.

        :return: The approval_info of this AggregationLogicTableVO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ApprovalVO`
        """
        return self._approval_info

    @approval_info.setter
    def approval_info(self, approval_info):
        r"""Sets the approval_info of this AggregationLogicTableVO.

        :param approval_info: The approval_info of this AggregationLogicTableVO.
        :type approval_info: :class:`huaweicloudsdkdataartsstudio.v1.ApprovalVO`
        """
        self._approval_info = approval_info

    @property
    def new_biz(self):
        r"""Gets the new_biz of this AggregationLogicTableVO.

        :return: The new_biz of this AggregationLogicTableVO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.BizVersionManageVO`
        """
        return self._new_biz

    @new_biz.setter
    def new_biz(self, new_biz):
        r"""Sets the new_biz of this AggregationLogicTableVO.

        :param new_biz: The new_biz of this AggregationLogicTableVO.
        :type new_biz: :class:`huaweicloudsdkdataartsstudio.v1.BizVersionManageVO`
        """
        self._new_biz = new_biz

    @property
    def dimension_group(self):
        r"""Gets the dimension_group of this AggregationLogicTableVO.

        颗粒度ID。

        :return: The dimension_group of this AggregationLogicTableVO.
        :rtype: str
        """
        return self._dimension_group

    @dimension_group.setter
    def dimension_group(self, dimension_group):
        r"""Sets the dimension_group of this AggregationLogicTableVO.

        颗粒度ID。

        :param dimension_group: The dimension_group of this AggregationLogicTableVO.
        :type dimension_group: str
        """
        self._dimension_group = dimension_group

    @property
    def group_name(self):
        r"""Gets the group_name of this AggregationLogicTableVO.

        颗粒度名称，只读。

        :return: The group_name of this AggregationLogicTableVO.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        r"""Sets the group_name of this AggregationLogicTableVO.

        颗粒度名称，只读。

        :param group_name: The group_name of this AggregationLogicTableVO.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def group_code(self):
        r"""Gets the group_code of this AggregationLogicTableVO.

        颗粒度编码，只读。

        :return: The group_code of this AggregationLogicTableVO.
        :rtype: str
        """
        return self._group_code

    @group_code.setter
    def group_code(self, group_code):
        r"""Sets the group_code of this AggregationLogicTableVO.

        颗粒度编码，只读。

        :param group_code: The group_code of this AggregationLogicTableVO.
        :type group_code: str
        """
        self._group_code = group_code

    @property
    def time_period(self):
        r"""Gets the time_period of this AggregationLogicTableVO.

        :return: The time_period of this AggregationLogicTableVO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.AggregationLogicTableAttributeVO`
        """
        return self._time_period

    @time_period.setter
    def time_period(self, time_period):
        r"""Sets the time_period of this AggregationLogicTableVO.

        :param time_period: The time_period of this AggregationLogicTableVO.
        :type time_period: :class:`huaweicloudsdkdataartsstudio.v1.AggregationLogicTableAttributeVO`
        """
        self._time_period = time_period

    @property
    def table_attributes(self):
        r"""Gets the table_attributes of this AggregationLogicTableVO.

        汇总表属性信息，依据attribute_type判断类型。

        :return: The table_attributes of this AggregationLogicTableVO.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.AggregationLogicTableAttributeVO`]
        """
        return self._table_attributes

    @table_attributes.setter
    def table_attributes(self, table_attributes):
        r"""Sets the table_attributes of this AggregationLogicTableVO.

        汇总表属性信息，依据attribute_type判断类型。

        :param table_attributes: The table_attributes of this AggregationLogicTableVO.
        :type table_attributes: list[:class:`huaweicloudsdkdataartsstudio.v1.AggregationLogicTableAttributeVO`]
        """
        self._table_attributes = table_attributes

    @property
    def physical_table(self):
        r"""Gets the physical_table of this AggregationLogicTableVO.

        :return: The physical_table of this AggregationLogicTableVO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.SyncStatusEnum`
        """
        return self._physical_table

    @physical_table.setter
    def physical_table(self, physical_table):
        r"""Sets the physical_table of this AggregationLogicTableVO.

        :param physical_table: The physical_table of this AggregationLogicTableVO.
        :type physical_table: :class:`huaweicloudsdkdataartsstudio.v1.SyncStatusEnum`
        """
        self._physical_table = physical_table

    @property
    def dev_physical_table(self):
        r"""Gets the dev_physical_table of this AggregationLogicTableVO.

        :return: The dev_physical_table of this AggregationLogicTableVO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.SyncStatusEnum`
        """
        return self._dev_physical_table

    @dev_physical_table.setter
    def dev_physical_table(self, dev_physical_table):
        r"""Sets the dev_physical_table of this AggregationLogicTableVO.

        :param dev_physical_table: The dev_physical_table of this AggregationLogicTableVO.
        :type dev_physical_table: :class:`huaweicloudsdkdataartsstudio.v1.SyncStatusEnum`
        """
        self._dev_physical_table = dev_physical_table

    @property
    def technical_asset(self):
        r"""Gets the technical_asset of this AggregationLogicTableVO.

        :return: The technical_asset of this AggregationLogicTableVO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.SyncStatusEnum`
        """
        return self._technical_asset

    @technical_asset.setter
    def technical_asset(self, technical_asset):
        r"""Sets the technical_asset of this AggregationLogicTableVO.

        :param technical_asset: The technical_asset of this AggregationLogicTableVO.
        :type technical_asset: :class:`huaweicloudsdkdataartsstudio.v1.SyncStatusEnum`
        """
        self._technical_asset = technical_asset

    @property
    def business_asset(self):
        r"""Gets the business_asset of this AggregationLogicTableVO.

        :return: The business_asset of this AggregationLogicTableVO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.SyncStatusEnum`
        """
        return self._business_asset

    @business_asset.setter
    def business_asset(self, business_asset):
        r"""Sets the business_asset of this AggregationLogicTableVO.

        :param business_asset: The business_asset of this AggregationLogicTableVO.
        :type business_asset: :class:`huaweicloudsdkdataartsstudio.v1.SyncStatusEnum`
        """
        self._business_asset = business_asset

    @property
    def meta_data_link(self):
        r"""Gets the meta_data_link of this AggregationLogicTableVO.

        :return: The meta_data_link of this AggregationLogicTableVO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.SyncStatusEnum`
        """
        return self._meta_data_link

    @meta_data_link.setter
    def meta_data_link(self, meta_data_link):
        r"""Sets the meta_data_link of this AggregationLogicTableVO.

        :param meta_data_link: The meta_data_link of this AggregationLogicTableVO.
        :type meta_data_link: :class:`huaweicloudsdkdataartsstudio.v1.SyncStatusEnum`
        """
        self._meta_data_link = meta_data_link

    @property
    def data_quality(self):
        r"""Gets the data_quality of this AggregationLogicTableVO.

        :return: The data_quality of this AggregationLogicTableVO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.SyncStatusEnum`
        """
        return self._data_quality

    @data_quality.setter
    def data_quality(self, data_quality):
        r"""Sets the data_quality of this AggregationLogicTableVO.

        :param data_quality: The data_quality of this AggregationLogicTableVO.
        :type data_quality: :class:`huaweicloudsdkdataartsstudio.v1.SyncStatusEnum`
        """
        self._data_quality = data_quality

    @property
    def dlf_task(self):
        r"""Gets the dlf_task of this AggregationLogicTableVO.

        :return: The dlf_task of this AggregationLogicTableVO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.SyncStatusEnum`
        """
        return self._dlf_task

    @dlf_task.setter
    def dlf_task(self, dlf_task):
        r"""Sets the dlf_task of this AggregationLogicTableVO.

        :param dlf_task: The dlf_task of this AggregationLogicTableVO.
        :type dlf_task: :class:`huaweicloudsdkdataartsstudio.v1.SyncStatusEnum`
        """
        self._dlf_task = dlf_task

    @property
    def publish_to_dlm(self):
        r"""Gets the publish_to_dlm of this AggregationLogicTableVO.

        :return: The publish_to_dlm of this AggregationLogicTableVO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.SyncStatusEnum`
        """
        return self._publish_to_dlm

    @publish_to_dlm.setter
    def publish_to_dlm(self, publish_to_dlm):
        r"""Sets the publish_to_dlm of this AggregationLogicTableVO.

        :param publish_to_dlm: The publish_to_dlm of this AggregationLogicTableVO.
        :type publish_to_dlm: :class:`huaweicloudsdkdataartsstudio.v1.SyncStatusEnum`
        """
        self._publish_to_dlm = publish_to_dlm

    @property
    def summary_status(self):
        r"""Gets the summary_status of this AggregationLogicTableVO.

        :return: The summary_status of this AggregationLogicTableVO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.SyncStatusEnum`
        """
        return self._summary_status

    @summary_status.setter
    def summary_status(self, summary_status):
        r"""Sets the summary_status of this AggregationLogicTableVO.

        :param summary_status: The summary_status of this AggregationLogicTableVO.
        :type summary_status: :class:`huaweicloudsdkdataartsstudio.v1.SyncStatusEnum`
        """
        self._summary_status = summary_status

    @property
    def distribute(self):
        r"""Gets the distribute of this AggregationLogicTableVO.

        DISTRIBUTE BY [HASH(column)|REPLICATION]。 枚举值：   - HASH: 对指定的列进行Hash，通过映射，把数据分布到指定DN   - REPLICATION: 表的每一行存在所有数据节点（DN）中，即每个数据节点都有完整的表数据 

        :return: The distribute of this AggregationLogicTableVO.
        :rtype: str
        """
        return self._distribute

    @distribute.setter
    def distribute(self, distribute):
        r"""Sets the distribute of this AggregationLogicTableVO.

        DISTRIBUTE BY [HASH(column)|REPLICATION]。 枚举值：   - HASH: 对指定的列进行Hash，通过映射，把数据分布到指定DN   - REPLICATION: 表的每一行存在所有数据节点（DN）中，即每个数据节点都有完整的表数据 

        :param distribute: The distribute of this AggregationLogicTableVO.
        :type distribute: str
        """
        self._distribute = distribute

    @property
    def distribute_column(self):
        r"""Gets the distribute_column of this AggregationLogicTableVO.

        DISTRIBUTE BY HASH column.

        :return: The distribute_column of this AggregationLogicTableVO.
        :rtype: str
        """
        return self._distribute_column

    @distribute_column.setter
    def distribute_column(self, distribute_column):
        r"""Sets the distribute_column of this AggregationLogicTableVO.

        DISTRIBUTE BY HASH column.

        :param distribute_column: The distribute_column of this AggregationLogicTableVO.
        :type distribute_column: str
        """
        self._distribute_column = distribute_column

    @property
    def compression(self):
        r"""Gets the compression of this AggregationLogicTableVO.

        DWS数据压缩等级，列压缩等级为no/low/middle/high，行压缩等级为no/yes。 枚举值：   - \"NO\": 不压缩   - \"YES\": 压缩   - \"LOW\": 低等级压缩   - \"MIDDLE\": 中等级压缩   - \"HIGH\": 高等级压缩 

        :return: The compression of this AggregationLogicTableVO.
        :rtype: str
        """
        return self._compression

    @compression.setter
    def compression(self, compression):
        r"""Sets the compression of this AggregationLogicTableVO.

        DWS数据压缩等级，列压缩等级为no/low/middle/high，行压缩等级为no/yes。 枚举值：   - \"NO\": 不压缩   - \"YES\": 压缩   - \"LOW\": 低等级压缩   - \"MIDDLE\": 中等级压缩   - \"HIGH\": 高等级压缩 

        :param compression: The compression of this AggregationLogicTableVO.
        :type compression: str
        """
        self._compression = compression

    @property
    def obs_location(self):
        r"""Gets the obs_location of this AggregationLogicTableVO.

        外表路径。

        :return: The obs_location of this AggregationLogicTableVO.
        :rtype: str
        """
        return self._obs_location

    @obs_location.setter
    def obs_location(self, obs_location):
        r"""Sets the obs_location of this AggregationLogicTableVO.

        外表路径。

        :param obs_location: The obs_location of this AggregationLogicTableVO.
        :type obs_location: str
        """
        self._obs_location = obs_location

    @property
    def pre_combine_field(self):
        r"""Gets the pre_combine_field of this AggregationLogicTableVO.

        版本字段。

        :return: The pre_combine_field of this AggregationLogicTableVO.
        :rtype: str
        """
        return self._pre_combine_field

    @pre_combine_field.setter
    def pre_combine_field(self, pre_combine_field):
        r"""Sets the pre_combine_field of this AggregationLogicTableVO.

        版本字段。

        :param pre_combine_field: The pre_combine_field of this AggregationLogicTableVO.
        :type pre_combine_field: str
        """
        self._pre_combine_field = pre_combine_field

    @property
    def table_type(self):
        r"""Gets the table_type of this AggregationLogicTableVO.

        表类型。

        :return: The table_type of this AggregationLogicTableVO.
        :rtype: str
        """
        return self._table_type

    @table_type.setter
    def table_type(self, table_type):
        r"""Sets the table_type of this AggregationLogicTableVO.

        表类型。

        :param table_type: The table_type of this AggregationLogicTableVO.
        :type table_type: str
        """
        self._table_type = table_type

    @property
    def dlf_task_id(self):
        r"""Gets the dlf_task_id of this AggregationLogicTableVO.

        DLF作业ID。

        :return: The dlf_task_id of this AggregationLogicTableVO.
        :rtype: str
        """
        return self._dlf_task_id

    @dlf_task_id.setter
    def dlf_task_id(self, dlf_task_id):
        r"""Sets the dlf_task_id of this AggregationLogicTableVO.

        DLF作业ID。

        :param dlf_task_id: The dlf_task_id of this AggregationLogicTableVO.
        :type dlf_task_id: str
        """
        self._dlf_task_id = dlf_task_id

    @property
    def quality_id(self):
        r"""Gets the quality_id of this AggregationLogicTableVO.

        质量ID，ID字符串。

        :return: The quality_id of this AggregationLogicTableVO.
        :rtype: str
        """
        return self._quality_id

    @quality_id.setter
    def quality_id(self, quality_id):
        r"""Sets the quality_id of this AggregationLogicTableVO.

        质量ID，ID字符串。

        :param quality_id: The quality_id of this AggregationLogicTableVO.
        :type quality_id: str
        """
        self._quality_id = quality_id

    @property
    def reversed(self):
        r"""Gets the reversed of this AggregationLogicTableVO.

        是否是逆向的，只读。

        :return: The reversed of this AggregationLogicTableVO.
        :rtype: bool
        """
        return self._reversed

    @reversed.setter
    def reversed(self, reversed):
        r"""Sets the reversed of this AggregationLogicTableVO.

        是否是逆向的，只读。

        :param reversed: The reversed of this AggregationLogicTableVO.
        :type reversed: bool
        """
        self._reversed = reversed

    @property
    def table_version(self):
        r"""Gets the table_version of this AggregationLogicTableVO.

        为2时，表示汇总表是汇总生成的，只读。

        :return: The table_version of this AggregationLogicTableVO.
        :rtype: int
        """
        return self._table_version

    @table_version.setter
    def table_version(self, table_version):
        r"""Sets the table_version of this AggregationLogicTableVO.

        为2时，表示汇总表是汇总生成的，只读。

        :param table_version: The table_version of this AggregationLogicTableVO.
        :type table_version: int
        """
        self._table_version = table_version

    @property
    def partition_conf(self):
        r"""Gets the partition_conf of this AggregationLogicTableVO.

        分区表达式。

        :return: The partition_conf of this AggregationLogicTableVO.
        :rtype: str
        """
        return self._partition_conf

    @partition_conf.setter
    def partition_conf(self, partition_conf):
        r"""Sets the partition_conf of this AggregationLogicTableVO.

        分区表达式。

        :param partition_conf: The partition_conf of this AggregationLogicTableVO.
        :type partition_conf: str
        """
        self._partition_conf = partition_conf

    @property
    def dirty_out_switch(self):
        r"""Gets the dirty_out_switch of this AggregationLogicTableVO.

        异常数据输出开关。

        :return: The dirty_out_switch of this AggregationLogicTableVO.
        :rtype: bool
        """
        return self._dirty_out_switch

    @dirty_out_switch.setter
    def dirty_out_switch(self, dirty_out_switch):
        r"""Sets the dirty_out_switch of this AggregationLogicTableVO.

        异常数据输出开关。

        :param dirty_out_switch: The dirty_out_switch of this AggregationLogicTableVO.
        :type dirty_out_switch: bool
        """
        self._dirty_out_switch = dirty_out_switch

    @property
    def dirty_out_database(self):
        r"""Gets the dirty_out_database of this AggregationLogicTableVO.

        异常数据输出库。

        :return: The dirty_out_database of this AggregationLogicTableVO.
        :rtype: str
        """
        return self._dirty_out_database

    @dirty_out_database.setter
    def dirty_out_database(self, dirty_out_database):
        r"""Sets the dirty_out_database of this AggregationLogicTableVO.

        异常数据输出库。

        :param dirty_out_database: The dirty_out_database of this AggregationLogicTableVO.
        :type dirty_out_database: str
        """
        self._dirty_out_database = dirty_out_database

    @property
    def dirty_out_prefix(self):
        r"""Gets the dirty_out_prefix of this AggregationLogicTableVO.

        异常表前缀。

        :return: The dirty_out_prefix of this AggregationLogicTableVO.
        :rtype: str
        """
        return self._dirty_out_prefix

    @dirty_out_prefix.setter
    def dirty_out_prefix(self, dirty_out_prefix):
        r"""Sets the dirty_out_prefix of this AggregationLogicTableVO.

        异常表前缀。

        :param dirty_out_prefix: The dirty_out_prefix of this AggregationLogicTableVO.
        :type dirty_out_prefix: str
        """
        self._dirty_out_prefix = dirty_out_prefix

    @property
    def dirty_out_suffix(self):
        r"""Gets the dirty_out_suffix of this AggregationLogicTableVO.

        异常表后缀。

        :return: The dirty_out_suffix of this AggregationLogicTableVO.
        :rtype: str
        """
        return self._dirty_out_suffix

    @dirty_out_suffix.setter
    def dirty_out_suffix(self, dirty_out_suffix):
        r"""Sets the dirty_out_suffix of this AggregationLogicTableVO.

        异常表后缀。

        :param dirty_out_suffix: The dirty_out_suffix of this AggregationLogicTableVO.
        :type dirty_out_suffix: str
        """
        self._dirty_out_suffix = dirty_out_suffix

    @property
    def alias(self):
        r"""Gets the alias of this AggregationLogicTableVO.

        别名。

        :return: The alias of this AggregationLogicTableVO.
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        r"""Sets the alias of this AggregationLogicTableVO.

        别名。

        :param alias: The alias of this AggregationLogicTableVO.
        :type alias: str
        """
        self._alias = alias

    @property
    def configs(self):
        r"""Gets the configs of this AggregationLogicTableVO.

        其他配置。

        :return: The configs of this AggregationLogicTableVO.
        :rtype: str
        """
        return self._configs

    @configs.setter
    def configs(self, configs):
        r"""Sets the configs of this AggregationLogicTableVO.

        其他配置。

        :param configs: The configs of this AggregationLogicTableVO.
        :type configs: str
        """
        self._configs = configs

    @property
    def self_defined_fields(self):
        r"""Gets the self_defined_fields of this AggregationLogicTableVO.

        自定义项。

        :return: The self_defined_fields of this AggregationLogicTableVO.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.SelfDefinedFieldVO`]
        """
        return self._self_defined_fields

    @self_defined_fields.setter
    def self_defined_fields(self, self_defined_fields):
        r"""Sets the self_defined_fields of this AggregationLogicTableVO.

        自定义项。

        :param self_defined_fields: The self_defined_fields of this AggregationLogicTableVO.
        :type self_defined_fields: list[:class:`huaweicloudsdkdataartsstudio.v1.SelfDefinedFieldVO`]
        """
        self._self_defined_fields = self_defined_fields

    @property
    def api_id(self):
        r"""Gets the api_id of this AggregationLogicTableVO.

        API ID。

        :return: The api_id of this AggregationLogicTableVO.
        :rtype: str
        """
        return self._api_id

    @api_id.setter
    def api_id(self, api_id):
        r"""Sets the api_id of this AggregationLogicTableVO.

        API ID。

        :param api_id: The api_id of this AggregationLogicTableVO.
        :type api_id: str
        """
        self._api_id = api_id

    @property
    def sql(self):
        r"""Gets the sql of this AggregationLogicTableVO.

        汇总表绑定的SQL。

        :return: The sql of this AggregationLogicTableVO.
        :rtype: str
        """
        return self._sql

    @sql.setter
    def sql(self, sql):
        r"""Sets the sql of this AggregationLogicTableVO.

        汇总表绑定的SQL。

        :param sql: The sql of this AggregationLogicTableVO.
        :type sql: str
        """
        self._sql = sql

    @property
    def dev_version(self):
        r"""Gets the dev_version of this AggregationLogicTableVO.

        开发环境版本，ID字符串。

        :return: The dev_version of this AggregationLogicTableVO.
        :rtype: str
        """
        return self._dev_version

    @dev_version.setter
    def dev_version(self, dev_version):
        r"""Sets the dev_version of this AggregationLogicTableVO.

        开发环境版本，ID字符串。

        :param dev_version: The dev_version of this AggregationLogicTableVO.
        :type dev_version: str
        """
        self._dev_version = dev_version

    @property
    def prod_version(self):
        r"""Gets the prod_version of this AggregationLogicTableVO.

        生产环境版本，ID字符串。

        :return: The prod_version of this AggregationLogicTableVO.
        :rtype: str
        """
        return self._prod_version

    @prod_version.setter
    def prod_version(self, prod_version):
        r"""Sets the prod_version of this AggregationLogicTableVO.

        生产环境版本，ID字符串。

        :param prod_version: The prod_version of this AggregationLogicTableVO.
        :type prod_version: str
        """
        self._prod_version = prod_version

    @property
    def dev_version_name(self):
        r"""Gets the dev_version_name of this AggregationLogicTableVO.

        开发环境版本名称

        :return: The dev_version_name of this AggregationLogicTableVO.
        :rtype: str
        """
        return self._dev_version_name

    @dev_version_name.setter
    def dev_version_name(self, dev_version_name):
        r"""Sets the dev_version_name of this AggregationLogicTableVO.

        开发环境版本名称

        :param dev_version_name: The dev_version_name of this AggregationLogicTableVO.
        :type dev_version_name: str
        """
        self._dev_version_name = dev_version_name

    @property
    def prod_version_name(self):
        r"""Gets the prod_version_name of this AggregationLogicTableVO.

        生产环境版本名称

        :return: The prod_version_name of this AggregationLogicTableVO.
        :rtype: str
        """
        return self._prod_version_name

    @prod_version_name.setter
    def prod_version_name(self, prod_version_name):
        r"""Sets the prod_version_name of this AggregationLogicTableVO.

        生产环境版本名称

        :param prod_version_name: The prod_version_name of this AggregationLogicTableVO.
        :type prod_version_name: str
        """
        self._prod_version_name = prod_version_name

    @property
    def env_type(self):
        r"""Gets the env_type of this AggregationLogicTableVO.

        :return: The env_type of this AggregationLogicTableVO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.EnvTypeEnum`
        """
        return self._env_type

    @env_type.setter
    def env_type(self, env_type):
        r"""Sets the env_type of this AggregationLogicTableVO.

        :param env_type: The env_type of this AggregationLogicTableVO.
        :type env_type: :class:`huaweicloudsdkdataartsstudio.v1.EnvTypeEnum`
        """
        self._env_type = env_type

    @property
    def model_id(self):
        r"""Gets the model_id of this AggregationLogicTableVO.

        所属模型ID，ID字符串。

        :return: The model_id of this AggregationLogicTableVO.
        :rtype: str
        """
        return self._model_id

    @model_id.setter
    def model_id(self, model_id):
        r"""Sets the model_id of this AggregationLogicTableVO.

        所属模型ID，ID字符串。

        :param model_id: The model_id of this AggregationLogicTableVO.
        :type model_id: str
        """
        self._model_id = model_id

    @property
    def model(self):
        r"""Gets the model of this AggregationLogicTableVO.

        :return: The model of this AggregationLogicTableVO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.WorkspaceVO`
        """
        return self._model

    @model.setter
    def model(self, model):
        r"""Sets the model of this AggregationLogicTableVO.

        :param model: The model of this AggregationLogicTableVO.
        :type model: :class:`huaweicloudsdkdataartsstudio.v1.WorkspaceVO`
        """
        self._model = model

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
        if not isinstance(other, AggregationLogicTableVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
