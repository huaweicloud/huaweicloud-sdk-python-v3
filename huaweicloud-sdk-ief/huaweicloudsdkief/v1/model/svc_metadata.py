# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SvcMetadata:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'labels': 'dict(str, str)',
        'name': 'str'
    }

    attribute_map = {
        'labels': 'labels',
        'name': 'name'
    }

    def __init__(self, labels=None, name=None):
        """SvcMetadata

        The model defined in huaweicloud sdk

        :param labels: 自定义标签属性列表
        :type labels: dict(str, str)
        :param name: 服务名称，只允许英文小写字母、数字、中划线，最大长度64，英文小写字母开头，数字或小写字母结尾
        :type name: str
        """
        
        

        self._labels = None
        self._name = None
        self.discriminator = None

        if labels is not None:
            self.labels = labels
        self.name = name

    @property
    def labels(self):
        """Gets the labels of this SvcMetadata.

        自定义标签属性列表

        :return: The labels of this SvcMetadata.
        :rtype: dict(str, str)
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this SvcMetadata.

        自定义标签属性列表

        :param labels: The labels of this SvcMetadata.
        :type labels: dict(str, str)
        """
        self._labels = labels

    @property
    def name(self):
        """Gets the name of this SvcMetadata.

        服务名称，只允许英文小写字母、数字、中划线，最大长度64，英文小写字母开头，数字或小写字母结尾

        :return: The name of this SvcMetadata.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SvcMetadata.

        服务名称，只允许英文小写字母、数字、中划线，最大长度64，英文小写字母开头，数字或小写字母结尾

        :param name: The name of this SvcMetadata.
        :type name: str
        """
        self._name = name

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
        if not isinstance(other, SvcMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
