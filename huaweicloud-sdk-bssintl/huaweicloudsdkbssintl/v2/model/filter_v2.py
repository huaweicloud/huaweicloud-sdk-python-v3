# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FilterV2:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'operator': 'int',
        'filter_factor': 'FilterFactor'
    }

    attribute_map = {
        'operator': 'operator',
        'filter_factor': 'filter_factor'
    }

    def __init__(self, operator=None, filter_factor=None):
        """FilterV2

        The model defined in huaweicloud sdk

        :param operator: 运算符，0：仅包含1：仅排除 此参数不携带或携带值为null时，不作为筛选条件。
        :type operator: int
        :param filter_factor: 
        :type filter_factor: :class:`huaweicloudsdkbssintl.v2.FilterFactor`
        """
        
        

        self._operator = None
        self._filter_factor = None
        self.discriminator = None

        self.operator = operator
        self.filter_factor = filter_factor

    @property
    def operator(self):
        """Gets the operator of this FilterV2.

        运算符，0：仅包含1：仅排除 此参数不携带或携带值为null时，不作为筛选条件。

        :return: The operator of this FilterV2.
        :rtype: int
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """Sets the operator of this FilterV2.

        运算符，0：仅包含1：仅排除 此参数不携带或携带值为null时，不作为筛选条件。

        :param operator: The operator of this FilterV2.
        :type operator: int
        """
        self._operator = operator

    @property
    def filter_factor(self):
        """Gets the filter_factor of this FilterV2.

        :return: The filter_factor of this FilterV2.
        :rtype: :class:`huaweicloudsdkbssintl.v2.FilterFactor`
        """
        return self._filter_factor

    @filter_factor.setter
    def filter_factor(self, filter_factor):
        """Sets the filter_factor of this FilterV2.

        :param filter_factor: The filter_factor of this FilterV2.
        :type filter_factor: :class:`huaweicloudsdkbssintl.v2.FilterFactor`
        """
        self._filter_factor = filter_factor

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
        if not isinstance(other, FilterV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
