# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSecuritySensitiveDataDetailsResponse(SdkResponse):

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
        'content': 'list[SensitiveDataDTO]',
        'page_info': 'PageInfo'
    }

    attribute_map = {
        'total': 'total',
        'content': 'content',
        'page_info': 'page_info'
    }

    def __init__(self, total=None, content=None, page_info=None):
        r"""ListSecuritySensitiveDataDetailsResponse

        The model defined in huaweicloud sdk

        :param total: 敏感数据发现详情总条数。
        :type total: int
        :param content: 敏感数据发现列表。
        :type content: list[:class:`huaweicloudsdkdataartsstudio.v1.SensitiveDataDTO`]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkdataartsstudio.v1.PageInfo`
        """
        
        super(ListSecuritySensitiveDataDetailsResponse, self).__init__()

        self._total = None
        self._content = None
        self._page_info = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if content is not None:
            self.content = content
        if page_info is not None:
            self.page_info = page_info

    @property
    def total(self):
        r"""Gets the total of this ListSecuritySensitiveDataDetailsResponse.

        敏感数据发现详情总条数。

        :return: The total of this ListSecuritySensitiveDataDetailsResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListSecuritySensitiveDataDetailsResponse.

        敏感数据发现详情总条数。

        :param total: The total of this ListSecuritySensitiveDataDetailsResponse.
        :type total: int
        """
        self._total = total

    @property
    def content(self):
        r"""Gets the content of this ListSecuritySensitiveDataDetailsResponse.

        敏感数据发现列表。

        :return: The content of this ListSecuritySensitiveDataDetailsResponse.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.SensitiveDataDTO`]
        """
        return self._content

    @content.setter
    def content(self, content):
        r"""Sets the content of this ListSecuritySensitiveDataDetailsResponse.

        敏感数据发现列表。

        :param content: The content of this ListSecuritySensitiveDataDetailsResponse.
        :type content: list[:class:`huaweicloudsdkdataartsstudio.v1.SensitiveDataDTO`]
        """
        self._content = content

    @property
    def page_info(self):
        r"""Gets the page_info of this ListSecuritySensitiveDataDetailsResponse.

        :return: The page_info of this ListSecuritySensitiveDataDetailsResponse.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.PageInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        r"""Sets the page_info of this ListSecuritySensitiveDataDetailsResponse.

        :param page_info: The page_info of this ListSecuritySensitiveDataDetailsResponse.
        :type page_info: :class:`huaweicloudsdkdataartsstudio.v1.PageInfo`
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
        if not isinstance(other, ListSecuritySensitiveDataDetailsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
