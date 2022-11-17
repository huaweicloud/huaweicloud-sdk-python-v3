# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Clusters:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'customer_config': 'CustomerConfig',
        'datastore': 'Datastore',
        'instances': 'list[ClusterDetailInstance]',
        'az_name': 'str',
        'dbuser': 'str',
        'flavor_name': 'str',
        'recent_event': 'int',
        'is_auto_off': 'bool',
        'is_schedule_boot_off': 'bool',
        'cluster_mode': 'str',
        'namespace': 'str',
        'task': 'ClusterTask',
        'public_endpoint': 'str',
        'action_progress': 'ActionProgress',
        'created': 'str',
        'bak_expected_start_time': 'str',
        'bak_keep_day': 'int',
        'name': 'str',
        'status_detail': 'str',
        'id': 'str',
        'is_frozen': 'str',
        'updated': 'str',
        'status': 'str',
        'failed_reasons': 'FailedReasons'
    }

    attribute_map = {
        'customer_config': 'customerConfig',
        'datastore': 'datastore',
        'instances': 'instances',
        'az_name': 'azName',
        'dbuser': 'dbuser',
        'flavor_name': 'flavorName',
        'recent_event': 'recentEvent',
        'is_auto_off': 'isAutoOff',
        'is_schedule_boot_off': 'isScheduleBootOff',
        'cluster_mode': 'clusterMode',
        'namespace': 'namespace',
        'task': 'task',
        'public_endpoint': 'publicEndpoint',
        'action_progress': 'actionProgress',
        'created': 'created',
        'bak_expected_start_time': 'bakExpectedStartTime',
        'bak_keep_day': 'bakKeepDay',
        'name': 'name',
        'status_detail': 'statusDetail',
        'id': 'id',
        'is_frozen': 'isFrozen',
        'updated': 'updated',
        'status': 'status',
        'failed_reasons': 'failedReasons'
    }

    def __init__(self, customer_config=None, datastore=None, instances=None, az_name=None, dbuser=None, flavor_name=None, recent_event=None, is_auto_off=None, is_schedule_boot_off=None, cluster_mode=None, namespace=None, task=None, public_endpoint=None, action_progress=None, created=None, bak_expected_start_time=None, bak_keep_day=None, name=None, status_detail=None, id=None, is_frozen=None, updated=None, status=None, failed_reasons=None):
        """Clusters

        The model defined in huaweicloud sdk

        :param customer_config: 
        :type customer_config: :class:`huaweicloudsdkcdm.v1.CustomerConfig`
        :param datastore: 
        :type datastore: :class:`huaweicloudsdkcdm.v1.Datastore`
        :param instances: 集群的节点信息，请参见instances参数说明
        :type instances: list[:class:`huaweicloudsdkcdm.v1.ClusterDetailInstance`]
        :param az_name: az名称
        :type az_name: str
        :param dbuser: 数据库用户
        :type dbuser: str
        :param flavor_name: 规格名称
        :type flavor_name: str
        :param recent_event: 事件数
        :type recent_event: int
        :param is_auto_off: 自动关机
        :type is_auto_off: bool
        :param is_schedule_boot_off: 选择是否启用定时开关机功能。定时开关机功能和自动关机功能不可同时开启
        :type is_schedule_boot_off: bool
        :param cluster_mode: 集群模式：sharding(分片集群)
        :type cluster_mode: str
        :param namespace: 命名空间
        :type namespace: str
        :param task: 
        :type task: :class:`huaweicloudsdkcdm.v1.ClusterTask`
        :param public_endpoint: 集群绑定的EIP
        :type public_endpoint: str
        :param action_progress: 
        :type action_progress: :class:`huaweicloudsdkcdm.v1.ActionProgress`
        :param created: 集群创建时间，格式为ISO8601：YYYY-MM-DDThh:mm:ssZ
        :type created: str
        :param bak_expected_start_time: 开始时间
        :type bak_expected_start_time: str
        :param bak_keep_day: 保留时间
        :type bak_keep_day: int
        :param name: 集群名称
        :type name: str
        :param status_detail: 集群状态描述：Normal（正常）
        :type status_detail: str
        :param id: 集群ID
        :type id: str
        :param is_frozen: 集群是否冻结：0：否 1：是
        :type is_frozen: str
        :param updated: 集群更新时间，格式为ISO8601：YYYY-MM-DDThh:mm:ssZ
        :type updated: str
        :param status: 集群状态： - 100：创建中 - 200：正常 - 300：失败 - 303：创建失败 - 500：重启中 - 800：冻结 - 900：已关机 - 910：正在关机 - 920：正在开机
        :type status: str
        :param failed_reasons: 
        :type failed_reasons: :class:`huaweicloudsdkcdm.v1.FailedReasons`
        """
        
        

        self._customer_config = None
        self._datastore = None
        self._instances = None
        self._az_name = None
        self._dbuser = None
        self._flavor_name = None
        self._recent_event = None
        self._is_auto_off = None
        self._is_schedule_boot_off = None
        self._cluster_mode = None
        self._namespace = None
        self._task = None
        self._public_endpoint = None
        self._action_progress = None
        self._created = None
        self._bak_expected_start_time = None
        self._bak_keep_day = None
        self._name = None
        self._status_detail = None
        self._id = None
        self._is_frozen = None
        self._updated = None
        self._status = None
        self._failed_reasons = None
        self.discriminator = None

        if customer_config is not None:
            self.customer_config = customer_config
        if datastore is not None:
            self.datastore = datastore
        if instances is not None:
            self.instances = instances
        if az_name is not None:
            self.az_name = az_name
        if dbuser is not None:
            self.dbuser = dbuser
        if flavor_name is not None:
            self.flavor_name = flavor_name
        if recent_event is not None:
            self.recent_event = recent_event
        if is_auto_off is not None:
            self.is_auto_off = is_auto_off
        if is_schedule_boot_off is not None:
            self.is_schedule_boot_off = is_schedule_boot_off
        if cluster_mode is not None:
            self.cluster_mode = cluster_mode
        if namespace is not None:
            self.namespace = namespace
        if task is not None:
            self.task = task
        if public_endpoint is not None:
            self.public_endpoint = public_endpoint
        if action_progress is not None:
            self.action_progress = action_progress
        self.created = created
        if bak_expected_start_time is not None:
            self.bak_expected_start_time = bak_expected_start_time
        if bak_keep_day is not None:
            self.bak_keep_day = bak_keep_day
        self.name = name
        if status_detail is not None:
            self.status_detail = status_detail
        self.id = id
        self.is_frozen = is_frozen
        self.updated = updated
        self.status = status
        if failed_reasons is not None:
            self.failed_reasons = failed_reasons

    @property
    def customer_config(self):
        """Gets the customer_config of this Clusters.

        :return: The customer_config of this Clusters.
        :rtype: :class:`huaweicloudsdkcdm.v1.CustomerConfig`
        """
        return self._customer_config

    @customer_config.setter
    def customer_config(self, customer_config):
        """Sets the customer_config of this Clusters.

        :param customer_config: The customer_config of this Clusters.
        :type customer_config: :class:`huaweicloudsdkcdm.v1.CustomerConfig`
        """
        self._customer_config = customer_config

    @property
    def datastore(self):
        """Gets the datastore of this Clusters.

        :return: The datastore of this Clusters.
        :rtype: :class:`huaweicloudsdkcdm.v1.Datastore`
        """
        return self._datastore

    @datastore.setter
    def datastore(self, datastore):
        """Sets the datastore of this Clusters.

        :param datastore: The datastore of this Clusters.
        :type datastore: :class:`huaweicloudsdkcdm.v1.Datastore`
        """
        self._datastore = datastore

    @property
    def instances(self):
        """Gets the instances of this Clusters.

        集群的节点信息，请参见instances参数说明

        :return: The instances of this Clusters.
        :rtype: list[:class:`huaweicloudsdkcdm.v1.ClusterDetailInstance`]
        """
        return self._instances

    @instances.setter
    def instances(self, instances):
        """Sets the instances of this Clusters.

        集群的节点信息，请参见instances参数说明

        :param instances: The instances of this Clusters.
        :type instances: list[:class:`huaweicloudsdkcdm.v1.ClusterDetailInstance`]
        """
        self._instances = instances

    @property
    def az_name(self):
        """Gets the az_name of this Clusters.

        az名称

        :return: The az_name of this Clusters.
        :rtype: str
        """
        return self._az_name

    @az_name.setter
    def az_name(self, az_name):
        """Sets the az_name of this Clusters.

        az名称

        :param az_name: The az_name of this Clusters.
        :type az_name: str
        """
        self._az_name = az_name

    @property
    def dbuser(self):
        """Gets the dbuser of this Clusters.

        数据库用户

        :return: The dbuser of this Clusters.
        :rtype: str
        """
        return self._dbuser

    @dbuser.setter
    def dbuser(self, dbuser):
        """Sets the dbuser of this Clusters.

        数据库用户

        :param dbuser: The dbuser of this Clusters.
        :type dbuser: str
        """
        self._dbuser = dbuser

    @property
    def flavor_name(self):
        """Gets the flavor_name of this Clusters.

        规格名称

        :return: The flavor_name of this Clusters.
        :rtype: str
        """
        return self._flavor_name

    @flavor_name.setter
    def flavor_name(self, flavor_name):
        """Sets the flavor_name of this Clusters.

        规格名称

        :param flavor_name: The flavor_name of this Clusters.
        :type flavor_name: str
        """
        self._flavor_name = flavor_name

    @property
    def recent_event(self):
        """Gets the recent_event of this Clusters.

        事件数

        :return: The recent_event of this Clusters.
        :rtype: int
        """
        return self._recent_event

    @recent_event.setter
    def recent_event(self, recent_event):
        """Sets the recent_event of this Clusters.

        事件数

        :param recent_event: The recent_event of this Clusters.
        :type recent_event: int
        """
        self._recent_event = recent_event

    @property
    def is_auto_off(self):
        """Gets the is_auto_off of this Clusters.

        自动关机

        :return: The is_auto_off of this Clusters.
        :rtype: bool
        """
        return self._is_auto_off

    @is_auto_off.setter
    def is_auto_off(self, is_auto_off):
        """Sets the is_auto_off of this Clusters.

        自动关机

        :param is_auto_off: The is_auto_off of this Clusters.
        :type is_auto_off: bool
        """
        self._is_auto_off = is_auto_off

    @property
    def is_schedule_boot_off(self):
        """Gets the is_schedule_boot_off of this Clusters.

        选择是否启用定时开关机功能。定时开关机功能和自动关机功能不可同时开启

        :return: The is_schedule_boot_off of this Clusters.
        :rtype: bool
        """
        return self._is_schedule_boot_off

    @is_schedule_boot_off.setter
    def is_schedule_boot_off(self, is_schedule_boot_off):
        """Sets the is_schedule_boot_off of this Clusters.

        选择是否启用定时开关机功能。定时开关机功能和自动关机功能不可同时开启

        :param is_schedule_boot_off: The is_schedule_boot_off of this Clusters.
        :type is_schedule_boot_off: bool
        """
        self._is_schedule_boot_off = is_schedule_boot_off

    @property
    def cluster_mode(self):
        """Gets the cluster_mode of this Clusters.

        集群模式：sharding(分片集群)

        :return: The cluster_mode of this Clusters.
        :rtype: str
        """
        return self._cluster_mode

    @cluster_mode.setter
    def cluster_mode(self, cluster_mode):
        """Sets the cluster_mode of this Clusters.

        集群模式：sharding(分片集群)

        :param cluster_mode: The cluster_mode of this Clusters.
        :type cluster_mode: str
        """
        self._cluster_mode = cluster_mode

    @property
    def namespace(self):
        """Gets the namespace of this Clusters.

        命名空间

        :return: The namespace of this Clusters.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this Clusters.

        命名空间

        :param namespace: The namespace of this Clusters.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def task(self):
        """Gets the task of this Clusters.

        :return: The task of this Clusters.
        :rtype: :class:`huaweicloudsdkcdm.v1.ClusterTask`
        """
        return self._task

    @task.setter
    def task(self, task):
        """Sets the task of this Clusters.

        :param task: The task of this Clusters.
        :type task: :class:`huaweicloudsdkcdm.v1.ClusterTask`
        """
        self._task = task

    @property
    def public_endpoint(self):
        """Gets the public_endpoint of this Clusters.

        集群绑定的EIP

        :return: The public_endpoint of this Clusters.
        :rtype: str
        """
        return self._public_endpoint

    @public_endpoint.setter
    def public_endpoint(self, public_endpoint):
        """Sets the public_endpoint of this Clusters.

        集群绑定的EIP

        :param public_endpoint: The public_endpoint of this Clusters.
        :type public_endpoint: str
        """
        self._public_endpoint = public_endpoint

    @property
    def action_progress(self):
        """Gets the action_progress of this Clusters.

        :return: The action_progress of this Clusters.
        :rtype: :class:`huaweicloudsdkcdm.v1.ActionProgress`
        """
        return self._action_progress

    @action_progress.setter
    def action_progress(self, action_progress):
        """Sets the action_progress of this Clusters.

        :param action_progress: The action_progress of this Clusters.
        :type action_progress: :class:`huaweicloudsdkcdm.v1.ActionProgress`
        """
        self._action_progress = action_progress

    @property
    def created(self):
        """Gets the created of this Clusters.

        集群创建时间，格式为ISO8601：YYYY-MM-DDThh:mm:ssZ

        :return: The created of this Clusters.
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this Clusters.

        集群创建时间，格式为ISO8601：YYYY-MM-DDThh:mm:ssZ

        :param created: The created of this Clusters.
        :type created: str
        """
        self._created = created

    @property
    def bak_expected_start_time(self):
        """Gets the bak_expected_start_time of this Clusters.

        开始时间

        :return: The bak_expected_start_time of this Clusters.
        :rtype: str
        """
        return self._bak_expected_start_time

    @bak_expected_start_time.setter
    def bak_expected_start_time(self, bak_expected_start_time):
        """Sets the bak_expected_start_time of this Clusters.

        开始时间

        :param bak_expected_start_time: The bak_expected_start_time of this Clusters.
        :type bak_expected_start_time: str
        """
        self._bak_expected_start_time = bak_expected_start_time

    @property
    def bak_keep_day(self):
        """Gets the bak_keep_day of this Clusters.

        保留时间

        :return: The bak_keep_day of this Clusters.
        :rtype: int
        """
        return self._bak_keep_day

    @bak_keep_day.setter
    def bak_keep_day(self, bak_keep_day):
        """Sets the bak_keep_day of this Clusters.

        保留时间

        :param bak_keep_day: The bak_keep_day of this Clusters.
        :type bak_keep_day: int
        """
        self._bak_keep_day = bak_keep_day

    @property
    def name(self):
        """Gets the name of this Clusters.

        集群名称

        :return: The name of this Clusters.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Clusters.

        集群名称

        :param name: The name of this Clusters.
        :type name: str
        """
        self._name = name

    @property
    def status_detail(self):
        """Gets the status_detail of this Clusters.

        集群状态描述：Normal（正常）

        :return: The status_detail of this Clusters.
        :rtype: str
        """
        return self._status_detail

    @status_detail.setter
    def status_detail(self, status_detail):
        """Sets the status_detail of this Clusters.

        集群状态描述：Normal（正常）

        :param status_detail: The status_detail of this Clusters.
        :type status_detail: str
        """
        self._status_detail = status_detail

    @property
    def id(self):
        """Gets the id of this Clusters.

        集群ID

        :return: The id of this Clusters.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Clusters.

        集群ID

        :param id: The id of this Clusters.
        :type id: str
        """
        self._id = id

    @property
    def is_frozen(self):
        """Gets the is_frozen of this Clusters.

        集群是否冻结：0：否 1：是

        :return: The is_frozen of this Clusters.
        :rtype: str
        """
        return self._is_frozen

    @is_frozen.setter
    def is_frozen(self, is_frozen):
        """Sets the is_frozen of this Clusters.

        集群是否冻结：0：否 1：是

        :param is_frozen: The is_frozen of this Clusters.
        :type is_frozen: str
        """
        self._is_frozen = is_frozen

    @property
    def updated(self):
        """Gets the updated of this Clusters.

        集群更新时间，格式为ISO8601：YYYY-MM-DDThh:mm:ssZ

        :return: The updated of this Clusters.
        :rtype: str
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this Clusters.

        集群更新时间，格式为ISO8601：YYYY-MM-DDThh:mm:ssZ

        :param updated: The updated of this Clusters.
        :type updated: str
        """
        self._updated = updated

    @property
    def status(self):
        """Gets the status of this Clusters.

        集群状态： - 100：创建中 - 200：正常 - 300：失败 - 303：创建失败 - 500：重启中 - 800：冻结 - 900：已关机 - 910：正在关机 - 920：正在开机

        :return: The status of this Clusters.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Clusters.

        集群状态： - 100：创建中 - 200：正常 - 300：失败 - 303：创建失败 - 500：重启中 - 800：冻结 - 900：已关机 - 910：正在关机 - 920：正在开机

        :param status: The status of this Clusters.
        :type status: str
        """
        self._status = status

    @property
    def failed_reasons(self):
        """Gets the failed_reasons of this Clusters.

        :return: The failed_reasons of this Clusters.
        :rtype: :class:`huaweicloudsdkcdm.v1.FailedReasons`
        """
        return self._failed_reasons

    @failed_reasons.setter
    def failed_reasons(self, failed_reasons):
        """Sets the failed_reasons of this Clusters.

        :param failed_reasons: The failed_reasons of this Clusters.
        :type failed_reasons: :class:`huaweicloudsdkcdm.v1.FailedReasons`
        """
        self._failed_reasons = failed_reasons

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
        if not isinstance(other, Clusters):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
