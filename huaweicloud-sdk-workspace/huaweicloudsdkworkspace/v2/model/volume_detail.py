# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VolumeDetail:

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
        'device': 'str',
        'id': 'str',
        'volume_id': 'str',
        'create_time': 'str',
        'display_name': 'str'
    }

    attribute_map = {
        'type': 'type',
        'size': 'size',
        'device': 'device',
        'id': 'id',
        'volume_id': 'volume_id',
        'create_time': 'create_time',
        'display_name': 'display_name'
    }

    def __init__(self, type=None, size=None, device=None, id=None, volume_id=None, create_time=None, display_name=None):
        """VolumeDetail

        The model defined in huaweicloud sdk

        :param type: 桌面数据盘对应的磁盘类型，需要与系统所提供的磁盘类型相匹配。  - SAS：高IO。 - SSD：超高IO。
        :type type: str
        :param size: 磁盘容量，单位GB。
        :type size: int
        :param device: 挂载目录。
        :type device: str
        :param id: 磁盘表唯一标识ID。
        :type id: str
        :param volume_id: 磁盘ID。
        :type volume_id: str
        :param create_time: 磁盘的创建时间
        :type create_time: str
        :param display_name: 磁盘名
        :type display_name: str
        """
        
        

        self._type = None
        self._size = None
        self._device = None
        self._id = None
        self._volume_id = None
        self._create_time = None
        self._display_name = None
        self.discriminator = None

        self.type = type
        self.size = size
        if device is not None:
            self.device = device
        if id is not None:
            self.id = id
        if volume_id is not None:
            self.volume_id = volume_id
        if create_time is not None:
            self.create_time = create_time
        if display_name is not None:
            self.display_name = display_name

    @property
    def type(self):
        """Gets the type of this VolumeDetail.

        桌面数据盘对应的磁盘类型，需要与系统所提供的磁盘类型相匹配。  - SAS：高IO。 - SSD：超高IO。

        :return: The type of this VolumeDetail.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this VolumeDetail.

        桌面数据盘对应的磁盘类型，需要与系统所提供的磁盘类型相匹配。  - SAS：高IO。 - SSD：超高IO。

        :param type: The type of this VolumeDetail.
        :type type: str
        """
        self._type = type

    @property
    def size(self):
        """Gets the size of this VolumeDetail.

        磁盘容量，单位GB。

        :return: The size of this VolumeDetail.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this VolumeDetail.

        磁盘容量，单位GB。

        :param size: The size of this VolumeDetail.
        :type size: int
        """
        self._size = size

    @property
    def device(self):
        """Gets the device of this VolumeDetail.

        挂载目录。

        :return: The device of this VolumeDetail.
        :rtype: str
        """
        return self._device

    @device.setter
    def device(self, device):
        """Sets the device of this VolumeDetail.

        挂载目录。

        :param device: The device of this VolumeDetail.
        :type device: str
        """
        self._device = device

    @property
    def id(self):
        """Gets the id of this VolumeDetail.

        磁盘表唯一标识ID。

        :return: The id of this VolumeDetail.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VolumeDetail.

        磁盘表唯一标识ID。

        :param id: The id of this VolumeDetail.
        :type id: str
        """
        self._id = id

    @property
    def volume_id(self):
        """Gets the volume_id of this VolumeDetail.

        磁盘ID。

        :return: The volume_id of this VolumeDetail.
        :rtype: str
        """
        return self._volume_id

    @volume_id.setter
    def volume_id(self, volume_id):
        """Sets the volume_id of this VolumeDetail.

        磁盘ID。

        :param volume_id: The volume_id of this VolumeDetail.
        :type volume_id: str
        """
        self._volume_id = volume_id

    @property
    def create_time(self):
        """Gets the create_time of this VolumeDetail.

        磁盘的创建时间

        :return: The create_time of this VolumeDetail.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this VolumeDetail.

        磁盘的创建时间

        :param create_time: The create_time of this VolumeDetail.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def display_name(self):
        """Gets the display_name of this VolumeDetail.

        磁盘名

        :return: The display_name of this VolumeDetail.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this VolumeDetail.

        磁盘名

        :param display_name: The display_name of this VolumeDetail.
        :type display_name: str
        """
        self._display_name = display_name

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
        if not isinstance(other, VolumeDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
