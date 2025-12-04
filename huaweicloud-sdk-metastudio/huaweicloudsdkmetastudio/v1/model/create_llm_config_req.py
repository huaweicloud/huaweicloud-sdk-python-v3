# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateLlmConfigReq:

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
        'llm_url': 'str',
        'api_key': 'str',
        'model': 'str'
    }

    attribute_map = {
        'name': 'name',
        'llm_url': 'llm_url',
        'api_key': 'api_key',
        'model': 'model'
    }

    def __init__(self, name=None, llm_url=None, api_key=None, model=None):
        r"""CreateLlmConfigReq

        The model defined in huaweicloud sdk

        :param name: 大语言模型配置名称。
        :type name: str
        :param llm_url: 大语言模型地址。
        :type llm_url: str
        :param api_key: 密钥。
        :type api_key: str
        :param model: model参数
        :type model: str
        """
        
        

        self._name = None
        self._llm_url = None
        self._api_key = None
        self._model = None
        self.discriminator = None

        self.name = name
        self.llm_url = llm_url
        self.api_key = api_key
        if model is not None:
            self.model = model

    @property
    def name(self):
        r"""Gets the name of this CreateLlmConfigReq.

        大语言模型配置名称。

        :return: The name of this CreateLlmConfigReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateLlmConfigReq.

        大语言模型配置名称。

        :param name: The name of this CreateLlmConfigReq.
        :type name: str
        """
        self._name = name

    @property
    def llm_url(self):
        r"""Gets the llm_url of this CreateLlmConfigReq.

        大语言模型地址。

        :return: The llm_url of this CreateLlmConfigReq.
        :rtype: str
        """
        return self._llm_url

    @llm_url.setter
    def llm_url(self, llm_url):
        r"""Sets the llm_url of this CreateLlmConfigReq.

        大语言模型地址。

        :param llm_url: The llm_url of this CreateLlmConfigReq.
        :type llm_url: str
        """
        self._llm_url = llm_url

    @property
    def api_key(self):
        r"""Gets the api_key of this CreateLlmConfigReq.

        密钥。

        :return: The api_key of this CreateLlmConfigReq.
        :rtype: str
        """
        return self._api_key

    @api_key.setter
    def api_key(self, api_key):
        r"""Sets the api_key of this CreateLlmConfigReq.

        密钥。

        :param api_key: The api_key of this CreateLlmConfigReq.
        :type api_key: str
        """
        self._api_key = api_key

    @property
    def model(self):
        r"""Gets the model of this CreateLlmConfigReq.

        model参数

        :return: The model of this CreateLlmConfigReq.
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        r"""Sets the model of this CreateLlmConfigReq.

        model参数

        :param model: The model of this CreateLlmConfigReq.
        :type model: str
        """
        self._model = model

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
        if not isinstance(other, CreateLlmConfigReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
