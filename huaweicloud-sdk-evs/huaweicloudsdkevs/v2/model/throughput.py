# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Throughput:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'frozened': 'bool',
        'id': 'str',
        'total_val': 'int'
    }

    attribute_map = {
        'frozened': 'frozened',
        'id': 'id',
        'total_val': 'total_val'
    }

    def __init__(self, frozened=None, id=None, total_val=None):
        """Throughput

        The model defined in huaweicloud sdk

        :param frozened: 冻结标签。
        :type frozened: bool
        :param id: 云硬盘吞吐量标识。
        :type id: str
        :param total_val: 吞吐量大小。
        :type total_val: int
        """
        
        

        self._frozened = None
        self._id = None
        self._total_val = None
        self.discriminator = None

        self.frozened = frozened
        self.id = id
        self.total_val = total_val

    @property
    def frozened(self):
        """Gets the frozened of this Throughput.

        冻结标签。

        :return: The frozened of this Throughput.
        :rtype: bool
        """
        return self._frozened

    @frozened.setter
    def frozened(self, frozened):
        """Sets the frozened of this Throughput.

        冻结标签。

        :param frozened: The frozened of this Throughput.
        :type frozened: bool
        """
        self._frozened = frozened

    @property
    def id(self):
        """Gets the id of this Throughput.

        云硬盘吞吐量标识。

        :return: The id of this Throughput.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Throughput.

        云硬盘吞吐量标识。

        :param id: The id of this Throughput.
        :type id: str
        """
        self._id = id

    @property
    def total_val(self):
        """Gets the total_val of this Throughput.

        吞吐量大小。

        :return: The total_val of this Throughput.
        :rtype: int
        """
        return self._total_val

    @total_val.setter
    def total_val(self, total_val):
        """Sets the total_val of this Throughput.

        吞吐量大小。

        :param total_val: The total_val of this Throughput.
        :type total_val: int
        """
        self._total_val = total_val

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
        if not isinstance(other, Throughput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
