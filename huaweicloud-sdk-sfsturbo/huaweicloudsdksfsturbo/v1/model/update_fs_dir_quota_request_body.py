# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateFsDirQuotaRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'path': 'str',
        'capacity': 'int',
        'inode': 'int'
    }

    attribute_map = {
        'path': 'path',
        'capacity': 'capacity',
        'inode': 'inode'
    }

    def __init__(self, path=None, capacity=None, inode=None):
        r"""UpdateFsDirQuotaRequestBody

        The model defined in huaweicloud sdk

        :param path: 合法的已存在的目录的全路径
        :type path: str
        :param capacity: 目录的容量大小，单位：MB; 设置为0会导致数据无法写入目录; capacity和quota至少二选一
        :type capacity: int
        :param inode: 目录的inode数量限制; 设置为0会导致数据无法写入目录; capacity和quota至少二选一
        :type inode: int
        """
        
        

        self._path = None
        self._capacity = None
        self._inode = None
        self.discriminator = None

        self.path = path
        if capacity is not None:
            self.capacity = capacity
        if inode is not None:
            self.inode = inode

    @property
    def path(self):
        r"""Gets the path of this UpdateFsDirQuotaRequestBody.

        合法的已存在的目录的全路径

        :return: The path of this UpdateFsDirQuotaRequestBody.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        r"""Sets the path of this UpdateFsDirQuotaRequestBody.

        合法的已存在的目录的全路径

        :param path: The path of this UpdateFsDirQuotaRequestBody.
        :type path: str
        """
        self._path = path

    @property
    def capacity(self):
        r"""Gets the capacity of this UpdateFsDirQuotaRequestBody.

        目录的容量大小，单位：MB; 设置为0会导致数据无法写入目录; capacity和quota至少二选一

        :return: The capacity of this UpdateFsDirQuotaRequestBody.
        :rtype: int
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        r"""Sets the capacity of this UpdateFsDirQuotaRequestBody.

        目录的容量大小，单位：MB; 设置为0会导致数据无法写入目录; capacity和quota至少二选一

        :param capacity: The capacity of this UpdateFsDirQuotaRequestBody.
        :type capacity: int
        """
        self._capacity = capacity

    @property
    def inode(self):
        r"""Gets the inode of this UpdateFsDirQuotaRequestBody.

        目录的inode数量限制; 设置为0会导致数据无法写入目录; capacity和quota至少二选一

        :return: The inode of this UpdateFsDirQuotaRequestBody.
        :rtype: int
        """
        return self._inode

    @inode.setter
    def inode(self, inode):
        r"""Sets the inode of this UpdateFsDirQuotaRequestBody.

        目录的inode数量限制; 设置为0会导致数据无法写入目录; capacity和quota至少二选一

        :param inode: The inode of this UpdateFsDirQuotaRequestBody.
        :type inode: int
        """
        self._inode = inode

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
        if not isinstance(other, UpdateFsDirQuotaRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
