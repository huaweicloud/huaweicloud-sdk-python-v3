# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IdcardFrontResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'sex': 'str',
        'birth': 'str',
        'ethnicity': 'str',
        'address': 'str',
        'number': 'str',
        'portrait_image': 'str',
        'adjusted_image': 'str',
        'verification_result': 'IdcardFrontVerificationResult',
        'text_location': 'object',
        'portrait_location': 'list[list[int]]',
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
        'name': 'name',
        'sex': 'sex',
        'birth': 'birth',
        'ethnicity': 'ethnicity',
        'address': 'address',
        'number': 'number',
        'portrait_image': 'portrait_image',
        'adjusted_image': 'adjusted_image',
        'verification_result': 'verification_result',
        'text_location': 'text_location',
        'portrait_location': 'portrait_location',
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

    def __init__(self, name=None, sex=None, birth=None, ethnicity=None, address=None, number=None, portrait_image=None, adjusted_image=None, verification_result=None, text_location=None, portrait_location=None, detect_reproduce_result=None, detect_copy_result=None, detect_tampering_result=None, detect_border_integrity_result=None, detect_blocking_within_border_result=None, detect_blur_result=None, detect_interim_result=None, detect_glare_result=None, score_info=None):
        r"""IdcardFrontResult

        The model defined in huaweicloud sdk

        :param name: 姓名。 
        :type name: str
        :param sex: 性别。 
        :type sex: str
        :param birth: 出生日期。 
        :type birth: str
        :param ethnicity: 民族。 
        :type ethnicity: str
        :param address: 地址。 
        :type address: str
        :param number: 身份证号。 
        :type number: str
        :param portrait_image: 身份证头像图片信息的base64码结果。  &gt; 说明： - 仅在输入参数return_portrait_image为true时，返回该字段。 - 当输入为身份证背面时返回为空字符串。 
        :type portrait_image: str
        :param adjusted_image: 身份证卡面图片信息的base64码结果。  &gt; 说明： - 仅在输入参数return_adjusted_image为true时，返回该字段。 
        :type adjusted_image: str
        :param verification_result: 
        :type verification_result: :class:`huaweicloudsdkocr.v1.IdcardFrontVerificationResult`
        :param text_location: 文本框在原图位置。输出左上、右上、右下、左下四个点坐标。 仅return_text_location设置为true时才返回。 
        :type text_location: object
        :param portrait_location: 身份证头像位置信息的结果。 仅在输入参数return_portrait_location为true时，返回该字段。 
        :type portrait_location: list[list[int]]
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
        
        

        self._name = None
        self._sex = None
        self._birth = None
        self._ethnicity = None
        self._address = None
        self._number = None
        self._portrait_image = None
        self._adjusted_image = None
        self._verification_result = None
        self._text_location = None
        self._portrait_location = None
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

        if name is not None:
            self.name = name
        if sex is not None:
            self.sex = sex
        if birth is not None:
            self.birth = birth
        if ethnicity is not None:
            self.ethnicity = ethnicity
        if address is not None:
            self.address = address
        if number is not None:
            self.number = number
        if portrait_image is not None:
            self.portrait_image = portrait_image
        if adjusted_image is not None:
            self.adjusted_image = adjusted_image
        if verification_result is not None:
            self.verification_result = verification_result
        if text_location is not None:
            self.text_location = text_location
        if portrait_location is not None:
            self.portrait_location = portrait_location
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
    def name(self):
        r"""Gets the name of this IdcardFrontResult.

        姓名。 

        :return: The name of this IdcardFrontResult.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this IdcardFrontResult.

        姓名。 

        :param name: The name of this IdcardFrontResult.
        :type name: str
        """
        self._name = name

    @property
    def sex(self):
        r"""Gets the sex of this IdcardFrontResult.

        性别。 

        :return: The sex of this IdcardFrontResult.
        :rtype: str
        """
        return self._sex

    @sex.setter
    def sex(self, sex):
        r"""Sets the sex of this IdcardFrontResult.

        性别。 

        :param sex: The sex of this IdcardFrontResult.
        :type sex: str
        """
        self._sex = sex

    @property
    def birth(self):
        r"""Gets the birth of this IdcardFrontResult.

        出生日期。 

        :return: The birth of this IdcardFrontResult.
        :rtype: str
        """
        return self._birth

    @birth.setter
    def birth(self, birth):
        r"""Sets the birth of this IdcardFrontResult.

        出生日期。 

        :param birth: The birth of this IdcardFrontResult.
        :type birth: str
        """
        self._birth = birth

    @property
    def ethnicity(self):
        r"""Gets the ethnicity of this IdcardFrontResult.

        民族。 

        :return: The ethnicity of this IdcardFrontResult.
        :rtype: str
        """
        return self._ethnicity

    @ethnicity.setter
    def ethnicity(self, ethnicity):
        r"""Sets the ethnicity of this IdcardFrontResult.

        民族。 

        :param ethnicity: The ethnicity of this IdcardFrontResult.
        :type ethnicity: str
        """
        self._ethnicity = ethnicity

    @property
    def address(self):
        r"""Gets the address of this IdcardFrontResult.

        地址。 

        :return: The address of this IdcardFrontResult.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        r"""Sets the address of this IdcardFrontResult.

        地址。 

        :param address: The address of this IdcardFrontResult.
        :type address: str
        """
        self._address = address

    @property
    def number(self):
        r"""Gets the number of this IdcardFrontResult.

        身份证号。 

        :return: The number of this IdcardFrontResult.
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        r"""Sets the number of this IdcardFrontResult.

        身份证号。 

        :param number: The number of this IdcardFrontResult.
        :type number: str
        """
        self._number = number

    @property
    def portrait_image(self):
        r"""Gets the portrait_image of this IdcardFrontResult.

        身份证头像图片信息的base64码结果。  > 说明： - 仅在输入参数return_portrait_image为true时，返回该字段。 - 当输入为身份证背面时返回为空字符串。 

        :return: The portrait_image of this IdcardFrontResult.
        :rtype: str
        """
        return self._portrait_image

    @portrait_image.setter
    def portrait_image(self, portrait_image):
        r"""Sets the portrait_image of this IdcardFrontResult.

        身份证头像图片信息的base64码结果。  > 说明： - 仅在输入参数return_portrait_image为true时，返回该字段。 - 当输入为身份证背面时返回为空字符串。 

        :param portrait_image: The portrait_image of this IdcardFrontResult.
        :type portrait_image: str
        """
        self._portrait_image = portrait_image

    @property
    def adjusted_image(self):
        r"""Gets the adjusted_image of this IdcardFrontResult.

        身份证卡面图片信息的base64码结果。  > 说明： - 仅在输入参数return_adjusted_image为true时，返回该字段。 

        :return: The adjusted_image of this IdcardFrontResult.
        :rtype: str
        """
        return self._adjusted_image

    @adjusted_image.setter
    def adjusted_image(self, adjusted_image):
        r"""Sets the adjusted_image of this IdcardFrontResult.

        身份证卡面图片信息的base64码结果。  > 说明： - 仅在输入参数return_adjusted_image为true时，返回该字段。 

        :param adjusted_image: The adjusted_image of this IdcardFrontResult.
        :type adjusted_image: str
        """
        self._adjusted_image = adjusted_image

    @property
    def verification_result(self):
        r"""Gets the verification_result of this IdcardFrontResult.

        :return: The verification_result of this IdcardFrontResult.
        :rtype: :class:`huaweicloudsdkocr.v1.IdcardFrontVerificationResult`
        """
        return self._verification_result

    @verification_result.setter
    def verification_result(self, verification_result):
        r"""Sets the verification_result of this IdcardFrontResult.

        :param verification_result: The verification_result of this IdcardFrontResult.
        :type verification_result: :class:`huaweicloudsdkocr.v1.IdcardFrontVerificationResult`
        """
        self._verification_result = verification_result

    @property
    def text_location(self):
        r"""Gets the text_location of this IdcardFrontResult.

        文本框在原图位置。输出左上、右上、右下、左下四个点坐标。 仅return_text_location设置为true时才返回。 

        :return: The text_location of this IdcardFrontResult.
        :rtype: object
        """
        return self._text_location

    @text_location.setter
    def text_location(self, text_location):
        r"""Sets the text_location of this IdcardFrontResult.

        文本框在原图位置。输出左上、右上、右下、左下四个点坐标。 仅return_text_location设置为true时才返回。 

        :param text_location: The text_location of this IdcardFrontResult.
        :type text_location: object
        """
        self._text_location = text_location

    @property
    def portrait_location(self):
        r"""Gets the portrait_location of this IdcardFrontResult.

        身份证头像位置信息的结果。 仅在输入参数return_portrait_location为true时，返回该字段。 

        :return: The portrait_location of this IdcardFrontResult.
        :rtype: list[list[int]]
        """
        return self._portrait_location

    @portrait_location.setter
    def portrait_location(self, portrait_location):
        r"""Sets the portrait_location of this IdcardFrontResult.

        身份证头像位置信息的结果。 仅在输入参数return_portrait_location为true时，返回该字段。 

        :param portrait_location: The portrait_location of this IdcardFrontResult.
        :type portrait_location: list[list[int]]
        """
        self._portrait_location = portrait_location

    @property
    def detect_reproduce_result(self):
        r"""Gets the detect_reproduce_result of this IdcardFrontResult.

        身份证图像是否翻拍告警结果。 - true：表示身份证图片经过翻拍。 - false：表示身份证图片未经过翻拍。 仅在输入参数detect_reproduce为true时，返回该字段。 

        :return: The detect_reproduce_result of this IdcardFrontResult.
        :rtype: bool
        """
        return self._detect_reproduce_result

    @detect_reproduce_result.setter
    def detect_reproduce_result(self, detect_reproduce_result):
        r"""Sets the detect_reproduce_result of this IdcardFrontResult.

        身份证图像是否翻拍告警结果。 - true：表示身份证图片经过翻拍。 - false：表示身份证图片未经过翻拍。 仅在输入参数detect_reproduce为true时，返回该字段。 

        :param detect_reproduce_result: The detect_reproduce_result of this IdcardFrontResult.
        :type detect_reproduce_result: bool
        """
        self._detect_reproduce_result = detect_reproduce_result

    @property
    def detect_copy_result(self):
        r"""Gets the detect_copy_result of this IdcardFrontResult.

        身份证图像是否黑白复印件告警结果。 - true：表示身份证图片是复印件。 - false”表示身份证图片是原件。 仅在输入参数detect_copy为true时，返回该字段。 

        :return: The detect_copy_result of this IdcardFrontResult.
        :rtype: bool
        """
        return self._detect_copy_result

    @detect_copy_result.setter
    def detect_copy_result(self, detect_copy_result):
        r"""Sets the detect_copy_result of this IdcardFrontResult.

        身份证图像是否黑白复印件告警结果。 - true：表示身份证图片是复印件。 - false”表示身份证图片是原件。 仅在输入参数detect_copy为true时，返回该字段。 

        :param detect_copy_result: The detect_copy_result of this IdcardFrontResult.
        :type detect_copy_result: bool
        """
        self._detect_copy_result = detect_copy_result

    @property
    def detect_tampering_result(self):
        r"""Gets the detect_tampering_result of this IdcardFrontResult.

        身份证图片是否PS告警结果。 - true：表示身份证经过PS。 - false：表示未经过PS。 仅在传入参数detect_tampering为true时，返回该字段。 

        :return: The detect_tampering_result of this IdcardFrontResult.
        :rtype: bool
        """
        return self._detect_tampering_result

    @detect_tampering_result.setter
    def detect_tampering_result(self, detect_tampering_result):
        r"""Sets the detect_tampering_result of this IdcardFrontResult.

        身份证图片是否PS告警结果。 - true：表示身份证经过PS。 - false：表示未经过PS。 仅在传入参数detect_tampering为true时，返回该字段。 

        :param detect_tampering_result: The detect_tampering_result of this IdcardFrontResult.
        :type detect_tampering_result: bool
        """
        self._detect_tampering_result = detect_tampering_result

    @property
    def detect_border_integrity_result(self):
        r"""Gets the detect_border_integrity_result of this IdcardFrontResult.

        身份证图片边框完整性告警结果。 - true：表示边框不完整 - false：表示边框完整。 仅在输入参数detect_border_integrity为true时，返回该字段。 

        :return: The detect_border_integrity_result of this IdcardFrontResult.
        :rtype: bool
        """
        return self._detect_border_integrity_result

    @detect_border_integrity_result.setter
    def detect_border_integrity_result(self, detect_border_integrity_result):
        r"""Sets the detect_border_integrity_result of this IdcardFrontResult.

        身份证图片边框完整性告警结果。 - true：表示边框不完整 - false：表示边框完整。 仅在输入参数detect_border_integrity为true时，返回该字段。 

        :param detect_border_integrity_result: The detect_border_integrity_result of this IdcardFrontResult.
        :type detect_border_integrity_result: bool
        """
        self._detect_border_integrity_result = detect_border_integrity_result

    @property
    def detect_blocking_within_border_result(self):
        r"""Gets the detect_blocking_within_border_result of this IdcardFrontResult.

        身份证图像框内是否存在遮挡的告警结果。 - true：表示边框内部存在遮挡。 - false：表示边框内部不存在遮挡。 仅在输入参数detect_blocking_within_border为true时，返回该字段。 

        :return: The detect_blocking_within_border_result of this IdcardFrontResult.
        :rtype: bool
        """
        return self._detect_blocking_within_border_result

    @detect_blocking_within_border_result.setter
    def detect_blocking_within_border_result(self, detect_blocking_within_border_result):
        r"""Sets the detect_blocking_within_border_result of this IdcardFrontResult.

        身份证图像框内是否存在遮挡的告警结果。 - true：表示边框内部存在遮挡。 - false：表示边框内部不存在遮挡。 仅在输入参数detect_blocking_within_border为true时，返回该字段。 

        :param detect_blocking_within_border_result: The detect_blocking_within_border_result of this IdcardFrontResult.
        :type detect_blocking_within_border_result: bool
        """
        self._detect_blocking_within_border_result = detect_blocking_within_border_result

    @property
    def detect_blur_result(self):
        r"""Gets the detect_blur_result of this IdcardFrontResult.

        身份证模糊告警结果。 - true：表示身份证图片较模糊。 - false：表示身份证清晰。 仅在输入参数detect_blur为true时，返回该字段。 

        :return: The detect_blur_result of this IdcardFrontResult.
        :rtype: bool
        """
        return self._detect_blur_result

    @detect_blur_result.setter
    def detect_blur_result(self, detect_blur_result):
        r"""Sets the detect_blur_result of this IdcardFrontResult.

        身份证模糊告警结果。 - true：表示身份证图片较模糊。 - false：表示身份证清晰。 仅在输入参数detect_blur为true时，返回该字段。 

        :param detect_blur_result: The detect_blur_result of this IdcardFrontResult.
        :type detect_blur_result: bool
        """
        self._detect_blur_result = detect_blur_result

    @property
    def detect_interim_result(self):
        r"""Gets the detect_interim_result of this IdcardFrontResult.

        临时身份证告警结果。 - true：表示是临时身份证。 - false：表示非临时身份证。 仅在输入参数detect_interim为true时，返回该字段。 

        :return: The detect_interim_result of this IdcardFrontResult.
        :rtype: bool
        """
        return self._detect_interim_result

    @detect_interim_result.setter
    def detect_interim_result(self, detect_interim_result):
        r"""Sets the detect_interim_result of this IdcardFrontResult.

        临时身份证告警结果。 - true：表示是临时身份证。 - false：表示非临时身份证。 仅在输入参数detect_interim为true时，返回该字段。 

        :param detect_interim_result: The detect_interim_result of this IdcardFrontResult.
        :type detect_interim_result: bool
        """
        self._detect_interim_result = detect_interim_result

    @property
    def detect_glare_result(self):
        r"""Gets the detect_glare_result of this IdcardFrontResult.

        身份证反光告警结果。 - true：表示身份证图片存在反光。 - false：表示是身份证不存在反光。 仅在输入参数detect_glare为true时，返回该字段。 

        :return: The detect_glare_result of this IdcardFrontResult.
        :rtype: bool
        """
        return self._detect_glare_result

    @detect_glare_result.setter
    def detect_glare_result(self, detect_glare_result):
        r"""Sets the detect_glare_result of this IdcardFrontResult.

        身份证反光告警结果。 - true：表示身份证图片存在反光。 - false：表示是身份证不存在反光。 仅在输入参数detect_glare为true时，返回该字段。 

        :param detect_glare_result: The detect_glare_result of this IdcardFrontResult.
        :type detect_glare_result: bool
        """
        self._detect_glare_result = detect_glare_result

    @property
    def score_info(self):
        r"""Gets the score_info of this IdcardFrontResult.

        :return: The score_info of this IdcardFrontResult.
        :rtype: :class:`huaweicloudsdkocr.v1.IdcardScoreInfoResult`
        """
        return self._score_info

    @score_info.setter
    def score_info(self, score_info):
        r"""Sets the score_info of this IdcardFrontResult.

        :param score_info: The score_info of this IdcardFrontResult.
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
        if not isinstance(other, IdcardFrontResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
