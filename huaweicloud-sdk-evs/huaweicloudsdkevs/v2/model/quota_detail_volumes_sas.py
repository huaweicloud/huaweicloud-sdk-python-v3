# coding: utf-8

import pprint
import re

import six





class QuotaDetailVolumesSAS:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'in_use': 'int',
        'limit': 'int',
        'reserved': 'int',
        'allocated': 'str'
    }

    attribute_map = {
        'in_use': 'in_use',
        'limit': 'limit',
        'reserved': 'reserved',
        'allocated': 'allocated'
    }

    def __init__(self, in_use=None, limit=None, reserved=None, allocated=None):
        """QuotaDetailVolumesSAS - a model defined in huaweicloud sdk"""
        
        

        self._in_use = None
        self._limit = None
        self._reserved = None
        self._allocated = None
        self.discriminator = None

        self.in_use = in_use
        self.limit = limit
        self.reserved = reserved
        self.allocated = allocated

    @property
    def in_use(self):
        """Gets the in_use of this QuotaDetailVolumesSAS.

        已使用的数量。

        :return: The in_use of this QuotaDetailVolumesSAS.
        :rtype: int
        """
        return self._in_use

    @in_use.setter
    def in_use(self, in_use):
        """Sets the in_use of this QuotaDetailVolumesSAS.

        已使用的数量。

        :param in_use: The in_use of this QuotaDetailVolumesSAS.
        :type: int
        """
        self._in_use = in_use

    @property
    def limit(self):
        """Gets the limit of this QuotaDetailVolumesSAS.

        最大的数量。

        :return: The limit of this QuotaDetailVolumesSAS.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this QuotaDetailVolumesSAS.

        最大的数量。

        :param limit: The limit of this QuotaDetailVolumesSAS.
        :type: int
        """
        self._limit = limit

    @property
    def reserved(self):
        """Gets the reserved of this QuotaDetailVolumesSAS.

        预留属性。

        :return: The reserved of this QuotaDetailVolumesSAS.
        :rtype: int
        """
        return self._reserved

    @reserved.setter
    def reserved(self, reserved):
        """Sets the reserved of this QuotaDetailVolumesSAS.

        预留属性。

        :param reserved: The reserved of this QuotaDetailVolumesSAS.
        :type: int
        """
        self._reserved = reserved

    @property
    def allocated(self):
        """Gets the allocated of this QuotaDetailVolumesSAS.

        预留属性。

        :return: The allocated of this QuotaDetailVolumesSAS.
        :rtype: str
        """
        return self._allocated

    @allocated.setter
    def allocated(self, allocated):
        """Sets the allocated of this QuotaDetailVolumesSAS.

        预留属性。

        :param allocated: The allocated of this QuotaDetailVolumesSAS.
        :type: str
        """
        self._allocated = allocated

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
        if not isinstance(other, QuotaDetailVolumesSAS):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
