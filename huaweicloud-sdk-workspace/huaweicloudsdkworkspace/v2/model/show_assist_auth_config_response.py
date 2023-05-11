# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAssistAuthConfigResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'otp_config_info': 'OtpConfigInfo'
    }

    attribute_map = {
        'otp_config_info': 'otp_config_info'
    }

    def __init__(self, otp_config_info=None):
        """ShowAssistAuthConfigResponse

        The model defined in huaweicloud sdk

        :param otp_config_info: 
        :type otp_config_info: :class:`huaweicloudsdkworkspace.v2.OtpConfigInfo`
        """
        
        super(ShowAssistAuthConfigResponse, self).__init__()

        self._otp_config_info = None
        self.discriminator = None

        if otp_config_info is not None:
            self.otp_config_info = otp_config_info

    @property
    def otp_config_info(self):
        """Gets the otp_config_info of this ShowAssistAuthConfigResponse.

        :return: The otp_config_info of this ShowAssistAuthConfigResponse.
        :rtype: :class:`huaweicloudsdkworkspace.v2.OtpConfigInfo`
        """
        return self._otp_config_info

    @otp_config_info.setter
    def otp_config_info(self, otp_config_info):
        """Sets the otp_config_info of this ShowAssistAuthConfigResponse.

        :param otp_config_info: The otp_config_info of this ShowAssistAuthConfigResponse.
        :type otp_config_info: :class:`huaweicloudsdkworkspace.v2.OtpConfigInfo`
        """
        self._otp_config_info = otp_config_info

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
        if not isinstance(other, ShowAssistAuthConfigResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
