# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UcbParam:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'alpha': 'float',
        'min_used_num': 'int'
    }

    attribute_map = {
        'alpha': 'alpha',
        'min_used_num': 'min_used_num'
    }

    def __init__(self, alpha=None, min_used_num=None):
        """UcbParam

        The model defined in huaweicloud sdk

        :param alpha: 折中参数。
        :type alpha: float
        :param min_used_num: 最小行为次数。
        :type min_used_num: int
        """
        
        

        self._alpha = None
        self._min_used_num = None
        self.discriminator = None

        self.alpha = alpha
        self.min_used_num = min_used_num

    @property
    def alpha(self):
        """Gets the alpha of this UcbParam.

        折中参数。

        :return: The alpha of this UcbParam.
        :rtype: float
        """
        return self._alpha

    @alpha.setter
    def alpha(self, alpha):
        """Sets the alpha of this UcbParam.

        折中参数。

        :param alpha: The alpha of this UcbParam.
        :type alpha: float
        """
        self._alpha = alpha

    @property
    def min_used_num(self):
        """Gets the min_used_num of this UcbParam.

        最小行为次数。

        :return: The min_used_num of this UcbParam.
        :rtype: int
        """
        return self._min_used_num

    @min_used_num.setter
    def min_used_num(self, min_used_num):
        """Sets the min_used_num of this UcbParam.

        最小行为次数。

        :param min_used_num: The min_used_num of this UcbParam.
        :type min_used_num: int
        """
        self._min_used_num = min_used_num

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
        if not isinstance(other, UcbParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
