# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowReplicationParams:

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
        'description': 'str',
        'status': 'str',
        'volume_ids': 'str',
        'attachment': 'list[ReplicationAttachment]',
        'created_at': 'str',
        'updated_at': 'str',
        'replication_model': 'str',
        'progress': 'int',
        'failure_detail': 'str',
        'record_metadata': 'ReplicationRecordMetadata',
        'fault_level': 'str',
        'server_group_id': 'str',
        'priority_station': 'str',
        'replication_status': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'status': 'status',
        'volume_ids': 'volume_ids',
        'attachment': 'attachment',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'replication_model': 'replication_model',
        'progress': 'progress',
        'failure_detail': 'failure_detail',
        'record_metadata': 'record_metadata',
        'fault_level': 'fault_level',
        'server_group_id': 'server_group_id',
        'priority_station': 'priority_station',
        'replication_status': 'replication_status'
    }

    def __init__(self, id=None, name=None, description=None, status=None, volume_ids=None, attachment=None, created_at=None, updated_at=None, replication_model=None, progress=None, failure_detail=None, record_metadata=None, fault_level=None, server_group_id=None, priority_station=None, replication_status=None):
        """ShowReplicationParams

        The model defined in huaweicloud sdk

        :param id: 复制对的ID。
        :type id: str
        :param name: 复制对的名称。
        :type name: str
        :param description: 复制对的描述。
        :type description: str
        :param status: 复制对的状态。
        :type status: str
        :param volume_ids: 复制对使用的云硬盘ID。
        :type volume_ids: str
        :param attachment: 挂载点。
        :type attachment: list[:class:`huaweicloudsdksdrs.v1.ReplicationAttachment`]
        :param created_at: 创建时间。默认格式为：\&quot;yyyy-MM-ddTHH:mm:ss.SSSZ\&quot;，例如：\&quot;2019-04-01T12:00:00.000Z\&quot;
        :type created_at: str
        :param updated_at: 更新时间。默认格式为：\&quot;yyyy-MM-ddTHH:mm:ss.SSSZ\&quot;，例如：\&quot;2019-04-01T12:00:00.000Z\&quot;
        :type updated_at: str
        :param replication_model: 复制对的复制类型。默认值为“hypermetro”，表示同步复制。
        :type replication_model: str
        :param progress: 复制对的同步进度。单位：百分比（%）。
        :type progress: int
        :param failure_detail: 仅在复制对的状态“status”为“error”时，返回的错误码。
        :type failure_detail: str
        :param record_metadata: 
        :type record_metadata: :class:`huaweicloudsdksdrs.v1.ReplicationRecordMetadata`
        :param fault_level: 复制对的故障等级。0：表示无故障。2：表示当前生产站点的云硬盘无读写数据权限，此时建议执行故障切换操作。5：表示复制链路已断，不能执行故障切换操作，需联系技术支持工程师。
        :type fault_level: str
        :param server_group_id: 保护组的ID。
        :type server_group_id: str
        :param priority_station: 标识复制对所在保护组的当前生产站点可用区。source：表示当前生产站点可用区为保护组source_availability_zone的值。target：表示当前生产站点可用区为保护组target_availability_zone的值。
        :type priority_station: str
        :param replication_status: 数据同步状态。active：表示数据已同步完成。inactive：表示数据未同步。copying：表示数据正在同步。active-stopped：表示数据已停止同步。
        :type replication_status: str
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._status = None
        self._volume_ids = None
        self._attachment = None
        self._created_at = None
        self._updated_at = None
        self._replication_model = None
        self._progress = None
        self._failure_detail = None
        self._record_metadata = None
        self._fault_level = None
        self._server_group_id = None
        self._priority_station = None
        self._replication_status = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.description = description
        self.status = status
        self.volume_ids = volume_ids
        self.attachment = attachment
        self.created_at = created_at
        self.updated_at = updated_at
        self.replication_model = replication_model
        self.progress = progress
        self.failure_detail = failure_detail
        self.record_metadata = record_metadata
        self.fault_level = fault_level
        self.server_group_id = server_group_id
        self.priority_station = priority_station
        self.replication_status = replication_status

    @property
    def id(self):
        """Gets the id of this ShowReplicationParams.

        复制对的ID。

        :return: The id of this ShowReplicationParams.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShowReplicationParams.

        复制对的ID。

        :param id: The id of this ShowReplicationParams.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ShowReplicationParams.

        复制对的名称。

        :return: The name of this ShowReplicationParams.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ShowReplicationParams.

        复制对的名称。

        :param name: The name of this ShowReplicationParams.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this ShowReplicationParams.

        复制对的描述。

        :return: The description of this ShowReplicationParams.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ShowReplicationParams.

        复制对的描述。

        :param description: The description of this ShowReplicationParams.
        :type description: str
        """
        self._description = description

    @property
    def status(self):
        """Gets the status of this ShowReplicationParams.

        复制对的状态。

        :return: The status of this ShowReplicationParams.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShowReplicationParams.

        复制对的状态。

        :param status: The status of this ShowReplicationParams.
        :type status: str
        """
        self._status = status

    @property
    def volume_ids(self):
        """Gets the volume_ids of this ShowReplicationParams.

        复制对使用的云硬盘ID。

        :return: The volume_ids of this ShowReplicationParams.
        :rtype: str
        """
        return self._volume_ids

    @volume_ids.setter
    def volume_ids(self, volume_ids):
        """Sets the volume_ids of this ShowReplicationParams.

        复制对使用的云硬盘ID。

        :param volume_ids: The volume_ids of this ShowReplicationParams.
        :type volume_ids: str
        """
        self._volume_ids = volume_ids

    @property
    def attachment(self):
        """Gets the attachment of this ShowReplicationParams.

        挂载点。

        :return: The attachment of this ShowReplicationParams.
        :rtype: list[:class:`huaweicloudsdksdrs.v1.ReplicationAttachment`]
        """
        return self._attachment

    @attachment.setter
    def attachment(self, attachment):
        """Sets the attachment of this ShowReplicationParams.

        挂载点。

        :param attachment: The attachment of this ShowReplicationParams.
        :type attachment: list[:class:`huaweicloudsdksdrs.v1.ReplicationAttachment`]
        """
        self._attachment = attachment

    @property
    def created_at(self):
        """Gets the created_at of this ShowReplicationParams.

        创建时间。默认格式为：\"yyyy-MM-ddTHH:mm:ss.SSSZ\"，例如：\"2019-04-01T12:00:00.000Z\"

        :return: The created_at of this ShowReplicationParams.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ShowReplicationParams.

        创建时间。默认格式为：\"yyyy-MM-ddTHH:mm:ss.SSSZ\"，例如：\"2019-04-01T12:00:00.000Z\"

        :param created_at: The created_at of this ShowReplicationParams.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this ShowReplicationParams.

        更新时间。默认格式为：\"yyyy-MM-ddTHH:mm:ss.SSSZ\"，例如：\"2019-04-01T12:00:00.000Z\"

        :return: The updated_at of this ShowReplicationParams.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this ShowReplicationParams.

        更新时间。默认格式为：\"yyyy-MM-ddTHH:mm:ss.SSSZ\"，例如：\"2019-04-01T12:00:00.000Z\"

        :param updated_at: The updated_at of this ShowReplicationParams.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def replication_model(self):
        """Gets the replication_model of this ShowReplicationParams.

        复制对的复制类型。默认值为“hypermetro”，表示同步复制。

        :return: The replication_model of this ShowReplicationParams.
        :rtype: str
        """
        return self._replication_model

    @replication_model.setter
    def replication_model(self, replication_model):
        """Sets the replication_model of this ShowReplicationParams.

        复制对的复制类型。默认值为“hypermetro”，表示同步复制。

        :param replication_model: The replication_model of this ShowReplicationParams.
        :type replication_model: str
        """
        self._replication_model = replication_model

    @property
    def progress(self):
        """Gets the progress of this ShowReplicationParams.

        复制对的同步进度。单位：百分比（%）。

        :return: The progress of this ShowReplicationParams.
        :rtype: int
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        """Sets the progress of this ShowReplicationParams.

        复制对的同步进度。单位：百分比（%）。

        :param progress: The progress of this ShowReplicationParams.
        :type progress: int
        """
        self._progress = progress

    @property
    def failure_detail(self):
        """Gets the failure_detail of this ShowReplicationParams.

        仅在复制对的状态“status”为“error”时，返回的错误码。

        :return: The failure_detail of this ShowReplicationParams.
        :rtype: str
        """
        return self._failure_detail

    @failure_detail.setter
    def failure_detail(self, failure_detail):
        """Sets the failure_detail of this ShowReplicationParams.

        仅在复制对的状态“status”为“error”时，返回的错误码。

        :param failure_detail: The failure_detail of this ShowReplicationParams.
        :type failure_detail: str
        """
        self._failure_detail = failure_detail

    @property
    def record_metadata(self):
        """Gets the record_metadata of this ShowReplicationParams.

        :return: The record_metadata of this ShowReplicationParams.
        :rtype: :class:`huaweicloudsdksdrs.v1.ReplicationRecordMetadata`
        """
        return self._record_metadata

    @record_metadata.setter
    def record_metadata(self, record_metadata):
        """Sets the record_metadata of this ShowReplicationParams.

        :param record_metadata: The record_metadata of this ShowReplicationParams.
        :type record_metadata: :class:`huaweicloudsdksdrs.v1.ReplicationRecordMetadata`
        """
        self._record_metadata = record_metadata

    @property
    def fault_level(self):
        """Gets the fault_level of this ShowReplicationParams.

        复制对的故障等级。0：表示无故障。2：表示当前生产站点的云硬盘无读写数据权限，此时建议执行故障切换操作。5：表示复制链路已断，不能执行故障切换操作，需联系技术支持工程师。

        :return: The fault_level of this ShowReplicationParams.
        :rtype: str
        """
        return self._fault_level

    @fault_level.setter
    def fault_level(self, fault_level):
        """Sets the fault_level of this ShowReplicationParams.

        复制对的故障等级。0：表示无故障。2：表示当前生产站点的云硬盘无读写数据权限，此时建议执行故障切换操作。5：表示复制链路已断，不能执行故障切换操作，需联系技术支持工程师。

        :param fault_level: The fault_level of this ShowReplicationParams.
        :type fault_level: str
        """
        self._fault_level = fault_level

    @property
    def server_group_id(self):
        """Gets the server_group_id of this ShowReplicationParams.

        保护组的ID。

        :return: The server_group_id of this ShowReplicationParams.
        :rtype: str
        """
        return self._server_group_id

    @server_group_id.setter
    def server_group_id(self, server_group_id):
        """Sets the server_group_id of this ShowReplicationParams.

        保护组的ID。

        :param server_group_id: The server_group_id of this ShowReplicationParams.
        :type server_group_id: str
        """
        self._server_group_id = server_group_id

    @property
    def priority_station(self):
        """Gets the priority_station of this ShowReplicationParams.

        标识复制对所在保护组的当前生产站点可用区。source：表示当前生产站点可用区为保护组source_availability_zone的值。target：表示当前生产站点可用区为保护组target_availability_zone的值。

        :return: The priority_station of this ShowReplicationParams.
        :rtype: str
        """
        return self._priority_station

    @priority_station.setter
    def priority_station(self, priority_station):
        """Sets the priority_station of this ShowReplicationParams.

        标识复制对所在保护组的当前生产站点可用区。source：表示当前生产站点可用区为保护组source_availability_zone的值。target：表示当前生产站点可用区为保护组target_availability_zone的值。

        :param priority_station: The priority_station of this ShowReplicationParams.
        :type priority_station: str
        """
        self._priority_station = priority_station

    @property
    def replication_status(self):
        """Gets the replication_status of this ShowReplicationParams.

        数据同步状态。active：表示数据已同步完成。inactive：表示数据未同步。copying：表示数据正在同步。active-stopped：表示数据已停止同步。

        :return: The replication_status of this ShowReplicationParams.
        :rtype: str
        """
        return self._replication_status

    @replication_status.setter
    def replication_status(self, replication_status):
        """Sets the replication_status of this ShowReplicationParams.

        数据同步状态。active：表示数据已同步完成。inactive：表示数据未同步。copying：表示数据正在同步。active-stopped：表示数据已停止同步。

        :param replication_status: The replication_status of this ShowReplicationParams.
        :type replication_status: str
        """
        self._replication_status = replication_status

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
        if not isinstance(other, ShowReplicationParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
