# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LabelSite:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'index': 'list[int]',
        'name': 'list[str]',
        'coordinate': 'list[list[float]]'
    }

    attribute_map = {
        'index': 'index',
        'name': 'name',
        'coordinate': 'coordinate'
    }

    def __init__(self, index=None, name=None, coordinate=None):
        r"""LabelSite

        The model defined in huaweicloud sdk

        :param index: 索引
        :type index: list[int]
        :param name: 标记位点名称
        :type name: list[str]
        :param coordinate: 位点三维坐标集
        :type coordinate: list[list[float]]
        """
        
        

        self._index = None
        self._name = None
        self._coordinate = None
        self.discriminator = None

        if index is not None:
            self.index = index
        if name is not None:
            self.name = name
        if coordinate is not None:
            self.coordinate = coordinate

    @property
    def index(self):
        r"""Gets the index of this LabelSite.

        索引

        :return: The index of this LabelSite.
        :rtype: list[int]
        """
        return self._index

    @index.setter
    def index(self, index):
        r"""Sets the index of this LabelSite.

        索引

        :param index: The index of this LabelSite.
        :type index: list[int]
        """
        self._index = index

    @property
    def name(self):
        r"""Gets the name of this LabelSite.

        标记位点名称

        :return: The name of this LabelSite.
        :rtype: list[str]
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this LabelSite.

        标记位点名称

        :param name: The name of this LabelSite.
        :type name: list[str]
        """
        self._name = name

    @property
    def coordinate(self):
        r"""Gets the coordinate of this LabelSite.

        位点三维坐标集

        :return: The coordinate of this LabelSite.
        :rtype: list[list[float]]
        """
        return self._coordinate

    @coordinate.setter
    def coordinate(self, coordinate):
        r"""Sets the coordinate of this LabelSite.

        位点三维坐标集

        :param coordinate: The coordinate of this LabelSite.
        :type coordinate: list[list[float]]
        """
        self._coordinate = coordinate

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
        if not isinstance(other, LabelSite):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
