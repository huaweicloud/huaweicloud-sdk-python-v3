# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


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
        'seq': 'int',
        'default': 'bool',
        'begin': 'str',
        'end': 'str'
    }

    attribute_map = {
        'seq': 'seq',
        'default': 'default',
        'begin': 'begin',
        'end': 'end'
    }

    def __init__(self, seq=None, default=None, begin=None, end=None):
        r"""MaintainWindowsEntity

        The model defined in huaweicloud sdk

        :param seq: 序号。
        :type seq: int
        :param default: 是否为默认时间段。
        :type default: bool
        :param begin: 维护时间窗开始时间
        :type begin: str
        :param end: 维护时间窗结束时间。
        :type end: str
        """
        
        

        self._seq = None
        self._default = None
        self._begin = None
        self._end = None
        self.discriminator = None

        if seq is not None:
            self.seq = seq
        if default is not None:
            self.default = default
        if begin is not None:
            self.begin = begin
        if end is not None:
            self.end = end

    @property
    def seq(self):
        r"""Gets the seq of this MaintainWindowsEntity.

        序号。

        :return: The seq of this MaintainWindowsEntity.
        :rtype: int
        """
        return self._seq

    @seq.setter
    def seq(self, seq):
        r"""Sets the seq of this MaintainWindowsEntity.

        序号。

        :param seq: The seq of this MaintainWindowsEntity.
        :type seq: int
        """
        self._seq = seq

    @property
    def default(self):
        r"""Gets the default of this MaintainWindowsEntity.

        是否为默认时间段。

        :return: The default of this MaintainWindowsEntity.
        :rtype: bool
        """
        return self._default

    @default.setter
    def default(self, default):
        r"""Sets the default of this MaintainWindowsEntity.

        是否为默认时间段。

        :param default: The default of this MaintainWindowsEntity.
        :type default: bool
        """
        self._default = default

    @property
    def begin(self):
        r"""Gets the begin of this MaintainWindowsEntity.

        维护时间窗开始时间

        :return: The begin of this MaintainWindowsEntity.
        :rtype: str
        """
        return self._begin

    @begin.setter
    def begin(self, begin):
        r"""Sets the begin of this MaintainWindowsEntity.

        维护时间窗开始时间

        :param begin: The begin of this MaintainWindowsEntity.
        :type begin: str
        """
        self._begin = begin

    @property
    def end(self):
        r"""Gets the end of this MaintainWindowsEntity.

        维护时间窗结束时间。

        :return: The end of this MaintainWindowsEntity.
        :rtype: str
        """
        return self._end

    @end.setter
    def end(self, end):
        r"""Sets the end of this MaintainWindowsEntity.

        维护时间窗结束时间。

        :param end: The end of this MaintainWindowsEntity.
        :type end: str
        """
        self._end = end

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
        if not isinstance(other, MaintainWindowsEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
