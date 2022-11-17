# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PutVolumeGroups:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'logical_volumes': 'list[PutLogicalVolume]',
        'id': 'str',
        'need_migration': 'bool',
        'adjust_size': 'int'
    }

    attribute_map = {
        'logical_volumes': 'logical_volumes',
        'id': 'id',
        'need_migration': 'need_migration',
        'adjust_size': 'adjust_size'
    }

    def __init__(self, logical_volumes=None, id=None, need_migration=None, adjust_size=None):
        """PutVolumeGroups

        The model defined in huaweicloud sdk

        :param logical_volumes: lv信息
        :type logical_volumes: list[:class:`huaweicloudsdksms.v3.PutLogicalVolume`]
        :param id: 卷组ID
        :type id: str
        :param need_migration: 是否迁移
        :type need_migration: bool
        :param adjust_size: 调整大小
        :type adjust_size: int
        """
        
        

        self._logical_volumes = None
        self._id = None
        self._need_migration = None
        self._adjust_size = None
        self.discriminator = None

        if logical_volumes is not None:
            self.logical_volumes = logical_volumes
        self.id = id
        if need_migration is not None:
            self.need_migration = need_migration
        if adjust_size is not None:
            self.adjust_size = adjust_size

    @property
    def logical_volumes(self):
        """Gets the logical_volumes of this PutVolumeGroups.

        lv信息

        :return: The logical_volumes of this PutVolumeGroups.
        :rtype: list[:class:`huaweicloudsdksms.v3.PutLogicalVolume`]
        """
        return self._logical_volumes

    @logical_volumes.setter
    def logical_volumes(self, logical_volumes):
        """Sets the logical_volumes of this PutVolumeGroups.

        lv信息

        :param logical_volumes: The logical_volumes of this PutVolumeGroups.
        :type logical_volumes: list[:class:`huaweicloudsdksms.v3.PutLogicalVolume`]
        """
        self._logical_volumes = logical_volumes

    @property
    def id(self):
        """Gets the id of this PutVolumeGroups.

        卷组ID

        :return: The id of this PutVolumeGroups.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PutVolumeGroups.

        卷组ID

        :param id: The id of this PutVolumeGroups.
        :type id: str
        """
        self._id = id

    @property
    def need_migration(self):
        """Gets the need_migration of this PutVolumeGroups.

        是否迁移

        :return: The need_migration of this PutVolumeGroups.
        :rtype: bool
        """
        return self._need_migration

    @need_migration.setter
    def need_migration(self, need_migration):
        """Sets the need_migration of this PutVolumeGroups.

        是否迁移

        :param need_migration: The need_migration of this PutVolumeGroups.
        :type need_migration: bool
        """
        self._need_migration = need_migration

    @property
    def adjust_size(self):
        """Gets the adjust_size of this PutVolumeGroups.

        调整大小

        :return: The adjust_size of this PutVolumeGroups.
        :rtype: int
        """
        return self._adjust_size

    @adjust_size.setter
    def adjust_size(self, adjust_size):
        """Sets the adjust_size of this PutVolumeGroups.

        调整大小

        :param adjust_size: The adjust_size of this PutVolumeGroups.
        :type adjust_size: int
        """
        self._adjust_size = adjust_size

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
        if not isinstance(other, PutVolumeGroups):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
