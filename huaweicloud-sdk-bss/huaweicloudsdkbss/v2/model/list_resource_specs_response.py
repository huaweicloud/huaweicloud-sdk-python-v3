# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListResourceSpecsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'page_info': 'PageInfo',
        'cloud_service_basics': 'list[CloudServiceBasic]'
    }

    attribute_map = {
        'page_info': 'page_info',
        'cloud_service_basics': 'cloud_service_basics'
    }

    def __init__(self, page_info=None, cloud_service_basics=None):
        r"""ListResourceSpecsResponse

        The model defined in huaweicloud sdk

        :param page_info: 
        :type page_info: :class:`huaweicloudsdkbss.v2.PageInfo`
        :param cloud_service_basics: |参数名称：资源规格信息列表| |参数的约束及描述：资源规格信息列表|
        :type cloud_service_basics: list[:class:`huaweicloudsdkbss.v2.CloudServiceBasic`]
        """
        
        super().__init__()

        self._page_info = None
        self._cloud_service_basics = None
        self.discriminator = None

        if page_info is not None:
            self.page_info = page_info
        if cloud_service_basics is not None:
            self.cloud_service_basics = cloud_service_basics

    @property
    def page_info(self):
        r"""Gets the page_info of this ListResourceSpecsResponse.

        :return: The page_info of this ListResourceSpecsResponse.
        :rtype: :class:`huaweicloudsdkbss.v2.PageInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        r"""Sets the page_info of this ListResourceSpecsResponse.

        :param page_info: The page_info of this ListResourceSpecsResponse.
        :type page_info: :class:`huaweicloudsdkbss.v2.PageInfo`
        """
        self._page_info = page_info

    @property
    def cloud_service_basics(self):
        r"""Gets the cloud_service_basics of this ListResourceSpecsResponse.

        |参数名称：资源规格信息列表| |参数的约束及描述：资源规格信息列表|

        :return: The cloud_service_basics of this ListResourceSpecsResponse.
        :rtype: list[:class:`huaweicloudsdkbss.v2.CloudServiceBasic`]
        """
        return self._cloud_service_basics

    @cloud_service_basics.setter
    def cloud_service_basics(self, cloud_service_basics):
        r"""Sets the cloud_service_basics of this ListResourceSpecsResponse.

        |参数名称：资源规格信息列表| |参数的约束及描述：资源规格信息列表|

        :param cloud_service_basics: The cloud_service_basics of this ListResourceSpecsResponse.
        :type cloud_service_basics: list[:class:`huaweicloudsdkbss.v2.CloudServiceBasic`]
        """
        self._cloud_service_basics = cloud_service_basics

    def to_dict(self):
        import warnings
        warnings.warn("ListResourceSpecsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListResourceSpecsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
