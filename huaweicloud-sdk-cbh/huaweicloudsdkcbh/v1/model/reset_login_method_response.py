# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResetLoginMethodResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'request_info': 'str'
    }

    attribute_map = {
        'request_info': 'request_info'
    }

    def __init__(self, request_info=None):
        """ResetLoginMethodResponse

        The model defined in huaweicloud sdk

        :param request_info: Requested information
        :type request_info: str
        """
        
        super(ResetLoginMethodResponse, self).__init__()

        self._request_info = None
        self.discriminator = None

        if request_info is not None:
            self.request_info = request_info

    @property
    def request_info(self):
        """Gets the request_info of this ResetLoginMethodResponse.

        Requested information

        :return: The request_info of this ResetLoginMethodResponse.
        :rtype: str
        """
        return self._request_info

    @request_info.setter
    def request_info(self, request_info):
        """Sets the request_info of this ResetLoginMethodResponse.

        Requested information

        :param request_info: The request_info of this ResetLoginMethodResponse.
        :type request_info: str
        """
        self._request_info = request_info

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
        if not isinstance(other, ResetLoginMethodResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
