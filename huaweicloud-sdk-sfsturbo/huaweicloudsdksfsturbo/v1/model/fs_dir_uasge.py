# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FsDirUasge:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'used_capacity': 'int'
    }

    attribute_map = {
        'used_capacity': 'used_capacity'
    }

    def __init__(self, used_capacity=None):
        r"""FsDirUasge

        The model defined in huaweicloud sdk

        :param used_capacity: 占用容量，单位：byte
        :type used_capacity: int
        """
        
        

        self._used_capacity = None
        self.discriminator = None

        self.used_capacity = used_capacity

    @property
    def used_capacity(self):
        r"""Gets the used_capacity of this FsDirUasge.

        占用容量，单位：byte

        :return: The used_capacity of this FsDirUasge.
        :rtype: int
        """
        return self._used_capacity

    @used_capacity.setter
    def used_capacity(self, used_capacity):
        r"""Sets the used_capacity of this FsDirUasge.

        占用容量，单位：byte

        :param used_capacity: The used_capacity of this FsDirUasge.
        :type used_capacity: int
        """
        self._used_capacity = used_capacity

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
        if not isinstance(other, FsDirUasge):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
