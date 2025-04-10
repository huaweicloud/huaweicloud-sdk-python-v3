# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateFsDirQuotaResponse(SdkResponse):

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
        'inode': 'int',
        'used_capacity': 'int',
        'used_inode': 'int'
    }

    attribute_map = {
        'path': 'path',
        'capacity': 'capacity',
        'inode': 'inode',
        'used_capacity': 'used_capacity',
        'used_inode': 'used_inode'
    }

    def __init__(self, path=None, capacity=None, inode=None, used_capacity=None, used_inode=None):
        r"""UpdateFsDirQuotaResponse

        The model defined in huaweicloud sdk

        :param path: 合法的已存在的目录的全路径
        :type path: str
        :param capacity: 目录的容量大小，单位：MB
        :type capacity: int
        :param inode: 目录的inode数量限制
        :type inode: int
        :param used_capacity: 目录已使用的容量大小，单位：MB。仅SFSTurbo 20MB/s/TiB、40MB/s/TiB、125MB/s/TiB、250MB/s/TiB、500MB/s/TiB、1000MB/s/TiB返回该字段
        :type used_capacity: int
        :param used_inode: 目录的已使用的inode数量。仅SFSTurbo 20MB/s/TiB、40MB/s/TiB、125MB/s/TiB、250MB/s/TiB、500MB/s/TiB、1000MB/s/TiB返回该字段
        :type used_inode: int
        """
        
        super(UpdateFsDirQuotaResponse, self).__init__()

        self._path = None
        self._capacity = None
        self._inode = None
        self._used_capacity = None
        self._used_inode = None
        self.discriminator = None

        if path is not None:
            self.path = path
        if capacity is not None:
            self.capacity = capacity
        if inode is not None:
            self.inode = inode
        if used_capacity is not None:
            self.used_capacity = used_capacity
        if used_inode is not None:
            self.used_inode = used_inode

    @property
    def path(self):
        r"""Gets the path of this UpdateFsDirQuotaResponse.

        合法的已存在的目录的全路径

        :return: The path of this UpdateFsDirQuotaResponse.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        r"""Sets the path of this UpdateFsDirQuotaResponse.

        合法的已存在的目录的全路径

        :param path: The path of this UpdateFsDirQuotaResponse.
        :type path: str
        """
        self._path = path

    @property
    def capacity(self):
        r"""Gets the capacity of this UpdateFsDirQuotaResponse.

        目录的容量大小，单位：MB

        :return: The capacity of this UpdateFsDirQuotaResponse.
        :rtype: int
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        r"""Sets the capacity of this UpdateFsDirQuotaResponse.

        目录的容量大小，单位：MB

        :param capacity: The capacity of this UpdateFsDirQuotaResponse.
        :type capacity: int
        """
        self._capacity = capacity

    @property
    def inode(self):
        r"""Gets the inode of this UpdateFsDirQuotaResponse.

        目录的inode数量限制

        :return: The inode of this UpdateFsDirQuotaResponse.
        :rtype: int
        """
        return self._inode

    @inode.setter
    def inode(self, inode):
        r"""Sets the inode of this UpdateFsDirQuotaResponse.

        目录的inode数量限制

        :param inode: The inode of this UpdateFsDirQuotaResponse.
        :type inode: int
        """
        self._inode = inode

    @property
    def used_capacity(self):
        r"""Gets the used_capacity of this UpdateFsDirQuotaResponse.

        目录已使用的容量大小，单位：MB。仅SFSTurbo 20MB/s/TiB、40MB/s/TiB、125MB/s/TiB、250MB/s/TiB、500MB/s/TiB、1000MB/s/TiB返回该字段

        :return: The used_capacity of this UpdateFsDirQuotaResponse.
        :rtype: int
        """
        return self._used_capacity

    @used_capacity.setter
    def used_capacity(self, used_capacity):
        r"""Sets the used_capacity of this UpdateFsDirQuotaResponse.

        目录已使用的容量大小，单位：MB。仅SFSTurbo 20MB/s/TiB、40MB/s/TiB、125MB/s/TiB、250MB/s/TiB、500MB/s/TiB、1000MB/s/TiB返回该字段

        :param used_capacity: The used_capacity of this UpdateFsDirQuotaResponse.
        :type used_capacity: int
        """
        self._used_capacity = used_capacity

    @property
    def used_inode(self):
        r"""Gets the used_inode of this UpdateFsDirQuotaResponse.

        目录的已使用的inode数量。仅SFSTurbo 20MB/s/TiB、40MB/s/TiB、125MB/s/TiB、250MB/s/TiB、500MB/s/TiB、1000MB/s/TiB返回该字段

        :return: The used_inode of this UpdateFsDirQuotaResponse.
        :rtype: int
        """
        return self._used_inode

    @used_inode.setter
    def used_inode(self, used_inode):
        r"""Sets the used_inode of this UpdateFsDirQuotaResponse.

        目录的已使用的inode数量。仅SFSTurbo 20MB/s/TiB、40MB/s/TiB、125MB/s/TiB、250MB/s/TiB、500MB/s/TiB、1000MB/s/TiB返回该字段

        :param used_inode: The used_inode of this UpdateFsDirQuotaResponse.
        :type used_inode: int
        """
        self._used_inode = used_inode

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
        if not isinstance(other, UpdateFsDirQuotaResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
