# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListResourceAssociationsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'request_id': 'str',
        'resource_associations': 'list[ResourceAssociation]',
        'page_info': 'PageInfo'
    }

    attribute_map = {
        'request_id': 'request_id',
        'resource_associations': 'resource_associations',
        'page_info': 'page_info'
    }

    def __init__(self, request_id=None, resource_associations=None, page_info=None):
        r"""ListResourceAssociationsResponse

        The model defined in huaweicloud sdk

        :param request_id: **参数解释**： 请求ID。 **取值范围**： 不涉及。
        :type request_id: str
        :param resource_associations: **参数解释**： 资源关联实例信息列表。 **取值范围**： 不涉及。
        :type resource_associations: list[:class:`huaweicloudsdkvpc.v3.ResourceAssociation`]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkvpc.v3.PageInfo`
        """
        
        super().__init__()

        self._request_id = None
        self._resource_associations = None
        self._page_info = None
        self.discriminator = None

        if request_id is not None:
            self.request_id = request_id
        if resource_associations is not None:
            self.resource_associations = resource_associations
        if page_info is not None:
            self.page_info = page_info

    @property
    def request_id(self):
        r"""Gets the request_id of this ListResourceAssociationsResponse.

        **参数解释**： 请求ID。 **取值范围**： 不涉及。

        :return: The request_id of this ListResourceAssociationsResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        r"""Sets the request_id of this ListResourceAssociationsResponse.

        **参数解释**： 请求ID。 **取值范围**： 不涉及。

        :param request_id: The request_id of this ListResourceAssociationsResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def resource_associations(self):
        r"""Gets the resource_associations of this ListResourceAssociationsResponse.

        **参数解释**： 资源关联实例信息列表。 **取值范围**： 不涉及。

        :return: The resource_associations of this ListResourceAssociationsResponse.
        :rtype: list[:class:`huaweicloudsdkvpc.v3.ResourceAssociation`]
        """
        return self._resource_associations

    @resource_associations.setter
    def resource_associations(self, resource_associations):
        r"""Sets the resource_associations of this ListResourceAssociationsResponse.

        **参数解释**： 资源关联实例信息列表。 **取值范围**： 不涉及。

        :param resource_associations: The resource_associations of this ListResourceAssociationsResponse.
        :type resource_associations: list[:class:`huaweicloudsdkvpc.v3.ResourceAssociation`]
        """
        self._resource_associations = resource_associations

    @property
    def page_info(self):
        r"""Gets the page_info of this ListResourceAssociationsResponse.

        :return: The page_info of this ListResourceAssociationsResponse.
        :rtype: :class:`huaweicloudsdkvpc.v3.PageInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        r"""Sets the page_info of this ListResourceAssociationsResponse.

        :param page_info: The page_info of this ListResourceAssociationsResponse.
        :type page_info: :class:`huaweicloudsdkvpc.v3.PageInfo`
        """
        self._page_info = page_info

    def to_dict(self):
        import warnings
        warnings.warn("ListResourceAssociationsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListResourceAssociationsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
