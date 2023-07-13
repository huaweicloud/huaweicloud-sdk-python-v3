# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTopStatisticsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'top_urls': 'list[TopUrl]'
    }

    attribute_map = {
        'top_urls': 'top_urls'
    }

    def __init__(self, top_urls=None):
        """ListTopStatisticsResponse

        The model defined in huaweicloud sdk

        :param top_urls: 
        :type top_urls: list[:class:`huaweicloudsdkvod.v1.TopUrl`]
        """
        
        super(ListTopStatisticsResponse, self).__init__()

        self._top_urls = None
        self.discriminator = None

        if top_urls is not None:
            self.top_urls = top_urls

    @property
    def top_urls(self):
        """Gets the top_urls of this ListTopStatisticsResponse.

        :return: The top_urls of this ListTopStatisticsResponse.
        :rtype: list[:class:`huaweicloudsdkvod.v1.TopUrl`]
        """
        return self._top_urls

    @top_urls.setter
    def top_urls(self, top_urls):
        """Sets the top_urls of this ListTopStatisticsResponse.

        :param top_urls: The top_urls of this ListTopStatisticsResponse.
        :type top_urls: list[:class:`huaweicloudsdkvod.v1.TopUrl`]
        """
        self._top_urls = top_urls

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
        if not isinstance(other, ListTopStatisticsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
