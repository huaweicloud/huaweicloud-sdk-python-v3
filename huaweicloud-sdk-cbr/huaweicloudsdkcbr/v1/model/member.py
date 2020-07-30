# coding: utf-8

import pprint
import re

import six





class Member:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'status': 'str',
        'created_at': 'str',
        'updated_at': 'str',
        'backup_id': 'str',
        'image_id': 'str',
        'dest_project_id': 'str',
        'vault_id': 'str',
        'id': 'str'
    }

    attribute_map = {
        'status': 'status',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'backup_id': 'backup_id',
        'image_id': 'image_id',
        'dest_project_id': 'dest_project_id',
        'vault_id': 'vault_id',
        'id': 'id'
    }

    def __init__(self, status=None, created_at=None, updated_at=None, backup_id=None, image_id=None, dest_project_id=None, vault_id=None, id=None):
        """Member - a model defined in huaweicloud sdk"""
        
        

        self._status = None
        self._created_at = None
        self._updated_at = None
        self._backup_id = None
        self._image_id = None
        self._dest_project_id = None
        self._vault_id = None
        self._id = None
        self.discriminator = None

        self.status = status
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if backup_id is not None:
            self.backup_id = backup_id
        if image_id is not None:
            self.image_id = image_id
        if dest_project_id is not None:
            self.dest_project_id = dest_project_id
        if vault_id is not None:
            self.vault_id = vault_id
        if id is not None:
            self.id = id

    @property
    def status(self):
        """Gets the status of this Member.

        共享状态

        :return: The status of this Member.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Member.

        共享状态

        :param status: The status of this Member.
        :type: str
        """
        self._status = status

    @property
    def created_at(self):
        """Gets the created_at of this Member.

        共享时间，例如:\"2020-02-05T10:38:34.209782\"

        :return: The created_at of this Member.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Member.

        共享时间，例如:\"2020-02-05T10:38:34.209782\"

        :param created_at: The created_at of this Member.
        :type: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this Member.

        更新时间，例如:\"2020-02-05T10:38:34.209782\"

        :return: The updated_at of this Member.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Member.

        更新时间，例如:\"2020-02-05T10:38:34.209782\"

        :param updated_at: The updated_at of this Member.
        :type: str
        """
        self._updated_at = updated_at

    @property
    def backup_id(self):
        """Gets the backup_id of this Member.

        备份副本id

        :return: The backup_id of this Member.
        :rtype: str
        """
        return self._backup_id

    @backup_id.setter
    def backup_id(self, backup_id):
        """Sets the backup_id of this Member.

        备份副本id

        :param backup_id: The backup_id of this Member.
        :type: str
        """
        self._backup_id = backup_id

    @property
    def image_id(self):
        """Gets the image_id of this Member.

        接受的共享备份副本注册的镜像id

        :return: The image_id of this Member.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """Sets the image_id of this Member.

        接受的共享备份副本注册的镜像id

        :param image_id: The image_id of this Member.
        :type: str
        """
        self._image_id = image_id

    @property
    def dest_project_id(self):
        """Gets the dest_project_id of this Member.

        接受备份共享的项目id

        :return: The dest_project_id of this Member.
        :rtype: str
        """
        return self._dest_project_id

    @dest_project_id.setter
    def dest_project_id(self, dest_project_id):
        """Sets the dest_project_id of this Member.

        接受备份共享的项目id

        :param dest_project_id: The dest_project_id of this Member.
        :type: str
        """
        self._dest_project_id = dest_project_id

    @property
    def vault_id(self):
        """Gets the vault_id of this Member.

        目标端接受共享备份的存储库id

        :return: The vault_id of this Member.
        :rtype: str
        """
        return self._vault_id

    @vault_id.setter
    def vault_id(self, vault_id):
        """Sets the vault_id of this Member.

        目标端接受共享备份的存储库id

        :param vault_id: The vault_id of this Member.
        :type: str
        """
        self._vault_id = vault_id

    @property
    def id(self):
        """Gets the id of this Member.

        共享记录id

        :return: The id of this Member.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Member.

        共享记录id

        :param id: The id of this Member.
        :type: str
        """
        self._id = id

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Member):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
