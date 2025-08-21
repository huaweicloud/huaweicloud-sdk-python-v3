# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowRepositoryWatermarkResponse(SdkResponse):

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
        'view_watermark': 'bool'
    }

    attribute_map = {
        'watermark': 'watermark',
        'view_watermark': 'view_watermark'
    }

    def __init__(self, watermark=None, view_watermark=None):
        r"""ShowRepositoryWatermarkResponse

        The model defined in huaweicloud sdk

        :param watermark: **参数解释：** 水印设置状态。 - true，开启水印。 - false，关闭水印。 
        :type watermark: bool
        :param view_watermark: **参数解释：** 仓库水印状态。 - true，开启水印。 - false，关闭水印。 
        :type view_watermark: bool
        """
        
        super(ShowRepositoryWatermarkResponse, self).__init__()

        self._watermark = None
        self._view_watermark = None
        self.discriminator = None

        if watermark is not None:
            self.watermark = watermark
        if view_watermark is not None:
            self.view_watermark = view_watermark

    @property
    def watermark(self):
        r"""Gets the watermark of this ShowRepositoryWatermarkResponse.

        **参数解释：** 水印设置状态。 - true，开启水印。 - false，关闭水印。 

        :return: The watermark of this ShowRepositoryWatermarkResponse.
        :rtype: bool
        """
        return self._watermark

    @watermark.setter
    def watermark(self, watermark):
        r"""Sets the watermark of this ShowRepositoryWatermarkResponse.

        **参数解释：** 水印设置状态。 - true，开启水印。 - false，关闭水印。 

        :param watermark: The watermark of this ShowRepositoryWatermarkResponse.
        :type watermark: bool
        """
        self._watermark = watermark

    @property
    def view_watermark(self):
        r"""Gets the view_watermark of this ShowRepositoryWatermarkResponse.

        **参数解释：** 仓库水印状态。 - true，开启水印。 - false，关闭水印。 

        :return: The view_watermark of this ShowRepositoryWatermarkResponse.
        :rtype: bool
        """
        return self._view_watermark

    @view_watermark.setter
    def view_watermark(self, view_watermark):
        r"""Sets the view_watermark of this ShowRepositoryWatermarkResponse.

        **参数解释：** 仓库水印状态。 - true，开启水印。 - false，关闭水印。 

        :param view_watermark: The view_watermark of this ShowRepositoryWatermarkResponse.
        :type view_watermark: bool
        """
        self._view_watermark = view_watermark

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
        if not isinstance(other, ShowRepositoryWatermarkResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
