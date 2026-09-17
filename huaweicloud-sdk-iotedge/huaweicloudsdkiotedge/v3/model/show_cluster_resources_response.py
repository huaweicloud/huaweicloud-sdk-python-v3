# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowClusterResourcesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'count': 'int',
        'page_info': 'PageInfoDTO',
        'resource_list': 'list[ResourceDetail]'
    }

    attribute_map = {
        'count': 'count',
        'page_info': 'page_info',
        'resource_list': 'resource_list'
    }

    def __init__(self, count=None, page_info=None, resource_list=None):
        r"""ShowClusterResourcesResponse

        The model defined in huaweicloud sdk

        :param count: 总记录数
        :type count: int
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkiotedge.v3.PageInfoDTO`
        :param resource_list: 查询资源列表返回消息体
        :type resource_list: list[:class:`huaweicloudsdkiotedge.v3.ResourceDetail`]
        """
        
        super().__init__()

        self._count = None
        self._page_info = None
        self._resource_list = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if page_info is not None:
            self.page_info = page_info
        if resource_list is not None:
            self.resource_list = resource_list

    @property
    def count(self):
        r"""Gets the count of this ShowClusterResourcesResponse.

        总记录数

        :return: The count of this ShowClusterResourcesResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ShowClusterResourcesResponse.

        总记录数

        :param count: The count of this ShowClusterResourcesResponse.
        :type count: int
        """
        self._count = count

    @property
    def page_info(self):
        r"""Gets the page_info of this ShowClusterResourcesResponse.

        :return: The page_info of this ShowClusterResourcesResponse.
        :rtype: :class:`huaweicloudsdkiotedge.v3.PageInfoDTO`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        r"""Sets the page_info of this ShowClusterResourcesResponse.

        :param page_info: The page_info of this ShowClusterResourcesResponse.
        :type page_info: :class:`huaweicloudsdkiotedge.v3.PageInfoDTO`
        """
        self._page_info = page_info

    @property
    def resource_list(self):
        r"""Gets the resource_list of this ShowClusterResourcesResponse.

        查询资源列表返回消息体

        :return: The resource_list of this ShowClusterResourcesResponse.
        :rtype: list[:class:`huaweicloudsdkiotedge.v3.ResourceDetail`]
        """
        return self._resource_list

    @resource_list.setter
    def resource_list(self, resource_list):
        r"""Sets the resource_list of this ShowClusterResourcesResponse.

        查询资源列表返回消息体

        :param resource_list: The resource_list of this ShowClusterResourcesResponse.
        :type resource_list: list[:class:`huaweicloudsdkiotedge.v3.ResourceDetail`]
        """
        self._resource_list = resource_list

    def to_dict(self):
        import warnings
        warnings.warn("ShowClusterResourcesResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowClusterResourcesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
