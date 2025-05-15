# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AutoIdDocClassificationAlarmConfidence:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'blur_score': 'int',
        'glare_score': 'int',
        'blocking_within_border_score': 'int',
        'insufficient_lighting_score': 'int',
        'copy_score': 'int',
        'border_integrity_score': 'int',
        'reproduce_score': 'int'
    }

    attribute_map = {
        'blur_score': 'blur_score',
        'glare_score': 'glare_score',
        'blocking_within_border_score': 'blocking_within_border_score',
        'insufficient_lighting_score': 'insufficient_lighting_score',
        'copy_score': 'copy_score',
        'border_integrity_score': 'border_integrity_score',
        'reproduce_score': 'reproduce_score'
    }

    def __init__(self, blur_score=None, glare_score=None, blocking_within_border_score=None, insufficient_lighting_score=None, copy_score=None, border_integrity_score=None, reproduce_score=None):
        r"""AutoIdDocClassificationAlarmConfidence

        The model defined in huaweicloud sdk

        :param blur_score: 证件图像模糊告警分数，分数越高，证件图像模糊的可能性越高。 
        :type blur_score: int
        :param glare_score: 证件图像反光告警分数，分数越高，证件图像反光的可能性越高。 
        :type glare_score: int
        :param blocking_within_border_score: 证件图像框内遮挡告警分数，分数越高，证件图像框内遮挡的可能性越高。 
        :type blocking_within_border_score: int
        :param insufficient_lighting_score: 证件图像过暗告警分数，分数越高，证件图像过暗的可能性越高。 
        :type insufficient_lighting_score: int
        :param copy_score: 证件图像复印件告警分数，分数越高，证件图像是复印件的可能性越高。 
        :type copy_score: int
        :param border_integrity_score: 证件图像边框完整性告警分数，分数越高，证件图像边框不完整的可能性越高。 
        :type border_integrity_score: int
        :param reproduce_score: 证件图像翻拍告警分数，分数越高，证件图像经过翻拍的可能性越高。 
        :type reproduce_score: int
        """
        
        

        self._blur_score = None
        self._glare_score = None
        self._blocking_within_border_score = None
        self._insufficient_lighting_score = None
        self._copy_score = None
        self._border_integrity_score = None
        self._reproduce_score = None
        self.discriminator = None

        if blur_score is not None:
            self.blur_score = blur_score
        if glare_score is not None:
            self.glare_score = glare_score
        if blocking_within_border_score is not None:
            self.blocking_within_border_score = blocking_within_border_score
        if insufficient_lighting_score is not None:
            self.insufficient_lighting_score = insufficient_lighting_score
        if copy_score is not None:
            self.copy_score = copy_score
        if border_integrity_score is not None:
            self.border_integrity_score = border_integrity_score
        if reproduce_score is not None:
            self.reproduce_score = reproduce_score

    @property
    def blur_score(self):
        r"""Gets the blur_score of this AutoIdDocClassificationAlarmConfidence.

        证件图像模糊告警分数，分数越高，证件图像模糊的可能性越高。 

        :return: The blur_score of this AutoIdDocClassificationAlarmConfidence.
        :rtype: int
        """
        return self._blur_score

    @blur_score.setter
    def blur_score(self, blur_score):
        r"""Sets the blur_score of this AutoIdDocClassificationAlarmConfidence.

        证件图像模糊告警分数，分数越高，证件图像模糊的可能性越高。 

        :param blur_score: The blur_score of this AutoIdDocClassificationAlarmConfidence.
        :type blur_score: int
        """
        self._blur_score = blur_score

    @property
    def glare_score(self):
        r"""Gets the glare_score of this AutoIdDocClassificationAlarmConfidence.

        证件图像反光告警分数，分数越高，证件图像反光的可能性越高。 

        :return: The glare_score of this AutoIdDocClassificationAlarmConfidence.
        :rtype: int
        """
        return self._glare_score

    @glare_score.setter
    def glare_score(self, glare_score):
        r"""Sets the glare_score of this AutoIdDocClassificationAlarmConfidence.

        证件图像反光告警分数，分数越高，证件图像反光的可能性越高。 

        :param glare_score: The glare_score of this AutoIdDocClassificationAlarmConfidence.
        :type glare_score: int
        """
        self._glare_score = glare_score

    @property
    def blocking_within_border_score(self):
        r"""Gets the blocking_within_border_score of this AutoIdDocClassificationAlarmConfidence.

        证件图像框内遮挡告警分数，分数越高，证件图像框内遮挡的可能性越高。 

        :return: The blocking_within_border_score of this AutoIdDocClassificationAlarmConfidence.
        :rtype: int
        """
        return self._blocking_within_border_score

    @blocking_within_border_score.setter
    def blocking_within_border_score(self, blocking_within_border_score):
        r"""Sets the blocking_within_border_score of this AutoIdDocClassificationAlarmConfidence.

        证件图像框内遮挡告警分数，分数越高，证件图像框内遮挡的可能性越高。 

        :param blocking_within_border_score: The blocking_within_border_score of this AutoIdDocClassificationAlarmConfidence.
        :type blocking_within_border_score: int
        """
        self._blocking_within_border_score = blocking_within_border_score

    @property
    def insufficient_lighting_score(self):
        r"""Gets the insufficient_lighting_score of this AutoIdDocClassificationAlarmConfidence.

        证件图像过暗告警分数，分数越高，证件图像过暗的可能性越高。 

        :return: The insufficient_lighting_score of this AutoIdDocClassificationAlarmConfidence.
        :rtype: int
        """
        return self._insufficient_lighting_score

    @insufficient_lighting_score.setter
    def insufficient_lighting_score(self, insufficient_lighting_score):
        r"""Sets the insufficient_lighting_score of this AutoIdDocClassificationAlarmConfidence.

        证件图像过暗告警分数，分数越高，证件图像过暗的可能性越高。 

        :param insufficient_lighting_score: The insufficient_lighting_score of this AutoIdDocClassificationAlarmConfidence.
        :type insufficient_lighting_score: int
        """
        self._insufficient_lighting_score = insufficient_lighting_score

    @property
    def copy_score(self):
        r"""Gets the copy_score of this AutoIdDocClassificationAlarmConfidence.

        证件图像复印件告警分数，分数越高，证件图像是复印件的可能性越高。 

        :return: The copy_score of this AutoIdDocClassificationAlarmConfidence.
        :rtype: int
        """
        return self._copy_score

    @copy_score.setter
    def copy_score(self, copy_score):
        r"""Sets the copy_score of this AutoIdDocClassificationAlarmConfidence.

        证件图像复印件告警分数，分数越高，证件图像是复印件的可能性越高。 

        :param copy_score: The copy_score of this AutoIdDocClassificationAlarmConfidence.
        :type copy_score: int
        """
        self._copy_score = copy_score

    @property
    def border_integrity_score(self):
        r"""Gets the border_integrity_score of this AutoIdDocClassificationAlarmConfidence.

        证件图像边框完整性告警分数，分数越高，证件图像边框不完整的可能性越高。 

        :return: The border_integrity_score of this AutoIdDocClassificationAlarmConfidence.
        :rtype: int
        """
        return self._border_integrity_score

    @border_integrity_score.setter
    def border_integrity_score(self, border_integrity_score):
        r"""Sets the border_integrity_score of this AutoIdDocClassificationAlarmConfidence.

        证件图像边框完整性告警分数，分数越高，证件图像边框不完整的可能性越高。 

        :param border_integrity_score: The border_integrity_score of this AutoIdDocClassificationAlarmConfidence.
        :type border_integrity_score: int
        """
        self._border_integrity_score = border_integrity_score

    @property
    def reproduce_score(self):
        r"""Gets the reproduce_score of this AutoIdDocClassificationAlarmConfidence.

        证件图像翻拍告警分数，分数越高，证件图像经过翻拍的可能性越高。 

        :return: The reproduce_score of this AutoIdDocClassificationAlarmConfidence.
        :rtype: int
        """
        return self._reproduce_score

    @reproduce_score.setter
    def reproduce_score(self, reproduce_score):
        r"""Sets the reproduce_score of this AutoIdDocClassificationAlarmConfidence.

        证件图像翻拍告警分数，分数越高，证件图像经过翻拍的可能性越高。 

        :param reproduce_score: The reproduce_score of this AutoIdDocClassificationAlarmConfidence.
        :type reproduce_score: int
        """
        self._reproduce_score = reproduce_score

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
        if not isinstance(other, AutoIdDocClassificationAlarmConfidence):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
