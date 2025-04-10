# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TbPosInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'origin_name': 'str',
        'name': 'str',
        'start': 'int',
        'end': 'int'
    }

    attribute_map = {
        'origin_name': 'origin_name',
        'name': 'name',
        'start': 'start',
        'end': 'end'
    }

    def __init__(self, origin_name=None, name=None, start=None, end=None):
        r"""TbPosInfo

        The model defined in huaweicloud sdk

        :param origin_name: 原始名称
        :type origin_name: str
        :param name: 名称
        :type name: str
        :param start: 开始
        :type start: int
        :param end: 结束
        :type end: int
        """
        
        

        self._origin_name = None
        self._name = None
        self._start = None
        self._end = None
        self.discriminator = None

        if origin_name is not None:
            self.origin_name = origin_name
        if name is not None:
            self.name = name
        if start is not None:
            self.start = start
        if end is not None:
            self.end = end

    @property
    def origin_name(self):
        r"""Gets the origin_name of this TbPosInfo.

        原始名称

        :return: The origin_name of this TbPosInfo.
        :rtype: str
        """
        return self._origin_name

    @origin_name.setter
    def origin_name(self, origin_name):
        r"""Sets the origin_name of this TbPosInfo.

        原始名称

        :param origin_name: The origin_name of this TbPosInfo.
        :type origin_name: str
        """
        self._origin_name = origin_name

    @property
    def name(self):
        r"""Gets the name of this TbPosInfo.

        名称

        :return: The name of this TbPosInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this TbPosInfo.

        名称

        :param name: The name of this TbPosInfo.
        :type name: str
        """
        self._name = name

    @property
    def start(self):
        r"""Gets the start of this TbPosInfo.

        开始

        :return: The start of this TbPosInfo.
        :rtype: int
        """
        return self._start

    @start.setter
    def start(self, start):
        r"""Sets the start of this TbPosInfo.

        开始

        :param start: The start of this TbPosInfo.
        :type start: int
        """
        self._start = start

    @property
    def end(self):
        r"""Gets the end of this TbPosInfo.

        结束

        :return: The end of this TbPosInfo.
        :rtype: int
        """
        return self._end

    @end.setter
    def end(self, end):
        r"""Sets the end of this TbPosInfo.

        结束

        :param end: The end of this TbPosInfo.
        :type end: int
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
        if not isinstance(other, TbPosInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
