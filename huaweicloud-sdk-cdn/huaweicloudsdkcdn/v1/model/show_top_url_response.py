# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTopUrlResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'service_area': 'str',
        'top_url_summary': 'list[TopUrlSummary]'
    }

    attribute_map = {
        'service_area': 'service_area',
        'top_url_summary': 'top_url_summary'
    }

    def __init__(self, service_area=None, top_url_summary=None):
        """ShowTopUrlResponse

        The model defined in huaweicloud sdk

        :param service_area: 服务区域。
        :type service_area: str
        :param top_url_summary: 详情数据对象。
        :type top_url_summary: list[:class:`huaweicloudsdkcdn.v1.TopUrlSummary`]
        """
        
        super(ShowTopUrlResponse, self).__init__()

        self._service_area = None
        self._top_url_summary = None
        self.discriminator = None

        if service_area is not None:
            self.service_area = service_area
        if top_url_summary is not None:
            self.top_url_summary = top_url_summary

    @property
    def service_area(self):
        """Gets the service_area of this ShowTopUrlResponse.

        服务区域。

        :return: The service_area of this ShowTopUrlResponse.
        :rtype: str
        """
        return self._service_area

    @service_area.setter
    def service_area(self, service_area):
        """Sets the service_area of this ShowTopUrlResponse.

        服务区域。

        :param service_area: The service_area of this ShowTopUrlResponse.
        :type service_area: str
        """
        self._service_area = service_area

    @property
    def top_url_summary(self):
        """Gets the top_url_summary of this ShowTopUrlResponse.

        详情数据对象。

        :return: The top_url_summary of this ShowTopUrlResponse.
        :rtype: list[:class:`huaweicloudsdkcdn.v1.TopUrlSummary`]
        """
        return self._top_url_summary

    @top_url_summary.setter
    def top_url_summary(self, top_url_summary):
        """Sets the top_url_summary of this ShowTopUrlResponse.

        详情数据对象。

        :param top_url_summary: The top_url_summary of this ShowTopUrlResponse.
        :type top_url_summary: list[:class:`huaweicloudsdkcdn.v1.TopUrlSummary`]
        """
        self._top_url_summary = top_url_summary

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
        if not isinstance(other, ShowTopUrlResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
