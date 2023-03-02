# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VideoCuttingInference:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'segment_info': 'list[VideoSegmentInfo]'
    }

    attribute_map = {
        'segment_info': 'segment_info'
    }

    def __init__(self, segment_info=None):
        """VideoCuttingInference

        The model defined in huaweicloud sdk

        :param segment_info: 视频剪切服务推理分段参数
        :type segment_info: list[:class:`huaweicloudsdkimage.v2.VideoSegmentInfo`]
        """
        
        

        self._segment_info = None
        self.discriminator = None

        self.segment_info = segment_info

    @property
    def segment_info(self):
        """Gets the segment_info of this VideoCuttingInference.

        视频剪切服务推理分段参数

        :return: The segment_info of this VideoCuttingInference.
        :rtype: list[:class:`huaweicloudsdkimage.v2.VideoSegmentInfo`]
        """
        return self._segment_info

    @segment_info.setter
    def segment_info(self, segment_info):
        """Sets the segment_info of this VideoCuttingInference.

        视频剪切服务推理分段参数

        :param segment_info: The segment_info of this VideoCuttingInference.
        :type segment_info: list[:class:`huaweicloudsdkimage.v2.VideoSegmentInfo`]
        """
        self._segment_info = segment_info

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
        if not isinstance(other, VideoCuttingInference):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
