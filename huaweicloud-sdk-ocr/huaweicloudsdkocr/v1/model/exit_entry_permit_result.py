# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExitEntryPermitResult:

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
        'name_en': 'str',
        'sex': 'str',
        'birth_date': 'str',
        'number': 'str',
        'issuing_authority': 'str',
        'issue_place': 'str',
        'valid_period': 'str',
        'machine_code': 'str',
        'portrait_image': 'str',
        'portrait_location': 'list[list[int]]',
        'type': 'str',
        'side': 'str',
        'endorsement_info_hk': 'ExitEntryPermitEndorsementInfo',
        'endorsement_info_mo': 'ExitEntryPermitEndorsementInfo',
        'endorsement_info_tw': 'ExitEntryPermitEndorsementInfo',
        'confidence': 'ExitEntryPermitConfidence'
    }

    attribute_map = {
        'name': 'name',
        'name_en': 'name_en',
        'sex': 'sex',
        'birth_date': 'birth_date',
        'number': 'number',
        'issuing_authority': 'issuing_authority',
        'issue_place': 'issue_place',
        'valid_period': 'valid_period',
        'machine_code': 'machine_code',
        'portrait_image': 'portrait_image',
        'portrait_location': 'portrait_location',
        'type': 'type',
        'side': 'side',
        'endorsement_info_hk': 'endorsement_info_hk',
        'endorsement_info_mo': 'endorsement_info_mo',
        'endorsement_info_tw': 'endorsement_info_tw',
        'confidence': 'confidence'
    }

    def __init__(self, name=None, name_en=None, sex=None, birth_date=None, number=None, issuing_authority=None, issue_place=None, valid_period=None, machine_code=None, portrait_image=None, portrait_location=None, type=None, side=None, endorsement_info_hk=None, endorsement_info_mo=None, endorsement_info_tw=None, confidence=None):
        r"""ExitEntryPermitResult

        The model defined in huaweicloud sdk

        :param name: 姓名。 
        :type name: str
        :param name_en: 英文姓名。 
        :type name_en: str
        :param sex: 性别。 
        :type sex: str
        :param birth_date: 出生日期。 
        :type birth_date: str
        :param number: 证件号。 
        :type number: str
        :param issuing_authority: 签发机关。 
        :type issuing_authority: str
        :param issue_place: 签发地点。 
        :type issue_place: str
        :param valid_period: 有效期限。 
        :type valid_period: str
        :param machine_code: 机器码。 
        :type machine_code: str
        :param portrait_image: 头像的base64编码。当输入参数“return_portrait_image”为“true”时，才返回该参数。 
        :type portrait_image: str
        :param portrait_location: 头像在原图上的位置。 当输入参数“return_portrait_location”为“true”时，才返回该参数。以列表形式显示，包含头像区域四个顶点的二维坐标（x,y），坐标原点为图片左上角，x轴沿水平方向，y轴沿竖直方向。 
        :type portrait_location: list[list[int]]
        :param type: 证件类型。可选值包括： - \&quot;往来港澳通行证 \&quot; - \&quot;往来台湾通行证\&quot; 
        :type type: str
        :param side: 证件图片正反面信息。可选值包括： - \&quot;front\&quot;：证件图片为正面 - \&quot;back\&quot;：证件图片为反面 
        :type side: str
        :param endorsement_info_hk: 
        :type endorsement_info_hk: :class:`huaweicloudsdkocr.v1.ExitEntryPermitEndorsementInfo`
        :param endorsement_info_mo: 
        :type endorsement_info_mo: :class:`huaweicloudsdkocr.v1.ExitEntryPermitEndorsementInfo`
        :param endorsement_info_tw: 
        :type endorsement_info_tw: :class:`huaweicloudsdkocr.v1.ExitEntryPermitEndorsementInfo`
        :param confidence: 
        :type confidence: :class:`huaweicloudsdkocr.v1.ExitEntryPermitConfidence`
        """
        
        

        self._name = None
        self._name_en = None
        self._sex = None
        self._birth_date = None
        self._number = None
        self._issuing_authority = None
        self._issue_place = None
        self._valid_period = None
        self._machine_code = None
        self._portrait_image = None
        self._portrait_location = None
        self._type = None
        self._side = None
        self._endorsement_info_hk = None
        self._endorsement_info_mo = None
        self._endorsement_info_tw = None
        self._confidence = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if name_en is not None:
            self.name_en = name_en
        if sex is not None:
            self.sex = sex
        if birth_date is not None:
            self.birth_date = birth_date
        if number is not None:
            self.number = number
        if issuing_authority is not None:
            self.issuing_authority = issuing_authority
        if issue_place is not None:
            self.issue_place = issue_place
        if valid_period is not None:
            self.valid_period = valid_period
        if machine_code is not None:
            self.machine_code = machine_code
        if portrait_image is not None:
            self.portrait_image = portrait_image
        if portrait_location is not None:
            self.portrait_location = portrait_location
        if type is not None:
            self.type = type
        if side is not None:
            self.side = side
        if endorsement_info_hk is not None:
            self.endorsement_info_hk = endorsement_info_hk
        if endorsement_info_mo is not None:
            self.endorsement_info_mo = endorsement_info_mo
        if endorsement_info_tw is not None:
            self.endorsement_info_tw = endorsement_info_tw
        if confidence is not None:
            self.confidence = confidence

    @property
    def name(self):
        r"""Gets the name of this ExitEntryPermitResult.

        姓名。 

        :return: The name of this ExitEntryPermitResult.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ExitEntryPermitResult.

        姓名。 

        :param name: The name of this ExitEntryPermitResult.
        :type name: str
        """
        self._name = name

    @property
    def name_en(self):
        r"""Gets the name_en of this ExitEntryPermitResult.

        英文姓名。 

        :return: The name_en of this ExitEntryPermitResult.
        :rtype: str
        """
        return self._name_en

    @name_en.setter
    def name_en(self, name_en):
        r"""Sets the name_en of this ExitEntryPermitResult.

        英文姓名。 

        :param name_en: The name_en of this ExitEntryPermitResult.
        :type name_en: str
        """
        self._name_en = name_en

    @property
    def sex(self):
        r"""Gets the sex of this ExitEntryPermitResult.

        性别。 

        :return: The sex of this ExitEntryPermitResult.
        :rtype: str
        """
        return self._sex

    @sex.setter
    def sex(self, sex):
        r"""Sets the sex of this ExitEntryPermitResult.

        性别。 

        :param sex: The sex of this ExitEntryPermitResult.
        :type sex: str
        """
        self._sex = sex

    @property
    def birth_date(self):
        r"""Gets the birth_date of this ExitEntryPermitResult.

        出生日期。 

        :return: The birth_date of this ExitEntryPermitResult.
        :rtype: str
        """
        return self._birth_date

    @birth_date.setter
    def birth_date(self, birth_date):
        r"""Sets the birth_date of this ExitEntryPermitResult.

        出生日期。 

        :param birth_date: The birth_date of this ExitEntryPermitResult.
        :type birth_date: str
        """
        self._birth_date = birth_date

    @property
    def number(self):
        r"""Gets the number of this ExitEntryPermitResult.

        证件号。 

        :return: The number of this ExitEntryPermitResult.
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        r"""Sets the number of this ExitEntryPermitResult.

        证件号。 

        :param number: The number of this ExitEntryPermitResult.
        :type number: str
        """
        self._number = number

    @property
    def issuing_authority(self):
        r"""Gets the issuing_authority of this ExitEntryPermitResult.

        签发机关。 

        :return: The issuing_authority of this ExitEntryPermitResult.
        :rtype: str
        """
        return self._issuing_authority

    @issuing_authority.setter
    def issuing_authority(self, issuing_authority):
        r"""Sets the issuing_authority of this ExitEntryPermitResult.

        签发机关。 

        :param issuing_authority: The issuing_authority of this ExitEntryPermitResult.
        :type issuing_authority: str
        """
        self._issuing_authority = issuing_authority

    @property
    def issue_place(self):
        r"""Gets the issue_place of this ExitEntryPermitResult.

        签发地点。 

        :return: The issue_place of this ExitEntryPermitResult.
        :rtype: str
        """
        return self._issue_place

    @issue_place.setter
    def issue_place(self, issue_place):
        r"""Sets the issue_place of this ExitEntryPermitResult.

        签发地点。 

        :param issue_place: The issue_place of this ExitEntryPermitResult.
        :type issue_place: str
        """
        self._issue_place = issue_place

    @property
    def valid_period(self):
        r"""Gets the valid_period of this ExitEntryPermitResult.

        有效期限。 

        :return: The valid_period of this ExitEntryPermitResult.
        :rtype: str
        """
        return self._valid_period

    @valid_period.setter
    def valid_period(self, valid_period):
        r"""Sets the valid_period of this ExitEntryPermitResult.

        有效期限。 

        :param valid_period: The valid_period of this ExitEntryPermitResult.
        :type valid_period: str
        """
        self._valid_period = valid_period

    @property
    def machine_code(self):
        r"""Gets the machine_code of this ExitEntryPermitResult.

        机器码。 

        :return: The machine_code of this ExitEntryPermitResult.
        :rtype: str
        """
        return self._machine_code

    @machine_code.setter
    def machine_code(self, machine_code):
        r"""Sets the machine_code of this ExitEntryPermitResult.

        机器码。 

        :param machine_code: The machine_code of this ExitEntryPermitResult.
        :type machine_code: str
        """
        self._machine_code = machine_code

    @property
    def portrait_image(self):
        r"""Gets the portrait_image of this ExitEntryPermitResult.

        头像的base64编码。当输入参数“return_portrait_image”为“true”时，才返回该参数。 

        :return: The portrait_image of this ExitEntryPermitResult.
        :rtype: str
        """
        return self._portrait_image

    @portrait_image.setter
    def portrait_image(self, portrait_image):
        r"""Sets the portrait_image of this ExitEntryPermitResult.

        头像的base64编码。当输入参数“return_portrait_image”为“true”时，才返回该参数。 

        :param portrait_image: The portrait_image of this ExitEntryPermitResult.
        :type portrait_image: str
        """
        self._portrait_image = portrait_image

    @property
    def portrait_location(self):
        r"""Gets the portrait_location of this ExitEntryPermitResult.

        头像在原图上的位置。 当输入参数“return_portrait_location”为“true”时，才返回该参数。以列表形式显示，包含头像区域四个顶点的二维坐标（x,y），坐标原点为图片左上角，x轴沿水平方向，y轴沿竖直方向。 

        :return: The portrait_location of this ExitEntryPermitResult.
        :rtype: list[list[int]]
        """
        return self._portrait_location

    @portrait_location.setter
    def portrait_location(self, portrait_location):
        r"""Sets the portrait_location of this ExitEntryPermitResult.

        头像在原图上的位置。 当输入参数“return_portrait_location”为“true”时，才返回该参数。以列表形式显示，包含头像区域四个顶点的二维坐标（x,y），坐标原点为图片左上角，x轴沿水平方向，y轴沿竖直方向。 

        :param portrait_location: The portrait_location of this ExitEntryPermitResult.
        :type portrait_location: list[list[int]]
        """
        self._portrait_location = portrait_location

    @property
    def type(self):
        r"""Gets the type of this ExitEntryPermitResult.

        证件类型。可选值包括： - \"往来港澳通行证 \" - \"往来台湾通行证\" 

        :return: The type of this ExitEntryPermitResult.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ExitEntryPermitResult.

        证件类型。可选值包括： - \"往来港澳通行证 \" - \"往来台湾通行证\" 

        :param type: The type of this ExitEntryPermitResult.
        :type type: str
        """
        self._type = type

    @property
    def side(self):
        r"""Gets the side of this ExitEntryPermitResult.

        证件图片正反面信息。可选值包括： - \"front\"：证件图片为正面 - \"back\"：证件图片为反面 

        :return: The side of this ExitEntryPermitResult.
        :rtype: str
        """
        return self._side

    @side.setter
    def side(self, side):
        r"""Sets the side of this ExitEntryPermitResult.

        证件图片正反面信息。可选值包括： - \"front\"：证件图片为正面 - \"back\"：证件图片为反面 

        :param side: The side of this ExitEntryPermitResult.
        :type side: str
        """
        self._side = side

    @property
    def endorsement_info_hk(self):
        r"""Gets the endorsement_info_hk of this ExitEntryPermitResult.

        :return: The endorsement_info_hk of this ExitEntryPermitResult.
        :rtype: :class:`huaweicloudsdkocr.v1.ExitEntryPermitEndorsementInfo`
        """
        return self._endorsement_info_hk

    @endorsement_info_hk.setter
    def endorsement_info_hk(self, endorsement_info_hk):
        r"""Sets the endorsement_info_hk of this ExitEntryPermitResult.

        :param endorsement_info_hk: The endorsement_info_hk of this ExitEntryPermitResult.
        :type endorsement_info_hk: :class:`huaweicloudsdkocr.v1.ExitEntryPermitEndorsementInfo`
        """
        self._endorsement_info_hk = endorsement_info_hk

    @property
    def endorsement_info_mo(self):
        r"""Gets the endorsement_info_mo of this ExitEntryPermitResult.

        :return: The endorsement_info_mo of this ExitEntryPermitResult.
        :rtype: :class:`huaweicloudsdkocr.v1.ExitEntryPermitEndorsementInfo`
        """
        return self._endorsement_info_mo

    @endorsement_info_mo.setter
    def endorsement_info_mo(self, endorsement_info_mo):
        r"""Sets the endorsement_info_mo of this ExitEntryPermitResult.

        :param endorsement_info_mo: The endorsement_info_mo of this ExitEntryPermitResult.
        :type endorsement_info_mo: :class:`huaweicloudsdkocr.v1.ExitEntryPermitEndorsementInfo`
        """
        self._endorsement_info_mo = endorsement_info_mo

    @property
    def endorsement_info_tw(self):
        r"""Gets the endorsement_info_tw of this ExitEntryPermitResult.

        :return: The endorsement_info_tw of this ExitEntryPermitResult.
        :rtype: :class:`huaweicloudsdkocr.v1.ExitEntryPermitEndorsementInfo`
        """
        return self._endorsement_info_tw

    @endorsement_info_tw.setter
    def endorsement_info_tw(self, endorsement_info_tw):
        r"""Sets the endorsement_info_tw of this ExitEntryPermitResult.

        :param endorsement_info_tw: The endorsement_info_tw of this ExitEntryPermitResult.
        :type endorsement_info_tw: :class:`huaweicloudsdkocr.v1.ExitEntryPermitEndorsementInfo`
        """
        self._endorsement_info_tw = endorsement_info_tw

    @property
    def confidence(self):
        r"""Gets the confidence of this ExitEntryPermitResult.

        :return: The confidence of this ExitEntryPermitResult.
        :rtype: :class:`huaweicloudsdkocr.v1.ExitEntryPermitConfidence`
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        r"""Sets the confidence of this ExitEntryPermitResult.

        :param confidence: The confidence of this ExitEntryPermitResult.
        :type confidence: :class:`huaweicloudsdkocr.v1.ExitEntryPermitConfidence`
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
        if not isinstance(other, ExitEntryPermitResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
