# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTrustedKeySpaceResponse(SdkResponse):

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
        'keyspaces': 'list[ListTrustedKeySpaceResponseBodyKeyspaces]'
    }

    attribute_map = {
        'page_info': 'page_info',
        'keyspaces': 'keyspaces'
    }

    def __init__(self, page_info=None, keyspaces=None):
        r"""ListTrustedKeySpaceResponse

        The model defined in huaweicloud sdk

        :param page_info: 
        :type page_info: :class:`huaweicloudsdkkms.v2.ListAccessPointResponseBodyPageInfo`
        :param keyspaces: **参数解释：** 密钥空间列表 **取值范围：** 不涉及
        :type keyspaces: list[:class:`huaweicloudsdkkms.v2.ListTrustedKeySpaceResponseBodyKeyspaces`]
        """
        
        super().__init__()

        self._page_info = None
        self._keyspaces = None
        self.discriminator = None

        if page_info is not None:
            self.page_info = page_info
        if keyspaces is not None:
            self.keyspaces = keyspaces

    @property
    def page_info(self):
        r"""Gets the page_info of this ListTrustedKeySpaceResponse.

        :return: The page_info of this ListTrustedKeySpaceResponse.
        :rtype: :class:`huaweicloudsdkkms.v2.ListAccessPointResponseBodyPageInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        r"""Sets the page_info of this ListTrustedKeySpaceResponse.

        :param page_info: The page_info of this ListTrustedKeySpaceResponse.
        :type page_info: :class:`huaweicloudsdkkms.v2.ListAccessPointResponseBodyPageInfo`
        """
        self._page_info = page_info

    @property
    def keyspaces(self):
        r"""Gets the keyspaces of this ListTrustedKeySpaceResponse.

        **参数解释：** 密钥空间列表 **取值范围：** 不涉及

        :return: The keyspaces of this ListTrustedKeySpaceResponse.
        :rtype: list[:class:`huaweicloudsdkkms.v2.ListTrustedKeySpaceResponseBodyKeyspaces`]
        """
        return self._keyspaces

    @keyspaces.setter
    def keyspaces(self, keyspaces):
        r"""Sets the keyspaces of this ListTrustedKeySpaceResponse.

        **参数解释：** 密钥空间列表 **取值范围：** 不涉及

        :param keyspaces: The keyspaces of this ListTrustedKeySpaceResponse.
        :type keyspaces: list[:class:`huaweicloudsdkkms.v2.ListTrustedKeySpaceResponseBodyKeyspaces`]
        """
        self._keyspaces = keyspaces

    def to_dict(self):
        import warnings
        warnings.warn("ListTrustedKeySpaceResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListTrustedKeySpaceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
