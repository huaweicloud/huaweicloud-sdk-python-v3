# coding: utf-8

import re
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
        'index': 'int',
        'name': 'str',
        'disktype': 'str',
        'size': 'int'
    }

    attribute_map = {
        'index': 'index',
        'name': 'name',
        'disktype': 'disktype',
        'size': 'size'
    }

    def __init__(self, index=None, name=None, disktype=None, size=None):
        """TemplateDisk - a model defined in huaweicloud sdk"""
        
        

        self._index = None
        self._name = None
        self._disktype = None
        self._size = None
        self.discriminator = None

        self.index = index
        self.name = name
        self.disktype = disktype
        self.size = size

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
        :type: int
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
        :type: str
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
        :type: str
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
        :type: int
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
        if not isinstance(other, TemplateDisk):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
