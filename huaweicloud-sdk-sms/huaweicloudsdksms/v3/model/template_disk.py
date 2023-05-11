# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TemplateDisk:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'index': 'int',
        'name': 'str',
        'disktype': 'str',
        'size': 'int',
        'device_use': 'str'
    }

    attribute_map = {
        'id': 'id',
        'index': 'index',
        'name': 'name',
        'disktype': 'disktype',
        'size': 'size',
        'device_use': 'device_use'
    }

    def __init__(self, id=None, index=None, name=None, disktype=None, size=None, device_use=None):
        """TemplateDisk

        The model defined in huaweicloud sdk

        :param id: 磁盘ID
        :type id: int
        :param index: 磁盘序号，从0开始
        :type index: int
        :param name: 磁盘名称
        :type name: str
        :param disktype: 磁盘类型，同volumetype字段
        :type disktype: str
        :param size: 磁盘大小，单位：GB
        :type size: int
        :param device_use: 磁盘使用
        :type device_use: str
        """
        
        

        self._id = None
        self._index = None
        self._name = None
        self._disktype = None
        self._size = None
        self._device_use = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.index = index
        self.name = name
        self.disktype = disktype
        self.size = size
        if device_use is not None:
            self.device_use = device_use

    @property
    def id(self):
        """Gets the id of this TemplateDisk.

        磁盘ID

        :return: The id of this TemplateDisk.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TemplateDisk.

        磁盘ID

        :param id: The id of this TemplateDisk.
        :type id: int
        """
        self._id = id

    @property
    def index(self):
        """Gets the index of this TemplateDisk.

        磁盘序号，从0开始

        :return: The index of this TemplateDisk.
        :rtype: int
        """
        return self._index

    @index.setter
    def index(self, index):
        """Sets the index of this TemplateDisk.

        磁盘序号，从0开始

        :param index: The index of this TemplateDisk.
        :type index: int
        """
        self._index = index

    @property
    def name(self):
        """Gets the name of this TemplateDisk.

        磁盘名称

        :return: The name of this TemplateDisk.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TemplateDisk.

        磁盘名称

        :param name: The name of this TemplateDisk.
        :type name: str
        """
        self._name = name

    @property
    def disktype(self):
        """Gets the disktype of this TemplateDisk.

        磁盘类型，同volumetype字段

        :return: The disktype of this TemplateDisk.
        :rtype: str
        """
        return self._disktype

    @disktype.setter
    def disktype(self, disktype):
        """Sets the disktype of this TemplateDisk.

        磁盘类型，同volumetype字段

        :param disktype: The disktype of this TemplateDisk.
        :type disktype: str
        """
        self._disktype = disktype

    @property
    def size(self):
        """Gets the size of this TemplateDisk.

        磁盘大小，单位：GB

        :return: The size of this TemplateDisk.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this TemplateDisk.

        磁盘大小，单位：GB

        :param size: The size of this TemplateDisk.
        :type size: int
        """
        self._size = size

    @property
    def device_use(self):
        """Gets the device_use of this TemplateDisk.

        磁盘使用

        :return: The device_use of this TemplateDisk.
        :rtype: str
        """
        return self._device_use

    @device_use.setter
    def device_use(self, device_use):
        """Sets the device_use of this TemplateDisk.

        磁盘使用

        :param device_use: The device_use of this TemplateDisk.
        :type device_use: str
        """
        self._device_use = device_use

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
        if not isinstance(other, TemplateDisk):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
