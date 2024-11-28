# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VolumeAddInfo:

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
        'type': 'str',
        'size': 'int',
        'cluster_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'type': 'type',
        'size': 'size',
        'cluster_id': 'cluster_id'
    }

    def __init__(self, id=None, type=None, size=None, cluster_id=None):
        """VolumeAddInfo

        The model defined in huaweicloud sdk

        :param id: 磁盘记录ID，删除或者扩容磁盘时必选。
        :type id: str
        :param type: 桌面数据盘对应的磁盘类型，需要与系统所提供的磁盘类型相匹配。 - SAS：高IO。 - SSD：超高IO。
        :type type: str
        :param size: 磁盘容量，单位GB。
        :type size: int
        :param cluster_id: 云服务器系统盘对应的存储池的ID。
        :type cluster_id: str
        """
        
        

        self._id = None
        self._type = None
        self._size = None
        self._cluster_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.type = type
        self.size = size
        if cluster_id is not None:
            self.cluster_id = cluster_id

    @property
    def id(self):
        """Gets the id of this VolumeAddInfo.

        磁盘记录ID，删除或者扩容磁盘时必选。

        :return: The id of this VolumeAddInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VolumeAddInfo.

        磁盘记录ID，删除或者扩容磁盘时必选。

        :param id: The id of this VolumeAddInfo.
        :type id: str
        """
        self._id = id

    @property
    def type(self):
        """Gets the type of this VolumeAddInfo.

        桌面数据盘对应的磁盘类型，需要与系统所提供的磁盘类型相匹配。 - SAS：高IO。 - SSD：超高IO。

        :return: The type of this VolumeAddInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this VolumeAddInfo.

        桌面数据盘对应的磁盘类型，需要与系统所提供的磁盘类型相匹配。 - SAS：高IO。 - SSD：超高IO。

        :param type: The type of this VolumeAddInfo.
        :type type: str
        """
        self._type = type

    @property
    def size(self):
        """Gets the size of this VolumeAddInfo.

        磁盘容量，单位GB。

        :return: The size of this VolumeAddInfo.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this VolumeAddInfo.

        磁盘容量，单位GB。

        :param size: The size of this VolumeAddInfo.
        :type size: int
        """
        self._size = size

    @property
    def cluster_id(self):
        """Gets the cluster_id of this VolumeAddInfo.

        云服务器系统盘对应的存储池的ID。

        :return: The cluster_id of this VolumeAddInfo.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this VolumeAddInfo.

        云服务器系统盘对应的存储池的ID。

        :param cluster_id: The cluster_id of this VolumeAddInfo.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

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
        if not isinstance(other, VolumeAddInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
