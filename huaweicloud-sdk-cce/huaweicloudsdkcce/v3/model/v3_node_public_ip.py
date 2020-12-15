# coding: utf-8

import pprint
import re

import six





class V3NodePublicIP:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'count': 'int',
        'eip': 'V3NodeEIPSpec',
        'ids': 'list[str]'
    }

    attribute_map = {
        'count': 'count',
        'eip': 'eip',
        'ids': 'ids'
    }

    def __init__(self, count=None, eip=None, ids=None):
        """V3NodePublicIP - a model defined in huaweicloud sdk"""
        
        

        self._count = None
        self._eip = None
        self._ids = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if eip is not None:
            self.eip = eip
        if ids is not None:
            self.ids = ids

    @property
    def count(self):
        """Gets the count of this V3NodePublicIP.

        要动态创建的弹性IP个数。 > count参数与eip参数必须同时配置。

        :return: The count of this V3NodePublicIP.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this V3NodePublicIP.

        要动态创建的弹性IP个数。 > count参数与eip参数必须同时配置。

        :param count: The count of this V3NodePublicIP.
        :type: int
        """
        self._count = count

    @property
    def eip(self):
        """Gets the eip of this V3NodePublicIP.


        :return: The eip of this V3NodePublicIP.
        :rtype: V3NodeEIPSpec
        """
        return self._eip

    @eip.setter
    def eip(self, eip):
        """Sets the eip of this V3NodePublicIP.


        :param eip: The eip of this V3NodePublicIP.
        :type: V3NodeEIPSpec
        """
        self._eip = eip

    @property
    def ids(self):
        """Gets the ids of this V3NodePublicIP.

        已有的弹性IP的ID列表。数量不得大于待创建节点数 > 若已配置ids参数，则无需配置count和eip参数

        :return: The ids of this V3NodePublicIP.
        :rtype: list[str]
        """
        return self._ids

    @ids.setter
    def ids(self, ids):
        """Sets the ids of this V3NodePublicIP.

        已有的弹性IP的ID列表。数量不得大于待创建节点数 > 若已配置ids参数，则无需配置count和eip参数

        :param ids: The ids of this V3NodePublicIP.
        :type: list[str]
        """
        self._ids = ids

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V3NodePublicIP):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
