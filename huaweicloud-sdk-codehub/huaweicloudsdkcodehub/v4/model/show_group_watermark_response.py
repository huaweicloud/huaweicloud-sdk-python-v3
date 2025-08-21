# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowGroupWatermarkResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'watermark': 'bool',
        'can_update': 'bool'
    }

    attribute_map = {
        'watermark': 'watermark',
        'can_update': 'can_update'
    }

    def __init__(self, watermark=None, can_update=None):
        r"""ShowGroupWatermarkResponse

        The model defined in huaweicloud sdk

        :param watermark: **参数解释：** 水印设置状态。 - true，开启水印。 - false，关闭水印。 
        :type watermark: bool
        :param can_update: **参数解释：** 当前用户是否有权限更新水印设置。 - true，有权限更新。 - false，无权限更新。 
        :type can_update: bool
        """
        
        super(ShowGroupWatermarkResponse, self).__init__()

        self._watermark = None
        self._can_update = None
        self.discriminator = None

        if watermark is not None:
            self.watermark = watermark
        if can_update is not None:
            self.can_update = can_update

    @property
    def watermark(self):
        r"""Gets the watermark of this ShowGroupWatermarkResponse.

        **参数解释：** 水印设置状态。 - true，开启水印。 - false，关闭水印。 

        :return: The watermark of this ShowGroupWatermarkResponse.
        :rtype: bool
        """
        return self._watermark

    @watermark.setter
    def watermark(self, watermark):
        r"""Sets the watermark of this ShowGroupWatermarkResponse.

        **参数解释：** 水印设置状态。 - true，开启水印。 - false，关闭水印。 

        :param watermark: The watermark of this ShowGroupWatermarkResponse.
        :type watermark: bool
        """
        self._watermark = watermark

    @property
    def can_update(self):
        r"""Gets the can_update of this ShowGroupWatermarkResponse.

        **参数解释：** 当前用户是否有权限更新水印设置。 - true，有权限更新。 - false，无权限更新。 

        :return: The can_update of this ShowGroupWatermarkResponse.
        :rtype: bool
        """
        return self._can_update

    @can_update.setter
    def can_update(self, can_update):
        r"""Sets the can_update of this ShowGroupWatermarkResponse.

        **参数解释：** 当前用户是否有权限更新水印设置。 - true，有权限更新。 - false，无权限更新。 

        :param can_update: The can_update of this ShowGroupWatermarkResponse.
        :type can_update: bool
        """
        self._can_update = can_update

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
        if not isinstance(other, ShowGroupWatermarkResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
