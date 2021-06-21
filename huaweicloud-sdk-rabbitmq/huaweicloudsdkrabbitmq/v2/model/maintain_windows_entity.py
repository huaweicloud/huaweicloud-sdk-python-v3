# coding: utf-8

import pprint
import re

import six





class MaintainWindowsEntity:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'default': 'bool',
        'end': 'str',
        'begin': 'str',
        'seq': 'int'
    }

    attribute_map = {
        'default': 'default',
        'end': 'end',
        'begin': 'begin',
        'seq': 'seq'
    }

    def __init__(self, default=None, end=None, begin=None, seq=None):
        """MaintainWindowsEntity - a model defined in huaweicloud sdk"""
        
        

        self._default = None
        self._end = None
        self._begin = None
        self._seq = None
        self.discriminator = None

        if default is not None:
            self.default = default
        if end is not None:
            self.end = end
        if begin is not None:
            self.begin = begin
        if seq is not None:
            self.seq = seq

    @property
    def default(self):
        """Gets the default of this MaintainWindowsEntity.

        是否为默认时间段。

        :return: The default of this MaintainWindowsEntity.
        :rtype: bool
        """
        return self._default

    @default.setter
    def default(self, default):
        """Sets the default of this MaintainWindowsEntity.

        是否为默认时间段。

        :param default: The default of this MaintainWindowsEntity.
        :type: bool
        """
        self._default = default

    @property
    def end(self):
        """Gets the end of this MaintainWindowsEntity.

        维护时间窗结束时间。

        :return: The end of this MaintainWindowsEntity.
        :rtype: str
        """
        return self._end

    @end.setter
    def end(self, end):
        """Sets the end of this MaintainWindowsEntity.

        维护时间窗结束时间。

        :param end: The end of this MaintainWindowsEntity.
        :type: str
        """
        self._end = end

    @property
    def begin(self):
        """Gets the begin of this MaintainWindowsEntity.

        维护时间窗开始时间。

        :return: The begin of this MaintainWindowsEntity.
        :rtype: str
        """
        return self._begin

    @begin.setter
    def begin(self, begin):
        """Sets the begin of this MaintainWindowsEntity.

        维护时间窗开始时间。

        :param begin: The begin of this MaintainWindowsEntity.
        :type: str
        """
        self._begin = begin

    @property
    def seq(self):
        """Gets the seq of this MaintainWindowsEntity.

        序号。

        :return: The seq of this MaintainWindowsEntity.
        :rtype: int
        """
        return self._seq

    @seq.setter
    def seq(self, seq):
        """Sets the seq of this MaintainWindowsEntity.

        序号。

        :param seq: The seq of this MaintainWindowsEntity.
        :type: int
        """
        self._seq = seq

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
        if not isinstance(other, MaintainWindowsEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
