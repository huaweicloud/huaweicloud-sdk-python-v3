# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CambodianIdCardResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id_number': 'str',
        'name_kh': 'str',
        'name_en': 'str',
        'birth_date': 'str',
        'sex': 'str',
        'height': 'str',
        'birth_place': 'str',
        'address': 'str',
        'issue_date': 'str',
        'expiry_date': 'str',
        'description': 'str',
        'machine_code1': 'str',
        'machine_code2': 'str',
        'machine_code3': 'str',
        'portrait_image': 'str',
        'portrait_location': 'list[list[int]]',
        'idcard_type': 'str',
        'adjusted_image': 'str',
        'detect_border_integrity_result': 'bool',
        'detect_blocking_within_border_result': 'bool',
        'detect_blur_result': 'bool',
        'detect_glare_result': 'bool',
        'detect_tampering_result': 'bool',
        'detect_reproduce_result': 'bool',
        'score_info': 'CambodianIdCardScoreInformationResult',
        'confidence': 'object'
    }

    attribute_map = {
        'id_number': 'id_number',
        'name_kh': 'name_kh',
        'name_en': 'name_en',
        'birth_date': 'birth_date',
        'sex': 'sex',
        'height': 'height',
        'birth_place': 'birth_place',
        'address': 'address',
        'issue_date': 'issue_date',
        'expiry_date': 'expiry_date',
        'description': 'description',
        'machine_code1': 'machine_code1',
        'machine_code2': 'machine_code2',
        'machine_code3': 'machine_code3',
        'portrait_image': 'portrait_image',
        'portrait_location': 'portrait_location',
        'idcard_type': 'idcard_type',
        'adjusted_image': 'adjusted_image',
        'detect_border_integrity_result': 'detect_border_integrity_result',
        'detect_blocking_within_border_result': 'detect_blocking_within_border_result',
        'detect_blur_result': 'detect_blur_result',
        'detect_glare_result': 'detect_glare_result',
        'detect_tampering_result': 'detect_tampering_result',
        'detect_reproduce_result': 'detect_reproduce_result',
        'score_info': 'score_info',
        'confidence': 'confidence'
    }

    def __init__(self, id_number=None, name_kh=None, name_en=None, birth_date=None, sex=None, height=None, birth_place=None, address=None, issue_date=None, expiry_date=None, description=None, machine_code1=None, machine_code2=None, machine_code3=None, portrait_image=None, portrait_location=None, idcard_type=None, adjusted_image=None, detect_border_integrity_result=None, detect_blocking_within_border_result=None, detect_blur_result=None, detect_glare_result=None, detect_tampering_result=None, detect_reproduce_result=None, score_info=None, confidence=None):
        r"""CambodianIdCardResult

        The model defined in huaweicloud sdk

        :param id_number: 身份证号码。 
        :type id_number: str
        :param name_kh: 高棉语版姓名。 
        :type name_kh: str
        :param name_en: 英文姓名。 
        :type name_en: str
        :param birth_date: 出生日期。 
        :type birth_date: str
        :param sex: 性别。 
        :type sex: str
        :param height: 身高。 
        :type height: str
        :param birth_place: 出生地。 
        :type birth_place: str
        :param address: 地址，以空格分隔。 
        :type address: str
        :param issue_date: 签发起始日期。 
        :type issue_date: str
        :param expiry_date: 签发结束日期。 
        :type expiry_date: str
        :param description: 图片中的个人特征。 
        :type description: str
        :param machine_code1: 机器码第一行。 
        :type machine_code1: str
        :param machine_code2: 机器码第二行。 
        :type machine_code2: str
        :param machine_code3: 机器码第三行。 
        :type machine_code3: str
        :param portrait_image: 头像的base64编码。 当输入参数“return_portrait_image”为“true”时，才返回该参数。 
        :type portrait_image: str
        :param portrait_location: 头像在原图上的位置。 当输入参数“return_portrait_location”为“true”时，才返回该参数。以列表形式显示，包含头像区域四个顶点的二维坐标（x,y），坐标原点为图片左上角，x轴沿水平方向，y轴沿竖直方向。 
        :type portrait_location: list[list[int]]
        :param idcard_type: 身份证的类型。当输入参数\&quot;idcard_type \&quot;为\&quot;true\&quot;时，才返回该参数。取值如下所示： - normal：身份证原件 - copy：复印的身份证 
        :type idcard_type: str
        :param adjusted_image: 身份证原图的base64编码。 当输入参数\&quot;return_adjusted_image\&quot;为\&quot;true\&quot;时，才返回该参数。 
        :type adjusted_image: str
        :param detect_border_integrity_result: 身份证图片边框完整性告警结果，\&quot;true\&quot;表示边框不完整，\&quot;false\&quot;表示边框完整。仅在输入参数detect_border_integrity为true时，返回该字段。 
        :type detect_border_integrity_result: bool
        :param detect_blocking_within_border_result: 身份证图像框内是否存在遮挡的告警结果，\&quot;true\&quot;表示边框内部存在遮挡，\&quot;false\&quot;表示边框内部完整。仅在输入参数detect_blocking_within_border为true时，返回该字段。 
        :type detect_blocking_within_border_result: bool
        :param detect_blur_result: 身份证模糊告警结果，\&quot;true\&quot;表示图片模糊，\&quot;false\&quot;表示身份证清晰。仅在输入参数detect_blur为true时，返回该字段。 
        :type detect_blur_result: bool
        :param detect_glare_result: 身份证反光告警结果，\&quot;true\&quot;表示身份证反光，\&quot;false\&quot;表示是身份证无反光。仅在输入参数detect_glare为true时，返回该字段。 
        :type detect_glare_result: bool
        :param detect_tampering_result: 身份证人像被篡改的告警结果，\&quot;true\&quot;表示身份证人像被篡改，\&quot;false\&quot;表示是身份证人像未被篡改。仅在输入参数detect_tampering为true时，返回该字段。 
        :type detect_tampering_result: bool
        :param detect_reproduce_result: 身份证是否经过翻拍的告警结果，“true”表示身份证经过翻拍，“false”表示身份证未经过翻拍。仅在输入参数detect_reproduce为true时，返回该字段。 
        :type detect_reproduce_result: bool
        :param score_info: 
        :type score_info: :class:`huaweicloudsdkocr.v1.CambodianIdCardScoreInformationResult`
        :param confidence: 相关字段的置信度信息，置信度越大，表示本次识别的对应字段的可靠性越高，在统计意义上，置信度越大，准确率越高。 置信度由算法给出，不直接等价于对应字段的准确率。 
        :type confidence: object
        """
        
        

        self._id_number = None
        self._name_kh = None
        self._name_en = None
        self._birth_date = None
        self._sex = None
        self._height = None
        self._birth_place = None
        self._address = None
        self._issue_date = None
        self._expiry_date = None
        self._description = None
        self._machine_code1 = None
        self._machine_code2 = None
        self._machine_code3 = None
        self._portrait_image = None
        self._portrait_location = None
        self._idcard_type = None
        self._adjusted_image = None
        self._detect_border_integrity_result = None
        self._detect_blocking_within_border_result = None
        self._detect_blur_result = None
        self._detect_glare_result = None
        self._detect_tampering_result = None
        self._detect_reproduce_result = None
        self._score_info = None
        self._confidence = None
        self.discriminator = None

        if id_number is not None:
            self.id_number = id_number
        if name_kh is not None:
            self.name_kh = name_kh
        if name_en is not None:
            self.name_en = name_en
        if birth_date is not None:
            self.birth_date = birth_date
        if sex is not None:
            self.sex = sex
        if height is not None:
            self.height = height
        if birth_place is not None:
            self.birth_place = birth_place
        if address is not None:
            self.address = address
        if issue_date is not None:
            self.issue_date = issue_date
        if expiry_date is not None:
            self.expiry_date = expiry_date
        if description is not None:
            self.description = description
        if machine_code1 is not None:
            self.machine_code1 = machine_code1
        if machine_code2 is not None:
            self.machine_code2 = machine_code2
        if machine_code3 is not None:
            self.machine_code3 = machine_code3
        if portrait_image is not None:
            self.portrait_image = portrait_image
        if portrait_location is not None:
            self.portrait_location = portrait_location
        if idcard_type is not None:
            self.idcard_type = idcard_type
        if adjusted_image is not None:
            self.adjusted_image = adjusted_image
        if detect_border_integrity_result is not None:
            self.detect_border_integrity_result = detect_border_integrity_result
        if detect_blocking_within_border_result is not None:
            self.detect_blocking_within_border_result = detect_blocking_within_border_result
        if detect_blur_result is not None:
            self.detect_blur_result = detect_blur_result
        if detect_glare_result is not None:
            self.detect_glare_result = detect_glare_result
        if detect_tampering_result is not None:
            self.detect_tampering_result = detect_tampering_result
        if detect_reproduce_result is not None:
            self.detect_reproduce_result = detect_reproduce_result
        if score_info is not None:
            self.score_info = score_info
        if confidence is not None:
            self.confidence = confidence

    @property
    def id_number(self):
        r"""Gets the id_number of this CambodianIdCardResult.

        身份证号码。 

        :return: The id_number of this CambodianIdCardResult.
        :rtype: str
        """
        return self._id_number

    @id_number.setter
    def id_number(self, id_number):
        r"""Sets the id_number of this CambodianIdCardResult.

        身份证号码。 

        :param id_number: The id_number of this CambodianIdCardResult.
        :type id_number: str
        """
        self._id_number = id_number

    @property
    def name_kh(self):
        r"""Gets the name_kh of this CambodianIdCardResult.

        高棉语版姓名。 

        :return: The name_kh of this CambodianIdCardResult.
        :rtype: str
        """
        return self._name_kh

    @name_kh.setter
    def name_kh(self, name_kh):
        r"""Sets the name_kh of this CambodianIdCardResult.

        高棉语版姓名。 

        :param name_kh: The name_kh of this CambodianIdCardResult.
        :type name_kh: str
        """
        self._name_kh = name_kh

    @property
    def name_en(self):
        r"""Gets the name_en of this CambodianIdCardResult.

        英文姓名。 

        :return: The name_en of this CambodianIdCardResult.
        :rtype: str
        """
        return self._name_en

    @name_en.setter
    def name_en(self, name_en):
        r"""Sets the name_en of this CambodianIdCardResult.

        英文姓名。 

        :param name_en: The name_en of this CambodianIdCardResult.
        :type name_en: str
        """
        self._name_en = name_en

    @property
    def birth_date(self):
        r"""Gets the birth_date of this CambodianIdCardResult.

        出生日期。 

        :return: The birth_date of this CambodianIdCardResult.
        :rtype: str
        """
        return self._birth_date

    @birth_date.setter
    def birth_date(self, birth_date):
        r"""Sets the birth_date of this CambodianIdCardResult.

        出生日期。 

        :param birth_date: The birth_date of this CambodianIdCardResult.
        :type birth_date: str
        """
        self._birth_date = birth_date

    @property
    def sex(self):
        r"""Gets the sex of this CambodianIdCardResult.

        性别。 

        :return: The sex of this CambodianIdCardResult.
        :rtype: str
        """
        return self._sex

    @sex.setter
    def sex(self, sex):
        r"""Sets the sex of this CambodianIdCardResult.

        性别。 

        :param sex: The sex of this CambodianIdCardResult.
        :type sex: str
        """
        self._sex = sex

    @property
    def height(self):
        r"""Gets the height of this CambodianIdCardResult.

        身高。 

        :return: The height of this CambodianIdCardResult.
        :rtype: str
        """
        return self._height

    @height.setter
    def height(self, height):
        r"""Sets the height of this CambodianIdCardResult.

        身高。 

        :param height: The height of this CambodianIdCardResult.
        :type height: str
        """
        self._height = height

    @property
    def birth_place(self):
        r"""Gets the birth_place of this CambodianIdCardResult.

        出生地。 

        :return: The birth_place of this CambodianIdCardResult.
        :rtype: str
        """
        return self._birth_place

    @birth_place.setter
    def birth_place(self, birth_place):
        r"""Sets the birth_place of this CambodianIdCardResult.

        出生地。 

        :param birth_place: The birth_place of this CambodianIdCardResult.
        :type birth_place: str
        """
        self._birth_place = birth_place

    @property
    def address(self):
        r"""Gets the address of this CambodianIdCardResult.

        地址，以空格分隔。 

        :return: The address of this CambodianIdCardResult.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        r"""Sets the address of this CambodianIdCardResult.

        地址，以空格分隔。 

        :param address: The address of this CambodianIdCardResult.
        :type address: str
        """
        self._address = address

    @property
    def issue_date(self):
        r"""Gets the issue_date of this CambodianIdCardResult.

        签发起始日期。 

        :return: The issue_date of this CambodianIdCardResult.
        :rtype: str
        """
        return self._issue_date

    @issue_date.setter
    def issue_date(self, issue_date):
        r"""Sets the issue_date of this CambodianIdCardResult.

        签发起始日期。 

        :param issue_date: The issue_date of this CambodianIdCardResult.
        :type issue_date: str
        """
        self._issue_date = issue_date

    @property
    def expiry_date(self):
        r"""Gets the expiry_date of this CambodianIdCardResult.

        签发结束日期。 

        :return: The expiry_date of this CambodianIdCardResult.
        :rtype: str
        """
        return self._expiry_date

    @expiry_date.setter
    def expiry_date(self, expiry_date):
        r"""Sets the expiry_date of this CambodianIdCardResult.

        签发结束日期。 

        :param expiry_date: The expiry_date of this CambodianIdCardResult.
        :type expiry_date: str
        """
        self._expiry_date = expiry_date

    @property
    def description(self):
        r"""Gets the description of this CambodianIdCardResult.

        图片中的个人特征。 

        :return: The description of this CambodianIdCardResult.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CambodianIdCardResult.

        图片中的个人特征。 

        :param description: The description of this CambodianIdCardResult.
        :type description: str
        """
        self._description = description

    @property
    def machine_code1(self):
        r"""Gets the machine_code1 of this CambodianIdCardResult.

        机器码第一行。 

        :return: The machine_code1 of this CambodianIdCardResult.
        :rtype: str
        """
        return self._machine_code1

    @machine_code1.setter
    def machine_code1(self, machine_code1):
        r"""Sets the machine_code1 of this CambodianIdCardResult.

        机器码第一行。 

        :param machine_code1: The machine_code1 of this CambodianIdCardResult.
        :type machine_code1: str
        """
        self._machine_code1 = machine_code1

    @property
    def machine_code2(self):
        r"""Gets the machine_code2 of this CambodianIdCardResult.

        机器码第二行。 

        :return: The machine_code2 of this CambodianIdCardResult.
        :rtype: str
        """
        return self._machine_code2

    @machine_code2.setter
    def machine_code2(self, machine_code2):
        r"""Sets the machine_code2 of this CambodianIdCardResult.

        机器码第二行。 

        :param machine_code2: The machine_code2 of this CambodianIdCardResult.
        :type machine_code2: str
        """
        self._machine_code2 = machine_code2

    @property
    def machine_code3(self):
        r"""Gets the machine_code3 of this CambodianIdCardResult.

        机器码第三行。 

        :return: The machine_code3 of this CambodianIdCardResult.
        :rtype: str
        """
        return self._machine_code3

    @machine_code3.setter
    def machine_code3(self, machine_code3):
        r"""Sets the machine_code3 of this CambodianIdCardResult.

        机器码第三行。 

        :param machine_code3: The machine_code3 of this CambodianIdCardResult.
        :type machine_code3: str
        """
        self._machine_code3 = machine_code3

    @property
    def portrait_image(self):
        r"""Gets the portrait_image of this CambodianIdCardResult.

        头像的base64编码。 当输入参数“return_portrait_image”为“true”时，才返回该参数。 

        :return: The portrait_image of this CambodianIdCardResult.
        :rtype: str
        """
        return self._portrait_image

    @portrait_image.setter
    def portrait_image(self, portrait_image):
        r"""Sets the portrait_image of this CambodianIdCardResult.

        头像的base64编码。 当输入参数“return_portrait_image”为“true”时，才返回该参数。 

        :param portrait_image: The portrait_image of this CambodianIdCardResult.
        :type portrait_image: str
        """
        self._portrait_image = portrait_image

    @property
    def portrait_location(self):
        r"""Gets the portrait_location of this CambodianIdCardResult.

        头像在原图上的位置。 当输入参数“return_portrait_location”为“true”时，才返回该参数。以列表形式显示，包含头像区域四个顶点的二维坐标（x,y），坐标原点为图片左上角，x轴沿水平方向，y轴沿竖直方向。 

        :return: The portrait_location of this CambodianIdCardResult.
        :rtype: list[list[int]]
        """
        return self._portrait_location

    @portrait_location.setter
    def portrait_location(self, portrait_location):
        r"""Sets the portrait_location of this CambodianIdCardResult.

        头像在原图上的位置。 当输入参数“return_portrait_location”为“true”时，才返回该参数。以列表形式显示，包含头像区域四个顶点的二维坐标（x,y），坐标原点为图片左上角，x轴沿水平方向，y轴沿竖直方向。 

        :param portrait_location: The portrait_location of this CambodianIdCardResult.
        :type portrait_location: list[list[int]]
        """
        self._portrait_location = portrait_location

    @property
    def idcard_type(self):
        r"""Gets the idcard_type of this CambodianIdCardResult.

        身份证的类型。当输入参数\"idcard_type \"为\"true\"时，才返回该参数。取值如下所示： - normal：身份证原件 - copy：复印的身份证 

        :return: The idcard_type of this CambodianIdCardResult.
        :rtype: str
        """
        return self._idcard_type

    @idcard_type.setter
    def idcard_type(self, idcard_type):
        r"""Sets the idcard_type of this CambodianIdCardResult.

        身份证的类型。当输入参数\"idcard_type \"为\"true\"时，才返回该参数。取值如下所示： - normal：身份证原件 - copy：复印的身份证 

        :param idcard_type: The idcard_type of this CambodianIdCardResult.
        :type idcard_type: str
        """
        self._idcard_type = idcard_type

    @property
    def adjusted_image(self):
        r"""Gets the adjusted_image of this CambodianIdCardResult.

        身份证原图的base64编码。 当输入参数\"return_adjusted_image\"为\"true\"时，才返回该参数。 

        :return: The adjusted_image of this CambodianIdCardResult.
        :rtype: str
        """
        return self._adjusted_image

    @adjusted_image.setter
    def adjusted_image(self, adjusted_image):
        r"""Sets the adjusted_image of this CambodianIdCardResult.

        身份证原图的base64编码。 当输入参数\"return_adjusted_image\"为\"true\"时，才返回该参数。 

        :param adjusted_image: The adjusted_image of this CambodianIdCardResult.
        :type adjusted_image: str
        """
        self._adjusted_image = adjusted_image

    @property
    def detect_border_integrity_result(self):
        r"""Gets the detect_border_integrity_result of this CambodianIdCardResult.

        身份证图片边框完整性告警结果，\"true\"表示边框不完整，\"false\"表示边框完整。仅在输入参数detect_border_integrity为true时，返回该字段。 

        :return: The detect_border_integrity_result of this CambodianIdCardResult.
        :rtype: bool
        """
        return self._detect_border_integrity_result

    @detect_border_integrity_result.setter
    def detect_border_integrity_result(self, detect_border_integrity_result):
        r"""Sets the detect_border_integrity_result of this CambodianIdCardResult.

        身份证图片边框完整性告警结果，\"true\"表示边框不完整，\"false\"表示边框完整。仅在输入参数detect_border_integrity为true时，返回该字段。 

        :param detect_border_integrity_result: The detect_border_integrity_result of this CambodianIdCardResult.
        :type detect_border_integrity_result: bool
        """
        self._detect_border_integrity_result = detect_border_integrity_result

    @property
    def detect_blocking_within_border_result(self):
        r"""Gets the detect_blocking_within_border_result of this CambodianIdCardResult.

        身份证图像框内是否存在遮挡的告警结果，\"true\"表示边框内部存在遮挡，\"false\"表示边框内部完整。仅在输入参数detect_blocking_within_border为true时，返回该字段。 

        :return: The detect_blocking_within_border_result of this CambodianIdCardResult.
        :rtype: bool
        """
        return self._detect_blocking_within_border_result

    @detect_blocking_within_border_result.setter
    def detect_blocking_within_border_result(self, detect_blocking_within_border_result):
        r"""Sets the detect_blocking_within_border_result of this CambodianIdCardResult.

        身份证图像框内是否存在遮挡的告警结果，\"true\"表示边框内部存在遮挡，\"false\"表示边框内部完整。仅在输入参数detect_blocking_within_border为true时，返回该字段。 

        :param detect_blocking_within_border_result: The detect_blocking_within_border_result of this CambodianIdCardResult.
        :type detect_blocking_within_border_result: bool
        """
        self._detect_blocking_within_border_result = detect_blocking_within_border_result

    @property
    def detect_blur_result(self):
        r"""Gets the detect_blur_result of this CambodianIdCardResult.

        身份证模糊告警结果，\"true\"表示图片模糊，\"false\"表示身份证清晰。仅在输入参数detect_blur为true时，返回该字段。 

        :return: The detect_blur_result of this CambodianIdCardResult.
        :rtype: bool
        """
        return self._detect_blur_result

    @detect_blur_result.setter
    def detect_blur_result(self, detect_blur_result):
        r"""Sets the detect_blur_result of this CambodianIdCardResult.

        身份证模糊告警结果，\"true\"表示图片模糊，\"false\"表示身份证清晰。仅在输入参数detect_blur为true时，返回该字段。 

        :param detect_blur_result: The detect_blur_result of this CambodianIdCardResult.
        :type detect_blur_result: bool
        """
        self._detect_blur_result = detect_blur_result

    @property
    def detect_glare_result(self):
        r"""Gets the detect_glare_result of this CambodianIdCardResult.

        身份证反光告警结果，\"true\"表示身份证反光，\"false\"表示是身份证无反光。仅在输入参数detect_glare为true时，返回该字段。 

        :return: The detect_glare_result of this CambodianIdCardResult.
        :rtype: bool
        """
        return self._detect_glare_result

    @detect_glare_result.setter
    def detect_glare_result(self, detect_glare_result):
        r"""Sets the detect_glare_result of this CambodianIdCardResult.

        身份证反光告警结果，\"true\"表示身份证反光，\"false\"表示是身份证无反光。仅在输入参数detect_glare为true时，返回该字段。 

        :param detect_glare_result: The detect_glare_result of this CambodianIdCardResult.
        :type detect_glare_result: bool
        """
        self._detect_glare_result = detect_glare_result

    @property
    def detect_tampering_result(self):
        r"""Gets the detect_tampering_result of this CambodianIdCardResult.

        身份证人像被篡改的告警结果，\"true\"表示身份证人像被篡改，\"false\"表示是身份证人像未被篡改。仅在输入参数detect_tampering为true时，返回该字段。 

        :return: The detect_tampering_result of this CambodianIdCardResult.
        :rtype: bool
        """
        return self._detect_tampering_result

    @detect_tampering_result.setter
    def detect_tampering_result(self, detect_tampering_result):
        r"""Sets the detect_tampering_result of this CambodianIdCardResult.

        身份证人像被篡改的告警结果，\"true\"表示身份证人像被篡改，\"false\"表示是身份证人像未被篡改。仅在输入参数detect_tampering为true时，返回该字段。 

        :param detect_tampering_result: The detect_tampering_result of this CambodianIdCardResult.
        :type detect_tampering_result: bool
        """
        self._detect_tampering_result = detect_tampering_result

    @property
    def detect_reproduce_result(self):
        r"""Gets the detect_reproduce_result of this CambodianIdCardResult.

        身份证是否经过翻拍的告警结果，“true”表示身份证经过翻拍，“false”表示身份证未经过翻拍。仅在输入参数detect_reproduce为true时，返回该字段。 

        :return: The detect_reproduce_result of this CambodianIdCardResult.
        :rtype: bool
        """
        return self._detect_reproduce_result

    @detect_reproduce_result.setter
    def detect_reproduce_result(self, detect_reproduce_result):
        r"""Sets the detect_reproduce_result of this CambodianIdCardResult.

        身份证是否经过翻拍的告警结果，“true”表示身份证经过翻拍，“false”表示身份证未经过翻拍。仅在输入参数detect_reproduce为true时，返回该字段。 

        :param detect_reproduce_result: The detect_reproduce_result of this CambodianIdCardResult.
        :type detect_reproduce_result: bool
        """
        self._detect_reproduce_result = detect_reproduce_result

    @property
    def score_info(self):
        r"""Gets the score_info of this CambodianIdCardResult.

        :return: The score_info of this CambodianIdCardResult.
        :rtype: :class:`huaweicloudsdkocr.v1.CambodianIdCardScoreInformationResult`
        """
        return self._score_info

    @score_info.setter
    def score_info(self, score_info):
        r"""Sets the score_info of this CambodianIdCardResult.

        :param score_info: The score_info of this CambodianIdCardResult.
        :type score_info: :class:`huaweicloudsdkocr.v1.CambodianIdCardScoreInformationResult`
        """
        self._score_info = score_info

    @property
    def confidence(self):
        r"""Gets the confidence of this CambodianIdCardResult.

        相关字段的置信度信息，置信度越大，表示本次识别的对应字段的可靠性越高，在统计意义上，置信度越大，准确率越高。 置信度由算法给出，不直接等价于对应字段的准确率。 

        :return: The confidence of this CambodianIdCardResult.
        :rtype: object
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        r"""Sets the confidence of this CambodianIdCardResult.

        相关字段的置信度信息，置信度越大，表示本次识别的对应字段的可靠性越高，在统计意义上，置信度越大，准确率越高。 置信度由算法给出，不直接等价于对应字段的准确率。 

        :param confidence: The confidence of this CambodianIdCardResult.
        :type confidence: object
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
        if not isinstance(other, CambodianIdCardResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
