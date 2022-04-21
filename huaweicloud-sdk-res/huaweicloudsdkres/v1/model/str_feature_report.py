# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StrFeatureReport:

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
        'data_type': 'str',
        'str_count': 'dict(str, int)'
    }

    attribute_map = {
        'name': 'name',
        'data_type': 'data_type',
        'str_count': 'str_count'
    }

    def __init__(self, name=None, data_type=None, str_count=None):
        """StrFeatureReport

        The model defined in huaweicloud sdk

        :param name: 特征名。
        :type name: str
        :param data_type: 特征类型。
        :type data_type: str
        :param str_count: 离散类型特征出现次数统计。
        :type str_count: dict(str, int)
        """
        
        

        self._name = None
        self._data_type = None
        self._str_count = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if data_type is not None:
            self.data_type = data_type
        if str_count is not None:
            self.str_count = str_count

    @property
    def name(self):
        """Gets the name of this StrFeatureReport.

        特征名。

        :return: The name of this StrFeatureReport.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this StrFeatureReport.

        特征名。

        :param name: The name of this StrFeatureReport.
        :type name: str
        """
        self._name = name

    @property
    def data_type(self):
        """Gets the data_type of this StrFeatureReport.

        特征类型。

        :return: The data_type of this StrFeatureReport.
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """Sets the data_type of this StrFeatureReport.

        特征类型。

        :param data_type: The data_type of this StrFeatureReport.
        :type data_type: str
        """
        self._data_type = data_type

    @property
    def str_count(self):
        """Gets the str_count of this StrFeatureReport.

        离散类型特征出现次数统计。

        :return: The str_count of this StrFeatureReport.
        :rtype: dict(str, int)
        """
        return self._str_count

    @str_count.setter
    def str_count(self, str_count):
        """Sets the str_count of this StrFeatureReport.

        离散类型特征出现次数统计。

        :param str_count: The str_count of this StrFeatureReport.
        :type str_count: dict(str, int)
        """
        self._str_count = str_count

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
        if not isinstance(other, StrFeatureReport):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
