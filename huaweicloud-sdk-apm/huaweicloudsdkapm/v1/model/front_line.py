# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FrontLine:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'point_list': 'list[FrontPoint]',
        'title': 'str',
        'unit': 'str',
        'precision': 'int',
        'data_type': 'str',
        'visible': 'bool'
    }

    attribute_map = {
        'point_list': 'point_list',
        'title': 'title',
        'unit': 'unit',
        'precision': 'precision',
        'data_type': 'data_type',
        'visible': 'visible'
    }

    def __init__(self, point_list=None, title=None, unit=None, precision=None, data_type=None, visible=None):
        """FrontLine

        The model defined in huaweicloud sdk

        :param point_list: 数据点集合。
        :type point_list: list[:class:`huaweicloudsdkapm.v1.FrontPoint`]
        :param title: 标题。
        :type title: str
        :param unit: 单位。
        :type unit: str
        :param precision: 百分比。
        :type precision: int
        :param data_type: 日期类型。
        :type data_type: str
        :param visible: 是否可见。
        :type visible: bool
        """
        
        

        self._point_list = None
        self._title = None
        self._unit = None
        self._precision = None
        self._data_type = None
        self._visible = None
        self.discriminator = None

        if point_list is not None:
            self.point_list = point_list
        if title is not None:
            self.title = title
        if unit is not None:
            self.unit = unit
        if precision is not None:
            self.precision = precision
        if data_type is not None:
            self.data_type = data_type
        if visible is not None:
            self.visible = visible

    @property
    def point_list(self):
        """Gets the point_list of this FrontLine.

        数据点集合。

        :return: The point_list of this FrontLine.
        :rtype: list[:class:`huaweicloudsdkapm.v1.FrontPoint`]
        """
        return self._point_list

    @point_list.setter
    def point_list(self, point_list):
        """Sets the point_list of this FrontLine.

        数据点集合。

        :param point_list: The point_list of this FrontLine.
        :type point_list: list[:class:`huaweicloudsdkapm.v1.FrontPoint`]
        """
        self._point_list = point_list

    @property
    def title(self):
        """Gets the title of this FrontLine.

        标题。

        :return: The title of this FrontLine.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this FrontLine.

        标题。

        :param title: The title of this FrontLine.
        :type title: str
        """
        self._title = title

    @property
    def unit(self):
        """Gets the unit of this FrontLine.

        单位。

        :return: The unit of this FrontLine.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this FrontLine.

        单位。

        :param unit: The unit of this FrontLine.
        :type unit: str
        """
        self._unit = unit

    @property
    def precision(self):
        """Gets the precision of this FrontLine.

        百分比。

        :return: The precision of this FrontLine.
        :rtype: int
        """
        return self._precision

    @precision.setter
    def precision(self, precision):
        """Sets the precision of this FrontLine.

        百分比。

        :param precision: The precision of this FrontLine.
        :type precision: int
        """
        self._precision = precision

    @property
    def data_type(self):
        """Gets the data_type of this FrontLine.

        日期类型。

        :return: The data_type of this FrontLine.
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """Sets the data_type of this FrontLine.

        日期类型。

        :param data_type: The data_type of this FrontLine.
        :type data_type: str
        """
        self._data_type = data_type

    @property
    def visible(self):
        """Gets the visible of this FrontLine.

        是否可见。

        :return: The visible of this FrontLine.
        :rtype: bool
        """
        return self._visible

    @visible.setter
    def visible(self, visible):
        """Sets the visible of this FrontLine.

        是否可见。

        :param visible: The visible of this FrontLine.
        :type visible: bool
        """
        self._visible = visible

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
        if not isinstance(other, FrontLine):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
