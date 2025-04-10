# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModelConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'llm_model_config': 'LlmModelConfig'
    }

    attribute_map = {
        'llm_model_config': 'llm_model_config'
    }

    def __init__(self, llm_model_config=None):
        r"""ModelConfig

        The model defined in huaweicloud sdk

        :param llm_model_config: 
        :type llm_model_config: :class:`huaweicloudsdkdataartsfabric.v1.LlmModelConfig`
        """
        
        

        self._llm_model_config = None
        self.discriminator = None

        if llm_model_config is not None:
            self.llm_model_config = llm_model_config

    @property
    def llm_model_config(self):
        r"""Gets the llm_model_config of this ModelConfig.

        :return: The llm_model_config of this ModelConfig.
        :rtype: :class:`huaweicloudsdkdataartsfabric.v1.LlmModelConfig`
        """
        return self._llm_model_config

    @llm_model_config.setter
    def llm_model_config(self, llm_model_config):
        r"""Sets the llm_model_config of this ModelConfig.

        :param llm_model_config: The llm_model_config of this ModelConfig.
        :type llm_model_config: :class:`huaweicloudsdkdataartsfabric.v1.LlmModelConfig`
        """
        self._llm_model_config = llm_model_config

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
        if not isinstance(other, ModelConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
