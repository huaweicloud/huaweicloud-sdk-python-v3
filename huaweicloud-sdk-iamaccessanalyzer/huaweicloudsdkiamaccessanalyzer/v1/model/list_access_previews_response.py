# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAccessPreviewsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'access_previews': 'list[AccessPreviewSummary]',
        'page_info': 'PageInfo'
    }

    attribute_map = {
        'access_previews': 'access_previews',
        'page_info': 'page_info'
    }

    def __init__(self, access_previews=None, page_info=None):
        """ListAccessPreviewsResponse

        The model defined in huaweicloud sdk

        :param access_previews: 访问预览列表。
        :type access_previews: list[:class:`huaweicloudsdkiamaccessanalyzer.v1.AccessPreviewSummary`]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkiamaccessanalyzer.v1.PageInfo`
        """
        
        super(ListAccessPreviewsResponse, self).__init__()

        self._access_previews = None
        self._page_info = None
        self.discriminator = None

        if access_previews is not None:
            self.access_previews = access_previews
        if page_info is not None:
            self.page_info = page_info

    @property
    def access_previews(self):
        """Gets the access_previews of this ListAccessPreviewsResponse.

        访问预览列表。

        :return: The access_previews of this ListAccessPreviewsResponse.
        :rtype: list[:class:`huaweicloudsdkiamaccessanalyzer.v1.AccessPreviewSummary`]
        """
        return self._access_previews

    @access_previews.setter
    def access_previews(self, access_previews):
        """Sets the access_previews of this ListAccessPreviewsResponse.

        访问预览列表。

        :param access_previews: The access_previews of this ListAccessPreviewsResponse.
        :type access_previews: list[:class:`huaweicloudsdkiamaccessanalyzer.v1.AccessPreviewSummary`]
        """
        self._access_previews = access_previews

    @property
    def page_info(self):
        """Gets the page_info of this ListAccessPreviewsResponse.

        :return: The page_info of this ListAccessPreviewsResponse.
        :rtype: :class:`huaweicloudsdkiamaccessanalyzer.v1.PageInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        """Sets the page_info of this ListAccessPreviewsResponse.

        :param page_info: The page_info of this ListAccessPreviewsResponse.
        :type page_info: :class:`huaweicloudsdkiamaccessanalyzer.v1.PageInfo`
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
        if not isinstance(other, ListAccessPreviewsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
