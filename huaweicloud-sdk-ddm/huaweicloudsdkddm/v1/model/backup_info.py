# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BackupInfo:

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
        'instance_id': 'str',
        'instance_name': 'str',
        'instance_status': 'str',
        'file_size': 'float',
        'created': 'str',
        'updated': 'str',
        'backup_type': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'status': 'status',
        'instance_id': 'instance_id',
        'instance_name': 'instance_name',
        'instance_status': 'instance_status',
        'file_size': 'file_size',
        'created': 'created',
        'updated': 'updated',
        'backup_type': 'backup_type'
    }

    def __init__(self, id=None, name=None, description=None, status=None, instance_id=None, instance_name=None, instance_status=None, file_size=None, created=None, updated=None, backup_type=None):
        r"""BackupInfo

        The model defined in huaweicloud sdk

        :param id: 备份ID。
        :type id: str
        :param name: 备份名称。
        :type name: str
        :param description: 描述。
        :type description: str
        :param status: 状态。
        :type status: str
        :param instance_id: 实例ID。
        :type instance_id: str
        :param instance_name: 实例名称。
        :type instance_name: str
        :param instance_status: 实例状态。
        :type instance_status: str
        :param file_size: 文件大小。
        :type file_size: float
        :param created: 创建时间。
        :type created: str
        :param updated: 更新时间。
        :type updated: str
        :param backup_type: 备份类型。
        :type backup_type: str
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._status = None
        self._instance_id = None
        self._instance_name = None
        self._instance_status = None
        self._file_size = None
        self._created = None
        self._updated = None
        self._backup_type = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if status is not None:
            self.status = status
        if instance_id is not None:
            self.instance_id = instance_id
        if instance_name is not None:
            self.instance_name = instance_name
        if instance_status is not None:
            self.instance_status = instance_status
        if file_size is not None:
            self.file_size = file_size
        if created is not None:
            self.created = created
        if updated is not None:
            self.updated = updated
        if backup_type is not None:
            self.backup_type = backup_type

    @property
    def id(self):
        r"""Gets the id of this BackupInfo.

        备份ID。

        :return: The id of this BackupInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this BackupInfo.

        备份ID。

        :param id: The id of this BackupInfo.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this BackupInfo.

        备份名称。

        :return: The name of this BackupInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this BackupInfo.

        备份名称。

        :param name: The name of this BackupInfo.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this BackupInfo.

        描述。

        :return: The description of this BackupInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this BackupInfo.

        描述。

        :param description: The description of this BackupInfo.
        :type description: str
        """
        self._description = description

    @property
    def status(self):
        r"""Gets the status of this BackupInfo.

        状态。

        :return: The status of this BackupInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this BackupInfo.

        状态。

        :param status: The status of this BackupInfo.
        :type status: str
        """
        self._status = status

    @property
    def instance_id(self):
        r"""Gets the instance_id of this BackupInfo.

        实例ID。

        :return: The instance_id of this BackupInfo.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this BackupInfo.

        实例ID。

        :param instance_id: The instance_id of this BackupInfo.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def instance_name(self):
        r"""Gets the instance_name of this BackupInfo.

        实例名称。

        :return: The instance_name of this BackupInfo.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        r"""Sets the instance_name of this BackupInfo.

        实例名称。

        :param instance_name: The instance_name of this BackupInfo.
        :type instance_name: str
        """
        self._instance_name = instance_name

    @property
    def instance_status(self):
        r"""Gets the instance_status of this BackupInfo.

        实例状态。

        :return: The instance_status of this BackupInfo.
        :rtype: str
        """
        return self._instance_status

    @instance_status.setter
    def instance_status(self, instance_status):
        r"""Sets the instance_status of this BackupInfo.

        实例状态。

        :param instance_status: The instance_status of this BackupInfo.
        :type instance_status: str
        """
        self._instance_status = instance_status

    @property
    def file_size(self):
        r"""Gets the file_size of this BackupInfo.

        文件大小。

        :return: The file_size of this BackupInfo.
        :rtype: float
        """
        return self._file_size

    @file_size.setter
    def file_size(self, file_size):
        r"""Sets the file_size of this BackupInfo.

        文件大小。

        :param file_size: The file_size of this BackupInfo.
        :type file_size: float
        """
        self._file_size = file_size

    @property
    def created(self):
        r"""Gets the created of this BackupInfo.

        创建时间。

        :return: The created of this BackupInfo.
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        r"""Sets the created of this BackupInfo.

        创建时间。

        :param created: The created of this BackupInfo.
        :type created: str
        """
        self._created = created

    @property
    def updated(self):
        r"""Gets the updated of this BackupInfo.

        更新时间。

        :return: The updated of this BackupInfo.
        :rtype: str
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        r"""Sets the updated of this BackupInfo.

        更新时间。

        :param updated: The updated of this BackupInfo.
        :type updated: str
        """
        self._updated = updated

    @property
    def backup_type(self):
        r"""Gets the backup_type of this BackupInfo.

        备份类型。

        :return: The backup_type of this BackupInfo.
        :rtype: str
        """
        return self._backup_type

    @backup_type.setter
    def backup_type(self, backup_type):
        r"""Sets the backup_type of this BackupInfo.

        备份类型。

        :param backup_type: The backup_type of this BackupInfo.
        :type backup_type: str
        """
        self._backup_type = backup_type

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, BackupInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
