# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTenantUserConfigurationResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'my_collections': 'list[CollectionInfo]',
        'x_request_id': 'str'
    }

    attribute_map = {
        'my_collections': 'my_collections',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, my_collections=None, x_request_id=None):
        r"""ShowTenantUserConfigurationResponse

        The model defined in huaweicloud sdk

        :param my_collections: 我的收藏列表
        :type my_collections: list[:class:`huaweicloudsdkmetastudio.v1.CollectionInfo`]
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super().__init__()

        self._my_collections = None
        self._x_request_id = None
        self.discriminator = None

        if my_collections is not None:
            self.my_collections = my_collections
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def my_collections(self):
        r"""Gets the my_collections of this ShowTenantUserConfigurationResponse.

        我的收藏列表

        :return: The my_collections of this ShowTenantUserConfigurationResponse.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.CollectionInfo`]
        """
        return self._my_collections

    @my_collections.setter
    def my_collections(self, my_collections):
        r"""Sets the my_collections of this ShowTenantUserConfigurationResponse.

        我的收藏列表

        :param my_collections: The my_collections of this ShowTenantUserConfigurationResponse.
        :type my_collections: list[:class:`huaweicloudsdkmetastudio.v1.CollectionInfo`]
        """
        self._my_collections = my_collections

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this ShowTenantUserConfigurationResponse.

        :return: The x_request_id of this ShowTenantUserConfigurationResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this ShowTenantUserConfigurationResponse.

        :param x_request_id: The x_request_id of this ShowTenantUserConfigurationResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

    def to_dict(self):
        import warnings
        warnings.warn("ShowTenantUserConfigurationResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowTenantUserConfigurationResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
