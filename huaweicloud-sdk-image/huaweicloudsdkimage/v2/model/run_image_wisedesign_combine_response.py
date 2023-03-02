# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RunImageWisedesignCombineResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'result_base64': 'str'
    }

    attribute_map = {
        'result_base64': 'result_base64'
    }

    def __init__(self, result_base64=None):
        """RunImageWisedesignCombineResponse

        The model defined in huaweicloud sdk

        :param result_base64: 图片合成后图像的64位编码
        :type result_base64: str
        """
        
        super(RunImageWisedesignCombineResponse, self).__init__()

        self._result_base64 = None
        self.discriminator = None

        if result_base64 is not None:
            self.result_base64 = result_base64

    @property
    def result_base64(self):
        """Gets the result_base64 of this RunImageWisedesignCombineResponse.

        图片合成后图像的64位编码

        :return: The result_base64 of this RunImageWisedesignCombineResponse.
        :rtype: str
        """
        return self._result_base64

    @result_base64.setter
    def result_base64(self, result_base64):
        """Sets the result_base64 of this RunImageWisedesignCombineResponse.

        图片合成后图像的64位编码

        :param result_base64: The result_base64 of this RunImageWisedesignCombineResponse.
        :type result_base64: str
        """
        self._result_base64 = result_base64

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
        if not isinstance(other, RunImageWisedesignCombineResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
