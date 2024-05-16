# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowFlameLineTreeResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'data': 'list[str]',
        'methods': 'list[str]'
    }

    attribute_map = {
        'data': 'data',
        'methods': 'methods'
    }

    def __init__(self, data=None, methods=None):
        """ShowFlameLineTreeResponse

        The model defined in huaweicloud sdk

        :param data: 火焰图的数据，是个二维数组 data[0][0]: self time，方法自己消耗的cpu毫秒时间，不包括方法内部调用其他方法的时间 data[0][1]: total time, 方法消耗的cpu毫秒时间，包括方法内部调用其他方法的时间 data[0][2]: 方法的index,对应methods中的数组下标 data[0][3]: 行号 data[0][4]: 方法的子节点，就是方法中调用的其他方法
        :type data: list[str]
        :param methods: 调用栈上的方法信息，是个二维数组 method[0][0]: 方法的唯一id method[0][1]: 方法的package包名 method[0][2]: 方法的class name 类名 method[0][3]: 方法名 method[0][4]: 方法的参数列表 method[0][5]: 方法是否为用户的方法 method[0][6]: 方法是否为native方法
        :type methods: list[str]
        """
        
        super(ShowFlameLineTreeResponse, self).__init__()

        self._data = None
        self._methods = None
        self.discriminator = None

        if data is not None:
            self.data = data
        if methods is not None:
            self.methods = methods

    @property
    def data(self):
        """Gets the data of this ShowFlameLineTreeResponse.

        火焰图的数据，是个二维数组 data[0][0]: self time，方法自己消耗的cpu毫秒时间，不包括方法内部调用其他方法的时间 data[0][1]: total time, 方法消耗的cpu毫秒时间，包括方法内部调用其他方法的时间 data[0][2]: 方法的index,对应methods中的数组下标 data[0][3]: 行号 data[0][4]: 方法的子节点，就是方法中调用的其他方法

        :return: The data of this ShowFlameLineTreeResponse.
        :rtype: list[str]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this ShowFlameLineTreeResponse.

        火焰图的数据，是个二维数组 data[0][0]: self time，方法自己消耗的cpu毫秒时间，不包括方法内部调用其他方法的时间 data[0][1]: total time, 方法消耗的cpu毫秒时间，包括方法内部调用其他方法的时间 data[0][2]: 方法的index,对应methods中的数组下标 data[0][3]: 行号 data[0][4]: 方法的子节点，就是方法中调用的其他方法

        :param data: The data of this ShowFlameLineTreeResponse.
        :type data: list[str]
        """
        self._data = data

    @property
    def methods(self):
        """Gets the methods of this ShowFlameLineTreeResponse.

        调用栈上的方法信息，是个二维数组 method[0][0]: 方法的唯一id method[0][1]: 方法的package包名 method[0][2]: 方法的class name 类名 method[0][3]: 方法名 method[0][4]: 方法的参数列表 method[0][5]: 方法是否为用户的方法 method[0][6]: 方法是否为native方法

        :return: The methods of this ShowFlameLineTreeResponse.
        :rtype: list[str]
        """
        return self._methods

    @methods.setter
    def methods(self, methods):
        """Sets the methods of this ShowFlameLineTreeResponse.

        调用栈上的方法信息，是个二维数组 method[0][0]: 方法的唯一id method[0][1]: 方法的package包名 method[0][2]: 方法的class name 类名 method[0][3]: 方法名 method[0][4]: 方法的参数列表 method[0][5]: 方法是否为用户的方法 method[0][6]: 方法是否为native方法

        :param methods: The methods of this ShowFlameLineTreeResponse.
        :type methods: list[str]
        """
        self._methods = methods

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
        if not isinstance(other, ShowFlameLineTreeResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
