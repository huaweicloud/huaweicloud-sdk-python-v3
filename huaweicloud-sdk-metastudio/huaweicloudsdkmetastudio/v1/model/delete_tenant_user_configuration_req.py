# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteTenantUserConfigurationReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'my_collections': 'list[CollectionInfo]'
    }

    attribute_map = {
        'my_collections': 'my_collections'
    }

    def __init__(self, my_collections=None):
        r"""DeleteTenantUserConfigurationReq

        The model defined in huaweicloud sdk

        :param my_collections: 我的收藏列表
        :type my_collections: list[:class:`huaweicloudsdkmetastudio.v1.CollectionInfo`]
        """
        
        

        self._my_collections = None
        self.discriminator = None

        if my_collections is not None:
            self.my_collections = my_collections

    @property
    def my_collections(self):
        r"""Gets the my_collections of this DeleteTenantUserConfigurationReq.

        我的收藏列表

        :return: The my_collections of this DeleteTenantUserConfigurationReq.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.CollectionInfo`]
        """
        return self._my_collections

    @my_collections.setter
    def my_collections(self, my_collections):
        r"""Sets the my_collections of this DeleteTenantUserConfigurationReq.

        我的收藏列表

        :param my_collections: The my_collections of this DeleteTenantUserConfigurationReq.
        :type my_collections: list[:class:`huaweicloudsdkmetastudio.v1.CollectionInfo`]
        """
        self._my_collections = my_collections

    def to_dict(self):
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
        if not isinstance(other, DeleteTenantUserConfigurationReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
