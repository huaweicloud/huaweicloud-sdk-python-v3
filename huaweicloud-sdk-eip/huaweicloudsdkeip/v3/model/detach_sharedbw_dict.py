# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DetachSharedbwDict:

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
        'size': 'int',
        'charge_mode': 'str'
    }

    attribute_map = {
        'name': 'name',
        'size': 'size',
        'charge_mode': 'charge_mode'
    }

    def __init__(self, name=None, size=None, charge_mode=None):
        r"""DetachSharedbwDict

        The model defined in huaweicloud sdk

        :param name: - 功能说明：带宽名称
        :type name: str
        :param size: - 功能说明：带宽大小
        :type size: int
        :param charge_mode: - 功能说明：带宽计费模式
        :type charge_mode: str
        """
        
        

        self._name = None
        self._size = None
        self._charge_mode = None
        self.discriminator = None

        if name is not None:
            self.name = name
        self.size = size
        self.charge_mode = charge_mode

    @property
    def name(self):
        r"""Gets the name of this DetachSharedbwDict.

        - 功能说明：带宽名称

        :return: The name of this DetachSharedbwDict.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this DetachSharedbwDict.

        - 功能说明：带宽名称

        :param name: The name of this DetachSharedbwDict.
        :type name: str
        """
        self._name = name

    @property
    def size(self):
        r"""Gets the size of this DetachSharedbwDict.

        - 功能说明：带宽大小

        :return: The size of this DetachSharedbwDict.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this DetachSharedbwDict.

        - 功能说明：带宽大小

        :param size: The size of this DetachSharedbwDict.
        :type size: int
        """
        self._size = size

    @property
    def charge_mode(self):
        r"""Gets the charge_mode of this DetachSharedbwDict.

        - 功能说明：带宽计费模式

        :return: The charge_mode of this DetachSharedbwDict.
        :rtype: str
        """
        return self._charge_mode

    @charge_mode.setter
    def charge_mode(self, charge_mode):
        r"""Sets the charge_mode of this DetachSharedbwDict.

        - 功能说明：带宽计费模式

        :param charge_mode: The charge_mode of this DetachSharedbwDict.
        :type charge_mode: str
        """
        self._charge_mode = charge_mode

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
        if not isinstance(other, DetachSharedbwDict):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
