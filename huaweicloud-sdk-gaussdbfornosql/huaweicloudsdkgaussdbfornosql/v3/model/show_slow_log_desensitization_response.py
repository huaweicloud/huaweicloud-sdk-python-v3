# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSlowLogDesensitizationResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'desensitization_status': 'str'
    }

    attribute_map = {
        'desensitization_status': 'desensitization_status'
    }

    def __init__(self, desensitization_status=None):
        """ShowSlowLogDesensitizationResponse

        The model defined in huaweicloud sdk

        :param desensitization_status: 实例慢日志脱敏开启状态，取值：  - on 开启  - off 关闭
        :type desensitization_status: str
        """
        
        super(ShowSlowLogDesensitizationResponse, self).__init__()

        self._desensitization_status = None
        self.discriminator = None

        if desensitization_status is not None:
            self.desensitization_status = desensitization_status

    @property
    def desensitization_status(self):
        """Gets the desensitization_status of this ShowSlowLogDesensitizationResponse.

        实例慢日志脱敏开启状态，取值：  - on 开启  - off 关闭

        :return: The desensitization_status of this ShowSlowLogDesensitizationResponse.
        :rtype: str
        """
        return self._desensitization_status

    @desensitization_status.setter
    def desensitization_status(self, desensitization_status):
        """Sets the desensitization_status of this ShowSlowLogDesensitizationResponse.

        实例慢日志脱敏开启状态，取值：  - on 开启  - off 关闭

        :param desensitization_status: The desensitization_status of this ShowSlowLogDesensitizationResponse.
        :type desensitization_status: str
        """
        self._desensitization_status = desensitization_status

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
        if not isinstance(other, ShowSlowLogDesensitizationResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
