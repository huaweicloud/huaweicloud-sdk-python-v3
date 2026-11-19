# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowInstanceStorageInfoResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'used': 'float',
        'prepaid_size': 'float',
        'limit': 'float',
        'type': 'str'
    }

    attribute_map = {
        'used': 'used',
        'prepaid_size': 'prepaid_size',
        'limit': 'limit',
        'type': 'type'
    }

    def __init__(self, used=None, prepaid_size=None, limit=None, type=None):
        r"""ShowInstanceStorageInfoResponse

        The model defined in huaweicloud sdk

        :param used: **参数解释**：  已使用存储空间大小，单位是GB。  **取值范围**：  大于等于0。
        :type used: float
        :param prepaid_size: **参数解释**：  包年/包月购买的存储空间大小，单位是GB。  **取值范围**：  大于0。
        :type prepaid_size: float
        :param limit: **参数解释**：  实例可使用的存储空间上限，单位是GB。  **取值范围**：  大于0。
        :type limit: float
        :param type: **参数解释**：  存储类型。  **取值范围**：  - POOL：DL6存储类型。 - STANDARDPOOL：DL5存储类型。
        :type type: str
        """
        
        super().__init__()

        self._used = None
        self._prepaid_size = None
        self._limit = None
        self._type = None
        self.discriminator = None

        if used is not None:
            self.used = used
        if prepaid_size is not None:
            self.prepaid_size = prepaid_size
        if limit is not None:
            self.limit = limit
        if type is not None:
            self.type = type

    @property
    def used(self):
        r"""Gets the used of this ShowInstanceStorageInfoResponse.

        **参数解释**：  已使用存储空间大小，单位是GB。  **取值范围**：  大于等于0。

        :return: The used of this ShowInstanceStorageInfoResponse.
        :rtype: float
        """
        return self._used

    @used.setter
    def used(self, used):
        r"""Sets the used of this ShowInstanceStorageInfoResponse.

        **参数解释**：  已使用存储空间大小，单位是GB。  **取值范围**：  大于等于0。

        :param used: The used of this ShowInstanceStorageInfoResponse.
        :type used: float
        """
        self._used = used

    @property
    def prepaid_size(self):
        r"""Gets the prepaid_size of this ShowInstanceStorageInfoResponse.

        **参数解释**：  包年/包月购买的存储空间大小，单位是GB。  **取值范围**：  大于0。

        :return: The prepaid_size of this ShowInstanceStorageInfoResponse.
        :rtype: float
        """
        return self._prepaid_size

    @prepaid_size.setter
    def prepaid_size(self, prepaid_size):
        r"""Sets the prepaid_size of this ShowInstanceStorageInfoResponse.

        **参数解释**：  包年/包月购买的存储空间大小，单位是GB。  **取值范围**：  大于0。

        :param prepaid_size: The prepaid_size of this ShowInstanceStorageInfoResponse.
        :type prepaid_size: float
        """
        self._prepaid_size = prepaid_size

    @property
    def limit(self):
        r"""Gets the limit of this ShowInstanceStorageInfoResponse.

        **参数解释**：  实例可使用的存储空间上限，单位是GB。  **取值范围**：  大于0。

        :return: The limit of this ShowInstanceStorageInfoResponse.
        :rtype: float
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ShowInstanceStorageInfoResponse.

        **参数解释**：  实例可使用的存储空间上限，单位是GB。  **取值范围**：  大于0。

        :param limit: The limit of this ShowInstanceStorageInfoResponse.
        :type limit: float
        """
        self._limit = limit

    @property
    def type(self):
        r"""Gets the type of this ShowInstanceStorageInfoResponse.

        **参数解释**：  存储类型。  **取值范围**：  - POOL：DL6存储类型。 - STANDARDPOOL：DL5存储类型。

        :return: The type of this ShowInstanceStorageInfoResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ShowInstanceStorageInfoResponse.

        **参数解释**：  存储类型。  **取值范围**：  - POOL：DL6存储类型。 - STANDARDPOOL：DL5存储类型。

        :param type: The type of this ShowInstanceStorageInfoResponse.
        :type type: str
        """
        self._type = type

    def to_dict(self):
        import warnings
        warnings.warn("ShowInstanceStorageInfoResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowInstanceStorageInfoResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
