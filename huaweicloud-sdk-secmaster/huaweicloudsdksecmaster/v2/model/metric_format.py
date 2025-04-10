# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MetricFormat:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'data': 'str',
        'display': 'str',
        'display_param': 'dict(str, str)',
        'data_param': 'dict(str, str)'
    }

    attribute_map = {
        'data': 'data',
        'display': 'display',
        'display_param': 'display_param',
        'data_param': 'data_param'
    }

    def __init__(self, data=None, display=None, display_param=None, data_param=None):
        r"""MetricFormat

        The model defined in huaweicloud sdk

        :param data: 数据格式
        :type data: str
        :param display: 显示格式
        :type display: str
        :param display_param: 显示参数
        :type display_param: dict(str, str)
        :param data_param: 数据参数
        :type data_param: dict(str, str)
        """
        
        

        self._data = None
        self._display = None
        self._display_param = None
        self._data_param = None
        self.discriminator = None

        if data is not None:
            self.data = data
        if display is not None:
            self.display = display
        if display_param is not None:
            self.display_param = display_param
        if data_param is not None:
            self.data_param = data_param

    @property
    def data(self):
        r"""Gets the data of this MetricFormat.

        数据格式

        :return: The data of this MetricFormat.
        :rtype: str
        """
        return self._data

    @data.setter
    def data(self, data):
        r"""Sets the data of this MetricFormat.

        数据格式

        :param data: The data of this MetricFormat.
        :type data: str
        """
        self._data = data

    @property
    def display(self):
        r"""Gets the display of this MetricFormat.

        显示格式

        :return: The display of this MetricFormat.
        :rtype: str
        """
        return self._display

    @display.setter
    def display(self, display):
        r"""Sets the display of this MetricFormat.

        显示格式

        :param display: The display of this MetricFormat.
        :type display: str
        """
        self._display = display

    @property
    def display_param(self):
        r"""Gets the display_param of this MetricFormat.

        显示参数

        :return: The display_param of this MetricFormat.
        :rtype: dict(str, str)
        """
        return self._display_param

    @display_param.setter
    def display_param(self, display_param):
        r"""Sets the display_param of this MetricFormat.

        显示参数

        :param display_param: The display_param of this MetricFormat.
        :type display_param: dict(str, str)
        """
        self._display_param = display_param

    @property
    def data_param(self):
        r"""Gets the data_param of this MetricFormat.

        数据参数

        :return: The data_param of this MetricFormat.
        :rtype: dict(str, str)
        """
        return self._data_param

    @data_param.setter
    def data_param(self, data_param):
        r"""Sets the data_param of this MetricFormat.

        数据参数

        :param data_param: The data_param of this MetricFormat.
        :type data_param: dict(str, str)
        """
        self._data_param = data_param

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
        if not isinstance(other, MetricFormat):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
