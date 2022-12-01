# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImageMediaTaggingDetInstance:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'bounding_box': 'object',
        'confidence': 'str'
    }

    attribute_map = {
        'bounding_box': 'bounding_box',
        'confidence': 'confidence'
    }

    def __init__(self, bounding_box=None, confidence=None):
        """ImageMediaTaggingDetInstance

        The model defined in huaweicloud sdk

        :param bounding_box: 目标检测框位置信息，包括4个值：  width：检测框区域宽度  height：检测框区域高度  top_left_x：检测框左上角到垂直轴距离  top_left_y：检测框左上角到水平轴距离 
        :type bounding_box: object
        :param confidence: 检测标签的置信度，将Float型置信度转为String类型返回，Float取值范围（0~100）。
        :type confidence: str
        """
        
        

        self._bounding_box = None
        self._confidence = None
        self.discriminator = None

        if bounding_box is not None:
            self.bounding_box = bounding_box
        if confidence is not None:
            self.confidence = confidence

    @property
    def bounding_box(self):
        """Gets the bounding_box of this ImageMediaTaggingDetInstance.

        目标检测框位置信息，包括4个值：  width：检测框区域宽度  height：检测框区域高度  top_left_x：检测框左上角到垂直轴距离  top_left_y：检测框左上角到水平轴距离 

        :return: The bounding_box of this ImageMediaTaggingDetInstance.
        :rtype: object
        """
        return self._bounding_box

    @bounding_box.setter
    def bounding_box(self, bounding_box):
        """Sets the bounding_box of this ImageMediaTaggingDetInstance.

        目标检测框位置信息，包括4个值：  width：检测框区域宽度  height：检测框区域高度  top_left_x：检测框左上角到垂直轴距离  top_left_y：检测框左上角到水平轴距离 

        :param bounding_box: The bounding_box of this ImageMediaTaggingDetInstance.
        :type bounding_box: object
        """
        self._bounding_box = bounding_box

    @property
    def confidence(self):
        """Gets the confidence of this ImageMediaTaggingDetInstance.

        检测标签的置信度，将Float型置信度转为String类型返回，Float取值范围（0~100）。

        :return: The confidence of this ImageMediaTaggingDetInstance.
        :rtype: str
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        """Sets the confidence of this ImageMediaTaggingDetInstance.

        检测标签的置信度，将Float型置信度转为String类型返回，Float取值范围（0~100）。

        :param confidence: The confidence of this ImageMediaTaggingDetInstance.
        :type confidence: str
        """
        self._confidence = confidence

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
        if not isinstance(other, ImageMediaTaggingDetInstance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
