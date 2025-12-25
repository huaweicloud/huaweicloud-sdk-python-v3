# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowGroupSummaryResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'groups': 'list[GroupSummary]',
        'page_info': 'PageInfo'
    }

    attribute_map = {
        'groups': 'groups',
        'page_info': 'page_info'
    }

    def __init__(self, groups=None, page_info=None):
        r"""ShowGroupSummaryResponse

        The model defined in huaweicloud sdk

        :param groups: 用户组列表。
        :type groups: list[:class:`huaweicloudsdkiam.v5.GroupSummary`]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkiam.v5.PageInfo`
        """
        
        super().__init__()

        self._groups = None
        self._page_info = None
        self.discriminator = None

        if groups is not None:
            self.groups = groups
        if page_info is not None:
            self.page_info = page_info

    @property
    def groups(self):
        r"""Gets the groups of this ShowGroupSummaryResponse.

        用户组列表。

        :return: The groups of this ShowGroupSummaryResponse.
        :rtype: list[:class:`huaweicloudsdkiam.v5.GroupSummary`]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        r"""Sets the groups of this ShowGroupSummaryResponse.

        用户组列表。

        :param groups: The groups of this ShowGroupSummaryResponse.
        :type groups: list[:class:`huaweicloudsdkiam.v5.GroupSummary`]
        """
        self._groups = groups

    @property
    def page_info(self):
        r"""Gets the page_info of this ShowGroupSummaryResponse.

        :return: The page_info of this ShowGroupSummaryResponse.
        :rtype: :class:`huaweicloudsdkiam.v5.PageInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        r"""Sets the page_info of this ShowGroupSummaryResponse.

        :param page_info: The page_info of this ShowGroupSummaryResponse.
        :type page_info: :class:`huaweicloudsdkiam.v5.PageInfo`
        """
        self._page_info = page_info

    def to_dict(self):
        import warnings
        warnings.warn("ShowGroupSummaryResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowGroupSummaryResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
