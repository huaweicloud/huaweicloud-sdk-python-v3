# coding: utf-8

import pprint
import re

import six





class CelebrityRecognitionResultBody:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'confidence': 'float',
        'face_detail': 'object',
        'label': 'str'
    }

    attribute_map = {
        'confidence': 'confidence',
        'face_detail': 'face_detail',
        'label': 'label'
    }

    def __init__(self, confidence=None, face_detail=None, label=None):
        """CelebrityRecognitionResultBody - a model defined in huaweicloud sdk"""
        
        

        self._confidence = None
        self._face_detail = None
        self._label = None
        self.discriminator = None

        if confidence is not None:
            self.confidence = confidence
        if face_detail is not None:
            self.face_detail = face_detail
        if label is not None:
            self.label = label

    @property
    def confidence(self):
        """Gets the confidence of this CelebrityRecognitionResultBody.

        置信度，取值范围 0-1。

        :return: The confidence of this CelebrityRecognitionResultBody.
        :rtype: float
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        """Sets the confidence of this CelebrityRecognitionResultBody.

        置信度，取值范围 0-1。

        :param confidence: The confidence of this CelebrityRecognitionResultBody.
        :type: float
        """
        self._confidence = confidence

    @property
    def face_detail(self):
        """Gets the face_detail of this CelebrityRecognitionResultBody.

        politics场景中的人物面部信息，包括4个值：  h：人脸区域高度  w：人脸区域宽度  x：人脸区域左上角到y轴距离  y：人脸区域左上角到x轴距离 

        :return: The face_detail of this CelebrityRecognitionResultBody.
        :rtype: object
        """
        return self._face_detail

    @face_detail.setter
    def face_detail(self, face_detail):
        """Sets the face_detail of this CelebrityRecognitionResultBody.

        politics场景中的人物面部信息，包括4个值：  h：人脸区域高度  w：人脸区域宽度  x：人脸区域左上角到y轴距离  y：人脸区域左上角到x轴距离 

        :param face_detail: The face_detail of this CelebrityRecognitionResultBody.
        :type: object
        """
        self._face_detail = face_detail

    @property
    def label(self):
        """Gets the label of this CelebrityRecognitionResultBody.

        label为对应的名人信息。

        :return: The label of this CelebrityRecognitionResultBody.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this CelebrityRecognitionResultBody.

        label为对应的名人信息。

        :param label: The label of this CelebrityRecognitionResultBody.
        :type: str
        """
        self._label = label

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CelebrityRecognitionResultBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
