# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Sfs3Storage:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'location': 'str',
        'usage': 'str',
        'create_time': 'datetime'
    }

    attribute_map = {
        'name': 'name',
        'location': 'location',
        'usage': 'usage',
        'create_time': 'create_time'
    }

    def __init__(self, name=None, location=None, usage=None, create_time=None):
        r"""Sfs3Storage

        The model defined in huaweicloud sdk

        :param name: 文件系统名称。
        :type name: str
        :param location: 挂载地址。
        :type location: str
        :param usage: 存储使用量(Byte)。
        :type usage: str
        :param create_time: 创建时间。
        :type create_time: datetime
        """
        
        

        self._name = None
        self._location = None
        self._usage = None
        self._create_time = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if location is not None:
            self.location = location
        if usage is not None:
            self.usage = usage
        if create_time is not None:
            self.create_time = create_time

    @property
    def name(self):
        r"""Gets the name of this Sfs3Storage.

        文件系统名称。

        :return: The name of this Sfs3Storage.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this Sfs3Storage.

        文件系统名称。

        :param name: The name of this Sfs3Storage.
        :type name: str
        """
        self._name = name

    @property
    def location(self):
        r"""Gets the location of this Sfs3Storage.

        挂载地址。

        :return: The location of this Sfs3Storage.
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        r"""Sets the location of this Sfs3Storage.

        挂载地址。

        :param location: The location of this Sfs3Storage.
        :type location: str
        """
        self._location = location

    @property
    def usage(self):
        r"""Gets the usage of this Sfs3Storage.

        存储使用量(Byte)。

        :return: The usage of this Sfs3Storage.
        :rtype: str
        """
        return self._usage

    @usage.setter
    def usage(self, usage):
        r"""Sets the usage of this Sfs3Storage.

        存储使用量(Byte)。

        :param usage: The usage of this Sfs3Storage.
        :type usage: str
        """
        self._usage = usage

    @property
    def create_time(self):
        r"""Gets the create_time of this Sfs3Storage.

        创建时间。

        :return: The create_time of this Sfs3Storage.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this Sfs3Storage.

        创建时间。

        :param create_time: The create_time of this Sfs3Storage.
        :type create_time: datetime
        """
        self._create_time = create_time

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
        if not isinstance(other, Sfs3Storage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
