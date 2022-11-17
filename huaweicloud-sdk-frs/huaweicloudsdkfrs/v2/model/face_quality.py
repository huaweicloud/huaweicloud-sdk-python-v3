# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FaceQuality:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_score': 'float',
        'blur': 'float',
        'pose': 'float',
        'occlusion': 'float',
        'illumination': 'float'
    }

    attribute_map = {
        'total_score': 'total_score',
        'blur': 'blur',
        'pose': 'pose',
        'occlusion': 'occlusion',
        'illumination': 'illumination'
    }

    def __init__(self, total_score=None, blur=None, pose=None, occlusion=None, illumination=None):
        """FaceQuality

        The model defined in huaweicloud sdk

        :param total_score: 人脸质量总分，取值范围[0-1]，分值越大质量越高。
        :type total_score: float
        :param blur: 模糊度，取值范围[0-1]，分值越大模糊问题越严重。
        :type blur: float
        :param pose: 姿态，取值范围[0-1]，分值越大姿态问题越严重。
        :type pose: float
        :param occlusion: 遮挡，取值范围[0-1]，分值越大遮挡问题越严重。
        :type occlusion: float
        :param illumination: 光照，取值范围[0-1]，分值越大光照问题越严重。
        :type illumination: float
        """
        
        

        self._total_score = None
        self._blur = None
        self._pose = None
        self._occlusion = None
        self._illumination = None
        self.discriminator = None

        self.total_score = total_score
        self.blur = blur
        self.pose = pose
        self.occlusion = occlusion
        self.illumination = illumination

    @property
    def total_score(self):
        """Gets the total_score of this FaceQuality.

        人脸质量总分，取值范围[0-1]，分值越大质量越高。

        :return: The total_score of this FaceQuality.
        :rtype: float
        """
        return self._total_score

    @total_score.setter
    def total_score(self, total_score):
        """Sets the total_score of this FaceQuality.

        人脸质量总分，取值范围[0-1]，分值越大质量越高。

        :param total_score: The total_score of this FaceQuality.
        :type total_score: float
        """
        self._total_score = total_score

    @property
    def blur(self):
        """Gets the blur of this FaceQuality.

        模糊度，取值范围[0-1]，分值越大模糊问题越严重。

        :return: The blur of this FaceQuality.
        :rtype: float
        """
        return self._blur

    @blur.setter
    def blur(self, blur):
        """Sets the blur of this FaceQuality.

        模糊度，取值范围[0-1]，分值越大模糊问题越严重。

        :param blur: The blur of this FaceQuality.
        :type blur: float
        """
        self._blur = blur

    @property
    def pose(self):
        """Gets the pose of this FaceQuality.

        姿态，取值范围[0-1]，分值越大姿态问题越严重。

        :return: The pose of this FaceQuality.
        :rtype: float
        """
        return self._pose

    @pose.setter
    def pose(self, pose):
        """Sets the pose of this FaceQuality.

        姿态，取值范围[0-1]，分值越大姿态问题越严重。

        :param pose: The pose of this FaceQuality.
        :type pose: float
        """
        self._pose = pose

    @property
    def occlusion(self):
        """Gets the occlusion of this FaceQuality.

        遮挡，取值范围[0-1]，分值越大遮挡问题越严重。

        :return: The occlusion of this FaceQuality.
        :rtype: float
        """
        return self._occlusion

    @occlusion.setter
    def occlusion(self, occlusion):
        """Sets the occlusion of this FaceQuality.

        遮挡，取值范围[0-1]，分值越大遮挡问题越严重。

        :param occlusion: The occlusion of this FaceQuality.
        :type occlusion: float
        """
        self._occlusion = occlusion

    @property
    def illumination(self):
        """Gets the illumination of this FaceQuality.

        光照，取值范围[0-1]，分值越大光照问题越严重。

        :return: The illumination of this FaceQuality.
        :rtype: float
        """
        return self._illumination

    @illumination.setter
    def illumination(self, illumination):
        """Sets the illumination of this FaceQuality.

        光照，取值范围[0-1]，分值越大光照问题越严重。

        :param illumination: The illumination of this FaceQuality.
        :type illumination: float
        """
        self._illumination = illumination

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
        if not isinstance(other, FaceQuality):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
