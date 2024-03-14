# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateDomainOriginResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'origin': 'ResourceBody',
        'x_request_id': 'str'
    }

    attribute_map = {
        'origin': 'origin',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, origin=None, x_request_id=None):
        """UpdateDomainOriginResponse

        The model defined in huaweicloud sdk

        :param origin: 
        :type origin: :class:`huaweicloudsdkcdn.v1.ResourceBody`
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(UpdateDomainOriginResponse, self).__init__()

        self._origin = None
        self._x_request_id = None
        self.discriminator = None

        if origin is not None:
            self.origin = origin
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def origin(self):
        """Gets the origin of this UpdateDomainOriginResponse.

        :return: The origin of this UpdateDomainOriginResponse.
        :rtype: :class:`huaweicloudsdkcdn.v1.ResourceBody`
        """
        return self._origin

    @origin.setter
    def origin(self, origin):
        """Sets the origin of this UpdateDomainOriginResponse.

        :param origin: The origin of this UpdateDomainOriginResponse.
        :type origin: :class:`huaweicloudsdkcdn.v1.ResourceBody`
        """
        self._origin = origin

    @property
    def x_request_id(self):
        """Gets the x_request_id of this UpdateDomainOriginResponse.

        :return: The x_request_id of this UpdateDomainOriginResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        """Sets the x_request_id of this UpdateDomainOriginResponse.

        :param x_request_id: The x_request_id of this UpdateDomainOriginResponse.
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
        if not isinstance(other, UpdateDomainOriginResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
