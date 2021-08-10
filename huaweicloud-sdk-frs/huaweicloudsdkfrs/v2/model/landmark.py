# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Landmark:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'eyes_contour': 'list[Point]',
        'mouth_contour': 'list[Point]',
        'face_contour': 'list[Point]',
        'eyebrow_contour': 'list[dict(str, Point)]',
        'nose_contour': 'list[Point]'
    }

    attribute_map = {
        'eyes_contour': 'eyes_contour',
        'mouth_contour': 'mouth_contour',
        'face_contour': 'face_contour',
        'eyebrow_contour': 'eyebrow_contour',
        'nose_contour': 'nose_contour'
    }

    def __init__(self, eyes_contour=None, mouth_contour=None, face_contour=None, eyebrow_contour=None, nose_contour=None):
        """Landmark - a model defined in huaweicloud sdk"""
        
        

        self._eyes_contour = None
        self._mouth_contour = None
        self._face_contour = None
        self._eyebrow_contour = None
        self._nose_contour = None
        self.discriminator = None

        self.eyes_contour = eyes_contour
        self.mouth_contour = mouth_contour
        self.face_contour = face_contour
        self.eyebrow_contour = eyebrow_contour
        self.nose_contour = nose_contour

    @property
    def eyes_contour(self):
        """Gets the eyes_contour of this Landmark.

        眼睛轮廓，Point为轮廓坐标值。

        :return: The eyes_contour of this Landmark.
        :rtype: list[Point]
        """
        return self._eyes_contour

    @eyes_contour.setter
    def eyes_contour(self, eyes_contour):
        """Sets the eyes_contour of this Landmark.

        眼睛轮廓，Point为轮廓坐标值。

        :param eyes_contour: The eyes_contour of this Landmark.
        :type: list[Point]
        """
        self._eyes_contour = eyes_contour

    @property
    def mouth_contour(self):
        """Gets the mouth_contour of this Landmark.

        嘴巴轮廓，Point为轮廓坐标值。

        :return: The mouth_contour of this Landmark.
        :rtype: list[Point]
        """
        return self._mouth_contour

    @mouth_contour.setter
    def mouth_contour(self, mouth_contour):
        """Sets the mouth_contour of this Landmark.

        嘴巴轮廓，Point为轮廓坐标值。

        :param mouth_contour: The mouth_contour of this Landmark.
        :type: list[Point]
        """
        self._mouth_contour = mouth_contour

    @property
    def face_contour(self):
        """Gets the face_contour of this Landmark.

        人脸轮廓，Point为轮廓坐标值。

        :return: The face_contour of this Landmark.
        :rtype: list[Point]
        """
        return self._face_contour

    @face_contour.setter
    def face_contour(self, face_contour):
        """Sets the face_contour of this Landmark.

        人脸轮廓，Point为轮廓坐标值。

        :param face_contour: The face_contour of this Landmark.
        :type: list[Point]
        """
        self._face_contour = face_contour

    @property
    def eyebrow_contour(self):
        """Gets the eyebrow_contour of this Landmark.

        眉毛轮廓，Point为轮廓坐标值。

        :return: The eyebrow_contour of this Landmark.
        :rtype: list[dict(str, Point)]
        """
        return self._eyebrow_contour

    @eyebrow_contour.setter
    def eyebrow_contour(self, eyebrow_contour):
        """Sets the eyebrow_contour of this Landmark.

        眉毛轮廓，Point为轮廓坐标值。

        :param eyebrow_contour: The eyebrow_contour of this Landmark.
        :type: list[dict(str, Point)]
        """
        self._eyebrow_contour = eyebrow_contour

    @property
    def nose_contour(self):
        """Gets the nose_contour of this Landmark.

        鼻子轮廓，Point为轮廓坐标值。

        :return: The nose_contour of this Landmark.
        :rtype: list[Point]
        """
        return self._nose_contour

    @nose_contour.setter
    def nose_contour(self, nose_contour):
        """Sets the nose_contour of this Landmark.

        鼻子轮廓，Point为轮廓坐标值。

        :param nose_contour: The nose_contour of this Landmark.
        :type: list[Point]
        """
        self._nose_contour = nose_contour

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
        if not isinstance(other, Landmark):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
