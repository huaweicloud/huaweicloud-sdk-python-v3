# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SnapshotList:

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
        'status': 'str',
        'name': 'str',
        'description': 'str',
        'created_at': 'str',
        'updated_at': 'str',
        'metadata': 'dict(str, str)',
        'volume_id': 'str',
        'size': 'int',
        'os_extended_snapshot_attributesproject_id': 'str',
        'os_extended_snapshot_attributesprogress': 'str',
        'dedicated_storage_id': 'str',
        'dedicated_storage_name': 'str',
        'service_type': 'str'
    }

    attribute_map = {
        'id': 'id',
        'status': 'status',
        'name': 'name',
        'description': 'description',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'metadata': 'metadata',
        'volume_id': 'volume_id',
        'size': 'size',
        'os_extended_snapshot_attributesproject_id': 'os-extended-snapshot-attributes:project_id',
        'os_extended_snapshot_attributesprogress': 'os-extended-snapshot-attributes:progress',
        'dedicated_storage_id': 'dedicated_storage_id',
        'dedicated_storage_name': 'dedicated_storage_name',
        'service_type': 'service_type'
    }

    def __init__(self, id=None, status=None, name=None, description=None, created_at=None, updated_at=None, metadata=None, volume_id=None, size=None, os_extended_snapshot_attributesproject_id=None, os_extended_snapshot_attributesprogress=None, dedicated_storage_id=None, dedicated_storage_name=None, service_type=None):
        """SnapshotList

        The model defined in huaweicloud sdk

        :param id: 云硬盘快照ID。
        :type id: str
        :param status: 云硬盘快照的状态。
        :type status: str
        :param name: 云硬盘快照名称。
        :type name: str
        :param description: 云硬盘快照描述信息。
        :type description: str
        :param created_at: 云硬盘快照创建时间。
        :type created_at: str
        :param updated_at: 云硬盘快照更新时间。
        :type updated_at: str
        :param metadata: 云硬盘快照的元数据信息。
        :type metadata: dict(str, str)
        :param volume_id: 快照所属的云硬盘。
        :type volume_id: str
        :param size: 云硬盘快照大小。
        :type size: int
        :param os_extended_snapshot_attributesproject_id: 项目ID。
        :type os_extended_snapshot_attributesproject_id: str
        :param os_extended_snapshot_attributesprogress: 快照进度。
        :type os_extended_snapshot_attributesprogress: str
        :param dedicated_storage_id: 专属存储ID。
        :type dedicated_storage_id: str
        :param dedicated_storage_name: 专属存储名称。
        :type dedicated_storage_name: str
        :param service_type: 服务类型。
        :type service_type: str
        """
        
        

        self._id = None
        self._status = None
        self._name = None
        self._description = None
        self._created_at = None
        self._updated_at = None
        self._metadata = None
        self._volume_id = None
        self._size = None
        self._os_extended_snapshot_attributesproject_id = None
        self._os_extended_snapshot_attributesprogress = None
        self._dedicated_storage_id = None
        self._dedicated_storage_name = None
        self._service_type = None
        self.discriminator = None

        self.id = id
        self.status = status
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if metadata is not None:
            self.metadata = metadata
        self.volume_id = volume_id
        self.size = size
        self.os_extended_snapshot_attributesproject_id = os_extended_snapshot_attributesproject_id
        self.os_extended_snapshot_attributesprogress = os_extended_snapshot_attributesprogress
        if dedicated_storage_id is not None:
            self.dedicated_storage_id = dedicated_storage_id
        if dedicated_storage_name is not None:
            self.dedicated_storage_name = dedicated_storage_name
        self.service_type = service_type

    @property
    def id(self):
        """Gets the id of this SnapshotList.

        云硬盘快照ID。

        :return: The id of this SnapshotList.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SnapshotList.

        云硬盘快照ID。

        :param id: The id of this SnapshotList.
        :type id: str
        """
        self._id = id

    @property
    def status(self):
        """Gets the status of this SnapshotList.

        云硬盘快照的状态。

        :return: The status of this SnapshotList.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this SnapshotList.

        云硬盘快照的状态。

        :param status: The status of this SnapshotList.
        :type status: str
        """
        self._status = status

    @property
    def name(self):
        """Gets the name of this SnapshotList.

        云硬盘快照名称。

        :return: The name of this SnapshotList.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SnapshotList.

        云硬盘快照名称。

        :param name: The name of this SnapshotList.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this SnapshotList.

        云硬盘快照描述信息。

        :return: The description of this SnapshotList.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this SnapshotList.

        云硬盘快照描述信息。

        :param description: The description of this SnapshotList.
        :type description: str
        """
        self._description = description

    @property
    def created_at(self):
        """Gets the created_at of this SnapshotList.

        云硬盘快照创建时间。

        :return: The created_at of this SnapshotList.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this SnapshotList.

        云硬盘快照创建时间。

        :param created_at: The created_at of this SnapshotList.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this SnapshotList.

        云硬盘快照更新时间。

        :return: The updated_at of this SnapshotList.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this SnapshotList.

        云硬盘快照更新时间。

        :param updated_at: The updated_at of this SnapshotList.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def metadata(self):
        """Gets the metadata of this SnapshotList.

        云硬盘快照的元数据信息。

        :return: The metadata of this SnapshotList.
        :rtype: dict(str, str)
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this SnapshotList.

        云硬盘快照的元数据信息。

        :param metadata: The metadata of this SnapshotList.
        :type metadata: dict(str, str)
        """
        self._metadata = metadata

    @property
    def volume_id(self):
        """Gets the volume_id of this SnapshotList.

        快照所属的云硬盘。

        :return: The volume_id of this SnapshotList.
        :rtype: str
        """
        return self._volume_id

    @volume_id.setter
    def volume_id(self, volume_id):
        """Sets the volume_id of this SnapshotList.

        快照所属的云硬盘。

        :param volume_id: The volume_id of this SnapshotList.
        :type volume_id: str
        """
        self._volume_id = volume_id

    @property
    def size(self):
        """Gets the size of this SnapshotList.

        云硬盘快照大小。

        :return: The size of this SnapshotList.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this SnapshotList.

        云硬盘快照大小。

        :param size: The size of this SnapshotList.
        :type size: int
        """
        self._size = size

    @property
    def os_extended_snapshot_attributesproject_id(self):
        """Gets the os_extended_snapshot_attributesproject_id of this SnapshotList.

        项目ID。

        :return: The os_extended_snapshot_attributesproject_id of this SnapshotList.
        :rtype: str
        """
        return self._os_extended_snapshot_attributesproject_id

    @os_extended_snapshot_attributesproject_id.setter
    def os_extended_snapshot_attributesproject_id(self, os_extended_snapshot_attributesproject_id):
        """Sets the os_extended_snapshot_attributesproject_id of this SnapshotList.

        项目ID。

        :param os_extended_snapshot_attributesproject_id: The os_extended_snapshot_attributesproject_id of this SnapshotList.
        :type os_extended_snapshot_attributesproject_id: str
        """
        self._os_extended_snapshot_attributesproject_id = os_extended_snapshot_attributesproject_id

    @property
    def os_extended_snapshot_attributesprogress(self):
        """Gets the os_extended_snapshot_attributesprogress of this SnapshotList.

        快照进度。

        :return: The os_extended_snapshot_attributesprogress of this SnapshotList.
        :rtype: str
        """
        return self._os_extended_snapshot_attributesprogress

    @os_extended_snapshot_attributesprogress.setter
    def os_extended_snapshot_attributesprogress(self, os_extended_snapshot_attributesprogress):
        """Sets the os_extended_snapshot_attributesprogress of this SnapshotList.

        快照进度。

        :param os_extended_snapshot_attributesprogress: The os_extended_snapshot_attributesprogress of this SnapshotList.
        :type os_extended_snapshot_attributesprogress: str
        """
        self._os_extended_snapshot_attributesprogress = os_extended_snapshot_attributesprogress

    @property
    def dedicated_storage_id(self):
        """Gets the dedicated_storage_id of this SnapshotList.

        专属存储ID。

        :return: The dedicated_storage_id of this SnapshotList.
        :rtype: str
        """
        return self._dedicated_storage_id

    @dedicated_storage_id.setter
    def dedicated_storage_id(self, dedicated_storage_id):
        """Sets the dedicated_storage_id of this SnapshotList.

        专属存储ID。

        :param dedicated_storage_id: The dedicated_storage_id of this SnapshotList.
        :type dedicated_storage_id: str
        """
        self._dedicated_storage_id = dedicated_storage_id

    @property
    def dedicated_storage_name(self):
        """Gets the dedicated_storage_name of this SnapshotList.

        专属存储名称。

        :return: The dedicated_storage_name of this SnapshotList.
        :rtype: str
        """
        return self._dedicated_storage_name

    @dedicated_storage_name.setter
    def dedicated_storage_name(self, dedicated_storage_name):
        """Sets the dedicated_storage_name of this SnapshotList.

        专属存储名称。

        :param dedicated_storage_name: The dedicated_storage_name of this SnapshotList.
        :type dedicated_storage_name: str
        """
        self._dedicated_storage_name = dedicated_storage_name

    @property
    def service_type(self):
        """Gets the service_type of this SnapshotList.

        服务类型。

        :return: The service_type of this SnapshotList.
        :rtype: str
        """
        return self._service_type

    @service_type.setter
    def service_type(self, service_type):
        """Sets the service_type of this SnapshotList.

        服务类型。

        :param service_type: The service_type of this SnapshotList.
        :type service_type: str
        """
        self._service_type = service_type

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
        if not isinstance(other, SnapshotList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
