# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IdcardScoreInfoResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tampering_score': 'int',
        'interim_score': 'int',
        'reproduce_score': 'int',
        'copy_score': 'int',
        'border_integrity_score': 'int',
        'blur_score': 'int',
        'glare_score': 'int',
        'blocking_within_border_score': 'int'
    }

    attribute_map = {
        'tampering_score': 'tampering_score',
        'interim_score': 'interim_score',
        'reproduce_score': 'reproduce_score',
        'copy_score': 'copy_score',
        'border_integrity_score': 'border_integrity_score',
        'blur_score': 'blur_score',
        'glare_score': 'glare_score',
        'blocking_within_border_score': 'blocking_within_border_score'
    }

    def __init__(self, tampering_score=None, interim_score=None, reproduce_score=None, copy_score=None, border_integrity_score=None, blur_score=None, glare_score=None, blocking_within_border_score=None):
        r"""IdcardScoreInfoResult

        The model defined in huaweicloud sdk

        :param tampering_score: 身份证PS告警分数，分数越高，PS的可能性越高。 仅在传入参数detect_tampering为true时，返回该字段。 
        :type tampering_score: int
        :param interim_score: 临时身份证告警分数，分数越高，临时身份证的可能性越高。 仅在传入参数detect_interim为true时，返回该字段。 
        :type interim_score: int
        :param reproduce_score: 身份证翻拍告警分数，分数越高，身份证图像经过翻拍的可能性越高。 仅在传入参数detect_reproduce为true时，返回该字段。 
        :type reproduce_score: int
        :param copy_score: 身份证复印告警分数, 分数越高，身份证图像是复印件的可能性越高。 仅在传入参数detect_copy为true时，返回该字段。 
        :type copy_score: int
        :param border_integrity_score: 身份证边缘完整性告警的分数，分数越高，身份证图像边缘不完整的可能性越高。 仅在传入参数detect_border_integrity为true时，返回该字段。 
        :type border_integrity_score: int
        :param blur_score: 身份证模糊告警分数，分数越高，身份证图像模糊的可能性越高。 仅在传入参数detect_blur为true时，返回该字段。 
        :type blur_score: int
        :param glare_score: 身份证反光告警分数，分数越高，身份证图像存在反光的可能性越高。 仅在传入参数detect_glare为true时，返回该字段。 
        :type glare_score: int
        :param blocking_within_border_score: 身份证图像框内是否有遮挡的告警分数，分数越高，身份证图像框内存在异物遮挡的可能性越高。 仅在传入参数detect_blocking_within_border为true时，返回该字段。 
        :type blocking_within_border_score: int
        """
        
        

        self._tampering_score = None
        self._interim_score = None
        self._reproduce_score = None
        self._copy_score = None
        self._border_integrity_score = None
        self._blur_score = None
        self._glare_score = None
        self._blocking_within_border_score = None
        self.discriminator = None

        if tampering_score is not None:
            self.tampering_score = tampering_score
        if interim_score is not None:
            self.interim_score = interim_score
        if reproduce_score is not None:
            self.reproduce_score = reproduce_score
        if copy_score is not None:
            self.copy_score = copy_score
        if border_integrity_score is not None:
            self.border_integrity_score = border_integrity_score
        if blur_score is not None:
            self.blur_score = blur_score
        if glare_score is not None:
            self.glare_score = glare_score
        if blocking_within_border_score is not None:
            self.blocking_within_border_score = blocking_within_border_score

    @property
    def tampering_score(self):
        r"""Gets the tampering_score of this IdcardScoreInfoResult.

        身份证PS告警分数，分数越高，PS的可能性越高。 仅在传入参数detect_tampering为true时，返回该字段。 

        :return: The tampering_score of this IdcardScoreInfoResult.
        :rtype: int
        """
        return self._tampering_score

    @tampering_score.setter
    def tampering_score(self, tampering_score):
        r"""Sets the tampering_score of this IdcardScoreInfoResult.

        身份证PS告警分数，分数越高，PS的可能性越高。 仅在传入参数detect_tampering为true时，返回该字段。 

        :param tampering_score: The tampering_score of this IdcardScoreInfoResult.
        :type tampering_score: int
        """
        self._tampering_score = tampering_score

    @property
    def interim_score(self):
        r"""Gets the interim_score of this IdcardScoreInfoResult.

        临时身份证告警分数，分数越高，临时身份证的可能性越高。 仅在传入参数detect_interim为true时，返回该字段。 

        :return: The interim_score of this IdcardScoreInfoResult.
        :rtype: int
        """
        return self._interim_score

    @interim_score.setter
    def interim_score(self, interim_score):
        r"""Sets the interim_score of this IdcardScoreInfoResult.

        临时身份证告警分数，分数越高，临时身份证的可能性越高。 仅在传入参数detect_interim为true时，返回该字段。 

        :param interim_score: The interim_score of this IdcardScoreInfoResult.
        :type interim_score: int
        """
        self._interim_score = interim_score

    @property
    def reproduce_score(self):
        r"""Gets the reproduce_score of this IdcardScoreInfoResult.

        身份证翻拍告警分数，分数越高，身份证图像经过翻拍的可能性越高。 仅在传入参数detect_reproduce为true时，返回该字段。 

        :return: The reproduce_score of this IdcardScoreInfoResult.
        :rtype: int
        """
        return self._reproduce_score

    @reproduce_score.setter
    def reproduce_score(self, reproduce_score):
        r"""Sets the reproduce_score of this IdcardScoreInfoResult.

        身份证翻拍告警分数，分数越高，身份证图像经过翻拍的可能性越高。 仅在传入参数detect_reproduce为true时，返回该字段。 

        :param reproduce_score: The reproduce_score of this IdcardScoreInfoResult.
        :type reproduce_score: int
        """
        self._reproduce_score = reproduce_score

    @property
    def copy_score(self):
        r"""Gets the copy_score of this IdcardScoreInfoResult.

        身份证复印告警分数, 分数越高，身份证图像是复印件的可能性越高。 仅在传入参数detect_copy为true时，返回该字段。 

        :return: The copy_score of this IdcardScoreInfoResult.
        :rtype: int
        """
        return self._copy_score

    @copy_score.setter
    def copy_score(self, copy_score):
        r"""Sets the copy_score of this IdcardScoreInfoResult.

        身份证复印告警分数, 分数越高，身份证图像是复印件的可能性越高。 仅在传入参数detect_copy为true时，返回该字段。 

        :param copy_score: The copy_score of this IdcardScoreInfoResult.
        :type copy_score: int
        """
        self._copy_score = copy_score

    @property
    def border_integrity_score(self):
        r"""Gets the border_integrity_score of this IdcardScoreInfoResult.

        身份证边缘完整性告警的分数，分数越高，身份证图像边缘不完整的可能性越高。 仅在传入参数detect_border_integrity为true时，返回该字段。 

        :return: The border_integrity_score of this IdcardScoreInfoResult.
        :rtype: int
        """
        return self._border_integrity_score

    @border_integrity_score.setter
    def border_integrity_score(self, border_integrity_score):
        r"""Sets the border_integrity_score of this IdcardScoreInfoResult.

        身份证边缘完整性告警的分数，分数越高，身份证图像边缘不完整的可能性越高。 仅在传入参数detect_border_integrity为true时，返回该字段。 

        :param border_integrity_score: The border_integrity_score of this IdcardScoreInfoResult.
        :type border_integrity_score: int
        """
        self._border_integrity_score = border_integrity_score

    @property
    def blur_score(self):
        r"""Gets the blur_score of this IdcardScoreInfoResult.

        身份证模糊告警分数，分数越高，身份证图像模糊的可能性越高。 仅在传入参数detect_blur为true时，返回该字段。 

        :return: The blur_score of this IdcardScoreInfoResult.
        :rtype: int
        """
        return self._blur_score

    @blur_score.setter
    def blur_score(self, blur_score):
        r"""Sets the blur_score of this IdcardScoreInfoResult.

        身份证模糊告警分数，分数越高，身份证图像模糊的可能性越高。 仅在传入参数detect_blur为true时，返回该字段。 

        :param blur_score: The blur_score of this IdcardScoreInfoResult.
        :type blur_score: int
        """
        self._blur_score = blur_score

    @property
    def glare_score(self):
        r"""Gets the glare_score of this IdcardScoreInfoResult.

        身份证反光告警分数，分数越高，身份证图像存在反光的可能性越高。 仅在传入参数detect_glare为true时，返回该字段。 

        :return: The glare_score of this IdcardScoreInfoResult.
        :rtype: int
        """
        return self._glare_score

    @glare_score.setter
    def glare_score(self, glare_score):
        r"""Sets the glare_score of this IdcardScoreInfoResult.

        身份证反光告警分数，分数越高，身份证图像存在反光的可能性越高。 仅在传入参数detect_glare为true时，返回该字段。 

        :param glare_score: The glare_score of this IdcardScoreInfoResult.
        :type glare_score: int
        """
        self._glare_score = glare_score

    @property
    def blocking_within_border_score(self):
        r"""Gets the blocking_within_border_score of this IdcardScoreInfoResult.

        身份证图像框内是否有遮挡的告警分数，分数越高，身份证图像框内存在异物遮挡的可能性越高。 仅在传入参数detect_blocking_within_border为true时，返回该字段。 

        :return: The blocking_within_border_score of this IdcardScoreInfoResult.
        :rtype: int
        """
        return self._blocking_within_border_score

    @blocking_within_border_score.setter
    def blocking_within_border_score(self, blocking_within_border_score):
        r"""Sets the blocking_within_border_score of this IdcardScoreInfoResult.

        身份证图像框内是否有遮挡的告警分数，分数越高，身份证图像框内存在异物遮挡的可能性越高。 仅在传入参数detect_blocking_within_border为true时，返回该字段。 

        :param blocking_within_border_score: The blocking_within_border_score of this IdcardScoreInfoResult.
        :type blocking_within_border_score: int
        """
        self._blocking_within_border_score = blocking_within_border_score

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
        if not isinstance(other, IdcardScoreInfoResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
