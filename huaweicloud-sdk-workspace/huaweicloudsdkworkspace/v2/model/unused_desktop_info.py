# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UnusedDesktopInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'desktop_id': 'str',
        'compute_name': 'str',
        'create_time': 'str',
        'disconnect_time': 'str'
    }

    attribute_map = {
        'desktop_id': 'desktop_id',
        'compute_name': 'compute_name',
        'create_time': 'create_time',
        'disconnect_time': 'disconnect_time'
    }

    def __init__(self, desktop_id=None, compute_name=None, create_time=None, disconnect_time=None):
        """UnusedDesktopInfo

        The model defined in huaweicloud sdk

        :param desktop_id: 桌面id。
        :type desktop_id: str
        :param compute_name: 桌面名称。
        :type compute_name: str
        :param create_time: 桌面创建时间。
        :type create_time: str
        :param disconnect_time: 最近一次断连时间。
        :type disconnect_time: str
        """
        
        

        self._desktop_id = None
        self._compute_name = None
        self._create_time = None
        self._disconnect_time = None
        self.discriminator = None

        if desktop_id is not None:
            self.desktop_id = desktop_id
        if compute_name is not None:
            self.compute_name = compute_name
        if create_time is not None:
            self.create_time = create_time
        if disconnect_time is not None:
            self.disconnect_time = disconnect_time

    @property
    def desktop_id(self):
        """Gets the desktop_id of this UnusedDesktopInfo.

        桌面id。

        :return: The desktop_id of this UnusedDesktopInfo.
        :rtype: str
        """
        return self._desktop_id

    @desktop_id.setter
    def desktop_id(self, desktop_id):
        """Sets the desktop_id of this UnusedDesktopInfo.

        桌面id。

        :param desktop_id: The desktop_id of this UnusedDesktopInfo.
        :type desktop_id: str
        """
        self._desktop_id = desktop_id

    @property
    def compute_name(self):
        """Gets the compute_name of this UnusedDesktopInfo.

        桌面名称。

        :return: The compute_name of this UnusedDesktopInfo.
        :rtype: str
        """
        return self._compute_name

    @compute_name.setter
    def compute_name(self, compute_name):
        """Sets the compute_name of this UnusedDesktopInfo.

        桌面名称。

        :param compute_name: The compute_name of this UnusedDesktopInfo.
        :type compute_name: str
        """
        self._compute_name = compute_name

    @property
    def create_time(self):
        """Gets the create_time of this UnusedDesktopInfo.

        桌面创建时间。

        :return: The create_time of this UnusedDesktopInfo.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this UnusedDesktopInfo.

        桌面创建时间。

        :param create_time: The create_time of this UnusedDesktopInfo.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def disconnect_time(self):
        """Gets the disconnect_time of this UnusedDesktopInfo.

        最近一次断连时间。

        :return: The disconnect_time of this UnusedDesktopInfo.
        :rtype: str
        """
        return self._disconnect_time

    @disconnect_time.setter
    def disconnect_time(self, disconnect_time):
        """Sets the disconnect_time of this UnusedDesktopInfo.

        最近一次断连时间。

        :param disconnect_time: The disconnect_time of this UnusedDesktopInfo.
        :type disconnect_time: str
        """
        self._disconnect_time = disconnect_time

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
        if not isinstance(other, UnusedDesktopInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
