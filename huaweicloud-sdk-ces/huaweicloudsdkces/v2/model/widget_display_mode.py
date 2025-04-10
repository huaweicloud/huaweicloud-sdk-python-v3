# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WidgetDisplayMode:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'row_widget_num': 'int'
    }

    attribute_map = {
        'row_widget_num': 'row_widget_num'
    }

    def __init__(self, row_widget_num=None):
        r"""WidgetDisplayMode

        The model defined in huaweicloud sdk

        :param row_widget_num: 监控视图展示模式，0表示自定义坐标，1代表每行一个
        :type row_widget_num: int
        """
        
        

        self._row_widget_num = None
        self.discriminator = None

        if row_widget_num is not None:
            self.row_widget_num = row_widget_num

    @property
    def row_widget_num(self):
        r"""Gets the row_widget_num of this WidgetDisplayMode.

        监控视图展示模式，0表示自定义坐标，1代表每行一个

        :return: The row_widget_num of this WidgetDisplayMode.
        :rtype: int
        """
        return self._row_widget_num

    @row_widget_num.setter
    def row_widget_num(self, row_widget_num):
        r"""Sets the row_widget_num of this WidgetDisplayMode.

        监控视图展示模式，0表示自定义坐标，1代表每行一个

        :param row_widget_num: The row_widget_num of this WidgetDisplayMode.
        :type row_widget_num: int
        """
        self._row_widget_num = row_widget_num

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
        if not isinstance(other, WidgetDisplayMode):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
