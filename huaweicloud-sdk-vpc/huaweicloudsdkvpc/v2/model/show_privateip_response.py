# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowPrivateipResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'privateip': 'Privateip'
    }

    attribute_map = {
        'privateip': 'privateip'
    }

    def __init__(self, privateip=None):
        """ShowPrivateipResponse

        The model defined in huaweicloud sdk

        :param privateip: 
        :type privateip: :class:`huaweicloudsdkvpc.v2.Privateip`
        """
        
        super(ShowPrivateipResponse, self).__init__()

        self._privateip = None
        self.discriminator = None

        if privateip is not None:
            self.privateip = privateip

    @property
    def privateip(self):
        """Gets the privateip of this ShowPrivateipResponse.

        :return: The privateip of this ShowPrivateipResponse.
        :rtype: :class:`huaweicloudsdkvpc.v2.Privateip`
        """
        return self._privateip

    @privateip.setter
    def privateip(self, privateip):
        """Sets the privateip of this ShowPrivateipResponse.

        :param privateip: The privateip of this ShowPrivateipResponse.
        :type privateip: :class:`huaweicloudsdkvpc.v2.Privateip`
        """
        self._privateip = privateip

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
        if not isinstance(other, ShowPrivateipResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
