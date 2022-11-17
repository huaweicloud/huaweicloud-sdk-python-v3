# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowProtectedInstanceParams:

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
        'source_server': 'str',
        'target_server': 'str',
        'server_group_id': 'str',
        'created_at': 'str',
        'updated_at': 'str',
        'metadata': 'MetadataParams',
        'attachment': 'list[ProtectedInstanceAttachment]',
        'tags': 'list[ResourceTag]',
        'progress': 'int',
        'priority_station': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'status': 'status',
        'source_server': 'source_server',
        'target_server': 'target_server',
        'server_group_id': 'server_group_id',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'metadata': 'metadata',
        'attachment': 'attachment',
        'tags': 'tags',
        'progress': 'progress',
        'priority_station': 'priority_station'
    }

    def __init__(self, id=None, name=None, description=None, status=None, source_server=None, target_server=None, server_group_id=None, created_at=None, updated_at=None, metadata=None, attachment=None, tags=None, progress=None, priority_station=None):
        """ShowProtectedInstanceParams

        The model defined in huaweicloud sdk

        :param id: 保护实例的ID。
        :type id: str
        :param name: 保护实例的名称。
        :type name: str
        :param description: 保护实例的描述。
        :type description: str
        :param status: 保护实例的状态。
        :type status: str
        :param source_server: 生产站点云服务器ID。
        :type source_server: str
        :param target_server: 容灾站点云服务器ID。
        :type target_server: str
        :param server_group_id: 保护组的ID。
        :type server_group_id: str
        :param created_at: 创建时间。默认格式为：\&quot;yyyy-MM-dd HH:mm:ss.SSS\&quot;，例：\&quot;2019-04-01 12:00:00.000\&quot;。
        :type created_at: str
        :param updated_at: 更新时间。默认格式为：\&quot;yyyy-MM-dd HH:mm:ss.SSS\&quot;，例：\&quot;2019-04-01 12:00:00.000\&quot;。
        :type updated_at: str
        :param metadata: 
        :type metadata: :class:`huaweicloudsdksdrs.v1.MetadataParams`
        :param attachment: 挂载的复制对列表。
        :type attachment: list[:class:`huaweicloudsdksdrs.v1.ProtectedInstanceAttachment`]
        :param tags: 标签列表。
        :type tags: list[:class:`huaweicloudsdksdrs.v1.ResourceTag`]
        :param progress: 保护实例的同步进度。单位：百分比（%）。
        :type progress: int
        :param priority_station: 标识保护实例所在保护组的当前生产站点可用区。source：表示当前生产站点可用区为保护组source_availability_zone的值。target：表示当前生产站点可用区为保护组的target_availability_zone的值。
        :type priority_station: str
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._status = None
        self._source_server = None
        self._target_server = None
        self._server_group_id = None
        self._created_at = None
        self._updated_at = None
        self._metadata = None
        self._attachment = None
        self._tags = None
        self._progress = None
        self._priority_station = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.description = description
        self.status = status
        self.source_server = source_server
        self.target_server = target_server
        self.server_group_id = server_group_id
        self.created_at = created_at
        self.updated_at = updated_at
        self.metadata = metadata
        self.attachment = attachment
        if tags is not None:
            self.tags = tags
        self.progress = progress
        self.priority_station = priority_station

    @property
    def id(self):
        """Gets the id of this ShowProtectedInstanceParams.

        保护实例的ID。

        :return: The id of this ShowProtectedInstanceParams.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShowProtectedInstanceParams.

        保护实例的ID。

        :param id: The id of this ShowProtectedInstanceParams.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ShowProtectedInstanceParams.

        保护实例的名称。

        :return: The name of this ShowProtectedInstanceParams.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ShowProtectedInstanceParams.

        保护实例的名称。

        :param name: The name of this ShowProtectedInstanceParams.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this ShowProtectedInstanceParams.

        保护实例的描述。

        :return: The description of this ShowProtectedInstanceParams.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ShowProtectedInstanceParams.

        保护实例的描述。

        :param description: The description of this ShowProtectedInstanceParams.
        :type description: str
        """
        self._description = description

    @property
    def status(self):
        """Gets the status of this ShowProtectedInstanceParams.

        保护实例的状态。

        :return: The status of this ShowProtectedInstanceParams.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShowProtectedInstanceParams.

        保护实例的状态。

        :param status: The status of this ShowProtectedInstanceParams.
        :type status: str
        """
        self._status = status

    @property
    def source_server(self):
        """Gets the source_server of this ShowProtectedInstanceParams.

        生产站点云服务器ID。

        :return: The source_server of this ShowProtectedInstanceParams.
        :rtype: str
        """
        return self._source_server

    @source_server.setter
    def source_server(self, source_server):
        """Sets the source_server of this ShowProtectedInstanceParams.

        生产站点云服务器ID。

        :param source_server: The source_server of this ShowProtectedInstanceParams.
        :type source_server: str
        """
        self._source_server = source_server

    @property
    def target_server(self):
        """Gets the target_server of this ShowProtectedInstanceParams.

        容灾站点云服务器ID。

        :return: The target_server of this ShowProtectedInstanceParams.
        :rtype: str
        """
        return self._target_server

    @target_server.setter
    def target_server(self, target_server):
        """Sets the target_server of this ShowProtectedInstanceParams.

        容灾站点云服务器ID。

        :param target_server: The target_server of this ShowProtectedInstanceParams.
        :type target_server: str
        """
        self._target_server = target_server

    @property
    def server_group_id(self):
        """Gets the server_group_id of this ShowProtectedInstanceParams.

        保护组的ID。

        :return: The server_group_id of this ShowProtectedInstanceParams.
        :rtype: str
        """
        return self._server_group_id

    @server_group_id.setter
    def server_group_id(self, server_group_id):
        """Sets the server_group_id of this ShowProtectedInstanceParams.

        保护组的ID。

        :param server_group_id: The server_group_id of this ShowProtectedInstanceParams.
        :type server_group_id: str
        """
        self._server_group_id = server_group_id

    @property
    def created_at(self):
        """Gets the created_at of this ShowProtectedInstanceParams.

        创建时间。默认格式为：\"yyyy-MM-dd HH:mm:ss.SSS\"，例：\"2019-04-01 12:00:00.000\"。

        :return: The created_at of this ShowProtectedInstanceParams.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ShowProtectedInstanceParams.

        创建时间。默认格式为：\"yyyy-MM-dd HH:mm:ss.SSS\"，例：\"2019-04-01 12:00:00.000\"。

        :param created_at: The created_at of this ShowProtectedInstanceParams.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this ShowProtectedInstanceParams.

        更新时间。默认格式为：\"yyyy-MM-dd HH:mm:ss.SSS\"，例：\"2019-04-01 12:00:00.000\"。

        :return: The updated_at of this ShowProtectedInstanceParams.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this ShowProtectedInstanceParams.

        更新时间。默认格式为：\"yyyy-MM-dd HH:mm:ss.SSS\"，例：\"2019-04-01 12:00:00.000\"。

        :param updated_at: The updated_at of this ShowProtectedInstanceParams.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def metadata(self):
        """Gets the metadata of this ShowProtectedInstanceParams.

        :return: The metadata of this ShowProtectedInstanceParams.
        :rtype: :class:`huaweicloudsdksdrs.v1.MetadataParams`
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this ShowProtectedInstanceParams.

        :param metadata: The metadata of this ShowProtectedInstanceParams.
        :type metadata: :class:`huaweicloudsdksdrs.v1.MetadataParams`
        """
        self._metadata = metadata

    @property
    def attachment(self):
        """Gets the attachment of this ShowProtectedInstanceParams.

        挂载的复制对列表。

        :return: The attachment of this ShowProtectedInstanceParams.
        :rtype: list[:class:`huaweicloudsdksdrs.v1.ProtectedInstanceAttachment`]
        """
        return self._attachment

    @attachment.setter
    def attachment(self, attachment):
        """Sets the attachment of this ShowProtectedInstanceParams.

        挂载的复制对列表。

        :param attachment: The attachment of this ShowProtectedInstanceParams.
        :type attachment: list[:class:`huaweicloudsdksdrs.v1.ProtectedInstanceAttachment`]
        """
        self._attachment = attachment

    @property
    def tags(self):
        """Gets the tags of this ShowProtectedInstanceParams.

        标签列表。

        :return: The tags of this ShowProtectedInstanceParams.
        :rtype: list[:class:`huaweicloudsdksdrs.v1.ResourceTag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ShowProtectedInstanceParams.

        标签列表。

        :param tags: The tags of this ShowProtectedInstanceParams.
        :type tags: list[:class:`huaweicloudsdksdrs.v1.ResourceTag`]
        """
        self._tags = tags

    @property
    def progress(self):
        """Gets the progress of this ShowProtectedInstanceParams.

        保护实例的同步进度。单位：百分比（%）。

        :return: The progress of this ShowProtectedInstanceParams.
        :rtype: int
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        """Sets the progress of this ShowProtectedInstanceParams.

        保护实例的同步进度。单位：百分比（%）。

        :param progress: The progress of this ShowProtectedInstanceParams.
        :type progress: int
        """
        self._progress = progress

    @property
    def priority_station(self):
        """Gets the priority_station of this ShowProtectedInstanceParams.

        标识保护实例所在保护组的当前生产站点可用区。source：表示当前生产站点可用区为保护组source_availability_zone的值。target：表示当前生产站点可用区为保护组的target_availability_zone的值。

        :return: The priority_station of this ShowProtectedInstanceParams.
        :rtype: str
        """
        return self._priority_station

    @priority_station.setter
    def priority_station(self, priority_station):
        """Sets the priority_station of this ShowProtectedInstanceParams.

        标识保护实例所在保护组的当前生产站点可用区。source：表示当前生产站点可用区为保护组source_availability_zone的值。target：表示当前生产站点可用区为保护组的target_availability_zone的值。

        :param priority_station: The priority_station of this ShowProtectedInstanceParams.
        :type priority_station: str
        """
        self._priority_station = priority_station

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
        if not isinstance(other, ShowProtectedInstanceParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
