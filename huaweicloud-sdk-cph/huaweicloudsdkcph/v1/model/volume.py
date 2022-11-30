# coding: utf-8

import re
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
        'volume_name': 'str',
        'volume_id': 'str',
        'volume_size': 'int',
        'volume_type': 'str',
        'create_time': 'str',
        'update_time': 'str'
    }

    attribute_map = {
        'volume_name': 'volume_name',
        'volume_id': 'volume_id',
        'volume_size': 'volume_size',
        'volume_type': 'volume_type',
        'create_time': 'create_time',
        'update_time': 'update_time'
    }

    def __init__(self, volume_name=None, volume_id=None, volume_size=None, volume_type=None, create_time=None, update_time=None):
        """Volume

        The model defined in huaweicloud sdk

        :param volume_name: 云手机服务器的硬盘名称
        :type volume_name: str
        :param volume_id: 云手机服务器的硬盘唯一标识
        :type volume_id: str
        :param volume_size: 云手机服务器的硬盘大小，单位G
        :type volume_size: int
        :param volume_type: 云手机服务器的硬盘类型
        :type volume_type: str
        :param create_time: 硬盘创建时间  时间格式为UTC，YYYY-MM-DDTHH:MM:SSZ
        :type create_time: str
        :param update_time: 硬盘更新时间  时间格式为UTC，YYYY-MM-DDTHH:MM:SSZ
        :type update_time: str
        """
        
        

        self._volume_name = None
        self._volume_id = None
        self._volume_size = None
        self._volume_type = None
        self._create_time = None
        self._update_time = None
        self.discriminator = None

        if volume_name is not None:
            self.volume_name = volume_name
        if volume_id is not None:
            self.volume_id = volume_id
        if volume_size is not None:
            self.volume_size = volume_size
        if volume_type is not None:
            self.volume_type = volume_type
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def volume_name(self):
        """Gets the volume_name of this Volume.

        云手机服务器的硬盘名称

        :return: The volume_name of this Volume.
        :rtype: str
        """
        return self._volume_name

    @volume_name.setter
    def volume_name(self, volume_name):
        """Sets the volume_name of this Volume.

        云手机服务器的硬盘名称

        :param volume_name: The volume_name of this Volume.
        :type volume_name: str
        """
        self._volume_name = volume_name

    @property
    def volume_id(self):
        """Gets the volume_id of this Volume.

        云手机服务器的硬盘唯一标识

        :return: The volume_id of this Volume.
        :rtype: str
        """
        return self._volume_id

    @volume_id.setter
    def volume_id(self, volume_id):
        """Sets the volume_id of this Volume.

        云手机服务器的硬盘唯一标识

        :param volume_id: The volume_id of this Volume.
        :type volume_id: str
        """
        self._volume_id = volume_id

    @property
    def volume_size(self):
        """Gets the volume_size of this Volume.

        云手机服务器的硬盘大小，单位G

        :return: The volume_size of this Volume.
        :rtype: int
        """
        return self._volume_size

    @volume_size.setter
    def volume_size(self, volume_size):
        """Sets the volume_size of this Volume.

        云手机服务器的硬盘大小，单位G

        :param volume_size: The volume_size of this Volume.
        :type volume_size: int
        """
        self._volume_size = volume_size

    @property
    def volume_type(self):
        """Gets the volume_type of this Volume.

        云手机服务器的硬盘类型

        :return: The volume_type of this Volume.
        :rtype: str
        """
        return self._volume_type

    @volume_type.setter
    def volume_type(self, volume_type):
        """Sets the volume_type of this Volume.

        云手机服务器的硬盘类型

        :param volume_type: The volume_type of this Volume.
        :type volume_type: str
        """
        self._volume_type = volume_type

    @property
    def create_time(self):
        """Gets the create_time of this Volume.

        硬盘创建时间  时间格式为UTC，YYYY-MM-DDTHH:MM:SSZ

        :return: The create_time of this Volume.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this Volume.

        硬盘创建时间  时间格式为UTC，YYYY-MM-DDTHH:MM:SSZ

        :param create_time: The create_time of this Volume.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this Volume.

        硬盘更新时间  时间格式为UTC，YYYY-MM-DDTHH:MM:SSZ

        :return: The update_time of this Volume.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this Volume.

        硬盘更新时间  时间格式为UTC，YYYY-MM-DDTHH:MM:SSZ

        :param update_time: The update_time of this Volume.
        :type update_time: str
        """
        self._update_time = update_time

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
