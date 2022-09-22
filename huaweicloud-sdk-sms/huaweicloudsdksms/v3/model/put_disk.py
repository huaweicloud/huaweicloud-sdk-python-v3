# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PutDisk:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'need_migration': 'bool',
        'id': 'str',
        'adjust_size': 'int',
        'physical_volumes': 'list[PutVolume]'
    }

    attribute_map = {
        'need_migration': 'need_migration',
        'id': 'id',
        'adjust_size': 'adjust_size',
        'physical_volumes': 'physical_volumes'
    }

    def __init__(self, need_migration=None, id=None, adjust_size=None, physical_volumes=None):
        """PutDisk

        The model defined in huaweicloud sdk

        :param need_migration: 磁盘名称
        :type need_migration: bool
        :param id: 磁盘ID
        :type id: str
        :param adjust_size: 调整大小
        :type adjust_size: int
        :param physical_volumes: 修改的卷信息
        :type physical_volumes: list[:class:`huaweicloudsdksms.v3.PutVolume`]
        """
        
        

        self._need_migration = None
        self._id = None
        self._adjust_size = None
        self._physical_volumes = None
        self.discriminator = None

        if need_migration is not None:
            self.need_migration = need_migration
        self.id = id
        self.adjust_size = adjust_size
        if physical_volumes is not None:
            self.physical_volumes = physical_volumes

    @property
    def need_migration(self):
        """Gets the need_migration of this PutDisk.

        磁盘名称

        :return: The need_migration of this PutDisk.
        :rtype: bool
        """
        return self._need_migration

    @need_migration.setter
    def need_migration(self, need_migration):
        """Sets the need_migration of this PutDisk.

        磁盘名称

        :param need_migration: The need_migration of this PutDisk.
        :type need_migration: bool
        """
        self._need_migration = need_migration

    @property
    def id(self):
        """Gets the id of this PutDisk.

        磁盘ID

        :return: The id of this PutDisk.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PutDisk.

        磁盘ID

        :param id: The id of this PutDisk.
        :type id: str
        """
        self._id = id

    @property
    def adjust_size(self):
        """Gets the adjust_size of this PutDisk.

        调整大小

        :return: The adjust_size of this PutDisk.
        :rtype: int
        """
        return self._adjust_size

    @adjust_size.setter
    def adjust_size(self, adjust_size):
        """Sets the adjust_size of this PutDisk.

        调整大小

        :param adjust_size: The adjust_size of this PutDisk.
        :type adjust_size: int
        """
        self._adjust_size = adjust_size

    @property
    def physical_volumes(self):
        """Gets the physical_volumes of this PutDisk.

        修改的卷信息

        :return: The physical_volumes of this PutDisk.
        :rtype: list[:class:`huaweicloudsdksms.v3.PutVolume`]
        """
        return self._physical_volumes

    @physical_volumes.setter
    def physical_volumes(self, physical_volumes):
        """Sets the physical_volumes of this PutDisk.

        修改的卷信息

        :param physical_volumes: The physical_volumes of this PutDisk.
        :type physical_volumes: list[:class:`huaweicloudsdksms.v3.PutVolume`]
        """
        self._physical_volumes = physical_volumes

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
        if not isinstance(other, PutDisk):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
