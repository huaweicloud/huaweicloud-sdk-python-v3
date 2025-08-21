# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateRepositoryWatermarkResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'watermark': 'bool'
    }

    attribute_map = {
        'watermark': 'watermark'
    }

    def __init__(self, watermark=None):
        r"""UpdateRepositoryWatermarkResponse

        The model defined in huaweicloud sdk

        :param watermark: **参数解释：** 水印开启状态。 - true，开启水印。 - false，关闭水印。 
        :type watermark: bool
        """
        
        super(UpdateRepositoryWatermarkResponse, self).__init__()

        self._watermark = None
        self.discriminator = None

        if watermark is not None:
            self.watermark = watermark

    @property
    def watermark(self):
        r"""Gets the watermark of this UpdateRepositoryWatermarkResponse.

        **参数解释：** 水印开启状态。 - true，开启水印。 - false，关闭水印。 

        :return: The watermark of this UpdateRepositoryWatermarkResponse.
        :rtype: bool
        """
        return self._watermark

    @watermark.setter
    def watermark(self, watermark):
        r"""Sets the watermark of this UpdateRepositoryWatermarkResponse.

        **参数解释：** 水印开启状态。 - true，开启水印。 - false，关闭水印。 

        :param watermark: The watermark of this UpdateRepositoryWatermarkResponse.
        :type watermark: bool
        """
        self._watermark = watermark

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
        if not isinstance(other, UpdateRepositoryWatermarkResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
