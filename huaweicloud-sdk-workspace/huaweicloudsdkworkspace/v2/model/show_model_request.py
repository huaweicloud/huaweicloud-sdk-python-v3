# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowModelRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'provider_id': 'str',
        'model_id': 'str'
    }

    attribute_map = {
        'provider_id': 'provider_id',
        'model_id': 'model_id'
    }

    def __init__(self, provider_id=None, model_id=None):
        r"""ShowModelRequest

        The model defined in huaweicloud sdk

        :param provider_id: 供应商id。
        :type provider_id: str
        :param model_id: 模型id。
        :type model_id: str
        """
        
        

        self._provider_id = None
        self._model_id = None
        self.discriminator = None

        self.provider_id = provider_id
        self.model_id = model_id

    @property
    def provider_id(self):
        r"""Gets the provider_id of this ShowModelRequest.

        供应商id。

        :return: The provider_id of this ShowModelRequest.
        :rtype: str
        """
        return self._provider_id

    @provider_id.setter
    def provider_id(self, provider_id):
        r"""Sets the provider_id of this ShowModelRequest.

        供应商id。

        :param provider_id: The provider_id of this ShowModelRequest.
        :type provider_id: str
        """
        self._provider_id = provider_id

    @property
    def model_id(self):
        r"""Gets the model_id of this ShowModelRequest.

        模型id。

        :return: The model_id of this ShowModelRequest.
        :rtype: str
        """
        return self._model_id

    @model_id.setter
    def model_id(self, model_id):
        r"""Sets the model_id of this ShowModelRequest.

        模型id。

        :param model_id: The model_id of this ShowModelRequest.
        :type model_id: str
        """
        self._model_id = model_id

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
        if not isinstance(other, ShowModelRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
