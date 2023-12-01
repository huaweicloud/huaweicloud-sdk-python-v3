# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TopUrl:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'value': 'int',
        'asset_id': 'str',
        'title': 'str',
        'duration': 'int',
        'duration_ms': 'int',
        'size': 'int'
    }

    attribute_map = {
        'value': 'value',
        'asset_id': 'asset_id',
        'title': 'title',
        'duration': 'duration',
        'duration_ms': 'duration_ms',
        'size': 'size'
    }

    def __init__(self, value=None, asset_id=None, title=None, duration=None, duration_ms=None, size=None):
        """TopUrl

        The model defined in huaweicloud sdk

        :param value: 总播放次数。
        :type value: int
        :param asset_id: 媒资ID。
        :type asset_id: str
        :param title: 媒资名称。
        :type title: str
        :param duration: 媒资时长。  单位：秒。
        :type duration: int
        :param duration_ms: 视频时长，单位毫秒。
        :type duration_ms: int
        :param size: 媒资原始大小。  单位：字节。
        :type size: int
        """
        
        

        self._value = None
        self._asset_id = None
        self._title = None
        self._duration = None
        self._duration_ms = None
        self._size = None
        self.discriminator = None

        if value is not None:
            self.value = value
        if asset_id is not None:
            self.asset_id = asset_id
        if title is not None:
            self.title = title
        if duration is not None:
            self.duration = duration
        if duration_ms is not None:
            self.duration_ms = duration_ms
        if size is not None:
            self.size = size

    @property
    def value(self):
        """Gets the value of this TopUrl.

        总播放次数。

        :return: The value of this TopUrl.
        :rtype: int
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this TopUrl.

        总播放次数。

        :param value: The value of this TopUrl.
        :type value: int
        """
        self._value = value

    @property
    def asset_id(self):
        """Gets the asset_id of this TopUrl.

        媒资ID。

        :return: The asset_id of this TopUrl.
        :rtype: str
        """
        return self._asset_id

    @asset_id.setter
    def asset_id(self, asset_id):
        """Sets the asset_id of this TopUrl.

        媒资ID。

        :param asset_id: The asset_id of this TopUrl.
        :type asset_id: str
        """
        self._asset_id = asset_id

    @property
    def title(self):
        """Gets the title of this TopUrl.

        媒资名称。

        :return: The title of this TopUrl.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this TopUrl.

        媒资名称。

        :param title: The title of this TopUrl.
        :type title: str
        """
        self._title = title

    @property
    def duration(self):
        """Gets the duration of this TopUrl.

        媒资时长。  单位：秒。

        :return: The duration of this TopUrl.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this TopUrl.

        媒资时长。  单位：秒。

        :param duration: The duration of this TopUrl.
        :type duration: int
        """
        self._duration = duration

    @property
    def duration_ms(self):
        """Gets the duration_ms of this TopUrl.

        视频时长，单位毫秒。

        :return: The duration_ms of this TopUrl.
        :rtype: int
        """
        return self._duration_ms

    @duration_ms.setter
    def duration_ms(self, duration_ms):
        """Sets the duration_ms of this TopUrl.

        视频时长，单位毫秒。

        :param duration_ms: The duration_ms of this TopUrl.
        :type duration_ms: int
        """
        self._duration_ms = duration_ms

    @property
    def size(self):
        """Gets the size of this TopUrl.

        媒资原始大小。  单位：字节。

        :return: The size of this TopUrl.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this TopUrl.

        媒资原始大小。  单位：字节。

        :param size: The size of this TopUrl.
        :type size: int
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
        if not isinstance(other, TopUrl):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
