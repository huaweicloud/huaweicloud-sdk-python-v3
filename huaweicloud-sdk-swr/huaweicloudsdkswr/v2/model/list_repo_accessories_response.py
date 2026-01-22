# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListRepoAccessoriesResponse(SdkResponse):

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
        'accessories': 'list[AccessoryListAccessories]'
    }

    attribute_map = {
        'total': 'total',
        'accessories': 'accessories'
    }

    def __init__(self, total=None, accessories=None):
        r"""ListRepoAccessoriesResponse

        The model defined in huaweicloud sdk

        :param total: 附件总数
        :type total: int
        :param accessories: 附件列表
        :type accessories: list[:class:`huaweicloudsdkswr.v2.AccessoryListAccessories`]
        """
        
        super().__init__()

        self._total = None
        self._accessories = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if accessories is not None:
            self.accessories = accessories

    @property
    def total(self):
        r"""Gets the total of this ListRepoAccessoriesResponse.

        附件总数

        :return: The total of this ListRepoAccessoriesResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListRepoAccessoriesResponse.

        附件总数

        :param total: The total of this ListRepoAccessoriesResponse.
        :type total: int
        """
        self._total = total

    @property
    def accessories(self):
        r"""Gets the accessories of this ListRepoAccessoriesResponse.

        附件列表

        :return: The accessories of this ListRepoAccessoriesResponse.
        :rtype: list[:class:`huaweicloudsdkswr.v2.AccessoryListAccessories`]
        """
        return self._accessories

    @accessories.setter
    def accessories(self, accessories):
        r"""Sets the accessories of this ListRepoAccessoriesResponse.

        附件列表

        :param accessories: The accessories of this ListRepoAccessoriesResponse.
        :type accessories: list[:class:`huaweicloudsdkswr.v2.AccessoryListAccessories`]
        """
        self._accessories = accessories

    def to_dict(self):
        import warnings
        warnings.warn("ListRepoAccessoriesResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListRepoAccessoriesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
