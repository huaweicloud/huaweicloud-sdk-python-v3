# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DimensionInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'filter_type': 'str',
        'values': 'list[str]'
    }

    attribute_map = {
        'name': 'name',
        'filter_type': 'filter_type',
        'values': 'values'
    }

    def __init__(self, name=None, filter_type=None, values=None):
        r"""DimensionInfo

        The model defined in huaweicloud sdk

        :param name: 维度名称，多维度用逗号分隔，各服务支持的维度可参考：“[服务维度名称](ces_03_0059.xml)”
        :type name: str
        :param filter_type: 资源类型, all_instances: 全部资源, specific_instances: 指定资源
        :type filter_type: str
        :param values: 维度值列表
        :type values: list[str]
        """
        
        

        self._name = None
        self._filter_type = None
        self._values = None
        self.discriminator = None

        self.name = name
        self.filter_type = filter_type
        if values is not None:
            self.values = values

    @property
    def name(self):
        r"""Gets the name of this DimensionInfo.

        维度名称，多维度用逗号分隔，各服务支持的维度可参考：“[服务维度名称](ces_03_0059.xml)”

        :return: The name of this DimensionInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this DimensionInfo.

        维度名称，多维度用逗号分隔，各服务支持的维度可参考：“[服务维度名称](ces_03_0059.xml)”

        :param name: The name of this DimensionInfo.
        :type name: str
        """
        self._name = name

    @property
    def filter_type(self):
        r"""Gets the filter_type of this DimensionInfo.

        资源类型, all_instances: 全部资源, specific_instances: 指定资源

        :return: The filter_type of this DimensionInfo.
        :rtype: str
        """
        return self._filter_type

    @filter_type.setter
    def filter_type(self, filter_type):
        r"""Sets the filter_type of this DimensionInfo.

        资源类型, all_instances: 全部资源, specific_instances: 指定资源

        :param filter_type: The filter_type of this DimensionInfo.
        :type filter_type: str
        """
        self._filter_type = filter_type

    @property
    def values(self):
        r"""Gets the values of this DimensionInfo.

        维度值列表

        :return: The values of this DimensionInfo.
        :rtype: list[str]
        """
        return self._values

    @values.setter
    def values(self, values):
        r"""Sets the values of this DimensionInfo.

        维度值列表

        :param values: The values of this DimensionInfo.
        :type values: list[str]
        """
        self._values = values

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
        if not isinstance(other, DimensionInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
