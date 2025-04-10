# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HttpIpGroup:

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
        'name': 'str',
        'ips': 'list[str]',
        'size': 'int',
        'description': 'str',
        'create_time': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'ips': 'ips',
        'size': 'size',
        'description': 'description',
        'create_time': 'create_time'
    }

    def __init__(self, id=None, name=None, ips=None, size=None, description=None, create_time=None):
        r"""HttpIpGroup

        The model defined in huaweicloud sdk

        :param id: ip地址组id
        :type id: str
        :param name: ip地址组名称
        :type name: str
        :param ips: ip地址/地址段列表
        :type ips: list[str]
        :param size: ip地址/地址段大小
        :type size: int
        :param description: ip地址组描述
        :type description: str
        :param create_time: ip地址组创建时间戳
        :type create_time: int
        """
        
        

        self._id = None
        self._name = None
        self._ips = None
        self._size = None
        self._description = None
        self._create_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if ips is not None:
            self.ips = ips
        if size is not None:
            self.size = size
        if description is not None:
            self.description = description
        if create_time is not None:
            self.create_time = create_time

    @property
    def id(self):
        r"""Gets the id of this HttpIpGroup.

        ip地址组id

        :return: The id of this HttpIpGroup.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this HttpIpGroup.

        ip地址组id

        :param id: The id of this HttpIpGroup.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this HttpIpGroup.

        ip地址组名称

        :return: The name of this HttpIpGroup.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this HttpIpGroup.

        ip地址组名称

        :param name: The name of this HttpIpGroup.
        :type name: str
        """
        self._name = name

    @property
    def ips(self):
        r"""Gets the ips of this HttpIpGroup.

        ip地址/地址段列表

        :return: The ips of this HttpIpGroup.
        :rtype: list[str]
        """
        return self._ips

    @ips.setter
    def ips(self, ips):
        r"""Sets the ips of this HttpIpGroup.

        ip地址/地址段列表

        :param ips: The ips of this HttpIpGroup.
        :type ips: list[str]
        """
        self._ips = ips

    @property
    def size(self):
        r"""Gets the size of this HttpIpGroup.

        ip地址/地址段大小

        :return: The size of this HttpIpGroup.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this HttpIpGroup.

        ip地址/地址段大小

        :param size: The size of this HttpIpGroup.
        :type size: int
        """
        self._size = size

    @property
    def description(self):
        r"""Gets the description of this HttpIpGroup.

        ip地址组描述

        :return: The description of this HttpIpGroup.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this HttpIpGroup.

        ip地址组描述

        :param description: The description of this HttpIpGroup.
        :type description: str
        """
        self._description = description

    @property
    def create_time(self):
        r"""Gets the create_time of this HttpIpGroup.

        ip地址组创建时间戳

        :return: The create_time of this HttpIpGroup.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this HttpIpGroup.

        ip地址组创建时间戳

        :param create_time: The create_time of this HttpIpGroup.
        :type create_time: int
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
        if not isinstance(other, HttpIpGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
