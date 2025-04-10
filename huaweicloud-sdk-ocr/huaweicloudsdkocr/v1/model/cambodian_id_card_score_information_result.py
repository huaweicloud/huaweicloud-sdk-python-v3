# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CambodianIdCardScoreInformationResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'idcard_type_score': 'int',
        'border_integrity_score': 'int',
        'blocking_within_border_score': 'int',
        'blur_score': 'int',
        'glare_score': 'int',
        'tampering_score': 'int',
        'reproduce_score': 'int'
    }

    attribute_map = {
        'idcard_type_score': 'idcard_type_score',
        'border_integrity_score': 'border_integrity_score',
        'blocking_within_border_score': 'blocking_within_border_score',
        'blur_score': 'blur_score',
        'glare_score': 'glare_score',
        'tampering_score': 'tampering_score',
        'reproduce_score': 'reproduce_score'
    }

    def __init__(self, idcard_type_score=None, border_integrity_score=None, blocking_within_border_score=None, blur_score=None, glare_score=None, tampering_score=None, reproduce_score=None):
        r"""CambodianIdCardScoreInformationResult

        The model defined in huaweicloud sdk

        :param idcard_type_score: 告警分数，字段取值范围[0, 99]值大于50表示复印件，小于等于50表示原件，值越靠近99，表示复印件的可能性越大，值越靠近0，表示原件的可能性越大。  仅在传入参数return_idcard_type为true时，返回该字段。 
        :type idcard_type_score: int
        :param border_integrity_score: 告警分数，字段取值范围[0, 99]值大于50表示边框不完整，小于50表示边框完整，值越靠近99，表示边框不完整的可能性越大，值越靠近0，表示边框完整的可能性越大。 仅在传入参数detect_border_integrity为true时，返回该字段。 
        :type border_integrity_score: int
        :param blocking_within_border_score: 告警分数，字段取值范围[0, 99]值大于50表示框内有遮挡，小于50表示框内无遮挡，值越靠近99，表示框内有遮挡的可能性越大，值越靠近0，表示框内无遮挡的可能性越大。 仅在传入参数detect_blocking_within_border为true时，返回该字段。 
        :type blocking_within_border_score: int
        :param blur_score: 告警分数，字段取值范围[0, 99]值大于50表示身份证模糊，小于50表示身份证清晰，值越靠近99，表示身份证模糊的可能性越大，值越靠近0，表示身份证清晰的可能性越大。 仅在传入参数detect_blur为true时，返回该字段。 
        :type blur_score: int
        :param glare_score: 告警分数，字段取值范围[0, 99]值大于50表示身份证反光，小于50表示身份证不反光，值越靠近99，表示身份证反光的可能性越大，值越靠近0，表示身份证不反光的可能性越大。 仅在传入参数detect_glare为true时，返回该字段。 
        :type glare_score: int
        :param tampering_score: 告警分数，字段取值范围[0, 99]值大于50表示身份证人像被其他非身份证人像篡改过，小于50表示身份证人像未被篡改，值越靠近99，表示身份证人像被篡改的可能性越大，值越靠近0，表示身份证未人像被篡改的可能性越大。 仅在传入参数detect_tampering为true时，返回该字段。 
        :type tampering_score: int
        :param reproduce_score: 告警分数，字段取值范围[0, 99]值大于50表示身份证经过翻拍，小于50表示身份证未经过翻拍，值越靠近99，表示身份证图像被翻拍过的可能性越大，值越靠近0，表示身份证图像未被翻拍的可能性越大。 仅在传入参数detect_reproduce为true时，返回该字段。 
        :type reproduce_score: int
        """
        
        

        self._idcard_type_score = None
        self._border_integrity_score = None
        self._blocking_within_border_score = None
        self._blur_score = None
        self._glare_score = None
        self._tampering_score = None
        self._reproduce_score = None
        self.discriminator = None

        if idcard_type_score is not None:
            self.idcard_type_score = idcard_type_score
        if border_integrity_score is not None:
            self.border_integrity_score = border_integrity_score
        if blocking_within_border_score is not None:
            self.blocking_within_border_score = blocking_within_border_score
        if blur_score is not None:
            self.blur_score = blur_score
        if glare_score is not None:
            self.glare_score = glare_score
        if tampering_score is not None:
            self.tampering_score = tampering_score
        if reproduce_score is not None:
            self.reproduce_score = reproduce_score

    @property
    def idcard_type_score(self):
        r"""Gets the idcard_type_score of this CambodianIdCardScoreInformationResult.

        告警分数，字段取值范围[0, 99]值大于50表示复印件，小于等于50表示原件，值越靠近99，表示复印件的可能性越大，值越靠近0，表示原件的可能性越大。  仅在传入参数return_idcard_type为true时，返回该字段。 

        :return: The idcard_type_score of this CambodianIdCardScoreInformationResult.
        :rtype: int
        """
        return self._idcard_type_score

    @idcard_type_score.setter
    def idcard_type_score(self, idcard_type_score):
        r"""Sets the idcard_type_score of this CambodianIdCardScoreInformationResult.

        告警分数，字段取值范围[0, 99]值大于50表示复印件，小于等于50表示原件，值越靠近99，表示复印件的可能性越大，值越靠近0，表示原件的可能性越大。  仅在传入参数return_idcard_type为true时，返回该字段。 

        :param idcard_type_score: The idcard_type_score of this CambodianIdCardScoreInformationResult.
        :type idcard_type_score: int
        """
        self._idcard_type_score = idcard_type_score

    @property
    def border_integrity_score(self):
        r"""Gets the border_integrity_score of this CambodianIdCardScoreInformationResult.

        告警分数，字段取值范围[0, 99]值大于50表示边框不完整，小于50表示边框完整，值越靠近99，表示边框不完整的可能性越大，值越靠近0，表示边框完整的可能性越大。 仅在传入参数detect_border_integrity为true时，返回该字段。 

        :return: The border_integrity_score of this CambodianIdCardScoreInformationResult.
        :rtype: int
        """
        return self._border_integrity_score

    @border_integrity_score.setter
    def border_integrity_score(self, border_integrity_score):
        r"""Sets the border_integrity_score of this CambodianIdCardScoreInformationResult.

        告警分数，字段取值范围[0, 99]值大于50表示边框不完整，小于50表示边框完整，值越靠近99，表示边框不完整的可能性越大，值越靠近0，表示边框完整的可能性越大。 仅在传入参数detect_border_integrity为true时，返回该字段。 

        :param border_integrity_score: The border_integrity_score of this CambodianIdCardScoreInformationResult.
        :type border_integrity_score: int
        """
        self._border_integrity_score = border_integrity_score

    @property
    def blocking_within_border_score(self):
        r"""Gets the blocking_within_border_score of this CambodianIdCardScoreInformationResult.

        告警分数，字段取值范围[0, 99]值大于50表示框内有遮挡，小于50表示框内无遮挡，值越靠近99，表示框内有遮挡的可能性越大，值越靠近0，表示框内无遮挡的可能性越大。 仅在传入参数detect_blocking_within_border为true时，返回该字段。 

        :return: The blocking_within_border_score of this CambodianIdCardScoreInformationResult.
        :rtype: int
        """
        return self._blocking_within_border_score

    @blocking_within_border_score.setter
    def blocking_within_border_score(self, blocking_within_border_score):
        r"""Sets the blocking_within_border_score of this CambodianIdCardScoreInformationResult.

        告警分数，字段取值范围[0, 99]值大于50表示框内有遮挡，小于50表示框内无遮挡，值越靠近99，表示框内有遮挡的可能性越大，值越靠近0，表示框内无遮挡的可能性越大。 仅在传入参数detect_blocking_within_border为true时，返回该字段。 

        :param blocking_within_border_score: The blocking_within_border_score of this CambodianIdCardScoreInformationResult.
        :type blocking_within_border_score: int
        """
        self._blocking_within_border_score = blocking_within_border_score

    @property
    def blur_score(self):
        r"""Gets the blur_score of this CambodianIdCardScoreInformationResult.

        告警分数，字段取值范围[0, 99]值大于50表示身份证模糊，小于50表示身份证清晰，值越靠近99，表示身份证模糊的可能性越大，值越靠近0，表示身份证清晰的可能性越大。 仅在传入参数detect_blur为true时，返回该字段。 

        :return: The blur_score of this CambodianIdCardScoreInformationResult.
        :rtype: int
        """
        return self._blur_score

    @blur_score.setter
    def blur_score(self, blur_score):
        r"""Sets the blur_score of this CambodianIdCardScoreInformationResult.

        告警分数，字段取值范围[0, 99]值大于50表示身份证模糊，小于50表示身份证清晰，值越靠近99，表示身份证模糊的可能性越大，值越靠近0，表示身份证清晰的可能性越大。 仅在传入参数detect_blur为true时，返回该字段。 

        :param blur_score: The blur_score of this CambodianIdCardScoreInformationResult.
        :type blur_score: int
        """
        self._blur_score = blur_score

    @property
    def glare_score(self):
        r"""Gets the glare_score of this CambodianIdCardScoreInformationResult.

        告警分数，字段取值范围[0, 99]值大于50表示身份证反光，小于50表示身份证不反光，值越靠近99，表示身份证反光的可能性越大，值越靠近0，表示身份证不反光的可能性越大。 仅在传入参数detect_glare为true时，返回该字段。 

        :return: The glare_score of this CambodianIdCardScoreInformationResult.
        :rtype: int
        """
        return self._glare_score

    @glare_score.setter
    def glare_score(self, glare_score):
        r"""Sets the glare_score of this CambodianIdCardScoreInformationResult.

        告警分数，字段取值范围[0, 99]值大于50表示身份证反光，小于50表示身份证不反光，值越靠近99，表示身份证反光的可能性越大，值越靠近0，表示身份证不反光的可能性越大。 仅在传入参数detect_glare为true时，返回该字段。 

        :param glare_score: The glare_score of this CambodianIdCardScoreInformationResult.
        :type glare_score: int
        """
        self._glare_score = glare_score

    @property
    def tampering_score(self):
        r"""Gets the tampering_score of this CambodianIdCardScoreInformationResult.

        告警分数，字段取值范围[0, 99]值大于50表示身份证人像被其他非身份证人像篡改过，小于50表示身份证人像未被篡改，值越靠近99，表示身份证人像被篡改的可能性越大，值越靠近0，表示身份证未人像被篡改的可能性越大。 仅在传入参数detect_tampering为true时，返回该字段。 

        :return: The tampering_score of this CambodianIdCardScoreInformationResult.
        :rtype: int
        """
        return self._tampering_score

    @tampering_score.setter
    def tampering_score(self, tampering_score):
        r"""Sets the tampering_score of this CambodianIdCardScoreInformationResult.

        告警分数，字段取值范围[0, 99]值大于50表示身份证人像被其他非身份证人像篡改过，小于50表示身份证人像未被篡改，值越靠近99，表示身份证人像被篡改的可能性越大，值越靠近0，表示身份证未人像被篡改的可能性越大。 仅在传入参数detect_tampering为true时，返回该字段。 

        :param tampering_score: The tampering_score of this CambodianIdCardScoreInformationResult.
        :type tampering_score: int
        """
        self._tampering_score = tampering_score

    @property
    def reproduce_score(self):
        r"""Gets the reproduce_score of this CambodianIdCardScoreInformationResult.

        告警分数，字段取值范围[0, 99]值大于50表示身份证经过翻拍，小于50表示身份证未经过翻拍，值越靠近99，表示身份证图像被翻拍过的可能性越大，值越靠近0，表示身份证图像未被翻拍的可能性越大。 仅在传入参数detect_reproduce为true时，返回该字段。 

        :return: The reproduce_score of this CambodianIdCardScoreInformationResult.
        :rtype: int
        """
        return self._reproduce_score

    @reproduce_score.setter
    def reproduce_score(self, reproduce_score):
        r"""Sets the reproduce_score of this CambodianIdCardScoreInformationResult.

        告警分数，字段取值范围[0, 99]值大于50表示身份证经过翻拍，小于50表示身份证未经过翻拍，值越靠近99，表示身份证图像被翻拍过的可能性越大，值越靠近0，表示身份证图像未被翻拍的可能性越大。 仅在传入参数detect_reproduce为true时，返回该字段。 

        :param reproduce_score: The reproduce_score of this CambodianIdCardScoreInformationResult.
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
        if not isinstance(other, CambodianIdCardScoreInformationResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
