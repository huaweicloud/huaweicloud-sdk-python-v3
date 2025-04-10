# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowGetLogSettingResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'log_configuration': 'LogConfiguration'
    }

    attribute_map = {
        'log_configuration': 'logConfiguration'
    }

    def __init__(self, log_configuration=None):
        r"""ShowGetLogSettingResponse

        The model defined in huaweicloud sdk

        :param log_configuration: 
        :type log_configuration: :class:`huaweicloudsdkcss.v1.LogConfiguration`
        """
        
        super(ShowGetLogSettingResponse, self).__init__()

        self._log_configuration = None
        self.discriminator = None

        if log_configuration is not None:
            self.log_configuration = log_configuration

    @property
    def log_configuration(self):
        r"""Gets the log_configuration of this ShowGetLogSettingResponse.

        :return: The log_configuration of this ShowGetLogSettingResponse.
        :rtype: :class:`huaweicloudsdkcss.v1.LogConfiguration`
        """
        return self._log_configuration

    @log_configuration.setter
    def log_configuration(self, log_configuration):
        r"""Sets the log_configuration of this ShowGetLogSettingResponse.

        :param log_configuration: The log_configuration of this ShowGetLogSettingResponse.
        :type log_configuration: :class:`huaweicloudsdkcss.v1.LogConfiguration`
        """
        self._log_configuration = log_configuration

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
        if not isinstance(other, ShowGetLogSettingResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
