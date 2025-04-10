# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TableModelUpdateVO:

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
        'model_id': 'str',
        'parent_table_id': 'str',
        'parent_table_name': 'str',
        'parent_table_code': 'str',
        'model': 'WorkspaceVO',
        'data_format': 'str',
        'obs_bucket': 'str',
        'obs_location': 'str',
        'configs': 'str',
        'table_type': 'str',
        'owner': 'str',
        'tb_name': 'str',
        'dw_id': 'str',
        'db_name': 'str',
        'queue_name': 'str',
        'schema': 'str',
        'extend_info': 'str',
        'tb_guid': 'str',
        'tb_id': 'str',
        'logic_tb_name': 'str',
        'logic_tb_guid': 'str',
        'description': 'str',
        'status': 'BizStatusEnum',
        'logic_tb_id': 'str',
        'biz_catalog_id': 'str',
        'catalog_path': 'str',
        'create_by': 'str',
        'update_by': 'str',
        'create_time': 'datetime',
        'update_time': 'datetime',
        'tags': 'list[TagVO]',
        'approval_info': 'ApprovalVO',
        'new_biz': 'BizVersionManageVO',
        'attributes': 'list[TableModelAttributeVO]',
        'mappings': 'list[TableMappingVO]',
        'relations': 'list[RelationVO]',
        'dw_type': 'str',
        'dw_name': 'str',
        'l1': 'str',
        'l2': 'str',
        'l3': 'str',
        'l1_id': 'str',
        'l2_id': 'str',
        'l3_id': 'str',
        'partition_conf': 'str',
        'dlf_task_id': 'str',
        'use_recently_partition': 'bool',
        'reversed': 'bool',
        'dirty_out_switch': 'bool',
        'dirty_out_database': 'str',
        'dirty_out_prefix': 'str',
        'dirty_out_suffix': 'str',
        'quality_owner': 'str',
        'quality_id': 'str',
        'distribute': 'str',
        'distribute_column': 'str',
        'is_partition': 'bool',
        'physical_table': 'SyncStatusEnum',
        'dev_physical_table': 'SyncStatusEnum',
        'technical_asset': 'SyncStatusEnum',
        'business_asset': 'SyncStatusEnum',
        'meta_data_link': 'SyncStatusEnum',
        'data_quality': 'SyncStatusEnum',
        'summary_status': 'SyncStatusEnum',
        'alias': 'str',
        'self_defined_fields': 'list[SelfDefinedFieldVO]',
        'dev_version': 'str',
        'prod_version': 'str',
        'dev_version_name': 'str',
        'prod_version_name': 'str',
        'env_type': 'EnvTypeEnum',
        'has_related_physical_table': 'bool',
        'has_related_logic_table': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'model_id': 'model_id',
        'parent_table_id': 'parent_table_id',
        'parent_table_name': 'parent_table_name',
        'parent_table_code': 'parent_table_code',
        'model': 'model',
        'data_format': 'data_format',
        'obs_bucket': 'obs_bucket',
        'obs_location': 'obs_location',
        'configs': 'configs',
        'table_type': 'table_type',
        'owner': 'owner',
        'tb_name': 'tb_name',
        'dw_id': 'dw_id',
        'db_name': 'db_name',
        'queue_name': 'queue_name',
        'schema': 'schema',
        'extend_info': 'extend_info',
        'tb_guid': 'tb_guid',
        'tb_id': 'tb_id',
        'logic_tb_name': 'logic_tb_name',
        'logic_tb_guid': 'logic_tb_guid',
        'description': 'description',
        'status': 'status',
        'logic_tb_id': 'logic_tb_id',
        'biz_catalog_id': 'biz_catalog_id',
        'catalog_path': 'catalog_path',
        'create_by': 'create_by',
        'update_by': 'update_by',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'tags': 'tags',
        'approval_info': 'approval_info',
        'new_biz': 'new_biz',
        'attributes': 'attributes',
        'mappings': 'mappings',
        'relations': 'relations',
        'dw_type': 'dw_type',
        'dw_name': 'dw_name',
        'l1': 'l1',
        'l2': 'l2',
        'l3': 'l3',
        'l1_id': 'l1_id',
        'l2_id': 'l2_id',
        'l3_id': 'l3_id',
        'partition_conf': 'partition_conf',
        'dlf_task_id': 'dlf_task_id',
        'use_recently_partition': 'use_recently_partition',
        'reversed': 'reversed',
        'dirty_out_switch': 'dirty_out_switch',
        'dirty_out_database': 'dirty_out_database',
        'dirty_out_prefix': 'dirty_out_prefix',
        'dirty_out_suffix': 'dirty_out_suffix',
        'quality_owner': 'quality_owner',
        'quality_id': 'quality_id',
        'distribute': 'distribute',
        'distribute_column': 'distribute_column',
        'is_partition': 'is_partition',
        'physical_table': 'physical_table',
        'dev_physical_table': 'dev_physical_table',
        'technical_asset': 'technical_asset',
        'business_asset': 'business_asset',
        'meta_data_link': 'meta_data_link',
        'data_quality': 'data_quality',
        'summary_status': 'summary_status',
        'alias': 'alias',
        'self_defined_fields': 'self_defined_fields',
        'dev_version': 'dev_version',
        'prod_version': 'prod_version',
        'dev_version_name': 'dev_version_name',
        'prod_version_name': 'prod_version_name',
        'env_type': 'env_type',
        'has_related_physical_table': 'has_related_physical_table',
        'has_related_logic_table': 'has_related_logic_table'
    }

    def __init__(self, id=None, model_id=None, parent_table_id=None, parent_table_name=None, parent_table_code=None, model=None, data_format=None, obs_bucket=None, obs_location=None, configs=None, table_type=None, owner=None, tb_name=None, dw_id=None, db_name=None, queue_name=None, schema=None, extend_info=None, tb_guid=None, tb_id=None, logic_tb_name=None, logic_tb_guid=None, description=None, status=None, logic_tb_id=None, biz_catalog_id=None, catalog_path=None, create_by=None, update_by=None, create_time=None, update_time=None, tags=None, approval_info=None, new_biz=None, attributes=None, mappings=None, relations=None, dw_type=None, dw_name=None, l1=None, l2=None, l3=None, l1_id=None, l2_id=None, l3_id=None, partition_conf=None, dlf_task_id=None, use_recently_partition=None, reversed=None, dirty_out_switch=None, dirty_out_database=None, dirty_out_prefix=None, dirty_out_suffix=None, quality_owner=None, quality_id=None, distribute=None, distribute_column=None, is_partition=None, physical_table=None, dev_physical_table=None, technical_asset=None, business_asset=None, meta_data_link=None, data_quality=None, summary_status=None, alias=None, self_defined_fields=None, dev_version=None, prod_version=None, dev_version_name=None, prod_version_name=None, env_type=None, has_related_physical_table=None, has_related_logic_table=None):
        r"""TableModelUpdateVO

        The model defined in huaweicloud sdk

        :param id: 编码，ID字符串。
        :type id: str
        :param model_id: 所属关系建模的模型ID，ID字符串。
        :type model_id: str
        :param parent_table_id: 父表ID，ID字符串。
        :type parent_table_id: str
        :param parent_table_name: 父表名称，只读。
        :type parent_table_name: str
        :param parent_table_code: 父表编码，只读。
        :type parent_table_code: str
        :param model: 
        :type model: :class:`huaweicloudsdkdataartsstudio.v1.WorkspaceVO`
        :param data_format: 数据格式。
        :type data_format: str
        :param obs_bucket: obs桶。
        :type obs_bucket: str
        :param obs_location: obs路径。
        :type obs_location: str
        :param configs: 其他配置。
        :type configs: str
        :param table_type: 表类型，只读。
        :type table_type: str
        :param owner: 责任人。
        :type owner: str
        :param tb_name: 表名。
        :type tb_name: str
        :param dw_id: 数据连接ID。
        :type dw_id: str
        :param db_name: 数据库名。
        :type db_name: str
        :param queue_name: dli数据连接执行sql所需的队列，数据连接类型为DLI时必须。
        :type queue_name: str
        :param schema: DWS类型需要。
        :type schema: str
        :param extend_info: 扩展信息。
        :type extend_info: str
        :param tb_guid: 表物化后的guid，只读。
        :type tb_guid: str
        :param tb_id: 数据表ID，只读。
        :type tb_id: str
        :param logic_tb_name: 逻辑实体名。
        :type logic_tb_name: str
        :param logic_tb_guid: 逻辑实体的guid，只读。
        :type logic_tb_guid: str
        :param description: 描述。
        :type description: str
        :param status: 
        :type status: :class:`huaweicloudsdkdataartsstudio.v1.BizStatusEnum`
        :param logic_tb_id: 逻辑实体的ID，ID字符串。
        :type logic_tb_id: str
        :param biz_catalog_id: 归属的业务分类的ID，ID字符串。
        :type biz_catalog_id: str
        :param catalog_path: 归属的业务分类的路径，格式： {\&quot;l1Id\&quot;:\&quot;958408897973161984\&quot;,\&quot;l2Id\&quot;:\&quot;958408897973161985\&quot;,\&quot;l3Id\&quot;:\&quot;958408897973161986\&quot;}。
        :type catalog_path: str
        :param create_by: 创建人，只读。
        :type create_by: str
        :param update_by: 更新人，只读。
        :type update_by: str
        :param create_time: 创建时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。
        :type create_time: datetime
        :param update_time: 更新时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。
        :type update_time: datetime
        :param tags: 表标签，只读。
        :type tags: list[:class:`huaweicloudsdkdataartsstudio.v1.TagVO`]
        :param approval_info: 
        :type approval_info: :class:`huaweicloudsdkdataartsstudio.v1.ApprovalVO`
        :param new_biz: 
        :type new_biz: :class:`huaweicloudsdkdataartsstudio.v1.BizVersionManageVO`
        :param attributes: 表属性信息。
        :type attributes: list[:class:`huaweicloudsdkdataartsstudio.v1.TableModelAttributeVO`]
        :param mappings: 表映射信息。
        :type mappings: list[:class:`huaweicloudsdkdataartsstudio.v1.TableMappingVO`]
        :param relations: 关系。
        :type relations: list[:class:`huaweicloudsdkdataartsstudio.v1.RelationVO`]
        :param dw_type: 数据连接类型，对应表所在的数仓类型，取值可以为DLI、DWS、MRS_HIVE、POSTGRESQL、MRS_SPARK、CLICKHOUSE、MYSQL、ORACLE和DORIS等。
        :type dw_type: str
        :param dw_name: 数据连接名称，只读，创建和更新时无需填写。
        :type dw_name: str
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
        :param partition_conf: 分区表达式
        :type partition_conf: str
        :param dlf_task_id: DLF作业ID。
        :type dlf_task_id: str
        :param use_recently_partition: 是否使用最新分区。
        :type use_recently_partition: bool
        :param reversed: 是否是逆向的。
        :type reversed: bool
        :param dirty_out_switch: 异常数据输出开关。
        :type dirty_out_switch: bool
        :param dirty_out_database: 异常数据输出库。
        :type dirty_out_database: str
        :param dirty_out_prefix: 异常表前缀。
        :type dirty_out_prefix: str
        :param dirty_out_suffix: 异常表后缀。
        :type dirty_out_suffix: str
        :param quality_owner: 质量责任人。
        :type quality_owner: str
        :param quality_id: 质量ID，ID字符串。
        :type quality_id: str
        :param distribute: DISTRIBUTE BY [HASH(column)|REPLICATION]。 枚举值：   - HASH: 对指定的列进行Hash，通过映射，把数据分布到指定DN   - REPLICATION: 表的每一行存在所有数据节点（DN）中，即每个数据节点都有完整的表数据 
        :type distribute: str
        :param distribute_column: DISTRIBUTE BY HASH column.
        :type distribute_column: str
        :param is_partition: 是否分区表，只读。
        :type is_partition: bool
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
        :param alias: 别名。
        :type alias: str
        :param self_defined_fields: 自定义项。
        :type self_defined_fields: list[:class:`huaweicloudsdkdataartsstudio.v1.SelfDefinedFieldVO`]
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
        :param has_related_physical_table: 是否关联了物理表
        :type has_related_physical_table: bool
        :param has_related_logic_table: 是否关联了逻辑实体
        :type has_related_logic_table: bool
        """
        
        

        self._id = None
        self._model_id = None
        self._parent_table_id = None
        self._parent_table_name = None
        self._parent_table_code = None
        self._model = None
        self._data_format = None
        self._obs_bucket = None
        self._obs_location = None
        self._configs = None
        self._table_type = None
        self._owner = None
        self._tb_name = None
        self._dw_id = None
        self._db_name = None
        self._queue_name = None
        self._schema = None
        self._extend_info = None
        self._tb_guid = None
        self._tb_id = None
        self._logic_tb_name = None
        self._logic_tb_guid = None
        self._description = None
        self._status = None
        self._logic_tb_id = None
        self._biz_catalog_id = None
        self._catalog_path = None
        self._create_by = None
        self._update_by = None
        self._create_time = None
        self._update_time = None
        self._tags = None
        self._approval_info = None
        self._new_biz = None
        self._attributes = None
        self._mappings = None
        self._relations = None
        self._dw_type = None
        self._dw_name = None
        self._l1 = None
        self._l2 = None
        self._l3 = None
        self._l1_id = None
        self._l2_id = None
        self._l3_id = None
        self._partition_conf = None
        self._dlf_task_id = None
        self._use_recently_partition = None
        self._reversed = None
        self._dirty_out_switch = None
        self._dirty_out_database = None
        self._dirty_out_prefix = None
        self._dirty_out_suffix = None
        self._quality_owner = None
        self._quality_id = None
        self._distribute = None
        self._distribute_column = None
        self._is_partition = None
        self._physical_table = None
        self._dev_physical_table = None
        self._technical_asset = None
        self._business_asset = None
        self._meta_data_link = None
        self._data_quality = None
        self._summary_status = None
        self._alias = None
        self._self_defined_fields = None
        self._dev_version = None
        self._prod_version = None
        self._dev_version_name = None
        self._prod_version_name = None
        self._env_type = None
        self._has_related_physical_table = None
        self._has_related_logic_table = None
        self.discriminator = None

        self.id = id
        self.model_id = model_id
        if parent_table_id is not None:
            self.parent_table_id = parent_table_id
        if parent_table_name is not None:
            self.parent_table_name = parent_table_name
        if parent_table_code is not None:
            self.parent_table_code = parent_table_code
        if model is not None:
            self.model = model
        if data_format is not None:
            self.data_format = data_format
        if obs_bucket is not None:
            self.obs_bucket = obs_bucket
        if obs_location is not None:
            self.obs_location = obs_location
        if configs is not None:
            self.configs = configs
        if table_type is not None:
            self.table_type = table_type
        if owner is not None:
            self.owner = owner
        self.tb_name = tb_name
        if dw_id is not None:
            self.dw_id = dw_id
        if db_name is not None:
            self.db_name = db_name
        if queue_name is not None:
            self.queue_name = queue_name
        if schema is not None:
            self.schema = schema
        if extend_info is not None:
            self.extend_info = extend_info
        if tb_guid is not None:
            self.tb_guid = tb_guid
        if tb_id is not None:
            self.tb_id = tb_id
        self.logic_tb_name = logic_tb_name
        if logic_tb_guid is not None:
            self.logic_tb_guid = logic_tb_guid
        self.description = description
        if status is not None:
            self.status = status
        if logic_tb_id is not None:
            self.logic_tb_id = logic_tb_id
        if biz_catalog_id is not None:
            self.biz_catalog_id = biz_catalog_id
        if catalog_path is not None:
            self.catalog_path = catalog_path
        if create_by is not None:
            self.create_by = create_by
        if update_by is not None:
            self.update_by = update_by
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if tags is not None:
            self.tags = tags
        if approval_info is not None:
            self.approval_info = approval_info
        if new_biz is not None:
            self.new_biz = new_biz
        self.attributes = attributes
        if mappings is not None:
            self.mappings = mappings
        if relations is not None:
            self.relations = relations
        self.dw_type = dw_type
        if dw_name is not None:
            self.dw_name = dw_name
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
        if partition_conf is not None:
            self.partition_conf = partition_conf
        if dlf_task_id is not None:
            self.dlf_task_id = dlf_task_id
        if use_recently_partition is not None:
            self.use_recently_partition = use_recently_partition
        if reversed is not None:
            self.reversed = reversed
        if dirty_out_switch is not None:
            self.dirty_out_switch = dirty_out_switch
        if dirty_out_database is not None:
            self.dirty_out_database = dirty_out_database
        if dirty_out_prefix is not None:
            self.dirty_out_prefix = dirty_out_prefix
        if dirty_out_suffix is not None:
            self.dirty_out_suffix = dirty_out_suffix
        if quality_owner is not None:
            self.quality_owner = quality_owner
        if quality_id is not None:
            self.quality_id = quality_id
        if distribute is not None:
            self.distribute = distribute
        if distribute_column is not None:
            self.distribute_column = distribute_column
        if is_partition is not None:
            self.is_partition = is_partition
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
        if alias is not None:
            self.alias = alias
        if self_defined_fields is not None:
            self.self_defined_fields = self_defined_fields
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
        if has_related_physical_table is not None:
            self.has_related_physical_table = has_related_physical_table
        if has_related_logic_table is not None:
            self.has_related_logic_table = has_related_logic_table

    @property
    def id(self):
        r"""Gets the id of this TableModelUpdateVO.

        编码，ID字符串。

        :return: The id of this TableModelUpdateVO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this TableModelUpdateVO.

        编码，ID字符串。

        :param id: The id of this TableModelUpdateVO.
        :type id: str
        """
        self._id = id

    @property
    def model_id(self):
        r"""Gets the model_id of this TableModelUpdateVO.

        所属关系建模的模型ID，ID字符串。

        :return: The model_id of this TableModelUpdateVO.
        :rtype: str
        """
        return self._model_id

    @model_id.setter
    def model_id(self, model_id):
        r"""Sets the model_id of this TableModelUpdateVO.

        所属关系建模的模型ID，ID字符串。

        :param model_id: The model_id of this TableModelUpdateVO.
        :type model_id: str
        """
        self._model_id = model_id

    @property
    def parent_table_id(self):
        r"""Gets the parent_table_id of this TableModelUpdateVO.

        父表ID，ID字符串。

        :return: The parent_table_id of this TableModelUpdateVO.
        :rtype: str
        """
        return self._parent_table_id

    @parent_table_id.setter
    def parent_table_id(self, parent_table_id):
        r"""Sets the parent_table_id of this TableModelUpdateVO.

        父表ID，ID字符串。

        :param parent_table_id: The parent_table_id of this TableModelUpdateVO.
        :type parent_table_id: str
        """
        self._parent_table_id = parent_table_id

    @property
    def parent_table_name(self):
        r"""Gets the parent_table_name of this TableModelUpdateVO.

        父表名称，只读。

        :return: The parent_table_name of this TableModelUpdateVO.
        :rtype: str
        """
        return self._parent_table_name

    @parent_table_name.setter
    def parent_table_name(self, parent_table_name):
        r"""Sets the parent_table_name of this TableModelUpdateVO.

        父表名称，只读。

        :param parent_table_name: The parent_table_name of this TableModelUpdateVO.
        :type parent_table_name: str
        """
        self._parent_table_name = parent_table_name

    @property
    def parent_table_code(self):
        r"""Gets the parent_table_code of this TableModelUpdateVO.

        父表编码，只读。

        :return: The parent_table_code of this TableModelUpdateVO.
        :rtype: str
        """
        return self._parent_table_code

    @parent_table_code.setter
    def parent_table_code(self, parent_table_code):
        r"""Sets the parent_table_code of this TableModelUpdateVO.

        父表编码，只读。

        :param parent_table_code: The parent_table_code of this TableModelUpdateVO.
        :type parent_table_code: str
        """
        self._parent_table_code = parent_table_code

    @property
    def model(self):
        r"""Gets the model of this TableModelUpdateVO.

        :return: The model of this TableModelUpdateVO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.WorkspaceVO`
        """
        return self._model

    @model.setter
    def model(self, model):
        r"""Sets the model of this TableModelUpdateVO.

        :param model: The model of this TableModelUpdateVO.
        :type model: :class:`huaweicloudsdkdataartsstudio.v1.WorkspaceVO`
        """
        self._model = model

    @property
    def data_format(self):
        r"""Gets the data_format of this TableModelUpdateVO.

        数据格式。

        :return: The data_format of this TableModelUpdateVO.
        :rtype: str
        """
        return self._data_format

    @data_format.setter
    def data_format(self, data_format):
        r"""Sets the data_format of this TableModelUpdateVO.

        数据格式。

        :param data_format: The data_format of this TableModelUpdateVO.
        :type data_format: str
        """
        self._data_format = data_format

    @property
    def obs_bucket(self):
        r"""Gets the obs_bucket of this TableModelUpdateVO.

        obs桶。

        :return: The obs_bucket of this TableModelUpdateVO.
        :rtype: str
        """
        return self._obs_bucket

    @obs_bucket.setter
    def obs_bucket(self, obs_bucket):
        r"""Sets the obs_bucket of this TableModelUpdateVO.

        obs桶。

        :param obs_bucket: The obs_bucket of this TableModelUpdateVO.
        :type obs_bucket: str
        """
        self._obs_bucket = obs_bucket

    @property
    def obs_location(self):
        r"""Gets the obs_location of this TableModelUpdateVO.

        obs路径。

        :return: The obs_location of this TableModelUpdateVO.
        :rtype: str
        """
        return self._obs_location

    @obs_location.setter
    def obs_location(self, obs_location):
        r"""Sets the obs_location of this TableModelUpdateVO.

        obs路径。

        :param obs_location: The obs_location of this TableModelUpdateVO.
        :type obs_location: str
        """
        self._obs_location = obs_location

    @property
    def configs(self):
        r"""Gets the configs of this TableModelUpdateVO.

        其他配置。

        :return: The configs of this TableModelUpdateVO.
        :rtype: str
        """
        return self._configs

    @configs.setter
    def configs(self, configs):
        r"""Sets the configs of this TableModelUpdateVO.

        其他配置。

        :param configs: The configs of this TableModelUpdateVO.
        :type configs: str
        """
        self._configs = configs

    @property
    def table_type(self):
        r"""Gets the table_type of this TableModelUpdateVO.

        表类型，只读。

        :return: The table_type of this TableModelUpdateVO.
        :rtype: str
        """
        return self._table_type

    @table_type.setter
    def table_type(self, table_type):
        r"""Sets the table_type of this TableModelUpdateVO.

        表类型，只读。

        :param table_type: The table_type of this TableModelUpdateVO.
        :type table_type: str
        """
        self._table_type = table_type

    @property
    def owner(self):
        r"""Gets the owner of this TableModelUpdateVO.

        责任人。

        :return: The owner of this TableModelUpdateVO.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        r"""Sets the owner of this TableModelUpdateVO.

        责任人。

        :param owner: The owner of this TableModelUpdateVO.
        :type owner: str
        """
        self._owner = owner

    @property
    def tb_name(self):
        r"""Gets the tb_name of this TableModelUpdateVO.

        表名。

        :return: The tb_name of this TableModelUpdateVO.
        :rtype: str
        """
        return self._tb_name

    @tb_name.setter
    def tb_name(self, tb_name):
        r"""Sets the tb_name of this TableModelUpdateVO.

        表名。

        :param tb_name: The tb_name of this TableModelUpdateVO.
        :type tb_name: str
        """
        self._tb_name = tb_name

    @property
    def dw_id(self):
        r"""Gets the dw_id of this TableModelUpdateVO.

        数据连接ID。

        :return: The dw_id of this TableModelUpdateVO.
        :rtype: str
        """
        return self._dw_id

    @dw_id.setter
    def dw_id(self, dw_id):
        r"""Sets the dw_id of this TableModelUpdateVO.

        数据连接ID。

        :param dw_id: The dw_id of this TableModelUpdateVO.
        :type dw_id: str
        """
        self._dw_id = dw_id

    @property
    def db_name(self):
        r"""Gets the db_name of this TableModelUpdateVO.

        数据库名。

        :return: The db_name of this TableModelUpdateVO.
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        r"""Sets the db_name of this TableModelUpdateVO.

        数据库名。

        :param db_name: The db_name of this TableModelUpdateVO.
        :type db_name: str
        """
        self._db_name = db_name

    @property
    def queue_name(self):
        r"""Gets the queue_name of this TableModelUpdateVO.

        dli数据连接执行sql所需的队列，数据连接类型为DLI时必须。

        :return: The queue_name of this TableModelUpdateVO.
        :rtype: str
        """
        return self._queue_name

    @queue_name.setter
    def queue_name(self, queue_name):
        r"""Sets the queue_name of this TableModelUpdateVO.

        dli数据连接执行sql所需的队列，数据连接类型为DLI时必须。

        :param queue_name: The queue_name of this TableModelUpdateVO.
        :type queue_name: str
        """
        self._queue_name = queue_name

    @property
    def schema(self):
        r"""Gets the schema of this TableModelUpdateVO.

        DWS类型需要。

        :return: The schema of this TableModelUpdateVO.
        :rtype: str
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        r"""Sets the schema of this TableModelUpdateVO.

        DWS类型需要。

        :param schema: The schema of this TableModelUpdateVO.
        :type schema: str
        """
        self._schema = schema

    @property
    def extend_info(self):
        r"""Gets the extend_info of this TableModelUpdateVO.

        扩展信息。

        :return: The extend_info of this TableModelUpdateVO.
        :rtype: str
        """
        return self._extend_info

    @extend_info.setter
    def extend_info(self, extend_info):
        r"""Sets the extend_info of this TableModelUpdateVO.

        扩展信息。

        :param extend_info: The extend_info of this TableModelUpdateVO.
        :type extend_info: str
        """
        self._extend_info = extend_info

    @property
    def tb_guid(self):
        r"""Gets the tb_guid of this TableModelUpdateVO.

        表物化后的guid，只读。

        :return: The tb_guid of this TableModelUpdateVO.
        :rtype: str
        """
        return self._tb_guid

    @tb_guid.setter
    def tb_guid(self, tb_guid):
        r"""Sets the tb_guid of this TableModelUpdateVO.

        表物化后的guid，只读。

        :param tb_guid: The tb_guid of this TableModelUpdateVO.
        :type tb_guid: str
        """
        self._tb_guid = tb_guid

    @property
    def tb_id(self):
        r"""Gets the tb_id of this TableModelUpdateVO.

        数据表ID，只读。

        :return: The tb_id of this TableModelUpdateVO.
        :rtype: str
        """
        return self._tb_id

    @tb_id.setter
    def tb_id(self, tb_id):
        r"""Sets the tb_id of this TableModelUpdateVO.

        数据表ID，只读。

        :param tb_id: The tb_id of this TableModelUpdateVO.
        :type tb_id: str
        """
        self._tb_id = tb_id

    @property
    def logic_tb_name(self):
        r"""Gets the logic_tb_name of this TableModelUpdateVO.

        逻辑实体名。

        :return: The logic_tb_name of this TableModelUpdateVO.
        :rtype: str
        """
        return self._logic_tb_name

    @logic_tb_name.setter
    def logic_tb_name(self, logic_tb_name):
        r"""Sets the logic_tb_name of this TableModelUpdateVO.

        逻辑实体名。

        :param logic_tb_name: The logic_tb_name of this TableModelUpdateVO.
        :type logic_tb_name: str
        """
        self._logic_tb_name = logic_tb_name

    @property
    def logic_tb_guid(self):
        r"""Gets the logic_tb_guid of this TableModelUpdateVO.

        逻辑实体的guid，只读。

        :return: The logic_tb_guid of this TableModelUpdateVO.
        :rtype: str
        """
        return self._logic_tb_guid

    @logic_tb_guid.setter
    def logic_tb_guid(self, logic_tb_guid):
        r"""Sets the logic_tb_guid of this TableModelUpdateVO.

        逻辑实体的guid，只读。

        :param logic_tb_guid: The logic_tb_guid of this TableModelUpdateVO.
        :type logic_tb_guid: str
        """
        self._logic_tb_guid = logic_tb_guid

    @property
    def description(self):
        r"""Gets the description of this TableModelUpdateVO.

        描述。

        :return: The description of this TableModelUpdateVO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this TableModelUpdateVO.

        描述。

        :param description: The description of this TableModelUpdateVO.
        :type description: str
        """
        self._description = description

    @property
    def status(self):
        r"""Gets the status of this TableModelUpdateVO.

        :return: The status of this TableModelUpdateVO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.BizStatusEnum`
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this TableModelUpdateVO.

        :param status: The status of this TableModelUpdateVO.
        :type status: :class:`huaweicloudsdkdataartsstudio.v1.BizStatusEnum`
        """
        self._status = status

    @property
    def logic_tb_id(self):
        r"""Gets the logic_tb_id of this TableModelUpdateVO.

        逻辑实体的ID，ID字符串。

        :return: The logic_tb_id of this TableModelUpdateVO.
        :rtype: str
        """
        return self._logic_tb_id

    @logic_tb_id.setter
    def logic_tb_id(self, logic_tb_id):
        r"""Sets the logic_tb_id of this TableModelUpdateVO.

        逻辑实体的ID，ID字符串。

        :param logic_tb_id: The logic_tb_id of this TableModelUpdateVO.
        :type logic_tb_id: str
        """
        self._logic_tb_id = logic_tb_id

    @property
    def biz_catalog_id(self):
        r"""Gets the biz_catalog_id of this TableModelUpdateVO.

        归属的业务分类的ID，ID字符串。

        :return: The biz_catalog_id of this TableModelUpdateVO.
        :rtype: str
        """
        return self._biz_catalog_id

    @biz_catalog_id.setter
    def biz_catalog_id(self, biz_catalog_id):
        r"""Sets the biz_catalog_id of this TableModelUpdateVO.

        归属的业务分类的ID，ID字符串。

        :param biz_catalog_id: The biz_catalog_id of this TableModelUpdateVO.
        :type biz_catalog_id: str
        """
        self._biz_catalog_id = biz_catalog_id

    @property
    def catalog_path(self):
        r"""Gets the catalog_path of this TableModelUpdateVO.

        归属的业务分类的路径，格式： {\"l1Id\":\"958408897973161984\",\"l2Id\":\"958408897973161985\",\"l3Id\":\"958408897973161986\"}。

        :return: The catalog_path of this TableModelUpdateVO.
        :rtype: str
        """
        return self._catalog_path

    @catalog_path.setter
    def catalog_path(self, catalog_path):
        r"""Sets the catalog_path of this TableModelUpdateVO.

        归属的业务分类的路径，格式： {\"l1Id\":\"958408897973161984\",\"l2Id\":\"958408897973161985\",\"l3Id\":\"958408897973161986\"}。

        :param catalog_path: The catalog_path of this TableModelUpdateVO.
        :type catalog_path: str
        """
        self._catalog_path = catalog_path

    @property
    def create_by(self):
        r"""Gets the create_by of this TableModelUpdateVO.

        创建人，只读。

        :return: The create_by of this TableModelUpdateVO.
        :rtype: str
        """
        return self._create_by

    @create_by.setter
    def create_by(self, create_by):
        r"""Sets the create_by of this TableModelUpdateVO.

        创建人，只读。

        :param create_by: The create_by of this TableModelUpdateVO.
        :type create_by: str
        """
        self._create_by = create_by

    @property
    def update_by(self):
        r"""Gets the update_by of this TableModelUpdateVO.

        更新人，只读。

        :return: The update_by of this TableModelUpdateVO.
        :rtype: str
        """
        return self._update_by

    @update_by.setter
    def update_by(self, update_by):
        r"""Sets the update_by of this TableModelUpdateVO.

        更新人，只读。

        :param update_by: The update_by of this TableModelUpdateVO.
        :type update_by: str
        """
        self._update_by = update_by

    @property
    def create_time(self):
        r"""Gets the create_time of this TableModelUpdateVO.

        创建时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。

        :return: The create_time of this TableModelUpdateVO.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this TableModelUpdateVO.

        创建时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。

        :param create_time: The create_time of this TableModelUpdateVO.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this TableModelUpdateVO.

        更新时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。

        :return: The update_time of this TableModelUpdateVO.
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this TableModelUpdateVO.

        更新时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。

        :param update_time: The update_time of this TableModelUpdateVO.
        :type update_time: datetime
        """
        self._update_time = update_time

    @property
    def tags(self):
        r"""Gets the tags of this TableModelUpdateVO.

        表标签，只读。

        :return: The tags of this TableModelUpdateVO.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.TagVO`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this TableModelUpdateVO.

        表标签，只读。

        :param tags: The tags of this TableModelUpdateVO.
        :type tags: list[:class:`huaweicloudsdkdataartsstudio.v1.TagVO`]
        """
        self._tags = tags

    @property
    def approval_info(self):
        r"""Gets the approval_info of this TableModelUpdateVO.

        :return: The approval_info of this TableModelUpdateVO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ApprovalVO`
        """
        return self._approval_info

    @approval_info.setter
    def approval_info(self, approval_info):
        r"""Sets the approval_info of this TableModelUpdateVO.

        :param approval_info: The approval_info of this TableModelUpdateVO.
        :type approval_info: :class:`huaweicloudsdkdataartsstudio.v1.ApprovalVO`
        """
        self._approval_info = approval_info

    @property
    def new_biz(self):
        r"""Gets the new_biz of this TableModelUpdateVO.

        :return: The new_biz of this TableModelUpdateVO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.BizVersionManageVO`
        """
        return self._new_biz

    @new_biz.setter
    def new_biz(self, new_biz):
        r"""Sets the new_biz of this TableModelUpdateVO.

        :param new_biz: The new_biz of this TableModelUpdateVO.
        :type new_biz: :class:`huaweicloudsdkdataartsstudio.v1.BizVersionManageVO`
        """
        self._new_biz = new_biz

    @property
    def attributes(self):
        r"""Gets the attributes of this TableModelUpdateVO.

        表属性信息。

        :return: The attributes of this TableModelUpdateVO.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.TableModelAttributeVO`]
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        r"""Sets the attributes of this TableModelUpdateVO.

        表属性信息。

        :param attributes: The attributes of this TableModelUpdateVO.
        :type attributes: list[:class:`huaweicloudsdkdataartsstudio.v1.TableModelAttributeVO`]
        """
        self._attributes = attributes

    @property
    def mappings(self):
        r"""Gets the mappings of this TableModelUpdateVO.

        表映射信息。

        :return: The mappings of this TableModelUpdateVO.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.TableMappingVO`]
        """
        return self._mappings

    @mappings.setter
    def mappings(self, mappings):
        r"""Sets the mappings of this TableModelUpdateVO.

        表映射信息。

        :param mappings: The mappings of this TableModelUpdateVO.
        :type mappings: list[:class:`huaweicloudsdkdataartsstudio.v1.TableMappingVO`]
        """
        self._mappings = mappings

    @property
    def relations(self):
        r"""Gets the relations of this TableModelUpdateVO.

        关系。

        :return: The relations of this TableModelUpdateVO.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.RelationVO`]
        """
        return self._relations

    @relations.setter
    def relations(self, relations):
        r"""Sets the relations of this TableModelUpdateVO.

        关系。

        :param relations: The relations of this TableModelUpdateVO.
        :type relations: list[:class:`huaweicloudsdkdataartsstudio.v1.RelationVO`]
        """
        self._relations = relations

    @property
    def dw_type(self):
        r"""Gets the dw_type of this TableModelUpdateVO.

        数据连接类型，对应表所在的数仓类型，取值可以为DLI、DWS、MRS_HIVE、POSTGRESQL、MRS_SPARK、CLICKHOUSE、MYSQL、ORACLE和DORIS等。

        :return: The dw_type of this TableModelUpdateVO.
        :rtype: str
        """
        return self._dw_type

    @dw_type.setter
    def dw_type(self, dw_type):
        r"""Sets the dw_type of this TableModelUpdateVO.

        数据连接类型，对应表所在的数仓类型，取值可以为DLI、DWS、MRS_HIVE、POSTGRESQL、MRS_SPARK、CLICKHOUSE、MYSQL、ORACLE和DORIS等。

        :param dw_type: The dw_type of this TableModelUpdateVO.
        :type dw_type: str
        """
        self._dw_type = dw_type

    @property
    def dw_name(self):
        r"""Gets the dw_name of this TableModelUpdateVO.

        数据连接名称，只读，创建和更新时无需填写。

        :return: The dw_name of this TableModelUpdateVO.
        :rtype: str
        """
        return self._dw_name

    @dw_name.setter
    def dw_name(self, dw_name):
        r"""Sets the dw_name of this TableModelUpdateVO.

        数据连接名称，只读，创建和更新时无需填写。

        :param dw_name: The dw_name of this TableModelUpdateVO.
        :type dw_name: str
        """
        self._dw_name = dw_name

    @property
    def l1(self):
        r"""Gets the l1 of this TableModelUpdateVO.

        主题域分组中文名，只读，创建和更新时无需填写。

        :return: The l1 of this TableModelUpdateVO.
        :rtype: str
        """
        return self._l1

    @l1.setter
    def l1(self, l1):
        r"""Sets the l1 of this TableModelUpdateVO.

        主题域分组中文名，只读，创建和更新时无需填写。

        :param l1: The l1 of this TableModelUpdateVO.
        :type l1: str
        """
        self._l1 = l1

    @property
    def l2(self):
        r"""Gets the l2 of this TableModelUpdateVO.

        主题域中文名，只读，创建和更新时无需填写。

        :return: The l2 of this TableModelUpdateVO.
        :rtype: str
        """
        return self._l2

    @l2.setter
    def l2(self, l2):
        r"""Sets the l2 of this TableModelUpdateVO.

        主题域中文名，只读，创建和更新时无需填写。

        :param l2: The l2 of this TableModelUpdateVO.
        :type l2: str
        """
        self._l2 = l2

    @property
    def l3(self):
        r"""Gets the l3 of this TableModelUpdateVO.

        业务对象中文名，只读，创建和更新时无需填写。

        :return: The l3 of this TableModelUpdateVO.
        :rtype: str
        """
        return self._l3

    @l3.setter
    def l3(self, l3):
        r"""Sets the l3 of this TableModelUpdateVO.

        业务对象中文名，只读，创建和更新时无需填写。

        :param l3: The l3 of this TableModelUpdateVO.
        :type l3: str
        """
        self._l3 = l3

    @property
    def l1_id(self):
        r"""Gets the l1_id of this TableModelUpdateVO.

        主题域分组ID，只读，ID字符串。

        :return: The l1_id of this TableModelUpdateVO.
        :rtype: str
        """
        return self._l1_id

    @l1_id.setter
    def l1_id(self, l1_id):
        r"""Sets the l1_id of this TableModelUpdateVO.

        主题域分组ID，只读，ID字符串。

        :param l1_id: The l1_id of this TableModelUpdateVO.
        :type l1_id: str
        """
        self._l1_id = l1_id

    @property
    def l2_id(self):
        r"""Gets the l2_id of this TableModelUpdateVO.

        主题域ID，只读，创建和更新时无需填写。

        :return: The l2_id of this TableModelUpdateVO.
        :rtype: str
        """
        return self._l2_id

    @l2_id.setter
    def l2_id(self, l2_id):
        r"""Sets the l2_id of this TableModelUpdateVO.

        主题域ID，只读，创建和更新时无需填写。

        :param l2_id: The l2_id of this TableModelUpdateVO.
        :type l2_id: str
        """
        self._l2_id = l2_id

    @property
    def l3_id(self):
        r"""Gets the l3_id of this TableModelUpdateVO.

        业务对象ID，只读，ID字符串。

        :return: The l3_id of this TableModelUpdateVO.
        :rtype: str
        """
        return self._l3_id

    @l3_id.setter
    def l3_id(self, l3_id):
        r"""Sets the l3_id of this TableModelUpdateVO.

        业务对象ID，只读，ID字符串。

        :param l3_id: The l3_id of this TableModelUpdateVO.
        :type l3_id: str
        """
        self._l3_id = l3_id

    @property
    def partition_conf(self):
        r"""Gets the partition_conf of this TableModelUpdateVO.

        分区表达式

        :return: The partition_conf of this TableModelUpdateVO.
        :rtype: str
        """
        return self._partition_conf

    @partition_conf.setter
    def partition_conf(self, partition_conf):
        r"""Sets the partition_conf of this TableModelUpdateVO.

        分区表达式

        :param partition_conf: The partition_conf of this TableModelUpdateVO.
        :type partition_conf: str
        """
        self._partition_conf = partition_conf

    @property
    def dlf_task_id(self):
        r"""Gets the dlf_task_id of this TableModelUpdateVO.

        DLF作业ID。

        :return: The dlf_task_id of this TableModelUpdateVO.
        :rtype: str
        """
        return self._dlf_task_id

    @dlf_task_id.setter
    def dlf_task_id(self, dlf_task_id):
        r"""Sets the dlf_task_id of this TableModelUpdateVO.

        DLF作业ID。

        :param dlf_task_id: The dlf_task_id of this TableModelUpdateVO.
        :type dlf_task_id: str
        """
        self._dlf_task_id = dlf_task_id

    @property
    def use_recently_partition(self):
        r"""Gets the use_recently_partition of this TableModelUpdateVO.

        是否使用最新分区。

        :return: The use_recently_partition of this TableModelUpdateVO.
        :rtype: bool
        """
        return self._use_recently_partition

    @use_recently_partition.setter
    def use_recently_partition(self, use_recently_partition):
        r"""Sets the use_recently_partition of this TableModelUpdateVO.

        是否使用最新分区。

        :param use_recently_partition: The use_recently_partition of this TableModelUpdateVO.
        :type use_recently_partition: bool
        """
        self._use_recently_partition = use_recently_partition

    @property
    def reversed(self):
        r"""Gets the reversed of this TableModelUpdateVO.

        是否是逆向的。

        :return: The reversed of this TableModelUpdateVO.
        :rtype: bool
        """
        return self._reversed

    @reversed.setter
    def reversed(self, reversed):
        r"""Sets the reversed of this TableModelUpdateVO.

        是否是逆向的。

        :param reversed: The reversed of this TableModelUpdateVO.
        :type reversed: bool
        """
        self._reversed = reversed

    @property
    def dirty_out_switch(self):
        r"""Gets the dirty_out_switch of this TableModelUpdateVO.

        异常数据输出开关。

        :return: The dirty_out_switch of this TableModelUpdateVO.
        :rtype: bool
        """
        return self._dirty_out_switch

    @dirty_out_switch.setter
    def dirty_out_switch(self, dirty_out_switch):
        r"""Sets the dirty_out_switch of this TableModelUpdateVO.

        异常数据输出开关。

        :param dirty_out_switch: The dirty_out_switch of this TableModelUpdateVO.
        :type dirty_out_switch: bool
        """
        self._dirty_out_switch = dirty_out_switch

    @property
    def dirty_out_database(self):
        r"""Gets the dirty_out_database of this TableModelUpdateVO.

        异常数据输出库。

        :return: The dirty_out_database of this TableModelUpdateVO.
        :rtype: str
        """
        return self._dirty_out_database

    @dirty_out_database.setter
    def dirty_out_database(self, dirty_out_database):
        r"""Sets the dirty_out_database of this TableModelUpdateVO.

        异常数据输出库。

        :param dirty_out_database: The dirty_out_database of this TableModelUpdateVO.
        :type dirty_out_database: str
        """
        self._dirty_out_database = dirty_out_database

    @property
    def dirty_out_prefix(self):
        r"""Gets the dirty_out_prefix of this TableModelUpdateVO.

        异常表前缀。

        :return: The dirty_out_prefix of this TableModelUpdateVO.
        :rtype: str
        """
        return self._dirty_out_prefix

    @dirty_out_prefix.setter
    def dirty_out_prefix(self, dirty_out_prefix):
        r"""Sets the dirty_out_prefix of this TableModelUpdateVO.

        异常表前缀。

        :param dirty_out_prefix: The dirty_out_prefix of this TableModelUpdateVO.
        :type dirty_out_prefix: str
        """
        self._dirty_out_prefix = dirty_out_prefix

    @property
    def dirty_out_suffix(self):
        r"""Gets the dirty_out_suffix of this TableModelUpdateVO.

        异常表后缀。

        :return: The dirty_out_suffix of this TableModelUpdateVO.
        :rtype: str
        """
        return self._dirty_out_suffix

    @dirty_out_suffix.setter
    def dirty_out_suffix(self, dirty_out_suffix):
        r"""Sets the dirty_out_suffix of this TableModelUpdateVO.

        异常表后缀。

        :param dirty_out_suffix: The dirty_out_suffix of this TableModelUpdateVO.
        :type dirty_out_suffix: str
        """
        self._dirty_out_suffix = dirty_out_suffix

    @property
    def quality_owner(self):
        r"""Gets the quality_owner of this TableModelUpdateVO.

        质量责任人。

        :return: The quality_owner of this TableModelUpdateVO.
        :rtype: str
        """
        return self._quality_owner

    @quality_owner.setter
    def quality_owner(self, quality_owner):
        r"""Sets the quality_owner of this TableModelUpdateVO.

        质量责任人。

        :param quality_owner: The quality_owner of this TableModelUpdateVO.
        :type quality_owner: str
        """
        self._quality_owner = quality_owner

    @property
    def quality_id(self):
        r"""Gets the quality_id of this TableModelUpdateVO.

        质量ID，ID字符串。

        :return: The quality_id of this TableModelUpdateVO.
        :rtype: str
        """
        return self._quality_id

    @quality_id.setter
    def quality_id(self, quality_id):
        r"""Sets the quality_id of this TableModelUpdateVO.

        质量ID，ID字符串。

        :param quality_id: The quality_id of this TableModelUpdateVO.
        :type quality_id: str
        """
        self._quality_id = quality_id

    @property
    def distribute(self):
        r"""Gets the distribute of this TableModelUpdateVO.

        DISTRIBUTE BY [HASH(column)|REPLICATION]。 枚举值：   - HASH: 对指定的列进行Hash，通过映射，把数据分布到指定DN   - REPLICATION: 表的每一行存在所有数据节点（DN）中，即每个数据节点都有完整的表数据 

        :return: The distribute of this TableModelUpdateVO.
        :rtype: str
        """
        return self._distribute

    @distribute.setter
    def distribute(self, distribute):
        r"""Sets the distribute of this TableModelUpdateVO.

        DISTRIBUTE BY [HASH(column)|REPLICATION]。 枚举值：   - HASH: 对指定的列进行Hash，通过映射，把数据分布到指定DN   - REPLICATION: 表的每一行存在所有数据节点（DN）中，即每个数据节点都有完整的表数据 

        :param distribute: The distribute of this TableModelUpdateVO.
        :type distribute: str
        """
        self._distribute = distribute

    @property
    def distribute_column(self):
        r"""Gets the distribute_column of this TableModelUpdateVO.

        DISTRIBUTE BY HASH column.

        :return: The distribute_column of this TableModelUpdateVO.
        :rtype: str
        """
        return self._distribute_column

    @distribute_column.setter
    def distribute_column(self, distribute_column):
        r"""Sets the distribute_column of this TableModelUpdateVO.

        DISTRIBUTE BY HASH column.

        :param distribute_column: The distribute_column of this TableModelUpdateVO.
        :type distribute_column: str
        """
        self._distribute_column = distribute_column

    @property
    def is_partition(self):
        r"""Gets the is_partition of this TableModelUpdateVO.

        是否分区表，只读。

        :return: The is_partition of this TableModelUpdateVO.
        :rtype: bool
        """
        return self._is_partition

    @is_partition.setter
    def is_partition(self, is_partition):
        r"""Sets the is_partition of this TableModelUpdateVO.

        是否分区表，只读。

        :param is_partition: The is_partition of this TableModelUpdateVO.
        :type is_partition: bool
        """
        self._is_partition = is_partition

    @property
    def physical_table(self):
        r"""Gets the physical_table of this TableModelUpdateVO.

        :return: The physical_table of this TableModelUpdateVO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.SyncStatusEnum`
        """
        return self._physical_table

    @physical_table.setter
    def physical_table(self, physical_table):
        r"""Sets the physical_table of this TableModelUpdateVO.

        :param physical_table: The physical_table of this TableModelUpdateVO.
        :type physical_table: :class:`huaweicloudsdkdataartsstudio.v1.SyncStatusEnum`
        """
        self._physical_table = physical_table

    @property
    def dev_physical_table(self):
        r"""Gets the dev_physical_table of this TableModelUpdateVO.

        :return: The dev_physical_table of this TableModelUpdateVO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.SyncStatusEnum`
        """
        return self._dev_physical_table

    @dev_physical_table.setter
    def dev_physical_table(self, dev_physical_table):
        r"""Sets the dev_physical_table of this TableModelUpdateVO.

        :param dev_physical_table: The dev_physical_table of this TableModelUpdateVO.
        :type dev_physical_table: :class:`huaweicloudsdkdataartsstudio.v1.SyncStatusEnum`
        """
        self._dev_physical_table = dev_physical_table

    @property
    def technical_asset(self):
        r"""Gets the technical_asset of this TableModelUpdateVO.

        :return: The technical_asset of this TableModelUpdateVO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.SyncStatusEnum`
        """
        return self._technical_asset

    @technical_asset.setter
    def technical_asset(self, technical_asset):
        r"""Sets the technical_asset of this TableModelUpdateVO.

        :param technical_asset: The technical_asset of this TableModelUpdateVO.
        :type technical_asset: :class:`huaweicloudsdkdataartsstudio.v1.SyncStatusEnum`
        """
        self._technical_asset = technical_asset

    @property
    def business_asset(self):
        r"""Gets the business_asset of this TableModelUpdateVO.

        :return: The business_asset of this TableModelUpdateVO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.SyncStatusEnum`
        """
        return self._business_asset

    @business_asset.setter
    def business_asset(self, business_asset):
        r"""Sets the business_asset of this TableModelUpdateVO.

        :param business_asset: The business_asset of this TableModelUpdateVO.
        :type business_asset: :class:`huaweicloudsdkdataartsstudio.v1.SyncStatusEnum`
        """
        self._business_asset = business_asset

    @property
    def meta_data_link(self):
        r"""Gets the meta_data_link of this TableModelUpdateVO.

        :return: The meta_data_link of this TableModelUpdateVO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.SyncStatusEnum`
        """
        return self._meta_data_link

    @meta_data_link.setter
    def meta_data_link(self, meta_data_link):
        r"""Sets the meta_data_link of this TableModelUpdateVO.

        :param meta_data_link: The meta_data_link of this TableModelUpdateVO.
        :type meta_data_link: :class:`huaweicloudsdkdataartsstudio.v1.SyncStatusEnum`
        """
        self._meta_data_link = meta_data_link

    @property
    def data_quality(self):
        r"""Gets the data_quality of this TableModelUpdateVO.

        :return: The data_quality of this TableModelUpdateVO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.SyncStatusEnum`
        """
        return self._data_quality

    @data_quality.setter
    def data_quality(self, data_quality):
        r"""Sets the data_quality of this TableModelUpdateVO.

        :param data_quality: The data_quality of this TableModelUpdateVO.
        :type data_quality: :class:`huaweicloudsdkdataartsstudio.v1.SyncStatusEnum`
        """
        self._data_quality = data_quality

    @property
    def summary_status(self):
        r"""Gets the summary_status of this TableModelUpdateVO.

        :return: The summary_status of this TableModelUpdateVO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.SyncStatusEnum`
        """
        return self._summary_status

    @summary_status.setter
    def summary_status(self, summary_status):
        r"""Sets the summary_status of this TableModelUpdateVO.

        :param summary_status: The summary_status of this TableModelUpdateVO.
        :type summary_status: :class:`huaweicloudsdkdataartsstudio.v1.SyncStatusEnum`
        """
        self._summary_status = summary_status

    @property
    def alias(self):
        r"""Gets the alias of this TableModelUpdateVO.

        别名。

        :return: The alias of this TableModelUpdateVO.
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        r"""Sets the alias of this TableModelUpdateVO.

        别名。

        :param alias: The alias of this TableModelUpdateVO.
        :type alias: str
        """
        self._alias = alias

    @property
    def self_defined_fields(self):
        r"""Gets the self_defined_fields of this TableModelUpdateVO.

        自定义项。

        :return: The self_defined_fields of this TableModelUpdateVO.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.SelfDefinedFieldVO`]
        """
        return self._self_defined_fields

    @self_defined_fields.setter
    def self_defined_fields(self, self_defined_fields):
        r"""Sets the self_defined_fields of this TableModelUpdateVO.

        自定义项。

        :param self_defined_fields: The self_defined_fields of this TableModelUpdateVO.
        :type self_defined_fields: list[:class:`huaweicloudsdkdataartsstudio.v1.SelfDefinedFieldVO`]
        """
        self._self_defined_fields = self_defined_fields

    @property
    def dev_version(self):
        r"""Gets the dev_version of this TableModelUpdateVO.

        开发环境版本，ID字符串。

        :return: The dev_version of this TableModelUpdateVO.
        :rtype: str
        """
        return self._dev_version

    @dev_version.setter
    def dev_version(self, dev_version):
        r"""Sets the dev_version of this TableModelUpdateVO.

        开发环境版本，ID字符串。

        :param dev_version: The dev_version of this TableModelUpdateVO.
        :type dev_version: str
        """
        self._dev_version = dev_version

    @property
    def prod_version(self):
        r"""Gets the prod_version of this TableModelUpdateVO.

        生产环境版本，ID字符串。

        :return: The prod_version of this TableModelUpdateVO.
        :rtype: str
        """
        return self._prod_version

    @prod_version.setter
    def prod_version(self, prod_version):
        r"""Sets the prod_version of this TableModelUpdateVO.

        生产环境版本，ID字符串。

        :param prod_version: The prod_version of this TableModelUpdateVO.
        :type prod_version: str
        """
        self._prod_version = prod_version

    @property
    def dev_version_name(self):
        r"""Gets the dev_version_name of this TableModelUpdateVO.

        开发环境版本名称

        :return: The dev_version_name of this TableModelUpdateVO.
        :rtype: str
        """
        return self._dev_version_name

    @dev_version_name.setter
    def dev_version_name(self, dev_version_name):
        r"""Sets the dev_version_name of this TableModelUpdateVO.

        开发环境版本名称

        :param dev_version_name: The dev_version_name of this TableModelUpdateVO.
        :type dev_version_name: str
        """
        self._dev_version_name = dev_version_name

    @property
    def prod_version_name(self):
        r"""Gets the prod_version_name of this TableModelUpdateVO.

        生产环境版本名称

        :return: The prod_version_name of this TableModelUpdateVO.
        :rtype: str
        """
        return self._prod_version_name

    @prod_version_name.setter
    def prod_version_name(self, prod_version_name):
        r"""Sets the prod_version_name of this TableModelUpdateVO.

        生产环境版本名称

        :param prod_version_name: The prod_version_name of this TableModelUpdateVO.
        :type prod_version_name: str
        """
        self._prod_version_name = prod_version_name

    @property
    def env_type(self):
        r"""Gets the env_type of this TableModelUpdateVO.

        :return: The env_type of this TableModelUpdateVO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.EnvTypeEnum`
        """
        return self._env_type

    @env_type.setter
    def env_type(self, env_type):
        r"""Sets the env_type of this TableModelUpdateVO.

        :param env_type: The env_type of this TableModelUpdateVO.
        :type env_type: :class:`huaweicloudsdkdataartsstudio.v1.EnvTypeEnum`
        """
        self._env_type = env_type

    @property
    def has_related_physical_table(self):
        r"""Gets the has_related_physical_table of this TableModelUpdateVO.

        是否关联了物理表

        :return: The has_related_physical_table of this TableModelUpdateVO.
        :rtype: bool
        """
        return self._has_related_physical_table

    @has_related_physical_table.setter
    def has_related_physical_table(self, has_related_physical_table):
        r"""Sets the has_related_physical_table of this TableModelUpdateVO.

        是否关联了物理表

        :param has_related_physical_table: The has_related_physical_table of this TableModelUpdateVO.
        :type has_related_physical_table: bool
        """
        self._has_related_physical_table = has_related_physical_table

    @property
    def has_related_logic_table(self):
        r"""Gets the has_related_logic_table of this TableModelUpdateVO.

        是否关联了逻辑实体

        :return: The has_related_logic_table of this TableModelUpdateVO.
        :rtype: bool
        """
        return self._has_related_logic_table

    @has_related_logic_table.setter
    def has_related_logic_table(self, has_related_logic_table):
        r"""Sets the has_related_logic_table of this TableModelUpdateVO.

        是否关联了逻辑实体

        :param has_related_logic_table: The has_related_logic_table of this TableModelUpdateVO.
        :type has_related_logic_table: bool
        """
        self._has_related_logic_table = has_related_logic_table

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
        if not isinstance(other, TableModelUpdateVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
