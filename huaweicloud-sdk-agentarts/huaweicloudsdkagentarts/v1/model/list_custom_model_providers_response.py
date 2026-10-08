# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCustomModelProvidersResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'model_providers': 'list[CreateCustomModelProviderResponseBody]',
        'size': 'int',
        'total': 'int'
    }

    attribute_map = {
        'model_providers': 'model_providers',
        'size': 'size',
        'total': 'total'
    }

    def __init__(self, model_providers=None, size=None, total=None):
        r"""ListCustomModelProvidersResponse

        The model defined in huaweicloud sdk

        :param model_providers: **参数解释：** 模型提供商列表。 **取值范围：** 数组长度为 0-100。 
        :type model_providers: list[:class:`huaweicloudsdkagentarts.v1.CreateCustomModelProviderResponseBody`]
        :param size: **参数解释：** 当前页返回的模型配置数量。 **取值范围：** 取值 0-100。 
        :type size: int
        :param total: **参数解释：** 模型配置总数。 **取值范围：** 取值 0-1000000。 
        :type total: int
        """
        
        super().__init__()

        self._model_providers = None
        self._size = None
        self._total = None
        self.discriminator = None

        if model_providers is not None:
            self.model_providers = model_providers
        if size is not None:
            self.size = size
        if total is not None:
            self.total = total

    @property
    def model_providers(self):
        r"""Gets the model_providers of this ListCustomModelProvidersResponse.

        **参数解释：** 模型提供商列表。 **取值范围：** 数组长度为 0-100。 

        :return: The model_providers of this ListCustomModelProvidersResponse.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.CreateCustomModelProviderResponseBody`]
        """
        return self._model_providers

    @model_providers.setter
    def model_providers(self, model_providers):
        r"""Sets the model_providers of this ListCustomModelProvidersResponse.

        **参数解释：** 模型提供商列表。 **取值范围：** 数组长度为 0-100。 

        :param model_providers: The model_providers of this ListCustomModelProvidersResponse.
        :type model_providers: list[:class:`huaweicloudsdkagentarts.v1.CreateCustomModelProviderResponseBody`]
        """
        self._model_providers = model_providers

    @property
    def size(self):
        r"""Gets the size of this ListCustomModelProvidersResponse.

        **参数解释：** 当前页返回的模型配置数量。 **取值范围：** 取值 0-100。 

        :return: The size of this ListCustomModelProvidersResponse.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this ListCustomModelProvidersResponse.

        **参数解释：** 当前页返回的模型配置数量。 **取值范围：** 取值 0-100。 

        :param size: The size of this ListCustomModelProvidersResponse.
        :type size: int
        """
        self._size = size

    @property
    def total(self):
        r"""Gets the total of this ListCustomModelProvidersResponse.

        **参数解释：** 模型配置总数。 **取值范围：** 取值 0-1000000。 

        :return: The total of this ListCustomModelProvidersResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListCustomModelProvidersResponse.

        **参数解释：** 模型配置总数。 **取值范围：** 取值 0-1000000。 

        :param total: The total of this ListCustomModelProvidersResponse.
        :type total: int
        """
        self._total = total

    def to_dict(self):
        import warnings
        warnings.warn("ListCustomModelProvidersResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ListCustomModelProvidersResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
