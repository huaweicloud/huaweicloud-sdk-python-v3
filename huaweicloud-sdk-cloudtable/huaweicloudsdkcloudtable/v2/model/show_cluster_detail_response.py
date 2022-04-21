# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowClusterDetailResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'actions': 'list[str]',
        'datastore': 'Datastore',
        'enable_open_tsdb': 'bool',
        'enable_lemon': 'bool',
        'cluster_name': 'str',
        'cu_num': 'str',
        'tsd_num': 'str',
        'lemon_num': 'str',
        'storage_type': 'str',
        'storage_quota': 'str',
        'used_storage_size': 'str',
        'auth_mode': 'bool',
        'enable_dfv': 'bool',
        'updated': 'str',
        'created': 'str',
        'cluster_id': 'str',
        'status': 'str',
        'open_tsdb_link': 'str',
        'tsd_public_endpoint': 'str',
        'lemon_link': 'str',
        'zookeeper_link': 'str',
        'hbase_public_endpoint': 'str',
        'is_frozen': 'str',
        'vpc_id': 'str',
        'sub_net_id': 'str',
        'security_group_id': 'str',
        'availability_zone': 'str'
    }

    attribute_map = {
        'actions': 'actions',
        'datastore': 'datastore',
        'enable_open_tsdb': 'enable_openTSDB',
        'enable_lemon': 'enable_lemon',
        'cluster_name': 'cluster_name',
        'cu_num': 'cu_num',
        'tsd_num': 'tsd_num',
        'lemon_num': 'lemon_num',
        'storage_type': 'storage_type',
        'storage_quota': 'storage_quota',
        'used_storage_size': 'used_storage_size',
        'auth_mode': 'auth_mode',
        'enable_dfv': 'enable_dfv',
        'updated': 'updated',
        'created': 'created',
        'cluster_id': 'cluster_id',
        'status': 'status',
        'open_tsdb_link': 'openTSDB_link',
        'tsd_public_endpoint': 'tsd_public_endpoint',
        'lemon_link': 'lemon_link',
        'zookeeper_link': 'zookeeper_link',
        'hbase_public_endpoint': 'hbase_public_endpoint',
        'is_frozen': 'is_frozen',
        'vpc_id': 'vpc_id',
        'sub_net_id': 'sub_net_id',
        'security_group_id': 'security_group_id',
        'availability_zone': 'availability_zone'
    }

    def __init__(self, actions=None, datastore=None, enable_open_tsdb=None, enable_lemon=None, cluster_name=None, cu_num=None, tsd_num=None, lemon_num=None, storage_type=None, storage_quota=None, used_storage_size=None, auth_mode=None, enable_dfv=None, updated=None, created=None, cluster_id=None, status=None, open_tsdb_link=None, tsd_public_endpoint=None, lemon_link=None, zookeeper_link=None, hbase_public_endpoint=None, is_frozen=None, vpc_id=None, sub_net_id=None, security_group_id=None, availability_zone=None):
        """ShowClusterDetailResponse

        The model defined in huaweicloud sdk

        :param actions: 集群当前状态列表： - 创建中 - 扩容中 - 重启中 - 开启opentsdb - 扩容失败 - 重启失败 - 开启opentsdb失败
        :type actions: list[str]
        :param datastore: 
        :type datastore: :class:`huaweicloudsdkcloudtable.v2.Datastore`
        :param enable_open_tsdb: 是否打开openTSDB特性。 - false：不开启 - true：开启
        :type enable_open_tsdb: bool
        :param enable_lemon: 是否打开SQL查询特性。 - false：不开启 - true：开启
        :type enable_lemon: bool
        :param cluster_name: 集群名称。
        :type cluster_name: str
        :param cu_num: RegionServer个数。
        :type cu_num: str
        :param tsd_num: TSD节点个数。
        :type tsd_num: str
        :param lemon_num: Lemon节点个数。
        :type lemon_num: str
        :param storage_type: 集群底层存储类型： - OBS - HDFS
        :type storage_type: str
        :param storage_quota: 集群存储配额。
        :type storage_quota: str
        :param used_storage_size: 当前使用存储空间。
        :type used_storage_size: str
        :param auth_mode: 是否打开IAM认证。 - false：不开启 - true：开启
        :type auth_mode: bool
        :param enable_dfv: 是否打开dfv
        :type enable_dfv: bool
        :param updated: 集群更新时间。
        :type updated: str
        :param created: 集群创建时间。
        :type created: str
        :param cluster_id: 集群唯一标识，集群ID。
        :type cluster_id: str
        :param status: 集群当前状态： - 200：集群正常 - 300：集群异常 - 400：集群已删除 - 303：集群创建失败
        :type status: str
        :param open_tsdb_link: 内网OpenTSDB连接访问地址。
        :type open_tsdb_link: str
        :param tsd_public_endpoint: OpenTSDB公网endpoint地址
        :type tsd_public_endpoint: str
        :param lemon_link: 内网Lemon连接访问地址。
        :type lemon_link: str
        :param zookeeper_link: 内网ZooKeeper连接访问地址。
        :type zookeeper_link: str
        :param hbase_public_endpoint: 公网HBase连接访问地址。
        :type hbase_public_endpoint: str
        :param is_frozen: 集群是否被冻结。 - false：不冻结 - true：冻结
        :type is_frozen: str
        :param vpc_id: VPC ID，创建集群节点所在的虚拟私有ID。
        :type vpc_id: str
        :param sub_net_id: 子网ID，创建集群所在子网段。
        :type sub_net_id: str
        :param security_group_id: 安全组对应的ID。
        :type security_group_id: str
        :param availability_zone: 集群所属的可用区。
        :type availability_zone: str
        """
        
        super(ShowClusterDetailResponse, self).__init__()

        self._actions = None
        self._datastore = None
        self._enable_open_tsdb = None
        self._enable_lemon = None
        self._cluster_name = None
        self._cu_num = None
        self._tsd_num = None
        self._lemon_num = None
        self._storage_type = None
        self._storage_quota = None
        self._used_storage_size = None
        self._auth_mode = None
        self._enable_dfv = None
        self._updated = None
        self._created = None
        self._cluster_id = None
        self._status = None
        self._open_tsdb_link = None
        self._tsd_public_endpoint = None
        self._lemon_link = None
        self._zookeeper_link = None
        self._hbase_public_endpoint = None
        self._is_frozen = None
        self._vpc_id = None
        self._sub_net_id = None
        self._security_group_id = None
        self._availability_zone = None
        self.discriminator = None

        if actions is not None:
            self.actions = actions
        if datastore is not None:
            self.datastore = datastore
        if enable_open_tsdb is not None:
            self.enable_open_tsdb = enable_open_tsdb
        if enable_lemon is not None:
            self.enable_lemon = enable_lemon
        if cluster_name is not None:
            self.cluster_name = cluster_name
        if cu_num is not None:
            self.cu_num = cu_num
        if tsd_num is not None:
            self.tsd_num = tsd_num
        if lemon_num is not None:
            self.lemon_num = lemon_num
        if storage_type is not None:
            self.storage_type = storage_type
        if storage_quota is not None:
            self.storage_quota = storage_quota
        if used_storage_size is not None:
            self.used_storage_size = used_storage_size
        if auth_mode is not None:
            self.auth_mode = auth_mode
        if enable_dfv is not None:
            self.enable_dfv = enable_dfv
        if updated is not None:
            self.updated = updated
        if created is not None:
            self.created = created
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if status is not None:
            self.status = status
        if open_tsdb_link is not None:
            self.open_tsdb_link = open_tsdb_link
        if tsd_public_endpoint is not None:
            self.tsd_public_endpoint = tsd_public_endpoint
        if lemon_link is not None:
            self.lemon_link = lemon_link
        if zookeeper_link is not None:
            self.zookeeper_link = zookeeper_link
        if hbase_public_endpoint is not None:
            self.hbase_public_endpoint = hbase_public_endpoint
        if is_frozen is not None:
            self.is_frozen = is_frozen
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if sub_net_id is not None:
            self.sub_net_id = sub_net_id
        if security_group_id is not None:
            self.security_group_id = security_group_id
        if availability_zone is not None:
            self.availability_zone = availability_zone

    @property
    def actions(self):
        """Gets the actions of this ShowClusterDetailResponse.

        集群当前状态列表： - 创建中 - 扩容中 - 重启中 - 开启opentsdb - 扩容失败 - 重启失败 - 开启opentsdb失败

        :return: The actions of this ShowClusterDetailResponse.
        :rtype: list[str]
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        """Sets the actions of this ShowClusterDetailResponse.

        集群当前状态列表： - 创建中 - 扩容中 - 重启中 - 开启opentsdb - 扩容失败 - 重启失败 - 开启opentsdb失败

        :param actions: The actions of this ShowClusterDetailResponse.
        :type actions: list[str]
        """
        self._actions = actions

    @property
    def datastore(self):
        """Gets the datastore of this ShowClusterDetailResponse.


        :return: The datastore of this ShowClusterDetailResponse.
        :rtype: :class:`huaweicloudsdkcloudtable.v2.Datastore`
        """
        return self._datastore

    @datastore.setter
    def datastore(self, datastore):
        """Sets the datastore of this ShowClusterDetailResponse.


        :param datastore: The datastore of this ShowClusterDetailResponse.
        :type datastore: :class:`huaweicloudsdkcloudtable.v2.Datastore`
        """
        self._datastore = datastore

    @property
    def enable_open_tsdb(self):
        """Gets the enable_open_tsdb of this ShowClusterDetailResponse.

        是否打开openTSDB特性。 - false：不开启 - true：开启

        :return: The enable_open_tsdb of this ShowClusterDetailResponse.
        :rtype: bool
        """
        return self._enable_open_tsdb

    @enable_open_tsdb.setter
    def enable_open_tsdb(self, enable_open_tsdb):
        """Sets the enable_open_tsdb of this ShowClusterDetailResponse.

        是否打开openTSDB特性。 - false：不开启 - true：开启

        :param enable_open_tsdb: The enable_open_tsdb of this ShowClusterDetailResponse.
        :type enable_open_tsdb: bool
        """
        self._enable_open_tsdb = enable_open_tsdb

    @property
    def enable_lemon(self):
        """Gets the enable_lemon of this ShowClusterDetailResponse.

        是否打开SQL查询特性。 - false：不开启 - true：开启

        :return: The enable_lemon of this ShowClusterDetailResponse.
        :rtype: bool
        """
        return self._enable_lemon

    @enable_lemon.setter
    def enable_lemon(self, enable_lemon):
        """Sets the enable_lemon of this ShowClusterDetailResponse.

        是否打开SQL查询特性。 - false：不开启 - true：开启

        :param enable_lemon: The enable_lemon of this ShowClusterDetailResponse.
        :type enable_lemon: bool
        """
        self._enable_lemon = enable_lemon

    @property
    def cluster_name(self):
        """Gets the cluster_name of this ShowClusterDetailResponse.

        集群名称。

        :return: The cluster_name of this ShowClusterDetailResponse.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        """Sets the cluster_name of this ShowClusterDetailResponse.

        集群名称。

        :param cluster_name: The cluster_name of this ShowClusterDetailResponse.
        :type cluster_name: str
        """
        self._cluster_name = cluster_name

    @property
    def cu_num(self):
        """Gets the cu_num of this ShowClusterDetailResponse.

        RegionServer个数。

        :return: The cu_num of this ShowClusterDetailResponse.
        :rtype: str
        """
        return self._cu_num

    @cu_num.setter
    def cu_num(self, cu_num):
        """Sets the cu_num of this ShowClusterDetailResponse.

        RegionServer个数。

        :param cu_num: The cu_num of this ShowClusterDetailResponse.
        :type cu_num: str
        """
        self._cu_num = cu_num

    @property
    def tsd_num(self):
        """Gets the tsd_num of this ShowClusterDetailResponse.

        TSD节点个数。

        :return: The tsd_num of this ShowClusterDetailResponse.
        :rtype: str
        """
        return self._tsd_num

    @tsd_num.setter
    def tsd_num(self, tsd_num):
        """Sets the tsd_num of this ShowClusterDetailResponse.

        TSD节点个数。

        :param tsd_num: The tsd_num of this ShowClusterDetailResponse.
        :type tsd_num: str
        """
        self._tsd_num = tsd_num

    @property
    def lemon_num(self):
        """Gets the lemon_num of this ShowClusterDetailResponse.

        Lemon节点个数。

        :return: The lemon_num of this ShowClusterDetailResponse.
        :rtype: str
        """
        return self._lemon_num

    @lemon_num.setter
    def lemon_num(self, lemon_num):
        """Sets the lemon_num of this ShowClusterDetailResponse.

        Lemon节点个数。

        :param lemon_num: The lemon_num of this ShowClusterDetailResponse.
        :type lemon_num: str
        """
        self._lemon_num = lemon_num

    @property
    def storage_type(self):
        """Gets the storage_type of this ShowClusterDetailResponse.

        集群底层存储类型： - OBS - HDFS

        :return: The storage_type of this ShowClusterDetailResponse.
        :rtype: str
        """
        return self._storage_type

    @storage_type.setter
    def storage_type(self, storage_type):
        """Sets the storage_type of this ShowClusterDetailResponse.

        集群底层存储类型： - OBS - HDFS

        :param storage_type: The storage_type of this ShowClusterDetailResponse.
        :type storage_type: str
        """
        self._storage_type = storage_type

    @property
    def storage_quota(self):
        """Gets the storage_quota of this ShowClusterDetailResponse.

        集群存储配额。

        :return: The storage_quota of this ShowClusterDetailResponse.
        :rtype: str
        """
        return self._storage_quota

    @storage_quota.setter
    def storage_quota(self, storage_quota):
        """Sets the storage_quota of this ShowClusterDetailResponse.

        集群存储配额。

        :param storage_quota: The storage_quota of this ShowClusterDetailResponse.
        :type storage_quota: str
        """
        self._storage_quota = storage_quota

    @property
    def used_storage_size(self):
        """Gets the used_storage_size of this ShowClusterDetailResponse.

        当前使用存储空间。

        :return: The used_storage_size of this ShowClusterDetailResponse.
        :rtype: str
        """
        return self._used_storage_size

    @used_storage_size.setter
    def used_storage_size(self, used_storage_size):
        """Sets the used_storage_size of this ShowClusterDetailResponse.

        当前使用存储空间。

        :param used_storage_size: The used_storage_size of this ShowClusterDetailResponse.
        :type used_storage_size: str
        """
        self._used_storage_size = used_storage_size

    @property
    def auth_mode(self):
        """Gets the auth_mode of this ShowClusterDetailResponse.

        是否打开IAM认证。 - false：不开启 - true：开启

        :return: The auth_mode of this ShowClusterDetailResponse.
        :rtype: bool
        """
        return self._auth_mode

    @auth_mode.setter
    def auth_mode(self, auth_mode):
        """Sets the auth_mode of this ShowClusterDetailResponse.

        是否打开IAM认证。 - false：不开启 - true：开启

        :param auth_mode: The auth_mode of this ShowClusterDetailResponse.
        :type auth_mode: bool
        """
        self._auth_mode = auth_mode

    @property
    def enable_dfv(self):
        """Gets the enable_dfv of this ShowClusterDetailResponse.

        是否打开dfv

        :return: The enable_dfv of this ShowClusterDetailResponse.
        :rtype: bool
        """
        return self._enable_dfv

    @enable_dfv.setter
    def enable_dfv(self, enable_dfv):
        """Sets the enable_dfv of this ShowClusterDetailResponse.

        是否打开dfv

        :param enable_dfv: The enable_dfv of this ShowClusterDetailResponse.
        :type enable_dfv: bool
        """
        self._enable_dfv = enable_dfv

    @property
    def updated(self):
        """Gets the updated of this ShowClusterDetailResponse.

        集群更新时间。

        :return: The updated of this ShowClusterDetailResponse.
        :rtype: str
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this ShowClusterDetailResponse.

        集群更新时间。

        :param updated: The updated of this ShowClusterDetailResponse.
        :type updated: str
        """
        self._updated = updated

    @property
    def created(self):
        """Gets the created of this ShowClusterDetailResponse.

        集群创建时间。

        :return: The created of this ShowClusterDetailResponse.
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this ShowClusterDetailResponse.

        集群创建时间。

        :param created: The created of this ShowClusterDetailResponse.
        :type created: str
        """
        self._created = created

    @property
    def cluster_id(self):
        """Gets the cluster_id of this ShowClusterDetailResponse.

        集群唯一标识，集群ID。

        :return: The cluster_id of this ShowClusterDetailResponse.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this ShowClusterDetailResponse.

        集群唯一标识，集群ID。

        :param cluster_id: The cluster_id of this ShowClusterDetailResponse.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def status(self):
        """Gets the status of this ShowClusterDetailResponse.

        集群当前状态： - 200：集群正常 - 300：集群异常 - 400：集群已删除 - 303：集群创建失败

        :return: The status of this ShowClusterDetailResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShowClusterDetailResponse.

        集群当前状态： - 200：集群正常 - 300：集群异常 - 400：集群已删除 - 303：集群创建失败

        :param status: The status of this ShowClusterDetailResponse.
        :type status: str
        """
        self._status = status

    @property
    def open_tsdb_link(self):
        """Gets the open_tsdb_link of this ShowClusterDetailResponse.

        内网OpenTSDB连接访问地址。

        :return: The open_tsdb_link of this ShowClusterDetailResponse.
        :rtype: str
        """
        return self._open_tsdb_link

    @open_tsdb_link.setter
    def open_tsdb_link(self, open_tsdb_link):
        """Sets the open_tsdb_link of this ShowClusterDetailResponse.

        内网OpenTSDB连接访问地址。

        :param open_tsdb_link: The open_tsdb_link of this ShowClusterDetailResponse.
        :type open_tsdb_link: str
        """
        self._open_tsdb_link = open_tsdb_link

    @property
    def tsd_public_endpoint(self):
        """Gets the tsd_public_endpoint of this ShowClusterDetailResponse.

        OpenTSDB公网endpoint地址

        :return: The tsd_public_endpoint of this ShowClusterDetailResponse.
        :rtype: str
        """
        return self._tsd_public_endpoint

    @tsd_public_endpoint.setter
    def tsd_public_endpoint(self, tsd_public_endpoint):
        """Sets the tsd_public_endpoint of this ShowClusterDetailResponse.

        OpenTSDB公网endpoint地址

        :param tsd_public_endpoint: The tsd_public_endpoint of this ShowClusterDetailResponse.
        :type tsd_public_endpoint: str
        """
        self._tsd_public_endpoint = tsd_public_endpoint

    @property
    def lemon_link(self):
        """Gets the lemon_link of this ShowClusterDetailResponse.

        内网Lemon连接访问地址。

        :return: The lemon_link of this ShowClusterDetailResponse.
        :rtype: str
        """
        return self._lemon_link

    @lemon_link.setter
    def lemon_link(self, lemon_link):
        """Sets the lemon_link of this ShowClusterDetailResponse.

        内网Lemon连接访问地址。

        :param lemon_link: The lemon_link of this ShowClusterDetailResponse.
        :type lemon_link: str
        """
        self._lemon_link = lemon_link

    @property
    def zookeeper_link(self):
        """Gets the zookeeper_link of this ShowClusterDetailResponse.

        内网ZooKeeper连接访问地址。

        :return: The zookeeper_link of this ShowClusterDetailResponse.
        :rtype: str
        """
        return self._zookeeper_link

    @zookeeper_link.setter
    def zookeeper_link(self, zookeeper_link):
        """Sets the zookeeper_link of this ShowClusterDetailResponse.

        内网ZooKeeper连接访问地址。

        :param zookeeper_link: The zookeeper_link of this ShowClusterDetailResponse.
        :type zookeeper_link: str
        """
        self._zookeeper_link = zookeeper_link

    @property
    def hbase_public_endpoint(self):
        """Gets the hbase_public_endpoint of this ShowClusterDetailResponse.

        公网HBase连接访问地址。

        :return: The hbase_public_endpoint of this ShowClusterDetailResponse.
        :rtype: str
        """
        return self._hbase_public_endpoint

    @hbase_public_endpoint.setter
    def hbase_public_endpoint(self, hbase_public_endpoint):
        """Sets the hbase_public_endpoint of this ShowClusterDetailResponse.

        公网HBase连接访问地址。

        :param hbase_public_endpoint: The hbase_public_endpoint of this ShowClusterDetailResponse.
        :type hbase_public_endpoint: str
        """
        self._hbase_public_endpoint = hbase_public_endpoint

    @property
    def is_frozen(self):
        """Gets the is_frozen of this ShowClusterDetailResponse.

        集群是否被冻结。 - false：不冻结 - true：冻结

        :return: The is_frozen of this ShowClusterDetailResponse.
        :rtype: str
        """
        return self._is_frozen

    @is_frozen.setter
    def is_frozen(self, is_frozen):
        """Sets the is_frozen of this ShowClusterDetailResponse.

        集群是否被冻结。 - false：不冻结 - true：冻结

        :param is_frozen: The is_frozen of this ShowClusterDetailResponse.
        :type is_frozen: str
        """
        self._is_frozen = is_frozen

    @property
    def vpc_id(self):
        """Gets the vpc_id of this ShowClusterDetailResponse.

        VPC ID，创建集群节点所在的虚拟私有ID。

        :return: The vpc_id of this ShowClusterDetailResponse.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this ShowClusterDetailResponse.

        VPC ID，创建集群节点所在的虚拟私有ID。

        :param vpc_id: The vpc_id of this ShowClusterDetailResponse.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def sub_net_id(self):
        """Gets the sub_net_id of this ShowClusterDetailResponse.

        子网ID，创建集群所在子网段。

        :return: The sub_net_id of this ShowClusterDetailResponse.
        :rtype: str
        """
        return self._sub_net_id

    @sub_net_id.setter
    def sub_net_id(self, sub_net_id):
        """Sets the sub_net_id of this ShowClusterDetailResponse.

        子网ID，创建集群所在子网段。

        :param sub_net_id: The sub_net_id of this ShowClusterDetailResponse.
        :type sub_net_id: str
        """
        self._sub_net_id = sub_net_id

    @property
    def security_group_id(self):
        """Gets the security_group_id of this ShowClusterDetailResponse.

        安全组对应的ID。

        :return: The security_group_id of this ShowClusterDetailResponse.
        :rtype: str
        """
        return self._security_group_id

    @security_group_id.setter
    def security_group_id(self, security_group_id):
        """Sets the security_group_id of this ShowClusterDetailResponse.

        安全组对应的ID。

        :param security_group_id: The security_group_id of this ShowClusterDetailResponse.
        :type security_group_id: str
        """
        self._security_group_id = security_group_id

    @property
    def availability_zone(self):
        """Gets the availability_zone of this ShowClusterDetailResponse.

        集群所属的可用区。

        :return: The availability_zone of this ShowClusterDetailResponse.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        """Sets the availability_zone of this ShowClusterDetailResponse.

        集群所属的可用区。

        :param availability_zone: The availability_zone of this ShowClusterDetailResponse.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

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
        if not isinstance(other, ShowClusterDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
