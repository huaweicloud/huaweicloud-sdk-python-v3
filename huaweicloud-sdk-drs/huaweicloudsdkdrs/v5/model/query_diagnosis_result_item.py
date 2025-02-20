# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueryDiagnosisResultItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'category': 'str',
        'name': 'str',
        'weight': 'float'
    }

    attribute_map = {
        'category': 'category',
        'name': 'name',
        'weight': 'weight'
    }

    def __init__(self, category=None, name=None, weight=None):
        """QueryDiagnosisResultItem

        The model defined in huaweicloud sdk

        :param category: 诊断项类别。
        :type category: str
        :param name: 诊断项名称。
        :type name: str
        :param weight: 诊断项权重。
        :type weight: float
        """
        
        

        self._category = None
        self._name = None
        self._weight = None
        self.discriminator = None

        if category is not None:
            self.category = category
        if name is not None:
            self.name = name
        if weight is not None:
            self.weight = weight

    @property
    def category(self):
        """Gets the category of this QueryDiagnosisResultItem.

        诊断项类别。

        :return: The category of this QueryDiagnosisResultItem.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this QueryDiagnosisResultItem.

        诊断项类别。

        :param category: The category of this QueryDiagnosisResultItem.
        :type category: str
        """
        self._category = category

    @property
    def name(self):
        """Gets the name of this QueryDiagnosisResultItem.

        诊断项名称。

        :return: The name of this QueryDiagnosisResultItem.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this QueryDiagnosisResultItem.

        诊断项名称。

        :param name: The name of this QueryDiagnosisResultItem.
        :type name: str
        """
        self._name = name

    @property
    def weight(self):
        """Gets the weight of this QueryDiagnosisResultItem.

        诊断项权重。

        :return: The weight of this QueryDiagnosisResultItem.
        :rtype: float
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this QueryDiagnosisResultItem.

        诊断项权重。

        :param weight: The weight of this QueryDiagnosisResultItem.
        :type weight: float
        """
        self._weight = weight

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
        if not isinstance(other, QueryDiagnosisResultItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
