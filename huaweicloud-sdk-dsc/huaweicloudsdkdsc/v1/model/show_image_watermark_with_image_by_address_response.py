# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowImageWatermarkWithImageByAddressResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'region_id': 'str',
        'image_watermark': 'str'
    }

    attribute_map = {
        'region_id': 'region_id',
        'image_watermark': 'image_watermark'
    }

    def __init__(self, region_id=None, image_watermark=None):
        r"""ShowImageWatermarkWithImageByAddressResponse

        The model defined in huaweicloud sdk

        :param region_id: 当前项目所在region的id，如：xx-xx-1。
        :type region_id: str
        :param image_watermark: 提取出的水印图片存放地址，当前只支持华为云OBS对象，格式为 **obs://bucket/object** ，其中bucket为和当前项目处于同一区域的OBS桶名称，object为对象全路径名。例如：**obs://hwbucket/hwinfo/hw.png**，其中obs://表示OBS存储，hwbucket为桶名，hwinfo/hw.png为对象全路径名。
        :type image_watermark: str
        """
        
        super(ShowImageWatermarkWithImageByAddressResponse, self).__init__()

        self._region_id = None
        self._image_watermark = None
        self.discriminator = None

        if region_id is not None:
            self.region_id = region_id
        if image_watermark is not None:
            self.image_watermark = image_watermark

    @property
    def region_id(self):
        r"""Gets the region_id of this ShowImageWatermarkWithImageByAddressResponse.

        当前项目所在region的id，如：xx-xx-1。

        :return: The region_id of this ShowImageWatermarkWithImageByAddressResponse.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this ShowImageWatermarkWithImageByAddressResponse.

        当前项目所在region的id，如：xx-xx-1。

        :param region_id: The region_id of this ShowImageWatermarkWithImageByAddressResponse.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def image_watermark(self):
        r"""Gets the image_watermark of this ShowImageWatermarkWithImageByAddressResponse.

        提取出的水印图片存放地址，当前只支持华为云OBS对象，格式为 **obs://bucket/object** ，其中bucket为和当前项目处于同一区域的OBS桶名称，object为对象全路径名。例如：**obs://hwbucket/hwinfo/hw.png**，其中obs://表示OBS存储，hwbucket为桶名，hwinfo/hw.png为对象全路径名。

        :return: The image_watermark of this ShowImageWatermarkWithImageByAddressResponse.
        :rtype: str
        """
        return self._image_watermark

    @image_watermark.setter
    def image_watermark(self, image_watermark):
        r"""Sets the image_watermark of this ShowImageWatermarkWithImageByAddressResponse.

        提取出的水印图片存放地址，当前只支持华为云OBS对象，格式为 **obs://bucket/object** ，其中bucket为和当前项目处于同一区域的OBS桶名称，object为对象全路径名。例如：**obs://hwbucket/hwinfo/hw.png**，其中obs://表示OBS存储，hwbucket为桶名，hwinfo/hw.png为对象全路径名。

        :param image_watermark: The image_watermark of this ShowImageWatermarkWithImageByAddressResponse.
        :type image_watermark: str
        """
        self._image_watermark = image_watermark

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
        if not isinstance(other, ShowImageWatermarkWithImageByAddressResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
