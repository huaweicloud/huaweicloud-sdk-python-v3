# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowImageWatermarkByAddressRequestBody:

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
        'mark_len': 'int'
    }

    attribute_map = {
        'region_id': 'region_id',
        'src_file': 'src_file',
        'mark_len': 'mark_len'
    }

    def __init__(self, region_id=None, src_file=None, mark_len=None):
        """ShowImageWatermarkByAddressRequestBody

        The model defined in huaweicloud sdk

        :param region_id: 项目所在region的id，如：xx-xx-1。
        :type region_id: str
        :param src_file: 待提取文字暗水印的图片地址，当前只支持华为云OBS，格式为 **obs://bucket/object** ，其中bucket为和当前项目处于同一区域的OBS桶名称，object为对象全路径名。例如：**obs://hwbucket/hwinfo/hw.png**，其中obs://表示OBS存储，hwbucket为桶名，hwinfo/hw.png为对象全路径名。
        :type src_file: str
        :param mark_len: 指定待提取水印的长度，最小0，最大32.。设置后可以提升水印提取性能。
        :type mark_len: int
        """
        
        

        self._region_id = None
        self._src_file = None
        self._mark_len = None
        self.discriminator = None

        self.region_id = region_id
        self.src_file = src_file
        if mark_len is not None:
            self.mark_len = mark_len

    @property
    def region_id(self):
        """Gets the region_id of this ShowImageWatermarkByAddressRequestBody.

        项目所在region的id，如：xx-xx-1。

        :return: The region_id of this ShowImageWatermarkByAddressRequestBody.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this ShowImageWatermarkByAddressRequestBody.

        项目所在region的id，如：xx-xx-1。

        :param region_id: The region_id of this ShowImageWatermarkByAddressRequestBody.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def src_file(self):
        """Gets the src_file of this ShowImageWatermarkByAddressRequestBody.

        待提取文字暗水印的图片地址，当前只支持华为云OBS，格式为 **obs://bucket/object** ，其中bucket为和当前项目处于同一区域的OBS桶名称，object为对象全路径名。例如：**obs://hwbucket/hwinfo/hw.png**，其中obs://表示OBS存储，hwbucket为桶名，hwinfo/hw.png为对象全路径名。

        :return: The src_file of this ShowImageWatermarkByAddressRequestBody.
        :rtype: str
        """
        return self._src_file

    @src_file.setter
    def src_file(self, src_file):
        """Sets the src_file of this ShowImageWatermarkByAddressRequestBody.

        待提取文字暗水印的图片地址，当前只支持华为云OBS，格式为 **obs://bucket/object** ，其中bucket为和当前项目处于同一区域的OBS桶名称，object为对象全路径名。例如：**obs://hwbucket/hwinfo/hw.png**，其中obs://表示OBS存储，hwbucket为桶名，hwinfo/hw.png为对象全路径名。

        :param src_file: The src_file of this ShowImageWatermarkByAddressRequestBody.
        :type src_file: str
        """
        self._src_file = src_file

    @property
    def mark_len(self):
        """Gets the mark_len of this ShowImageWatermarkByAddressRequestBody.

        指定待提取水印的长度，最小0，最大32.。设置后可以提升水印提取性能。

        :return: The mark_len of this ShowImageWatermarkByAddressRequestBody.
        :rtype: int
        """
        return self._mark_len

    @mark_len.setter
    def mark_len(self, mark_len):
        """Sets the mark_len of this ShowImageWatermarkByAddressRequestBody.

        指定待提取水印的长度，最小0，最大32.。设置后可以提升水印提取性能。

        :param mark_len: The mark_len of this ShowImageWatermarkByAddressRequestBody.
        :type mark_len: int
        """
        self._mark_len = mark_len

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
        if not isinstance(other, ShowImageWatermarkByAddressRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
