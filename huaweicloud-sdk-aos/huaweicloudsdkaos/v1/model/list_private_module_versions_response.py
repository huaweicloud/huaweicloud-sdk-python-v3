# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPrivateModuleVersionsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'versions': 'list[PrivateModuleVersionSummary]',
        'page_info': 'PageInfo'
    }

    attribute_map = {
        'versions': 'versions',
        'page_info': 'page_info'
    }

    def __init__(self, versions=None, page_info=None):
        r"""ListPrivateModuleVersionsResponse

        The model defined in huaweicloud sdk

        :param versions: 私有模块版本的列表。默认以创建时间升序排序。
        :type versions: list[:class:`huaweicloudsdkaos.v1.PrivateModuleVersionSummary`]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkaos.v1.PageInfo`
        """
        
        super(ListPrivateModuleVersionsResponse, self).__init__()

        self._versions = None
        self._page_info = None
        self.discriminator = None

        if versions is not None:
            self.versions = versions
        if page_info is not None:
            self.page_info = page_info

    @property
    def versions(self):
        r"""Gets the versions of this ListPrivateModuleVersionsResponse.

        私有模块版本的列表。默认以创建时间升序排序。

        :return: The versions of this ListPrivateModuleVersionsResponse.
        :rtype: list[:class:`huaweicloudsdkaos.v1.PrivateModuleVersionSummary`]
        """
        return self._versions

    @versions.setter
    def versions(self, versions):
        r"""Sets the versions of this ListPrivateModuleVersionsResponse.

        私有模块版本的列表。默认以创建时间升序排序。

        :param versions: The versions of this ListPrivateModuleVersionsResponse.
        :type versions: list[:class:`huaweicloudsdkaos.v1.PrivateModuleVersionSummary`]
        """
        self._versions = versions

    @property
    def page_info(self):
        r"""Gets the page_info of this ListPrivateModuleVersionsResponse.

        :return: The page_info of this ListPrivateModuleVersionsResponse.
        :rtype: :class:`huaweicloudsdkaos.v1.PageInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        r"""Sets the page_info of this ListPrivateModuleVersionsResponse.

        :param page_info: The page_info of this ListPrivateModuleVersionsResponse.
        :type page_info: :class:`huaweicloudsdkaos.v1.PageInfo`
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
        if not isinstance(other, ListPrivateModuleVersionsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
