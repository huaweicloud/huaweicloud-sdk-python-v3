# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SynthesisParamDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'top_n': 'int',
        'max_search_depth': 'int',
        'time_limit': 'int',
        'max_prediction_per_product': 'int'
    }

    attribute_map = {
        'top_n': 'top_n',
        'max_search_depth': 'max_search_depth',
        'time_limit': 'time_limit',
        'max_prediction_per_product': 'max_prediction_per_product'
    }

    def __init__(self, top_n=None, max_search_depth=None, time_limit=None, max_prediction_per_product=None):
        r"""SynthesisParamDto

        The model defined in huaweicloud sdk

        :param top_n: 期望最大返回条目数（排序后取TopN）
        :type top_n: int
        :param max_search_depth: 预测路径的最大深度
        :type max_search_depth: int
        :param time_limit: 搜索最大时间，单位:分钟
        :type time_limit: int
        :param max_prediction_per_product: 每个产物的最大反应数量
        :type max_prediction_per_product: int
        """
        
        

        self._top_n = None
        self._max_search_depth = None
        self._time_limit = None
        self._max_prediction_per_product = None
        self.discriminator = None

        self.top_n = top_n
        self.max_search_depth = max_search_depth
        self.time_limit = time_limit
        self.max_prediction_per_product = max_prediction_per_product

    @property
    def top_n(self):
        r"""Gets the top_n of this SynthesisParamDto.

        期望最大返回条目数（排序后取TopN）

        :return: The top_n of this SynthesisParamDto.
        :rtype: int
        """
        return self._top_n

    @top_n.setter
    def top_n(self, top_n):
        r"""Sets the top_n of this SynthesisParamDto.

        期望最大返回条目数（排序后取TopN）

        :param top_n: The top_n of this SynthesisParamDto.
        :type top_n: int
        """
        self._top_n = top_n

    @property
    def max_search_depth(self):
        r"""Gets the max_search_depth of this SynthesisParamDto.

        预测路径的最大深度

        :return: The max_search_depth of this SynthesisParamDto.
        :rtype: int
        """
        return self._max_search_depth

    @max_search_depth.setter
    def max_search_depth(self, max_search_depth):
        r"""Sets the max_search_depth of this SynthesisParamDto.

        预测路径的最大深度

        :param max_search_depth: The max_search_depth of this SynthesisParamDto.
        :type max_search_depth: int
        """
        self._max_search_depth = max_search_depth

    @property
    def time_limit(self):
        r"""Gets the time_limit of this SynthesisParamDto.

        搜索最大时间，单位:分钟

        :return: The time_limit of this SynthesisParamDto.
        :rtype: int
        """
        return self._time_limit

    @time_limit.setter
    def time_limit(self, time_limit):
        r"""Sets the time_limit of this SynthesisParamDto.

        搜索最大时间，单位:分钟

        :param time_limit: The time_limit of this SynthesisParamDto.
        :type time_limit: int
        """
        self._time_limit = time_limit

    @property
    def max_prediction_per_product(self):
        r"""Gets the max_prediction_per_product of this SynthesisParamDto.

        每个产物的最大反应数量

        :return: The max_prediction_per_product of this SynthesisParamDto.
        :rtype: int
        """
        return self._max_prediction_per_product

    @max_prediction_per_product.setter
    def max_prediction_per_product(self, max_prediction_per_product):
        r"""Sets the max_prediction_per_product of this SynthesisParamDto.

        每个产物的最大反应数量

        :param max_prediction_per_product: The max_prediction_per_product of this SynthesisParamDto.
        :type max_prediction_per_product: int
        """
        self._max_prediction_per_product = max_prediction_per_product

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
        if not isinstance(other, SynthesisParamDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
