# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LlmModelConfig:

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
        'model_path': 'str'
    }

    attribute_map = {
        'base_model_type': 'base_model_type',
        'model_path': 'model_path'
    }

    def __init__(self, base_model_type=None, model_path=None):
        r"""LlmModelConfig

        The model defined in huaweicloud sdk

        :param base_model_type: 类型请从ListBaseModels列举基模型接口响应中获取
        :type base_model_type: str
        :param model_path: 模型文件路径
        :type model_path: str
        """
        
        

        self._base_model_type = None
        self._model_path = None
        self.discriminator = None

        self.base_model_type = base_model_type
        self.model_path = model_path

    @property
    def base_model_type(self):
        r"""Gets the base_model_type of this LlmModelConfig.

        类型请从ListBaseModels列举基模型接口响应中获取

        :return: The base_model_type of this LlmModelConfig.
        :rtype: str
        """
        return self._base_model_type

    @base_model_type.setter
    def base_model_type(self, base_model_type):
        r"""Sets the base_model_type of this LlmModelConfig.

        类型请从ListBaseModels列举基模型接口响应中获取

        :param base_model_type: The base_model_type of this LlmModelConfig.
        :type base_model_type: str
        """
        self._base_model_type = base_model_type

    @property
    def model_path(self):
        r"""Gets the model_path of this LlmModelConfig.

        模型文件路径

        :return: The model_path of this LlmModelConfig.
        :rtype: str
        """
        return self._model_path

    @model_path.setter
    def model_path(self, model_path):
        r"""Sets the model_path of this LlmModelConfig.

        模型文件路径

        :param model_path: The model_path of this LlmModelConfig.
        :type model_path: str
        """
        self._model_path = model_path

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
        if not isinstance(other, LlmModelConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
