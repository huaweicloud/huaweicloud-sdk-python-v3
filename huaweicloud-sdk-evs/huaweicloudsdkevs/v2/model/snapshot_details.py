# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SnapshotDetails:

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
        'metadata': 'object',
        'volume_id': 'str',
        'size': 'int',
        'os_extended_snapshot_attributesproject_id': 'str',
        'os_extended_snapshot_attributesprogress': 'str'
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
        'os_extended_snapshot_attributesprogress': 'os-extended-snapshot-attributes:progress'
    }

    def __init__(self, id=None, status=None, name=None, description=None, created_at=None, updated_at=None, metadata=None, volume_id=None, size=None, os_extended_snapshot_attributesproject_id=None, os_extended_snapshot_attributesprogress=None):
        """SnapshotDetails

        The model defined in huaweicloud sdk

        :param id: 云硬盘快照ID。
        :type id: str
        :param status: 云硬盘快照状态。
        :type status: str
        :param name: 云硬盘快照名称。
        :type name: str
        :param description: 云硬盘快照描述信息。
        :type description: str
        :param created_at: 云硬盘快照创建时间。 时间格式：UTC YYYY-MM-DDTHH:MM:SS.XXXXXX
        :type created_at: str
        :param updated_at: 快照更新时间。 时间格式：UTC YYYY-MM-DDTHH:MM:SS.XXXXXX
        :type updated_at: str
        :param metadata: 云硬盘快照的元数据信息。
        :type metadata: object
        :param volume_id: 快照所属的云硬盘ID。
        :type volume_id: str
        :param size: 云硬盘快照大小，单位为GB。
        :type size: int
        :param os_extended_snapshot_attributesproject_id: 预留属性。
        :type os_extended_snapshot_attributesproject_id: str
        :param os_extended_snapshot_attributesprogress: 预留属性。
        :type os_extended_snapshot_attributesprogress: str
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
        self.discriminator = None

        if id is not None:
            self.id = id
        if status is not None:
            self.status = status
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if metadata is not None:
            self.metadata = metadata
        if volume_id is not None:
            self.volume_id = volume_id
        if size is not None:
            self.size = size
        if os_extended_snapshot_attributesproject_id is not None:
            self.os_extended_snapshot_attributesproject_id = os_extended_snapshot_attributesproject_id
        if os_extended_snapshot_attributesprogress is not None:
            self.os_extended_snapshot_attributesprogress = os_extended_snapshot_attributesprogress

    @property
    def id(self):
        """Gets the id of this SnapshotDetails.

        云硬盘快照ID。

        :return: The id of this SnapshotDetails.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SnapshotDetails.

        云硬盘快照ID。

        :param id: The id of this SnapshotDetails.
        :type id: str
        """
        self._id = id

    @property
    def status(self):
        """Gets the status of this SnapshotDetails.

        云硬盘快照状态。

        :return: The status of this SnapshotDetails.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this SnapshotDetails.

        云硬盘快照状态。

        :param status: The status of this SnapshotDetails.
        :type status: str
        """
        self._status = status

    @property
    def name(self):
        """Gets the name of this SnapshotDetails.

        云硬盘快照名称。

        :return: The name of this SnapshotDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SnapshotDetails.

        云硬盘快照名称。

        :param name: The name of this SnapshotDetails.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this SnapshotDetails.

        云硬盘快照描述信息。

        :return: The description of this SnapshotDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this SnapshotDetails.

        云硬盘快照描述信息。

        :param description: The description of this SnapshotDetails.
        :type description: str
        """
        self._description = description

    @property
    def created_at(self):
        """Gets the created_at of this SnapshotDetails.

        云硬盘快照创建时间。 时间格式：UTC YYYY-MM-DDTHH:MM:SS.XXXXXX

        :return: The created_at of this SnapshotDetails.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this SnapshotDetails.

        云硬盘快照创建时间。 时间格式：UTC YYYY-MM-DDTHH:MM:SS.XXXXXX

        :param created_at: The created_at of this SnapshotDetails.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this SnapshotDetails.

        快照更新时间。 时间格式：UTC YYYY-MM-DDTHH:MM:SS.XXXXXX

        :return: The updated_at of this SnapshotDetails.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this SnapshotDetails.

        快照更新时间。 时间格式：UTC YYYY-MM-DDTHH:MM:SS.XXXXXX

        :param updated_at: The updated_at of this SnapshotDetails.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def metadata(self):
        """Gets the metadata of this SnapshotDetails.

        云硬盘快照的元数据信息。

        :return: The metadata of this SnapshotDetails.
        :rtype: object
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this SnapshotDetails.

        云硬盘快照的元数据信息。

        :param metadata: The metadata of this SnapshotDetails.
        :type metadata: object
        """
        self._metadata = metadata

    @property
    def volume_id(self):
        """Gets the volume_id of this SnapshotDetails.

        快照所属的云硬盘ID。

        :return: The volume_id of this SnapshotDetails.
        :rtype: str
        """
        return self._volume_id

    @volume_id.setter
    def volume_id(self, volume_id):
        """Sets the volume_id of this SnapshotDetails.

        快照所属的云硬盘ID。

        :param volume_id: The volume_id of this SnapshotDetails.
        :type volume_id: str
        """
        self._volume_id = volume_id

    @property
    def size(self):
        """Gets the size of this SnapshotDetails.

        云硬盘快照大小，单位为GB。

        :return: The size of this SnapshotDetails.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this SnapshotDetails.

        云硬盘快照大小，单位为GB。

        :param size: The size of this SnapshotDetails.
        :type size: int
        """
        self._size = size

    @property
    def os_extended_snapshot_attributesproject_id(self):
        """Gets the os_extended_snapshot_attributesproject_id of this SnapshotDetails.

        预留属性。

        :return: The os_extended_snapshot_attributesproject_id of this SnapshotDetails.
        :rtype: str
        """
        return self._os_extended_snapshot_attributesproject_id

    @os_extended_snapshot_attributesproject_id.setter
    def os_extended_snapshot_attributesproject_id(self, os_extended_snapshot_attributesproject_id):
        """Sets the os_extended_snapshot_attributesproject_id of this SnapshotDetails.

        预留属性。

        :param os_extended_snapshot_attributesproject_id: The os_extended_snapshot_attributesproject_id of this SnapshotDetails.
        :type os_extended_snapshot_attributesproject_id: str
        """
        self._os_extended_snapshot_attributesproject_id = os_extended_snapshot_attributesproject_id

    @property
    def os_extended_snapshot_attributesprogress(self):
        """Gets the os_extended_snapshot_attributesprogress of this SnapshotDetails.

        预留属性。

        :return: The os_extended_snapshot_attributesprogress of this SnapshotDetails.
        :rtype: str
        """
        return self._os_extended_snapshot_attributesprogress

    @os_extended_snapshot_attributesprogress.setter
    def os_extended_snapshot_attributesprogress(self, os_extended_snapshot_attributesprogress):
        """Sets the os_extended_snapshot_attributesprogress of this SnapshotDetails.

        预留属性。

        :param os_extended_snapshot_attributesprogress: The os_extended_snapshot_attributesprogress of this SnapshotDetails.
        :type os_extended_snapshot_attributesprogress: str
        """
        self._os_extended_snapshot_attributesprogress = os_extended_snapshot_attributesprogress

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
        if not isinstance(other, SnapshotDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
