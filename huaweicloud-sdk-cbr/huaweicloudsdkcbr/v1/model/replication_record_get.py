# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ReplicationRecordGet:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'created_at': 'str',
        'destination_backup_id': 'str',
        'destination_checkpoint_id': 'str',
        'destination_project_id': 'str',
        'destination_region': 'str',
        'destination_vault_id': 'str',
        'extra_info': 'ReplicationRecordsExtraInfo',
        'id': 'str',
        'source_backup_id': 'str',
        'source_checkpoint_id': 'str',
        'source_project_id': 'str',
        'source_region': 'str',
        'status': 'str',
        'vault_id': 'str'
    }

    attribute_map = {
        'created_at': 'created_at',
        'destination_backup_id': 'destination_backup_id',
        'destination_checkpoint_id': 'destination_checkpoint_id',
        'destination_project_id': 'destination_project_id',
        'destination_region': 'destination_region',
        'destination_vault_id': 'destination_vault_id',
        'extra_info': 'extra_info',
        'id': 'id',
        'source_backup_id': 'source_backup_id',
        'source_checkpoint_id': 'source_checkpoint_id',
        'source_project_id': 'source_project_id',
        'source_region': 'source_region',
        'status': 'status',
        'vault_id': 'vault_id'
    }

    def __init__(self, created_at=None, destination_backup_id=None, destination_checkpoint_id=None, destination_project_id=None, destination_region=None, destination_vault_id=None, extra_info=None, id=None, source_backup_id=None, source_checkpoint_id=None, source_project_id=None, source_region=None, status=None, vault_id=None):
        """ReplicationRecordGet

        The model defined in huaweicloud sdk

        :param created_at: 复制的开始时间
        :type created_at: str
        :param destination_backup_id: 复制的目的备份ID
        :type destination_backup_id: str
        :param destination_checkpoint_id: 复制的目的备份记录ID
        :type destination_checkpoint_id: str
        :param destination_project_id: 复制的目标项目ID
        :type destination_project_id: str
        :param destination_region: 复制的目标区域
        :type destination_region: str
        :param destination_vault_id: 目标存储库ID
        :type destination_vault_id: str
        :param extra_info: 
        :type extra_info: :class:`huaweicloudsdkcbr.v1.ReplicationRecordsExtraInfo`
        :param id: 复制记录ID
        :type id: str
        :param source_backup_id: 复制的源备份ID
        :type source_backup_id: str
        :param source_checkpoint_id: 复制的源备份记录ID
        :type source_checkpoint_id: str
        :param source_project_id: 复制的源项目ID
        :type source_project_id: str
        :param source_region: 复制的源区域
        :type source_region: str
        :param status: 复制的状态
        :type status: str
        :param vault_id: 备份所在的存储库ID
        :type vault_id: str
        """
        
        

        self._created_at = None
        self._destination_backup_id = None
        self._destination_checkpoint_id = None
        self._destination_project_id = None
        self._destination_region = None
        self._destination_vault_id = None
        self._extra_info = None
        self._id = None
        self._source_backup_id = None
        self._source_checkpoint_id = None
        self._source_project_id = None
        self._source_region = None
        self._status = None
        self._vault_id = None
        self.discriminator = None

        if created_at is not None:
            self.created_at = created_at
        if destination_backup_id is not None:
            self.destination_backup_id = destination_backup_id
        if destination_checkpoint_id is not None:
            self.destination_checkpoint_id = destination_checkpoint_id
        if destination_project_id is not None:
            self.destination_project_id = destination_project_id
        if destination_region is not None:
            self.destination_region = destination_region
        if destination_vault_id is not None:
            self.destination_vault_id = destination_vault_id
        if extra_info is not None:
            self.extra_info = extra_info
        self.id = id
        if source_backup_id is not None:
            self.source_backup_id = source_backup_id
        if source_checkpoint_id is not None:
            self.source_checkpoint_id = source_checkpoint_id
        if source_project_id is not None:
            self.source_project_id = source_project_id
        if source_region is not None:
            self.source_region = source_region
        if status is not None:
            self.status = status
        if vault_id is not None:
            self.vault_id = vault_id

    @property
    def created_at(self):
        """Gets the created_at of this ReplicationRecordGet.

        复制的开始时间

        :return: The created_at of this ReplicationRecordGet.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ReplicationRecordGet.

        复制的开始时间

        :param created_at: The created_at of this ReplicationRecordGet.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def destination_backup_id(self):
        """Gets the destination_backup_id of this ReplicationRecordGet.

        复制的目的备份ID

        :return: The destination_backup_id of this ReplicationRecordGet.
        :rtype: str
        """
        return self._destination_backup_id

    @destination_backup_id.setter
    def destination_backup_id(self, destination_backup_id):
        """Sets the destination_backup_id of this ReplicationRecordGet.

        复制的目的备份ID

        :param destination_backup_id: The destination_backup_id of this ReplicationRecordGet.
        :type destination_backup_id: str
        """
        self._destination_backup_id = destination_backup_id

    @property
    def destination_checkpoint_id(self):
        """Gets the destination_checkpoint_id of this ReplicationRecordGet.

        复制的目的备份记录ID

        :return: The destination_checkpoint_id of this ReplicationRecordGet.
        :rtype: str
        """
        return self._destination_checkpoint_id

    @destination_checkpoint_id.setter
    def destination_checkpoint_id(self, destination_checkpoint_id):
        """Sets the destination_checkpoint_id of this ReplicationRecordGet.

        复制的目的备份记录ID

        :param destination_checkpoint_id: The destination_checkpoint_id of this ReplicationRecordGet.
        :type destination_checkpoint_id: str
        """
        self._destination_checkpoint_id = destination_checkpoint_id

    @property
    def destination_project_id(self):
        """Gets the destination_project_id of this ReplicationRecordGet.

        复制的目标项目ID

        :return: The destination_project_id of this ReplicationRecordGet.
        :rtype: str
        """
        return self._destination_project_id

    @destination_project_id.setter
    def destination_project_id(self, destination_project_id):
        """Sets the destination_project_id of this ReplicationRecordGet.

        复制的目标项目ID

        :param destination_project_id: The destination_project_id of this ReplicationRecordGet.
        :type destination_project_id: str
        """
        self._destination_project_id = destination_project_id

    @property
    def destination_region(self):
        """Gets the destination_region of this ReplicationRecordGet.

        复制的目标区域

        :return: The destination_region of this ReplicationRecordGet.
        :rtype: str
        """
        return self._destination_region

    @destination_region.setter
    def destination_region(self, destination_region):
        """Sets the destination_region of this ReplicationRecordGet.

        复制的目标区域

        :param destination_region: The destination_region of this ReplicationRecordGet.
        :type destination_region: str
        """
        self._destination_region = destination_region

    @property
    def destination_vault_id(self):
        """Gets the destination_vault_id of this ReplicationRecordGet.

        目标存储库ID

        :return: The destination_vault_id of this ReplicationRecordGet.
        :rtype: str
        """
        return self._destination_vault_id

    @destination_vault_id.setter
    def destination_vault_id(self, destination_vault_id):
        """Sets the destination_vault_id of this ReplicationRecordGet.

        目标存储库ID

        :param destination_vault_id: The destination_vault_id of this ReplicationRecordGet.
        :type destination_vault_id: str
        """
        self._destination_vault_id = destination_vault_id

    @property
    def extra_info(self):
        """Gets the extra_info of this ReplicationRecordGet.

        :return: The extra_info of this ReplicationRecordGet.
        :rtype: :class:`huaweicloudsdkcbr.v1.ReplicationRecordsExtraInfo`
        """
        return self._extra_info

    @extra_info.setter
    def extra_info(self, extra_info):
        """Sets the extra_info of this ReplicationRecordGet.

        :param extra_info: The extra_info of this ReplicationRecordGet.
        :type extra_info: :class:`huaweicloudsdkcbr.v1.ReplicationRecordsExtraInfo`
        """
        self._extra_info = extra_info

    @property
    def id(self):
        """Gets the id of this ReplicationRecordGet.

        复制记录ID

        :return: The id of this ReplicationRecordGet.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ReplicationRecordGet.

        复制记录ID

        :param id: The id of this ReplicationRecordGet.
        :type id: str
        """
        self._id = id

    @property
    def source_backup_id(self):
        """Gets the source_backup_id of this ReplicationRecordGet.

        复制的源备份ID

        :return: The source_backup_id of this ReplicationRecordGet.
        :rtype: str
        """
        return self._source_backup_id

    @source_backup_id.setter
    def source_backup_id(self, source_backup_id):
        """Sets the source_backup_id of this ReplicationRecordGet.

        复制的源备份ID

        :param source_backup_id: The source_backup_id of this ReplicationRecordGet.
        :type source_backup_id: str
        """
        self._source_backup_id = source_backup_id

    @property
    def source_checkpoint_id(self):
        """Gets the source_checkpoint_id of this ReplicationRecordGet.

        复制的源备份记录ID

        :return: The source_checkpoint_id of this ReplicationRecordGet.
        :rtype: str
        """
        return self._source_checkpoint_id

    @source_checkpoint_id.setter
    def source_checkpoint_id(self, source_checkpoint_id):
        """Sets the source_checkpoint_id of this ReplicationRecordGet.

        复制的源备份记录ID

        :param source_checkpoint_id: The source_checkpoint_id of this ReplicationRecordGet.
        :type source_checkpoint_id: str
        """
        self._source_checkpoint_id = source_checkpoint_id

    @property
    def source_project_id(self):
        """Gets the source_project_id of this ReplicationRecordGet.

        复制的源项目ID

        :return: The source_project_id of this ReplicationRecordGet.
        :rtype: str
        """
        return self._source_project_id

    @source_project_id.setter
    def source_project_id(self, source_project_id):
        """Sets the source_project_id of this ReplicationRecordGet.

        复制的源项目ID

        :param source_project_id: The source_project_id of this ReplicationRecordGet.
        :type source_project_id: str
        """
        self._source_project_id = source_project_id

    @property
    def source_region(self):
        """Gets the source_region of this ReplicationRecordGet.

        复制的源区域

        :return: The source_region of this ReplicationRecordGet.
        :rtype: str
        """
        return self._source_region

    @source_region.setter
    def source_region(self, source_region):
        """Sets the source_region of this ReplicationRecordGet.

        复制的源区域

        :param source_region: The source_region of this ReplicationRecordGet.
        :type source_region: str
        """
        self._source_region = source_region

    @property
    def status(self):
        """Gets the status of this ReplicationRecordGet.

        复制的状态

        :return: The status of this ReplicationRecordGet.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ReplicationRecordGet.

        复制的状态

        :param status: The status of this ReplicationRecordGet.
        :type status: str
        """
        self._status = status

    @property
    def vault_id(self):
        """Gets the vault_id of this ReplicationRecordGet.

        备份所在的存储库ID

        :return: The vault_id of this ReplicationRecordGet.
        :rtype: str
        """
        return self._vault_id

    @vault_id.setter
    def vault_id(self, vault_id):
        """Sets the vault_id of this ReplicationRecordGet.

        备份所在的存储库ID

        :param vault_id: The vault_id of this ReplicationRecordGet.
        :type vault_id: str
        """
        self._vault_id = vault_id

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
        if not isinstance(other, ReplicationRecordGet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
