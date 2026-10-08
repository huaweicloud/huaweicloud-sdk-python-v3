# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListModelProxiesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'model_proxies': 'list[ListModelProxiesItem]',
        'size': 'int',
        'total': 'int'
    }

    attribute_map = {
        'model_proxies': 'model_proxies',
        'size': 'size',
        'total': 'total'
    }

    def __init__(self, model_proxies=None, size=None, total=None):
        r"""ListModelProxiesResponse

        The model defined in huaweicloud sdk

        :param model_proxies: **参数解释：** 模型代理详情。 **取值范围：** 数组长度为0-500个。 
        :type model_proxies: list[:class:`huaweicloudsdkagentarts.v1.ListModelProxiesItem`]
        :param size: **参数解释：** 当前页返回的模型代理数量。 **取值范围：** 取值 0-100。 
        :type size: int
        :param total: **参数解释：** 模型代理总数。 **取值范围：** 取值 0-1000000。 
        :type total: int
        """
        
        super().__init__()

        self._model_proxies = None
        self._size = None
        self._total = None
        self.discriminator = None

        if model_proxies is not None:
            self.model_proxies = model_proxies
        if size is not None:
            self.size = size
        if total is not None:
            self.total = total

    @property
    def model_proxies(self):
        r"""Gets the model_proxies of this ListModelProxiesResponse.

        **参数解释：** 模型代理详情。 **取值范围：** 数组长度为0-500个。 

        :return: The model_proxies of this ListModelProxiesResponse.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.ListModelProxiesItem`]
        """
        return self._model_proxies

    @model_proxies.setter
    def model_proxies(self, model_proxies):
        r"""Sets the model_proxies of this ListModelProxiesResponse.

        **参数解释：** 模型代理详情。 **取值范围：** 数组长度为0-500个。 

        :param model_proxies: The model_proxies of this ListModelProxiesResponse.
        :type model_proxies: list[:class:`huaweicloudsdkagentarts.v1.ListModelProxiesItem`]
        """
        self._model_proxies = model_proxies

    @property
    def size(self):
        r"""Gets the size of this ListModelProxiesResponse.

        **参数解释：** 当前页返回的模型代理数量。 **取值范围：** 取值 0-100。 

        :return: The size of this ListModelProxiesResponse.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this ListModelProxiesResponse.

        **参数解释：** 当前页返回的模型代理数量。 **取值范围：** 取值 0-100。 

        :param size: The size of this ListModelProxiesResponse.
        :type size: int
        """
        self._size = size

    @property
    def total(self):
        r"""Gets the total of this ListModelProxiesResponse.

        **参数解释：** 模型代理总数。 **取值范围：** 取值 0-1000000。 

        :return: The total of this ListModelProxiesResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListModelProxiesResponse.

        **参数解释：** 模型代理总数。 **取值范围：** 取值 0-1000000。 

        :param total: The total of this ListModelProxiesResponse.
        :type total: int
        """
        self._total = total

    def to_dict(self):
        import warnings
        warnings.warn("ListModelProxiesResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListModelProxiesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
