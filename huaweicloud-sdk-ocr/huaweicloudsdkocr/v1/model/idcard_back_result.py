# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IdcardBackResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'issue': 'str',
        'valid_from': 'str',
        'valid_to': 'str',
        'adjusted_image': 'str',
        'verification_result': 'IdcardBackVerificationResult',
        'text_location': 'object',
        'detect_reproduce_result': 'bool',
        'detect_copy_result': 'bool',
        'detect_tampering_result': 'bool',
        'detect_border_integrity_result': 'bool',
        'detect_blocking_within_border_result': 'bool',
        'detect_blur_result': 'bool',
        'detect_interim_result': 'bool',
        'detect_glare_result': 'bool',
        'score_info': 'IdcardScoreInfoResult'
    }

    attribute_map = {
        'issue': 'issue',
        'valid_from': 'valid_from',
        'valid_to': 'valid_to',
        'adjusted_image': 'adjusted_image',
        'verification_result': 'verification_result',
        'text_location': 'text_location',
        'detect_reproduce_result': 'detect_reproduce_result',
        'detect_copy_result': 'detect_copy_result',
        'detect_tampering_result': 'detect_tampering_result',
        'detect_border_integrity_result': 'detect_border_integrity_result',
        'detect_blocking_within_border_result': 'detect_blocking_within_border_result',
        'detect_blur_result': 'detect_blur_result',
        'detect_interim_result': 'detect_interim_result',
        'detect_glare_result': 'detect_glare_result',
        'score_info': 'score_info'
    }

    def __init__(self, issue=None, valid_from=None, valid_to=None, adjusted_image=None, verification_result=None, text_location=None, detect_reproduce_result=None, detect_copy_result=None, detect_tampering_result=None, detect_border_integrity_result=None, detect_blocking_within_border_result=None, detect_blur_result=None, detect_interim_result=None, detect_glare_result=None, score_info=None):
        r"""IdcardBackResult

        The model defined in huaweicloud sdk

        :param issue: 发证机关。 
        :type issue: str
        :param valid_from: 有效起始日期。 
        :type valid_from: str
        :param valid_to: 有效结束日期。 
        :type valid_to: str
        :param adjusted_image: 身份证卡面图片信息的base64码结果。  &gt; 说明： - 仅在输入参数return_adjusted_image为true时，返回该字段。 
        :type adjusted_image: str
        :param verification_result: 
        :type verification_result: :class:`huaweicloudsdkocr.v1.IdcardBackVerificationResult`
        :param text_location: 文本框在原图位置。输出左上、右上、右下、左下四个点坐标。 仅return_text_location设置为true时才返回。 
        :type text_location: object
        :param detect_reproduce_result: 身份证图像是否翻拍告警结果。 - true：表示身份证图片经过翻拍。 - false：表示身份证图片未经过翻拍。 仅在输入参数detect_reproduce为true时，返回该字段。 
        :type detect_reproduce_result: bool
        :param detect_copy_result: 身份证图像是否黑白复印件告警结果。 - true：表示身份证图片是复印件。 - false”表示身份证图片是原件。 仅在输入参数detect_copy为true时，返回该字段。 
        :type detect_copy_result: bool
        :param detect_tampering_result: 身份证图片是否PS告警结果。 - true：表示身份证经过PS。 - false：表示未经过PS。 仅在传入参数detect_tampering为true时，返回该字段。 
        :type detect_tampering_result: bool
        :param detect_border_integrity_result: 身份证图片边框完整性告警结果。 - true：表示边框不完整 - false：表示边框完整。 仅在输入参数detect_border_integrity为true时，返回该字段。 
        :type detect_border_integrity_result: bool
        :param detect_blocking_within_border_result: 身份证图像框内是否存在遮挡的告警结果。 - true：表示边框内部存在遮挡。 - false：表示边框内部不存在遮挡。 仅在输入参数detect_blocking_within_border为true时，返回该字段。 
        :type detect_blocking_within_border_result: bool
        :param detect_blur_result: 身份证模糊告警结果。 - true：表示身份证图片较模糊。 - false：表示身份证清晰。 仅在输入参数detect_blur为true时，返回该字段。 
        :type detect_blur_result: bool
        :param detect_interim_result: 临时身份证告警结果。 - true：表示是临时身份证。 - false：表示非临时身份证。 仅在输入参数detect_interim为true时，返回该字段。 
        :type detect_interim_result: bool
        :param detect_glare_result: 身份证反光告警结果。 - true：表示身份证图片存在反光。 - false：表示是身份证不存在反光。 仅在输入参数detect_glare为true时，返回该字段。 
        :type detect_glare_result: bool
        :param score_info: 
        :type score_info: :class:`huaweicloudsdkocr.v1.IdcardScoreInfoResult`
        """
        
        

        self._issue = None
        self._valid_from = None
        self._valid_to = None
        self._adjusted_image = None
        self._verification_result = None
        self._text_location = None
        self._detect_reproduce_result = None
        self._detect_copy_result = None
        self._detect_tampering_result = None
        self._detect_border_integrity_result = None
        self._detect_blocking_within_border_result = None
        self._detect_blur_result = None
        self._detect_interim_result = None
        self._detect_glare_result = None
        self._score_info = None
        self.discriminator = None

        if issue is not None:
            self.issue = issue
        if valid_from is not None:
            self.valid_from = valid_from
        if valid_to is not None:
            self.valid_to = valid_to
        if adjusted_image is not None:
            self.adjusted_image = adjusted_image
        if verification_result is not None:
            self.verification_result = verification_result
        if text_location is not None:
            self.text_location = text_location
        if detect_reproduce_result is not None:
            self.detect_reproduce_result = detect_reproduce_result
        if detect_copy_result is not None:
            self.detect_copy_result = detect_copy_result
        if detect_tampering_result is not None:
            self.detect_tampering_result = detect_tampering_result
        if detect_border_integrity_result is not None:
            self.detect_border_integrity_result = detect_border_integrity_result
        if detect_blocking_within_border_result is not None:
            self.detect_blocking_within_border_result = detect_blocking_within_border_result
        if detect_blur_result is not None:
            self.detect_blur_result = detect_blur_result
        if detect_interim_result is not None:
            self.detect_interim_result = detect_interim_result
        if detect_glare_result is not None:
            self.detect_glare_result = detect_glare_result
        if score_info is not None:
            self.score_info = score_info

    @property
    def issue(self):
        r"""Gets the issue of this IdcardBackResult.

        发证机关。 

        :return: The issue of this IdcardBackResult.
        :rtype: str
        """
        return self._issue

    @issue.setter
    def issue(self, issue):
        r"""Sets the issue of this IdcardBackResult.

        发证机关。 

        :param issue: The issue of this IdcardBackResult.
        :type issue: str
        """
        self._issue = issue

    @property
    def valid_from(self):
        r"""Gets the valid_from of this IdcardBackResult.

        有效起始日期。 

        :return: The valid_from of this IdcardBackResult.
        :rtype: str
        """
        return self._valid_from

    @valid_from.setter
    def valid_from(self, valid_from):
        r"""Sets the valid_from of this IdcardBackResult.

        有效起始日期。 

        :param valid_from: The valid_from of this IdcardBackResult.
        :type valid_from: str
        """
        self._valid_from = valid_from

    @property
    def valid_to(self):
        r"""Gets the valid_to of this IdcardBackResult.

        有效结束日期。 

        :return: The valid_to of this IdcardBackResult.
        :rtype: str
        """
        return self._valid_to

    @valid_to.setter
    def valid_to(self, valid_to):
        r"""Sets the valid_to of this IdcardBackResult.

        有效结束日期。 

        :param valid_to: The valid_to of this IdcardBackResult.
        :type valid_to: str
        """
        self._valid_to = valid_to

    @property
    def adjusted_image(self):
        r"""Gets the adjusted_image of this IdcardBackResult.

        身份证卡面图片信息的base64码结果。  > 说明： - 仅在输入参数return_adjusted_image为true时，返回该字段。 

        :return: The adjusted_image of this IdcardBackResult.
        :rtype: str
        """
        return self._adjusted_image

    @adjusted_image.setter
    def adjusted_image(self, adjusted_image):
        r"""Sets the adjusted_image of this IdcardBackResult.

        身份证卡面图片信息的base64码结果。  > 说明： - 仅在输入参数return_adjusted_image为true时，返回该字段。 

        :param adjusted_image: The adjusted_image of this IdcardBackResult.
        :type adjusted_image: str
        """
        self._adjusted_image = adjusted_image

    @property
    def verification_result(self):
        r"""Gets the verification_result of this IdcardBackResult.

        :return: The verification_result of this IdcardBackResult.
        :rtype: :class:`huaweicloudsdkocr.v1.IdcardBackVerificationResult`
        """
        return self._verification_result

    @verification_result.setter
    def verification_result(self, verification_result):
        r"""Sets the verification_result of this IdcardBackResult.

        :param verification_result: The verification_result of this IdcardBackResult.
        :type verification_result: :class:`huaweicloudsdkocr.v1.IdcardBackVerificationResult`
        """
        self._verification_result = verification_result

    @property
    def text_location(self):
        r"""Gets the text_location of this IdcardBackResult.

        文本框在原图位置。输出左上、右上、右下、左下四个点坐标。 仅return_text_location设置为true时才返回。 

        :return: The text_location of this IdcardBackResult.
        :rtype: object
        """
        return self._text_location

    @text_location.setter
    def text_location(self, text_location):
        r"""Sets the text_location of this IdcardBackResult.

        文本框在原图位置。输出左上、右上、右下、左下四个点坐标。 仅return_text_location设置为true时才返回。 

        :param text_location: The text_location of this IdcardBackResult.
        :type text_location: object
        """
        self._text_location = text_location

    @property
    def detect_reproduce_result(self):
        r"""Gets the detect_reproduce_result of this IdcardBackResult.

        身份证图像是否翻拍告警结果。 - true：表示身份证图片经过翻拍。 - false：表示身份证图片未经过翻拍。 仅在输入参数detect_reproduce为true时，返回该字段。 

        :return: The detect_reproduce_result of this IdcardBackResult.
        :rtype: bool
        """
        return self._detect_reproduce_result

    @detect_reproduce_result.setter
    def detect_reproduce_result(self, detect_reproduce_result):
        r"""Sets the detect_reproduce_result of this IdcardBackResult.

        身份证图像是否翻拍告警结果。 - true：表示身份证图片经过翻拍。 - false：表示身份证图片未经过翻拍。 仅在输入参数detect_reproduce为true时，返回该字段。 

        :param detect_reproduce_result: The detect_reproduce_result of this IdcardBackResult.
        :type detect_reproduce_result: bool
        """
        self._detect_reproduce_result = detect_reproduce_result

    @property
    def detect_copy_result(self):
        r"""Gets the detect_copy_result of this IdcardBackResult.

        身份证图像是否黑白复印件告警结果。 - true：表示身份证图片是复印件。 - false”表示身份证图片是原件。 仅在输入参数detect_copy为true时，返回该字段。 

        :return: The detect_copy_result of this IdcardBackResult.
        :rtype: bool
        """
        return self._detect_copy_result

    @detect_copy_result.setter
    def detect_copy_result(self, detect_copy_result):
        r"""Sets the detect_copy_result of this IdcardBackResult.

        身份证图像是否黑白复印件告警结果。 - true：表示身份证图片是复印件。 - false”表示身份证图片是原件。 仅在输入参数detect_copy为true时，返回该字段。 

        :param detect_copy_result: The detect_copy_result of this IdcardBackResult.
        :type detect_copy_result: bool
        """
        self._detect_copy_result = detect_copy_result

    @property
    def detect_tampering_result(self):
        r"""Gets the detect_tampering_result of this IdcardBackResult.

        身份证图片是否PS告警结果。 - true：表示身份证经过PS。 - false：表示未经过PS。 仅在传入参数detect_tampering为true时，返回该字段。 

        :return: The detect_tampering_result of this IdcardBackResult.
        :rtype: bool
        """
        return self._detect_tampering_result

    @detect_tampering_result.setter
    def detect_tampering_result(self, detect_tampering_result):
        r"""Sets the detect_tampering_result of this IdcardBackResult.

        身份证图片是否PS告警结果。 - true：表示身份证经过PS。 - false：表示未经过PS。 仅在传入参数detect_tampering为true时，返回该字段。 

        :param detect_tampering_result: The detect_tampering_result of this IdcardBackResult.
        :type detect_tampering_result: bool
        """
        self._detect_tampering_result = detect_tampering_result

    @property
    def detect_border_integrity_result(self):
        r"""Gets the detect_border_integrity_result of this IdcardBackResult.

        身份证图片边框完整性告警结果。 - true：表示边框不完整 - false：表示边框完整。 仅在输入参数detect_border_integrity为true时，返回该字段。 

        :return: The detect_border_integrity_result of this IdcardBackResult.
        :rtype: bool
        """
        return self._detect_border_integrity_result

    @detect_border_integrity_result.setter
    def detect_border_integrity_result(self, detect_border_integrity_result):
        r"""Sets the detect_border_integrity_result of this IdcardBackResult.

        身份证图片边框完整性告警结果。 - true：表示边框不完整 - false：表示边框完整。 仅在输入参数detect_border_integrity为true时，返回该字段。 

        :param detect_border_integrity_result: The detect_border_integrity_result of this IdcardBackResult.
        :type detect_border_integrity_result: bool
        """
        self._detect_border_integrity_result = detect_border_integrity_result

    @property
    def detect_blocking_within_border_result(self):
        r"""Gets the detect_blocking_within_border_result of this IdcardBackResult.

        身份证图像框内是否存在遮挡的告警结果。 - true：表示边框内部存在遮挡。 - false：表示边框内部不存在遮挡。 仅在输入参数detect_blocking_within_border为true时，返回该字段。 

        :return: The detect_blocking_within_border_result of this IdcardBackResult.
        :rtype: bool
        """
        return self._detect_blocking_within_border_result

    @detect_blocking_within_border_result.setter
    def detect_blocking_within_border_result(self, detect_blocking_within_border_result):
        r"""Sets the detect_blocking_within_border_result of this IdcardBackResult.

        身份证图像框内是否存在遮挡的告警结果。 - true：表示边框内部存在遮挡。 - false：表示边框内部不存在遮挡。 仅在输入参数detect_blocking_within_border为true时，返回该字段。 

        :param detect_blocking_within_border_result: The detect_blocking_within_border_result of this IdcardBackResult.
        :type detect_blocking_within_border_result: bool
        """
        self._detect_blocking_within_border_result = detect_blocking_within_border_result

    @property
    def detect_blur_result(self):
        r"""Gets the detect_blur_result of this IdcardBackResult.

        身份证模糊告警结果。 - true：表示身份证图片较模糊。 - false：表示身份证清晰。 仅在输入参数detect_blur为true时，返回该字段。 

        :return: The detect_blur_result of this IdcardBackResult.
        :rtype: bool
        """
        return self._detect_blur_result

    @detect_blur_result.setter
    def detect_blur_result(self, detect_blur_result):
        r"""Sets the detect_blur_result of this IdcardBackResult.

        身份证模糊告警结果。 - true：表示身份证图片较模糊。 - false：表示身份证清晰。 仅在输入参数detect_blur为true时，返回该字段。 

        :param detect_blur_result: The detect_blur_result of this IdcardBackResult.
        :type detect_blur_result: bool
        """
        self._detect_blur_result = detect_blur_result

    @property
    def detect_interim_result(self):
        r"""Gets the detect_interim_result of this IdcardBackResult.

        临时身份证告警结果。 - true：表示是临时身份证。 - false：表示非临时身份证。 仅在输入参数detect_interim为true时，返回该字段。 

        :return: The detect_interim_result of this IdcardBackResult.
        :rtype: bool
        """
        return self._detect_interim_result

    @detect_interim_result.setter
    def detect_interim_result(self, detect_interim_result):
        r"""Sets the detect_interim_result of this IdcardBackResult.

        临时身份证告警结果。 - true：表示是临时身份证。 - false：表示非临时身份证。 仅在输入参数detect_interim为true时，返回该字段。 

        :param detect_interim_result: The detect_interim_result of this IdcardBackResult.
        :type detect_interim_result: bool
        """
        self._detect_interim_result = detect_interim_result

    @property
    def detect_glare_result(self):
        r"""Gets the detect_glare_result of this IdcardBackResult.

        身份证反光告警结果。 - true：表示身份证图片存在反光。 - false：表示是身份证不存在反光。 仅在输入参数detect_glare为true时，返回该字段。 

        :return: The detect_glare_result of this IdcardBackResult.
        :rtype: bool
        """
        return self._detect_glare_result

    @detect_glare_result.setter
    def detect_glare_result(self, detect_glare_result):
        r"""Sets the detect_glare_result of this IdcardBackResult.

        身份证反光告警结果。 - true：表示身份证图片存在反光。 - false：表示是身份证不存在反光。 仅在输入参数detect_glare为true时，返回该字段。 

        :param detect_glare_result: The detect_glare_result of this IdcardBackResult.
        :type detect_glare_result: bool
        """
        self._detect_glare_result = detect_glare_result

    @property
    def score_info(self):
        r"""Gets the score_info of this IdcardBackResult.

        :return: The score_info of this IdcardBackResult.
        :rtype: :class:`huaweicloudsdkocr.v1.IdcardScoreInfoResult`
        """
        return self._score_info

    @score_info.setter
    def score_info(self, score_info):
        r"""Sets the score_info of this IdcardBackResult.

        :param score_info: The score_info of this IdcardBackResult.
        :type score_info: :class:`huaweicloudsdkocr.v1.IdcardScoreInfoResult`
        """
        self._score_info = score_info

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
        if not isinstance(other, IdcardBackResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
