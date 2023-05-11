# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowExtremumInfoResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'maximum': 'ExtremumDto',
        'minimum': 'ExtremumDto'
    }

    attribute_map = {
        'maximum': 'maximum',
        'minimum': 'minimum'
    }

    def __init__(self, maximum=None, minimum=None):
        """ShowExtremumInfoResponse

        The model defined in huaweicloud sdk

        :param maximum: 
        :type maximum: :class:`huaweicloudsdkeihealth.v1.ExtremumDto`
        :param minimum: 
        :type minimum: :class:`huaweicloudsdkeihealth.v1.ExtremumDto`
        """
        
        super(ShowExtremumInfoResponse, self).__init__()

        self._maximum = None
        self._minimum = None
        self.discriminator = None

        if maximum is not None:
            self.maximum = maximum
        if minimum is not None:
            self.minimum = minimum

    @property
    def maximum(self):
        """Gets the maximum of this ShowExtremumInfoResponse.

        :return: The maximum of this ShowExtremumInfoResponse.
        :rtype: :class:`huaweicloudsdkeihealth.v1.ExtremumDto`
        """
        return self._maximum

    @maximum.setter
    def maximum(self, maximum):
        """Sets the maximum of this ShowExtremumInfoResponse.

        :param maximum: The maximum of this ShowExtremumInfoResponse.
        :type maximum: :class:`huaweicloudsdkeihealth.v1.ExtremumDto`
        """
        self._maximum = maximum

    @property
    def minimum(self):
        """Gets the minimum of this ShowExtremumInfoResponse.

        :return: The minimum of this ShowExtremumInfoResponse.
        :rtype: :class:`huaweicloudsdkeihealth.v1.ExtremumDto`
        """
        return self._minimum

    @minimum.setter
    def minimum(self, minimum):
        """Sets the minimum of this ShowExtremumInfoResponse.

        :param minimum: The minimum of this ShowExtremumInfoResponse.
        :type minimum: :class:`huaweicloudsdkeihealth.v1.ExtremumDto`
        """
        self._minimum = minimum

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
        if not isinstance(other, ShowExtremumInfoResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
