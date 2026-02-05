# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAiApiKeysResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'size': 'int',
        'total': 'int',
        'ai_api_keys': 'list[AiApiKeyBaseInfo]'
    }

    attribute_map = {
        'size': 'size',
        'total': 'total',
        'ai_api_keys': 'ai_api_keys'
    }

    def __init__(self, size=None, total=None, ai_api_keys=None):
        r"""ListAiApiKeysResponse

        The model defined in huaweicloud sdk

        :param size: 本次返回的列表长度
        :type size: int
        :param total: 满足条件的记录数
        :type total: int
        :param ai_api_keys: AIAPIKey列表，展示匿名化的已经创建的AIAPIKey。 AIAPIKey的创建数量上限可以通过配额调整。 
        :type ai_api_keys: list[:class:`huaweicloudsdkapig.v2.AiApiKeyBaseInfo`]
        """
        
        super().__init__()

        self._size = None
        self._total = None
        self._ai_api_keys = None
        self.discriminator = None

        self.size = size
        self.total = total
        if ai_api_keys is not None:
            self.ai_api_keys = ai_api_keys

    @property
    def size(self):
        r"""Gets the size of this ListAiApiKeysResponse.

        本次返回的列表长度

        :return: The size of this ListAiApiKeysResponse.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this ListAiApiKeysResponse.

        本次返回的列表长度

        :param size: The size of this ListAiApiKeysResponse.
        :type size: int
        """
        self._size = size

    @property
    def total(self):
        r"""Gets the total of this ListAiApiKeysResponse.

        满足条件的记录数

        :return: The total of this ListAiApiKeysResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListAiApiKeysResponse.

        满足条件的记录数

        :param total: The total of this ListAiApiKeysResponse.
        :type total: int
        """
        self._total = total

    @property
    def ai_api_keys(self):
        r"""Gets the ai_api_keys of this ListAiApiKeysResponse.

        AIAPIKey列表，展示匿名化的已经创建的AIAPIKey。 AIAPIKey的创建数量上限可以通过配额调整。 

        :return: The ai_api_keys of this ListAiApiKeysResponse.
        :rtype: list[:class:`huaweicloudsdkapig.v2.AiApiKeyBaseInfo`]
        """
        return self._ai_api_keys

    @ai_api_keys.setter
    def ai_api_keys(self, ai_api_keys):
        r"""Sets the ai_api_keys of this ListAiApiKeysResponse.

        AIAPIKey列表，展示匿名化的已经创建的AIAPIKey。 AIAPIKey的创建数量上限可以通过配额调整。 

        :param ai_api_keys: The ai_api_keys of this ListAiApiKeysResponse.
        :type ai_api_keys: list[:class:`huaweicloudsdkapig.v2.AiApiKeyBaseInfo`]
        """
        self._ai_api_keys = ai_api_keys

    def to_dict(self):
        import warnings
        warnings.warn("ListAiApiKeysResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListAiApiKeysResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
