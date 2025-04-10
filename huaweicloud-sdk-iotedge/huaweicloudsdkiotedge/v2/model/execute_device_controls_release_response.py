# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExecuteDeviceControlsReleaseResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'result_code': 'int',
        'result_desc': 'str'
    }

    attribute_map = {
        'result_code': 'result_code',
        'result_desc': 'result_desc'
    }

    def __init__(self, result_code=None, result_desc=None):
        r"""ExecuteDeviceControlsReleaseResponse

        The model defined in huaweicloud sdk

        :param result_code: 属性设置的响应码，具体为实际设备返回的响应码
        :type result_code: int
        :param result_desc: 属性设置的描述，具体为实际设备返回的描述
        :type result_desc: str
        """
        
        super(ExecuteDeviceControlsReleaseResponse, self).__init__()

        self._result_code = None
        self._result_desc = None
        self.discriminator = None

        if result_code is not None:
            self.result_code = result_code
        if result_desc is not None:
            self.result_desc = result_desc

    @property
    def result_code(self):
        r"""Gets the result_code of this ExecuteDeviceControlsReleaseResponse.

        属性设置的响应码，具体为实际设备返回的响应码

        :return: The result_code of this ExecuteDeviceControlsReleaseResponse.
        :rtype: int
        """
        return self._result_code

    @result_code.setter
    def result_code(self, result_code):
        r"""Sets the result_code of this ExecuteDeviceControlsReleaseResponse.

        属性设置的响应码，具体为实际设备返回的响应码

        :param result_code: The result_code of this ExecuteDeviceControlsReleaseResponse.
        :type result_code: int
        """
        self._result_code = result_code

    @property
    def result_desc(self):
        r"""Gets the result_desc of this ExecuteDeviceControlsReleaseResponse.

        属性设置的描述，具体为实际设备返回的描述

        :return: The result_desc of this ExecuteDeviceControlsReleaseResponse.
        :rtype: str
        """
        return self._result_desc

    @result_desc.setter
    def result_desc(self, result_desc):
        r"""Sets the result_desc of this ExecuteDeviceControlsReleaseResponse.

        属性设置的描述，具体为实际设备返回的描述

        :param result_desc: The result_desc of this ExecuteDeviceControlsReleaseResponse.
        :type result_desc: str
        """
        self._result_desc = result_desc

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
        if not isinstance(other, ExecuteDeviceControlsReleaseResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
