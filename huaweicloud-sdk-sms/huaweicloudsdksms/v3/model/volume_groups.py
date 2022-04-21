# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VolumeGroups:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'components': 'str',
        'free_size': 'int',
        'logical_volumes': 'list[LogicalVolumes]',
        'name': 'str',
        'size': 'int'
    }

    attribute_map = {
        'components': 'components',
        'free_size': 'free_size',
        'logical_volumes': 'logical_volumes',
        'name': 'name',
        'size': 'size'
    }

    def __init__(self, components=None, free_size=None, logical_volumes=None, name=None, size=None):
        """VolumeGroups

        The model defined in huaweicloud sdk

        :param components: Pv信息
        :type components: str
        :param free_size: 剩余空间
        :type free_size: int
        :param logical_volumes: lv信息
        :type logical_volumes: list[:class:`huaweicloudsdksms.v3.LogicalVolumes`]
        :param name: 名称
        :type name: str
        :param size: 大小
        :type size: int
        """
        
        

        self._components = None
        self._free_size = None
        self._logical_volumes = None
        self._name = None
        self._size = None
        self.discriminator = None

        if components is not None:
            self.components = components
        if free_size is not None:
            self.free_size = free_size
        if logical_volumes is not None:
            self.logical_volumes = logical_volumes
        if name is not None:
            self.name = name
        if size is not None:
            self.size = size

    @property
    def components(self):
        """Gets the components of this VolumeGroups.

        Pv信息

        :return: The components of this VolumeGroups.
        :rtype: str
        """
        return self._components

    @components.setter
    def components(self, components):
        """Sets the components of this VolumeGroups.

        Pv信息

        :param components: The components of this VolumeGroups.
        :type components: str
        """
        self._components = components

    @property
    def free_size(self):
        """Gets the free_size of this VolumeGroups.

        剩余空间

        :return: The free_size of this VolumeGroups.
        :rtype: int
        """
        return self._free_size

    @free_size.setter
    def free_size(self, free_size):
        """Sets the free_size of this VolumeGroups.

        剩余空间

        :param free_size: The free_size of this VolumeGroups.
        :type free_size: int
        """
        self._free_size = free_size

    @property
    def logical_volumes(self):
        """Gets the logical_volumes of this VolumeGroups.

        lv信息

        :return: The logical_volumes of this VolumeGroups.
        :rtype: list[:class:`huaweicloudsdksms.v3.LogicalVolumes`]
        """
        return self._logical_volumes

    @logical_volumes.setter
    def logical_volumes(self, logical_volumes):
        """Sets the logical_volumes of this VolumeGroups.

        lv信息

        :param logical_volumes: The logical_volumes of this VolumeGroups.
        :type logical_volumes: list[:class:`huaweicloudsdksms.v3.LogicalVolumes`]
        """
        self._logical_volumes = logical_volumes

    @property
    def name(self):
        """Gets the name of this VolumeGroups.

        名称

        :return: The name of this VolumeGroups.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VolumeGroups.

        名称

        :param name: The name of this VolumeGroups.
        :type name: str
        """
        self._name = name

    @property
    def size(self):
        """Gets the size of this VolumeGroups.

        大小

        :return: The size of this VolumeGroups.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this VolumeGroups.

        大小

        :param size: The size of this VolumeGroups.
        :type size: int
        """
        self._size = size

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
        if not isinstance(other, VolumeGroups):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
