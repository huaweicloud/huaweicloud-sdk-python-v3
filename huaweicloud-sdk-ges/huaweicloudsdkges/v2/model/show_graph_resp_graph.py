# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowGraphRespGraph:

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
        'enable_multi_label': 'bool'
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
        'enable_multi_label': 'enable_multi_label'
    }

    def __init__(self, id=None, name=None, created_by=None, is_multi_az=None, region_code=None, az_code=None, schema_path=None, edgeset_path=None, vertexset_path=None, edgeset_format=None, edgeset_default_label=None, vertexset_format=None, vertexset_default_label=None, data_store_version=None, sys_tags=None, status=None, action_progress=None, graph_size_type_index=None, vpc_id=None, subnet_id=None, security_group_id=None, replication=None, created=None, updated=None, private_ip=None, public_ip=None, arch=None, encrypted=None, master_key_id=None, master_key_name=None, enable_rbac=None, enable_full_text_index=None, enable_hyg=None, traffic_ip_list=None, crypt_algorithm=None, enable_https=None, tags=None, product_type=None, vertex_id_type=None, origin_graph_size_type_index=None, expand_time=None, resize_time=None, enable_multi_label=None):
        """ShowGraphRespGraph

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

    @property
    def id(self):
        """Gets the id of this ShowGraphRespGraph.

        图ID。

        :return: The id of this ShowGraphRespGraph.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShowGraphRespGraph.

        图ID。

        :param id: The id of this ShowGraphRespGraph.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ShowGraphRespGraph.

        图名称。

        :return: The name of this ShowGraphRespGraph.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ShowGraphRespGraph.

        图名称。

        :param name: The name of this ShowGraphRespGraph.
        :type name: str
        """
        self._name = name

    @property
    def created_by(self):
        """Gets the created_by of this ShowGraphRespGraph.

        图的创建人账号。

        :return: The created_by of this ShowGraphRespGraph.
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this ShowGraphRespGraph.

        图的创建人账号。

        :param created_by: The created_by of this ShowGraphRespGraph.
        :type created_by: str
        """
        self._created_by = created_by

    @property
    def is_multi_az(self):
        """Gets the is_multi_az of this ShowGraphRespGraph.

        是否支持跨AZ高可用。

        :return: The is_multi_az of this ShowGraphRespGraph.
        :rtype: str
        """
        return self._is_multi_az

    @is_multi_az.setter
    def is_multi_az(self, is_multi_az):
        """Sets the is_multi_az of this ShowGraphRespGraph.

        是否支持跨AZ高可用。

        :param is_multi_az: The is_multi_az of this ShowGraphRespGraph.
        :type is_multi_az: str
        """
        self._is_multi_az = is_multi_az

    @property
    def region_code(self):
        """Gets the region_code of this ShowGraphRespGraph.

        域编码。

        :return: The region_code of this ShowGraphRespGraph.
        :rtype: str
        """
        return self._region_code

    @region_code.setter
    def region_code(self, region_code):
        """Sets the region_code of this ShowGraphRespGraph.

        域编码。

        :param region_code: The region_code of this ShowGraphRespGraph.
        :type region_code: str
        """
        self._region_code = region_code

    @property
    def az_code(self):
        """Gets the az_code of this ShowGraphRespGraph.

        可用区编码。

        :return: The az_code of this ShowGraphRespGraph.
        :rtype: str
        """
        return self._az_code

    @az_code.setter
    def az_code(self, az_code):
        """Sets the az_code of this ShowGraphRespGraph.

        可用区编码。

        :param az_code: The az_code of this ShowGraphRespGraph.
        :type az_code: str
        """
        self._az_code = az_code

    @property
    def schema_path(self):
        """Gets the schema_path of this ShowGraphRespGraph.

        元数据文件路径。

        :return: The schema_path of this ShowGraphRespGraph.
        :rtype: list[:class:`huaweicloudsdkges.v2.ListGraphsRespSchemaPath`]
        """
        return self._schema_path

    @schema_path.setter
    def schema_path(self, schema_path):
        """Sets the schema_path of this ShowGraphRespGraph.

        元数据文件路径。

        :param schema_path: The schema_path of this ShowGraphRespGraph.
        :type schema_path: list[:class:`huaweicloudsdkges.v2.ListGraphsRespSchemaPath`]
        """
        self._schema_path = schema_path

    @property
    def edgeset_path(self):
        """Gets the edgeset_path of this ShowGraphRespGraph.

        边数据集OBS路径。

        :return: The edgeset_path of this ShowGraphRespGraph.
        :rtype: list[:class:`huaweicloudsdkges.v2.ListGraphsRespSchemaPath`]
        """
        return self._edgeset_path

    @edgeset_path.setter
    def edgeset_path(self, edgeset_path):
        """Sets the edgeset_path of this ShowGraphRespGraph.

        边数据集OBS路径。

        :param edgeset_path: The edgeset_path of this ShowGraphRespGraph.
        :type edgeset_path: list[:class:`huaweicloudsdkges.v2.ListGraphsRespSchemaPath`]
        """
        self._edgeset_path = edgeset_path

    @property
    def vertexset_path(self):
        """Gets the vertexset_path of this ShowGraphRespGraph.

        点数据集OBS路径。

        :return: The vertexset_path of this ShowGraphRespGraph.
        :rtype: list[:class:`huaweicloudsdkges.v2.ListGraphsRespSchemaPath`]
        """
        return self._vertexset_path

    @vertexset_path.setter
    def vertexset_path(self, vertexset_path):
        """Sets the vertexset_path of this ShowGraphRespGraph.

        点数据集OBS路径。

        :param vertexset_path: The vertexset_path of this ShowGraphRespGraph.
        :type vertexset_path: list[:class:`huaweicloudsdkges.v2.ListGraphsRespSchemaPath`]
        """
        self._vertexset_path = vertexset_path

    @property
    def edgeset_format(self):
        """Gets the edgeset_format of this ShowGraphRespGraph.

        边数据集文件格式。

        :return: The edgeset_format of this ShowGraphRespGraph.
        :rtype: str
        """
        return self._edgeset_format

    @edgeset_format.setter
    def edgeset_format(self, edgeset_format):
        """Sets the edgeset_format of this ShowGraphRespGraph.

        边数据集文件格式。

        :param edgeset_format: The edgeset_format of this ShowGraphRespGraph.
        :type edgeset_format: str
        """
        self._edgeset_format = edgeset_format

    @property
    def edgeset_default_label(self):
        """Gets the edgeset_default_label of this ShowGraphRespGraph.

        边数据集文件默认Label。

        :return: The edgeset_default_label of this ShowGraphRespGraph.
        :rtype: str
        """
        return self._edgeset_default_label

    @edgeset_default_label.setter
    def edgeset_default_label(self, edgeset_default_label):
        """Sets the edgeset_default_label of this ShowGraphRespGraph.

        边数据集文件默认Label。

        :param edgeset_default_label: The edgeset_default_label of this ShowGraphRespGraph.
        :type edgeset_default_label: str
        """
        self._edgeset_default_label = edgeset_default_label

    @property
    def vertexset_format(self):
        """Gets the vertexset_format of this ShowGraphRespGraph.

        点数据集文件格式。

        :return: The vertexset_format of this ShowGraphRespGraph.
        :rtype: str
        """
        return self._vertexset_format

    @vertexset_format.setter
    def vertexset_format(self, vertexset_format):
        """Sets the vertexset_format of this ShowGraphRespGraph.

        点数据集文件格式。

        :param vertexset_format: The vertexset_format of this ShowGraphRespGraph.
        :type vertexset_format: str
        """
        self._vertexset_format = vertexset_format

    @property
    def vertexset_default_label(self):
        """Gets the vertexset_default_label of this ShowGraphRespGraph.

        点数据集文件默认Label。

        :return: The vertexset_default_label of this ShowGraphRespGraph.
        :rtype: str
        """
        return self._vertexset_default_label

    @vertexset_default_label.setter
    def vertexset_default_label(self, vertexset_default_label):
        """Sets the vertexset_default_label of this ShowGraphRespGraph.

        点数据集文件默认Label。

        :param vertexset_default_label: The vertexset_default_label of this ShowGraphRespGraph.
        :type vertexset_default_label: str
        """
        self._vertexset_default_label = vertexset_default_label

    @property
    def data_store_version(self):
        """Gets the data_store_version of this ShowGraphRespGraph.

        图版本。

        :return: The data_store_version of this ShowGraphRespGraph.
        :rtype: str
        """
        return self._data_store_version

    @data_store_version.setter
    def data_store_version(self, data_store_version):
        """Sets the data_store_version of this ShowGraphRespGraph.

        图版本。

        :param data_store_version: The data_store_version of this ShowGraphRespGraph.
        :type data_store_version: str
        """
        self._data_store_version = data_store_version

    @property
    def sys_tags(self):
        """Gets the sys_tags of this ShowGraphRespGraph.

        企业项目信息，如果未指定则不开启，默认不开启。

        :return: The sys_tags of this ShowGraphRespGraph.
        :rtype: list[str]
        """
        return self._sys_tags

    @sys_tags.setter
    def sys_tags(self, sys_tags):
        """Sets the sys_tags of this ShowGraphRespGraph.

        企业项目信息，如果未指定则不开启，默认不开启。

        :param sys_tags: The sys_tags of this ShowGraphRespGraph.
        :type sys_tags: list[str]
        """
        self._sys_tags = sys_tags

    @property
    def status(self):
        """Gets the status of this ShowGraphRespGraph.

        图的状态码。  - 100：准备中 - 200：运行中 - 201：升级中 - 202：导入中 - 203：回滚中 - 204：导出中 - 205：清空中 - 206：扩容准备中 - 207：扩容中 - 208：扩容回退中 - 210：扩副本准备中 - 211：扩副本中 - 300：故障 - 303：创建失败 - 400：被删除 - 800：已冻结 - 900：停止 - 901：停止中 - 920：启动中

        :return: The status of this ShowGraphRespGraph.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShowGraphRespGraph.

        图的状态码。  - 100：准备中 - 200：运行中 - 201：升级中 - 202：导入中 - 203：回滚中 - 204：导出中 - 205：清空中 - 206：扩容准备中 - 207：扩容中 - 208：扩容回退中 - 210：扩副本准备中 - 211：扩副本中 - 300：故障 - 303：创建失败 - 400：被删除 - 800：已冻结 - 900：停止 - 901：停止中 - 920：启动中

        :param status: The status of this ShowGraphRespGraph.
        :type status: str
        """
        self._status = status

    @property
    def action_progress(self):
        """Gets the action_progress of this ShowGraphRespGraph.

        图创建进度百分比。 > 只有图状态码为100时返回该字段。

        :return: The action_progress of this ShowGraphRespGraph.
        :rtype: str
        """
        return self._action_progress

    @action_progress.setter
    def action_progress(self, action_progress):
        """Sets the action_progress of this ShowGraphRespGraph.

        图创建进度百分比。 > 只有图状态码为100时返回该字段。

        :param action_progress: The action_progress of this ShowGraphRespGraph.
        :type action_progress: str
        """
        self._action_progress = action_progress

    @property
    def graph_size_type_index(self):
        """Gets the graph_size_type_index of this ShowGraphRespGraph.

        图规模类型索引。  - 0：一万边 - 1：百万边 - 2：千万边 - 3：一亿边 - 4：十亿边 - 5：百亿边 - 6：千亿边 - 401：十亿增强边

        :return: The graph_size_type_index of this ShowGraphRespGraph.
        :rtype: str
        """
        return self._graph_size_type_index

    @graph_size_type_index.setter
    def graph_size_type_index(self, graph_size_type_index):
        """Sets the graph_size_type_index of this ShowGraphRespGraph.

        图规模类型索引。  - 0：一万边 - 1：百万边 - 2：千万边 - 3：一亿边 - 4：十亿边 - 5：百亿边 - 6：千亿边 - 401：十亿增强边

        :param graph_size_type_index: The graph_size_type_index of this ShowGraphRespGraph.
        :type graph_size_type_index: str
        """
        self._graph_size_type_index = graph_size_type_index

    @property
    def vpc_id(self):
        """Gets the vpc_id of this ShowGraphRespGraph.

        虚拟私有云ID。

        :return: The vpc_id of this ShowGraphRespGraph.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this ShowGraphRespGraph.

        虚拟私有云ID。

        :param vpc_id: The vpc_id of this ShowGraphRespGraph.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def subnet_id(self):
        """Gets the subnet_id of this ShowGraphRespGraph.

        指定虚拟私有云下的子网ID。

        :return: The subnet_id of this ShowGraphRespGraph.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this ShowGraphRespGraph.

        指定虚拟私有云下的子网ID。

        :param subnet_id: The subnet_id of this ShowGraphRespGraph.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def security_group_id(self):
        """Gets the security_group_id of this ShowGraphRespGraph.

        安全组ID。

        :return: The security_group_id of this ShowGraphRespGraph.
        :rtype: str
        """
        return self._security_group_id

    @security_group_id.setter
    def security_group_id(self, security_group_id):
        """Sets the security_group_id of this ShowGraphRespGraph.

        安全组ID。

        :param security_group_id: The security_group_id of this ShowGraphRespGraph.
        :type security_group_id: str
        """
        self._security_group_id = security_group_id

    @property
    def replication(self):
        """Gets the replication of this ShowGraphRespGraph.

        副本个数，默认为1。

        :return: The replication of this ShowGraphRespGraph.
        :rtype: int
        """
        return self._replication

    @replication.setter
    def replication(self, replication):
        """Sets the replication of this ShowGraphRespGraph.

        副本个数，默认为1。

        :param replication: The replication of this ShowGraphRespGraph.
        :type replication: int
        """
        self._replication = replication

    @property
    def created(self):
        """Gets the created of this ShowGraphRespGraph.

        图创建时间。

        :return: The created of this ShowGraphRespGraph.
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this ShowGraphRespGraph.

        图创建时间。

        :param created: The created of this ShowGraphRespGraph.
        :type created: str
        """
        self._created = created

    @property
    def updated(self):
        """Gets the updated of this ShowGraphRespGraph.

        图更新时间。

        :return: The updated of this ShowGraphRespGraph.
        :rtype: str
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this ShowGraphRespGraph.

        图更新时间。

        :param updated: The updated of this ShowGraphRespGraph.
        :type updated: str
        """
        self._updated = updated

    @property
    def private_ip(self):
        """Gets the private_ip of this ShowGraphRespGraph.

        图实例私有网络访问浮动IP地址，通过该IP用户可以通过私有网络中已部署的弹性云服务器对图实例进行访问。

        :return: The private_ip of this ShowGraphRespGraph.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        """Sets the private_ip of this ShowGraphRespGraph.

        图实例私有网络访问浮动IP地址，通过该IP用户可以通过私有网络中已部署的弹性云服务器对图实例进行访问。

        :param private_ip: The private_ip of this ShowGraphRespGraph.
        :type private_ip: str
        """
        self._private_ip = private_ip

    @property
    def public_ip(self):
        """Gets the public_ip of this ShowGraphRespGraph.

        图实例公网访问地址，通过该IP用户可以从互联网对图实例进行访问。

        :return: The public_ip of this ShowGraphRespGraph.
        :rtype: str
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        """Sets the public_ip of this ShowGraphRespGraph.

        图实例公网访问地址，通过该IP用户可以从互联网对图实例进行访问。

        :param public_ip: The public_ip of this ShowGraphRespGraph.
        :type public_ip: str
        """
        self._public_ip = public_ip

    @property
    def arch(self):
        """Gets the arch of this ShowGraphRespGraph.

        图实例CPU架构类型，取值为x86_64和aarch64。

        :return: The arch of this ShowGraphRespGraph.
        :rtype: str
        """
        return self._arch

    @arch.setter
    def arch(self, arch):
        """Sets the arch of this ShowGraphRespGraph.

        图实例CPU架构类型，取值为x86_64和aarch64。

        :param arch: The arch of this ShowGraphRespGraph.
        :type arch: str
        """
        self._arch = arch

    @property
    def encrypted(self):
        """Gets the encrypted of this ShowGraphRespGraph.

        是否加密。默认值为“false”，默认不加密。

        :return: The encrypted of this ShowGraphRespGraph.
        :rtype: bool
        """
        return self._encrypted

    @encrypted.setter
    def encrypted(self, encrypted):
        """Sets the encrypted of this ShowGraphRespGraph.

        是否加密。默认值为“false”，默认不加密。

        :param encrypted: The encrypted of this ShowGraphRespGraph.
        :type encrypted: bool
        """
        self._encrypted = encrypted

    @property
    def master_key_id(self):
        """Gets the master_key_id of this ShowGraphRespGraph.

        用户主密钥ID。

        :return: The master_key_id of this ShowGraphRespGraph.
        :rtype: str
        """
        return self._master_key_id

    @master_key_id.setter
    def master_key_id(self, master_key_id):
        """Sets the master_key_id of this ShowGraphRespGraph.

        用户主密钥ID。

        :param master_key_id: The master_key_id of this ShowGraphRespGraph.
        :type master_key_id: str
        """
        self._master_key_id = master_key_id

    @property
    def master_key_name(self):
        """Gets the master_key_name of this ShowGraphRespGraph.

        用户主密钥名称。

        :return: The master_key_name of this ShowGraphRespGraph.
        :rtype: str
        """
        return self._master_key_name

    @master_key_name.setter
    def master_key_name(self, master_key_name):
        """Sets the master_key_name of this ShowGraphRespGraph.

        用户主密钥名称。

        :param master_key_name: The master_key_name of this ShowGraphRespGraph.
        :type master_key_name: str
        """
        self._master_key_name = master_key_name

    @property
    def enable_rbac(self):
        """Gets the enable_rbac of this ShowGraphRespGraph.

        是否启用细粒度权限控制。

        :return: The enable_rbac of this ShowGraphRespGraph.
        :rtype: bool
        """
        return self._enable_rbac

    @enable_rbac.setter
    def enable_rbac(self, enable_rbac):
        """Sets the enable_rbac of this ShowGraphRespGraph.

        是否启用细粒度权限控制。

        :param enable_rbac: The enable_rbac of this ShowGraphRespGraph.
        :type enable_rbac: bool
        """
        self._enable_rbac = enable_rbac

    @property
    def enable_full_text_index(self):
        """Gets the enable_full_text_index of this ShowGraphRespGraph.

        是否启用全文索引。

        :return: The enable_full_text_index of this ShowGraphRespGraph.
        :rtype: bool
        """
        return self._enable_full_text_index

    @enable_full_text_index.setter
    def enable_full_text_index(self, enable_full_text_index):
        """Sets the enable_full_text_index of this ShowGraphRespGraph.

        是否启用全文索引。

        :param enable_full_text_index: The enable_full_text_index of this ShowGraphRespGraph.
        :type enable_full_text_index: bool
        """
        self._enable_full_text_index = enable_full_text_index

    @property
    def enable_hyg(self):
        """Gets the enable_hyg of this ShowGraphRespGraph.

        是否启用HyG，该参数只对千亿规格图生效。

        :return: The enable_hyg of this ShowGraphRespGraph.
        :rtype: bool
        """
        return self._enable_hyg

    @enable_hyg.setter
    def enable_hyg(self, enable_hyg):
        """Sets the enable_hyg of this ShowGraphRespGraph.

        是否启用HyG，该参数只对千亿规格图生效。

        :param enable_hyg: The enable_hyg of this ShowGraphRespGraph.
        :type enable_hyg: bool
        """
        self._enable_hyg = enable_hyg

    @property
    def traffic_ip_list(self):
        """Gets the traffic_ip_list of this ShowGraphRespGraph.

        图实例私有网络访问物理地址列表。为了防止浮动IP切换造成业务闪断，我们推荐您通过轮询的方式使用物理IP访问图实例。

        :return: The traffic_ip_list of this ShowGraphRespGraph.
        :rtype: list[str]
        """
        return self._traffic_ip_list

    @traffic_ip_list.setter
    def traffic_ip_list(self, traffic_ip_list):
        """Sets the traffic_ip_list of this ShowGraphRespGraph.

        图实例私有网络访问物理地址列表。为了防止浮动IP切换造成业务闪断，我们推荐您通过轮询的方式使用物理IP访问图实例。

        :param traffic_ip_list: The traffic_ip_list of this ShowGraphRespGraph.
        :type traffic_ip_list: list[str]
        """
        self._traffic_ip_list = traffic_ip_list

    @property
    def crypt_algorithm(self):
        """Gets the crypt_algorithm of this ShowGraphRespGraph.

        图实例加密算法，取值为：  - generalCipher：国密算法 - SMcompatible：商密算法（兼容国际）

        :return: The crypt_algorithm of this ShowGraphRespGraph.
        :rtype: str
        """
        return self._crypt_algorithm

    @crypt_algorithm.setter
    def crypt_algorithm(self, crypt_algorithm):
        """Sets the crypt_algorithm of this ShowGraphRespGraph.

        图实例加密算法，取值为：  - generalCipher：国密算法 - SMcompatible：商密算法（兼容国际）

        :param crypt_algorithm: The crypt_algorithm of this ShowGraphRespGraph.
        :type crypt_algorithm: str
        """
        self._crypt_algorithm = crypt_algorithm

    @property
    def enable_https(self):
        """Gets the enable_https of this ShowGraphRespGraph.

        是否开启安全模式，开启安全模式会对性能有较大影响

        :return: The enable_https of this ShowGraphRespGraph.
        :rtype: bool
        """
        return self._enable_https

    @enable_https.setter
    def enable_https(self, enable_https):
        """Sets the enable_https of this ShowGraphRespGraph.

        是否开启安全模式，开启安全模式会对性能有较大影响

        :param enable_https: The enable_https of this ShowGraphRespGraph.
        :type enable_https: bool
        """
        self._enable_https = enable_https

    @property
    def tags(self):
        """Gets the tags of this ShowGraphRespGraph.

        标签列表，每个标签用<key,value>键值对表示。

        :return: The tags of this ShowGraphRespGraph.
        :rtype: list[:class:`huaweicloudsdkges.v2.ListGraphsRespTags`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ShowGraphRespGraph.

        标签列表，每个标签用<key,value>键值对表示。

        :param tags: The tags of this ShowGraphRespGraph.
        :type tags: list[:class:`huaweicloudsdkges.v2.ListGraphsRespTags`]
        """
        self._tags = tags

    @property
    def product_type(self):
        """Gets the product_type of this ShowGraphRespGraph.

        图产品类型，取值为InMemory和Persistence，默认为InMemory，当graph_size_type_index取值为\"6\"时，默认为Persistence。  - InMemory：内存版 - Persistence：持久化版

        :return: The product_type of this ShowGraphRespGraph.
        :rtype: str
        """
        return self._product_type

    @product_type.setter
    def product_type(self, product_type):
        """Sets the product_type of this ShowGraphRespGraph.

        图产品类型，取值为InMemory和Persistence，默认为InMemory，当graph_size_type_index取值为\"6\"时，默认为Persistence。  - InMemory：内存版 - Persistence：持久化版

        :param product_type: The product_type of this ShowGraphRespGraph.
        :type product_type: str
        """
        self._product_type = product_type

    @property
    def vertex_id_type(self):
        """Gets the vertex_id_type of this ShowGraphRespGraph.

        :return: The vertex_id_type of this ShowGraphRespGraph.
        :rtype: :class:`huaweicloudsdkges.v2.ListGraphsRespVertexIdType`
        """
        return self._vertex_id_type

    @vertex_id_type.setter
    def vertex_id_type(self, vertex_id_type):
        """Sets the vertex_id_type of this ShowGraphRespGraph.

        :param vertex_id_type: The vertex_id_type of this ShowGraphRespGraph.
        :type vertex_id_type: :class:`huaweicloudsdkges.v2.ListGraphsRespVertexIdType`
        """
        self._vertex_id_type = vertex_id_type

    @property
    def origin_graph_size_type_index(self):
        """Gets the origin_graph_size_type_index of this ShowGraphRespGraph.

        图的初始规格。该参数从2.3.15版本后开始支持。

        :return: The origin_graph_size_type_index of this ShowGraphRespGraph.
        :rtype: str
        """
        return self._origin_graph_size_type_index

    @origin_graph_size_type_index.setter
    def origin_graph_size_type_index(self, origin_graph_size_type_index):
        """Sets the origin_graph_size_type_index of this ShowGraphRespGraph.

        图的初始规格。该参数从2.3.15版本后开始支持。

        :param origin_graph_size_type_index: The origin_graph_size_type_index of this ShowGraphRespGraph.
        :type origin_graph_size_type_index: str
        """
        self._origin_graph_size_type_index = origin_graph_size_type_index

    @property
    def expand_time(self):
        """Gets the expand_time of this ShowGraphRespGraph.

        图扩副本的时间。

        :return: The expand_time of this ShowGraphRespGraph.
        :rtype: str
        """
        return self._expand_time

    @expand_time.setter
    def expand_time(self, expand_time):
        """Sets the expand_time of this ShowGraphRespGraph.

        图扩副本的时间。

        :param expand_time: The expand_time of this ShowGraphRespGraph.
        :type expand_time: str
        """
        self._expand_time = expand_time

    @property
    def resize_time(self):
        """Gets the resize_time of this ShowGraphRespGraph.

        图扩容的时间。

        :return: The resize_time of this ShowGraphRespGraph.
        :rtype: str
        """
        return self._resize_time

    @resize_time.setter
    def resize_time(self, resize_time):
        """Sets the resize_time of this ShowGraphRespGraph.

        图扩容的时间。

        :param resize_time: The resize_time of this ShowGraphRespGraph.
        :type resize_time: str
        """
        self._resize_time = resize_time

    @property
    def enable_multi_label(self):
        """Gets the enable_multi_label of this ShowGraphRespGraph.

        是否启用多标签。

        :return: The enable_multi_label of this ShowGraphRespGraph.
        :rtype: bool
        """
        return self._enable_multi_label

    @enable_multi_label.setter
    def enable_multi_label(self, enable_multi_label):
        """Sets the enable_multi_label of this ShowGraphRespGraph.

        是否启用多标签。

        :param enable_multi_label: The enable_multi_label of this ShowGraphRespGraph.
        :type enable_multi_label: bool
        """
        self._enable_multi_label = enable_multi_label

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
        if not isinstance(other, ShowGraphRespGraph):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
