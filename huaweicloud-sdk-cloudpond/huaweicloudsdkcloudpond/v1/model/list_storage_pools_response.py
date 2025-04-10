# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListStoragePoolsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'storage_pools': 'list[StoragePool]',
        'page_info': 'PageInfo'
    }

    attribute_map = {
        'storage_pools': 'storage_pools',
        'page_info': 'page_info'
    }

    def __init__(self, storage_pools=None, page_info=None):
        r"""ListStoragePoolsResponse

        The model defined in huaweicloud sdk

        :param storage_pools: 存储池列表
        :type storage_pools: list[:class:`huaweicloudsdkcloudpond.v1.StoragePool`]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkcloudpond.v1.PageInfo`
        """
        
        super(ListStoragePoolsResponse, self).__init__()

        self._storage_pools = None
        self._page_info = None
        self.discriminator = None

        if storage_pools is not None:
            self.storage_pools = storage_pools
        if page_info is not None:
            self.page_info = page_info

    @property
    def storage_pools(self):
        r"""Gets the storage_pools of this ListStoragePoolsResponse.

        存储池列表

        :return: The storage_pools of this ListStoragePoolsResponse.
        :rtype: list[:class:`huaweicloudsdkcloudpond.v1.StoragePool`]
        """
        return self._storage_pools

    @storage_pools.setter
    def storage_pools(self, storage_pools):
        r"""Sets the storage_pools of this ListStoragePoolsResponse.

        存储池列表

        :param storage_pools: The storage_pools of this ListStoragePoolsResponse.
        :type storage_pools: list[:class:`huaweicloudsdkcloudpond.v1.StoragePool`]
        """
        self._storage_pools = storage_pools

    @property
    def page_info(self):
        r"""Gets the page_info of this ListStoragePoolsResponse.

        :return: The page_info of this ListStoragePoolsResponse.
        :rtype: :class:`huaweicloudsdkcloudpond.v1.PageInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        r"""Sets the page_info of this ListStoragePoolsResponse.

        :param page_info: The page_info of this ListStoragePoolsResponse.
        :type page_info: :class:`huaweicloudsdkcloudpond.v1.PageInfo`
        """
        self._page_info = page_info

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListStoragePoolsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
