# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSecurityDatasourceUrlsResponse(SdkResponse):

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
        'urls': 'list[UrlDTO]'
    }

    attribute_map = {
        'total': 'total',
        'urls': 'urls'
    }

    def __init__(self, total=None, urls=None):
        r"""ListSecurityDatasourceUrlsResponse

        The model defined in huaweicloud sdk

        :param total: 总条数
        :type total: int
        :param urls: url列表
        :type urls: list[:class:`huaweicloudsdkdataartsstudio.v1.UrlDTO`]
        """
        
        super(ListSecurityDatasourceUrlsResponse, self).__init__()

        self._total = None
        self._urls = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if urls is not None:
            self.urls = urls

    @property
    def total(self):
        r"""Gets the total of this ListSecurityDatasourceUrlsResponse.

        总条数

        :return: The total of this ListSecurityDatasourceUrlsResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListSecurityDatasourceUrlsResponse.

        总条数

        :param total: The total of this ListSecurityDatasourceUrlsResponse.
        :type total: int
        """
        self._total = total

    @property
    def urls(self):
        r"""Gets the urls of this ListSecurityDatasourceUrlsResponse.

        url列表

        :return: The urls of this ListSecurityDatasourceUrlsResponse.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.UrlDTO`]
        """
        return self._urls

    @urls.setter
    def urls(self, urls):
        r"""Sets the urls of this ListSecurityDatasourceUrlsResponse.

        url列表

        :param urls: The urls of this ListSecurityDatasourceUrlsResponse.
        :type urls: list[:class:`huaweicloudsdkdataartsstudio.v1.UrlDTO`]
        """
        self._urls = urls

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
        if not isinstance(other, ListSecurityDatasourceUrlsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
