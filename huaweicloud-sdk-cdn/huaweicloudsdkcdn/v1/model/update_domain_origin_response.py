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
        'origin': 'ResourceBody'
    }

    attribute_map = {
        'origin': 'origin'
    }

    def __init__(self, origin=None):
        """UpdateDomainOriginResponse

        The model defined in huaweicloud sdk

        :param origin: 
        :type origin: :class:`huaweicloudsdkcdn.v1.ResourceBody`
        """
        
        super(UpdateDomainOriginResponse, self).__init__()

        self._origin = None
        self.discriminator = None

        if origin is not None:
            self.origin = origin

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
