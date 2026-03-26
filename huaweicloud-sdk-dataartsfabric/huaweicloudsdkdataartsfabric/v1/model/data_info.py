# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DataInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'input_path': 'str',
        'output_path': 'str',
        'env_var_name': 'str'
    }

    attribute_map = {
        'input_path': 'input_path',
        'output_path': 'output_path',
        'env_var_name': 'env_var_name'
    }

    def __init__(self, input_path=None, output_path=None, env_var_name=None):
        r"""DataInfo

        The model defined in huaweicloud sdk

        :param input_path: **参数解释**：地址。 **约束限制**：不涉及。 **取值范围**：长度[4,1024]。 **默认取值**：不涉及。 
        :type input_path: str
        :param output_path: **参数解释**：地址。 **约束限制**：不涉及。 **取值范围**：长度[4,1024]。 **默认取值**：不涉及。 
        :type output_path: str
        :param env_var_name: **参数解释**：环境变量名称。 **约束限制**：不涉及。 **取值范围**：长度[2,100]。 **默认取值**：不涉及。 
        :type env_var_name: str
        """
        
        

        self._input_path = None
        self._output_path = None
        self._env_var_name = None
        self.discriminator = None

        if input_path is not None:
            self.input_path = input_path
        if output_path is not None:
            self.output_path = output_path
        if env_var_name is not None:
            self.env_var_name = env_var_name

    @property
    def input_path(self):
        r"""Gets the input_path of this DataInfo.

        **参数解释**：地址。 **约束限制**：不涉及。 **取值范围**：长度[4,1024]。 **默认取值**：不涉及。 

        :return: The input_path of this DataInfo.
        :rtype: str
        """
        return self._input_path

    @input_path.setter
    def input_path(self, input_path):
        r"""Sets the input_path of this DataInfo.

        **参数解释**：地址。 **约束限制**：不涉及。 **取值范围**：长度[4,1024]。 **默认取值**：不涉及。 

        :param input_path: The input_path of this DataInfo.
        :type input_path: str
        """
        self._input_path = input_path

    @property
    def output_path(self):
        r"""Gets the output_path of this DataInfo.

        **参数解释**：地址。 **约束限制**：不涉及。 **取值范围**：长度[4,1024]。 **默认取值**：不涉及。 

        :return: The output_path of this DataInfo.
        :rtype: str
        """
        return self._output_path

    @output_path.setter
    def output_path(self, output_path):
        r"""Sets the output_path of this DataInfo.

        **参数解释**：地址。 **约束限制**：不涉及。 **取值范围**：长度[4,1024]。 **默认取值**：不涉及。 

        :param output_path: The output_path of this DataInfo.
        :type output_path: str
        """
        self._output_path = output_path

    @property
    def env_var_name(self):
        r"""Gets the env_var_name of this DataInfo.

        **参数解释**：环境变量名称。 **约束限制**：不涉及。 **取值范围**：长度[2,100]。 **默认取值**：不涉及。 

        :return: The env_var_name of this DataInfo.
        :rtype: str
        """
        return self._env_var_name

    @env_var_name.setter
    def env_var_name(self, env_var_name):
        r"""Sets the env_var_name of this DataInfo.

        **参数解释**：环境变量名称。 **约束限制**：不涉及。 **取值范围**：长度[2,100]。 **默认取值**：不涉及。 

        :param env_var_name: The env_var_name of this DataInfo.
        :type env_var_name: str
        """
        self._env_var_name = env_var_name

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DataInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
