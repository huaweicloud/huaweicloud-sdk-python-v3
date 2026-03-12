# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListThumbnailInfoResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total': 'int',
        'thumbnails': 'list[QueryThumbnailInfo]'
    }

    attribute_map = {
        'total': 'total',
        'thumbnails': 'thumbnails'
    }

    def __init__(self, total=None, thumbnails=None):
        r"""ListThumbnailInfoResponse

        The model defined in huaweicloud sdk

        :param total: 截图结果总数 
        :type total: int
        :param thumbnails: 截图结果列表 
        :type thumbnails: list[:class:`huaweicloudsdkvod.v1.QueryThumbnailInfo`]
        """
        
        super().__init__()

        self._total = None
        self._thumbnails = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if thumbnails is not None:
            self.thumbnails = thumbnails

    @property
    def total(self):
        r"""Gets the total of this ListThumbnailInfoResponse.

        截图结果总数 

        :return: The total of this ListThumbnailInfoResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListThumbnailInfoResponse.

        截图结果总数 

        :param total: The total of this ListThumbnailInfoResponse.
        :type total: int
        """
        self._total = total

    @property
    def thumbnails(self):
        r"""Gets the thumbnails of this ListThumbnailInfoResponse.

        截图结果列表 

        :return: The thumbnails of this ListThumbnailInfoResponse.
        :rtype: list[:class:`huaweicloudsdkvod.v1.QueryThumbnailInfo`]
        """
        return self._thumbnails

    @thumbnails.setter
    def thumbnails(self, thumbnails):
        r"""Sets the thumbnails of this ListThumbnailInfoResponse.

        截图结果列表 

        :param thumbnails: The thumbnails of this ListThumbnailInfoResponse.
        :type thumbnails: list[:class:`huaweicloudsdkvod.v1.QueryThumbnailInfo`]
        """
        self._thumbnails = thumbnails

    def to_dict(self):
        import warnings
        warnings.warn("ListThumbnailInfoResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListThumbnailInfoResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
