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
        'name': 'str',
        'status_detail': 'str',
        'id': 'str',
        'is_frozen': 'str',
        'config_status': 'str',
        'updated': 'str',
        'version': 'str',
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
        'name': 'name',
        'status_detail': 'statusDetail',
        'id': 'id',
        'is_frozen': 'isFrozen',
        'config_status': 'config_status',
        'updated': 'updated',
        'version': 'version',
        'status': 'status',
        'failed_reasons': 'failedReasons'
    }

    def __init__(self, customer_config=None, datastore=None, instances=None, az_name=None, dbuser=None, flavor_name=None, recent_event=None, is_auto_off=None, is_schedule_boot_off=None, cluster_mode=None, namespace=None, task=None, public_endpoint=None, action_progress=None, created=None, name=None, status_detail=None, id=None, is_frozen=None, config_status=None, updated=None, version=None, status=None, failed_reasons=None):
        """Clusters - a model defined in huaweicloud sdk"""
        
        

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
        self._name = None
        self._status_detail = None
        self._id = None
        self._is_frozen = None
        self._config_status = None
        self._updated = None
        self._version = None
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
        self.name = name
        if status_detail is not None:
            self.status_detail = status_detail
        self.id = id
        self.is_frozen = is_frozen
        if config_status is not None:
            self.config_status = config_status
        self.updated = updated
        self.version = version
        self.status = status
        if failed_reasons is not None:
            self.failed_reasons = failed_reasons

    @property
    def customer_config(self):
        """Gets the customer_config of this Clusters.


        :return: The customer_config of this Clusters.
        :rtype: CustomerConfig
        """
        return self._customer_config

    @customer_config.setter
    def customer_config(self, customer_config):
        """Sets the customer_config of this Clusters.


        :param customer_config: The customer_config of this Clusters.
        :type: CustomerConfig
        """
        self._customer_config = customer_config

    @property
    def datastore(self):
        """Gets the datastore of this Clusters.


        :return: The datastore of this Clusters.
        :rtype: Datastore
        """
        return self._datastore

    @datastore.setter
    def datastore(self, datastore):
        """Sets the datastore of this Clusters.


        :param datastore: The datastore of this Clusters.
        :type: Datastore
        """
        self._datastore = datastore

    @property
    def instances(self):
        """Gets the instances of this Clusters.

        集群的节点信息，请参见instances参数说明

        :return: The instances of this Clusters.
        :rtype: list[ClusterDetailInstance]
        """
        return self._instances

    @instances.setter
    def instances(self, instances):
        """Sets the instances of this Clusters.

        集群的节点信息，请参见instances参数说明

        :param instances: The instances of this Clusters.
        :type: list[ClusterDetailInstance]
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
        :type: str
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
        :type: str
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
        :type: str
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
        :type: int
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
        :type: bool
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
        :type: bool
        """
        self._is_schedule_boot_off = is_schedule_boot_off

    @property
    def cluster_mode(self):
        """Gets the cluster_mode of this Clusters.

        集群模式

        :return: The cluster_mode of this Clusters.
        :rtype: str
        """
        return self._cluster_mode

    @cluster_mode.setter
    def cluster_mode(self, cluster_mode):
        """Sets the cluster_mode of this Clusters.

        集群模式

        :param cluster_mode: The cluster_mode of this Clusters.
        :type: str
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
        :type: str
        """
        self._namespace = namespace

    @property
    def task(self):
        """Gets the task of this Clusters.


        :return: The task of this Clusters.
        :rtype: ClusterTask
        """
        return self._task

    @task.setter
    def task(self, task):
        """Sets the task of this Clusters.


        :param task: The task of this Clusters.
        :type: ClusterTask
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
        :type: str
        """
        self._public_endpoint = public_endpoint

    @property
    def action_progress(self):
        """Gets the action_progress of this Clusters.


        :return: The action_progress of this Clusters.
        :rtype: ActionProgress
        """
        return self._action_progress

    @action_progress.setter
    def action_progress(self, action_progress):
        """Sets the action_progress of this Clusters.


        :param action_progress: The action_progress of this Clusters.
        :type: ActionProgress
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
        :type: str
        """
        self._created = created

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
        :type: str
        """
        self._name = name

    @property
    def status_detail(self):
        """Gets the status_detail of this Clusters.

        集群状态描述

        :return: The status_detail of this Clusters.
        :rtype: str
        """
        return self._status_detail

    @status_detail.setter
    def status_detail(self, status_detail):
        """Sets the status_detail of this Clusters.

        集群状态描述

        :param status_detail: The status_detail of this Clusters.
        :type: str
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
        :type: str
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
        :type: str
        """
        self._is_frozen = is_frozen

    @property
    def config_status(self):
        """Gets the config_status of this Clusters.

        集群配置状态：In-Sync：配置已同步。Applying：配置中。Sync-Failure：配置失败

        :return: The config_status of this Clusters.
        :rtype: str
        """
        return self._config_status

    @config_status.setter
    def config_status(self, config_status):
        """Sets the config_status of this Clusters.

        集群配置状态：In-Sync：配置已同步。Applying：配置中。Sync-Failure：配置失败

        :param config_status: The config_status of this Clusters.
        :type: str
        """
        self._config_status = config_status

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
        :type: str
        """
        self._updated = updated

    @property
    def version(self):
        """Gets the version of this Clusters.

        集群版本

        :return: The version of this Clusters.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Clusters.

        集群版本

        :param version: The version of this Clusters.
        :type: str
        """
        self._version = version

    @property
    def status(self):
        """Gets the status of this Clusters.

        集群状态： - 100：创建中 - 200：正常 - 300：失败 - 303：创建失败 - 800：冻结 - 900：已关机 - 910：正在关机 - 920：正在开机

        :return: The status of this Clusters.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Clusters.

        集群状态： - 100：创建中 - 200：正常 - 300：失败 - 303：创建失败 - 800：冻结 - 900：已关机 - 910：正在关机 - 920：正在开机

        :param status: The status of this Clusters.
        :type: str
        """
        self._status = status

    @property
    def failed_reasons(self):
        """Gets the failed_reasons of this Clusters.


        :return: The failed_reasons of this Clusters.
        :rtype: FailedReasons
        """
        return self._failed_reasons

    @failed_reasons.setter
    def failed_reasons(self, failed_reasons):
        """Sets the failed_reasons of this Clusters.


        :param failed_reasons: The failed_reasons of this Clusters.
        :type: FailedReasons
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
