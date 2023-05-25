# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StorageUsage:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'backup_count': 'int',
        'backup_size': 'int',
        'resource_id': 'str',
        'resource_name': 'str',
        'resource_type': 'str',
        'backup_size_multiaz': 'int'
    }

    attribute_map = {
        'backup_count': 'backup_count',
        'backup_size': 'backup_size',
        'resource_id': 'resource_id',
        'resource_name': 'resource_name',
        'resource_type': 'resource_type',
        'backup_size_multiaz': 'backup_size_multiaz'
    }

    def __init__(self, backup_count=None, backup_size=None, resource_id=None, resource_name=None, resource_type=None, backup_size_multiaz=None):
        """StorageUsage

        The model defined in huaweicloud sdk

        :param backup_count: 备份数量
        :type backup_count: int
        :param backup_size: 备份容量
        :type backup_size: int
        :param resource_id: 资源ID
        :type resource_id: str
        :param resource_name: 资源名称
        :type resource_name: str
        :param resource_type: 资源类型
        :type resource_type: str
        :param backup_size_multiaz: 多AZ备份大小
        :type backup_size_multiaz: int
        """
        
        

        self._backup_count = None
        self._backup_size = None
        self._resource_id = None
        self._resource_name = None
        self._resource_type = None
        self._backup_size_multiaz = None
        self.discriminator = None

        if backup_count is not None:
            self.backup_count = backup_count
        if backup_size is not None:
            self.backup_size = backup_size
        self.resource_id = resource_id
        self.resource_name = resource_name
        self.resource_type = resource_type
        if backup_size_multiaz is not None:
            self.backup_size_multiaz = backup_size_multiaz

    @property
    def backup_count(self):
        """Gets the backup_count of this StorageUsage.

        备份数量

        :return: The backup_count of this StorageUsage.
        :rtype: int
        """
        return self._backup_count

    @backup_count.setter
    def backup_count(self, backup_count):
        """Sets the backup_count of this StorageUsage.

        备份数量

        :param backup_count: The backup_count of this StorageUsage.
        :type backup_count: int
        """
        self._backup_count = backup_count

    @property
    def backup_size(self):
        """Gets the backup_size of this StorageUsage.

        备份容量

        :return: The backup_size of this StorageUsage.
        :rtype: int
        """
        return self._backup_size

    @backup_size.setter
    def backup_size(self, backup_size):
        """Sets the backup_size of this StorageUsage.

        备份容量

        :param backup_size: The backup_size of this StorageUsage.
        :type backup_size: int
        """
        self._backup_size = backup_size

    @property
    def resource_id(self):
        """Gets the resource_id of this StorageUsage.

        资源ID

        :return: The resource_id of this StorageUsage.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this StorageUsage.

        资源ID

        :param resource_id: The resource_id of this StorageUsage.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def resource_name(self):
        """Gets the resource_name of this StorageUsage.

        资源名称

        :return: The resource_name of this StorageUsage.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        """Sets the resource_name of this StorageUsage.

        资源名称

        :param resource_name: The resource_name of this StorageUsage.
        :type resource_name: str
        """
        self._resource_name = resource_name

    @property
    def resource_type(self):
        """Gets the resource_type of this StorageUsage.

        资源类型

        :return: The resource_type of this StorageUsage.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this StorageUsage.

        资源类型

        :param resource_type: The resource_type of this StorageUsage.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def backup_size_multiaz(self):
        """Gets the backup_size_multiaz of this StorageUsage.

        多AZ备份大小

        :return: The backup_size_multiaz of this StorageUsage.
        :rtype: int
        """
        return self._backup_size_multiaz

    @backup_size_multiaz.setter
    def backup_size_multiaz(self, backup_size_multiaz):
        """Sets the backup_size_multiaz of this StorageUsage.

        多AZ备份大小

        :param backup_size_multiaz: The backup_size_multiaz of this StorageUsage.
        :type backup_size_multiaz: int
        """
        self._backup_size_multiaz = backup_size_multiaz

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
        if not isinstance(other, StorageUsage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
