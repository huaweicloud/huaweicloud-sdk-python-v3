# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DimensionVO:

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
        'dimension_type': 'str',
        'name_ch': 'str',
        'description': 'str',
        'create_by': 'str',
        'update_by': 'str',
        'code_table_id': 'str',
        'code_table': 'CodeTableVO',
        'l1_id': 'str',
        'l2_id': 'str',
        'l3_id': 'str',
        'hierarchies': 'list[DimensionHierarchiesVO]',
        'status': 'BizStatusEnum',
        'create_time': 'datetime',
        'update_time': 'datetime',
        'approval_info': 'ApprovalVO',
        'new_biz': 'BizVersionManageVO',
        'l1': 'str',
        'l2': 'str',
        'l3': 'str',
        'attributes': 'list[DimensionAttributeVO]',
        'mappings': 'list[TableMappingVO]',
        'datasource': 'BizDatasourceRelationVO',
        'owner': 'str',
        'obs_location': 'str',
        'table_type': 'str',
        'distribute': 'str',
        'distribute_column': 'str',
        'alias': 'str',
        'self_defined_fields': 'list[SelfDefinedFieldVO]',
        'configs': 'str',
        'dev_version': 'str',
        'prod_version': 'str',
        'dev_version_name': 'str',
        'prod_version_name': 'str',
        'env_type': 'EnvTypeEnum'
    }

    attribute_map = {
        'id': 'id',
        'name_en': 'name_en',
        'dimension_type': 'dimension_type',
        'name_ch': 'name_ch',
        'description': 'description',
        'create_by': 'create_by',
        'update_by': 'update_by',
        'code_table_id': 'code_table_id',
        'code_table': 'code_table',
        'l1_id': 'l1_id',
        'l2_id': 'l2_id',
        'l3_id': 'l3_id',
        'hierarchies': 'hierarchies',
        'status': 'status',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'approval_info': 'approval_info',
        'new_biz': 'new_biz',
        'l1': 'l1',
        'l2': 'l2',
        'l3': 'l3',
        'attributes': 'attributes',
        'mappings': 'mappings',
        'datasource': 'datasource',
        'owner': 'owner',
        'obs_location': 'obs_location',
        'table_type': 'table_type',
        'distribute': 'distribute',
        'distribute_column': 'distribute_column',
        'alias': 'alias',
        'self_defined_fields': 'self_defined_fields',
        'configs': 'configs',
        'dev_version': 'dev_version',
        'prod_version': 'prod_version',
        'dev_version_name': 'dev_version_name',
        'prod_version_name': 'prod_version_name',
        'env_type': 'env_type'
    }

    def __init__(self, id=None, name_en=None, dimension_type=None, name_ch=None, description=None, create_by=None, update_by=None, code_table_id=None, code_table=None, l1_id=None, l2_id=None, l3_id=None, hierarchies=None, status=None, create_time=None, update_time=None, approval_info=None, new_biz=None, l1=None, l2=None, l3=None, attributes=None, mappings=None, datasource=None, owner=None, obs_location=None, table_type=None, distribute=None, distribute_column=None, alias=None, self_defined_fields=None, configs=None, dev_version=None, prod_version=None, dev_version_name=None, prod_version_name=None, env_type=None):
        """DimensionVO

        The model defined in huaweicloud sdk

        :param id: 编码，填写String类型替代Long类型。
        :type id: str
        :param name_en: 字段名。
        :type name_en: str
        :param dimension_type: 维度类型。 枚举值：   - COMMON: 普通维度   - LOOKUP: 码表维度   - HIERARCHIES: 层级维度 
        :type dimension_type: str
        :param name_ch: 业务属性。
        :type name_ch: str
        :param description: 描述。
        :type description: str
        :param create_by: 创建人。
        :type create_by: str
        :param update_by: 更新人。
        :type update_by: str
        :param code_table_id: 引用码表ID，填写String类型替代Long类型。
        :type code_table_id: str
        :param code_table: 
        :type code_table: :class:`huaweicloudsdkdataartsstudio.v1.CodeTableVO`
        :param l1_id: 主题域分组ID，只读，填写String类型替代Long类型。
        :type l1_id: str
        :param l2_id: 主题域ID，只读，创建和更新时无需填写。
        :type l2_id: str
        :param l3_id: 业务对象ID，填写String类型替代Long类型。
        :type l3_id: str
        :param hierarchies: 层级属性。
        :type hierarchies: list[:class:`huaweicloudsdkdataartsstudio.v1.DimensionHierarchiesVO`]
        :param status: 
        :type status: :class:`huaweicloudsdkdataartsstudio.v1.BizStatusEnum`
        :param create_time: 创建时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。
        :type create_time: datetime
        :param update_time: 更新时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。
        :type update_time: datetime
        :param approval_info: 
        :type approval_info: :class:`huaweicloudsdkdataartsstudio.v1.ApprovalVO`
        :param new_biz: 
        :type new_biz: :class:`huaweicloudsdkdataartsstudio.v1.BizVersionManageVO`
        :param l1: 主题域分组中文名，只读，创建和更新时无需填写。
        :type l1: str
        :param l2: 主题域中文名，只读，创建和更新时无需填写。
        :type l2: str
        :param l3: 业务对象中文名，只读，创建和更新时无需填写。
        :type l3: str
        :param attributes: 维度属性信息。
        :type attributes: list[:class:`huaweicloudsdkdataartsstudio.v1.DimensionAttributeVO`]
        :param mappings: 表映射信息。
        :type mappings: list[:class:`huaweicloudsdkdataartsstudio.v1.TableMappingVO`]
        :param datasource: 
        :type datasource: :class:`huaweicloudsdkdataartsstudio.v1.BizDatasourceRelationVO`
        :param owner: 资产责任人。
        :type owner: str
        :param obs_location: 外表路径
        :type obs_location: str
        :param table_type: 表类型。
        :type table_type: str
        :param distribute: DISTRIBUTE BY [HASH(column)|REPLICATION]。 枚举值：   - HASH: 对指定的列进行Hash，通过映射，把数据分布到指定DN   - REPLICATION: 表的每一行存在所有数据节点（DN）中，即每个数据节点都有完整的表数据 
        :type distribute: str
        :param distribute_column: DISTRIBUTE BY HASH column.
        :type distribute_column: str
        :param alias: 别名。
        :type alias: str
        :param self_defined_fields: 自定义项。
        :type self_defined_fields: list[:class:`huaweicloudsdkdataartsstudio.v1.SelfDefinedFieldVO`]
        :param configs: 其他配置
        :type configs: str
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
        self._name_en = None
        self._dimension_type = None
        self._name_ch = None
        self._description = None
        self._create_by = None
        self._update_by = None
        self._code_table_id = None
        self._code_table = None
        self._l1_id = None
        self._l2_id = None
        self._l3_id = None
        self._hierarchies = None
        self._status = None
        self._create_time = None
        self._update_time = None
        self._approval_info = None
        self._new_biz = None
        self._l1 = None
        self._l2 = None
        self._l3 = None
        self._attributes = None
        self._mappings = None
        self._datasource = None
        self._owner = None
        self._obs_location = None
        self._table_type = None
        self._distribute = None
        self._distribute_column = None
        self._alias = None
        self._self_defined_fields = None
        self._configs = None
        self._dev_version = None
        self._prod_version = None
        self._dev_version_name = None
        self._prod_version_name = None
        self._env_type = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.name_en = name_en
        self.dimension_type = dimension_type
        self.name_ch = name_ch
        if description is not None:
            self.description = description
        if create_by is not None:
            self.create_by = create_by
        if update_by is not None:
            self.update_by = update_by
        if code_table_id is not None:
            self.code_table_id = code_table_id
        if code_table is not None:
            self.code_table = code_table
        if l1_id is not None:
            self.l1_id = l1_id
        if l2_id is not None:
            self.l2_id = l2_id
        self.l3_id = l3_id
        if hierarchies is not None:
            self.hierarchies = hierarchies
        if status is not None:
            self.status = status
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if approval_info is not None:
            self.approval_info = approval_info
        if new_biz is not None:
            self.new_biz = new_biz
        if l1 is not None:
            self.l1 = l1
        if l2 is not None:
            self.l2 = l2
        if l3 is not None:
            self.l3 = l3
        self.attributes = attributes
        if mappings is not None:
            self.mappings = mappings
        if datasource is not None:
            self.datasource = datasource
        if owner is not None:
            self.owner = owner
        if obs_location is not None:
            self.obs_location = obs_location
        if table_type is not None:
            self.table_type = table_type
        if distribute is not None:
            self.distribute = distribute
        if distribute_column is not None:
            self.distribute_column = distribute_column
        if alias is not None:
            self.alias = alias
        if self_defined_fields is not None:
            self.self_defined_fields = self_defined_fields
        if configs is not None:
            self.configs = configs
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
        """Gets the id of this DimensionVO.

        编码，填写String类型替代Long类型。

        :return: The id of this DimensionVO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DimensionVO.

        编码，填写String类型替代Long类型。

        :param id: The id of this DimensionVO.
        :type id: str
        """
        self._id = id

    @property
    def name_en(self):
        """Gets the name_en of this DimensionVO.

        字段名。

        :return: The name_en of this DimensionVO.
        :rtype: str
        """
        return self._name_en

    @name_en.setter
    def name_en(self, name_en):
        """Sets the name_en of this DimensionVO.

        字段名。

        :param name_en: The name_en of this DimensionVO.
        :type name_en: str
        """
        self._name_en = name_en

    @property
    def dimension_type(self):
        """Gets the dimension_type of this DimensionVO.

        维度类型。 枚举值：   - COMMON: 普通维度   - LOOKUP: 码表维度   - HIERARCHIES: 层级维度 

        :return: The dimension_type of this DimensionVO.
        :rtype: str
        """
        return self._dimension_type

    @dimension_type.setter
    def dimension_type(self, dimension_type):
        """Sets the dimension_type of this DimensionVO.

        维度类型。 枚举值：   - COMMON: 普通维度   - LOOKUP: 码表维度   - HIERARCHIES: 层级维度 

        :param dimension_type: The dimension_type of this DimensionVO.
        :type dimension_type: str
        """
        self._dimension_type = dimension_type

    @property
    def name_ch(self):
        """Gets the name_ch of this DimensionVO.

        业务属性。

        :return: The name_ch of this DimensionVO.
        :rtype: str
        """
        return self._name_ch

    @name_ch.setter
    def name_ch(self, name_ch):
        """Sets the name_ch of this DimensionVO.

        业务属性。

        :param name_ch: The name_ch of this DimensionVO.
        :type name_ch: str
        """
        self._name_ch = name_ch

    @property
    def description(self):
        """Gets the description of this DimensionVO.

        描述。

        :return: The description of this DimensionVO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DimensionVO.

        描述。

        :param description: The description of this DimensionVO.
        :type description: str
        """
        self._description = description

    @property
    def create_by(self):
        """Gets the create_by of this DimensionVO.

        创建人。

        :return: The create_by of this DimensionVO.
        :rtype: str
        """
        return self._create_by

    @create_by.setter
    def create_by(self, create_by):
        """Sets the create_by of this DimensionVO.

        创建人。

        :param create_by: The create_by of this DimensionVO.
        :type create_by: str
        """
        self._create_by = create_by

    @property
    def update_by(self):
        """Gets the update_by of this DimensionVO.

        更新人。

        :return: The update_by of this DimensionVO.
        :rtype: str
        """
        return self._update_by

    @update_by.setter
    def update_by(self, update_by):
        """Sets the update_by of this DimensionVO.

        更新人。

        :param update_by: The update_by of this DimensionVO.
        :type update_by: str
        """
        self._update_by = update_by

    @property
    def code_table_id(self):
        """Gets the code_table_id of this DimensionVO.

        引用码表ID，填写String类型替代Long类型。

        :return: The code_table_id of this DimensionVO.
        :rtype: str
        """
        return self._code_table_id

    @code_table_id.setter
    def code_table_id(self, code_table_id):
        """Sets the code_table_id of this DimensionVO.

        引用码表ID，填写String类型替代Long类型。

        :param code_table_id: The code_table_id of this DimensionVO.
        :type code_table_id: str
        """
        self._code_table_id = code_table_id

    @property
    def code_table(self):
        """Gets the code_table of this DimensionVO.

        :return: The code_table of this DimensionVO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.CodeTableVO`
        """
        return self._code_table

    @code_table.setter
    def code_table(self, code_table):
        """Sets the code_table of this DimensionVO.

        :param code_table: The code_table of this DimensionVO.
        :type code_table: :class:`huaweicloudsdkdataartsstudio.v1.CodeTableVO`
        """
        self._code_table = code_table

    @property
    def l1_id(self):
        """Gets the l1_id of this DimensionVO.

        主题域分组ID，只读，填写String类型替代Long类型。

        :return: The l1_id of this DimensionVO.
        :rtype: str
        """
        return self._l1_id

    @l1_id.setter
    def l1_id(self, l1_id):
        """Sets the l1_id of this DimensionVO.

        主题域分组ID，只读，填写String类型替代Long类型。

        :param l1_id: The l1_id of this DimensionVO.
        :type l1_id: str
        """
        self._l1_id = l1_id

    @property
    def l2_id(self):
        """Gets the l2_id of this DimensionVO.

        主题域ID，只读，创建和更新时无需填写。

        :return: The l2_id of this DimensionVO.
        :rtype: str
        """
        return self._l2_id

    @l2_id.setter
    def l2_id(self, l2_id):
        """Sets the l2_id of this DimensionVO.

        主题域ID，只读，创建和更新时无需填写。

        :param l2_id: The l2_id of this DimensionVO.
        :type l2_id: str
        """
        self._l2_id = l2_id

    @property
    def l3_id(self):
        """Gets the l3_id of this DimensionVO.

        业务对象ID，填写String类型替代Long类型。

        :return: The l3_id of this DimensionVO.
        :rtype: str
        """
        return self._l3_id

    @l3_id.setter
    def l3_id(self, l3_id):
        """Sets the l3_id of this DimensionVO.

        业务对象ID，填写String类型替代Long类型。

        :param l3_id: The l3_id of this DimensionVO.
        :type l3_id: str
        """
        self._l3_id = l3_id

    @property
    def hierarchies(self):
        """Gets the hierarchies of this DimensionVO.

        层级属性。

        :return: The hierarchies of this DimensionVO.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.DimensionHierarchiesVO`]
        """
        return self._hierarchies

    @hierarchies.setter
    def hierarchies(self, hierarchies):
        """Sets the hierarchies of this DimensionVO.

        层级属性。

        :param hierarchies: The hierarchies of this DimensionVO.
        :type hierarchies: list[:class:`huaweicloudsdkdataartsstudio.v1.DimensionHierarchiesVO`]
        """
        self._hierarchies = hierarchies

    @property
    def status(self):
        """Gets the status of this DimensionVO.

        :return: The status of this DimensionVO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.BizStatusEnum`
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DimensionVO.

        :param status: The status of this DimensionVO.
        :type status: :class:`huaweicloudsdkdataartsstudio.v1.BizStatusEnum`
        """
        self._status = status

    @property
    def create_time(self):
        """Gets the create_time of this DimensionVO.

        创建时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。

        :return: The create_time of this DimensionVO.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this DimensionVO.

        创建时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。

        :param create_time: The create_time of this DimensionVO.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this DimensionVO.

        更新时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。

        :return: The update_time of this DimensionVO.
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this DimensionVO.

        更新时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。

        :param update_time: The update_time of this DimensionVO.
        :type update_time: datetime
        """
        self._update_time = update_time

    @property
    def approval_info(self):
        """Gets the approval_info of this DimensionVO.

        :return: The approval_info of this DimensionVO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ApprovalVO`
        """
        return self._approval_info

    @approval_info.setter
    def approval_info(self, approval_info):
        """Sets the approval_info of this DimensionVO.

        :param approval_info: The approval_info of this DimensionVO.
        :type approval_info: :class:`huaweicloudsdkdataartsstudio.v1.ApprovalVO`
        """
        self._approval_info = approval_info

    @property
    def new_biz(self):
        """Gets the new_biz of this DimensionVO.

        :return: The new_biz of this DimensionVO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.BizVersionManageVO`
        """
        return self._new_biz

    @new_biz.setter
    def new_biz(self, new_biz):
        """Sets the new_biz of this DimensionVO.

        :param new_biz: The new_biz of this DimensionVO.
        :type new_biz: :class:`huaweicloudsdkdataartsstudio.v1.BizVersionManageVO`
        """
        self._new_biz = new_biz

    @property
    def l1(self):
        """Gets the l1 of this DimensionVO.

        主题域分组中文名，只读，创建和更新时无需填写。

        :return: The l1 of this DimensionVO.
        :rtype: str
        """
        return self._l1

    @l1.setter
    def l1(self, l1):
        """Sets the l1 of this DimensionVO.

        主题域分组中文名，只读，创建和更新时无需填写。

        :param l1: The l1 of this DimensionVO.
        :type l1: str
        """
        self._l1 = l1

    @property
    def l2(self):
        """Gets the l2 of this DimensionVO.

        主题域中文名，只读，创建和更新时无需填写。

        :return: The l2 of this DimensionVO.
        :rtype: str
        """
        return self._l2

    @l2.setter
    def l2(self, l2):
        """Sets the l2 of this DimensionVO.

        主题域中文名，只读，创建和更新时无需填写。

        :param l2: The l2 of this DimensionVO.
        :type l2: str
        """
        self._l2 = l2

    @property
    def l3(self):
        """Gets the l3 of this DimensionVO.

        业务对象中文名，只读，创建和更新时无需填写。

        :return: The l3 of this DimensionVO.
        :rtype: str
        """
        return self._l3

    @l3.setter
    def l3(self, l3):
        """Sets the l3 of this DimensionVO.

        业务对象中文名，只读，创建和更新时无需填写。

        :param l3: The l3 of this DimensionVO.
        :type l3: str
        """
        self._l3 = l3

    @property
    def attributes(self):
        """Gets the attributes of this DimensionVO.

        维度属性信息。

        :return: The attributes of this DimensionVO.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.DimensionAttributeVO`]
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this DimensionVO.

        维度属性信息。

        :param attributes: The attributes of this DimensionVO.
        :type attributes: list[:class:`huaweicloudsdkdataartsstudio.v1.DimensionAttributeVO`]
        """
        self._attributes = attributes

    @property
    def mappings(self):
        """Gets the mappings of this DimensionVO.

        表映射信息。

        :return: The mappings of this DimensionVO.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.TableMappingVO`]
        """
        return self._mappings

    @mappings.setter
    def mappings(self, mappings):
        """Sets the mappings of this DimensionVO.

        表映射信息。

        :param mappings: The mappings of this DimensionVO.
        :type mappings: list[:class:`huaweicloudsdkdataartsstudio.v1.TableMappingVO`]
        """
        self._mappings = mappings

    @property
    def datasource(self):
        """Gets the datasource of this DimensionVO.

        :return: The datasource of this DimensionVO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.BizDatasourceRelationVO`
        """
        return self._datasource

    @datasource.setter
    def datasource(self, datasource):
        """Sets the datasource of this DimensionVO.

        :param datasource: The datasource of this DimensionVO.
        :type datasource: :class:`huaweicloudsdkdataartsstudio.v1.BizDatasourceRelationVO`
        """
        self._datasource = datasource

    @property
    def owner(self):
        """Gets the owner of this DimensionVO.

        资产责任人。

        :return: The owner of this DimensionVO.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this DimensionVO.

        资产责任人。

        :param owner: The owner of this DimensionVO.
        :type owner: str
        """
        self._owner = owner

    @property
    def obs_location(self):
        """Gets the obs_location of this DimensionVO.

        外表路径

        :return: The obs_location of this DimensionVO.
        :rtype: str
        """
        return self._obs_location

    @obs_location.setter
    def obs_location(self, obs_location):
        """Sets the obs_location of this DimensionVO.

        外表路径

        :param obs_location: The obs_location of this DimensionVO.
        :type obs_location: str
        """
        self._obs_location = obs_location

    @property
    def table_type(self):
        """Gets the table_type of this DimensionVO.

        表类型。

        :return: The table_type of this DimensionVO.
        :rtype: str
        """
        return self._table_type

    @table_type.setter
    def table_type(self, table_type):
        """Sets the table_type of this DimensionVO.

        表类型。

        :param table_type: The table_type of this DimensionVO.
        :type table_type: str
        """
        self._table_type = table_type

    @property
    def distribute(self):
        """Gets the distribute of this DimensionVO.

        DISTRIBUTE BY [HASH(column)|REPLICATION]。 枚举值：   - HASH: 对指定的列进行Hash，通过映射，把数据分布到指定DN   - REPLICATION: 表的每一行存在所有数据节点（DN）中，即每个数据节点都有完整的表数据 

        :return: The distribute of this DimensionVO.
        :rtype: str
        """
        return self._distribute

    @distribute.setter
    def distribute(self, distribute):
        """Sets the distribute of this DimensionVO.

        DISTRIBUTE BY [HASH(column)|REPLICATION]。 枚举值：   - HASH: 对指定的列进行Hash，通过映射，把数据分布到指定DN   - REPLICATION: 表的每一行存在所有数据节点（DN）中，即每个数据节点都有完整的表数据 

        :param distribute: The distribute of this DimensionVO.
        :type distribute: str
        """
        self._distribute = distribute

    @property
    def distribute_column(self):
        """Gets the distribute_column of this DimensionVO.

        DISTRIBUTE BY HASH column.

        :return: The distribute_column of this DimensionVO.
        :rtype: str
        """
        return self._distribute_column

    @distribute_column.setter
    def distribute_column(self, distribute_column):
        """Sets the distribute_column of this DimensionVO.

        DISTRIBUTE BY HASH column.

        :param distribute_column: The distribute_column of this DimensionVO.
        :type distribute_column: str
        """
        self._distribute_column = distribute_column

    @property
    def alias(self):
        """Gets the alias of this DimensionVO.

        别名。

        :return: The alias of this DimensionVO.
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """Sets the alias of this DimensionVO.

        别名。

        :param alias: The alias of this DimensionVO.
        :type alias: str
        """
        self._alias = alias

    @property
    def self_defined_fields(self):
        """Gets the self_defined_fields of this DimensionVO.

        自定义项。

        :return: The self_defined_fields of this DimensionVO.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.SelfDefinedFieldVO`]
        """
        return self._self_defined_fields

    @self_defined_fields.setter
    def self_defined_fields(self, self_defined_fields):
        """Sets the self_defined_fields of this DimensionVO.

        自定义项。

        :param self_defined_fields: The self_defined_fields of this DimensionVO.
        :type self_defined_fields: list[:class:`huaweicloudsdkdataartsstudio.v1.SelfDefinedFieldVO`]
        """
        self._self_defined_fields = self_defined_fields

    @property
    def configs(self):
        """Gets the configs of this DimensionVO.

        其他配置

        :return: The configs of this DimensionVO.
        :rtype: str
        """
        return self._configs

    @configs.setter
    def configs(self, configs):
        """Sets the configs of this DimensionVO.

        其他配置

        :param configs: The configs of this DimensionVO.
        :type configs: str
        """
        self._configs = configs

    @property
    def dev_version(self):
        """Gets the dev_version of this DimensionVO.

        开发环境版本，填写String类型替代Long类型。

        :return: The dev_version of this DimensionVO.
        :rtype: str
        """
        return self._dev_version

    @dev_version.setter
    def dev_version(self, dev_version):
        """Sets the dev_version of this DimensionVO.

        开发环境版本，填写String类型替代Long类型。

        :param dev_version: The dev_version of this DimensionVO.
        :type dev_version: str
        """
        self._dev_version = dev_version

    @property
    def prod_version(self):
        """Gets the prod_version of this DimensionVO.

        生产环境版本，填写String类型替代Long类型。

        :return: The prod_version of this DimensionVO.
        :rtype: str
        """
        return self._prod_version

    @prod_version.setter
    def prod_version(self, prod_version):
        """Sets the prod_version of this DimensionVO.

        生产环境版本，填写String类型替代Long类型。

        :param prod_version: The prod_version of this DimensionVO.
        :type prod_version: str
        """
        self._prod_version = prod_version

    @property
    def dev_version_name(self):
        """Gets the dev_version_name of this DimensionVO.

        开发环境版本名称

        :return: The dev_version_name of this DimensionVO.
        :rtype: str
        """
        return self._dev_version_name

    @dev_version_name.setter
    def dev_version_name(self, dev_version_name):
        """Sets the dev_version_name of this DimensionVO.

        开发环境版本名称

        :param dev_version_name: The dev_version_name of this DimensionVO.
        :type dev_version_name: str
        """
        self._dev_version_name = dev_version_name

    @property
    def prod_version_name(self):
        """Gets the prod_version_name of this DimensionVO.

        生产环境版本名称

        :return: The prod_version_name of this DimensionVO.
        :rtype: str
        """
        return self._prod_version_name

    @prod_version_name.setter
    def prod_version_name(self, prod_version_name):
        """Sets the prod_version_name of this DimensionVO.

        生产环境版本名称

        :param prod_version_name: The prod_version_name of this DimensionVO.
        :type prod_version_name: str
        """
        self._prod_version_name = prod_version_name

    @property
    def env_type(self):
        """Gets the env_type of this DimensionVO.

        :return: The env_type of this DimensionVO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.EnvTypeEnum`
        """
        return self._env_type

    @env_type.setter
    def env_type(self, env_type):
        """Sets the env_type of this DimensionVO.

        :param env_type: The env_type of this DimensionVO.
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
        if not isinstance(other, DimensionVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
