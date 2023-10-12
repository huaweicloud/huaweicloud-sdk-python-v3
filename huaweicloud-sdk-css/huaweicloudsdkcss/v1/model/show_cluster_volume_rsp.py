# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowClusterVolumeRsp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'size': 'int',
        'resource_ids': 'list[str]'
    }

    attribute_map = {
        'type': 'type',
        'size': 'size',
        'resource_ids': 'resourceIds'
    }

    def __init__(self, type=None, size=None, resource_ids=None):
        """ShowClusterVolumeRsp

        The model defined in huaweicloud sdk

        :param type: 实例磁盘类型。
        :type type: str
        :param size: 实例磁盘大小。
        :type size: int
        :param resource_ids: 该实例拥有的磁盘对应的资源Id。
        :type resource_ids: list[str]
        """
        
        

        self._type = None
        self._size = None
        self._resource_ids = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if size is not None:
            self.size = size
        if resource_ids is not None:
            self.resource_ids = resource_ids

    @property
    def type(self):
        """Gets the type of this ShowClusterVolumeRsp.

        实例磁盘类型。

        :return: The type of this ShowClusterVolumeRsp.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ShowClusterVolumeRsp.

        实例磁盘类型。

        :param type: The type of this ShowClusterVolumeRsp.
        :type type: str
        """
        self._type = type

    @property
    def size(self):
        """Gets the size of this ShowClusterVolumeRsp.

        实例磁盘大小。

        :return: The size of this ShowClusterVolumeRsp.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this ShowClusterVolumeRsp.

        实例磁盘大小。

        :param size: The size of this ShowClusterVolumeRsp.
        :type size: int
        """
        self._size = size

    @property
    def resource_ids(self):
        """Gets the resource_ids of this ShowClusterVolumeRsp.

        该实例拥有的磁盘对应的资源Id。

        :return: The resource_ids of this ShowClusterVolumeRsp.
        :rtype: list[str]
        """
        return self._resource_ids

    @resource_ids.setter
    def resource_ids(self, resource_ids):
        """Sets the resource_ids of this ShowClusterVolumeRsp.

        该实例拥有的磁盘对应的资源Id。

        :param resource_ids: The resource_ids of this ShowClusterVolumeRsp.
        :type resource_ids: list[str]
        """
        self._resource_ids = resource_ids

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
        if not isinstance(other, ShowClusterVolumeRsp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
