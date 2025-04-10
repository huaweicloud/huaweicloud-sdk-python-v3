# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BaseModel:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'base_model_type': 'str',
        'max_tokens': 'int',
        'num_of_mu': 'int'
    }

    attribute_map = {
        'base_model_type': 'base_model_type',
        'max_tokens': 'max_tokens',
        'num_of_mu': 'num_of_mu'
    }

    def __init__(self, base_model_type=None, max_tokens=None, num_of_mu=None):
        r"""BaseModel

        The model defined in huaweicloud sdk

        :param base_model_type: 类型请从ListBaseModels列举基模型接口响应中获取
        :type base_model_type: str
        :param max_tokens: 支持的最大token数
        :type max_tokens: int
        :param num_of_mu: 消耗MU数量
        :type num_of_mu: int
        """
        
        

        self._base_model_type = None
        self._max_tokens = None
        self._num_of_mu = None
        self.discriminator = None

        self.base_model_type = base_model_type
        self.max_tokens = max_tokens
        self.num_of_mu = num_of_mu

    @property
    def base_model_type(self):
        r"""Gets the base_model_type of this BaseModel.

        类型请从ListBaseModels列举基模型接口响应中获取

        :return: The base_model_type of this BaseModel.
        :rtype: str
        """
        return self._base_model_type

    @base_model_type.setter
    def base_model_type(self, base_model_type):
        r"""Sets the base_model_type of this BaseModel.

        类型请从ListBaseModels列举基模型接口响应中获取

        :param base_model_type: The base_model_type of this BaseModel.
        :type base_model_type: str
        """
        self._base_model_type = base_model_type

    @property
    def max_tokens(self):
        r"""Gets the max_tokens of this BaseModel.

        支持的最大token数

        :return: The max_tokens of this BaseModel.
        :rtype: int
        """
        return self._max_tokens

    @max_tokens.setter
    def max_tokens(self, max_tokens):
        r"""Sets the max_tokens of this BaseModel.

        支持的最大token数

        :param max_tokens: The max_tokens of this BaseModel.
        :type max_tokens: int
        """
        self._max_tokens = max_tokens

    @property
    def num_of_mu(self):
        r"""Gets the num_of_mu of this BaseModel.

        消耗MU数量

        :return: The num_of_mu of this BaseModel.
        :rtype: int
        """
        return self._num_of_mu

    @num_of_mu.setter
    def num_of_mu(self, num_of_mu):
        r"""Sets the num_of_mu of this BaseModel.

        消耗MU数量

        :param num_of_mu: The num_of_mu of this BaseModel.
        :type num_of_mu: int
        """
        self._num_of_mu = num_of_mu

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
        if not isinstance(other, BaseModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
