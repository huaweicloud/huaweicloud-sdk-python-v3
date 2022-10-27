# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CriteriaSnake:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'filter_type': 'int',
        'value': 'str'
    }

    attribute_map = {
        'filter_type': 'filter_type',
        'value': 'value'
    }

    def __init__(self, filter_type=None, value=None):
        """CriteriaSnake

        The model defined in huaweicloud sdk

        :param filter_type: 过滤类型 - 1 按插件Tag过滤 - 2 按diplayName过滤 - 3 按publisherId过滤 - 4 按插件Id过滤 - 5 按插件分类过滤 - 7 按照作者名.插件名过滤 - 8 按Target（客户端）过滤 - 10 按关键字（客户端输入的）过滤 - 12 根据flags传入的值来进行过滤,eg:flags&#x3D;2name就排除flags&#x3D;2的插件. - 13 根据flags传入的值来进行过滤,eg:flags&#x3D;2name就查询出flags&#x3D;2的插件 - 18 按publisherName过滤 - 19 按publisherDisplayName过滤 - 102 按照插件状态排除插件 - 103 按照插件状态过滤出插件 - 107 supportIdeInfo - 108 根据插件ids查询
        :type filter_type: int
        :param value: 过滤类型对应字段名称
        :type value: str
        """
        
        

        self._filter_type = None
        self._value = None
        self.discriminator = None

        if filter_type is not None:
            self.filter_type = filter_type
        if value is not None:
            self.value = value

    @property
    def filter_type(self):
        """Gets the filter_type of this CriteriaSnake.

        过滤类型 - 1 按插件Tag过滤 - 2 按diplayName过滤 - 3 按publisherId过滤 - 4 按插件Id过滤 - 5 按插件分类过滤 - 7 按照作者名.插件名过滤 - 8 按Target（客户端）过滤 - 10 按关键字（客户端输入的）过滤 - 12 根据flags传入的值来进行过滤,eg:flags=2name就排除flags=2的插件. - 13 根据flags传入的值来进行过滤,eg:flags=2name就查询出flags=2的插件 - 18 按publisherName过滤 - 19 按publisherDisplayName过滤 - 102 按照插件状态排除插件 - 103 按照插件状态过滤出插件 - 107 supportIdeInfo - 108 根据插件ids查询

        :return: The filter_type of this CriteriaSnake.
        :rtype: int
        """
        return self._filter_type

    @filter_type.setter
    def filter_type(self, filter_type):
        """Sets the filter_type of this CriteriaSnake.

        过滤类型 - 1 按插件Tag过滤 - 2 按diplayName过滤 - 3 按publisherId过滤 - 4 按插件Id过滤 - 5 按插件分类过滤 - 7 按照作者名.插件名过滤 - 8 按Target（客户端）过滤 - 10 按关键字（客户端输入的）过滤 - 12 根据flags传入的值来进行过滤,eg:flags=2name就排除flags=2的插件. - 13 根据flags传入的值来进行过滤,eg:flags=2name就查询出flags=2的插件 - 18 按publisherName过滤 - 19 按publisherDisplayName过滤 - 102 按照插件状态排除插件 - 103 按照插件状态过滤出插件 - 107 supportIdeInfo - 108 根据插件ids查询

        :param filter_type: The filter_type of this CriteriaSnake.
        :type filter_type: int
        """
        self._filter_type = filter_type

    @property
    def value(self):
        """Gets the value of this CriteriaSnake.

        过滤类型对应字段名称

        :return: The value of this CriteriaSnake.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this CriteriaSnake.

        过滤类型对应字段名称

        :param value: The value of this CriteriaSnake.
        :type value: str
        """
        self._value = value

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
        if not isinstance(other, CriteriaSnake):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
