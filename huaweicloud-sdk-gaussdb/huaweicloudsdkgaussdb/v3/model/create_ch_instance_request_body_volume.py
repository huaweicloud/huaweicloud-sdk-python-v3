# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateChInstanceRequestBodyVolume:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'io_type': 'str',
        'capacity_in_gb': 'int'
    }

    attribute_map = {
        'io_type': 'io_type',
        'capacity_in_gb': 'capacity_in_gb'
    }

    def __init__(self, io_type=None, capacity_in_gb=None):
        r"""CreateChInstanceRequestBodyVolume

        The model defined in huaweicloud sdk

        :param io_type: 磁盘IO类型。 取值范围： - SSD：超高IO - ESSD：极速型SSD
        :type io_type: str
        :param capacity_in_gb: 磁盘容量。取值范围：50GB~32000GB。
        :type capacity_in_gb: int
        """
        
        

        self._io_type = None
        self._capacity_in_gb = None
        self.discriminator = None

        self.io_type = io_type
        self.capacity_in_gb = capacity_in_gb

    @property
    def io_type(self):
        r"""Gets the io_type of this CreateChInstanceRequestBodyVolume.

        磁盘IO类型。 取值范围： - SSD：超高IO - ESSD：极速型SSD

        :return: The io_type of this CreateChInstanceRequestBodyVolume.
        :rtype: str
        """
        return self._io_type

    @io_type.setter
    def io_type(self, io_type):
        r"""Sets the io_type of this CreateChInstanceRequestBodyVolume.

        磁盘IO类型。 取值范围： - SSD：超高IO - ESSD：极速型SSD

        :param io_type: The io_type of this CreateChInstanceRequestBodyVolume.
        :type io_type: str
        """
        self._io_type = io_type

    @property
    def capacity_in_gb(self):
        r"""Gets the capacity_in_gb of this CreateChInstanceRequestBodyVolume.

        磁盘容量。取值范围：50GB~32000GB。

        :return: The capacity_in_gb of this CreateChInstanceRequestBodyVolume.
        :rtype: int
        """
        return self._capacity_in_gb

    @capacity_in_gb.setter
    def capacity_in_gb(self, capacity_in_gb):
        r"""Sets the capacity_in_gb of this CreateChInstanceRequestBodyVolume.

        磁盘容量。取值范围：50GB~32000GB。

        :param capacity_in_gb: The capacity_in_gb of this CreateChInstanceRequestBodyVolume.
        :type capacity_in_gb: int
        """
        self._capacity_in_gb = capacity_in_gb

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
        if not isinstance(other, CreateChInstanceRequestBodyVolume):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
