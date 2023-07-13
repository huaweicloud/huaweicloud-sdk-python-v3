# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SynthesisResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'smiles': 'str',
        'top_n': 'int',
        'max_search_depth': 'int',
        'max_prediction_per_product': 'int',
        'result': 'SynthesisResultResult'
    }

    attribute_map = {
        'smiles': 'smiles',
        'top_n': 'top_n',
        'max_search_depth': 'max_search_depth',
        'max_prediction_per_product': 'max_prediction_per_product',
        'result': 'result'
    }

    def __init__(self, smiles=None, top_n=None, max_search_depth=None, max_prediction_per_product=None, result=None):
        """SynthesisResult

        The model defined in huaweicloud sdk

        :param smiles: 分子SMILES表达式
        :type smiles: str
        :param top_n: 期望返回的条目数
        :type top_n: int
        :param max_search_depth: 期望搜索的最大深度
        :type max_search_depth: int
        :param max_prediction_per_product: 期望每个产物的最多反应数量
        :type max_prediction_per_product: int
        :param result: 
        :type result: :class:`huaweicloudsdkeihealth.v1.SynthesisResultResult`
        """
        
        

        self._smiles = None
        self._top_n = None
        self._max_search_depth = None
        self._max_prediction_per_product = None
        self._result = None
        self.discriminator = None

        self.smiles = smiles
        self.top_n = top_n
        self.max_search_depth = max_search_depth
        self.max_prediction_per_product = max_prediction_per_product
        self.result = result

    @property
    def smiles(self):
        """Gets the smiles of this SynthesisResult.

        分子SMILES表达式

        :return: The smiles of this SynthesisResult.
        :rtype: str
        """
        return self._smiles

    @smiles.setter
    def smiles(self, smiles):
        """Sets the smiles of this SynthesisResult.

        分子SMILES表达式

        :param smiles: The smiles of this SynthesisResult.
        :type smiles: str
        """
        self._smiles = smiles

    @property
    def top_n(self):
        """Gets the top_n of this SynthesisResult.

        期望返回的条目数

        :return: The top_n of this SynthesisResult.
        :rtype: int
        """
        return self._top_n

    @top_n.setter
    def top_n(self, top_n):
        """Sets the top_n of this SynthesisResult.

        期望返回的条目数

        :param top_n: The top_n of this SynthesisResult.
        :type top_n: int
        """
        self._top_n = top_n

    @property
    def max_search_depth(self):
        """Gets the max_search_depth of this SynthesisResult.

        期望搜索的最大深度

        :return: The max_search_depth of this SynthesisResult.
        :rtype: int
        """
        return self._max_search_depth

    @max_search_depth.setter
    def max_search_depth(self, max_search_depth):
        """Sets the max_search_depth of this SynthesisResult.

        期望搜索的最大深度

        :param max_search_depth: The max_search_depth of this SynthesisResult.
        :type max_search_depth: int
        """
        self._max_search_depth = max_search_depth

    @property
    def max_prediction_per_product(self):
        """Gets the max_prediction_per_product of this SynthesisResult.

        期望每个产物的最多反应数量

        :return: The max_prediction_per_product of this SynthesisResult.
        :rtype: int
        """
        return self._max_prediction_per_product

    @max_prediction_per_product.setter
    def max_prediction_per_product(self, max_prediction_per_product):
        """Sets the max_prediction_per_product of this SynthesisResult.

        期望每个产物的最多反应数量

        :param max_prediction_per_product: The max_prediction_per_product of this SynthesisResult.
        :type max_prediction_per_product: int
        """
        self._max_prediction_per_product = max_prediction_per_product

    @property
    def result(self):
        """Gets the result of this SynthesisResult.

        :return: The result of this SynthesisResult.
        :rtype: :class:`huaweicloudsdkeihealth.v1.SynthesisResultResult`
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this SynthesisResult.

        :param result: The result of this SynthesisResult.
        :type result: :class:`huaweicloudsdkeihealth.v1.SynthesisResultResult`
        """
        self._result = result

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
        if not isinstance(other, SynthesisResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
