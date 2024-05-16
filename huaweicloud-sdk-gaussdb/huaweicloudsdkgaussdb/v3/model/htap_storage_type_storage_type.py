# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HtapStorageTypeStorageType:

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
        'az_status': 'dict(str, str)',
        'min_volume_size': 'int'
    }

    attribute_map = {
        'name': 'name',
        'az_status': 'az_status',
        'min_volume_size': 'min_volume_size'
    }

    def __init__(self, name=None, az_status=None, min_volume_size=None):
        """HtapStorageTypeStorageType

        The model defined in huaweicloud sdk

        :param name: 存储介质名。
        :type name: str
        :param az_status: 可支持可用区信息。
        :type az_status: dict(str, str)
        :param min_volume_size: 最小可提供磁盘大小。
        :type min_volume_size: int
        """
        
        

        self._name = None
        self._az_status = None
        self._min_volume_size = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if az_status is not None:
            self.az_status = az_status
        if min_volume_size is not None:
            self.min_volume_size = min_volume_size

    @property
    def name(self):
        """Gets the name of this HtapStorageTypeStorageType.

        存储介质名。

        :return: The name of this HtapStorageTypeStorageType.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this HtapStorageTypeStorageType.

        存储介质名。

        :param name: The name of this HtapStorageTypeStorageType.
        :type name: str
        """
        self._name = name

    @property
    def az_status(self):
        """Gets the az_status of this HtapStorageTypeStorageType.

        可支持可用区信息。

        :return: The az_status of this HtapStorageTypeStorageType.
        :rtype: dict(str, str)
        """
        return self._az_status

    @az_status.setter
    def az_status(self, az_status):
        """Sets the az_status of this HtapStorageTypeStorageType.

        可支持可用区信息。

        :param az_status: The az_status of this HtapStorageTypeStorageType.
        :type az_status: dict(str, str)
        """
        self._az_status = az_status

    @property
    def min_volume_size(self):
        """Gets the min_volume_size of this HtapStorageTypeStorageType.

        最小可提供磁盘大小。

        :return: The min_volume_size of this HtapStorageTypeStorageType.
        :rtype: int
        """
        return self._min_volume_size

    @min_volume_size.setter
    def min_volume_size(self, min_volume_size):
        """Sets the min_volume_size of this HtapStorageTypeStorageType.

        最小可提供磁盘大小。

        :param min_volume_size: The min_volume_size of this HtapStorageTypeStorageType.
        :type min_volume_size: int
        """
        self._min_volume_size = min_volume_size

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
        if not isinstance(other, HtapStorageTypeStorageType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
