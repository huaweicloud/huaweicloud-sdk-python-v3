# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListResourceConfigurationsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_configurations': 'list[ResourceConfiguration]',
        'page_info': 'PageInfo'
    }

    attribute_map = {
        'resource_configurations': 'resource_configurations',
        'page_info': 'page_info'
    }

    def __init__(self, resource_configurations=None, page_info=None):
        r"""ListResourceConfigurationsResponse

        The model defined in huaweicloud sdk

        :param resource_configurations: 提权访问中的资源配置。
        :type resource_configurations: list[:class:`huaweicloudsdkiamaccessanalyzer.v1.ResourceConfiguration`]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkiamaccessanalyzer.v1.PageInfo`
        """
        
        super().__init__()

        self._resource_configurations = None
        self._page_info = None
        self.discriminator = None

        if resource_configurations is not None:
            self.resource_configurations = resource_configurations
        if page_info is not None:
            self.page_info = page_info

    @property
    def resource_configurations(self):
        r"""Gets the resource_configurations of this ListResourceConfigurationsResponse.

        提权访问中的资源配置。

        :return: The resource_configurations of this ListResourceConfigurationsResponse.
        :rtype: list[:class:`huaweicloudsdkiamaccessanalyzer.v1.ResourceConfiguration`]
        """
        return self._resource_configurations

    @resource_configurations.setter
    def resource_configurations(self, resource_configurations):
        r"""Sets the resource_configurations of this ListResourceConfigurationsResponse.

        提权访问中的资源配置。

        :param resource_configurations: The resource_configurations of this ListResourceConfigurationsResponse.
        :type resource_configurations: list[:class:`huaweicloudsdkiamaccessanalyzer.v1.ResourceConfiguration`]
        """
        self._resource_configurations = resource_configurations

    @property
    def page_info(self):
        r"""Gets the page_info of this ListResourceConfigurationsResponse.

        :return: The page_info of this ListResourceConfigurationsResponse.
        :rtype: :class:`huaweicloudsdkiamaccessanalyzer.v1.PageInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        r"""Sets the page_info of this ListResourceConfigurationsResponse.

        :param page_info: The page_info of this ListResourceConfigurationsResponse.
        :type page_info: :class:`huaweicloudsdkiamaccessanalyzer.v1.PageInfo`
        """
        self._page_info = page_info

    def to_dict(self):
        import warnings
        warnings.warn("ListResourceConfigurationsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListResourceConfigurationsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
