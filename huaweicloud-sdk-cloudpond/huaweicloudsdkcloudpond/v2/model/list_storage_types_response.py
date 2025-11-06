# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListStorageTypesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'storage_types': 'list[StorageTypeOption]',
        'page_info': 'PageInfo'
    }

    attribute_map = {
        'storage_types': 'storage_types',
        'page_info': 'page_info'
    }

    def __init__(self, storage_types=None, page_info=None):
        r"""ListStorageTypesResponse

        The model defined in huaweicloud sdk

        :param storage_types: 存储类型列表
        :type storage_types: list[:class:`huaweicloudsdkcloudpond.v2.StorageTypeOption`]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkcloudpond.v2.PageInfo`
        """
        
        super().__init__()

        self._storage_types = None
        self._page_info = None
        self.discriminator = None

        if storage_types is not None:
            self.storage_types = storage_types
        if page_info is not None:
            self.page_info = page_info

    @property
    def storage_types(self):
        r"""Gets the storage_types of this ListStorageTypesResponse.

        存储类型列表

        :return: The storage_types of this ListStorageTypesResponse.
        :rtype: list[:class:`huaweicloudsdkcloudpond.v2.StorageTypeOption`]
        """
        return self._storage_types

    @storage_types.setter
    def storage_types(self, storage_types):
        r"""Sets the storage_types of this ListStorageTypesResponse.

        存储类型列表

        :param storage_types: The storage_types of this ListStorageTypesResponse.
        :type storage_types: list[:class:`huaweicloudsdkcloudpond.v2.StorageTypeOption`]
        """
        self._storage_types = storage_types

    @property
    def page_info(self):
        r"""Gets the page_info of this ListStorageTypesResponse.

        :return: The page_info of this ListStorageTypesResponse.
        :rtype: :class:`huaweicloudsdkcloudpond.v2.PageInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        r"""Sets the page_info of this ListStorageTypesResponse.

        :param page_info: The page_info of this ListStorageTypesResponse.
        :type page_info: :class:`huaweicloudsdkcloudpond.v2.PageInfo`
        """
        self._page_info = page_info

    def to_dict(self):
        import warnings
        warnings.warn("ListStorageTypesResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListStorageTypesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
