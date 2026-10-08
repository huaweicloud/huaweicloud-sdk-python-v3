# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCustomModelProviderModelsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'models': 'list[CreateCustomModelProviderModelResponseBody]',
        'size': 'int',
        'total': 'int'
    }

    attribute_map = {
        'models': 'models',
        'size': 'size',
        'total': 'total'
    }

    def __init__(self, models=None, size=None, total=None):
        r"""ListCustomModelProviderModelsResponse

        The model defined in huaweicloud sdk

        :param models: **参数解释：** 模型配置列表。 **取值范围：** 数组长度为 0-100。 
        :type models: list[:class:`huaweicloudsdkagentarts.v1.CreateCustomModelProviderModelResponseBody`]
        :param size: **参数解释：** 当前页返回的模型配置数量。 **取值范围：** 取值 0-100。 
        :type size: int
        :param total: **参数解释：** 模型配置总数。 **取值范围：** 取值 0-1000000。 
        :type total: int
        """
        
        super().__init__()

        self._models = None
        self._size = None
        self._total = None
        self.discriminator = None

        if models is not None:
            self.models = models
        if size is not None:
            self.size = size
        if total is not None:
            self.total = total

    @property
    def models(self):
        r"""Gets the models of this ListCustomModelProviderModelsResponse.

        **参数解释：** 模型配置列表。 **取值范围：** 数组长度为 0-100。 

        :return: The models of this ListCustomModelProviderModelsResponse.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.CreateCustomModelProviderModelResponseBody`]
        """
        return self._models

    @models.setter
    def models(self, models):
        r"""Sets the models of this ListCustomModelProviderModelsResponse.

        **参数解释：** 模型配置列表。 **取值范围：** 数组长度为 0-100。 

        :param models: The models of this ListCustomModelProviderModelsResponse.
        :type models: list[:class:`huaweicloudsdkagentarts.v1.CreateCustomModelProviderModelResponseBody`]
        """
        self._models = models

    @property
    def size(self):
        r"""Gets the size of this ListCustomModelProviderModelsResponse.

        **参数解释：** 当前页返回的模型配置数量。 **取值范围：** 取值 0-100。 

        :return: The size of this ListCustomModelProviderModelsResponse.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this ListCustomModelProviderModelsResponse.

        **参数解释：** 当前页返回的模型配置数量。 **取值范围：** 取值 0-100。 

        :param size: The size of this ListCustomModelProviderModelsResponse.
        :type size: int
        """
        self._size = size

    @property
    def total(self):
        r"""Gets the total of this ListCustomModelProviderModelsResponse.

        **参数解释：** 模型配置总数。 **取值范围：** 取值 0-1000000。 

        :return: The total of this ListCustomModelProviderModelsResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListCustomModelProviderModelsResponse.

        **参数解释：** 模型配置总数。 **取值范围：** 取值 0-1000000。 

        :param total: The total of this ListCustomModelProviderModelsResponse.
        :type total: int
        """
        self._total = total

    def to_dict(self):
        import warnings
        warnings.warn("ListCustomModelProviderModelsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListCustomModelProviderModelsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
