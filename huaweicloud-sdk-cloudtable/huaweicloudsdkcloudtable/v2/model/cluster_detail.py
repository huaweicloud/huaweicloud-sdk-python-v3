# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ClusterDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'action_progress': 'ActionProgress',
        'actions': 'list[str]',
        'local_hdfs': 'bool',
        'is_show_222_version_feature': 'str',
        'actions_count': 'list[str]',
        'support_auth': 'bool',
        'eps_id': 'str',
        'cluster_type': 'str',
        'order_id': 'str',
        'order_status': 'str',
        'is_local_hdfs': 'bool',
        'ck_deploy_mode': 'str',
        'flavor_type_en': 'str',
        'enable_hot_cold_feature_cluster': 'str',
        'enable_hot_cold_feature': 'str',
        'data_flavor': 'str',
        'control_flavor': 'str',
        'data_node_num': 'str',
        'control_node_num': 'str',
        'data_node_total_storage_size': 'str',
        'control_node_total_storage_size': 'str',
        'cold_storage_used_size': 'str',
        'data_node_volume_type': 'str',
        'control_node_volume_type': 'str',
        'auth_mode': 'str',
        'az_code': 'str',
        'cluster_id': 'str',
        'cluster_name': 'str',
        'created': 'str',
        'enable_dfv': 'str',
        'enable_free': 'str',
        'enable_lemon': 'str',
        'enable_open_tsdb': 'str',
        'status': 'str',
        'tags': 'str',
        'version': 'str',
        'zookeeper_link': 'str'
    }

    attribute_map = {
        'action_progress': 'action_progress',
        'actions': 'actions',
        'local_hdfs': 'localHdfs',
        'is_show_222_version_feature': 'is_show_222_version_feature',
        'actions_count': 'actionsCount',
        'support_auth': 'support_auth',
        'eps_id': 'eps_id',
        'cluster_type': 'cluster_type',
        'order_id': 'order_id',
        'order_status': 'order_status',
        'is_local_hdfs': 'is_local_hdfs',
        'ck_deploy_mode': 'ck_deploy_mode',
        'flavor_type_en': 'flavor_type_en',
        'enable_hot_cold_feature_cluster': 'enable_hot_cold_feature_cluster',
        'enable_hot_cold_feature': 'enable_hot_cold_feature',
        'data_flavor': 'data_flavor',
        'control_flavor': 'control_flavor',
        'data_node_num': 'data_node_num',
        'control_node_num': 'control_node_num',
        'data_node_total_storage_size': 'data_node_total_storage_size',
        'control_node_total_storage_size': 'control_node_total_storage_size',
        'cold_storage_used_size': 'cold_storage_used_size',
        'data_node_volume_type': 'data_node_volume_type',
        'control_node_volume_type': 'control_node_volume_type',
        'auth_mode': 'auth_mode',
        'az_code': 'az_code',
        'cluster_id': 'cluster_id',
        'cluster_name': 'cluster_name',
        'created': 'created',
        'enable_dfv': 'enable_dfv',
        'enable_free': 'enable_free',
        'enable_lemon': 'enable_lemon',
        'enable_open_tsdb': 'enable_openTSDB',
        'status': 'status',
        'tags': 'tags',
        'version': 'version',
        'zookeeper_link': 'zookeeper_link'
    }

    def __init__(self, action_progress=None, actions=None, local_hdfs=None, is_show_222_version_feature=None, actions_count=None, support_auth=None, eps_id=None, cluster_type=None, order_id=None, order_status=None, is_local_hdfs=None, ck_deploy_mode=None, flavor_type_en=None, enable_hot_cold_feature_cluster=None, enable_hot_cold_feature=None, data_flavor=None, control_flavor=None, data_node_num=None, control_node_num=None, data_node_total_storage_size=None, control_node_total_storage_size=None, cold_storage_used_size=None, data_node_volume_type=None, control_node_volume_type=None, auth_mode=None, az_code=None, cluster_id=None, cluster_name=None, created=None, enable_dfv=None, enable_free=None, enable_lemon=None, enable_open_tsdb=None, status=None, tags=None, version=None, zookeeper_link=None):
        r"""ClusterDetail

        The model defined in huaweicloud sdk

        :param action_progress: 
        :type action_progress: :class:`huaweicloudsdkcloudtable.v2.ActionProgress`
        :param actions: 集群操作记录
        :type actions: list[str]
        :param local_hdfs: 是否开启hdfs。 - false：不开启 - true：开启
        :type local_hdfs: bool
        :param is_show_222_version_feature: 是否开222版本特性。 - false：不开启 - true：开启
        :type is_show_222_version_feature: str
        :param actions_count: 集群操作记录
        :type actions_count: list[str]
        :param support_auth: 是否支持开启认证。 - false：不支持 - true：支持
        :type support_auth: bool
        :param eps_id: eps_id。
        :type eps_id: str
        :param cluster_type: 集群类型。
        :type cluster_type: str
        :param order_id: 包周期订单号。
        :type order_id: str
        :param order_status: 包周期订单状态。
        :type order_status: str
        :param is_local_hdfs: 是否开启hdfs。 - false：不开启 - true：开启
        :type is_local_hdfs: bool
        :param ck_deploy_mode: ClickHouse部署模式。
        :type ck_deploy_mode: str
        :param flavor_type_en: 节点磁盘类型。
        :type flavor_type_en: str
        :param enable_hot_cold_feature_cluster: 集群是否支持开启冷热分离。
        :type enable_hot_cold_feature_cluster: str
        :param enable_hot_cold_feature: 集群是否开启冷热分离。
        :type enable_hot_cold_feature: str
        :param data_flavor: 数据节点规格。
        :type data_flavor: str
        :param control_flavor: 数据同步节点规格。
        :type control_flavor: str
        :param data_node_num: 数据节点个数。
        :type data_node_num: str
        :param control_node_num: 数据同步节点个数。
        :type control_node_num: str
        :param data_node_total_storage_size: 数据节点磁盘容量。
        :type data_node_total_storage_size: str
        :param control_node_total_storage_size: 数据同步节点磁盘容量。
        :type control_node_total_storage_size: str
        :param cold_storage_used_size: 冷存储使用量。
        :type cold_storage_used_size: str
        :param data_node_volume_type: 数据节点磁盘类型。
        :type data_node_volume_type: str
        :param control_node_volume_type: 数据同步节点磁盘类型。
        :type control_node_volume_type: str
        :param auth_mode: 是否开启IAM权限认证。 - false：不开启 - true：开启
        :type auth_mode: str
        :param az_code: 集群所在的可用区（AZ)。
        :type az_code: str
        :param cluster_id: 集群ID，集群唯一标识。
        :type cluster_id: str
        :param cluster_name: CloudTable集群名称。
        :type cluster_name: str
        :param created: 集群创建时间。
        :type created: str
        :param enable_dfv: 是否开启DFV。 - false：不开启 - true：开启
        :type enable_dfv: str
        :param enable_free: 集群是否免费。 - false：不免费 - true：免费
        :type enable_free: str
        :param enable_lemon: 是否开启Lemon。 - false：不开启 - true：开启
        :type enable_lemon: str
        :param enable_open_tsdb: 是否开启OpenTSDB。 - false：不开启 - true：开启
        :type enable_open_tsdb: str
        :param status: 集群状态： - 200：集群正常 - 300：集群异常 - 303：集群创建失败 - 400：集群已删除
        :type status: str
        :param tags: 集群标识符。
        :type tags: str
        :param version: 集群版本号。
        :type version: str
        :param zookeeper_link: CloudTable集群ZooKeeper的链接地址。例如：cloudtable-3058-zk3-Dqcwuh6R.mycloudtable.com:2181,cloudtable-3058-zk2-TCwkZEie.mycloudtable.com:2181,cloudtable-3058-zk1-TBELUFOK.mycloudtable.com:2181
        :type zookeeper_link: str
        """
        
        

        self._action_progress = None
        self._actions = None
        self._local_hdfs = None
        self._is_show_222_version_feature = None
        self._actions_count = None
        self._support_auth = None
        self._eps_id = None
        self._cluster_type = None
        self._order_id = None
        self._order_status = None
        self._is_local_hdfs = None
        self._ck_deploy_mode = None
        self._flavor_type_en = None
        self._enable_hot_cold_feature_cluster = None
        self._enable_hot_cold_feature = None
        self._data_flavor = None
        self._control_flavor = None
        self._data_node_num = None
        self._control_node_num = None
        self._data_node_total_storage_size = None
        self._control_node_total_storage_size = None
        self._cold_storage_used_size = None
        self._data_node_volume_type = None
        self._control_node_volume_type = None
        self._auth_mode = None
        self._az_code = None
        self._cluster_id = None
        self._cluster_name = None
        self._created = None
        self._enable_dfv = None
        self._enable_free = None
        self._enable_lemon = None
        self._enable_open_tsdb = None
        self._status = None
        self._tags = None
        self._version = None
        self._zookeeper_link = None
        self.discriminator = None

        if action_progress is not None:
            self.action_progress = action_progress
        if actions is not None:
            self.actions = actions
        if local_hdfs is not None:
            self.local_hdfs = local_hdfs
        if is_show_222_version_feature is not None:
            self.is_show_222_version_feature = is_show_222_version_feature
        if actions_count is not None:
            self.actions_count = actions_count
        if support_auth is not None:
            self.support_auth = support_auth
        if eps_id is not None:
            self.eps_id = eps_id
        if cluster_type is not None:
            self.cluster_type = cluster_type
        if order_id is not None:
            self.order_id = order_id
        if order_status is not None:
            self.order_status = order_status
        if is_local_hdfs is not None:
            self.is_local_hdfs = is_local_hdfs
        if ck_deploy_mode is not None:
            self.ck_deploy_mode = ck_deploy_mode
        if flavor_type_en is not None:
            self.flavor_type_en = flavor_type_en
        if enable_hot_cold_feature_cluster is not None:
            self.enable_hot_cold_feature_cluster = enable_hot_cold_feature_cluster
        if enable_hot_cold_feature is not None:
            self.enable_hot_cold_feature = enable_hot_cold_feature
        if data_flavor is not None:
            self.data_flavor = data_flavor
        if control_flavor is not None:
            self.control_flavor = control_flavor
        if data_node_num is not None:
            self.data_node_num = data_node_num
        if control_node_num is not None:
            self.control_node_num = control_node_num
        if data_node_total_storage_size is not None:
            self.data_node_total_storage_size = data_node_total_storage_size
        if control_node_total_storage_size is not None:
            self.control_node_total_storage_size = control_node_total_storage_size
        if cold_storage_used_size is not None:
            self.cold_storage_used_size = cold_storage_used_size
        if data_node_volume_type is not None:
            self.data_node_volume_type = data_node_volume_type
        if control_node_volume_type is not None:
            self.control_node_volume_type = control_node_volume_type
        if auth_mode is not None:
            self.auth_mode = auth_mode
        if az_code is not None:
            self.az_code = az_code
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if cluster_name is not None:
            self.cluster_name = cluster_name
        if created is not None:
            self.created = created
        if enable_dfv is not None:
            self.enable_dfv = enable_dfv
        if enable_free is not None:
            self.enable_free = enable_free
        if enable_lemon is not None:
            self.enable_lemon = enable_lemon
        if enable_open_tsdb is not None:
            self.enable_open_tsdb = enable_open_tsdb
        if status is not None:
            self.status = status
        if tags is not None:
            self.tags = tags
        if version is not None:
            self.version = version
        if zookeeper_link is not None:
            self.zookeeper_link = zookeeper_link

    @property
    def action_progress(self):
        r"""Gets the action_progress of this ClusterDetail.

        :return: The action_progress of this ClusterDetail.
        :rtype: :class:`huaweicloudsdkcloudtable.v2.ActionProgress`
        """
        return self._action_progress

    @action_progress.setter
    def action_progress(self, action_progress):
        r"""Sets the action_progress of this ClusterDetail.

        :param action_progress: The action_progress of this ClusterDetail.
        :type action_progress: :class:`huaweicloudsdkcloudtable.v2.ActionProgress`
        """
        self._action_progress = action_progress

    @property
    def actions(self):
        r"""Gets the actions of this ClusterDetail.

        集群操作记录

        :return: The actions of this ClusterDetail.
        :rtype: list[str]
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        r"""Sets the actions of this ClusterDetail.

        集群操作记录

        :param actions: The actions of this ClusterDetail.
        :type actions: list[str]
        """
        self._actions = actions

    @property
    def local_hdfs(self):
        r"""Gets the local_hdfs of this ClusterDetail.

        是否开启hdfs。 - false：不开启 - true：开启

        :return: The local_hdfs of this ClusterDetail.
        :rtype: bool
        """
        return self._local_hdfs

    @local_hdfs.setter
    def local_hdfs(self, local_hdfs):
        r"""Sets the local_hdfs of this ClusterDetail.

        是否开启hdfs。 - false：不开启 - true：开启

        :param local_hdfs: The local_hdfs of this ClusterDetail.
        :type local_hdfs: bool
        """
        self._local_hdfs = local_hdfs

    @property
    def is_show_222_version_feature(self):
        r"""Gets the is_show_222_version_feature of this ClusterDetail.

        是否开222版本特性。 - false：不开启 - true：开启

        :return: The is_show_222_version_feature of this ClusterDetail.
        :rtype: str
        """
        return self._is_show_222_version_feature

    @is_show_222_version_feature.setter
    def is_show_222_version_feature(self, is_show_222_version_feature):
        r"""Sets the is_show_222_version_feature of this ClusterDetail.

        是否开222版本特性。 - false：不开启 - true：开启

        :param is_show_222_version_feature: The is_show_222_version_feature of this ClusterDetail.
        :type is_show_222_version_feature: str
        """
        self._is_show_222_version_feature = is_show_222_version_feature

    @property
    def actions_count(self):
        r"""Gets the actions_count of this ClusterDetail.

        集群操作记录

        :return: The actions_count of this ClusterDetail.
        :rtype: list[str]
        """
        return self._actions_count

    @actions_count.setter
    def actions_count(self, actions_count):
        r"""Sets the actions_count of this ClusterDetail.

        集群操作记录

        :param actions_count: The actions_count of this ClusterDetail.
        :type actions_count: list[str]
        """
        self._actions_count = actions_count

    @property
    def support_auth(self):
        r"""Gets the support_auth of this ClusterDetail.

        是否支持开启认证。 - false：不支持 - true：支持

        :return: The support_auth of this ClusterDetail.
        :rtype: bool
        """
        return self._support_auth

    @support_auth.setter
    def support_auth(self, support_auth):
        r"""Sets the support_auth of this ClusterDetail.

        是否支持开启认证。 - false：不支持 - true：支持

        :param support_auth: The support_auth of this ClusterDetail.
        :type support_auth: bool
        """
        self._support_auth = support_auth

    @property
    def eps_id(self):
        r"""Gets the eps_id of this ClusterDetail.

        eps_id。

        :return: The eps_id of this ClusterDetail.
        :rtype: str
        """
        return self._eps_id

    @eps_id.setter
    def eps_id(self, eps_id):
        r"""Sets the eps_id of this ClusterDetail.

        eps_id。

        :param eps_id: The eps_id of this ClusterDetail.
        :type eps_id: str
        """
        self._eps_id = eps_id

    @property
    def cluster_type(self):
        r"""Gets the cluster_type of this ClusterDetail.

        集群类型。

        :return: The cluster_type of this ClusterDetail.
        :rtype: str
        """
        return self._cluster_type

    @cluster_type.setter
    def cluster_type(self, cluster_type):
        r"""Sets the cluster_type of this ClusterDetail.

        集群类型。

        :param cluster_type: The cluster_type of this ClusterDetail.
        :type cluster_type: str
        """
        self._cluster_type = cluster_type

    @property
    def order_id(self):
        r"""Gets the order_id of this ClusterDetail.

        包周期订单号。

        :return: The order_id of this ClusterDetail.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        r"""Sets the order_id of this ClusterDetail.

        包周期订单号。

        :param order_id: The order_id of this ClusterDetail.
        :type order_id: str
        """
        self._order_id = order_id

    @property
    def order_status(self):
        r"""Gets the order_status of this ClusterDetail.

        包周期订单状态。

        :return: The order_status of this ClusterDetail.
        :rtype: str
        """
        return self._order_status

    @order_status.setter
    def order_status(self, order_status):
        r"""Sets the order_status of this ClusterDetail.

        包周期订单状态。

        :param order_status: The order_status of this ClusterDetail.
        :type order_status: str
        """
        self._order_status = order_status

    @property
    def is_local_hdfs(self):
        r"""Gets the is_local_hdfs of this ClusterDetail.

        是否开启hdfs。 - false：不开启 - true：开启

        :return: The is_local_hdfs of this ClusterDetail.
        :rtype: bool
        """
        return self._is_local_hdfs

    @is_local_hdfs.setter
    def is_local_hdfs(self, is_local_hdfs):
        r"""Sets the is_local_hdfs of this ClusterDetail.

        是否开启hdfs。 - false：不开启 - true：开启

        :param is_local_hdfs: The is_local_hdfs of this ClusterDetail.
        :type is_local_hdfs: bool
        """
        self._is_local_hdfs = is_local_hdfs

    @property
    def ck_deploy_mode(self):
        r"""Gets the ck_deploy_mode of this ClusterDetail.

        ClickHouse部署模式。

        :return: The ck_deploy_mode of this ClusterDetail.
        :rtype: str
        """
        return self._ck_deploy_mode

    @ck_deploy_mode.setter
    def ck_deploy_mode(self, ck_deploy_mode):
        r"""Sets the ck_deploy_mode of this ClusterDetail.

        ClickHouse部署模式。

        :param ck_deploy_mode: The ck_deploy_mode of this ClusterDetail.
        :type ck_deploy_mode: str
        """
        self._ck_deploy_mode = ck_deploy_mode

    @property
    def flavor_type_en(self):
        r"""Gets the flavor_type_en of this ClusterDetail.

        节点磁盘类型。

        :return: The flavor_type_en of this ClusterDetail.
        :rtype: str
        """
        return self._flavor_type_en

    @flavor_type_en.setter
    def flavor_type_en(self, flavor_type_en):
        r"""Sets the flavor_type_en of this ClusterDetail.

        节点磁盘类型。

        :param flavor_type_en: The flavor_type_en of this ClusterDetail.
        :type flavor_type_en: str
        """
        self._flavor_type_en = flavor_type_en

    @property
    def enable_hot_cold_feature_cluster(self):
        r"""Gets the enable_hot_cold_feature_cluster of this ClusterDetail.

        集群是否支持开启冷热分离。

        :return: The enable_hot_cold_feature_cluster of this ClusterDetail.
        :rtype: str
        """
        return self._enable_hot_cold_feature_cluster

    @enable_hot_cold_feature_cluster.setter
    def enable_hot_cold_feature_cluster(self, enable_hot_cold_feature_cluster):
        r"""Sets the enable_hot_cold_feature_cluster of this ClusterDetail.

        集群是否支持开启冷热分离。

        :param enable_hot_cold_feature_cluster: The enable_hot_cold_feature_cluster of this ClusterDetail.
        :type enable_hot_cold_feature_cluster: str
        """
        self._enable_hot_cold_feature_cluster = enable_hot_cold_feature_cluster

    @property
    def enable_hot_cold_feature(self):
        r"""Gets the enable_hot_cold_feature of this ClusterDetail.

        集群是否开启冷热分离。

        :return: The enable_hot_cold_feature of this ClusterDetail.
        :rtype: str
        """
        return self._enable_hot_cold_feature

    @enable_hot_cold_feature.setter
    def enable_hot_cold_feature(self, enable_hot_cold_feature):
        r"""Sets the enable_hot_cold_feature of this ClusterDetail.

        集群是否开启冷热分离。

        :param enable_hot_cold_feature: The enable_hot_cold_feature of this ClusterDetail.
        :type enable_hot_cold_feature: str
        """
        self._enable_hot_cold_feature = enable_hot_cold_feature

    @property
    def data_flavor(self):
        r"""Gets the data_flavor of this ClusterDetail.

        数据节点规格。

        :return: The data_flavor of this ClusterDetail.
        :rtype: str
        """
        return self._data_flavor

    @data_flavor.setter
    def data_flavor(self, data_flavor):
        r"""Sets the data_flavor of this ClusterDetail.

        数据节点规格。

        :param data_flavor: The data_flavor of this ClusterDetail.
        :type data_flavor: str
        """
        self._data_flavor = data_flavor

    @property
    def control_flavor(self):
        r"""Gets the control_flavor of this ClusterDetail.

        数据同步节点规格。

        :return: The control_flavor of this ClusterDetail.
        :rtype: str
        """
        return self._control_flavor

    @control_flavor.setter
    def control_flavor(self, control_flavor):
        r"""Sets the control_flavor of this ClusterDetail.

        数据同步节点规格。

        :param control_flavor: The control_flavor of this ClusterDetail.
        :type control_flavor: str
        """
        self._control_flavor = control_flavor

    @property
    def data_node_num(self):
        r"""Gets the data_node_num of this ClusterDetail.

        数据节点个数。

        :return: The data_node_num of this ClusterDetail.
        :rtype: str
        """
        return self._data_node_num

    @data_node_num.setter
    def data_node_num(self, data_node_num):
        r"""Sets the data_node_num of this ClusterDetail.

        数据节点个数。

        :param data_node_num: The data_node_num of this ClusterDetail.
        :type data_node_num: str
        """
        self._data_node_num = data_node_num

    @property
    def control_node_num(self):
        r"""Gets the control_node_num of this ClusterDetail.

        数据同步节点个数。

        :return: The control_node_num of this ClusterDetail.
        :rtype: str
        """
        return self._control_node_num

    @control_node_num.setter
    def control_node_num(self, control_node_num):
        r"""Sets the control_node_num of this ClusterDetail.

        数据同步节点个数。

        :param control_node_num: The control_node_num of this ClusterDetail.
        :type control_node_num: str
        """
        self._control_node_num = control_node_num

    @property
    def data_node_total_storage_size(self):
        r"""Gets the data_node_total_storage_size of this ClusterDetail.

        数据节点磁盘容量。

        :return: The data_node_total_storage_size of this ClusterDetail.
        :rtype: str
        """
        return self._data_node_total_storage_size

    @data_node_total_storage_size.setter
    def data_node_total_storage_size(self, data_node_total_storage_size):
        r"""Sets the data_node_total_storage_size of this ClusterDetail.

        数据节点磁盘容量。

        :param data_node_total_storage_size: The data_node_total_storage_size of this ClusterDetail.
        :type data_node_total_storage_size: str
        """
        self._data_node_total_storage_size = data_node_total_storage_size

    @property
    def control_node_total_storage_size(self):
        r"""Gets the control_node_total_storage_size of this ClusterDetail.

        数据同步节点磁盘容量。

        :return: The control_node_total_storage_size of this ClusterDetail.
        :rtype: str
        """
        return self._control_node_total_storage_size

    @control_node_total_storage_size.setter
    def control_node_total_storage_size(self, control_node_total_storage_size):
        r"""Sets the control_node_total_storage_size of this ClusterDetail.

        数据同步节点磁盘容量。

        :param control_node_total_storage_size: The control_node_total_storage_size of this ClusterDetail.
        :type control_node_total_storage_size: str
        """
        self._control_node_total_storage_size = control_node_total_storage_size

    @property
    def cold_storage_used_size(self):
        r"""Gets the cold_storage_used_size of this ClusterDetail.

        冷存储使用量。

        :return: The cold_storage_used_size of this ClusterDetail.
        :rtype: str
        """
        return self._cold_storage_used_size

    @cold_storage_used_size.setter
    def cold_storage_used_size(self, cold_storage_used_size):
        r"""Sets the cold_storage_used_size of this ClusterDetail.

        冷存储使用量。

        :param cold_storage_used_size: The cold_storage_used_size of this ClusterDetail.
        :type cold_storage_used_size: str
        """
        self._cold_storage_used_size = cold_storage_used_size

    @property
    def data_node_volume_type(self):
        r"""Gets the data_node_volume_type of this ClusterDetail.

        数据节点磁盘类型。

        :return: The data_node_volume_type of this ClusterDetail.
        :rtype: str
        """
        return self._data_node_volume_type

    @data_node_volume_type.setter
    def data_node_volume_type(self, data_node_volume_type):
        r"""Sets the data_node_volume_type of this ClusterDetail.

        数据节点磁盘类型。

        :param data_node_volume_type: The data_node_volume_type of this ClusterDetail.
        :type data_node_volume_type: str
        """
        self._data_node_volume_type = data_node_volume_type

    @property
    def control_node_volume_type(self):
        r"""Gets the control_node_volume_type of this ClusterDetail.

        数据同步节点磁盘类型。

        :return: The control_node_volume_type of this ClusterDetail.
        :rtype: str
        """
        return self._control_node_volume_type

    @control_node_volume_type.setter
    def control_node_volume_type(self, control_node_volume_type):
        r"""Sets the control_node_volume_type of this ClusterDetail.

        数据同步节点磁盘类型。

        :param control_node_volume_type: The control_node_volume_type of this ClusterDetail.
        :type control_node_volume_type: str
        """
        self._control_node_volume_type = control_node_volume_type

    @property
    def auth_mode(self):
        r"""Gets the auth_mode of this ClusterDetail.

        是否开启IAM权限认证。 - false：不开启 - true：开启

        :return: The auth_mode of this ClusterDetail.
        :rtype: str
        """
        return self._auth_mode

    @auth_mode.setter
    def auth_mode(self, auth_mode):
        r"""Sets the auth_mode of this ClusterDetail.

        是否开启IAM权限认证。 - false：不开启 - true：开启

        :param auth_mode: The auth_mode of this ClusterDetail.
        :type auth_mode: str
        """
        self._auth_mode = auth_mode

    @property
    def az_code(self):
        r"""Gets the az_code of this ClusterDetail.

        集群所在的可用区（AZ)。

        :return: The az_code of this ClusterDetail.
        :rtype: str
        """
        return self._az_code

    @az_code.setter
    def az_code(self, az_code):
        r"""Sets the az_code of this ClusterDetail.

        集群所在的可用区（AZ)。

        :param az_code: The az_code of this ClusterDetail.
        :type az_code: str
        """
        self._az_code = az_code

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this ClusterDetail.

        集群ID，集群唯一标识。

        :return: The cluster_id of this ClusterDetail.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this ClusterDetail.

        集群ID，集群唯一标识。

        :param cluster_id: The cluster_id of this ClusterDetail.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def cluster_name(self):
        r"""Gets the cluster_name of this ClusterDetail.

        CloudTable集群名称。

        :return: The cluster_name of this ClusterDetail.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        r"""Sets the cluster_name of this ClusterDetail.

        CloudTable集群名称。

        :param cluster_name: The cluster_name of this ClusterDetail.
        :type cluster_name: str
        """
        self._cluster_name = cluster_name

    @property
    def created(self):
        r"""Gets the created of this ClusterDetail.

        集群创建时间。

        :return: The created of this ClusterDetail.
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        r"""Sets the created of this ClusterDetail.

        集群创建时间。

        :param created: The created of this ClusterDetail.
        :type created: str
        """
        self._created = created

    @property
    def enable_dfv(self):
        r"""Gets the enable_dfv of this ClusterDetail.

        是否开启DFV。 - false：不开启 - true：开启

        :return: The enable_dfv of this ClusterDetail.
        :rtype: str
        """
        return self._enable_dfv

    @enable_dfv.setter
    def enable_dfv(self, enable_dfv):
        r"""Sets the enable_dfv of this ClusterDetail.

        是否开启DFV。 - false：不开启 - true：开启

        :param enable_dfv: The enable_dfv of this ClusterDetail.
        :type enable_dfv: str
        """
        self._enable_dfv = enable_dfv

    @property
    def enable_free(self):
        r"""Gets the enable_free of this ClusterDetail.

        集群是否免费。 - false：不免费 - true：免费

        :return: The enable_free of this ClusterDetail.
        :rtype: str
        """
        return self._enable_free

    @enable_free.setter
    def enable_free(self, enable_free):
        r"""Sets the enable_free of this ClusterDetail.

        集群是否免费。 - false：不免费 - true：免费

        :param enable_free: The enable_free of this ClusterDetail.
        :type enable_free: str
        """
        self._enable_free = enable_free

    @property
    def enable_lemon(self):
        r"""Gets the enable_lemon of this ClusterDetail.

        是否开启Lemon。 - false：不开启 - true：开启

        :return: The enable_lemon of this ClusterDetail.
        :rtype: str
        """
        return self._enable_lemon

    @enable_lemon.setter
    def enable_lemon(self, enable_lemon):
        r"""Sets the enable_lemon of this ClusterDetail.

        是否开启Lemon。 - false：不开启 - true：开启

        :param enable_lemon: The enable_lemon of this ClusterDetail.
        :type enable_lemon: str
        """
        self._enable_lemon = enable_lemon

    @property
    def enable_open_tsdb(self):
        r"""Gets the enable_open_tsdb of this ClusterDetail.

        是否开启OpenTSDB。 - false：不开启 - true：开启

        :return: The enable_open_tsdb of this ClusterDetail.
        :rtype: str
        """
        return self._enable_open_tsdb

    @enable_open_tsdb.setter
    def enable_open_tsdb(self, enable_open_tsdb):
        r"""Sets the enable_open_tsdb of this ClusterDetail.

        是否开启OpenTSDB。 - false：不开启 - true：开启

        :param enable_open_tsdb: The enable_open_tsdb of this ClusterDetail.
        :type enable_open_tsdb: str
        """
        self._enable_open_tsdb = enable_open_tsdb

    @property
    def status(self):
        r"""Gets the status of this ClusterDetail.

        集群状态： - 200：集群正常 - 300：集群异常 - 303：集群创建失败 - 400：集群已删除

        :return: The status of this ClusterDetail.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ClusterDetail.

        集群状态： - 200：集群正常 - 300：集群异常 - 303：集群创建失败 - 400：集群已删除

        :param status: The status of this ClusterDetail.
        :type status: str
        """
        self._status = status

    @property
    def tags(self):
        r"""Gets the tags of this ClusterDetail.

        集群标识符。

        :return: The tags of this ClusterDetail.
        :rtype: str
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this ClusterDetail.

        集群标识符。

        :param tags: The tags of this ClusterDetail.
        :type tags: str
        """
        self._tags = tags

    @property
    def version(self):
        r"""Gets the version of this ClusterDetail.

        集群版本号。

        :return: The version of this ClusterDetail.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this ClusterDetail.

        集群版本号。

        :param version: The version of this ClusterDetail.
        :type version: str
        """
        self._version = version

    @property
    def zookeeper_link(self):
        r"""Gets the zookeeper_link of this ClusterDetail.

        CloudTable集群ZooKeeper的链接地址。例如：cloudtable-3058-zk3-Dqcwuh6R.mycloudtable.com:2181,cloudtable-3058-zk2-TCwkZEie.mycloudtable.com:2181,cloudtable-3058-zk1-TBELUFOK.mycloudtable.com:2181

        :return: The zookeeper_link of this ClusterDetail.
        :rtype: str
        """
        return self._zookeeper_link

    @zookeeper_link.setter
    def zookeeper_link(self, zookeeper_link):
        r"""Sets the zookeeper_link of this ClusterDetail.

        CloudTable集群ZooKeeper的链接地址。例如：cloudtable-3058-zk3-Dqcwuh6R.mycloudtable.com:2181,cloudtable-3058-zk2-TCwkZEie.mycloudtable.com:2181,cloudtable-3058-zk1-TBELUFOK.mycloudtable.com:2181

        :param zookeeper_link: The zookeeper_link of this ClusterDetail.
        :type zookeeper_link: str
        """
        self._zookeeper_link = zookeeper_link

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
        if not isinstance(other, ClusterDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
