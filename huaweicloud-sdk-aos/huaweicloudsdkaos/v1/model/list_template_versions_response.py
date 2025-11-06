# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTemplateVersionsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'versions': 'list[TemplateVersion]',
        'page_info': 'PageInfo'
    }

    attribute_map = {
        'versions': 'versions',
        'page_info': 'page_info'
    }

    def __init__(self, versions=None, page_info=None):
        r"""ListTemplateVersionsResponse

        The model defined in huaweicloud sdk

        :param versions: 模板版本列表
        :type versions: list[:class:`huaweicloudsdkaos.v1.TemplateVersion`]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkaos.v1.PageInfo`
        """
        
        super().__init__()

        self._versions = None
        self._page_info = None
        self.discriminator = None

        if versions is not None:
            self.versions = versions
        if page_info is not None:
            self.page_info = page_info

    @property
    def versions(self):
        r"""Gets the versions of this ListTemplateVersionsResponse.

        模板版本列表

        :return: The versions of this ListTemplateVersionsResponse.
        :rtype: list[:class:`huaweicloudsdkaos.v1.TemplateVersion`]
        """
        return self._versions

    @versions.setter
    def versions(self, versions):
        r"""Sets the versions of this ListTemplateVersionsResponse.

        模板版本列表

        :param versions: The versions of this ListTemplateVersionsResponse.
        :type versions: list[:class:`huaweicloudsdkaos.v1.TemplateVersion`]
        """
        self._versions = versions

    @property
    def page_info(self):
        r"""Gets the page_info of this ListTemplateVersionsResponse.

        :return: The page_info of this ListTemplateVersionsResponse.
        :rtype: :class:`huaweicloudsdkaos.v1.PageInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        r"""Sets the page_info of this ListTemplateVersionsResponse.

        :param page_info: The page_info of this ListTemplateVersionsResponse.
        :type page_info: :class:`huaweicloudsdkaos.v1.PageInfo`
        """
        self._page_info = page_info

    def to_dict(self):
        import warnings
        warnings.warn("ListTemplateVersionsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListTemplateVersionsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
