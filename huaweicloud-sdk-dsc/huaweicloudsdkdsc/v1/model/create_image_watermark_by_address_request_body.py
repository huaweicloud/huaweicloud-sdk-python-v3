# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateImageWatermarkByAddressRequestBody:

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
        'src_file': 'str',
        'blind_watermark': 'str',
        'image_watermark': 'str',
        'dst_file': 'str'
    }

    attribute_map = {
        'region_id': 'region_id',
        'src_file': 'src_file',
        'blind_watermark': 'blind_watermark',
        'image_watermark': 'image_watermark',
        'dst_file': 'dst_file'
    }

    def __init__(self, region_id=None, src_file=None, blind_watermark=None, image_watermark=None, dst_file=None):
        """CreateImageWatermarkByAddressRequestBody

        The model defined in huaweicloud sdk

        :param region_id: 当前项目所在region的id，如：xx-xx-1。
        :type region_id: str
        :param src_file: 待加暗水印的图片地址，当前只支持华为云OBS文件，格式为 **obs://bucket/object** ，其中bucket为和当前项目处于同一区域的OBS桶名称，object为对象全路径名。例如：**obs://hwbucket/hwinfo/hw.png**，其中obs://表示OBS存储，hwbucket为桶名，hwinfo/hw.png为对象全路径名。
        :type src_file: str
        :param blind_watermark: 待嵌入的文字暗水印内容，长度不超过32个字符。当前仅支持数字及英文大小写。与图片暗水印image_watermark二选一。
        :type blind_watermark: str
        :param image_watermark: 待嵌入的图片暗水印地址，格式要求同src_file字段，与文字暗水印 blind_watermark 二选一，都填写时，生效image_watermark。
        :type image_watermark: str
        :param dst_file: 添加水印后的图片存放的地址，格式要求同src_file字段，不设置时，默认取src_file的值，即添加水印后覆盖原文件。
        :type dst_file: str
        """
        
        

        self._region_id = None
        self._src_file = None
        self._blind_watermark = None
        self._image_watermark = None
        self._dst_file = None
        self.discriminator = None

        self.region_id = region_id
        self.src_file = src_file
        if blind_watermark is not None:
            self.blind_watermark = blind_watermark
        if image_watermark is not None:
            self.image_watermark = image_watermark
        if dst_file is not None:
            self.dst_file = dst_file

    @property
    def region_id(self):
        """Gets the region_id of this CreateImageWatermarkByAddressRequestBody.

        当前项目所在region的id，如：xx-xx-1。

        :return: The region_id of this CreateImageWatermarkByAddressRequestBody.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this CreateImageWatermarkByAddressRequestBody.

        当前项目所在region的id，如：xx-xx-1。

        :param region_id: The region_id of this CreateImageWatermarkByAddressRequestBody.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def src_file(self):
        """Gets the src_file of this CreateImageWatermarkByAddressRequestBody.

        待加暗水印的图片地址，当前只支持华为云OBS文件，格式为 **obs://bucket/object** ，其中bucket为和当前项目处于同一区域的OBS桶名称，object为对象全路径名。例如：**obs://hwbucket/hwinfo/hw.png**，其中obs://表示OBS存储，hwbucket为桶名，hwinfo/hw.png为对象全路径名。

        :return: The src_file of this CreateImageWatermarkByAddressRequestBody.
        :rtype: str
        """
        return self._src_file

    @src_file.setter
    def src_file(self, src_file):
        """Sets the src_file of this CreateImageWatermarkByAddressRequestBody.

        待加暗水印的图片地址，当前只支持华为云OBS文件，格式为 **obs://bucket/object** ，其中bucket为和当前项目处于同一区域的OBS桶名称，object为对象全路径名。例如：**obs://hwbucket/hwinfo/hw.png**，其中obs://表示OBS存储，hwbucket为桶名，hwinfo/hw.png为对象全路径名。

        :param src_file: The src_file of this CreateImageWatermarkByAddressRequestBody.
        :type src_file: str
        """
        self._src_file = src_file

    @property
    def blind_watermark(self):
        """Gets the blind_watermark of this CreateImageWatermarkByAddressRequestBody.

        待嵌入的文字暗水印内容，长度不超过32个字符。当前仅支持数字及英文大小写。与图片暗水印image_watermark二选一。

        :return: The blind_watermark of this CreateImageWatermarkByAddressRequestBody.
        :rtype: str
        """
        return self._blind_watermark

    @blind_watermark.setter
    def blind_watermark(self, blind_watermark):
        """Sets the blind_watermark of this CreateImageWatermarkByAddressRequestBody.

        待嵌入的文字暗水印内容，长度不超过32个字符。当前仅支持数字及英文大小写。与图片暗水印image_watermark二选一。

        :param blind_watermark: The blind_watermark of this CreateImageWatermarkByAddressRequestBody.
        :type blind_watermark: str
        """
        self._blind_watermark = blind_watermark

    @property
    def image_watermark(self):
        """Gets the image_watermark of this CreateImageWatermarkByAddressRequestBody.

        待嵌入的图片暗水印地址，格式要求同src_file字段，与文字暗水印 blind_watermark 二选一，都填写时，生效image_watermark。

        :return: The image_watermark of this CreateImageWatermarkByAddressRequestBody.
        :rtype: str
        """
        return self._image_watermark

    @image_watermark.setter
    def image_watermark(self, image_watermark):
        """Sets the image_watermark of this CreateImageWatermarkByAddressRequestBody.

        待嵌入的图片暗水印地址，格式要求同src_file字段，与文字暗水印 blind_watermark 二选一，都填写时，生效image_watermark。

        :param image_watermark: The image_watermark of this CreateImageWatermarkByAddressRequestBody.
        :type image_watermark: str
        """
        self._image_watermark = image_watermark

    @property
    def dst_file(self):
        """Gets the dst_file of this CreateImageWatermarkByAddressRequestBody.

        添加水印后的图片存放的地址，格式要求同src_file字段，不设置时，默认取src_file的值，即添加水印后覆盖原文件。

        :return: The dst_file of this CreateImageWatermarkByAddressRequestBody.
        :rtype: str
        """
        return self._dst_file

    @dst_file.setter
    def dst_file(self, dst_file):
        """Sets the dst_file of this CreateImageWatermarkByAddressRequestBody.

        添加水印后的图片存放的地址，格式要求同src_file字段，不设置时，默认取src_file的值，即添加水印后覆盖原文件。

        :param dst_file: The dst_file of this CreateImageWatermarkByAddressRequestBody.
        :type dst_file: str
        """
        self._dst_file = dst_file

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
        if not isinstance(other, CreateImageWatermarkByAddressRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
