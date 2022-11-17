# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ReplicationRecordMetadata:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'multiattach': 'bool',
        'bootable': 'bool',
        'volume_size': 'int',
        'volume_type': 'str'
    }

    attribute_map = {
        'multiattach': 'multiattach',
        'bootable': 'bootable',
        'volume_size': 'volume_size',
        'volume_type': 'volume_type'
    }

    def __init__(self, multiattach=None, bootable=None, volume_size=None, volume_type=None):
        """ReplicationRecordMetadata

        The model defined in huaweicloud sdk

        :param multiattach: 复制对中的云硬盘是否为共享云硬盘。
        :type multiattach: bool
        :param bootable: 复制对中的云硬盘是否为系统盘。
        :type bootable: bool
        :param volume_size: 复制对中的云硬盘容量。单位：GB
        :type volume_size: int
        :param volume_type: 复制对中的云硬盘类型。SATA：普通IO磁盘类型。SAS：高IO磁盘类型。SSD：超高IO磁盘类型。co-p1：高IO（性能优化I型）uh-l1：超高IO（时延优化）其中co-p1和uh-l1两种云硬盘只能使用在HANA云服务器、HL1型云服务器、HL2型云服务器上。
        :type volume_type: str
        """
        
        

        self._multiattach = None
        self._bootable = None
        self._volume_size = None
        self._volume_type = None
        self.discriminator = None

        self.multiattach = multiattach
        self.bootable = bootable
        self.volume_size = volume_size
        self.volume_type = volume_type

    @property
    def multiattach(self):
        """Gets the multiattach of this ReplicationRecordMetadata.

        复制对中的云硬盘是否为共享云硬盘。

        :return: The multiattach of this ReplicationRecordMetadata.
        :rtype: bool
        """
        return self._multiattach

    @multiattach.setter
    def multiattach(self, multiattach):
        """Sets the multiattach of this ReplicationRecordMetadata.

        复制对中的云硬盘是否为共享云硬盘。

        :param multiattach: The multiattach of this ReplicationRecordMetadata.
        :type multiattach: bool
        """
        self._multiattach = multiattach

    @property
    def bootable(self):
        """Gets the bootable of this ReplicationRecordMetadata.

        复制对中的云硬盘是否为系统盘。

        :return: The bootable of this ReplicationRecordMetadata.
        :rtype: bool
        """
        return self._bootable

    @bootable.setter
    def bootable(self, bootable):
        """Sets the bootable of this ReplicationRecordMetadata.

        复制对中的云硬盘是否为系统盘。

        :param bootable: The bootable of this ReplicationRecordMetadata.
        :type bootable: bool
        """
        self._bootable = bootable

    @property
    def volume_size(self):
        """Gets the volume_size of this ReplicationRecordMetadata.

        复制对中的云硬盘容量。单位：GB

        :return: The volume_size of this ReplicationRecordMetadata.
        :rtype: int
        """
        return self._volume_size

    @volume_size.setter
    def volume_size(self, volume_size):
        """Sets the volume_size of this ReplicationRecordMetadata.

        复制对中的云硬盘容量。单位：GB

        :param volume_size: The volume_size of this ReplicationRecordMetadata.
        :type volume_size: int
        """
        self._volume_size = volume_size

    @property
    def volume_type(self):
        """Gets the volume_type of this ReplicationRecordMetadata.

        复制对中的云硬盘类型。SATA：普通IO磁盘类型。SAS：高IO磁盘类型。SSD：超高IO磁盘类型。co-p1：高IO（性能优化I型）uh-l1：超高IO（时延优化）其中co-p1和uh-l1两种云硬盘只能使用在HANA云服务器、HL1型云服务器、HL2型云服务器上。

        :return: The volume_type of this ReplicationRecordMetadata.
        :rtype: str
        """
        return self._volume_type

    @volume_type.setter
    def volume_type(self, volume_type):
        """Sets the volume_type of this ReplicationRecordMetadata.

        复制对中的云硬盘类型。SATA：普通IO磁盘类型。SAS：高IO磁盘类型。SSD：超高IO磁盘类型。co-p1：高IO（性能优化I型）uh-l1：超高IO（时延优化）其中co-p1和uh-l1两种云硬盘只能使用在HANA云服务器、HL1型云服务器、HL2型云服务器上。

        :param volume_type: The volume_type of this ReplicationRecordMetadata.
        :type volume_type: str
        """
        self._volume_type = volume_type

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
        if not isinstance(other, ReplicationRecordMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
