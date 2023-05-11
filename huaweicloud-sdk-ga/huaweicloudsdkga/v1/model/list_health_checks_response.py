# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListHealthChecksResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'health_checks': 'list[HealthCheckDetail]',
        'page_info': 'PageInfo',
        'request_id': 'str'
    }

    attribute_map = {
        'health_checks': 'health_checks',
        'page_info': 'page_info',
        'request_id': 'request_id'
    }

    def __init__(self, health_checks=None, page_info=None, request_id=None):
        """ListHealthChecksResponse

        The model defined in huaweicloud sdk

        :param health_checks: 健康检查列表。
        :type health_checks: list[:class:`huaweicloudsdkga.v1.HealthCheckDetail`]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkga.v1.PageInfo`
        :param request_id: 请求ID。
        :type request_id: str
        """
        
        super(ListHealthChecksResponse, self).__init__()

        self._health_checks = None
        self._page_info = None
        self._request_id = None
        self.discriminator = None

        if health_checks is not None:
            self.health_checks = health_checks
        if page_info is not None:
            self.page_info = page_info
        if request_id is not None:
            self.request_id = request_id

    @property
    def health_checks(self):
        """Gets the health_checks of this ListHealthChecksResponse.

        健康检查列表。

        :return: The health_checks of this ListHealthChecksResponse.
        :rtype: list[:class:`huaweicloudsdkga.v1.HealthCheckDetail`]
        """
        return self._health_checks

    @health_checks.setter
    def health_checks(self, health_checks):
        """Sets the health_checks of this ListHealthChecksResponse.

        健康检查列表。

        :param health_checks: The health_checks of this ListHealthChecksResponse.
        :type health_checks: list[:class:`huaweicloudsdkga.v1.HealthCheckDetail`]
        """
        self._health_checks = health_checks

    @property
    def page_info(self):
        """Gets the page_info of this ListHealthChecksResponse.

        :return: The page_info of this ListHealthChecksResponse.
        :rtype: :class:`huaweicloudsdkga.v1.PageInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        """Sets the page_info of this ListHealthChecksResponse.

        :param page_info: The page_info of this ListHealthChecksResponse.
        :type page_info: :class:`huaweicloudsdkga.v1.PageInfo`
        """
        self._page_info = page_info

    @property
    def request_id(self):
        """Gets the request_id of this ListHealthChecksResponse.

        请求ID。

        :return: The request_id of this ListHealthChecksResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this ListHealthChecksResponse.

        请求ID。

        :param request_id: The request_id of this ListHealthChecksResponse.
        :type request_id: str
        """
        self._request_id = request_id

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
        if not isinstance(other, ListHealthChecksResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
