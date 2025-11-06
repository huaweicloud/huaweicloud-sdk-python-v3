# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListStorageGearsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'storage_gears': 'list[StorageGearV2]',
        'page_info': 'PageInfo'
    }

    attribute_map = {
        'storage_gears': 'storage_gears',
        'page_info': 'page_info'
    }

    def __init__(self, storage_gears=None, page_info=None):
        r"""ListStorageGearsResponse

        The model defined in huaweicloud sdk

        :param storage_gears: 支持的存储档位列表
        :type storage_gears: list[:class:`huaweicloudsdkcloudpond.v2.StorageGearV2`]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkcloudpond.v2.PageInfo`
        """
        
        super().__init__()

        self._storage_gears = None
        self._page_info = None
        self.discriminator = None

        if storage_gears is not None:
            self.storage_gears = storage_gears
        if page_info is not None:
            self.page_info = page_info

    @property
    def storage_gears(self):
        r"""Gets the storage_gears of this ListStorageGearsResponse.

        支持的存储档位列表

        :return: The storage_gears of this ListStorageGearsResponse.
        :rtype: list[:class:`huaweicloudsdkcloudpond.v2.StorageGearV2`]
        """
        return self._storage_gears

    @storage_gears.setter
    def storage_gears(self, storage_gears):
        r"""Sets the storage_gears of this ListStorageGearsResponse.

        支持的存储档位列表

        :param storage_gears: The storage_gears of this ListStorageGearsResponse.
        :type storage_gears: list[:class:`huaweicloudsdkcloudpond.v2.StorageGearV2`]
        """
        self._storage_gears = storage_gears

    @property
    def page_info(self):
        r"""Gets the page_info of this ListStorageGearsResponse.

        :return: The page_info of this ListStorageGearsResponse.
        :rtype: :class:`huaweicloudsdkcloudpond.v2.PageInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        r"""Sets the page_info of this ListStorageGearsResponse.

        :param page_info: The page_info of this ListStorageGearsResponse.
        :type page_info: :class:`huaweicloudsdkcloudpond.v2.PageInfo`
        """
        self._page_info = page_info

    def to_dict(self):
        import warnings
        warnings.warn("ListStorageGearsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListStorageGearsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
