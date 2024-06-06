# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Volume:

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
        'resource_info': 'dict(str, str)',
        'resource_name': 'str',
        'resource_type': 'str',
        'resource_sub_type': 'str',
        'access': 'str',
        'time': 'str'
    }

    attribute_map = {
        'id': 'id',
        'resource_info': 'resource_info',
        'resource_name': 'resource_name',
        'resource_type': 'resource_type',
        'resource_sub_type': 'resource_sub_type',
        'access': 'access',
        'time': 'time'
    }

    def __init__(self, id=None, resource_info=None, resource_name=None, resource_type=None, resource_sub_type=None, access=None, time=None):
        """Volume

        The model defined in huaweicloud sdk

        :param id: 云存储ID。
        :type id: str
        :param resource_info: 存储资源详情。
        :type resource_info: dict(str, str)
        :param resource_name: 云存储名称。
        :type resource_name: str
        :param resource_type: 资源类型，当前只支持“obs”和“sfs”。
        :type resource_type: str
        :param resource_sub_type: 存储资源子类型。
        :type resource_sub_type: str
        :param access: 用户access key。
        :type access: str
        :param time: 创建时间。
        :type time: str
        """
        
        

        self._id = None
        self._resource_info = None
        self._resource_name = None
        self._resource_type = None
        self._resource_sub_type = None
        self._access = None
        self._time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if resource_info is not None:
            self.resource_info = resource_info
        if resource_name is not None:
            self.resource_name = resource_name
        if resource_type is not None:
            self.resource_type = resource_type
        if resource_sub_type is not None:
            self.resource_sub_type = resource_sub_type
        if access is not None:
            self.access = access
        if time is not None:
            self.time = time

    @property
    def id(self):
        """Gets the id of this Volume.

        云存储ID。

        :return: The id of this Volume.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Volume.

        云存储ID。

        :param id: The id of this Volume.
        :type id: str
        """
        self._id = id

    @property
    def resource_info(self):
        """Gets the resource_info of this Volume.

        存储资源详情。

        :return: The resource_info of this Volume.
        :rtype: dict(str, str)
        """
        return self._resource_info

    @resource_info.setter
    def resource_info(self, resource_info):
        """Sets the resource_info of this Volume.

        存储资源详情。

        :param resource_info: The resource_info of this Volume.
        :type resource_info: dict(str, str)
        """
        self._resource_info = resource_info

    @property
    def resource_name(self):
        """Gets the resource_name of this Volume.

        云存储名称。

        :return: The resource_name of this Volume.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        """Sets the resource_name of this Volume.

        云存储名称。

        :param resource_name: The resource_name of this Volume.
        :type resource_name: str
        """
        self._resource_name = resource_name

    @property
    def resource_type(self):
        """Gets the resource_type of this Volume.

        资源类型，当前只支持“obs”和“sfs”。

        :return: The resource_type of this Volume.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this Volume.

        资源类型，当前只支持“obs”和“sfs”。

        :param resource_type: The resource_type of this Volume.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def resource_sub_type(self):
        """Gets the resource_sub_type of this Volume.

        存储资源子类型。

        :return: The resource_sub_type of this Volume.
        :rtype: str
        """
        return self._resource_sub_type

    @resource_sub_type.setter
    def resource_sub_type(self, resource_sub_type):
        """Sets the resource_sub_type of this Volume.

        存储资源子类型。

        :param resource_sub_type: The resource_sub_type of this Volume.
        :type resource_sub_type: str
        """
        self._resource_sub_type = resource_sub_type

    @property
    def access(self):
        """Gets the access of this Volume.

        用户access key。

        :return: The access of this Volume.
        :rtype: str
        """
        return self._access

    @access.setter
    def access(self, access):
        """Sets the access of this Volume.

        用户access key。

        :param access: The access of this Volume.
        :type access: str
        """
        self._access = access

    @property
    def time(self):
        """Gets the time of this Volume.

        创建时间。

        :return: The time of this Volume.
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this Volume.

        创建时间。

        :param time: The time of this Volume.
        :type time: str
        """
        self._time = time

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
        if not isinstance(other, Volume):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
