# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SearchResourceShareAssociationsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_share_associations': 'list[ResourceShareAssociation]',
        'page_info': 'PageInfo'
    }

    attribute_map = {
        'resource_share_associations': 'resource_share_associations',
        'page_info': 'page_info'
    }

    def __init__(self, resource_share_associations=None, page_info=None):
        r"""SearchResourceShareAssociationsResponse

        The model defined in huaweicloud sdk

        :param resource_share_associations: 绑定的详细信息列表。
        :type resource_share_associations: list[:class:`huaweicloudsdkram.v1.ResourceShareAssociation`]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkram.v1.PageInfo`
        """
        
        super(SearchResourceShareAssociationsResponse, self).__init__()

        self._resource_share_associations = None
        self._page_info = None
        self.discriminator = None

        if resource_share_associations is not None:
            self.resource_share_associations = resource_share_associations
        if page_info is not None:
            self.page_info = page_info

    @property
    def resource_share_associations(self):
        r"""Gets the resource_share_associations of this SearchResourceShareAssociationsResponse.

        绑定的详细信息列表。

        :return: The resource_share_associations of this SearchResourceShareAssociationsResponse.
        :rtype: list[:class:`huaweicloudsdkram.v1.ResourceShareAssociation`]
        """
        return self._resource_share_associations

    @resource_share_associations.setter
    def resource_share_associations(self, resource_share_associations):
        r"""Sets the resource_share_associations of this SearchResourceShareAssociationsResponse.

        绑定的详细信息列表。

        :param resource_share_associations: The resource_share_associations of this SearchResourceShareAssociationsResponse.
        :type resource_share_associations: list[:class:`huaweicloudsdkram.v1.ResourceShareAssociation`]
        """
        self._resource_share_associations = resource_share_associations

    @property
    def page_info(self):
        r"""Gets the page_info of this SearchResourceShareAssociationsResponse.

        :return: The page_info of this SearchResourceShareAssociationsResponse.
        :rtype: :class:`huaweicloudsdkram.v1.PageInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        r"""Sets the page_info of this SearchResourceShareAssociationsResponse.

        :param page_info: The page_info of this SearchResourceShareAssociationsResponse.
        :type page_info: :class:`huaweicloudsdkram.v1.PageInfo`
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
        if not isinstance(other, SearchResourceShareAssociationsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
