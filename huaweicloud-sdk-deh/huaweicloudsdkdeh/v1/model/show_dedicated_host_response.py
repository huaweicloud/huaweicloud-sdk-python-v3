# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDedicatedHostResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'dedicated_host': 'RespDedicatedHost'
    }

    attribute_map = {
        'dedicated_host': 'dedicated_host'
    }

    def __init__(self, dedicated_host=None):
        r"""ShowDedicatedHostResponse

        The model defined in huaweicloud sdk

        :param dedicated_host: 
        :type dedicated_host: :class:`huaweicloudsdkdeh.v1.RespDedicatedHost`
        """
        
        super(ShowDedicatedHostResponse, self).__init__()

        self._dedicated_host = None
        self.discriminator = None

        if dedicated_host is not None:
            self.dedicated_host = dedicated_host

    @property
    def dedicated_host(self):
        r"""Gets the dedicated_host of this ShowDedicatedHostResponse.

        :return: The dedicated_host of this ShowDedicatedHostResponse.
        :rtype: :class:`huaweicloudsdkdeh.v1.RespDedicatedHost`
        """
        return self._dedicated_host

    @dedicated_host.setter
    def dedicated_host(self, dedicated_host):
        r"""Sets the dedicated_host of this ShowDedicatedHostResponse.

        :param dedicated_host: The dedicated_host of this ShowDedicatedHostResponse.
        :type dedicated_host: :class:`huaweicloudsdkdeh.v1.RespDedicatedHost`
        """
        self._dedicated_host = dedicated_host

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
        if not isinstance(other, ShowDedicatedHostResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
