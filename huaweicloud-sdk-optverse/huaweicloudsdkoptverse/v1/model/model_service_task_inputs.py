# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModelServiceTaskInputs:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'model_data': 'str',
        'model_request': 'str'
    }

    attribute_map = {
        'model_data': 'model_data',
        'model_request': 'model_request'
    }

    def __init__(self, model_data=None, model_request=None):
        r"""ModelServiceTaskInputs

        The model defined in huaweicloud sdk

        :param model_data: **参数解释**： 创建沙箱任务输入数据文件路径。支持求解助手类型的模型服务任务时使用，优先级高于model_request。 **约束限制**： 不涉及 **取值范围**： 长度为[0-2048]个字符。 **默认取值**： 不涉及 
        :type model_data: str
        :param model_request: **参数解释**： 创建沙箱任务输入请求体。 **约束限制**： 不涉及 **取值范围**： 长度为[0-12582912]个字符，上限12MB。 **默认取值**： 不涉及 
        :type model_request: str
        """
        
        

        self._model_data = None
        self._model_request = None
        self.discriminator = None

        if model_data is not None:
            self.model_data = model_data
        if model_request is not None:
            self.model_request = model_request

    @property
    def model_data(self):
        r"""Gets the model_data of this ModelServiceTaskInputs.

        **参数解释**： 创建沙箱任务输入数据文件路径。支持求解助手类型的模型服务任务时使用，优先级高于model_request。 **约束限制**： 不涉及 **取值范围**： 长度为[0-2048]个字符。 **默认取值**： 不涉及 

        :return: The model_data of this ModelServiceTaskInputs.
        :rtype: str
        """
        return self._model_data

    @model_data.setter
    def model_data(self, model_data):
        r"""Sets the model_data of this ModelServiceTaskInputs.

        **参数解释**： 创建沙箱任务输入数据文件路径。支持求解助手类型的模型服务任务时使用，优先级高于model_request。 **约束限制**： 不涉及 **取值范围**： 长度为[0-2048]个字符。 **默认取值**： 不涉及 

        :param model_data: The model_data of this ModelServiceTaskInputs.
        :type model_data: str
        """
        self._model_data = model_data

    @property
    def model_request(self):
        r"""Gets the model_request of this ModelServiceTaskInputs.

        **参数解释**： 创建沙箱任务输入请求体。 **约束限制**： 不涉及 **取值范围**： 长度为[0-12582912]个字符，上限12MB。 **默认取值**： 不涉及 

        :return: The model_request of this ModelServiceTaskInputs.
        :rtype: str
        """
        return self._model_request

    @model_request.setter
    def model_request(self, model_request):
        r"""Sets the model_request of this ModelServiceTaskInputs.

        **参数解释**： 创建沙箱任务输入请求体。 **约束限制**： 不涉及 **取值范围**： 长度为[0-12582912]个字符，上限12MB。 **默认取值**： 不涉及 

        :param model_request: The model_request of this ModelServiceTaskInputs.
        :type model_request: str
        """
        self._model_request = model_request

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
        if not isinstance(other, ModelServiceTaskInputs):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
