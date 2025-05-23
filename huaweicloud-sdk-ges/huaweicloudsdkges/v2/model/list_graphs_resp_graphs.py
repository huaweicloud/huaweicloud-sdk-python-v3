# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListGraphsRespGraphs:

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
        'created_by': 'str',
        'is_multi_az': 'str',
        'region_code': 'str',
        'az_code': 'str',
        'schema_path': 'list[ListGraphsRespSchemaPath]',
        'edgeset_path': 'list[ListGraphsRespSchemaPath]',
        'vertexset_path': 'list[ListGraphsRespSchemaPath]',
        'edgeset_format': 'str',
        'edgeset_default_label': 'str',
        'vertexset_format': 'str',
        'vertexset_default_label': 'str',
        'data_store_version': 'str',
        'sys_tags': 'list[str]',
        'status': 'str',
        'action_progress': 'str',
        'graph_size_type_index': 'str',
        'vpc_id': 'str',
        'subnet_id': 'str',
        'security_group_id': 'str',
        'replication': 'int',
        'created': 'str',
        'updated': 'str',
        'private_ip': 'str',
        'public_ip': 'str',
        'arch': 'str',
        'encrypted': 'bool',
        'master_key_id': 'str',
        'master_key_name': 'str',
        'enable_rbac': 'bool',
        'enable_full_text_index': 'bool',
        'enable_hyg': 'bool',
        'traffic_ip_list': 'list[str]',
        'crypt_algorithm': 'str',
        'enable_https': 'bool',
        'tags': 'list[ListGraphsRespTags]',
        'product_type': 'str',
        'vertex_id_type': 'ListGraphsRespVertexIdType',
        'origin_graph_size_type_index': 'str',
        'expand_time': 'str',
        'resize_time': 'str',
        'enable_multi_label': 'bool',
        'capacity_ratio': 'int',
        'sort_key_type': 'str',
        'enable_lts': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'created_by': 'created_by',
        'is_multi_az': 'is_multi_az',
        'region_code': 'region_code',
        'az_code': 'az_code',
        'schema_path': 'schema_path',
        'edgeset_path': 'edgeset_path',
        'vertexset_path': 'vertexset_path',
        'edgeset_format': 'edgeset_format',
        'edgeset_default_label': 'edgeset_default_label',
        'vertexset_format': 'vertexset_format',
        'vertexset_default_label': 'vertexset_default_label',
        'data_store_version': 'data_store_version',
        'sys_tags': 'sys_tags',
        'status': 'status',
        'action_progress': 'action_progress',
        'graph_size_type_index': 'graph_size_type_index',
        'vpc_id': 'vpc_id',
        'subnet_id': 'subnet_id',
        'security_group_id': 'security_group_id',
        'replication': 'replication',
        'created': 'created',
        'updated': 'updated',
        'private_ip': 'private_ip',
        'public_ip': 'public_ip',
        'arch': 'arch',
        'encrypted': 'encrypted',
        'master_key_id': 'master_key_id',
        'master_key_name': 'master_key_name',
        'enable_rbac': 'enable_rbac',
        'enable_full_text_index': 'enable_full_text_index',
        'enable_hyg': 'enable_hyg',
        'traffic_ip_list': 'traffic_ip_list',
        'crypt_algorithm': 'crypt_algorithm',
        'enable_https': 'enable_https',
        'tags': 'tags',
        'product_type': 'product_type',
        'vertex_id_type': 'vertex_id_type',
        'origin_graph_size_type_index': 'origin_graph_size_type_index',
        'expand_time': 'expand_time',
        'resize_time': 'resize_time',
        'enable_multi_label': 'enable_multi_label',
        'capacity_ratio': 'capacity_ratio',
        'sort_key_type': 'sort_key_type',
        'enable_lts': 'enable_lts'
    }

    def __init__(self, id=None, name=None, created_by=None, is_multi_az=None, region_code=None, az_code=None, schema_path=None, edgeset_path=None, vertexset_path=None, edgeset_format=None, edgeset_default_label=None, vertexset_format=None, vertexset_default_label=None, data_store_version=None, sys_tags=None, status=None, action_progress=None, graph_size_type_index=None, vpc_id=None, subnet_id=None, security_group_id=None, replication=None, created=None, updated=None, private_ip=None, public_ip=None, arch=None, encrypted=None, master_key_id=None, master_key_name=None, enable_rbac=None, enable_full_text_index=None, enable_hyg=None, traffic_ip_list=None, crypt_algorithm=None, enable_https=None, tags=None, product_type=None, vertex_id_type=None, origin_graph_size_type_index=None, expand_time=None, resize_time=None, enable_multi_label=None, capacity_ratio=None, sort_key_type=None, enable_lts=None):
        r"""ListGraphsRespGraphs

        The model defined in huaweicloud sdk

        :param id: 图ID。
        :type id: str
        :param name: 图名称。
        :type name: str
        :param created_by: 图的创建人账号。
        :type created_by: str
        :param is_multi_az: 是否支持跨AZ高可用。
        :type is_multi_az: str
        :param region_code: 域编码。
        :type region_code: str
        :param az_code: 可用区编码。
        :type az_code: str
        :param schema_path: 元数据文件路径。
        :type schema_path: list[:class:`huaweicloudsdkges.v2.ListGraphsRespSchemaPath`]
        :param edgeset_path: 边数据集OBS路径。
        :type edgeset_path: list[:class:`huaweicloudsdkges.v2.ListGraphsRespSchemaPath`]
        :param vertexset_path: 点数据集OBS路径。
        :type vertexset_path: list[:class:`huaweicloudsdkges.v2.ListGraphsRespSchemaPath`]
        :param edgeset_format: 边数据集文件格式。
        :type edgeset_format: str
        :param edgeset_default_label: 边数据集文件默认Label。
        :type edgeset_default_label: str
        :param vertexset_format: 点数据集文件格式。
        :type vertexset_format: str
        :param vertexset_default_label: 点数据集文件默认Label。
        :type vertexset_default_label: str
        :param data_store_version: 图版本。
        :type data_store_version: str
        :param sys_tags: 企业项目信息，如果未指定则不开启，默认不开启。
        :type sys_tags: list[str]
        :param status: 图的状态码。  - 100：准备中 - 200：运行中 - 201：升级中 - 202：导入中 - 203：回滚中 - 204：导出中 - 205：清空中 - 206：扩容准备中 - 207：扩容中 - 208：扩容回退中 - 210：扩副本准备中 - 211：扩副本中 - 300：故障 - 303：创建失败 - 400：被删除 - 800：已冻结 - 900：停止 - 901：停止中 - 920：启动中
        :type status: str
        :param action_progress: 图创建进度百分比。 &gt; 只有图状态码为100时返回该字段。
        :type action_progress: str
        :param graph_size_type_index: 图规模类型索引。  - 0：一万边 - 1：百万边 - 2：千万边 - 3：一亿边 - 4：十亿边 - 5：百亿边 - 6：千亿边 - 401：十亿增强边
        :type graph_size_type_index: str
        :param vpc_id: 虚拟私有云ID。
        :type vpc_id: str
        :param subnet_id: 指定虚拟私有云下的子网ID。
        :type subnet_id: str
        :param security_group_id: 安全组ID。
        :type security_group_id: str
        :param replication: 副本个数，默认为1。
        :type replication: int
        :param created: 图创建时间。
        :type created: str
        :param updated: 图更新时间。
        :type updated: str
        :param private_ip: 图实例私有网络访问浮动IP地址，通过该IP用户可以通过私有网络中已部署的弹性云服务器对图实例进行访问。
        :type private_ip: str
        :param public_ip: 图实例公网访问地址，通过该IP用户可以从互联网对图实例进行访问。
        :type public_ip: str
        :param arch: 图实例CPU架构类型，取值为x86_64和aarch64。
        :type arch: str
        :param encrypted: 是否加密。默认值为“false”，默认不加密。
        :type encrypted: bool
        :param master_key_id: 用户主密钥ID。
        :type master_key_id: str
        :param master_key_name: 用户主密钥名称。
        :type master_key_name: str
        :param enable_rbac: 是否启用细粒度权限控制。
        :type enable_rbac: bool
        :param enable_full_text_index: 是否启用全文索引。
        :type enable_full_text_index: bool
        :param enable_hyg: 是否启用HyG，该参数只对千亿规格图生效。
        :type enable_hyg: bool
        :param traffic_ip_list: 图实例私有网络访问物理地址列表。为了防止浮动IP切换造成业务闪断，我们推荐您通过轮询的方式使用物理IP访问图实例。
        :type traffic_ip_list: list[str]
        :param crypt_algorithm: 图实例加密算法，取值为：  - generalCipher：国密算法 - SMcompatible：商密算法（兼容国际）
        :type crypt_algorithm: str
        :param enable_https: 是否开启安全模式，开启安全模式会对性能有较大影响
        :type enable_https: bool
        :param tags: 标签列表，每个标签用&lt;key,value&gt;键值对表示。
        :type tags: list[:class:`huaweicloudsdkges.v2.ListGraphsRespTags`]
        :param product_type: 图产品类型，取值为InMemory和Persistence，默认为InMemory，当graph_size_type_index取值为\&quot;6\&quot;时，默认为Persistence。  - InMemory：内存版 - Persistence：持久化版
        :type product_type: str
        :param vertex_id_type: 
        :type vertex_id_type: :class:`huaweicloudsdkges.v2.ListGraphsRespVertexIdType`
        :param origin_graph_size_type_index: 图的初始规格。该参数从2.3.15版本后开始支持。
        :type origin_graph_size_type_index: str
        :param expand_time: 图扩副本的时间。
        :type expand_time: str
        :param resize_time: 图扩容的时间。
        :type resize_time: str
        :param enable_multi_label: 是否启用多标签。
        :type enable_multi_label: bool
        :param capacity_ratio: 图的容量倍率。只有持久化版百亿规格图支持该参数，该参数从2.3.18版本后开始支持。
        :type capacity_ratio: int
        :param sort_key_type: 图的sortKey类型，内存版图无此值。
        :type sort_key_type: str
        :param enable_lts: 对接云服务LTS日志开启状态。  - true：日志对接开启中。 - false：日志对接关闭中。
        :type enable_lts: bool
        """
        
        

        self._id = None
        self._name = None
        self._created_by = None
        self._is_multi_az = None
        self._region_code = None
        self._az_code = None
        self._schema_path = None
        self._edgeset_path = None
        self._vertexset_path = None
        self._edgeset_format = None
        self._edgeset_default_label = None
        self._vertexset_format = None
        self._vertexset_default_label = None
        self._data_store_version = None
        self._sys_tags = None
        self._status = None
        self._action_progress = None
        self._graph_size_type_index = None
        self._vpc_id = None
        self._subnet_id = None
        self._security_group_id = None
        self._replication = None
        self._created = None
        self._updated = None
        self._private_ip = None
        self._public_ip = None
        self._arch = None
        self._encrypted = None
        self._master_key_id = None
        self._master_key_name = None
        self._enable_rbac = None
        self._enable_full_text_index = None
        self._enable_hyg = None
        self._traffic_ip_list = None
        self._crypt_algorithm = None
        self._enable_https = None
        self._tags = None
        self._product_type = None
        self._vertex_id_type = None
        self._origin_graph_size_type_index = None
        self._expand_time = None
        self._resize_time = None
        self._enable_multi_label = None
        self._capacity_ratio = None
        self._sort_key_type = None
        self._enable_lts = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if created_by is not None:
            self.created_by = created_by
        if is_multi_az is not None:
            self.is_multi_az = is_multi_az
        if region_code is not None:
            self.region_code = region_code
        if az_code is not None:
            self.az_code = az_code
        if schema_path is not None:
            self.schema_path = schema_path
        if edgeset_path is not None:
            self.edgeset_path = edgeset_path
        if vertexset_path is not None:
            self.vertexset_path = vertexset_path
        if edgeset_format is not None:
            self.edgeset_format = edgeset_format
        if edgeset_default_label is not None:
            self.edgeset_default_label = edgeset_default_label
        if vertexset_format is not None:
            self.vertexset_format = vertexset_format
        if vertexset_default_label is not None:
            self.vertexset_default_label = vertexset_default_label
        if data_store_version is not None:
            self.data_store_version = data_store_version
        if sys_tags is not None:
            self.sys_tags = sys_tags
        if status is not None:
            self.status = status
        if action_progress is not None:
            self.action_progress = action_progress
        if graph_size_type_index is not None:
            self.graph_size_type_index = graph_size_type_index
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if subnet_id is not None:
            self.subnet_id = subnet_id
        if security_group_id is not None:
            self.security_group_id = security_group_id
        if replication is not None:
            self.replication = replication
        if created is not None:
            self.created = created
        if updated is not None:
            self.updated = updated
        if private_ip is not None:
            self.private_ip = private_ip
        if public_ip is not None:
            self.public_ip = public_ip
        if arch is not None:
            self.arch = arch
        if encrypted is not None:
            self.encrypted = encrypted
        if master_key_id is not None:
            self.master_key_id = master_key_id
        if master_key_name is not None:
            self.master_key_name = master_key_name
        if enable_rbac is not None:
            self.enable_rbac = enable_rbac
        if enable_full_text_index is not None:
            self.enable_full_text_index = enable_full_text_index
        if enable_hyg is not None:
            self.enable_hyg = enable_hyg
        if traffic_ip_list is not None:
            self.traffic_ip_list = traffic_ip_list
        if crypt_algorithm is not None:
            self.crypt_algorithm = crypt_algorithm
        if enable_https is not None:
            self.enable_https = enable_https
        if tags is not None:
            self.tags = tags
        if product_type is not None:
            self.product_type = product_type
        if vertex_id_type is not None:
            self.vertex_id_type = vertex_id_type
        if origin_graph_size_type_index is not None:
            self.origin_graph_size_type_index = origin_graph_size_type_index
        if expand_time is not None:
            self.expand_time = expand_time
        if resize_time is not None:
            self.resize_time = resize_time
        if enable_multi_label is not None:
            self.enable_multi_label = enable_multi_label
        if capacity_ratio is not None:
            self.capacity_ratio = capacity_ratio
        if sort_key_type is not None:
            self.sort_key_type = sort_key_type
        if enable_lts is not None:
            self.enable_lts = enable_lts

    @property
    def id(self):
        r"""Gets the id of this ListGraphsRespGraphs.

        图ID。

        :return: The id of this ListGraphsRespGraphs.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListGraphsRespGraphs.

        图ID。

        :param id: The id of this ListGraphsRespGraphs.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ListGraphsRespGraphs.

        图名称。

        :return: The name of this ListGraphsRespGraphs.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListGraphsRespGraphs.

        图名称。

        :param name: The name of this ListGraphsRespGraphs.
        :type name: str
        """
        self._name = name

    @property
    def created_by(self):
        r"""Gets the created_by of this ListGraphsRespGraphs.

        图的创建人账号。

        :return: The created_by of this ListGraphsRespGraphs.
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        r"""Sets the created_by of this ListGraphsRespGraphs.

        图的创建人账号。

        :param created_by: The created_by of this ListGraphsRespGraphs.
        :type created_by: str
        """
        self._created_by = created_by

    @property
    def is_multi_az(self):
        r"""Gets the is_multi_az of this ListGraphsRespGraphs.

        是否支持跨AZ高可用。

        :return: The is_multi_az of this ListGraphsRespGraphs.
        :rtype: str
        """
        return self._is_multi_az

    @is_multi_az.setter
    def is_multi_az(self, is_multi_az):
        r"""Sets the is_multi_az of this ListGraphsRespGraphs.

        是否支持跨AZ高可用。

        :param is_multi_az: The is_multi_az of this ListGraphsRespGraphs.
        :type is_multi_az: str
        """
        self._is_multi_az = is_multi_az

    @property
    def region_code(self):
        r"""Gets the region_code of this ListGraphsRespGraphs.

        域编码。

        :return: The region_code of this ListGraphsRespGraphs.
        :rtype: str
        """
        return self._region_code

    @region_code.setter
    def region_code(self, region_code):
        r"""Sets the region_code of this ListGraphsRespGraphs.

        域编码。

        :param region_code: The region_code of this ListGraphsRespGraphs.
        :type region_code: str
        """
        self._region_code = region_code

    @property
    def az_code(self):
        r"""Gets the az_code of this ListGraphsRespGraphs.

        可用区编码。

        :return: The az_code of this ListGraphsRespGraphs.
        :rtype: str
        """
        return self._az_code

    @az_code.setter
    def az_code(self, az_code):
        r"""Sets the az_code of this ListGraphsRespGraphs.

        可用区编码。

        :param az_code: The az_code of this ListGraphsRespGraphs.
        :type az_code: str
        """
        self._az_code = az_code

    @property
    def schema_path(self):
        r"""Gets the schema_path of this ListGraphsRespGraphs.

        元数据文件路径。

        :return: The schema_path of this ListGraphsRespGraphs.
        :rtype: list[:class:`huaweicloudsdkges.v2.ListGraphsRespSchemaPath`]
        """
        return self._schema_path

    @schema_path.setter
    def schema_path(self, schema_path):
        r"""Sets the schema_path of this ListGraphsRespGraphs.

        元数据文件路径。

        :param schema_path: The schema_path of this ListGraphsRespGraphs.
        :type schema_path: list[:class:`huaweicloudsdkges.v2.ListGraphsRespSchemaPath`]
        """
        self._schema_path = schema_path

    @property
    def edgeset_path(self):
        r"""Gets the edgeset_path of this ListGraphsRespGraphs.

        边数据集OBS路径。

        :return: The edgeset_path of this ListGraphsRespGraphs.
        :rtype: list[:class:`huaweicloudsdkges.v2.ListGraphsRespSchemaPath`]
        """
        return self._edgeset_path

    @edgeset_path.setter
    def edgeset_path(self, edgeset_path):
        r"""Sets the edgeset_path of this ListGraphsRespGraphs.

        边数据集OBS路径。

        :param edgeset_path: The edgeset_path of this ListGraphsRespGraphs.
        :type edgeset_path: list[:class:`huaweicloudsdkges.v2.ListGraphsRespSchemaPath`]
        """
        self._edgeset_path = edgeset_path

    @property
    def vertexset_path(self):
        r"""Gets the vertexset_path of this ListGraphsRespGraphs.

        点数据集OBS路径。

        :return: The vertexset_path of this ListGraphsRespGraphs.
        :rtype: list[:class:`huaweicloudsdkges.v2.ListGraphsRespSchemaPath`]
        """
        return self._vertexset_path

    @vertexset_path.setter
    def vertexset_path(self, vertexset_path):
        r"""Sets the vertexset_path of this ListGraphsRespGraphs.

        点数据集OBS路径。

        :param vertexset_path: The vertexset_path of this ListGraphsRespGraphs.
        :type vertexset_path: list[:class:`huaweicloudsdkges.v2.ListGraphsRespSchemaPath`]
        """
        self._vertexset_path = vertexset_path

    @property
    def edgeset_format(self):
        r"""Gets the edgeset_format of this ListGraphsRespGraphs.

        边数据集文件格式。

        :return: The edgeset_format of this ListGraphsRespGraphs.
        :rtype: str
        """
        return self._edgeset_format

    @edgeset_format.setter
    def edgeset_format(self, edgeset_format):
        r"""Sets the edgeset_format of this ListGraphsRespGraphs.

        边数据集文件格式。

        :param edgeset_format: The edgeset_format of this ListGraphsRespGraphs.
        :type edgeset_format: str
        """
        self._edgeset_format = edgeset_format

    @property
    def edgeset_default_label(self):
        r"""Gets the edgeset_default_label of this ListGraphsRespGraphs.

        边数据集文件默认Label。

        :return: The edgeset_default_label of this ListGraphsRespGraphs.
        :rtype: str
        """
        return self._edgeset_default_label

    @edgeset_default_label.setter
    def edgeset_default_label(self, edgeset_default_label):
        r"""Sets the edgeset_default_label of this ListGraphsRespGraphs.

        边数据集文件默认Label。

        :param edgeset_default_label: The edgeset_default_label of this ListGraphsRespGraphs.
        :type edgeset_default_label: str
        """
        self._edgeset_default_label = edgeset_default_label

    @property
    def vertexset_format(self):
        r"""Gets the vertexset_format of this ListGraphsRespGraphs.

        点数据集文件格式。

        :return: The vertexset_format of this ListGraphsRespGraphs.
        :rtype: str
        """
        return self._vertexset_format

    @vertexset_format.setter
    def vertexset_format(self, vertexset_format):
        r"""Sets the vertexset_format of this ListGraphsRespGraphs.

        点数据集文件格式。

        :param vertexset_format: The vertexset_format of this ListGraphsRespGraphs.
        :type vertexset_format: str
        """
        self._vertexset_format = vertexset_format

    @property
    def vertexset_default_label(self):
        r"""Gets the vertexset_default_label of this ListGraphsRespGraphs.

        点数据集文件默认Label。

        :return: The vertexset_default_label of this ListGraphsRespGraphs.
        :rtype: str
        """
        return self._vertexset_default_label

    @vertexset_default_label.setter
    def vertexset_default_label(self, vertexset_default_label):
        r"""Sets the vertexset_default_label of this ListGraphsRespGraphs.

        点数据集文件默认Label。

        :param vertexset_default_label: The vertexset_default_label of this ListGraphsRespGraphs.
        :type vertexset_default_label: str
        """
        self._vertexset_default_label = vertexset_default_label

    @property
    def data_store_version(self):
        r"""Gets the data_store_version of this ListGraphsRespGraphs.

        图版本。

        :return: The data_store_version of this ListGraphsRespGraphs.
        :rtype: str
        """
        return self._data_store_version

    @data_store_version.setter
    def data_store_version(self, data_store_version):
        r"""Sets the data_store_version of this ListGraphsRespGraphs.

        图版本。

        :param data_store_version: The data_store_version of this ListGraphsRespGraphs.
        :type data_store_version: str
        """
        self._data_store_version = data_store_version

    @property
    def sys_tags(self):
        r"""Gets the sys_tags of this ListGraphsRespGraphs.

        企业项目信息，如果未指定则不开启，默认不开启。

        :return: The sys_tags of this ListGraphsRespGraphs.
        :rtype: list[str]
        """
        return self._sys_tags

    @sys_tags.setter
    def sys_tags(self, sys_tags):
        r"""Sets the sys_tags of this ListGraphsRespGraphs.

        企业项目信息，如果未指定则不开启，默认不开启。

        :param sys_tags: The sys_tags of this ListGraphsRespGraphs.
        :type sys_tags: list[str]
        """
        self._sys_tags = sys_tags

    @property
    def status(self):
        r"""Gets the status of this ListGraphsRespGraphs.

        图的状态码。  - 100：准备中 - 200：运行中 - 201：升级中 - 202：导入中 - 203：回滚中 - 204：导出中 - 205：清空中 - 206：扩容准备中 - 207：扩容中 - 208：扩容回退中 - 210：扩副本准备中 - 211：扩副本中 - 300：故障 - 303：创建失败 - 400：被删除 - 800：已冻结 - 900：停止 - 901：停止中 - 920：启动中

        :return: The status of this ListGraphsRespGraphs.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListGraphsRespGraphs.

        图的状态码。  - 100：准备中 - 200：运行中 - 201：升级中 - 202：导入中 - 203：回滚中 - 204：导出中 - 205：清空中 - 206：扩容准备中 - 207：扩容中 - 208：扩容回退中 - 210：扩副本准备中 - 211：扩副本中 - 300：故障 - 303：创建失败 - 400：被删除 - 800：已冻结 - 900：停止 - 901：停止中 - 920：启动中

        :param status: The status of this ListGraphsRespGraphs.
        :type status: str
        """
        self._status = status

    @property
    def action_progress(self):
        r"""Gets the action_progress of this ListGraphsRespGraphs.

        图创建进度百分比。 > 只有图状态码为100时返回该字段。

        :return: The action_progress of this ListGraphsRespGraphs.
        :rtype: str
        """
        return self._action_progress

    @action_progress.setter
    def action_progress(self, action_progress):
        r"""Sets the action_progress of this ListGraphsRespGraphs.

        图创建进度百分比。 > 只有图状态码为100时返回该字段。

        :param action_progress: The action_progress of this ListGraphsRespGraphs.
        :type action_progress: str
        """
        self._action_progress = action_progress

    @property
    def graph_size_type_index(self):
        r"""Gets the graph_size_type_index of this ListGraphsRespGraphs.

        图规模类型索引。  - 0：一万边 - 1：百万边 - 2：千万边 - 3：一亿边 - 4：十亿边 - 5：百亿边 - 6：千亿边 - 401：十亿增强边

        :return: The graph_size_type_index of this ListGraphsRespGraphs.
        :rtype: str
        """
        return self._graph_size_type_index

    @graph_size_type_index.setter
    def graph_size_type_index(self, graph_size_type_index):
        r"""Sets the graph_size_type_index of this ListGraphsRespGraphs.

        图规模类型索引。  - 0：一万边 - 1：百万边 - 2：千万边 - 3：一亿边 - 4：十亿边 - 5：百亿边 - 6：千亿边 - 401：十亿增强边

        :param graph_size_type_index: The graph_size_type_index of this ListGraphsRespGraphs.
        :type graph_size_type_index: str
        """
        self._graph_size_type_index = graph_size_type_index

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this ListGraphsRespGraphs.

        虚拟私有云ID。

        :return: The vpc_id of this ListGraphsRespGraphs.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this ListGraphsRespGraphs.

        虚拟私有云ID。

        :param vpc_id: The vpc_id of this ListGraphsRespGraphs.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def subnet_id(self):
        r"""Gets the subnet_id of this ListGraphsRespGraphs.

        指定虚拟私有云下的子网ID。

        :return: The subnet_id of this ListGraphsRespGraphs.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        r"""Sets the subnet_id of this ListGraphsRespGraphs.

        指定虚拟私有云下的子网ID。

        :param subnet_id: The subnet_id of this ListGraphsRespGraphs.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def security_group_id(self):
        r"""Gets the security_group_id of this ListGraphsRespGraphs.

        安全组ID。

        :return: The security_group_id of this ListGraphsRespGraphs.
        :rtype: str
        """
        return self._security_group_id

    @security_group_id.setter
    def security_group_id(self, security_group_id):
        r"""Sets the security_group_id of this ListGraphsRespGraphs.

        安全组ID。

        :param security_group_id: The security_group_id of this ListGraphsRespGraphs.
        :type security_group_id: str
        """
        self._security_group_id = security_group_id

    @property
    def replication(self):
        r"""Gets the replication of this ListGraphsRespGraphs.

        副本个数，默认为1。

        :return: The replication of this ListGraphsRespGraphs.
        :rtype: int
        """
        return self._replication

    @replication.setter
    def replication(self, replication):
        r"""Sets the replication of this ListGraphsRespGraphs.

        副本个数，默认为1。

        :param replication: The replication of this ListGraphsRespGraphs.
        :type replication: int
        """
        self._replication = replication

    @property
    def created(self):
        r"""Gets the created of this ListGraphsRespGraphs.

        图创建时间。

        :return: The created of this ListGraphsRespGraphs.
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        r"""Sets the created of this ListGraphsRespGraphs.

        图创建时间。

        :param created: The created of this ListGraphsRespGraphs.
        :type created: str
        """
        self._created = created

    @property
    def updated(self):
        r"""Gets the updated of this ListGraphsRespGraphs.

        图更新时间。

        :return: The updated of this ListGraphsRespGraphs.
        :rtype: str
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        r"""Sets the updated of this ListGraphsRespGraphs.

        图更新时间。

        :param updated: The updated of this ListGraphsRespGraphs.
        :type updated: str
        """
        self._updated = updated

    @property
    def private_ip(self):
        r"""Gets the private_ip of this ListGraphsRespGraphs.

        图实例私有网络访问浮动IP地址，通过该IP用户可以通过私有网络中已部署的弹性云服务器对图实例进行访问。

        :return: The private_ip of this ListGraphsRespGraphs.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        r"""Sets the private_ip of this ListGraphsRespGraphs.

        图实例私有网络访问浮动IP地址，通过该IP用户可以通过私有网络中已部署的弹性云服务器对图实例进行访问。

        :param private_ip: The private_ip of this ListGraphsRespGraphs.
        :type private_ip: str
        """
        self._private_ip = private_ip

    @property
    def public_ip(self):
        r"""Gets the public_ip of this ListGraphsRespGraphs.

        图实例公网访问地址，通过该IP用户可以从互联网对图实例进行访问。

        :return: The public_ip of this ListGraphsRespGraphs.
        :rtype: str
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        r"""Sets the public_ip of this ListGraphsRespGraphs.

        图实例公网访问地址，通过该IP用户可以从互联网对图实例进行访问。

        :param public_ip: The public_ip of this ListGraphsRespGraphs.
        :type public_ip: str
        """
        self._public_ip = public_ip

    @property
    def arch(self):
        r"""Gets the arch of this ListGraphsRespGraphs.

        图实例CPU架构类型，取值为x86_64和aarch64。

        :return: The arch of this ListGraphsRespGraphs.
        :rtype: str
        """
        return self._arch

    @arch.setter
    def arch(self, arch):
        r"""Sets the arch of this ListGraphsRespGraphs.

        图实例CPU架构类型，取值为x86_64和aarch64。

        :param arch: The arch of this ListGraphsRespGraphs.
        :type arch: str
        """
        self._arch = arch

    @property
    def encrypted(self):
        r"""Gets the encrypted of this ListGraphsRespGraphs.

        是否加密。默认值为“false”，默认不加密。

        :return: The encrypted of this ListGraphsRespGraphs.
        :rtype: bool
        """
        return self._encrypted

    @encrypted.setter
    def encrypted(self, encrypted):
        r"""Sets the encrypted of this ListGraphsRespGraphs.

        是否加密。默认值为“false”，默认不加密。

        :param encrypted: The encrypted of this ListGraphsRespGraphs.
        :type encrypted: bool
        """
        self._encrypted = encrypted

    @property
    def master_key_id(self):
        r"""Gets the master_key_id of this ListGraphsRespGraphs.

        用户主密钥ID。

        :return: The master_key_id of this ListGraphsRespGraphs.
        :rtype: str
        """
        return self._master_key_id

    @master_key_id.setter
    def master_key_id(self, master_key_id):
        r"""Sets the master_key_id of this ListGraphsRespGraphs.

        用户主密钥ID。

        :param master_key_id: The master_key_id of this ListGraphsRespGraphs.
        :type master_key_id: str
        """
        self._master_key_id = master_key_id

    @property
    def master_key_name(self):
        r"""Gets the master_key_name of this ListGraphsRespGraphs.

        用户主密钥名称。

        :return: The master_key_name of this ListGraphsRespGraphs.
        :rtype: str
        """
        return self._master_key_name

    @master_key_name.setter
    def master_key_name(self, master_key_name):
        r"""Sets the master_key_name of this ListGraphsRespGraphs.

        用户主密钥名称。

        :param master_key_name: The master_key_name of this ListGraphsRespGraphs.
        :type master_key_name: str
        """
        self._master_key_name = master_key_name

    @property
    def enable_rbac(self):
        r"""Gets the enable_rbac of this ListGraphsRespGraphs.

        是否启用细粒度权限控制。

        :return: The enable_rbac of this ListGraphsRespGraphs.
        :rtype: bool
        """
        return self._enable_rbac

    @enable_rbac.setter
    def enable_rbac(self, enable_rbac):
        r"""Sets the enable_rbac of this ListGraphsRespGraphs.

        是否启用细粒度权限控制。

        :param enable_rbac: The enable_rbac of this ListGraphsRespGraphs.
        :type enable_rbac: bool
        """
        self._enable_rbac = enable_rbac

    @property
    def enable_full_text_index(self):
        r"""Gets the enable_full_text_index of this ListGraphsRespGraphs.

        是否启用全文索引。

        :return: The enable_full_text_index of this ListGraphsRespGraphs.
        :rtype: bool
        """
        return self._enable_full_text_index

    @enable_full_text_index.setter
    def enable_full_text_index(self, enable_full_text_index):
        r"""Sets the enable_full_text_index of this ListGraphsRespGraphs.

        是否启用全文索引。

        :param enable_full_text_index: The enable_full_text_index of this ListGraphsRespGraphs.
        :type enable_full_text_index: bool
        """
        self._enable_full_text_index = enable_full_text_index

    @property
    def enable_hyg(self):
        r"""Gets the enable_hyg of this ListGraphsRespGraphs.

        是否启用HyG，该参数只对千亿规格图生效。

        :return: The enable_hyg of this ListGraphsRespGraphs.
        :rtype: bool
        """
        return self._enable_hyg

    @enable_hyg.setter
    def enable_hyg(self, enable_hyg):
        r"""Sets the enable_hyg of this ListGraphsRespGraphs.

        是否启用HyG，该参数只对千亿规格图生效。

        :param enable_hyg: The enable_hyg of this ListGraphsRespGraphs.
        :type enable_hyg: bool
        """
        self._enable_hyg = enable_hyg

    @property
    def traffic_ip_list(self):
        r"""Gets the traffic_ip_list of this ListGraphsRespGraphs.

        图实例私有网络访问物理地址列表。为了防止浮动IP切换造成业务闪断，我们推荐您通过轮询的方式使用物理IP访问图实例。

        :return: The traffic_ip_list of this ListGraphsRespGraphs.
        :rtype: list[str]
        """
        return self._traffic_ip_list

    @traffic_ip_list.setter
    def traffic_ip_list(self, traffic_ip_list):
        r"""Sets the traffic_ip_list of this ListGraphsRespGraphs.

        图实例私有网络访问物理地址列表。为了防止浮动IP切换造成业务闪断，我们推荐您通过轮询的方式使用物理IP访问图实例。

        :param traffic_ip_list: The traffic_ip_list of this ListGraphsRespGraphs.
        :type traffic_ip_list: list[str]
        """
        self._traffic_ip_list = traffic_ip_list

    @property
    def crypt_algorithm(self):
        r"""Gets the crypt_algorithm of this ListGraphsRespGraphs.

        图实例加密算法，取值为：  - generalCipher：国密算法 - SMcompatible：商密算法（兼容国际）

        :return: The crypt_algorithm of this ListGraphsRespGraphs.
        :rtype: str
        """
        return self._crypt_algorithm

    @crypt_algorithm.setter
    def crypt_algorithm(self, crypt_algorithm):
        r"""Sets the crypt_algorithm of this ListGraphsRespGraphs.

        图实例加密算法，取值为：  - generalCipher：国密算法 - SMcompatible：商密算法（兼容国际）

        :param crypt_algorithm: The crypt_algorithm of this ListGraphsRespGraphs.
        :type crypt_algorithm: str
        """
        self._crypt_algorithm = crypt_algorithm

    @property
    def enable_https(self):
        r"""Gets the enable_https of this ListGraphsRespGraphs.

        是否开启安全模式，开启安全模式会对性能有较大影响

        :return: The enable_https of this ListGraphsRespGraphs.
        :rtype: bool
        """
        return self._enable_https

    @enable_https.setter
    def enable_https(self, enable_https):
        r"""Sets the enable_https of this ListGraphsRespGraphs.

        是否开启安全模式，开启安全模式会对性能有较大影响

        :param enable_https: The enable_https of this ListGraphsRespGraphs.
        :type enable_https: bool
        """
        self._enable_https = enable_https

    @property
    def tags(self):
        r"""Gets the tags of this ListGraphsRespGraphs.

        标签列表，每个标签用<key,value>键值对表示。

        :return: The tags of this ListGraphsRespGraphs.
        :rtype: list[:class:`huaweicloudsdkges.v2.ListGraphsRespTags`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this ListGraphsRespGraphs.

        标签列表，每个标签用<key,value>键值对表示。

        :param tags: The tags of this ListGraphsRespGraphs.
        :type tags: list[:class:`huaweicloudsdkges.v2.ListGraphsRespTags`]
        """
        self._tags = tags

    @property
    def product_type(self):
        r"""Gets the product_type of this ListGraphsRespGraphs.

        图产品类型，取值为InMemory和Persistence，默认为InMemory，当graph_size_type_index取值为\"6\"时，默认为Persistence。  - InMemory：内存版 - Persistence：持久化版

        :return: The product_type of this ListGraphsRespGraphs.
        :rtype: str
        """
        return self._product_type

    @product_type.setter
    def product_type(self, product_type):
        r"""Sets the product_type of this ListGraphsRespGraphs.

        图产品类型，取值为InMemory和Persistence，默认为InMemory，当graph_size_type_index取值为\"6\"时，默认为Persistence。  - InMemory：内存版 - Persistence：持久化版

        :param product_type: The product_type of this ListGraphsRespGraphs.
        :type product_type: str
        """
        self._product_type = product_type

    @property
    def vertex_id_type(self):
        r"""Gets the vertex_id_type of this ListGraphsRespGraphs.

        :return: The vertex_id_type of this ListGraphsRespGraphs.
        :rtype: :class:`huaweicloudsdkges.v2.ListGraphsRespVertexIdType`
        """
        return self._vertex_id_type

    @vertex_id_type.setter
    def vertex_id_type(self, vertex_id_type):
        r"""Sets the vertex_id_type of this ListGraphsRespGraphs.

        :param vertex_id_type: The vertex_id_type of this ListGraphsRespGraphs.
        :type vertex_id_type: :class:`huaweicloudsdkges.v2.ListGraphsRespVertexIdType`
        """
        self._vertex_id_type = vertex_id_type

    @property
    def origin_graph_size_type_index(self):
        r"""Gets the origin_graph_size_type_index of this ListGraphsRespGraphs.

        图的初始规格。该参数从2.3.15版本后开始支持。

        :return: The origin_graph_size_type_index of this ListGraphsRespGraphs.
        :rtype: str
        """
        return self._origin_graph_size_type_index

    @origin_graph_size_type_index.setter
    def origin_graph_size_type_index(self, origin_graph_size_type_index):
        r"""Sets the origin_graph_size_type_index of this ListGraphsRespGraphs.

        图的初始规格。该参数从2.3.15版本后开始支持。

        :param origin_graph_size_type_index: The origin_graph_size_type_index of this ListGraphsRespGraphs.
        :type origin_graph_size_type_index: str
        """
        self._origin_graph_size_type_index = origin_graph_size_type_index

    @property
    def expand_time(self):
        r"""Gets the expand_time of this ListGraphsRespGraphs.

        图扩副本的时间。

        :return: The expand_time of this ListGraphsRespGraphs.
        :rtype: str
        """
        return self._expand_time

    @expand_time.setter
    def expand_time(self, expand_time):
        r"""Sets the expand_time of this ListGraphsRespGraphs.

        图扩副本的时间。

        :param expand_time: The expand_time of this ListGraphsRespGraphs.
        :type expand_time: str
        """
        self._expand_time = expand_time

    @property
    def resize_time(self):
        r"""Gets the resize_time of this ListGraphsRespGraphs.

        图扩容的时间。

        :return: The resize_time of this ListGraphsRespGraphs.
        :rtype: str
        """
        return self._resize_time

    @resize_time.setter
    def resize_time(self, resize_time):
        r"""Sets the resize_time of this ListGraphsRespGraphs.

        图扩容的时间。

        :param resize_time: The resize_time of this ListGraphsRespGraphs.
        :type resize_time: str
        """
        self._resize_time = resize_time

    @property
    def enable_multi_label(self):
        r"""Gets the enable_multi_label of this ListGraphsRespGraphs.

        是否启用多标签。

        :return: The enable_multi_label of this ListGraphsRespGraphs.
        :rtype: bool
        """
        return self._enable_multi_label

    @enable_multi_label.setter
    def enable_multi_label(self, enable_multi_label):
        r"""Sets the enable_multi_label of this ListGraphsRespGraphs.

        是否启用多标签。

        :param enable_multi_label: The enable_multi_label of this ListGraphsRespGraphs.
        :type enable_multi_label: bool
        """
        self._enable_multi_label = enable_multi_label

    @property
    def capacity_ratio(self):
        r"""Gets the capacity_ratio of this ListGraphsRespGraphs.

        图的容量倍率。只有持久化版百亿规格图支持该参数，该参数从2.3.18版本后开始支持。

        :return: The capacity_ratio of this ListGraphsRespGraphs.
        :rtype: int
        """
        return self._capacity_ratio

    @capacity_ratio.setter
    def capacity_ratio(self, capacity_ratio):
        r"""Sets the capacity_ratio of this ListGraphsRespGraphs.

        图的容量倍率。只有持久化版百亿规格图支持该参数，该参数从2.3.18版本后开始支持。

        :param capacity_ratio: The capacity_ratio of this ListGraphsRespGraphs.
        :type capacity_ratio: int
        """
        self._capacity_ratio = capacity_ratio

    @property
    def sort_key_type(self):
        r"""Gets the sort_key_type of this ListGraphsRespGraphs.

        图的sortKey类型，内存版图无此值。

        :return: The sort_key_type of this ListGraphsRespGraphs.
        :rtype: str
        """
        return self._sort_key_type

    @sort_key_type.setter
    def sort_key_type(self, sort_key_type):
        r"""Sets the sort_key_type of this ListGraphsRespGraphs.

        图的sortKey类型，内存版图无此值。

        :param sort_key_type: The sort_key_type of this ListGraphsRespGraphs.
        :type sort_key_type: str
        """
        self._sort_key_type = sort_key_type

    @property
    def enable_lts(self):
        r"""Gets the enable_lts of this ListGraphsRespGraphs.

        对接云服务LTS日志开启状态。  - true：日志对接开启中。 - false：日志对接关闭中。

        :return: The enable_lts of this ListGraphsRespGraphs.
        :rtype: bool
        """
        return self._enable_lts

    @enable_lts.setter
    def enable_lts(self, enable_lts):
        r"""Sets the enable_lts of this ListGraphsRespGraphs.

        对接云服务LTS日志开启状态。  - true：日志对接开启中。 - false：日志对接关闭中。

        :param enable_lts: The enable_lts of this ListGraphsRespGraphs.
        :type enable_lts: bool
        """
        self._enable_lts = enable_lts

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
        if not isinstance(other, ListGraphsRespGraphs):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
