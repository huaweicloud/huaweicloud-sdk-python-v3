# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListResourceSpecsPriceResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'page_info': 'ResourceSpecsPricePageInfo',
        'region_code': 'str',
        'resource_spec_infos': 'list[ResourceSpecInfo]'
    }

    attribute_map = {
        'page_info': 'page_info',
        'region_code': 'region_code',
        'resource_spec_infos': 'resource_spec_infos'
    }

    def __init__(self, page_info=None, region_code=None, resource_spec_infos=None):
        r"""ListResourceSpecsPriceResponse

        The model defined in huaweicloud sdk

        :param page_info: 
        :type page_info: :class:`huaweicloudsdkbssintl.v2.ResourceSpecsPricePageInfo`
        :param region_code: 云服务区编码
        :type region_code: str
        :param resource_spec_infos: 资源规格列表
        :type resource_spec_infos: list[:class:`huaweicloudsdkbssintl.v2.ResourceSpecInfo`]
        """
        
        super().__init__()

        self._page_info = None
        self._region_code = None
        self._resource_spec_infos = None
        self.discriminator = None

        if page_info is not None:
            self.page_info = page_info
        if region_code is not None:
            self.region_code = region_code
        if resource_spec_infos is not None:
            self.resource_spec_infos = resource_spec_infos

    @property
    def page_info(self):
        r"""Gets the page_info of this ListResourceSpecsPriceResponse.

        :return: The page_info of this ListResourceSpecsPriceResponse.
        :rtype: :class:`huaweicloudsdkbssintl.v2.ResourceSpecsPricePageInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        r"""Sets the page_info of this ListResourceSpecsPriceResponse.

        :param page_info: The page_info of this ListResourceSpecsPriceResponse.
        :type page_info: :class:`huaweicloudsdkbssintl.v2.ResourceSpecsPricePageInfo`
        """
        self._page_info = page_info

    @property
    def region_code(self):
        r"""Gets the region_code of this ListResourceSpecsPriceResponse.

        云服务区编码

        :return: The region_code of this ListResourceSpecsPriceResponse.
        :rtype: str
        """
        return self._region_code

    @region_code.setter
    def region_code(self, region_code):
        r"""Sets the region_code of this ListResourceSpecsPriceResponse.

        云服务区编码

        :param region_code: The region_code of this ListResourceSpecsPriceResponse.
        :type region_code: str
        """
        self._region_code = region_code

    @property
    def resource_spec_infos(self):
        r"""Gets the resource_spec_infos of this ListResourceSpecsPriceResponse.

        资源规格列表

        :return: The resource_spec_infos of this ListResourceSpecsPriceResponse.
        :rtype: list[:class:`huaweicloudsdkbssintl.v2.ResourceSpecInfo`]
        """
        return self._resource_spec_infos

    @resource_spec_infos.setter
    def resource_spec_infos(self, resource_spec_infos):
        r"""Sets the resource_spec_infos of this ListResourceSpecsPriceResponse.

        资源规格列表

        :param resource_spec_infos: The resource_spec_infos of this ListResourceSpecsPriceResponse.
        :type resource_spec_infos: list[:class:`huaweicloudsdkbssintl.v2.ResourceSpecInfo`]
        """
        self._resource_spec_infos = resource_spec_infos

    def to_dict(self):
        import warnings
        warnings.warn("ListResourceSpecsPriceResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListResourceSpecsPriceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
