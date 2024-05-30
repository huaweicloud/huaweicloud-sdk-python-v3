# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FactLogicTableVO:

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
        'dw_name': 'str',
        'owner': 'str',
        'create_by': 'str',
        'queue_name': 'str',
        'dw_id': 'str',
        'db_name': 'str',
        'tb_id': 'str',
        'dim_table_ids': 'list[str]',
        'reversed': 'bool',
        'partition_conf': 'str',
        'dirty_out_switch': 'bool',
        'dirty_out_database': 'str',
        'dirty_out_prefix': 'str',
        'dirty_out_suffix': 'str',
        'schema': 'str',
        'distribute': 'str',
        'distribute_column': 'str',
        'table_type': 'str',
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
        'dimensions': 'list[FactTableAttributeVO]',
        'attributes': 'list[FactTableAttributeVO]',
        'mappings': 'list[TableMappingVO]',
        'measures': 'list[FactTableAttributeVO]',
        'table_attributes': 'list[FactTableAttributeVO]',
        'configs': 'str',
        'physical_table': 'SyncStatusEnum',
        'dev_physical_table': 'SyncStatusEnum',
        'technical_asset': 'SyncStatusEnum',
        'business_asset': 'SyncStatusEnum',
        'meta_data_link': 'SyncStatusEnum',
        'data_quality': 'SyncStatusEnum',
        'summary_status': 'SyncStatusEnum',
        'quality_id': 'str',
        'alias': 'str',
        'self_defined_fields': 'list[SelfDefinedFieldVO]',
        'obs_location': 'str',
        'dev_version': 'str',
        'prod_version': 'str',
        'dev_version_name': 'str',
        'prod_version_name': 'str',
        'env_type': 'EnvTypeEnum',
        'secrecy_levels': 'list[SecrecyLevelVO]'
    }

    attribute_map = {
        'id': 'id',
        'tb_name': 'tb_name',
        'tb_logic_name': 'tb_logic_name',
        'l1_id': 'l1_id',
        'l2_id': 'l2_id',
        'l3_id': 'l3_id',
        'description': 'description',
        'dw_name': 'dw_name',
        'owner': 'owner',
        'create_by': 'create_by',
        'queue_name': 'queue_name',
        'dw_id': 'dw_id',
        'db_name': 'db_name',
        'tb_id': 'tb_id',
        'dim_table_ids': 'dim_table_ids',
        'reversed': 'reversed',
        'partition_conf': 'partition_conf',
        'dirty_out_switch': 'dirty_out_switch',
        'dirty_out_database': 'dirty_out_database',
        'dirty_out_prefix': 'dirty_out_prefix',
        'dirty_out_suffix': 'dirty_out_suffix',
        'schema': 'schema',
        'distribute': 'distribute',
        'distribute_column': 'distribute_column',
        'table_type': 'table_type',
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
        'dimensions': 'dimensions',
        'attributes': 'attributes',
        'mappings': 'mappings',
        'measures': 'measures',
        'table_attributes': 'table_attributes',
        'configs': 'configs',
        'physical_table': 'physical_table',
        'dev_physical_table': 'dev_physical_table',
        'technical_asset': 'technical_asset',
        'business_asset': 'business_asset',
        'meta_data_link': 'meta_data_link',
        'data_quality': 'data_quality',
        'summary_status': 'summary_status',
        'quality_id': 'quality_id',
        'alias': 'alias',
        'self_defined_fields': 'self_defined_fields',
        'obs_location': 'obs_location',
        'dev_version': 'dev_version',
        'prod_version': 'prod_version',
        'dev_version_name': 'dev_version_name',
        'prod_version_name': 'prod_version_name',
        'env_type': 'env_type',
        'secrecy_levels': 'secrecy_levels'
    }

    def __init__(self, id=None, tb_name=None, tb_logic_name=None, l1_id=None, l2_id=None, l3_id=None, description=None, dw_name=None, owner=None, create_by=None, queue_name=None, dw_id=None, db_name=None, tb_id=None, dim_table_ids=None, reversed=None, partition_conf=None, dirty_out_switch=None, dirty_out_database=None, dirty_out_prefix=None, dirty_out_suffix=None, schema=None, distribute=None, distribute_column=None, table_type=None, status=None, tb_guid=None, tb_logic_guid=None, dw_type=None, l1=None, l2=None, l3=None, create_time=None, update_time=None, approval_info=None, new_biz=None, dimensions=None, attributes=None, mappings=None, measures=None, table_attributes=None, configs=None, physical_table=None, dev_physical_table=None, technical_asset=None, business_asset=None, meta_data_link=None, data_quality=None, summary_status=None, quality_id=None, alias=None, self_defined_fields=None, obs_location=None, dev_version=None, prod_version=None, dev_version_name=None, prod_version_name=None, env_type=None, secrecy_levels=None):
        """FactLogicTableVO

        The model defined in huaweicloud sdk

        :param id: 事实表ID，填写String类型替代Long类型。
        :type id: str
        :param tb_name: 表名称。
        :type tb_name: str
        :param tb_logic_name: 逻辑实体名。
        :type tb_logic_name: str
        :param l1_id: 主题域分组ID，只读，填写String类型替代Long类型。
        :type l1_id: str
        :param l2_id: 主题域ID，只读，创建和更新时无需填写。
        :type l2_id: str
        :param l3_id: 业务对象guid，填写String类型替代Long类型。
        :type l3_id: str
        :param description: 描述。
        :type description: str
        :param dw_name: 数据连接名称，只读，创建和更新时无需填写。
        :type dw_name: str
        :param owner: 资产责任人。
        :type owner: str
        :param create_by: 创建人。
        :type create_by: str
        :param queue_name: dli数据连接执行sql所需的队列，数据连接类型为DLI时必须。
        :type queue_name: str
        :param dw_id: 数据连接ID。
        :type dw_id: str
        :param db_name: 库名。
        :type db_name: str
        :param tb_id: 数据表ID，只读。
        :type tb_id: str
        :param dim_table_ids: 关联维度表ID。
        :type dim_table_ids: list[str]
        :param reversed: 是否是逆向的。
        :type reversed: bool
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
        :param schema: DWS类型需要。
        :type schema: str
        :param distribute: DISTRIBUTE BY [HASH(column)|REPLICATION]。 枚举值：   - HASH: 对指定的列进行Hash，通过映射，把数据分布到指定DN   - REPLICATION: 表的每一行存在所有数据节点（DN）中，即每个数据节点都有完整的表数据 
        :type distribute: str
        :param distribute_column: DISTRIBUTE BY HASH column.
        :type distribute_column: str
        :param table_type: 表类型。
        :type table_type: str
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
        :param create_time: 创建时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。
        :type create_time: datetime
        :param update_time: 更新时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。
        :type update_time: datetime
        :param approval_info: 
        :type approval_info: :class:`huaweicloudsdkdataartsstudio.v1.ApprovalVO`
        :param new_biz: 
        :type new_biz: :class:`huaweicloudsdkdataartsstudio.v1.BizVersionManageVO`
        :param dimensions: 事实表维度信息，只读。
        :type dimensions: list[:class:`huaweicloudsdkdataartsstudio.v1.FactTableAttributeVO`]
        :param attributes: 事实表事实属性信息，只读。
        :type attributes: list[:class:`huaweicloudsdkdataartsstudio.v1.FactTableAttributeVO`]
        :param mappings: 表映射信息。
        :type mappings: list[:class:`huaweicloudsdkdataartsstudio.v1.TableMappingVO`]
        :param measures: 事实表度量信息，只读。
        :type measures: list[:class:`huaweicloudsdkdataartsstudio.v1.FactTableAttributeVO`]
        :param table_attributes: 事实表所有属性。
        :type table_attributes: list[:class:`huaweicloudsdkdataartsstudio.v1.FactTableAttributeVO`]
        :param configs: 其他配置
        :type configs: str
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
        :param summary_status: 
        :type summary_status: :class:`huaweicloudsdkdataartsstudio.v1.SyncStatusEnum`
        :param quality_id: 质量ID，填写String类型替代Long类型。
        :type quality_id: str
        :param alias: 别名。
        :type alias: str
        :param self_defined_fields: 自定义项。
        :type self_defined_fields: list[:class:`huaweicloudsdkdataartsstudio.v1.SelfDefinedFieldVO`]
        :param obs_location: 外表路径
        :type obs_location: str
        :param dev_version: 开发环境版本，填写String类型替代Long类型。
        :type dev_version: str
        :param prod_version: 生产环境版本，填写String类型替代Long类型。
        :type prod_version: str
        :param dev_version_name: 开发环境版本名称
        :type dev_version_name: str
        :param prod_version_name: 生产环境版本名称
        :type prod_version_name: str
        :param env_type: 
        :type env_type: :class:`huaweicloudsdkdataartsstudio.v1.EnvTypeEnum`
        :param secrecy_levels: 密级
        :type secrecy_levels: list[:class:`huaweicloudsdkdataartsstudio.v1.SecrecyLevelVO`]
        """
        
        

        self._id = None
        self._tb_name = None
        self._tb_logic_name = None
        self._l1_id = None
        self._l2_id = None
        self._l3_id = None
        self._description = None
        self._dw_name = None
        self._owner = None
        self._create_by = None
        self._queue_name = None
        self._dw_id = None
        self._db_name = None
        self._tb_id = None
        self._dim_table_ids = None
        self._reversed = None
        self._partition_conf = None
        self._dirty_out_switch = None
        self._dirty_out_database = None
        self._dirty_out_prefix = None
        self._dirty_out_suffix = None
        self._schema = None
        self._distribute = None
        self._distribute_column = None
        self._table_type = None
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
        self._dimensions = None
        self._attributes = None
        self._mappings = None
        self._measures = None
        self._table_attributes = None
        self._configs = None
        self._physical_table = None
        self._dev_physical_table = None
        self._technical_asset = None
        self._business_asset = None
        self._meta_data_link = None
        self._data_quality = None
        self._summary_status = None
        self._quality_id = None
        self._alias = None
        self._self_defined_fields = None
        self._obs_location = None
        self._dev_version = None
        self._prod_version = None
        self._dev_version_name = None
        self._prod_version_name = None
        self._env_type = None
        self._secrecy_levels = None
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
        if dw_name is not None:
            self.dw_name = dw_name
        self.owner = owner
        if create_by is not None:
            self.create_by = create_by
        if queue_name is not None:
            self.queue_name = queue_name
        self.dw_id = dw_id
        self.db_name = db_name
        if tb_id is not None:
            self.tb_id = tb_id
        if dim_table_ids is not None:
            self.dim_table_ids = dim_table_ids
        if reversed is not None:
            self.reversed = reversed
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
        if schema is not None:
            self.schema = schema
        if distribute is not None:
            self.distribute = distribute
        if distribute_column is not None:
            self.distribute_column = distribute_column
        if table_type is not None:
            self.table_type = table_type
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
        if dimensions is not None:
            self.dimensions = dimensions
        if attributes is not None:
            self.attributes = attributes
        if mappings is not None:
            self.mappings = mappings
        if measures is not None:
            self.measures = measures
        if table_attributes is not None:
            self.table_attributes = table_attributes
        if configs is not None:
            self.configs = configs
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
        if summary_status is not None:
            self.summary_status = summary_status
        if quality_id is not None:
            self.quality_id = quality_id
        if alias is not None:
            self.alias = alias
        if self_defined_fields is not None:
            self.self_defined_fields = self_defined_fields
        if obs_location is not None:
            self.obs_location = obs_location
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
        if secrecy_levels is not None:
            self.secrecy_levels = secrecy_levels

    @property
    def id(self):
        """Gets the id of this FactLogicTableVO.

        事实表ID，填写String类型替代Long类型。

        :return: The id of this FactLogicTableVO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FactLogicTableVO.

        事实表ID，填写String类型替代Long类型。

        :param id: The id of this FactLogicTableVO.
        :type id: str
        """
        self._id = id

    @property
    def tb_name(self):
        """Gets the tb_name of this FactLogicTableVO.

        表名称。

        :return: The tb_name of this FactLogicTableVO.
        :rtype: str
        """
        return self._tb_name

    @tb_name.setter
    def tb_name(self, tb_name):
        """Sets the tb_name of this FactLogicTableVO.

        表名称。

        :param tb_name: The tb_name of this FactLogicTableVO.
        :type tb_name: str
        """
        self._tb_name = tb_name

    @property
    def tb_logic_name(self):
        """Gets the tb_logic_name of this FactLogicTableVO.

        逻辑实体名。

        :return: The tb_logic_name of this FactLogicTableVO.
        :rtype: str
        """
        return self._tb_logic_name

    @tb_logic_name.setter
    def tb_logic_name(self, tb_logic_name):
        """Sets the tb_logic_name of this FactLogicTableVO.

        逻辑实体名。

        :param tb_logic_name: The tb_logic_name of this FactLogicTableVO.
        :type tb_logic_name: str
        """
        self._tb_logic_name = tb_logic_name

    @property
    def l1_id(self):
        """Gets the l1_id of this FactLogicTableVO.

        主题域分组ID，只读，填写String类型替代Long类型。

        :return: The l1_id of this FactLogicTableVO.
        :rtype: str
        """
        return self._l1_id

    @l1_id.setter
    def l1_id(self, l1_id):
        """Sets the l1_id of this FactLogicTableVO.

        主题域分组ID，只读，填写String类型替代Long类型。

        :param l1_id: The l1_id of this FactLogicTableVO.
        :type l1_id: str
        """
        self._l1_id = l1_id

    @property
    def l2_id(self):
        """Gets the l2_id of this FactLogicTableVO.

        主题域ID，只读，创建和更新时无需填写。

        :return: The l2_id of this FactLogicTableVO.
        :rtype: str
        """
        return self._l2_id

    @l2_id.setter
    def l2_id(self, l2_id):
        """Sets the l2_id of this FactLogicTableVO.

        主题域ID，只读，创建和更新时无需填写。

        :param l2_id: The l2_id of this FactLogicTableVO.
        :type l2_id: str
        """
        self._l2_id = l2_id

    @property
    def l3_id(self):
        """Gets the l3_id of this FactLogicTableVO.

        业务对象guid，填写String类型替代Long类型。

        :return: The l3_id of this FactLogicTableVO.
        :rtype: str
        """
        return self._l3_id

    @l3_id.setter
    def l3_id(self, l3_id):
        """Sets the l3_id of this FactLogicTableVO.

        业务对象guid，填写String类型替代Long类型。

        :param l3_id: The l3_id of this FactLogicTableVO.
        :type l3_id: str
        """
        self._l3_id = l3_id

    @property
    def description(self):
        """Gets the description of this FactLogicTableVO.

        描述。

        :return: The description of this FactLogicTableVO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this FactLogicTableVO.

        描述。

        :param description: The description of this FactLogicTableVO.
        :type description: str
        """
        self._description = description

    @property
    def dw_name(self):
        """Gets the dw_name of this FactLogicTableVO.

        数据连接名称，只读，创建和更新时无需填写。

        :return: The dw_name of this FactLogicTableVO.
        :rtype: str
        """
        return self._dw_name

    @dw_name.setter
    def dw_name(self, dw_name):
        """Sets the dw_name of this FactLogicTableVO.

        数据连接名称，只读，创建和更新时无需填写。

        :param dw_name: The dw_name of this FactLogicTableVO.
        :type dw_name: str
        """
        self._dw_name = dw_name

    @property
    def owner(self):
        """Gets the owner of this FactLogicTableVO.

        资产责任人。

        :return: The owner of this FactLogicTableVO.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this FactLogicTableVO.

        资产责任人。

        :param owner: The owner of this FactLogicTableVO.
        :type owner: str
        """
        self._owner = owner

    @property
    def create_by(self):
        """Gets the create_by of this FactLogicTableVO.

        创建人。

        :return: The create_by of this FactLogicTableVO.
        :rtype: str
        """
        return self._create_by

    @create_by.setter
    def create_by(self, create_by):
        """Sets the create_by of this FactLogicTableVO.

        创建人。

        :param create_by: The create_by of this FactLogicTableVO.
        :type create_by: str
        """
        self._create_by = create_by

    @property
    def queue_name(self):
        """Gets the queue_name of this FactLogicTableVO.

        dli数据连接执行sql所需的队列，数据连接类型为DLI时必须。

        :return: The queue_name of this FactLogicTableVO.
        :rtype: str
        """
        return self._queue_name

    @queue_name.setter
    def queue_name(self, queue_name):
        """Sets the queue_name of this FactLogicTableVO.

        dli数据连接执行sql所需的队列，数据连接类型为DLI时必须。

        :param queue_name: The queue_name of this FactLogicTableVO.
        :type queue_name: str
        """
        self._queue_name = queue_name

    @property
    def dw_id(self):
        """Gets the dw_id of this FactLogicTableVO.

        数据连接ID。

        :return: The dw_id of this FactLogicTableVO.
        :rtype: str
        """
        return self._dw_id

    @dw_id.setter
    def dw_id(self, dw_id):
        """Sets the dw_id of this FactLogicTableVO.

        数据连接ID。

        :param dw_id: The dw_id of this FactLogicTableVO.
        :type dw_id: str
        """
        self._dw_id = dw_id

    @property
    def db_name(self):
        """Gets the db_name of this FactLogicTableVO.

        库名。

        :return: The db_name of this FactLogicTableVO.
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        """Sets the db_name of this FactLogicTableVO.

        库名。

        :param db_name: The db_name of this FactLogicTableVO.
        :type db_name: str
        """
        self._db_name = db_name

    @property
    def tb_id(self):
        """Gets the tb_id of this FactLogicTableVO.

        数据表ID，只读。

        :return: The tb_id of this FactLogicTableVO.
        :rtype: str
        """
        return self._tb_id

    @tb_id.setter
    def tb_id(self, tb_id):
        """Sets the tb_id of this FactLogicTableVO.

        数据表ID，只读。

        :param tb_id: The tb_id of this FactLogicTableVO.
        :type tb_id: str
        """
        self._tb_id = tb_id

    @property
    def dim_table_ids(self):
        """Gets the dim_table_ids of this FactLogicTableVO.

        关联维度表ID。

        :return: The dim_table_ids of this FactLogicTableVO.
        :rtype: list[str]
        """
        return self._dim_table_ids

    @dim_table_ids.setter
    def dim_table_ids(self, dim_table_ids):
        """Sets the dim_table_ids of this FactLogicTableVO.

        关联维度表ID。

        :param dim_table_ids: The dim_table_ids of this FactLogicTableVO.
        :type dim_table_ids: list[str]
        """
        self._dim_table_ids = dim_table_ids

    @property
    def reversed(self):
        """Gets the reversed of this FactLogicTableVO.

        是否是逆向的。

        :return: The reversed of this FactLogicTableVO.
        :rtype: bool
        """
        return self._reversed

    @reversed.setter
    def reversed(self, reversed):
        """Sets the reversed of this FactLogicTableVO.

        是否是逆向的。

        :param reversed: The reversed of this FactLogicTableVO.
        :type reversed: bool
        """
        self._reversed = reversed

    @property
    def partition_conf(self):
        """Gets the partition_conf of this FactLogicTableVO.

        分区表达式。

        :return: The partition_conf of this FactLogicTableVO.
        :rtype: str
        """
        return self._partition_conf

    @partition_conf.setter
    def partition_conf(self, partition_conf):
        """Sets the partition_conf of this FactLogicTableVO.

        分区表达式。

        :param partition_conf: The partition_conf of this FactLogicTableVO.
        :type partition_conf: str
        """
        self._partition_conf = partition_conf

    @property
    def dirty_out_switch(self):
        """Gets the dirty_out_switch of this FactLogicTableVO.

        异常数据输出开关。

        :return: The dirty_out_switch of this FactLogicTableVO.
        :rtype: bool
        """
        return self._dirty_out_switch

    @dirty_out_switch.setter
    def dirty_out_switch(self, dirty_out_switch):
        """Sets the dirty_out_switch of this FactLogicTableVO.

        异常数据输出开关。

        :param dirty_out_switch: The dirty_out_switch of this FactLogicTableVO.
        :type dirty_out_switch: bool
        """
        self._dirty_out_switch = dirty_out_switch

    @property
    def dirty_out_database(self):
        """Gets the dirty_out_database of this FactLogicTableVO.

        异常数据输出库。

        :return: The dirty_out_database of this FactLogicTableVO.
        :rtype: str
        """
        return self._dirty_out_database

    @dirty_out_database.setter
    def dirty_out_database(self, dirty_out_database):
        """Sets the dirty_out_database of this FactLogicTableVO.

        异常数据输出库。

        :param dirty_out_database: The dirty_out_database of this FactLogicTableVO.
        :type dirty_out_database: str
        """
        self._dirty_out_database = dirty_out_database

    @property
    def dirty_out_prefix(self):
        """Gets the dirty_out_prefix of this FactLogicTableVO.

        异常表前缀。

        :return: The dirty_out_prefix of this FactLogicTableVO.
        :rtype: str
        """
        return self._dirty_out_prefix

    @dirty_out_prefix.setter
    def dirty_out_prefix(self, dirty_out_prefix):
        """Sets the dirty_out_prefix of this FactLogicTableVO.

        异常表前缀。

        :param dirty_out_prefix: The dirty_out_prefix of this FactLogicTableVO.
        :type dirty_out_prefix: str
        """
        self._dirty_out_prefix = dirty_out_prefix

    @property
    def dirty_out_suffix(self):
        """Gets the dirty_out_suffix of this FactLogicTableVO.

        异常表后缀。

        :return: The dirty_out_suffix of this FactLogicTableVO.
        :rtype: str
        """
        return self._dirty_out_suffix

    @dirty_out_suffix.setter
    def dirty_out_suffix(self, dirty_out_suffix):
        """Sets the dirty_out_suffix of this FactLogicTableVO.

        异常表后缀。

        :param dirty_out_suffix: The dirty_out_suffix of this FactLogicTableVO.
        :type dirty_out_suffix: str
        """
        self._dirty_out_suffix = dirty_out_suffix

    @property
    def schema(self):
        """Gets the schema of this FactLogicTableVO.

        DWS类型需要。

        :return: The schema of this FactLogicTableVO.
        :rtype: str
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        """Sets the schema of this FactLogicTableVO.

        DWS类型需要。

        :param schema: The schema of this FactLogicTableVO.
        :type schema: str
        """
        self._schema = schema

    @property
    def distribute(self):
        """Gets the distribute of this FactLogicTableVO.

        DISTRIBUTE BY [HASH(column)|REPLICATION]。 枚举值：   - HASH: 对指定的列进行Hash，通过映射，把数据分布到指定DN   - REPLICATION: 表的每一行存在所有数据节点（DN）中，即每个数据节点都有完整的表数据 

        :return: The distribute of this FactLogicTableVO.
        :rtype: str
        """
        return self._distribute

    @distribute.setter
    def distribute(self, distribute):
        """Sets the distribute of this FactLogicTableVO.

        DISTRIBUTE BY [HASH(column)|REPLICATION]。 枚举值：   - HASH: 对指定的列进行Hash，通过映射，把数据分布到指定DN   - REPLICATION: 表的每一行存在所有数据节点（DN）中，即每个数据节点都有完整的表数据 

        :param distribute: The distribute of this FactLogicTableVO.
        :type distribute: str
        """
        self._distribute = distribute

    @property
    def distribute_column(self):
        """Gets the distribute_column of this FactLogicTableVO.

        DISTRIBUTE BY HASH column.

        :return: The distribute_column of this FactLogicTableVO.
        :rtype: str
        """
        return self._distribute_column

    @distribute_column.setter
    def distribute_column(self, distribute_column):
        """Sets the distribute_column of this FactLogicTableVO.

        DISTRIBUTE BY HASH column.

        :param distribute_column: The distribute_column of this FactLogicTableVO.
        :type distribute_column: str
        """
        self._distribute_column = distribute_column

    @property
    def table_type(self):
        """Gets the table_type of this FactLogicTableVO.

        表类型。

        :return: The table_type of this FactLogicTableVO.
        :rtype: str
        """
        return self._table_type

    @table_type.setter
    def table_type(self, table_type):
        """Sets the table_type of this FactLogicTableVO.

        表类型。

        :param table_type: The table_type of this FactLogicTableVO.
        :type table_type: str
        """
        self._table_type = table_type

    @property
    def status(self):
        """Gets the status of this FactLogicTableVO.

        :return: The status of this FactLogicTableVO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.BizStatusEnum`
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this FactLogicTableVO.

        :param status: The status of this FactLogicTableVO.
        :type status: :class:`huaweicloudsdkdataartsstudio.v1.BizStatusEnum`
        """
        self._status = status

    @property
    def tb_guid(self):
        """Gets the tb_guid of this FactLogicTableVO.

        表发布后，创建的数据目录技术资产guid，只读，创建和更新时无需填写。

        :return: The tb_guid of this FactLogicTableVO.
        :rtype: str
        """
        return self._tb_guid

    @tb_guid.setter
    def tb_guid(self, tb_guid):
        """Sets the tb_guid of this FactLogicTableVO.

        表发布后，创建的数据目录技术资产guid，只读，创建和更新时无需填写。

        :param tb_guid: The tb_guid of this FactLogicTableVO.
        :type tb_guid: str
        """
        self._tb_guid = tb_guid

    @property
    def tb_logic_guid(self):
        """Gets the tb_logic_guid of this FactLogicTableVO.

        表发布后，创建的数据目录业务资产guid，只读，创建和更新时无需填写。

        :return: The tb_logic_guid of this FactLogicTableVO.
        :rtype: str
        """
        return self._tb_logic_guid

    @tb_logic_guid.setter
    def tb_logic_guid(self, tb_logic_guid):
        """Sets the tb_logic_guid of this FactLogicTableVO.

        表发布后，创建的数据目录业务资产guid，只读，创建和更新时无需填写。

        :param tb_logic_guid: The tb_logic_guid of this FactLogicTableVO.
        :type tb_logic_guid: str
        """
        self._tb_logic_guid = tb_logic_guid

    @property
    def dw_type(self):
        """Gets the dw_type of this FactLogicTableVO.

        数据连接类型，对应表所在的数仓类型，取值可以为DLI、DWS、MRS_HIVE、POSTGRESQL、MRS_SPARK、CLICKHOUSE、MYSQL、ORACLE和DORIS等。

        :return: The dw_type of this FactLogicTableVO.
        :rtype: str
        """
        return self._dw_type

    @dw_type.setter
    def dw_type(self, dw_type):
        """Sets the dw_type of this FactLogicTableVO.

        数据连接类型，对应表所在的数仓类型，取值可以为DLI、DWS、MRS_HIVE、POSTGRESQL、MRS_SPARK、CLICKHOUSE、MYSQL、ORACLE和DORIS等。

        :param dw_type: The dw_type of this FactLogicTableVO.
        :type dw_type: str
        """
        self._dw_type = dw_type

    @property
    def l1(self):
        """Gets the l1 of this FactLogicTableVO.

        主题域分组中文名，只读，创建和更新时无需填写。

        :return: The l1 of this FactLogicTableVO.
        :rtype: str
        """
        return self._l1

    @l1.setter
    def l1(self, l1):
        """Sets the l1 of this FactLogicTableVO.

        主题域分组中文名，只读，创建和更新时无需填写。

        :param l1: The l1 of this FactLogicTableVO.
        :type l1: str
        """
        self._l1 = l1

    @property
    def l2(self):
        """Gets the l2 of this FactLogicTableVO.

        主题域中文名，只读，创建和更新时无需填写。

        :return: The l2 of this FactLogicTableVO.
        :rtype: str
        """
        return self._l2

    @l2.setter
    def l2(self, l2):
        """Sets the l2 of this FactLogicTableVO.

        主题域中文名，只读，创建和更新时无需填写。

        :param l2: The l2 of this FactLogicTableVO.
        :type l2: str
        """
        self._l2 = l2

    @property
    def l3(self):
        """Gets the l3 of this FactLogicTableVO.

        业务对象中文名，只读，创建和更新时无需填写。

        :return: The l3 of this FactLogicTableVO.
        :rtype: str
        """
        return self._l3

    @l3.setter
    def l3(self, l3):
        """Sets the l3 of this FactLogicTableVO.

        业务对象中文名，只读，创建和更新时无需填写。

        :param l3: The l3 of this FactLogicTableVO.
        :type l3: str
        """
        self._l3 = l3

    @property
    def create_time(self):
        """Gets the create_time of this FactLogicTableVO.

        创建时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。

        :return: The create_time of this FactLogicTableVO.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this FactLogicTableVO.

        创建时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。

        :param create_time: The create_time of this FactLogicTableVO.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this FactLogicTableVO.

        更新时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。

        :return: The update_time of this FactLogicTableVO.
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this FactLogicTableVO.

        更新时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。

        :param update_time: The update_time of this FactLogicTableVO.
        :type update_time: datetime
        """
        self._update_time = update_time

    @property
    def approval_info(self):
        """Gets the approval_info of this FactLogicTableVO.

        :return: The approval_info of this FactLogicTableVO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ApprovalVO`
        """
        return self._approval_info

    @approval_info.setter
    def approval_info(self, approval_info):
        """Sets the approval_info of this FactLogicTableVO.

        :param approval_info: The approval_info of this FactLogicTableVO.
        :type approval_info: :class:`huaweicloudsdkdataartsstudio.v1.ApprovalVO`
        """
        self._approval_info = approval_info

    @property
    def new_biz(self):
        """Gets the new_biz of this FactLogicTableVO.

        :return: The new_biz of this FactLogicTableVO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.BizVersionManageVO`
        """
        return self._new_biz

    @new_biz.setter
    def new_biz(self, new_biz):
        """Sets the new_biz of this FactLogicTableVO.

        :param new_biz: The new_biz of this FactLogicTableVO.
        :type new_biz: :class:`huaweicloudsdkdataartsstudio.v1.BizVersionManageVO`
        """
        self._new_biz = new_biz

    @property
    def dimensions(self):
        """Gets the dimensions of this FactLogicTableVO.

        事实表维度信息，只读。

        :return: The dimensions of this FactLogicTableVO.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.FactTableAttributeVO`]
        """
        return self._dimensions

    @dimensions.setter
    def dimensions(self, dimensions):
        """Sets the dimensions of this FactLogicTableVO.

        事实表维度信息，只读。

        :param dimensions: The dimensions of this FactLogicTableVO.
        :type dimensions: list[:class:`huaweicloudsdkdataartsstudio.v1.FactTableAttributeVO`]
        """
        self._dimensions = dimensions

    @property
    def attributes(self):
        """Gets the attributes of this FactLogicTableVO.

        事实表事实属性信息，只读。

        :return: The attributes of this FactLogicTableVO.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.FactTableAttributeVO`]
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this FactLogicTableVO.

        事实表事实属性信息，只读。

        :param attributes: The attributes of this FactLogicTableVO.
        :type attributes: list[:class:`huaweicloudsdkdataartsstudio.v1.FactTableAttributeVO`]
        """
        self._attributes = attributes

    @property
    def mappings(self):
        """Gets the mappings of this FactLogicTableVO.

        表映射信息。

        :return: The mappings of this FactLogicTableVO.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.TableMappingVO`]
        """
        return self._mappings

    @mappings.setter
    def mappings(self, mappings):
        """Sets the mappings of this FactLogicTableVO.

        表映射信息。

        :param mappings: The mappings of this FactLogicTableVO.
        :type mappings: list[:class:`huaweicloudsdkdataartsstudio.v1.TableMappingVO`]
        """
        self._mappings = mappings

    @property
    def measures(self):
        """Gets the measures of this FactLogicTableVO.

        事实表度量信息，只读。

        :return: The measures of this FactLogicTableVO.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.FactTableAttributeVO`]
        """
        return self._measures

    @measures.setter
    def measures(self, measures):
        """Sets the measures of this FactLogicTableVO.

        事实表度量信息，只读。

        :param measures: The measures of this FactLogicTableVO.
        :type measures: list[:class:`huaweicloudsdkdataartsstudio.v1.FactTableAttributeVO`]
        """
        self._measures = measures

    @property
    def table_attributes(self):
        """Gets the table_attributes of this FactLogicTableVO.

        事实表所有属性。

        :return: The table_attributes of this FactLogicTableVO.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.FactTableAttributeVO`]
        """
        return self._table_attributes

    @table_attributes.setter
    def table_attributes(self, table_attributes):
        """Sets the table_attributes of this FactLogicTableVO.

        事实表所有属性。

        :param table_attributes: The table_attributes of this FactLogicTableVO.
        :type table_attributes: list[:class:`huaweicloudsdkdataartsstudio.v1.FactTableAttributeVO`]
        """
        self._table_attributes = table_attributes

    @property
    def configs(self):
        """Gets the configs of this FactLogicTableVO.

        其他配置

        :return: The configs of this FactLogicTableVO.
        :rtype: str
        """
        return self._configs

    @configs.setter
    def configs(self, configs):
        """Sets the configs of this FactLogicTableVO.

        其他配置

        :param configs: The configs of this FactLogicTableVO.
        :type configs: str
        """
        self._configs = configs

    @property
    def physical_table(self):
        """Gets the physical_table of this FactLogicTableVO.

        :return: The physical_table of this FactLogicTableVO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.SyncStatusEnum`
        """
        return self._physical_table

    @physical_table.setter
    def physical_table(self, physical_table):
        """Sets the physical_table of this FactLogicTableVO.

        :param physical_table: The physical_table of this FactLogicTableVO.
        :type physical_table: :class:`huaweicloudsdkdataartsstudio.v1.SyncStatusEnum`
        """
        self._physical_table = physical_table

    @property
    def dev_physical_table(self):
        """Gets the dev_physical_table of this FactLogicTableVO.

        :return: The dev_physical_table of this FactLogicTableVO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.SyncStatusEnum`
        """
        return self._dev_physical_table

    @dev_physical_table.setter
    def dev_physical_table(self, dev_physical_table):
        """Sets the dev_physical_table of this FactLogicTableVO.

        :param dev_physical_table: The dev_physical_table of this FactLogicTableVO.
        :type dev_physical_table: :class:`huaweicloudsdkdataartsstudio.v1.SyncStatusEnum`
        """
        self._dev_physical_table = dev_physical_table

    @property
    def technical_asset(self):
        """Gets the technical_asset of this FactLogicTableVO.

        :return: The technical_asset of this FactLogicTableVO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.SyncStatusEnum`
        """
        return self._technical_asset

    @technical_asset.setter
    def technical_asset(self, technical_asset):
        """Sets the technical_asset of this FactLogicTableVO.

        :param technical_asset: The technical_asset of this FactLogicTableVO.
        :type technical_asset: :class:`huaweicloudsdkdataartsstudio.v1.SyncStatusEnum`
        """
        self._technical_asset = technical_asset

    @property
    def business_asset(self):
        """Gets the business_asset of this FactLogicTableVO.

        :return: The business_asset of this FactLogicTableVO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.SyncStatusEnum`
        """
        return self._business_asset

    @business_asset.setter
    def business_asset(self, business_asset):
        """Sets the business_asset of this FactLogicTableVO.

        :param business_asset: The business_asset of this FactLogicTableVO.
        :type business_asset: :class:`huaweicloudsdkdataartsstudio.v1.SyncStatusEnum`
        """
        self._business_asset = business_asset

    @property
    def meta_data_link(self):
        """Gets the meta_data_link of this FactLogicTableVO.

        :return: The meta_data_link of this FactLogicTableVO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.SyncStatusEnum`
        """
        return self._meta_data_link

    @meta_data_link.setter
    def meta_data_link(self, meta_data_link):
        """Sets the meta_data_link of this FactLogicTableVO.

        :param meta_data_link: The meta_data_link of this FactLogicTableVO.
        :type meta_data_link: :class:`huaweicloudsdkdataartsstudio.v1.SyncStatusEnum`
        """
        self._meta_data_link = meta_data_link

    @property
    def data_quality(self):
        """Gets the data_quality of this FactLogicTableVO.

        :return: The data_quality of this FactLogicTableVO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.SyncStatusEnum`
        """
        return self._data_quality

    @data_quality.setter
    def data_quality(self, data_quality):
        """Sets the data_quality of this FactLogicTableVO.

        :param data_quality: The data_quality of this FactLogicTableVO.
        :type data_quality: :class:`huaweicloudsdkdataartsstudio.v1.SyncStatusEnum`
        """
        self._data_quality = data_quality

    @property
    def summary_status(self):
        """Gets the summary_status of this FactLogicTableVO.

        :return: The summary_status of this FactLogicTableVO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.SyncStatusEnum`
        """
        return self._summary_status

    @summary_status.setter
    def summary_status(self, summary_status):
        """Sets the summary_status of this FactLogicTableVO.

        :param summary_status: The summary_status of this FactLogicTableVO.
        :type summary_status: :class:`huaweicloudsdkdataartsstudio.v1.SyncStatusEnum`
        """
        self._summary_status = summary_status

    @property
    def quality_id(self):
        """Gets the quality_id of this FactLogicTableVO.

        质量ID，填写String类型替代Long类型。

        :return: The quality_id of this FactLogicTableVO.
        :rtype: str
        """
        return self._quality_id

    @quality_id.setter
    def quality_id(self, quality_id):
        """Sets the quality_id of this FactLogicTableVO.

        质量ID，填写String类型替代Long类型。

        :param quality_id: The quality_id of this FactLogicTableVO.
        :type quality_id: str
        """
        self._quality_id = quality_id

    @property
    def alias(self):
        """Gets the alias of this FactLogicTableVO.

        别名。

        :return: The alias of this FactLogicTableVO.
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """Sets the alias of this FactLogicTableVO.

        别名。

        :param alias: The alias of this FactLogicTableVO.
        :type alias: str
        """
        self._alias = alias

    @property
    def self_defined_fields(self):
        """Gets the self_defined_fields of this FactLogicTableVO.

        自定义项。

        :return: The self_defined_fields of this FactLogicTableVO.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.SelfDefinedFieldVO`]
        """
        return self._self_defined_fields

    @self_defined_fields.setter
    def self_defined_fields(self, self_defined_fields):
        """Sets the self_defined_fields of this FactLogicTableVO.

        自定义项。

        :param self_defined_fields: The self_defined_fields of this FactLogicTableVO.
        :type self_defined_fields: list[:class:`huaweicloudsdkdataartsstudio.v1.SelfDefinedFieldVO`]
        """
        self._self_defined_fields = self_defined_fields

    @property
    def obs_location(self):
        """Gets the obs_location of this FactLogicTableVO.

        外表路径

        :return: The obs_location of this FactLogicTableVO.
        :rtype: str
        """
        return self._obs_location

    @obs_location.setter
    def obs_location(self, obs_location):
        """Sets the obs_location of this FactLogicTableVO.

        外表路径

        :param obs_location: The obs_location of this FactLogicTableVO.
        :type obs_location: str
        """
        self._obs_location = obs_location

    @property
    def dev_version(self):
        """Gets the dev_version of this FactLogicTableVO.

        开发环境版本，填写String类型替代Long类型。

        :return: The dev_version of this FactLogicTableVO.
        :rtype: str
        """
        return self._dev_version

    @dev_version.setter
    def dev_version(self, dev_version):
        """Sets the dev_version of this FactLogicTableVO.

        开发环境版本，填写String类型替代Long类型。

        :param dev_version: The dev_version of this FactLogicTableVO.
        :type dev_version: str
        """
        self._dev_version = dev_version

    @property
    def prod_version(self):
        """Gets the prod_version of this FactLogicTableVO.

        生产环境版本，填写String类型替代Long类型。

        :return: The prod_version of this FactLogicTableVO.
        :rtype: str
        """
        return self._prod_version

    @prod_version.setter
    def prod_version(self, prod_version):
        """Sets the prod_version of this FactLogicTableVO.

        生产环境版本，填写String类型替代Long类型。

        :param prod_version: The prod_version of this FactLogicTableVO.
        :type prod_version: str
        """
        self._prod_version = prod_version

    @property
    def dev_version_name(self):
        """Gets the dev_version_name of this FactLogicTableVO.

        开发环境版本名称

        :return: The dev_version_name of this FactLogicTableVO.
        :rtype: str
        """
        return self._dev_version_name

    @dev_version_name.setter
    def dev_version_name(self, dev_version_name):
        """Sets the dev_version_name of this FactLogicTableVO.

        开发环境版本名称

        :param dev_version_name: The dev_version_name of this FactLogicTableVO.
        :type dev_version_name: str
        """
        self._dev_version_name = dev_version_name

    @property
    def prod_version_name(self):
        """Gets the prod_version_name of this FactLogicTableVO.

        生产环境版本名称

        :return: The prod_version_name of this FactLogicTableVO.
        :rtype: str
        """
        return self._prod_version_name

    @prod_version_name.setter
    def prod_version_name(self, prod_version_name):
        """Sets the prod_version_name of this FactLogicTableVO.

        生产环境版本名称

        :param prod_version_name: The prod_version_name of this FactLogicTableVO.
        :type prod_version_name: str
        """
        self._prod_version_name = prod_version_name

    @property
    def env_type(self):
        """Gets the env_type of this FactLogicTableVO.

        :return: The env_type of this FactLogicTableVO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.EnvTypeEnum`
        """
        return self._env_type

    @env_type.setter
    def env_type(self, env_type):
        """Sets the env_type of this FactLogicTableVO.

        :param env_type: The env_type of this FactLogicTableVO.
        :type env_type: :class:`huaweicloudsdkdataartsstudio.v1.EnvTypeEnum`
        """
        self._env_type = env_type

    @property
    def secrecy_levels(self):
        """Gets the secrecy_levels of this FactLogicTableVO.

        密级

        :return: The secrecy_levels of this FactLogicTableVO.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.SecrecyLevelVO`]
        """
        return self._secrecy_levels

    @secrecy_levels.setter
    def secrecy_levels(self, secrecy_levels):
        """Sets the secrecy_levels of this FactLogicTableVO.

        密级

        :param secrecy_levels: The secrecy_levels of this FactLogicTableVO.
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
        if not isinstance(other, FactLogicTableVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
