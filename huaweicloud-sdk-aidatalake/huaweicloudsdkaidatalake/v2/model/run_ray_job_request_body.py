# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RunRayJobRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'endpoint_name': 'str',
        'config': 'RayJobConfig',
        'description': 'str'
    }

    attribute_map = {
        'name': 'name',
        'endpoint_name': 'endpoint_name',
        'config': 'config',
        'description': 'description'
    }

    def __init__(self, name=None, endpoint_name=None, config=None, description=None):
        r"""RunRayJobRequestBody

        The model defined in huaweicloud sdk

        :param name: **参数解释**：Job名称。 **约束限制**：不涉及。 **取值范围**：长度为1~47的英文字母、数字、中划线的组合。 **默认取值**：不涉及。 
        :type name: str
        :param endpoint_name: **参数解释**：端点名称。 **约束限制**：不涉及。 **取值范围**：长度为1~63个字符。包含小写字母、数字、中划线的组合。字母开头、字母或数字结尾。 **默认取值**：不涉及。
        :type endpoint_name: str
        :param config: 
        :type config: :class:`huaweicloudsdkaidatalake.v2.RayJobConfig`
        :param description: **参数解释**：描述信息。 **约束限制**：不涉及。 **取值范围**：0~1024。 **默认取值**：不涉及。 
        :type description: str
        """
        
        

        self._name = None
        self._endpoint_name = None
        self._config = None
        self._description = None
        self.discriminator = None

        self.name = name
        self.endpoint_name = endpoint_name
        self.config = config
        if description is not None:
            self.description = description

    @property
    def name(self):
        r"""Gets the name of this RunRayJobRequestBody.

        **参数解释**：Job名称。 **约束限制**：不涉及。 **取值范围**：长度为1~47的英文字母、数字、中划线的组合。 **默认取值**：不涉及。 

        :return: The name of this RunRayJobRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this RunRayJobRequestBody.

        **参数解释**：Job名称。 **约束限制**：不涉及。 **取值范围**：长度为1~47的英文字母、数字、中划线的组合。 **默认取值**：不涉及。 

        :param name: The name of this RunRayJobRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def endpoint_name(self):
        r"""Gets the endpoint_name of this RunRayJobRequestBody.

        **参数解释**：端点名称。 **约束限制**：不涉及。 **取值范围**：长度为1~63个字符。包含小写字母、数字、中划线的组合。字母开头、字母或数字结尾。 **默认取值**：不涉及。

        :return: The endpoint_name of this RunRayJobRequestBody.
        :rtype: str
        """
        return self._endpoint_name

    @endpoint_name.setter
    def endpoint_name(self, endpoint_name):
        r"""Sets the endpoint_name of this RunRayJobRequestBody.

        **参数解释**：端点名称。 **约束限制**：不涉及。 **取值范围**：长度为1~63个字符。包含小写字母、数字、中划线的组合。字母开头、字母或数字结尾。 **默认取值**：不涉及。

        :param endpoint_name: The endpoint_name of this RunRayJobRequestBody.
        :type endpoint_name: str
        """
        self._endpoint_name = endpoint_name

    @property
    def config(self):
        r"""Gets the config of this RunRayJobRequestBody.

        :return: The config of this RunRayJobRequestBody.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.RayJobConfig`
        """
        return self._config

    @config.setter
    def config(self, config):
        r"""Sets the config of this RunRayJobRequestBody.

        :param config: The config of this RunRayJobRequestBody.
        :type config: :class:`huaweicloudsdkaidatalake.v2.RayJobConfig`
        """
        self._config = config

    @property
    def description(self):
        r"""Gets the description of this RunRayJobRequestBody.

        **参数解释**：描述信息。 **约束限制**：不涉及。 **取值范围**：0~1024。 **默认取值**：不涉及。 

        :return: The description of this RunRayJobRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this RunRayJobRequestBody.

        **参数解释**：描述信息。 **约束限制**：不涉及。 **取值范围**：0~1024。 **默认取值**：不涉及。 

        :param description: The description of this RunRayJobRequestBody.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, RunRayJobRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
