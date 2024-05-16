# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSecurityMemberSyncTaskResponse(SdkResponse):

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
        'project_id': 'str',
        'domain_id': 'str',
        'instance_id': 'str',
        'data_connection_workspace': 'str',
        'cluster_type': 'str',
        'data_connection_id': 'str',
        'data_connection_name': 'str',
        'cluster_id': 'str',
        'cluster_name': 'str',
        'schedule_start_hour': 'int',
        'schedule_end_hour': 'int',
        'schedule_period': 'str',
        'schedule_interval': 'int',
        'schedule_status': 'str',
        'sync_status': 'str',
        'sync_msg': 'str',
        'sync_time': 'int',
        'create_time': 'int',
        'create_user': 'str',
        'update_time': 'int',
        'update_user': 'str'
    }

    attribute_map = {
        'id': 'id',
        'project_id': 'project_id',
        'domain_id': 'domain_id',
        'instance_id': 'instance_id',
        'data_connection_workspace': 'data_connection_workspace',
        'cluster_type': 'cluster_type',
        'data_connection_id': 'data_connection_id',
        'data_connection_name': 'data_connection_name',
        'cluster_id': 'cluster_id',
        'cluster_name': 'cluster_name',
        'schedule_start_hour': 'schedule_start_hour',
        'schedule_end_hour': 'schedule_end_hour',
        'schedule_period': 'schedule_period',
        'schedule_interval': 'schedule_interval',
        'schedule_status': 'schedule_status',
        'sync_status': 'sync_status',
        'sync_msg': 'sync_msg',
        'sync_time': 'sync_time',
        'create_time': 'create_time',
        'create_user': 'create_user',
        'update_time': 'update_time',
        'update_user': 'update_user'
    }

    def __init__(self, id=None, project_id=None, domain_id=None, instance_id=None, data_connection_workspace=None, cluster_type=None, data_connection_id=None, data_connection_name=None, cluster_id=None, cluster_name=None, schedule_start_hour=None, schedule_end_hour=None, schedule_period=None, schedule_interval=None, schedule_status=None, sync_status=None, sync_msg=None, sync_time=None, create_time=None, create_user=None, update_time=None, update_user=None):
        """ShowSecurityMemberSyncTaskResponse

        The model defined in huaweicloud sdk

        :param id: 用户同步任务id。
        :type id: str
        :param project_id: 项目ID。
        :type project_id: str
        :param domain_id: 租户ID。
        :type domain_id: str
        :param instance_id: 实例ID。
        :type instance_id: str
        :param data_connection_workspace: 数据连接工作空间ID。
        :type data_connection_workspace: str
        :param cluster_type: 集群类型 * MRS集群 * DWS集群
        :type cluster_type: str
        :param data_connection_id: 数据连接id。
        :type data_connection_id: str
        :param data_connection_name: 数据连接名称。
        :type data_connection_name: str
        :param cluster_id: 集群id。
        :type cluster_id: str
        :param cluster_name: 集群名称。
        :type cluster_name: str
        :param schedule_start_hour: 调度开始时间, 单位为小时, 0~23。
        :type schedule_start_hour: int
        :param schedule_end_hour: 调度结束时间, 单位为小时, 0~23。
        :type schedule_end_hour: int
        :param schedule_period: 调度周期 * MINUTE  分钟为单位调度 * HOUR    小时为单位调度
        :type schedule_period: str
        :param schedule_interval: 调度间隔。
        :type schedule_interval: int
        :param schedule_status: 调度状态 * NOT_SCHEDULE  未启用任务调度 * SCHEDULING    任务调度中
        :type schedule_status: str
        :param sync_status: 同步状态 * UNKNOWN 未知 * NOT_SYNC 未同步 * SYNCING 同步中 * SYNC_SUCCESS 同步成功 * SYNC_FAIL 同步失败
        :type sync_status: str
        :param sync_msg: 同步日志。
        :type sync_msg: str
        :param sync_time: 同步时间。
        :type sync_time: int
        :param create_time: 创建时间。
        :type create_time: int
        :param create_user: 创建者。
        :type create_user: str
        :param update_time: 更新时间。
        :type update_time: int
        :param update_user: 更新者。
        :type update_user: str
        """
        
        super(ShowSecurityMemberSyncTaskResponse, self).__init__()

        self._id = None
        self._project_id = None
        self._domain_id = None
        self._instance_id = None
        self._data_connection_workspace = None
        self._cluster_type = None
        self._data_connection_id = None
        self._data_connection_name = None
        self._cluster_id = None
        self._cluster_name = None
        self._schedule_start_hour = None
        self._schedule_end_hour = None
        self._schedule_period = None
        self._schedule_interval = None
        self._schedule_status = None
        self._sync_status = None
        self._sync_msg = None
        self._sync_time = None
        self._create_time = None
        self._create_user = None
        self._update_time = None
        self._update_user = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if project_id is not None:
            self.project_id = project_id
        if domain_id is not None:
            self.domain_id = domain_id
        if instance_id is not None:
            self.instance_id = instance_id
        if data_connection_workspace is not None:
            self.data_connection_workspace = data_connection_workspace
        if cluster_type is not None:
            self.cluster_type = cluster_type
        if data_connection_id is not None:
            self.data_connection_id = data_connection_id
        if data_connection_name is not None:
            self.data_connection_name = data_connection_name
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if cluster_name is not None:
            self.cluster_name = cluster_name
        if schedule_start_hour is not None:
            self.schedule_start_hour = schedule_start_hour
        if schedule_end_hour is not None:
            self.schedule_end_hour = schedule_end_hour
        if schedule_period is not None:
            self.schedule_period = schedule_period
        if schedule_interval is not None:
            self.schedule_interval = schedule_interval
        if schedule_status is not None:
            self.schedule_status = schedule_status
        if sync_status is not None:
            self.sync_status = sync_status
        if sync_msg is not None:
            self.sync_msg = sync_msg
        if sync_time is not None:
            self.sync_time = sync_time
        if create_time is not None:
            self.create_time = create_time
        if create_user is not None:
            self.create_user = create_user
        if update_time is not None:
            self.update_time = update_time
        if update_user is not None:
            self.update_user = update_user

    @property
    def id(self):
        """Gets the id of this ShowSecurityMemberSyncTaskResponse.

        用户同步任务id。

        :return: The id of this ShowSecurityMemberSyncTaskResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShowSecurityMemberSyncTaskResponse.

        用户同步任务id。

        :param id: The id of this ShowSecurityMemberSyncTaskResponse.
        :type id: str
        """
        self._id = id

    @property
    def project_id(self):
        """Gets the project_id of this ShowSecurityMemberSyncTaskResponse.

        项目ID。

        :return: The project_id of this ShowSecurityMemberSyncTaskResponse.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this ShowSecurityMemberSyncTaskResponse.

        项目ID。

        :param project_id: The project_id of this ShowSecurityMemberSyncTaskResponse.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def domain_id(self):
        """Gets the domain_id of this ShowSecurityMemberSyncTaskResponse.

        租户ID。

        :return: The domain_id of this ShowSecurityMemberSyncTaskResponse.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this ShowSecurityMemberSyncTaskResponse.

        租户ID。

        :param domain_id: The domain_id of this ShowSecurityMemberSyncTaskResponse.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def instance_id(self):
        """Gets the instance_id of this ShowSecurityMemberSyncTaskResponse.

        实例ID。

        :return: The instance_id of this ShowSecurityMemberSyncTaskResponse.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ShowSecurityMemberSyncTaskResponse.

        实例ID。

        :param instance_id: The instance_id of this ShowSecurityMemberSyncTaskResponse.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def data_connection_workspace(self):
        """Gets the data_connection_workspace of this ShowSecurityMemberSyncTaskResponse.

        数据连接工作空间ID。

        :return: The data_connection_workspace of this ShowSecurityMemberSyncTaskResponse.
        :rtype: str
        """
        return self._data_connection_workspace

    @data_connection_workspace.setter
    def data_connection_workspace(self, data_connection_workspace):
        """Sets the data_connection_workspace of this ShowSecurityMemberSyncTaskResponse.

        数据连接工作空间ID。

        :param data_connection_workspace: The data_connection_workspace of this ShowSecurityMemberSyncTaskResponse.
        :type data_connection_workspace: str
        """
        self._data_connection_workspace = data_connection_workspace

    @property
    def cluster_type(self):
        """Gets the cluster_type of this ShowSecurityMemberSyncTaskResponse.

        集群类型 * MRS集群 * DWS集群

        :return: The cluster_type of this ShowSecurityMemberSyncTaskResponse.
        :rtype: str
        """
        return self._cluster_type

    @cluster_type.setter
    def cluster_type(self, cluster_type):
        """Sets the cluster_type of this ShowSecurityMemberSyncTaskResponse.

        集群类型 * MRS集群 * DWS集群

        :param cluster_type: The cluster_type of this ShowSecurityMemberSyncTaskResponse.
        :type cluster_type: str
        """
        self._cluster_type = cluster_type

    @property
    def data_connection_id(self):
        """Gets the data_connection_id of this ShowSecurityMemberSyncTaskResponse.

        数据连接id。

        :return: The data_connection_id of this ShowSecurityMemberSyncTaskResponse.
        :rtype: str
        """
        return self._data_connection_id

    @data_connection_id.setter
    def data_connection_id(self, data_connection_id):
        """Sets the data_connection_id of this ShowSecurityMemberSyncTaskResponse.

        数据连接id。

        :param data_connection_id: The data_connection_id of this ShowSecurityMemberSyncTaskResponse.
        :type data_connection_id: str
        """
        self._data_connection_id = data_connection_id

    @property
    def data_connection_name(self):
        """Gets the data_connection_name of this ShowSecurityMemberSyncTaskResponse.

        数据连接名称。

        :return: The data_connection_name of this ShowSecurityMemberSyncTaskResponse.
        :rtype: str
        """
        return self._data_connection_name

    @data_connection_name.setter
    def data_connection_name(self, data_connection_name):
        """Sets the data_connection_name of this ShowSecurityMemberSyncTaskResponse.

        数据连接名称。

        :param data_connection_name: The data_connection_name of this ShowSecurityMemberSyncTaskResponse.
        :type data_connection_name: str
        """
        self._data_connection_name = data_connection_name

    @property
    def cluster_id(self):
        """Gets the cluster_id of this ShowSecurityMemberSyncTaskResponse.

        集群id。

        :return: The cluster_id of this ShowSecurityMemberSyncTaskResponse.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this ShowSecurityMemberSyncTaskResponse.

        集群id。

        :param cluster_id: The cluster_id of this ShowSecurityMemberSyncTaskResponse.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def cluster_name(self):
        """Gets the cluster_name of this ShowSecurityMemberSyncTaskResponse.

        集群名称。

        :return: The cluster_name of this ShowSecurityMemberSyncTaskResponse.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        """Sets the cluster_name of this ShowSecurityMemberSyncTaskResponse.

        集群名称。

        :param cluster_name: The cluster_name of this ShowSecurityMemberSyncTaskResponse.
        :type cluster_name: str
        """
        self._cluster_name = cluster_name

    @property
    def schedule_start_hour(self):
        """Gets the schedule_start_hour of this ShowSecurityMemberSyncTaskResponse.

        调度开始时间, 单位为小时, 0~23。

        :return: The schedule_start_hour of this ShowSecurityMemberSyncTaskResponse.
        :rtype: int
        """
        return self._schedule_start_hour

    @schedule_start_hour.setter
    def schedule_start_hour(self, schedule_start_hour):
        """Sets the schedule_start_hour of this ShowSecurityMemberSyncTaskResponse.

        调度开始时间, 单位为小时, 0~23。

        :param schedule_start_hour: The schedule_start_hour of this ShowSecurityMemberSyncTaskResponse.
        :type schedule_start_hour: int
        """
        self._schedule_start_hour = schedule_start_hour

    @property
    def schedule_end_hour(self):
        """Gets the schedule_end_hour of this ShowSecurityMemberSyncTaskResponse.

        调度结束时间, 单位为小时, 0~23。

        :return: The schedule_end_hour of this ShowSecurityMemberSyncTaskResponse.
        :rtype: int
        """
        return self._schedule_end_hour

    @schedule_end_hour.setter
    def schedule_end_hour(self, schedule_end_hour):
        """Sets the schedule_end_hour of this ShowSecurityMemberSyncTaskResponse.

        调度结束时间, 单位为小时, 0~23。

        :param schedule_end_hour: The schedule_end_hour of this ShowSecurityMemberSyncTaskResponse.
        :type schedule_end_hour: int
        """
        self._schedule_end_hour = schedule_end_hour

    @property
    def schedule_period(self):
        """Gets the schedule_period of this ShowSecurityMemberSyncTaskResponse.

        调度周期 * MINUTE  分钟为单位调度 * HOUR    小时为单位调度

        :return: The schedule_period of this ShowSecurityMemberSyncTaskResponse.
        :rtype: str
        """
        return self._schedule_period

    @schedule_period.setter
    def schedule_period(self, schedule_period):
        """Sets the schedule_period of this ShowSecurityMemberSyncTaskResponse.

        调度周期 * MINUTE  分钟为单位调度 * HOUR    小时为单位调度

        :param schedule_period: The schedule_period of this ShowSecurityMemberSyncTaskResponse.
        :type schedule_period: str
        """
        self._schedule_period = schedule_period

    @property
    def schedule_interval(self):
        """Gets the schedule_interval of this ShowSecurityMemberSyncTaskResponse.

        调度间隔。

        :return: The schedule_interval of this ShowSecurityMemberSyncTaskResponse.
        :rtype: int
        """
        return self._schedule_interval

    @schedule_interval.setter
    def schedule_interval(self, schedule_interval):
        """Sets the schedule_interval of this ShowSecurityMemberSyncTaskResponse.

        调度间隔。

        :param schedule_interval: The schedule_interval of this ShowSecurityMemberSyncTaskResponse.
        :type schedule_interval: int
        """
        self._schedule_interval = schedule_interval

    @property
    def schedule_status(self):
        """Gets the schedule_status of this ShowSecurityMemberSyncTaskResponse.

        调度状态 * NOT_SCHEDULE  未启用任务调度 * SCHEDULING    任务调度中

        :return: The schedule_status of this ShowSecurityMemberSyncTaskResponse.
        :rtype: str
        """
        return self._schedule_status

    @schedule_status.setter
    def schedule_status(self, schedule_status):
        """Sets the schedule_status of this ShowSecurityMemberSyncTaskResponse.

        调度状态 * NOT_SCHEDULE  未启用任务调度 * SCHEDULING    任务调度中

        :param schedule_status: The schedule_status of this ShowSecurityMemberSyncTaskResponse.
        :type schedule_status: str
        """
        self._schedule_status = schedule_status

    @property
    def sync_status(self):
        """Gets the sync_status of this ShowSecurityMemberSyncTaskResponse.

        同步状态 * UNKNOWN 未知 * NOT_SYNC 未同步 * SYNCING 同步中 * SYNC_SUCCESS 同步成功 * SYNC_FAIL 同步失败

        :return: The sync_status of this ShowSecurityMemberSyncTaskResponse.
        :rtype: str
        """
        return self._sync_status

    @sync_status.setter
    def sync_status(self, sync_status):
        """Sets the sync_status of this ShowSecurityMemberSyncTaskResponse.

        同步状态 * UNKNOWN 未知 * NOT_SYNC 未同步 * SYNCING 同步中 * SYNC_SUCCESS 同步成功 * SYNC_FAIL 同步失败

        :param sync_status: The sync_status of this ShowSecurityMemberSyncTaskResponse.
        :type sync_status: str
        """
        self._sync_status = sync_status

    @property
    def sync_msg(self):
        """Gets the sync_msg of this ShowSecurityMemberSyncTaskResponse.

        同步日志。

        :return: The sync_msg of this ShowSecurityMemberSyncTaskResponse.
        :rtype: str
        """
        return self._sync_msg

    @sync_msg.setter
    def sync_msg(self, sync_msg):
        """Sets the sync_msg of this ShowSecurityMemberSyncTaskResponse.

        同步日志。

        :param sync_msg: The sync_msg of this ShowSecurityMemberSyncTaskResponse.
        :type sync_msg: str
        """
        self._sync_msg = sync_msg

    @property
    def sync_time(self):
        """Gets the sync_time of this ShowSecurityMemberSyncTaskResponse.

        同步时间。

        :return: The sync_time of this ShowSecurityMemberSyncTaskResponse.
        :rtype: int
        """
        return self._sync_time

    @sync_time.setter
    def sync_time(self, sync_time):
        """Sets the sync_time of this ShowSecurityMemberSyncTaskResponse.

        同步时间。

        :param sync_time: The sync_time of this ShowSecurityMemberSyncTaskResponse.
        :type sync_time: int
        """
        self._sync_time = sync_time

    @property
    def create_time(self):
        """Gets the create_time of this ShowSecurityMemberSyncTaskResponse.

        创建时间。

        :return: The create_time of this ShowSecurityMemberSyncTaskResponse.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ShowSecurityMemberSyncTaskResponse.

        创建时间。

        :param create_time: The create_time of this ShowSecurityMemberSyncTaskResponse.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def create_user(self):
        """Gets the create_user of this ShowSecurityMemberSyncTaskResponse.

        创建者。

        :return: The create_user of this ShowSecurityMemberSyncTaskResponse.
        :rtype: str
        """
        return self._create_user

    @create_user.setter
    def create_user(self, create_user):
        """Sets the create_user of this ShowSecurityMemberSyncTaskResponse.

        创建者。

        :param create_user: The create_user of this ShowSecurityMemberSyncTaskResponse.
        :type create_user: str
        """
        self._create_user = create_user

    @property
    def update_time(self):
        """Gets the update_time of this ShowSecurityMemberSyncTaskResponse.

        更新时间。

        :return: The update_time of this ShowSecurityMemberSyncTaskResponse.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this ShowSecurityMemberSyncTaskResponse.

        更新时间。

        :param update_time: The update_time of this ShowSecurityMemberSyncTaskResponse.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def update_user(self):
        """Gets the update_user of this ShowSecurityMemberSyncTaskResponse.

        更新者。

        :return: The update_user of this ShowSecurityMemberSyncTaskResponse.
        :rtype: str
        """
        return self._update_user

    @update_user.setter
    def update_user(self, update_user):
        """Sets the update_user of this ShowSecurityMemberSyncTaskResponse.

        更新者。

        :param update_user: The update_user of this ShowSecurityMemberSyncTaskResponse.
        :type update_user: str
        """
        self._update_user = update_user

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
        if not isinstance(other, ShowSecurityMemberSyncTaskResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
