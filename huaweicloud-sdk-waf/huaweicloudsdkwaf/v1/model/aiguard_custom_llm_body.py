# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AiguardCustomLlmBody:

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
        'description': 'str',
        'model_name': 'str',
        'protocol': 'str',
        'url': 'str',
        'api_key': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'model_name': 'model_name',
        'protocol': 'protocol',
        'url': 'url',
        'api_key': 'api_key'
    }

    def __init__(self, name=None, description=None, model_name=None, protocol=None, url=None, api_key=None):
        r"""AiguardCustomLlmBody

        The model defined in huaweicloud sdk

        :param name: 自定义大模型名称
        :type name: str
        :param description: 自定义大模型描述
        :type description: str
        :param model_name: 模型名称
        :type model_name: str
        :param protocol: 协议类型
        :type protocol: str
        :param url: API地址
        :type url: str
        :param api_key: API密钥
        :type api_key: str
        """
        
        

        self._name = None
        self._description = None
        self._model_name = None
        self._protocol = None
        self._url = None
        self._api_key = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        self.model_name = model_name
        self.protocol = protocol
        self.url = url
        self.api_key = api_key

    @property
    def name(self):
        r"""Gets the name of this AiguardCustomLlmBody.

        自定义大模型名称

        :return: The name of this AiguardCustomLlmBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this AiguardCustomLlmBody.

        自定义大模型名称

        :param name: The name of this AiguardCustomLlmBody.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this AiguardCustomLlmBody.

        自定义大模型描述

        :return: The description of this AiguardCustomLlmBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this AiguardCustomLlmBody.

        自定义大模型描述

        :param description: The description of this AiguardCustomLlmBody.
        :type description: str
        """
        self._description = description

    @property
    def model_name(self):
        r"""Gets the model_name of this AiguardCustomLlmBody.

        模型名称

        :return: The model_name of this AiguardCustomLlmBody.
        :rtype: str
        """
        return self._model_name

    @model_name.setter
    def model_name(self, model_name):
        r"""Sets the model_name of this AiguardCustomLlmBody.

        模型名称

        :param model_name: The model_name of this AiguardCustomLlmBody.
        :type model_name: str
        """
        self._model_name = model_name

    @property
    def protocol(self):
        r"""Gets the protocol of this AiguardCustomLlmBody.

        协议类型

        :return: The protocol of this AiguardCustomLlmBody.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        r"""Sets the protocol of this AiguardCustomLlmBody.

        协议类型

        :param protocol: The protocol of this AiguardCustomLlmBody.
        :type protocol: str
        """
        self._protocol = protocol

    @property
    def url(self):
        r"""Gets the url of this AiguardCustomLlmBody.

        API地址

        :return: The url of this AiguardCustomLlmBody.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this AiguardCustomLlmBody.

        API地址

        :param url: The url of this AiguardCustomLlmBody.
        :type url: str
        """
        self._url = url

    @property
    def api_key(self):
        r"""Gets the api_key of this AiguardCustomLlmBody.

        API密钥

        :return: The api_key of this AiguardCustomLlmBody.
        :rtype: str
        """
        return self._api_key

    @api_key.setter
    def api_key(self, api_key):
        r"""Sets the api_key of this AiguardCustomLlmBody.

        API密钥

        :param api_key: The api_key of this AiguardCustomLlmBody.
        :type api_key: str
        """
        self._api_key = api_key

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
        if not isinstance(other, AiguardCustomLlmBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
