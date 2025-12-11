# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListIDcsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'idcs': 'list[IDc]',
        'page_info': 'PageInfo',
        'count': 'int'
    }

    attribute_map = {
        'idcs': 'idcs',
        'page_info': 'page_info',
        'count': 'count'
    }

    def __init__(self, idcs=None, page_info=None, count=None):
        r"""ListIDcsResponse

        The model defined in huaweicloud sdk

        :param idcs: 
        :type idcs: list[:class:`huaweicloudsdkclouddc.v1.IDc`]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkclouddc.v1.PageInfo`
        :param count: 机房总数
        :type count: int
        """
        
        super().__init__()

        self._idcs = None
        self._page_info = None
        self._count = None
        self.discriminator = None

        if idcs is not None:
            self.idcs = idcs
        if page_info is not None:
            self.page_info = page_info
        if count is not None:
            self.count = count

    @property
    def idcs(self):
        r"""Gets the idcs of this ListIDcsResponse.

        :return: The idcs of this ListIDcsResponse.
        :rtype: list[:class:`huaweicloudsdkclouddc.v1.IDc`]
        """
        return self._idcs

    @idcs.setter
    def idcs(self, idcs):
        r"""Sets the idcs of this ListIDcsResponse.

        :param idcs: The idcs of this ListIDcsResponse.
        :type idcs: list[:class:`huaweicloudsdkclouddc.v1.IDc`]
        """
        self._idcs = idcs

    @property
    def page_info(self):
        r"""Gets the page_info of this ListIDcsResponse.

        :return: The page_info of this ListIDcsResponse.
        :rtype: :class:`huaweicloudsdkclouddc.v1.PageInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        r"""Sets the page_info of this ListIDcsResponse.

        :param page_info: The page_info of this ListIDcsResponse.
        :type page_info: :class:`huaweicloudsdkclouddc.v1.PageInfo`
        """
        self._page_info = page_info

    @property
    def count(self):
        r"""Gets the count of this ListIDcsResponse.

        机房总数

        :return: The count of this ListIDcsResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ListIDcsResponse.

        机房总数

        :param count: The count of this ListIDcsResponse.
        :type count: int
        """
        self._count = count

    def to_dict(self):
        import warnings
        warnings.warn("ListIDcsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListIDcsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
