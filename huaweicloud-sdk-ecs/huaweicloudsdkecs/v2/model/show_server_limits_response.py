# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowServerLimitsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'absolute': 'ServerLimits'
    }

    attribute_map = {
        'absolute': 'absolute'
    }

    def __init__(self, absolute=None):
        """ShowServerLimitsResponse

        The model defined in huaweicloud sdk

        :param absolute: 
        :type absolute: :class:`huaweicloudsdkecs.v2.ServerLimits`
        """
        
        super(ShowServerLimitsResponse, self).__init__()

        self._absolute = None
        self.discriminator = None

        if absolute is not None:
            self.absolute = absolute

    @property
    def absolute(self):
        """Gets the absolute of this ShowServerLimitsResponse.

        :return: The absolute of this ShowServerLimitsResponse.
        :rtype: :class:`huaweicloudsdkecs.v2.ServerLimits`
        """
        return self._absolute

    @absolute.setter
    def absolute(self, absolute):
        """Sets the absolute of this ShowServerLimitsResponse.

        :param absolute: The absolute of this ShowServerLimitsResponse.
        :type absolute: :class:`huaweicloudsdkecs.v2.ServerLimits`
        """
        self._absolute = absolute

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
        if not isinstance(other, ShowServerLimitsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
