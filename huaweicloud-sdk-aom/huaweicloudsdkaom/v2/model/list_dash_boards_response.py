# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDashBoardsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'page_size': 'int',
        'dashboards': 'list[Dashboard]'
    }

    attribute_map = {
        'page_size': 'page_size',
        'dashboards': 'dashboards'
    }

    def __init__(self, page_size=None, dashboards=None):
        r"""ListDashBoardsResponse

        The model defined in huaweicloud sdk

        :param page_size: 当前页大小。
        :type page_size: int
        :param dashboards: 仪表盘详情列表。
        :type dashboards: list[:class:`huaweicloudsdkaom.v2.Dashboard`]
        """
        
        super().__init__()

        self._page_size = None
        self._dashboards = None
        self.discriminator = None

        if page_size is not None:
            self.page_size = page_size
        if dashboards is not None:
            self.dashboards = dashboards

    @property
    def page_size(self):
        r"""Gets the page_size of this ListDashBoardsResponse.

        当前页大小。

        :return: The page_size of this ListDashBoardsResponse.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        r"""Sets the page_size of this ListDashBoardsResponse.

        当前页大小。

        :param page_size: The page_size of this ListDashBoardsResponse.
        :type page_size: int
        """
        self._page_size = page_size

    @property
    def dashboards(self):
        r"""Gets the dashboards of this ListDashBoardsResponse.

        仪表盘详情列表。

        :return: The dashboards of this ListDashBoardsResponse.
        :rtype: list[:class:`huaweicloudsdkaom.v2.Dashboard`]
        """
        return self._dashboards

    @dashboards.setter
    def dashboards(self, dashboards):
        r"""Sets the dashboards of this ListDashBoardsResponse.

        仪表盘详情列表。

        :param dashboards: The dashboards of this ListDashBoardsResponse.
        :type dashboards: list[:class:`huaweicloudsdkaom.v2.Dashboard`]
        """
        self._dashboards = dashboards

    def to_dict(self):
        import warnings
        warnings.warn("ListDashBoardsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListDashBoardsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
