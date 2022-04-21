# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BackupSync:

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
        'backup_name': 'str',
        'bucket_name': 'str',
        'image_path': 'str',
        'resource_id': 'str',
        'resource_name': 'str',
        'resource_type': 'str',
        'created_at': 'int'
    }

    attribute_map = {
        'backup_id': 'backup_id',
        'backup_name': 'backup_name',
        'bucket_name': 'bucket_name',
        'image_path': 'image_path',
        'resource_id': 'resource_id',
        'resource_name': 'resource_name',
        'resource_type': 'resource_type',
        'created_at': 'created_at'
    }

    def __init__(self, backup_id=None, backup_name=None, bucket_name=None, image_path=None, resource_id=None, resource_name=None, resource_type=None, created_at=None):
        """BackupSync

        The model defined in huaweicloud sdk

        :param backup_id: 备份副本ID
        :type backup_id: str
        :param backup_name: 备份名称
        :type backup_name: str
        :param bucket_name: 桶名
        :type bucket_name: str
        :param image_path: 备份链在存储单元上的路径
        :type image_path: str
        :param resource_id: 备份对象ID
        :type resource_id: str
        :param resource_name: 备份对象名称
        :type resource_name: str
        :param resource_type: 备份对象资源类型
        :type resource_type: str
        :param created_at: 备份时间戳，例如1548898428
        :type created_at: int
        """
        
        

        self._backup_id = None
        self._backup_name = None
        self._bucket_name = None
        self._image_path = None
        self._resource_id = None
        self._resource_name = None
        self._resource_type = None
        self._created_at = None
        self.discriminator = None

        self.backup_id = backup_id
        self.backup_name = backup_name
        self.bucket_name = bucket_name
        self.image_path = image_path
        self.resource_id = resource_id
        self.resource_name = resource_name
        self.resource_type = resource_type
        self.created_at = created_at

    @property
    def backup_id(self):
        """Gets the backup_id of this BackupSync.

        备份副本ID

        :return: The backup_id of this BackupSync.
        :rtype: str
        """
        return self._backup_id

    @backup_id.setter
    def backup_id(self, backup_id):
        """Sets the backup_id of this BackupSync.

        备份副本ID

        :param backup_id: The backup_id of this BackupSync.
        :type backup_id: str
        """
        self._backup_id = backup_id

    @property
    def backup_name(self):
        """Gets the backup_name of this BackupSync.

        备份名称

        :return: The backup_name of this BackupSync.
        :rtype: str
        """
        return self._backup_name

    @backup_name.setter
    def backup_name(self, backup_name):
        """Sets the backup_name of this BackupSync.

        备份名称

        :param backup_name: The backup_name of this BackupSync.
        :type backup_name: str
        """
        self._backup_name = backup_name

    @property
    def bucket_name(self):
        """Gets the bucket_name of this BackupSync.

        桶名

        :return: The bucket_name of this BackupSync.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        """Sets the bucket_name of this BackupSync.

        桶名

        :param bucket_name: The bucket_name of this BackupSync.
        :type bucket_name: str
        """
        self._bucket_name = bucket_name

    @property
    def image_path(self):
        """Gets the image_path of this BackupSync.

        备份链在存储单元上的路径

        :return: The image_path of this BackupSync.
        :rtype: str
        """
        return self._image_path

    @image_path.setter
    def image_path(self, image_path):
        """Sets the image_path of this BackupSync.

        备份链在存储单元上的路径

        :param image_path: The image_path of this BackupSync.
        :type image_path: str
        """
        self._image_path = image_path

    @property
    def resource_id(self):
        """Gets the resource_id of this BackupSync.

        备份对象ID

        :return: The resource_id of this BackupSync.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this BackupSync.

        备份对象ID

        :param resource_id: The resource_id of this BackupSync.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def resource_name(self):
        """Gets the resource_name of this BackupSync.

        备份对象名称

        :return: The resource_name of this BackupSync.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        """Sets the resource_name of this BackupSync.

        备份对象名称

        :param resource_name: The resource_name of this BackupSync.
        :type resource_name: str
        """
        self._resource_name = resource_name

    @property
    def resource_type(self):
        """Gets the resource_type of this BackupSync.

        备份对象资源类型

        :return: The resource_type of this BackupSync.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this BackupSync.

        备份对象资源类型

        :param resource_type: The resource_type of this BackupSync.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def created_at(self):
        """Gets the created_at of this BackupSync.

        备份时间戳，例如1548898428

        :return: The created_at of this BackupSync.
        :rtype: int
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this BackupSync.

        备份时间戳，例如1548898428

        :param created_at: The created_at of this BackupSync.
        :type created_at: int
        """
        self._created_at = created_at

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
        if not isinstance(other, BackupSync):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
