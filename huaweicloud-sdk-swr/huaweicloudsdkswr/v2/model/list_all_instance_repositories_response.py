# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAllInstanceRepositoriesResponse(SdkResponse):

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
        'repositories': 'list[InstanceRepository]'
    }

    attribute_map = {
        'page_info': 'page_info',
        'repositories': 'repositories'
    }

    def __init__(self, page_info=None, repositories=None):
        r"""ListAllInstanceRepositoriesResponse

        The model defined in huaweicloud sdk

        :param page_info: 
        :type page_info: :class:`huaweicloudsdkswr.v2.PageInfo`
        :param repositories: 仓库列表详情
        :type repositories: list[:class:`huaweicloudsdkswr.v2.InstanceRepository`]
        """
        
        super().__init__()

        self._page_info = None
        self._repositories = None
        self.discriminator = None

        if page_info is not None:
            self.page_info = page_info
        if repositories is not None:
            self.repositories = repositories

    @property
    def page_info(self):
        r"""Gets the page_info of this ListAllInstanceRepositoriesResponse.

        :return: The page_info of this ListAllInstanceRepositoriesResponse.
        :rtype: :class:`huaweicloudsdkswr.v2.PageInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        r"""Sets the page_info of this ListAllInstanceRepositoriesResponse.

        :param page_info: The page_info of this ListAllInstanceRepositoriesResponse.
        :type page_info: :class:`huaweicloudsdkswr.v2.PageInfo`
        """
        self._page_info = page_info

    @property
    def repositories(self):
        r"""Gets the repositories of this ListAllInstanceRepositoriesResponse.

        仓库列表详情

        :return: The repositories of this ListAllInstanceRepositoriesResponse.
        :rtype: list[:class:`huaweicloudsdkswr.v2.InstanceRepository`]
        """
        return self._repositories

    @repositories.setter
    def repositories(self, repositories):
        r"""Sets the repositories of this ListAllInstanceRepositoriesResponse.

        仓库列表详情

        :param repositories: The repositories of this ListAllInstanceRepositoriesResponse.
        :type repositories: list[:class:`huaweicloudsdkswr.v2.InstanceRepository`]
        """
        self._repositories = repositories

    def to_dict(self):
        import warnings
        warnings.warn("ListAllInstanceRepositoriesResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListAllInstanceRepositoriesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
