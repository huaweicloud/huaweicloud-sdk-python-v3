# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAccessPointResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'page_info': 'ListAccessPointResponseBodyPageInfo',
        'access_points': 'list[ListAccessPointResponseBodyAccessPoints]'
    }

    attribute_map = {
        'page_info': 'page_info',
        'access_points': 'access_points'
    }

    def __init__(self, page_info=None, access_points=None):
        r"""ListAccessPointResponse

        The model defined in huaweicloud sdk

        :param page_info: 
        :type page_info: :class:`huaweicloudsdkkms.v2.ListAccessPointResponseBodyPageInfo`
        :param access_points: **参数解释：** 接入点列表 **取值范围：** 不涉及
        :type access_points: list[:class:`huaweicloudsdkkms.v2.ListAccessPointResponseBodyAccessPoints`]
        """
        
        super().__init__()

        self._page_info = None
        self._access_points = None
        self.discriminator = None

        if page_info is not None:
            self.page_info = page_info
        if access_points is not None:
            self.access_points = access_points

    @property
    def page_info(self):
        r"""Gets the page_info of this ListAccessPointResponse.

        :return: The page_info of this ListAccessPointResponse.
        :rtype: :class:`huaweicloudsdkkms.v2.ListAccessPointResponseBodyPageInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        r"""Sets the page_info of this ListAccessPointResponse.

        :param page_info: The page_info of this ListAccessPointResponse.
        :type page_info: :class:`huaweicloudsdkkms.v2.ListAccessPointResponseBodyPageInfo`
        """
        self._page_info = page_info

    @property
    def access_points(self):
        r"""Gets the access_points of this ListAccessPointResponse.

        **参数解释：** 接入点列表 **取值范围：** 不涉及

        :return: The access_points of this ListAccessPointResponse.
        :rtype: list[:class:`huaweicloudsdkkms.v2.ListAccessPointResponseBodyAccessPoints`]
        """
        return self._access_points

    @access_points.setter
    def access_points(self, access_points):
        r"""Sets the access_points of this ListAccessPointResponse.

        **参数解释：** 接入点列表 **取值范围：** 不涉及

        :param access_points: The access_points of this ListAccessPointResponse.
        :type access_points: list[:class:`huaweicloudsdkkms.v2.ListAccessPointResponseBodyAccessPoints`]
        """
        self._access_points = access_points

    def to_dict(self):
        import warnings
        warnings.warn("ListAccessPointResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListAccessPointResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
