# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListLogContextRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'line_num': 'str',
        'time__': 'str',
        'backwards_size': 'int',
        'forwards_size': 'int'
    }

    attribute_map = {
        'line_num': 'line_num',
        'time__': '__time__',
        'backwards_size': 'backwardsSize',
        'forwards_size': 'forwardsSize'
    }

    def __init__(self, line_num=None, time__=None, backwards_size=None, forwards_size=None):
        r"""ListLogContextRequestBody

        The model defined in huaweicloud sdk

        :param line_num: 日志单行序列号，字段值需要从日志结果中获取，纳秒级时间戳。
        :type line_num: str
        :param time__: 自定义时间特性时间字段，字段值需要从日志结果中获取，毫秒级时间戳。若已开启云端结构化自定义时间功能，需要使用该字段和line_num字段共同进行上下文查询。
        :type time__: str
        :param backwards_size: 指定起始日志往前（上文）的日志条数，取值范围 [0, 500] ，默认值100
        :type backwards_size: int
        :param forwards_size: 指定起始日志往后（下文）的日志条数，取值范围 [0, 500] ，默认值100
        :type forwards_size: int
        """
        
        

        self._line_num = None
        self._time__ = None
        self._backwards_size = None
        self._forwards_size = None
        self.discriminator = None

        if line_num is not None:
            self.line_num = line_num
        if time__ is not None:
            self.time__ = time__
        if backwards_size is not None:
            self.backwards_size = backwards_size
        if forwards_size is not None:
            self.forwards_size = forwards_size

    @property
    def line_num(self):
        r"""Gets the line_num of this ListLogContextRequestBody.

        日志单行序列号，字段值需要从日志结果中获取，纳秒级时间戳。

        :return: The line_num of this ListLogContextRequestBody.
        :rtype: str
        """
        return self._line_num

    @line_num.setter
    def line_num(self, line_num):
        r"""Sets the line_num of this ListLogContextRequestBody.

        日志单行序列号，字段值需要从日志结果中获取，纳秒级时间戳。

        :param line_num: The line_num of this ListLogContextRequestBody.
        :type line_num: str
        """
        self._line_num = line_num

    @property
    def time__(self):
        r"""Gets the time__ of this ListLogContextRequestBody.

        自定义时间特性时间字段，字段值需要从日志结果中获取，毫秒级时间戳。若已开启云端结构化自定义时间功能，需要使用该字段和line_num字段共同进行上下文查询。

        :return: The time__ of this ListLogContextRequestBody.
        :rtype: str
        """
        return self._time__

    @time__.setter
    def time__(self, time__):
        r"""Sets the time__ of this ListLogContextRequestBody.

        自定义时间特性时间字段，字段值需要从日志结果中获取，毫秒级时间戳。若已开启云端结构化自定义时间功能，需要使用该字段和line_num字段共同进行上下文查询。

        :param time__: The time__ of this ListLogContextRequestBody.
        :type time__: str
        """
        self._time__ = time__

    @property
    def backwards_size(self):
        r"""Gets the backwards_size of this ListLogContextRequestBody.

        指定起始日志往前（上文）的日志条数，取值范围 [0, 500] ，默认值100

        :return: The backwards_size of this ListLogContextRequestBody.
        :rtype: int
        """
        return self._backwards_size

    @backwards_size.setter
    def backwards_size(self, backwards_size):
        r"""Sets the backwards_size of this ListLogContextRequestBody.

        指定起始日志往前（上文）的日志条数，取值范围 [0, 500] ，默认值100

        :param backwards_size: The backwards_size of this ListLogContextRequestBody.
        :type backwards_size: int
        """
        self._backwards_size = backwards_size

    @property
    def forwards_size(self):
        r"""Gets the forwards_size of this ListLogContextRequestBody.

        指定起始日志往后（下文）的日志条数，取值范围 [0, 500] ，默认值100

        :return: The forwards_size of this ListLogContextRequestBody.
        :rtype: int
        """
        return self._forwards_size

    @forwards_size.setter
    def forwards_size(self, forwards_size):
        r"""Sets the forwards_size of this ListLogContextRequestBody.

        指定起始日志往后（下文）的日志条数，取值范围 [0, 500] ，默认值100

        :param forwards_size: The forwards_size of this ListLogContextRequestBody.
        :type forwards_size: int
        """
        self._forwards_size = forwards_size

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
        if not isinstance(other, ListLogContextRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
