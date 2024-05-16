# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSecurityMemberSyncTasksRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'workspace': 'str',
        'limit': 'int',
        'offset': 'int',
        'cluster_type': 'str',
        'cluster_name': 'str',
        'sync_status': 'str',
        'schedule_status': 'str',
        'order_by': 'str',
        'order_by_asc': 'bool'
    }

    attribute_map = {
        'workspace': 'workspace',
        'limit': 'limit',
        'offset': 'offset',
        'cluster_type': 'cluster_type',
        'cluster_name': 'cluster_name',
        'sync_status': 'sync_status',
        'schedule_status': 'schedule_status',
        'order_by': 'order_by',
        'order_by_asc': 'order_by_asc'
    }

    def __init__(self, workspace=None, limit=None, offset=None, cluster_type=None, cluster_name=None, sync_status=None, schedule_status=None, order_by=None, order_by_asc=None):
        """ListSecurityMemberSyncTasksRequest

        The model defined in huaweicloud sdk

        :param workspace: DataArts Studio工作空间ID
        :type workspace: str
        :param limit: limit
        :type limit: int
        :param offset: offset
        :type offset: int
        :param cluster_type: 集群类型 * MRS数据源 * DWS数据源
        :type cluster_type: str
        :param cluster_name: 集群名称
        :type cluster_name: str
        :param sync_status: 同步状态 * UNKNOWN 未知 * NOT_SYNC 未同步 * SYNCING 同步中 * SYNC_SUCCESS 同步成功 * SYNC_FAIL 同步失败
        :type sync_status: str
        :param schedule_status: 用户同步任务调度状态 * NOT_SCHEDULE 未启用调度 * SCHEDULING 调度中
        :type schedule_status: str
        :param order_by: 排序字段 * CLUSTER_NAME  按照集群名称排序 * CREATE_TIME   按照创建时间排序 * UPDATE_TIME   按照更新时间排序 * SYNC_TIME     按照同步时间排序
        :type order_by: str
        :param order_by_asc: 是否升序（仅指定排序参数时有效）。
        :type order_by_asc: bool
        """
        
        

        self._workspace = None
        self._limit = None
        self._offset = None
        self._cluster_type = None
        self._cluster_name = None
        self._sync_status = None
        self._schedule_status = None
        self._order_by = None
        self._order_by_asc = None
        self.discriminator = None

        self.workspace = workspace
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if cluster_type is not None:
            self.cluster_type = cluster_type
        if cluster_name is not None:
            self.cluster_name = cluster_name
        if sync_status is not None:
            self.sync_status = sync_status
        if schedule_status is not None:
            self.schedule_status = schedule_status
        if order_by is not None:
            self.order_by = order_by
        if order_by_asc is not None:
            self.order_by_asc = order_by_asc

    @property
    def workspace(self):
        """Gets the workspace of this ListSecurityMemberSyncTasksRequest.

        DataArts Studio工作空间ID

        :return: The workspace of this ListSecurityMemberSyncTasksRequest.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        """Sets the workspace of this ListSecurityMemberSyncTasksRequest.

        DataArts Studio工作空间ID

        :param workspace: The workspace of this ListSecurityMemberSyncTasksRequest.
        :type workspace: str
        """
        self._workspace = workspace

    @property
    def limit(self):
        """Gets the limit of this ListSecurityMemberSyncTasksRequest.

        limit

        :return: The limit of this ListSecurityMemberSyncTasksRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListSecurityMemberSyncTasksRequest.

        limit

        :param limit: The limit of this ListSecurityMemberSyncTasksRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListSecurityMemberSyncTasksRequest.

        offset

        :return: The offset of this ListSecurityMemberSyncTasksRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListSecurityMemberSyncTasksRequest.

        offset

        :param offset: The offset of this ListSecurityMemberSyncTasksRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def cluster_type(self):
        """Gets the cluster_type of this ListSecurityMemberSyncTasksRequest.

        集群类型 * MRS数据源 * DWS数据源

        :return: The cluster_type of this ListSecurityMemberSyncTasksRequest.
        :rtype: str
        """
        return self._cluster_type

    @cluster_type.setter
    def cluster_type(self, cluster_type):
        """Sets the cluster_type of this ListSecurityMemberSyncTasksRequest.

        集群类型 * MRS数据源 * DWS数据源

        :param cluster_type: The cluster_type of this ListSecurityMemberSyncTasksRequest.
        :type cluster_type: str
        """
        self._cluster_type = cluster_type

    @property
    def cluster_name(self):
        """Gets the cluster_name of this ListSecurityMemberSyncTasksRequest.

        集群名称

        :return: The cluster_name of this ListSecurityMemberSyncTasksRequest.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        """Sets the cluster_name of this ListSecurityMemberSyncTasksRequest.

        集群名称

        :param cluster_name: The cluster_name of this ListSecurityMemberSyncTasksRequest.
        :type cluster_name: str
        """
        self._cluster_name = cluster_name

    @property
    def sync_status(self):
        """Gets the sync_status of this ListSecurityMemberSyncTasksRequest.

        同步状态 * UNKNOWN 未知 * NOT_SYNC 未同步 * SYNCING 同步中 * SYNC_SUCCESS 同步成功 * SYNC_FAIL 同步失败

        :return: The sync_status of this ListSecurityMemberSyncTasksRequest.
        :rtype: str
        """
        return self._sync_status

    @sync_status.setter
    def sync_status(self, sync_status):
        """Sets the sync_status of this ListSecurityMemberSyncTasksRequest.

        同步状态 * UNKNOWN 未知 * NOT_SYNC 未同步 * SYNCING 同步中 * SYNC_SUCCESS 同步成功 * SYNC_FAIL 同步失败

        :param sync_status: The sync_status of this ListSecurityMemberSyncTasksRequest.
        :type sync_status: str
        """
        self._sync_status = sync_status

    @property
    def schedule_status(self):
        """Gets the schedule_status of this ListSecurityMemberSyncTasksRequest.

        用户同步任务调度状态 * NOT_SCHEDULE 未启用调度 * SCHEDULING 调度中

        :return: The schedule_status of this ListSecurityMemberSyncTasksRequest.
        :rtype: str
        """
        return self._schedule_status

    @schedule_status.setter
    def schedule_status(self, schedule_status):
        """Sets the schedule_status of this ListSecurityMemberSyncTasksRequest.

        用户同步任务调度状态 * NOT_SCHEDULE 未启用调度 * SCHEDULING 调度中

        :param schedule_status: The schedule_status of this ListSecurityMemberSyncTasksRequest.
        :type schedule_status: str
        """
        self._schedule_status = schedule_status

    @property
    def order_by(self):
        """Gets the order_by of this ListSecurityMemberSyncTasksRequest.

        排序字段 * CLUSTER_NAME  按照集群名称排序 * CREATE_TIME   按照创建时间排序 * UPDATE_TIME   按照更新时间排序 * SYNC_TIME     按照同步时间排序

        :return: The order_by of this ListSecurityMemberSyncTasksRequest.
        :rtype: str
        """
        return self._order_by

    @order_by.setter
    def order_by(self, order_by):
        """Sets the order_by of this ListSecurityMemberSyncTasksRequest.

        排序字段 * CLUSTER_NAME  按照集群名称排序 * CREATE_TIME   按照创建时间排序 * UPDATE_TIME   按照更新时间排序 * SYNC_TIME     按照同步时间排序

        :param order_by: The order_by of this ListSecurityMemberSyncTasksRequest.
        :type order_by: str
        """
        self._order_by = order_by

    @property
    def order_by_asc(self):
        """Gets the order_by_asc of this ListSecurityMemberSyncTasksRequest.

        是否升序（仅指定排序参数时有效）。

        :return: The order_by_asc of this ListSecurityMemberSyncTasksRequest.
        :rtype: bool
        """
        return self._order_by_asc

    @order_by_asc.setter
    def order_by_asc(self, order_by_asc):
        """Sets the order_by_asc of this ListSecurityMemberSyncTasksRequest.

        是否升序（仅指定排序参数时有效）。

        :param order_by_asc: The order_by_asc of this ListSecurityMemberSyncTasksRequest.
        :type order_by_asc: bool
        """
        self._order_by_asc = order_by_asc

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
        if not isinstance(other, ListSecurityMemberSyncTasksRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
