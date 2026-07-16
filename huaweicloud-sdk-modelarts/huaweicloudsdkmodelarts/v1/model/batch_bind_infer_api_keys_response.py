# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchBindInferApiKeysResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total': 'int',
        'success_count': 'int',
        'success_items': 'list[ApiKeyResponseV2]',
        'failure_count': 'int',
        'failure_items': 'list[ApiKeyFailureResponse]'
    }

    attribute_map = {
        'total': 'total',
        'success_count': 'success_count',
        'success_items': 'success_items',
        'failure_count': 'failure_count',
        'failure_items': 'failure_items'
    }

    def __init__(self, total=None, success_count=None, success_items=None, failure_count=None, failure_items=None):
        r"""BatchBindInferApiKeysResponse

        The model defined in huaweicloud sdk

        :param total: **参数解释：** 请求绑定apikey总个数。 **取值范围：** 不涉及。
        :type total: int
        :param success_count: **参数解释：** 绑定apikey成功个数。 **取值范围：** 不涉及。
        :type success_count: int
        :param success_items: **参数解释：** 绑定成功的apikey列表。
        :type success_items: list[:class:`huaweicloudsdkmodelarts.v1.ApiKeyResponseV2`]
        :param failure_count: **参数解释：** 绑定apikey失败个数。 **取值范围：** 不涉及。
        :type failure_count: int
        :param failure_items: **参数解释：** 绑定失败的apikey列表。
        :type failure_items: list[:class:`huaweicloudsdkmodelarts.v1.ApiKeyFailureResponse`]
        """
        
        super().__init__()

        self._total = None
        self._success_count = None
        self._success_items = None
        self._failure_count = None
        self._failure_items = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if success_count is not None:
            self.success_count = success_count
        if success_items is not None:
            self.success_items = success_items
        if failure_count is not None:
            self.failure_count = failure_count
        if failure_items is not None:
            self.failure_items = failure_items

    @property
    def total(self):
        r"""Gets the total of this BatchBindInferApiKeysResponse.

        **参数解释：** 请求绑定apikey总个数。 **取值范围：** 不涉及。

        :return: The total of this BatchBindInferApiKeysResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this BatchBindInferApiKeysResponse.

        **参数解释：** 请求绑定apikey总个数。 **取值范围：** 不涉及。

        :param total: The total of this BatchBindInferApiKeysResponse.
        :type total: int
        """
        self._total = total

    @property
    def success_count(self):
        r"""Gets the success_count of this BatchBindInferApiKeysResponse.

        **参数解释：** 绑定apikey成功个数。 **取值范围：** 不涉及。

        :return: The success_count of this BatchBindInferApiKeysResponse.
        :rtype: int
        """
        return self._success_count

    @success_count.setter
    def success_count(self, success_count):
        r"""Sets the success_count of this BatchBindInferApiKeysResponse.

        **参数解释：** 绑定apikey成功个数。 **取值范围：** 不涉及。

        :param success_count: The success_count of this BatchBindInferApiKeysResponse.
        :type success_count: int
        """
        self._success_count = success_count

    @property
    def success_items(self):
        r"""Gets the success_items of this BatchBindInferApiKeysResponse.

        **参数解释：** 绑定成功的apikey列表。

        :return: The success_items of this BatchBindInferApiKeysResponse.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.ApiKeyResponseV2`]
        """
        return self._success_items

    @success_items.setter
    def success_items(self, success_items):
        r"""Sets the success_items of this BatchBindInferApiKeysResponse.

        **参数解释：** 绑定成功的apikey列表。

        :param success_items: The success_items of this BatchBindInferApiKeysResponse.
        :type success_items: list[:class:`huaweicloudsdkmodelarts.v1.ApiKeyResponseV2`]
        """
        self._success_items = success_items

    @property
    def failure_count(self):
        r"""Gets the failure_count of this BatchBindInferApiKeysResponse.

        **参数解释：** 绑定apikey失败个数。 **取值范围：** 不涉及。

        :return: The failure_count of this BatchBindInferApiKeysResponse.
        :rtype: int
        """
        return self._failure_count

    @failure_count.setter
    def failure_count(self, failure_count):
        r"""Sets the failure_count of this BatchBindInferApiKeysResponse.

        **参数解释：** 绑定apikey失败个数。 **取值范围：** 不涉及。

        :param failure_count: The failure_count of this BatchBindInferApiKeysResponse.
        :type failure_count: int
        """
        self._failure_count = failure_count

    @property
    def failure_items(self):
        r"""Gets the failure_items of this BatchBindInferApiKeysResponse.

        **参数解释：** 绑定失败的apikey列表。

        :return: The failure_items of this BatchBindInferApiKeysResponse.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.ApiKeyFailureResponse`]
        """
        return self._failure_items

    @failure_items.setter
    def failure_items(self, failure_items):
        r"""Sets the failure_items of this BatchBindInferApiKeysResponse.

        **参数解释：** 绑定失败的apikey列表。

        :param failure_items: The failure_items of this BatchBindInferApiKeysResponse.
        :type failure_items: list[:class:`huaweicloudsdkmodelarts.v1.ApiKeyFailureResponse`]
        """
        self._failure_items = failure_items

    def to_dict(self):
        import warnings
        warnings.warn("BatchBindInferApiKeysResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, BatchBindInferApiKeysResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
