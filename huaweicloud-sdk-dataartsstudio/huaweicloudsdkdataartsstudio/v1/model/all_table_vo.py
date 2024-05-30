# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AllTableVO:

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
        'name': 'str',
        'tb_logic_guid': 'str',
        'quality_id': 'str',
        'reversed': 'bool',
        'partition_conf': 'str',
        'dirty_out_switch': 'bool',
        'dirty_out_database': 'str',
        'dirty_out_prefix': 'str',
        'dirty_out_suffix': 'str',
        'tb_guid': 'str',
        'code': 'str',
        'create_by': 'str',
        'tenant_id': 'str',
        'description': 'str',
        'status': 'BizStatusEnum',
        'biz_type': 'BizTypeEnum',
        'create_time': 'datetime',
        'update_time': 'datetime',
        'db_name': 'str',
        'dw_type': 'str',
        'queue_name': 'str',
        'schema': 'str',
        'l1': 'str',
        'l2': 'str',
        'l3': 'str',
        'l1_id': 'str',
        'l2_id': 'str',
        'l3_id': 'str',
        'new_biz': 'BizVersionManageVO',
        'physical_table': 'SyncStatusEnum',
        'dev_physical_table': 'SyncStatusEnum',
        'technical_asset': 'SyncStatusEnum',
        'business_asset': 'SyncStatusEnum',
        'meta_data_link': 'SyncStatusEnum',
        'data_quality': 'SyncStatusEnum',
        'dlf_task': 'SyncStatusEnum',
        'materialization': 'SyncStatusEnum',
        'publish_to_dlm': 'SyncStatusEnum',
        'summary_status': 'SyncStatusEnum',
        'standard_count': 'str',
        'alias': 'str',
        'api_id': 'str',
        'workspace_id': 'str',
        'workspace_name': 'str',
        'dev_version': 'str',
        'prod_version': 'str',
        'dev_version_name': 'str',
        'prod_version_name': 'str',
        'env_type': 'EnvTypeEnum'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'tb_logic_guid': 'tb_logic_guid',
        'quality_id': 'quality_id',
        'reversed': 'reversed',
        'partition_conf': 'partition_conf',
        'dirty_out_switch': 'dirty_out_switch',
        'dirty_out_database': 'dirty_out_database',
        'dirty_out_prefix': 'dirty_out_prefix',
        'dirty_out_suffix': 'dirty_out_suffix',
        'tb_guid': 'tb_guid',
        'code': 'code',
        'create_by': 'create_by',
        'tenant_id': 'tenant_id',
        'description': 'description',
        'status': 'status',
        'biz_type': 'biz_type',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'db_name': 'db_name',
        'dw_type': 'dw_type',
        'queue_name': 'queue_name',
        'schema': 'schema',
        'l1': 'l1',
        'l2': 'l2',
        'l3': 'l3',
        'l1_id': 'l1_id',
        'l2_id': 'l2_id',
        'l3_id': 'l3_id',
        'new_biz': 'new_biz',
        'physical_table': 'physical_table',
        'dev_physical_table': 'dev_physical_table',
        'technical_asset': 'technical_asset',
        'business_asset': 'business_asset',
        'meta_data_link': 'meta_data_link',
        'data_quality': 'data_quality',
        'dlf_task': 'dlf_task',
        'materialization': 'materialization',
        'publish_to_dlm': 'publish_to_dlm',
        'summary_status': 'summary_status',
        'standard_count': 'standard_count',
        'alias': 'alias',
        'api_id': 'api_id',
        'workspace_id': 'workspace_id',
        'workspace_name': 'workspace_name',
        'dev_version': 'dev_version',
        'prod_version': 'prod_version',
        'dev_version_name': 'dev_version_name',
        'prod_version_name': 'prod_version_name',
        'env_type': 'env_type'
    }

    def __init__(self, id=None, name=None, tb_logic_guid=None, quality_id=None, reversed=None, partition_conf=None, dirty_out_switch=None, dirty_out_database=None, dirty_out_prefix=None, dirty_out_suffix=None, tb_guid=None, code=None, create_by=None, tenant_id=None, description=None, status=None, biz_type=None, create_time=None, update_time=None, db_name=None, dw_type=None, queue_name=None, schema=None, l1=None, l2=None, l3=None, l1_id=None, l2_id=None, l3_id=None, new_biz=None, physical_table=None, dev_physical_table=None, technical_asset=None, business_asset=None, meta_data_link=None, data_quality=None, dlf_task=None, materialization=None, publish_to_dlm=None, summary_status=None, standard_count=None, alias=None, api_id=None, workspace_id=None, workspace_name=None, dev_version=None, prod_version=None, dev_version_name=None, prod_version_name=None, env_type=None):
        """AllTableVO

        The model defined in huaweicloud sdk

        :param id: l1的ID，填写String类型替代Long类型。
        :type id: str
        :param name: l1名称。
        :type name: str
        :param tb_logic_guid: 表发布后对应的逻辑实体guid。
        :type tb_logic_guid: str
        :param quality_id: 质量ID。
        :type quality_id: str
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
        :param tb_guid: 表发布后对应的物理表guid。
        :type tb_guid: str
        :param code: 编码。
        :type code: str
        :param create_by: 创建人。
        :type create_by: str
        :param tenant_id: 租户ID。
        :type tenant_id: str
        :param description: 描述。
        :type description: str
        :param status: 
        :type status: :class:`huaweicloudsdkdataartsstudio.v1.BizStatusEnum`
        :param biz_type: 
        :type biz_type: :class:`huaweicloudsdkdataartsstudio.v1.BizTypeEnum`
        :param create_time: 创建时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。
        :type create_time: datetime
        :param update_time: 更新时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。
        :type update_time: datetime
        :param db_name: 数据库名。
        :type db_name: str
        :param dw_type: 数据连接类型，对应表所在的数仓类型，取值可以为DLI、DWS、MRS_HIVE、POSTGRESQL、MRS_SPARK、CLICKHOUSE、MYSQL、ORACLE和DORIS等。
        :type dw_type: str
        :param queue_name: dli数据连接执行sql所需的队列，数据连接类型为DLI时必须。
        :type queue_name: str
        :param schema: DWS类型需要。
        :type schema: str
        :param l1: 主题域分组中文名，只读，创建和更新时无需填写。
        :type l1: str
        :param l2: 主题域中文名，只读，创建和更新时无需填写。
        :type l2: str
        :param l3: 业务对象中文名，只读，创建和更新时无需填写。
        :type l3: str
        :param l1_id: 主题域分组ID，只读，填写String类型替代Long类型。
        :type l1_id: str
        :param l2_id: 主题域ID，只读，创建和更新时无需填写。
        :type l2_id: str
        :param l3_id: 业务对象ID，只读，填写String类型替代Long类型。
        :type l3_id: str
        :param new_biz: 
        :type new_biz: :class:`huaweicloudsdkdataartsstudio.v1.BizVersionManageVO`
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
        :param materialization: 
        :type materialization: :class:`huaweicloudsdkdataartsstudio.v1.SyncStatusEnum`
        :param publish_to_dlm: 
        :type publish_to_dlm: :class:`huaweicloudsdkdataartsstudio.v1.SyncStatusEnum`
        :param summary_status: 
        :type summary_status: :class:`huaweicloudsdkdataartsstudio.v1.SyncStatusEnum`
        :param standard_count: 标准数量，只读，填写String类型替代Long类型。
        :type standard_count: str
        :param alias: 别名。
        :type alias: str
        :param api_id: 汇总表API ID。
        :type api_id: str
        :param workspace_id: 工作空间ID。
        :type workspace_id: str
        :param workspace_name: 工作空间名称。
        :type workspace_name: str
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
        """
        
        

        self._id = None
        self._name = None
        self._tb_logic_guid = None
        self._quality_id = None
        self._reversed = None
        self._partition_conf = None
        self._dirty_out_switch = None
        self._dirty_out_database = None
        self._dirty_out_prefix = None
        self._dirty_out_suffix = None
        self._tb_guid = None
        self._code = None
        self._create_by = None
        self._tenant_id = None
        self._description = None
        self._status = None
        self._biz_type = None
        self._create_time = None
        self._update_time = None
        self._db_name = None
        self._dw_type = None
        self._queue_name = None
        self._schema = None
        self._l1 = None
        self._l2 = None
        self._l3 = None
        self._l1_id = None
        self._l2_id = None
        self._l3_id = None
        self._new_biz = None
        self._physical_table = None
        self._dev_physical_table = None
        self._technical_asset = None
        self._business_asset = None
        self._meta_data_link = None
        self._data_quality = None
        self._dlf_task = None
        self._materialization = None
        self._publish_to_dlm = None
        self._summary_status = None
        self._standard_count = None
        self._alias = None
        self._api_id = None
        self._workspace_id = None
        self._workspace_name = None
        self._dev_version = None
        self._prod_version = None
        self._dev_version_name = None
        self._prod_version_name = None
        self._env_type = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if tb_logic_guid is not None:
            self.tb_logic_guid = tb_logic_guid
        if quality_id is not None:
            self.quality_id = quality_id
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
        if tb_guid is not None:
            self.tb_guid = tb_guid
        if code is not None:
            self.code = code
        if create_by is not None:
            self.create_by = create_by
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if description is not None:
            self.description = description
        if status is not None:
            self.status = status
        if biz_type is not None:
            self.biz_type = biz_type
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if db_name is not None:
            self.db_name = db_name
        if dw_type is not None:
            self.dw_type = dw_type
        if queue_name is not None:
            self.queue_name = queue_name
        if schema is not None:
            self.schema = schema
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
        if new_biz is not None:
            self.new_biz = new_biz
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
        if summary_status is not None:
            self.summary_status = summary_status
        if standard_count is not None:
            self.standard_count = standard_count
        if alias is not None:
            self.alias = alias
        if api_id is not None:
            self.api_id = api_id
        if workspace_id is not None:
            self.workspace_id = workspace_id
        if workspace_name is not None:
            self.workspace_name = workspace_name
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

    @property
    def id(self):
        """Gets the id of this AllTableVO.

        l1的ID，填写String类型替代Long类型。

        :return: The id of this AllTableVO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AllTableVO.

        l1的ID，填写String类型替代Long类型。

        :param id: The id of this AllTableVO.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this AllTableVO.

        l1名称。

        :return: The name of this AllTableVO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AllTableVO.

        l1名称。

        :param name: The name of this AllTableVO.
        :type name: str
        """
        self._name = name

    @property
    def tb_logic_guid(self):
        """Gets the tb_logic_guid of this AllTableVO.

        表发布后对应的逻辑实体guid。

        :return: The tb_logic_guid of this AllTableVO.
        :rtype: str
        """
        return self._tb_logic_guid

    @tb_logic_guid.setter
    def tb_logic_guid(self, tb_logic_guid):
        """Sets the tb_logic_guid of this AllTableVO.

        表发布后对应的逻辑实体guid。

        :param tb_logic_guid: The tb_logic_guid of this AllTableVO.
        :type tb_logic_guid: str
        """
        self._tb_logic_guid = tb_logic_guid

    @property
    def quality_id(self):
        """Gets the quality_id of this AllTableVO.

        质量ID。

        :return: The quality_id of this AllTableVO.
        :rtype: str
        """
        return self._quality_id

    @quality_id.setter
    def quality_id(self, quality_id):
        """Sets the quality_id of this AllTableVO.

        质量ID。

        :param quality_id: The quality_id of this AllTableVO.
        :type quality_id: str
        """
        self._quality_id = quality_id

    @property
    def reversed(self):
        """Gets the reversed of this AllTableVO.

        是否是逆向的。

        :return: The reversed of this AllTableVO.
        :rtype: bool
        """
        return self._reversed

    @reversed.setter
    def reversed(self, reversed):
        """Sets the reversed of this AllTableVO.

        是否是逆向的。

        :param reversed: The reversed of this AllTableVO.
        :type reversed: bool
        """
        self._reversed = reversed

    @property
    def partition_conf(self):
        """Gets the partition_conf of this AllTableVO.

        分区表达式。

        :return: The partition_conf of this AllTableVO.
        :rtype: str
        """
        return self._partition_conf

    @partition_conf.setter
    def partition_conf(self, partition_conf):
        """Sets the partition_conf of this AllTableVO.

        分区表达式。

        :param partition_conf: The partition_conf of this AllTableVO.
        :type partition_conf: str
        """
        self._partition_conf = partition_conf

    @property
    def dirty_out_switch(self):
        """Gets the dirty_out_switch of this AllTableVO.

        异常数据输出开关。

        :return: The dirty_out_switch of this AllTableVO.
        :rtype: bool
        """
        return self._dirty_out_switch

    @dirty_out_switch.setter
    def dirty_out_switch(self, dirty_out_switch):
        """Sets the dirty_out_switch of this AllTableVO.

        异常数据输出开关。

        :param dirty_out_switch: The dirty_out_switch of this AllTableVO.
        :type dirty_out_switch: bool
        """
        self._dirty_out_switch = dirty_out_switch

    @property
    def dirty_out_database(self):
        """Gets the dirty_out_database of this AllTableVO.

        异常数据输出库。

        :return: The dirty_out_database of this AllTableVO.
        :rtype: str
        """
        return self._dirty_out_database

    @dirty_out_database.setter
    def dirty_out_database(self, dirty_out_database):
        """Sets the dirty_out_database of this AllTableVO.

        异常数据输出库。

        :param dirty_out_database: The dirty_out_database of this AllTableVO.
        :type dirty_out_database: str
        """
        self._dirty_out_database = dirty_out_database

    @property
    def dirty_out_prefix(self):
        """Gets the dirty_out_prefix of this AllTableVO.

        异常表前缀。

        :return: The dirty_out_prefix of this AllTableVO.
        :rtype: str
        """
        return self._dirty_out_prefix

    @dirty_out_prefix.setter
    def dirty_out_prefix(self, dirty_out_prefix):
        """Sets the dirty_out_prefix of this AllTableVO.

        异常表前缀。

        :param dirty_out_prefix: The dirty_out_prefix of this AllTableVO.
        :type dirty_out_prefix: str
        """
        self._dirty_out_prefix = dirty_out_prefix

    @property
    def dirty_out_suffix(self):
        """Gets the dirty_out_suffix of this AllTableVO.

        异常表后缀。

        :return: The dirty_out_suffix of this AllTableVO.
        :rtype: str
        """
        return self._dirty_out_suffix

    @dirty_out_suffix.setter
    def dirty_out_suffix(self, dirty_out_suffix):
        """Sets the dirty_out_suffix of this AllTableVO.

        异常表后缀。

        :param dirty_out_suffix: The dirty_out_suffix of this AllTableVO.
        :type dirty_out_suffix: str
        """
        self._dirty_out_suffix = dirty_out_suffix

    @property
    def tb_guid(self):
        """Gets the tb_guid of this AllTableVO.

        表发布后对应的物理表guid。

        :return: The tb_guid of this AllTableVO.
        :rtype: str
        """
        return self._tb_guid

    @tb_guid.setter
    def tb_guid(self, tb_guid):
        """Sets the tb_guid of this AllTableVO.

        表发布后对应的物理表guid。

        :param tb_guid: The tb_guid of this AllTableVO.
        :type tb_guid: str
        """
        self._tb_guid = tb_guid

    @property
    def code(self):
        """Gets the code of this AllTableVO.

        编码。

        :return: The code of this AllTableVO.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this AllTableVO.

        编码。

        :param code: The code of this AllTableVO.
        :type code: str
        """
        self._code = code

    @property
    def create_by(self):
        """Gets the create_by of this AllTableVO.

        创建人。

        :return: The create_by of this AllTableVO.
        :rtype: str
        """
        return self._create_by

    @create_by.setter
    def create_by(self, create_by):
        """Sets the create_by of this AllTableVO.

        创建人。

        :param create_by: The create_by of this AllTableVO.
        :type create_by: str
        """
        self._create_by = create_by

    @property
    def tenant_id(self):
        """Gets the tenant_id of this AllTableVO.

        租户ID。

        :return: The tenant_id of this AllTableVO.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this AllTableVO.

        租户ID。

        :param tenant_id: The tenant_id of this AllTableVO.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def description(self):
        """Gets the description of this AllTableVO.

        描述。

        :return: The description of this AllTableVO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AllTableVO.

        描述。

        :param description: The description of this AllTableVO.
        :type description: str
        """
        self._description = description

    @property
    def status(self):
        """Gets the status of this AllTableVO.

        :return: The status of this AllTableVO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.BizStatusEnum`
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this AllTableVO.

        :param status: The status of this AllTableVO.
        :type status: :class:`huaweicloudsdkdataartsstudio.v1.BizStatusEnum`
        """
        self._status = status

    @property
    def biz_type(self):
        """Gets the biz_type of this AllTableVO.

        :return: The biz_type of this AllTableVO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.BizTypeEnum`
        """
        return self._biz_type

    @biz_type.setter
    def biz_type(self, biz_type):
        """Sets the biz_type of this AllTableVO.

        :param biz_type: The biz_type of this AllTableVO.
        :type biz_type: :class:`huaweicloudsdkdataartsstudio.v1.BizTypeEnum`
        """
        self._biz_type = biz_type

    @property
    def create_time(self):
        """Gets the create_time of this AllTableVO.

        创建时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。

        :return: The create_time of this AllTableVO.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this AllTableVO.

        创建时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。

        :param create_time: The create_time of this AllTableVO.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this AllTableVO.

        更新时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。

        :return: The update_time of this AllTableVO.
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this AllTableVO.

        更新时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。

        :param update_time: The update_time of this AllTableVO.
        :type update_time: datetime
        """
        self._update_time = update_time

    @property
    def db_name(self):
        """Gets the db_name of this AllTableVO.

        数据库名。

        :return: The db_name of this AllTableVO.
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        """Sets the db_name of this AllTableVO.

        数据库名。

        :param db_name: The db_name of this AllTableVO.
        :type db_name: str
        """
        self._db_name = db_name

    @property
    def dw_type(self):
        """Gets the dw_type of this AllTableVO.

        数据连接类型，对应表所在的数仓类型，取值可以为DLI、DWS、MRS_HIVE、POSTGRESQL、MRS_SPARK、CLICKHOUSE、MYSQL、ORACLE和DORIS等。

        :return: The dw_type of this AllTableVO.
        :rtype: str
        """
        return self._dw_type

    @dw_type.setter
    def dw_type(self, dw_type):
        """Sets the dw_type of this AllTableVO.

        数据连接类型，对应表所在的数仓类型，取值可以为DLI、DWS、MRS_HIVE、POSTGRESQL、MRS_SPARK、CLICKHOUSE、MYSQL、ORACLE和DORIS等。

        :param dw_type: The dw_type of this AllTableVO.
        :type dw_type: str
        """
        self._dw_type = dw_type

    @property
    def queue_name(self):
        """Gets the queue_name of this AllTableVO.

        dli数据连接执行sql所需的队列，数据连接类型为DLI时必须。

        :return: The queue_name of this AllTableVO.
        :rtype: str
        """
        return self._queue_name

    @queue_name.setter
    def queue_name(self, queue_name):
        """Sets the queue_name of this AllTableVO.

        dli数据连接执行sql所需的队列，数据连接类型为DLI时必须。

        :param queue_name: The queue_name of this AllTableVO.
        :type queue_name: str
        """
        self._queue_name = queue_name

    @property
    def schema(self):
        """Gets the schema of this AllTableVO.

        DWS类型需要。

        :return: The schema of this AllTableVO.
        :rtype: str
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        """Sets the schema of this AllTableVO.

        DWS类型需要。

        :param schema: The schema of this AllTableVO.
        :type schema: str
        """
        self._schema = schema

    @property
    def l1(self):
        """Gets the l1 of this AllTableVO.

        主题域分组中文名，只读，创建和更新时无需填写。

        :return: The l1 of this AllTableVO.
        :rtype: str
        """
        return self._l1

    @l1.setter
    def l1(self, l1):
        """Sets the l1 of this AllTableVO.

        主题域分组中文名，只读，创建和更新时无需填写。

        :param l1: The l1 of this AllTableVO.
        :type l1: str
        """
        self._l1 = l1

    @property
    def l2(self):
        """Gets the l2 of this AllTableVO.

        主题域中文名，只读，创建和更新时无需填写。

        :return: The l2 of this AllTableVO.
        :rtype: str
        """
        return self._l2

    @l2.setter
    def l2(self, l2):
        """Sets the l2 of this AllTableVO.

        主题域中文名，只读，创建和更新时无需填写。

        :param l2: The l2 of this AllTableVO.
        :type l2: str
        """
        self._l2 = l2

    @property
    def l3(self):
        """Gets the l3 of this AllTableVO.

        业务对象中文名，只读，创建和更新时无需填写。

        :return: The l3 of this AllTableVO.
        :rtype: str
        """
        return self._l3

    @l3.setter
    def l3(self, l3):
        """Sets the l3 of this AllTableVO.

        业务对象中文名，只读，创建和更新时无需填写。

        :param l3: The l3 of this AllTableVO.
        :type l3: str
        """
        self._l3 = l3

    @property
    def l1_id(self):
        """Gets the l1_id of this AllTableVO.

        主题域分组ID，只读，填写String类型替代Long类型。

        :return: The l1_id of this AllTableVO.
        :rtype: str
        """
        return self._l1_id

    @l1_id.setter
    def l1_id(self, l1_id):
        """Sets the l1_id of this AllTableVO.

        主题域分组ID，只读，填写String类型替代Long类型。

        :param l1_id: The l1_id of this AllTableVO.
        :type l1_id: str
        """
        self._l1_id = l1_id

    @property
    def l2_id(self):
        """Gets the l2_id of this AllTableVO.

        主题域ID，只读，创建和更新时无需填写。

        :return: The l2_id of this AllTableVO.
        :rtype: str
        """
        return self._l2_id

    @l2_id.setter
    def l2_id(self, l2_id):
        """Sets the l2_id of this AllTableVO.

        主题域ID，只读，创建和更新时无需填写。

        :param l2_id: The l2_id of this AllTableVO.
        :type l2_id: str
        """
        self._l2_id = l2_id

    @property
    def l3_id(self):
        """Gets the l3_id of this AllTableVO.

        业务对象ID，只读，填写String类型替代Long类型。

        :return: The l3_id of this AllTableVO.
        :rtype: str
        """
        return self._l3_id

    @l3_id.setter
    def l3_id(self, l3_id):
        """Sets the l3_id of this AllTableVO.

        业务对象ID，只读，填写String类型替代Long类型。

        :param l3_id: The l3_id of this AllTableVO.
        :type l3_id: str
        """
        self._l3_id = l3_id

    @property
    def new_biz(self):
        """Gets the new_biz of this AllTableVO.

        :return: The new_biz of this AllTableVO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.BizVersionManageVO`
        """
        return self._new_biz

    @new_biz.setter
    def new_biz(self, new_biz):
        """Sets the new_biz of this AllTableVO.

        :param new_biz: The new_biz of this AllTableVO.
        :type new_biz: :class:`huaweicloudsdkdataartsstudio.v1.BizVersionManageVO`
        """
        self._new_biz = new_biz

    @property
    def physical_table(self):
        """Gets the physical_table of this AllTableVO.

        :return: The physical_table of this AllTableVO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.SyncStatusEnum`
        """
        return self._physical_table

    @physical_table.setter
    def physical_table(self, physical_table):
        """Sets the physical_table of this AllTableVO.

        :param physical_table: The physical_table of this AllTableVO.
        :type physical_table: :class:`huaweicloudsdkdataartsstudio.v1.SyncStatusEnum`
        """
        self._physical_table = physical_table

    @property
    def dev_physical_table(self):
        """Gets the dev_physical_table of this AllTableVO.

        :return: The dev_physical_table of this AllTableVO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.SyncStatusEnum`
        """
        return self._dev_physical_table

    @dev_physical_table.setter
    def dev_physical_table(self, dev_physical_table):
        """Sets the dev_physical_table of this AllTableVO.

        :param dev_physical_table: The dev_physical_table of this AllTableVO.
        :type dev_physical_table: :class:`huaweicloudsdkdataartsstudio.v1.SyncStatusEnum`
        """
        self._dev_physical_table = dev_physical_table

    @property
    def technical_asset(self):
        """Gets the technical_asset of this AllTableVO.

        :return: The technical_asset of this AllTableVO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.SyncStatusEnum`
        """
        return self._technical_asset

    @technical_asset.setter
    def technical_asset(self, technical_asset):
        """Sets the technical_asset of this AllTableVO.

        :param technical_asset: The technical_asset of this AllTableVO.
        :type technical_asset: :class:`huaweicloudsdkdataartsstudio.v1.SyncStatusEnum`
        """
        self._technical_asset = technical_asset

    @property
    def business_asset(self):
        """Gets the business_asset of this AllTableVO.

        :return: The business_asset of this AllTableVO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.SyncStatusEnum`
        """
        return self._business_asset

    @business_asset.setter
    def business_asset(self, business_asset):
        """Sets the business_asset of this AllTableVO.

        :param business_asset: The business_asset of this AllTableVO.
        :type business_asset: :class:`huaweicloudsdkdataartsstudio.v1.SyncStatusEnum`
        """
        self._business_asset = business_asset

    @property
    def meta_data_link(self):
        """Gets the meta_data_link of this AllTableVO.

        :return: The meta_data_link of this AllTableVO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.SyncStatusEnum`
        """
        return self._meta_data_link

    @meta_data_link.setter
    def meta_data_link(self, meta_data_link):
        """Sets the meta_data_link of this AllTableVO.

        :param meta_data_link: The meta_data_link of this AllTableVO.
        :type meta_data_link: :class:`huaweicloudsdkdataartsstudio.v1.SyncStatusEnum`
        """
        self._meta_data_link = meta_data_link

    @property
    def data_quality(self):
        """Gets the data_quality of this AllTableVO.

        :return: The data_quality of this AllTableVO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.SyncStatusEnum`
        """
        return self._data_quality

    @data_quality.setter
    def data_quality(self, data_quality):
        """Sets the data_quality of this AllTableVO.

        :param data_quality: The data_quality of this AllTableVO.
        :type data_quality: :class:`huaweicloudsdkdataartsstudio.v1.SyncStatusEnum`
        """
        self._data_quality = data_quality

    @property
    def dlf_task(self):
        """Gets the dlf_task of this AllTableVO.

        :return: The dlf_task of this AllTableVO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.SyncStatusEnum`
        """
        return self._dlf_task

    @dlf_task.setter
    def dlf_task(self, dlf_task):
        """Sets the dlf_task of this AllTableVO.

        :param dlf_task: The dlf_task of this AllTableVO.
        :type dlf_task: :class:`huaweicloudsdkdataartsstudio.v1.SyncStatusEnum`
        """
        self._dlf_task = dlf_task

    @property
    def materialization(self):
        """Gets the materialization of this AllTableVO.

        :return: The materialization of this AllTableVO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.SyncStatusEnum`
        """
        return self._materialization

    @materialization.setter
    def materialization(self, materialization):
        """Sets the materialization of this AllTableVO.

        :param materialization: The materialization of this AllTableVO.
        :type materialization: :class:`huaweicloudsdkdataartsstudio.v1.SyncStatusEnum`
        """
        self._materialization = materialization

    @property
    def publish_to_dlm(self):
        """Gets the publish_to_dlm of this AllTableVO.

        :return: The publish_to_dlm of this AllTableVO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.SyncStatusEnum`
        """
        return self._publish_to_dlm

    @publish_to_dlm.setter
    def publish_to_dlm(self, publish_to_dlm):
        """Sets the publish_to_dlm of this AllTableVO.

        :param publish_to_dlm: The publish_to_dlm of this AllTableVO.
        :type publish_to_dlm: :class:`huaweicloudsdkdataartsstudio.v1.SyncStatusEnum`
        """
        self._publish_to_dlm = publish_to_dlm

    @property
    def summary_status(self):
        """Gets the summary_status of this AllTableVO.

        :return: The summary_status of this AllTableVO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.SyncStatusEnum`
        """
        return self._summary_status

    @summary_status.setter
    def summary_status(self, summary_status):
        """Sets the summary_status of this AllTableVO.

        :param summary_status: The summary_status of this AllTableVO.
        :type summary_status: :class:`huaweicloudsdkdataartsstudio.v1.SyncStatusEnum`
        """
        self._summary_status = summary_status

    @property
    def standard_count(self):
        """Gets the standard_count of this AllTableVO.

        标准数量，只读，填写String类型替代Long类型。

        :return: The standard_count of this AllTableVO.
        :rtype: str
        """
        return self._standard_count

    @standard_count.setter
    def standard_count(self, standard_count):
        """Sets the standard_count of this AllTableVO.

        标准数量，只读，填写String类型替代Long类型。

        :param standard_count: The standard_count of this AllTableVO.
        :type standard_count: str
        """
        self._standard_count = standard_count

    @property
    def alias(self):
        """Gets the alias of this AllTableVO.

        别名。

        :return: The alias of this AllTableVO.
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """Sets the alias of this AllTableVO.

        别名。

        :param alias: The alias of this AllTableVO.
        :type alias: str
        """
        self._alias = alias

    @property
    def api_id(self):
        """Gets the api_id of this AllTableVO.

        汇总表API ID。

        :return: The api_id of this AllTableVO.
        :rtype: str
        """
        return self._api_id

    @api_id.setter
    def api_id(self, api_id):
        """Sets the api_id of this AllTableVO.

        汇总表API ID。

        :param api_id: The api_id of this AllTableVO.
        :type api_id: str
        """
        self._api_id = api_id

    @property
    def workspace_id(self):
        """Gets the workspace_id of this AllTableVO.

        工作空间ID。

        :return: The workspace_id of this AllTableVO.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        """Sets the workspace_id of this AllTableVO.

        工作空间ID。

        :param workspace_id: The workspace_id of this AllTableVO.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def workspace_name(self):
        """Gets the workspace_name of this AllTableVO.

        工作空间名称。

        :return: The workspace_name of this AllTableVO.
        :rtype: str
        """
        return self._workspace_name

    @workspace_name.setter
    def workspace_name(self, workspace_name):
        """Sets the workspace_name of this AllTableVO.

        工作空间名称。

        :param workspace_name: The workspace_name of this AllTableVO.
        :type workspace_name: str
        """
        self._workspace_name = workspace_name

    @property
    def dev_version(self):
        """Gets the dev_version of this AllTableVO.

        开发环境版本，填写String类型替代Long类型。

        :return: The dev_version of this AllTableVO.
        :rtype: str
        """
        return self._dev_version

    @dev_version.setter
    def dev_version(self, dev_version):
        """Sets the dev_version of this AllTableVO.

        开发环境版本，填写String类型替代Long类型。

        :param dev_version: The dev_version of this AllTableVO.
        :type dev_version: str
        """
        self._dev_version = dev_version

    @property
    def prod_version(self):
        """Gets the prod_version of this AllTableVO.

        生产环境版本，填写String类型替代Long类型。

        :return: The prod_version of this AllTableVO.
        :rtype: str
        """
        return self._prod_version

    @prod_version.setter
    def prod_version(self, prod_version):
        """Sets the prod_version of this AllTableVO.

        生产环境版本，填写String类型替代Long类型。

        :param prod_version: The prod_version of this AllTableVO.
        :type prod_version: str
        """
        self._prod_version = prod_version

    @property
    def dev_version_name(self):
        """Gets the dev_version_name of this AllTableVO.

        开发环境版本名称

        :return: The dev_version_name of this AllTableVO.
        :rtype: str
        """
        return self._dev_version_name

    @dev_version_name.setter
    def dev_version_name(self, dev_version_name):
        """Sets the dev_version_name of this AllTableVO.

        开发环境版本名称

        :param dev_version_name: The dev_version_name of this AllTableVO.
        :type dev_version_name: str
        """
        self._dev_version_name = dev_version_name

    @property
    def prod_version_name(self):
        """Gets the prod_version_name of this AllTableVO.

        生产环境版本名称

        :return: The prod_version_name of this AllTableVO.
        :rtype: str
        """
        return self._prod_version_name

    @prod_version_name.setter
    def prod_version_name(self, prod_version_name):
        """Sets the prod_version_name of this AllTableVO.

        生产环境版本名称

        :param prod_version_name: The prod_version_name of this AllTableVO.
        :type prod_version_name: str
        """
        self._prod_version_name = prod_version_name

    @property
    def env_type(self):
        """Gets the env_type of this AllTableVO.

        :return: The env_type of this AllTableVO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.EnvTypeEnum`
        """
        return self._env_type

    @env_type.setter
    def env_type(self, env_type):
        """Sets the env_type of this AllTableVO.

        :param env_type: The env_type of this AllTableVO.
        :type env_type: :class:`huaweicloudsdkdataartsstudio.v1.EnvTypeEnum`
        """
        self._env_type = env_type

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
        if not isinstance(other, AllTableVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
