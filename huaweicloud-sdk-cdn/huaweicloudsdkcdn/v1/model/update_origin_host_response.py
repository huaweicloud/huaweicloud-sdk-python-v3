# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateOriginHostResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'origin_host': 'DomainOriginHost',
        'x_request_id': 'str'
    }

    attribute_map = {
        'origin_host': 'origin_host',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, origin_host=None, x_request_id=None):
        r"""UpdateOriginHostResponse

        The model defined in huaweicloud sdk

        :param origin_host: 
        :type origin_host: :class:`huaweicloudsdkcdn.v1.DomainOriginHost`
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(UpdateOriginHostResponse, self).__init__()

        self._origin_host = None
        self._x_request_id = None
        self.discriminator = None

        if origin_host is not None:
            self.origin_host = origin_host
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def origin_host(self):
        r"""Gets the origin_host of this UpdateOriginHostResponse.

        :return: The origin_host of this UpdateOriginHostResponse.
        :rtype: :class:`huaweicloudsdkcdn.v1.DomainOriginHost`
        """
        return self._origin_host

    @origin_host.setter
    def origin_host(self, origin_host):
        r"""Sets the origin_host of this UpdateOriginHostResponse.

        :param origin_host: The origin_host of this UpdateOriginHostResponse.
        :type origin_host: :class:`huaweicloudsdkcdn.v1.DomainOriginHost`
        """
        self._origin_host = origin_host

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this UpdateOriginHostResponse.

        :return: The x_request_id of this UpdateOriginHostResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this UpdateOriginHostResponse.

        :param x_request_id: The x_request_id of this UpdateOriginHostResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

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
        if not isinstance(other, UpdateOriginHostResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
