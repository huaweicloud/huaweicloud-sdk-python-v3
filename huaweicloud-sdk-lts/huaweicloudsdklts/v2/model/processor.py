# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Processor:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'detail': 'Detail'
    }

    attribute_map = {
        'type': 'type',
        'detail': 'detail'
    }

    def __init__(self, type=None, detail=None):
        r"""Processor

        The model defined in huaweicloud sdk

        :param type: 解析器类型 processor_regex 正则解析 processor_split_string 分词符 processor_json json解析器类型 processor_gotime自定义时间类型 processor_filter_regex日志过滤 processor_drop删除字段类型 processor_rename修改字段类型
        :type type: str
        :param detail: 
        :type detail: :class:`huaweicloudsdklts.v2.Detail`
        """
        
        

        self._type = None
        self._detail = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if detail is not None:
            self.detail = detail

    @property
    def type(self):
        r"""Gets the type of this Processor.

        解析器类型 processor_regex 正则解析 processor_split_string 分词符 processor_json json解析器类型 processor_gotime自定义时间类型 processor_filter_regex日志过滤 processor_drop删除字段类型 processor_rename修改字段类型

        :return: The type of this Processor.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this Processor.

        解析器类型 processor_regex 正则解析 processor_split_string 分词符 processor_json json解析器类型 processor_gotime自定义时间类型 processor_filter_regex日志过滤 processor_drop删除字段类型 processor_rename修改字段类型

        :param type: The type of this Processor.
        :type type: str
        """
        self._type = type

    @property
    def detail(self):
        r"""Gets the detail of this Processor.

        :return: The detail of this Processor.
        :rtype: :class:`huaweicloudsdklts.v2.Detail`
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        r"""Sets the detail of this Processor.

        :param detail: The detail of this Processor.
        :type detail: :class:`huaweicloudsdklts.v2.Detail`
        """
        self._detail = detail

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
        if not isinstance(other, Processor):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
