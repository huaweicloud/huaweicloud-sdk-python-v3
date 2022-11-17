# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MatrixFactorization:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'implicit_vector_rank': 'int',
        'regular_param': 'float',
        'max_iterator_num': 'int'
    }

    attribute_map = {
        'implicit_vector_rank': 'implicit_vector_rank',
        'regular_param': 'regular_param',
        'max_iterator_num': 'max_iterator_num'
    }

    def __init__(self, implicit_vector_rank=None, regular_param=None, max_iterator_num=None):
        """MatrixFactorization

        The model defined in huaweicloud sdk

        :param implicit_vector_rank: 隐向量维度。
        :type implicit_vector_rank: int
        :param regular_param: 优化正则化系数。
        :type regular_param: float
        :param max_iterator_num: 迭代次数。
        :type max_iterator_num: int
        """
        
        

        self._implicit_vector_rank = None
        self._regular_param = None
        self._max_iterator_num = None
        self.discriminator = None

        self.implicit_vector_rank = implicit_vector_rank
        self.regular_param = regular_param
        self.max_iterator_num = max_iterator_num

    @property
    def implicit_vector_rank(self):
        """Gets the implicit_vector_rank of this MatrixFactorization.

        隐向量维度。

        :return: The implicit_vector_rank of this MatrixFactorization.
        :rtype: int
        """
        return self._implicit_vector_rank

    @implicit_vector_rank.setter
    def implicit_vector_rank(self, implicit_vector_rank):
        """Sets the implicit_vector_rank of this MatrixFactorization.

        隐向量维度。

        :param implicit_vector_rank: The implicit_vector_rank of this MatrixFactorization.
        :type implicit_vector_rank: int
        """
        self._implicit_vector_rank = implicit_vector_rank

    @property
    def regular_param(self):
        """Gets the regular_param of this MatrixFactorization.

        优化正则化系数。

        :return: The regular_param of this MatrixFactorization.
        :rtype: float
        """
        return self._regular_param

    @regular_param.setter
    def regular_param(self, regular_param):
        """Sets the regular_param of this MatrixFactorization.

        优化正则化系数。

        :param regular_param: The regular_param of this MatrixFactorization.
        :type regular_param: float
        """
        self._regular_param = regular_param

    @property
    def max_iterator_num(self):
        """Gets the max_iterator_num of this MatrixFactorization.

        迭代次数。

        :return: The max_iterator_num of this MatrixFactorization.
        :rtype: int
        """
        return self._max_iterator_num

    @max_iterator_num.setter
    def max_iterator_num(self, max_iterator_num):
        """Sets the max_iterator_num of this MatrixFactorization.

        迭代次数。

        :param max_iterator_num: The max_iterator_num of this MatrixFactorization.
        :type max_iterator_num: int
        """
        self._max_iterator_num = max_iterator_num

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
        if not isinstance(other, MatrixFactorization):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
