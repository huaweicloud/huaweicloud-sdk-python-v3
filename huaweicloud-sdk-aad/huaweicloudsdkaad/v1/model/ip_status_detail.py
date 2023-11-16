# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IpStatusDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'block_time': 'int',
        'unblock_time': 'int'
    }

    attribute_map = {
        'block_time': 'block_time',
        'unblock_time': 'unblock_time'
    }

    def __init__(self, block_time=None, unblock_time=None):
        """IpStatusDetail

        The model defined in huaweicloud sdk

        :param block_time: 封堵时间
        :type block_time: int
        :param unblock_time: 解封时间
        :type unblock_time: int
        """
        
        

        self._block_time = None
        self._unblock_time = None
        self.discriminator = None

        self.block_time = block_time
        self.unblock_time = unblock_time

    @property
    def block_time(self):
        """Gets the block_time of this IpStatusDetail.

        封堵时间

        :return: The block_time of this IpStatusDetail.
        :rtype: int
        """
        return self._block_time

    @block_time.setter
    def block_time(self, block_time):
        """Sets the block_time of this IpStatusDetail.

        封堵时间

        :param block_time: The block_time of this IpStatusDetail.
        :type block_time: int
        """
        self._block_time = block_time

    @property
    def unblock_time(self):
        """Gets the unblock_time of this IpStatusDetail.

        解封时间

        :return: The unblock_time of this IpStatusDetail.
        :rtype: int
        """
        return self._unblock_time

    @unblock_time.setter
    def unblock_time(self, unblock_time):
        """Sets the unblock_time of this IpStatusDetail.

        解封时间

        :param unblock_time: The unblock_time of this IpStatusDetail.
        :type unblock_time: int
        """
        self._unblock_time = unblock_time

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
        if not isinstance(other, IpStatusDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
