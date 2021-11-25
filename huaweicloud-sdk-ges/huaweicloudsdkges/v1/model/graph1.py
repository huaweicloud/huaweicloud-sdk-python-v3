# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Graph1:


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
        'schema_path': 'list[SchemaPath1]',
        'edgeset_path': 'list[EdgesetPath1]',
        'edgeset_format': 'str',
        'edgeset_default_label': 'str',
        'vertexset_path': 'list[VertexsetPath1]',
        'vertexset_format': 'str',
        'vertexset_default_label': 'str',
        'data_store_version': 'str',
        'sys_tags': 'list[SysTagsRes]',
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
        'enable_fulltext_index': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'created_by': 'createdBy',
        'is_multi_az': 'isMultiAz',
        'region_code': 'regionCode',
        'az_code': 'azCode',
        'schema_path': 'schemaPath',
        'edgeset_path': 'edgesetPath',
        'edgeset_format': 'edgesetFormat',
        'edgeset_default_label': 'edgesetDefaultLabel',
        'vertexset_path': 'vertexsetPath',
        'vertexset_format': 'vertexsetFormat',
        'vertexset_default_label': 'vertexsetDefaultLabel',
        'data_store_version': 'dataStoreVersion',
        'sys_tags': 'sys_tags',
        'status': 'status',
        'action_progress': 'actionProgress',
        'graph_size_type_index': 'graphSizeTypeIndex',
        'vpc_id': 'vpcId',
        'subnet_id': 'subnetId',
        'security_group_id': 'securityGroupId',
        'replication': 'replication',
        'created': 'created',
        'updated': 'updated',
        'private_ip': 'privateIp',
        'public_ip': 'publicIp',
        'arch': 'arch',
        'encrypted': 'encrypted',
        'master_key_id': 'masterKeyId',
        'master_key_name': 'masterKeyName',
        'enable_rbac': 'enableRBAC',
        'enable_fulltext_index': 'enableFulltextIndex'
    }

    def __init__(self, id=None, name=None, created_by=None, is_multi_az=None, region_code=None, az_code=None, schema_path=None, edgeset_path=None, edgeset_format=None, edgeset_default_label=None, vertexset_path=None, vertexset_format=None, vertexset_default_label=None, data_store_version=None, sys_tags=None, status=None, action_progress=None, graph_size_type_index=None, vpc_id=None, subnet_id=None, security_group_id=None, replication=None, created=None, updated=None, private_ip=None, public_ip=None, arch=None, encrypted=None, master_key_id=None, master_key_name=None, enable_rbac=None, enable_fulltext_index=None):
        """Graph1 - a model defined in huaweicloud sdk"""
        
        

        self._id = None
        self._name = None
        self._created_by = None
        self._is_multi_az = None
        self._region_code = None
        self._az_code = None
        self._schema_path = None
        self._edgeset_path = None
        self._edgeset_format = None
        self._edgeset_default_label = None
        self._vertexset_path = None
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
        self._enable_fulltext_index = None
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
        if edgeset_format is not None:
            self.edgeset_format = edgeset_format
        if edgeset_default_label is not None:
            self.edgeset_default_label = edgeset_default_label
        if vertexset_path is not None:
            self.vertexset_path = vertexset_path
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
        if enable_fulltext_index is not None:
            self.enable_fulltext_index = enable_fulltext_index

    @property
    def id(self):
        """Gets the id of this Graph1.

        图ID。

        :return: The id of this Graph1.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Graph1.

        图ID。

        :param id: The id of this Graph1.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this Graph1.

        图名称。

        :return: The name of this Graph1.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Graph1.

        图名称。

        :param name: The name of this Graph1.
        :type: str
        """
        self._name = name

    @property
    def created_by(self):
        """Gets the created_by of this Graph1.

        图的创建人账号。

        :return: The created_by of this Graph1.
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this Graph1.

        图的创建人账号。

        :param created_by: The created_by of this Graph1.
        :type: str
        """
        self._created_by = created_by

    @property
    def is_multi_az(self):
        """Gets the is_multi_az of this Graph1.

        是否支持跨AZ高可用。

        :return: The is_multi_az of this Graph1.
        :rtype: str
        """
        return self._is_multi_az

    @is_multi_az.setter
    def is_multi_az(self, is_multi_az):
        """Sets the is_multi_az of this Graph1.

        是否支持跨AZ高可用。

        :param is_multi_az: The is_multi_az of this Graph1.
        :type: str
        """
        self._is_multi_az = is_multi_az

    @property
    def region_code(self):
        """Gets the region_code of this Graph1.

        域编码。

        :return: The region_code of this Graph1.
        :rtype: str
        """
        return self._region_code

    @region_code.setter
    def region_code(self, region_code):
        """Sets the region_code of this Graph1.

        域编码。

        :param region_code: The region_code of this Graph1.
        :type: str
        """
        self._region_code = region_code

    @property
    def az_code(self):
        """Gets the az_code of this Graph1.

        可用区编码。

        :return: The az_code of this Graph1.
        :rtype: str
        """
        return self._az_code

    @az_code.setter
    def az_code(self, az_code):
        """Sets the az_code of this Graph1.

        可用区编码。

        :param az_code: The az_code of this Graph1.
        :type: str
        """
        self._az_code = az_code

    @property
    def schema_path(self):
        """Gets the schema_path of this Graph1.

        元数据文件路径。

        :return: The schema_path of this Graph1.
        :rtype: list[SchemaPath1]
        """
        return self._schema_path

    @schema_path.setter
    def schema_path(self, schema_path):
        """Sets the schema_path of this Graph1.

        元数据文件路径。

        :param schema_path: The schema_path of this Graph1.
        :type: list[SchemaPath1]
        """
        self._schema_path = schema_path

    @property
    def edgeset_path(self):
        """Gets the edgeset_path of this Graph1.

        边数据集OBS路径。

        :return: The edgeset_path of this Graph1.
        :rtype: list[EdgesetPath1]
        """
        return self._edgeset_path

    @edgeset_path.setter
    def edgeset_path(self, edgeset_path):
        """Sets the edgeset_path of this Graph1.

        边数据集OBS路径。

        :param edgeset_path: The edgeset_path of this Graph1.
        :type: list[EdgesetPath1]
        """
        self._edgeset_path = edgeset_path

    @property
    def edgeset_format(self):
        """Gets the edgeset_format of this Graph1.

        边数据集文件格式。

        :return: The edgeset_format of this Graph1.
        :rtype: str
        """
        return self._edgeset_format

    @edgeset_format.setter
    def edgeset_format(self, edgeset_format):
        """Sets the edgeset_format of this Graph1.

        边数据集文件格式。

        :param edgeset_format: The edgeset_format of this Graph1.
        :type: str
        """
        self._edgeset_format = edgeset_format

    @property
    def edgeset_default_label(self):
        """Gets the edgeset_default_label of this Graph1.

        边数据集文件默认Label。

        :return: The edgeset_default_label of this Graph1.
        :rtype: str
        """
        return self._edgeset_default_label

    @edgeset_default_label.setter
    def edgeset_default_label(self, edgeset_default_label):
        """Sets the edgeset_default_label of this Graph1.

        边数据集文件默认Label。

        :param edgeset_default_label: The edgeset_default_label of this Graph1.
        :type: str
        """
        self._edgeset_default_label = edgeset_default_label

    @property
    def vertexset_path(self):
        """Gets the vertexset_path of this Graph1.

        点数据集OBS路径。

        :return: The vertexset_path of this Graph1.
        :rtype: list[VertexsetPath1]
        """
        return self._vertexset_path

    @vertexset_path.setter
    def vertexset_path(self, vertexset_path):
        """Sets the vertexset_path of this Graph1.

        点数据集OBS路径。

        :param vertexset_path: The vertexset_path of this Graph1.
        :type: list[VertexsetPath1]
        """
        self._vertexset_path = vertexset_path

    @property
    def vertexset_format(self):
        """Gets the vertexset_format of this Graph1.

        点数据集文件格式。

        :return: The vertexset_format of this Graph1.
        :rtype: str
        """
        return self._vertexset_format

    @vertexset_format.setter
    def vertexset_format(self, vertexset_format):
        """Sets the vertexset_format of this Graph1.

        点数据集文件格式。

        :param vertexset_format: The vertexset_format of this Graph1.
        :type: str
        """
        self._vertexset_format = vertexset_format

    @property
    def vertexset_default_label(self):
        """Gets the vertexset_default_label of this Graph1.

        点数据集文件默认Label。

        :return: The vertexset_default_label of this Graph1.
        :rtype: str
        """
        return self._vertexset_default_label

    @vertexset_default_label.setter
    def vertexset_default_label(self, vertexset_default_label):
        """Sets the vertexset_default_label of this Graph1.

        点数据集文件默认Label。

        :param vertexset_default_label: The vertexset_default_label of this Graph1.
        :type: str
        """
        self._vertexset_default_label = vertexset_default_label

    @property
    def data_store_version(self):
        """Gets the data_store_version of this Graph1.

        图版本。

        :return: The data_store_version of this Graph1.
        :rtype: str
        """
        return self._data_store_version

    @data_store_version.setter
    def data_store_version(self, data_store_version):
        """Sets the data_store_version of this Graph1.

        图版本。

        :param data_store_version: The data_store_version of this Graph1.
        :type: str
        """
        self._data_store_version = data_store_version

    @property
    def sys_tags(self):
        """Gets the sys_tags of this Graph1.

        企业项目信息，如果未指定则不开启，默认不开启。

        :return: The sys_tags of this Graph1.
        :rtype: list[SysTagsRes]
        """
        return self._sys_tags

    @sys_tags.setter
    def sys_tags(self, sys_tags):
        """Sets the sys_tags of this Graph1.

        企业项目信息，如果未指定则不开启，默认不开启。

        :param sys_tags: The sys_tags of this Graph1.
        :type: list[SysTagsRes]
        """
        self._sys_tags = sys_tags

    @property
    def status(self):
        """Gets the status of this Graph1.

        图的状态码。  - 100：准备中 - 200：运行中 - 201：升级中 - 202：导入中 - 203：回滚中 - 204：导出中 - 205：清空中 - 206：扩容准备中 - 207：扩容中 - 208：扩容回退中 - 300：故障 - 303：创建失败 - 400：被删除 - 800：已冻结 - 900：停止 - 901：停止中 - 920：启动中

        :return: The status of this Graph1.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Graph1.

        图的状态码。  - 100：准备中 - 200：运行中 - 201：升级中 - 202：导入中 - 203：回滚中 - 204：导出中 - 205：清空中 - 206：扩容准备中 - 207：扩容中 - 208：扩容回退中 - 300：故障 - 303：创建失败 - 400：被删除 - 800：已冻结 - 900：停止 - 901：停止中 - 920：启动中

        :param status: The status of this Graph1.
        :type: str
        """
        self._status = status

    @property
    def action_progress(self):
        """Gets the action_progress of this Graph1.

        图创建进度百分比。 >只有图状态码为100时返回该字段。

        :return: The action_progress of this Graph1.
        :rtype: str
        """
        return self._action_progress

    @action_progress.setter
    def action_progress(self, action_progress):
        """Sets the action_progress of this Graph1.

        图创建进度百分比。 >只有图状态码为100时返回该字段。

        :param action_progress: The action_progress of this Graph1.
        :type: str
        """
        self._action_progress = action_progress

    @property
    def graph_size_type_index(self):
        """Gets the graph_size_type_index of this Graph1.

        图规模类型索引。  - 0：一万边 - 1：百万边 - 2：千万边 - 3：一亿边 - 4：十亿边 - 5：百亿边 - 6：千亿边

        :return: The graph_size_type_index of this Graph1.
        :rtype: str
        """
        return self._graph_size_type_index

    @graph_size_type_index.setter
    def graph_size_type_index(self, graph_size_type_index):
        """Sets the graph_size_type_index of this Graph1.

        图规模类型索引。  - 0：一万边 - 1：百万边 - 2：千万边 - 3：一亿边 - 4：十亿边 - 5：百亿边 - 6：千亿边

        :param graph_size_type_index: The graph_size_type_index of this Graph1.
        :type: str
        """
        self._graph_size_type_index = graph_size_type_index

    @property
    def vpc_id(self):
        """Gets the vpc_id of this Graph1.

        虚拟私有云ID。

        :return: The vpc_id of this Graph1.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this Graph1.

        虚拟私有云ID。

        :param vpc_id: The vpc_id of this Graph1.
        :type: str
        """
        self._vpc_id = vpc_id

    @property
    def subnet_id(self):
        """Gets the subnet_id of this Graph1.

        指定虚拟私有云下的子网ID。

        :return: The subnet_id of this Graph1.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this Graph1.

        指定虚拟私有云下的子网ID。

        :param subnet_id: The subnet_id of this Graph1.
        :type: str
        """
        self._subnet_id = subnet_id

    @property
    def security_group_id(self):
        """Gets the security_group_id of this Graph1.

        安全组ID。

        :return: The security_group_id of this Graph1.
        :rtype: str
        """
        return self._security_group_id

    @security_group_id.setter
    def security_group_id(self, security_group_id):
        """Sets the security_group_id of this Graph1.

        安全组ID。

        :param security_group_id: The security_group_id of this Graph1.
        :type: str
        """
        self._security_group_id = security_group_id

    @property
    def replication(self):
        """Gets the replication of this Graph1.

        副本个数，默认为1。

        :return: The replication of this Graph1.
        :rtype: int
        """
        return self._replication

    @replication.setter
    def replication(self, replication):
        """Sets the replication of this Graph1.

        副本个数，默认为1。

        :param replication: The replication of this Graph1.
        :type: int
        """
        self._replication = replication

    @property
    def created(self):
        """Gets the created of this Graph1.

        图创建时间。

        :return: The created of this Graph1.
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this Graph1.

        图创建时间。

        :param created: The created of this Graph1.
        :type: str
        """
        self._created = created

    @property
    def updated(self):
        """Gets the updated of this Graph1.

        图更新时间。

        :return: The updated of this Graph1.
        :rtype: str
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this Graph1.

        图更新时间。

        :param updated: The updated of this Graph1.
        :type: str
        """
        self._updated = updated

    @property
    def private_ip(self):
        """Gets the private_ip of this Graph1.

        图实例私有网络访问地址，通过该IP用户可以通过私有网络中已部署的弹性云服务器对图实例进行访问。

        :return: The private_ip of this Graph1.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        """Sets the private_ip of this Graph1.

        图实例私有网络访问地址，通过该IP用户可以通过私有网络中已部署的弹性云服务器对图实例进行访问。

        :param private_ip: The private_ip of this Graph1.
        :type: str
        """
        self._private_ip = private_ip

    @property
    def public_ip(self):
        """Gets the public_ip of this Graph1.

        图实例公网访问地址，通过该IP用户可以从互联网对图实例进行访问。

        :return: The public_ip of this Graph1.
        :rtype: str
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        """Sets the public_ip of this Graph1.

        图实例公网访问地址，通过该IP用户可以从互联网对图实例进行访问。

        :param public_ip: The public_ip of this Graph1.
        :type: str
        """
        self._public_ip = public_ip

    @property
    def arch(self):
        """Gets the arch of this Graph1.

        图实例CPU架构类型，取值为x86_64和aarch64。

        :return: The arch of this Graph1.
        :rtype: str
        """
        return self._arch

    @arch.setter
    def arch(self, arch):
        """Sets the arch of this Graph1.

        图实例CPU架构类型，取值为x86_64和aarch64。

        :param arch: The arch of this Graph1.
        :type: str
        """
        self._arch = arch

    @property
    def encrypted(self):
        """Gets the encrypted of this Graph1.

        是否加密。默认值为“false”，默认不加密。

        :return: The encrypted of this Graph1.
        :rtype: bool
        """
        return self._encrypted

    @encrypted.setter
    def encrypted(self, encrypted):
        """Sets the encrypted of this Graph1.

        是否加密。默认值为“false”，默认不加密。

        :param encrypted: The encrypted of this Graph1.
        :type: bool
        """
        self._encrypted = encrypted

    @property
    def master_key_id(self):
        """Gets the master_key_id of this Graph1.

        用户主密钥ID。

        :return: The master_key_id of this Graph1.
        :rtype: str
        """
        return self._master_key_id

    @master_key_id.setter
    def master_key_id(self, master_key_id):
        """Sets the master_key_id of this Graph1.

        用户主密钥ID。

        :param master_key_id: The master_key_id of this Graph1.
        :type: str
        """
        self._master_key_id = master_key_id

    @property
    def master_key_name(self):
        """Gets the master_key_name of this Graph1.

        用户主密钥名称。

        :return: The master_key_name of this Graph1.
        :rtype: str
        """
        return self._master_key_name

    @master_key_name.setter
    def master_key_name(self, master_key_name):
        """Sets the master_key_name of this Graph1.

        用户主密钥名称。

        :param master_key_name: The master_key_name of this Graph1.
        :type: str
        """
        self._master_key_name = master_key_name

    @property
    def enable_rbac(self):
        """Gets the enable_rbac of this Graph1.

        是否启用细粒度权限控制。

        :return: The enable_rbac of this Graph1.
        :rtype: bool
        """
        return self._enable_rbac

    @enable_rbac.setter
    def enable_rbac(self, enable_rbac):
        """Sets the enable_rbac of this Graph1.

        是否启用细粒度权限控制。

        :param enable_rbac: The enable_rbac of this Graph1.
        :type: bool
        """
        self._enable_rbac = enable_rbac

    @property
    def enable_fulltext_index(self):
        """Gets the enable_fulltext_index of this Graph1.

        是否启用全文索引。

        :return: The enable_fulltext_index of this Graph1.
        :rtype: bool
        """
        return self._enable_fulltext_index

    @enable_fulltext_index.setter
    def enable_fulltext_index(self, enable_fulltext_index):
        """Sets the enable_fulltext_index of this Graph1.

        是否启用全文索引。

        :param enable_fulltext_index: The enable_fulltext_index of this Graph1.
        :type: bool
        """
        self._enable_fulltext_index = enable_fulltext_index

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
        if not isinstance(other, Graph1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
