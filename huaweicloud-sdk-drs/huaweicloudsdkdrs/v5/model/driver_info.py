# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DriverInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'driver_name': 'str',
        'last_modified': 'str',
        'size': 'int'
    }

    attribute_map = {
        'driver_name': 'driver_name',
        'last_modified': 'last_modified',
        'size': 'size'
    }

    def __init__(self, driver_name=None, last_modified=None, size=None):
        r"""DriverInfo

        The model defined in huaweicloud sdk

        :param driver_name: 文件名称。
        :type driver_name: str
        :param last_modified: 最后修改时间。
        :type last_modified: str
        :param size: 文件大小，单位：byte
        :type size: int
        """
        
        

        self._driver_name = None
        self._last_modified = None
        self._size = None
        self.discriminator = None

        if driver_name is not None:
            self.driver_name = driver_name
        if last_modified is not None:
            self.last_modified = last_modified
        if size is not None:
            self.size = size

    @property
    def driver_name(self):
        r"""Gets the driver_name of this DriverInfo.

        文件名称。

        :return: The driver_name of this DriverInfo.
        :rtype: str
        """
        return self._driver_name

    @driver_name.setter
    def driver_name(self, driver_name):
        r"""Sets the driver_name of this DriverInfo.

        文件名称。

        :param driver_name: The driver_name of this DriverInfo.
        :type driver_name: str
        """
        self._driver_name = driver_name

    @property
    def last_modified(self):
        r"""Gets the last_modified of this DriverInfo.

        最后修改时间。

        :return: The last_modified of this DriverInfo.
        :rtype: str
        """
        return self._last_modified

    @last_modified.setter
    def last_modified(self, last_modified):
        r"""Sets the last_modified of this DriverInfo.

        最后修改时间。

        :param last_modified: The last_modified of this DriverInfo.
        :type last_modified: str
        """
        self._last_modified = last_modified

    @property
    def size(self):
        r"""Gets the size of this DriverInfo.

        文件大小，单位：byte

        :return: The size of this DriverInfo.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this DriverInfo.

        文件大小，单位：byte

        :param size: The size of this DriverInfo.
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
        if not isinstance(other, DriverInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
