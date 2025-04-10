# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateDirectConnectRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'direct_connect': 'UpdateDirectConnect'
    }

    attribute_map = {
        'direct_connect': 'direct_connect'
    }

    def __init__(self, direct_connect=None):
        r"""UpdateDirectConnectRequestBody

        The model defined in huaweicloud sdk

        :param direct_connect: 
        :type direct_connect: :class:`huaweicloudsdkdc.v3.UpdateDirectConnect`
        """
        
        

        self._direct_connect = None
        self.discriminator = None

        if direct_connect is not None:
            self.direct_connect = direct_connect

    @property
    def direct_connect(self):
        r"""Gets the direct_connect of this UpdateDirectConnectRequestBody.

        :return: The direct_connect of this UpdateDirectConnectRequestBody.
        :rtype: :class:`huaweicloudsdkdc.v3.UpdateDirectConnect`
        """
        return self._direct_connect

    @direct_connect.setter
    def direct_connect(self, direct_connect):
        r"""Sets the direct_connect of this UpdateDirectConnectRequestBody.

        :param direct_connect: The direct_connect of this UpdateDirectConnectRequestBody.
        :type direct_connect: :class:`huaweicloudsdkdc.v3.UpdateDirectConnect`
        """
        self._direct_connect = direct_connect

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
        if not isinstance(other, UpdateDirectConnectRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
