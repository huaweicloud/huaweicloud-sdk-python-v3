# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImageMainObjectDetectionInstance:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'label': 'str',
        'location': 'object',
        'confidence': 'str'
    }

    attribute_map = {
        'label': 'label',
        'location': 'location',
        'confidence': 'confidence'
    }

    def __init__(self, label=None, location=None, confidence=None):
        """ImageMainObjectDetectionInstance

        The model defined in huaweicloud sdk

        :param label: 主体的类别，现阶段分为：bounding_box和main_object_box
        :type label: str
        :param location:  目标检测框位置信息，包括4个值：  width：检测框区域宽度  height：检测框区域高度  top_left_x：检测框左上角到垂直轴距离  top_left_y：检测框左上角到水平轴距离 properties: width: type: string description: 检测框区域高度 example: 139.58 height: type: string description: 检测框区域高度 example: 261.32 top_left_x: type: string description: 检测框左上角到垂直轴距离 example: 256.13 top_left_y: type: string description: 检测框左上角到水平轴距离 example: 85.2 
        :type location: object
        :param confidence: 主体框的置信度,将Float型置信度转为String类型返回,Float取值范围（0~100）。
        :type confidence: str
        """
        
        

        self._label = None
        self._location = None
        self._confidence = None
        self.discriminator = None

        if label is not None:
            self.label = label
        if location is not None:
            self.location = location
        if confidence is not None:
            self.confidence = confidence

    @property
    def label(self):
        """Gets the label of this ImageMainObjectDetectionInstance.

        主体的类别，现阶段分为：bounding_box和main_object_box

        :return: The label of this ImageMainObjectDetectionInstance.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this ImageMainObjectDetectionInstance.

        主体的类别，现阶段分为：bounding_box和main_object_box

        :param label: The label of this ImageMainObjectDetectionInstance.
        :type label: str
        """
        self._label = label

    @property
    def location(self):
        """Gets the location of this ImageMainObjectDetectionInstance.

         目标检测框位置信息，包括4个值：  width：检测框区域宽度  height：检测框区域高度  top_left_x：检测框左上角到垂直轴距离  top_left_y：检测框左上角到水平轴距离 properties: width: type: string description: 检测框区域高度 example: 139.58 height: type: string description: 检测框区域高度 example: 261.32 top_left_x: type: string description: 检测框左上角到垂直轴距离 example: 256.13 top_left_y: type: string description: 检测框左上角到水平轴距离 example: 85.2 

        :return: The location of this ImageMainObjectDetectionInstance.
        :rtype: object
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this ImageMainObjectDetectionInstance.

         目标检测框位置信息，包括4个值：  width：检测框区域宽度  height：检测框区域高度  top_left_x：检测框左上角到垂直轴距离  top_left_y：检测框左上角到水平轴距离 properties: width: type: string description: 检测框区域高度 example: 139.58 height: type: string description: 检测框区域高度 example: 261.32 top_left_x: type: string description: 检测框左上角到垂直轴距离 example: 256.13 top_left_y: type: string description: 检测框左上角到水平轴距离 example: 85.2 

        :param location: The location of this ImageMainObjectDetectionInstance.
        :type location: object
        """
        self._location = location

    @property
    def confidence(self):
        """Gets the confidence of this ImageMainObjectDetectionInstance.

        主体框的置信度,将Float型置信度转为String类型返回,Float取值范围（0~100）。

        :return: The confidence of this ImageMainObjectDetectionInstance.
        :rtype: str
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        """Sets the confidence of this ImageMainObjectDetectionInstance.

        主体框的置信度,将Float型置信度转为String类型返回,Float取值范围（0~100）。

        :param confidence: The confidence of this ImageMainObjectDetectionInstance.
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
        if not isinstance(other, ImageMainObjectDetectionInstance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
