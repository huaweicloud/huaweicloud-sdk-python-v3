# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BackupReplicateRespBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'backup_id': 'str',
        'destination_project_id': 'str',
        'destination_region': 'str',
        'destination_vault_id': 'str',
        'project_id': 'str',
        'provider_id': 'str',
        'replication_record_id': 'str',
        'source_region': 'str'
    }

    attribute_map = {
        'backup_id': 'backup_id',
        'destination_project_id': 'destination_project_id',
        'destination_region': 'destination_region',
        'destination_vault_id': 'destination_vault_id',
        'project_id': 'project_id',
        'provider_id': 'provider_id',
        'replication_record_id': 'replication_record_id',
        'source_region': 'source_region'
    }

    def __init__(self, backup_id=None, destination_project_id=None, destination_region=None, destination_vault_id=None, project_id=None, provider_id=None, replication_record_id=None, source_region=None):
        """BackupReplicateRespBody

        The model defined in huaweicloud sdk

        :param backup_id: 待复制的备份ID
        :type backup_id: str
        :param destination_project_id: 复制的目标项目ID
        :type destination_project_id: str
        :param destination_region: 复制的目标区域
        :type destination_region: str
        :param destination_vault_id: 复制的目标区域存储库ID
        :type destination_vault_id: str
        :param project_id: 执行复制的项目ID
        :type project_id: str
        :param provider_id: 资源类型id
        :type provider_id: str
        :param replication_record_id: 复制记录ID
        :type replication_record_id: str
        :param source_region: 复制的源区域
        :type source_region: str
        """
        
        

        self._backup_id = None
        self._destination_project_id = None
        self._destination_region = None
        self._destination_vault_id = None
        self._project_id = None
        self._provider_id = None
        self._replication_record_id = None
        self._source_region = None
        self.discriminator = None

        if backup_id is not None:
            self.backup_id = backup_id
        if destination_project_id is not None:
            self.destination_project_id = destination_project_id
        if destination_region is not None:
            self.destination_region = destination_region
        if destination_vault_id is not None:
            self.destination_vault_id = destination_vault_id
        if project_id is not None:
            self.project_id = project_id
        if provider_id is not None:
            self.provider_id = provider_id
        if replication_record_id is not None:
            self.replication_record_id = replication_record_id
        if source_region is not None:
            self.source_region = source_region

    @property
    def backup_id(self):
        """Gets the backup_id of this BackupReplicateRespBody.

        待复制的备份ID

        :return: The backup_id of this BackupReplicateRespBody.
        :rtype: str
        """
        return self._backup_id

    @backup_id.setter
    def backup_id(self, backup_id):
        """Sets the backup_id of this BackupReplicateRespBody.

        待复制的备份ID

        :param backup_id: The backup_id of this BackupReplicateRespBody.
        :type backup_id: str
        """
        self._backup_id = backup_id

    @property
    def destination_project_id(self):
        """Gets the destination_project_id of this BackupReplicateRespBody.

        复制的目标项目ID

        :return: The destination_project_id of this BackupReplicateRespBody.
        :rtype: str
        """
        return self._destination_project_id

    @destination_project_id.setter
    def destination_project_id(self, destination_project_id):
        """Sets the destination_project_id of this BackupReplicateRespBody.

        复制的目标项目ID

        :param destination_project_id: The destination_project_id of this BackupReplicateRespBody.
        :type destination_project_id: str
        """
        self._destination_project_id = destination_project_id

    @property
    def destination_region(self):
        """Gets the destination_region of this BackupReplicateRespBody.

        复制的目标区域

        :return: The destination_region of this BackupReplicateRespBody.
        :rtype: str
        """
        return self._destination_region

    @destination_region.setter
    def destination_region(self, destination_region):
        """Sets the destination_region of this BackupReplicateRespBody.

        复制的目标区域

        :param destination_region: The destination_region of this BackupReplicateRespBody.
        :type destination_region: str
        """
        self._destination_region = destination_region

    @property
    def destination_vault_id(self):
        """Gets the destination_vault_id of this BackupReplicateRespBody.

        复制的目标区域存储库ID

        :return: The destination_vault_id of this BackupReplicateRespBody.
        :rtype: str
        """
        return self._destination_vault_id

    @destination_vault_id.setter
    def destination_vault_id(self, destination_vault_id):
        """Sets the destination_vault_id of this BackupReplicateRespBody.

        复制的目标区域存储库ID

        :param destination_vault_id: The destination_vault_id of this BackupReplicateRespBody.
        :type destination_vault_id: str
        """
        self._destination_vault_id = destination_vault_id

    @property
    def project_id(self):
        """Gets the project_id of this BackupReplicateRespBody.

        执行复制的项目ID

        :return: The project_id of this BackupReplicateRespBody.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this BackupReplicateRespBody.

        执行复制的项目ID

        :param project_id: The project_id of this BackupReplicateRespBody.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def provider_id(self):
        """Gets the provider_id of this BackupReplicateRespBody.

        资源类型id

        :return: The provider_id of this BackupReplicateRespBody.
        :rtype: str
        """
        return self._provider_id

    @provider_id.setter
    def provider_id(self, provider_id):
        """Sets the provider_id of this BackupReplicateRespBody.

        资源类型id

        :param provider_id: The provider_id of this BackupReplicateRespBody.
        :type provider_id: str
        """
        self._provider_id = provider_id

    @property
    def replication_record_id(self):
        """Gets the replication_record_id of this BackupReplicateRespBody.

        复制记录ID

        :return: The replication_record_id of this BackupReplicateRespBody.
        :rtype: str
        """
        return self._replication_record_id

    @replication_record_id.setter
    def replication_record_id(self, replication_record_id):
        """Sets the replication_record_id of this BackupReplicateRespBody.

        复制记录ID

        :param replication_record_id: The replication_record_id of this BackupReplicateRespBody.
        :type replication_record_id: str
        """
        self._replication_record_id = replication_record_id

    @property
    def source_region(self):
        """Gets the source_region of this BackupReplicateRespBody.

        复制的源区域

        :return: The source_region of this BackupReplicateRespBody.
        :rtype: str
        """
        return self._source_region

    @source_region.setter
    def source_region(self, source_region):
        """Sets the source_region of this BackupReplicateRespBody.

        复制的源区域

        :param source_region: The source_region of this BackupReplicateRespBody.
        :type source_region: str
        """
        self._source_region = source_region

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
        if not isinstance(other, BackupReplicateRespBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
