# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MainlandTravelPermitResult:

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
        'birth_date': 'str',
        'sex': 'str',
        'valid_period': 'str',
        'issuing_authority': 'str',
        'number': 'str',
        'issue_place': 'str',
        'issue_times': 'str',
        'id_name': 'str',
        'id_number': 'str',
        'machine_code1': 'str',
        'machine_code2': 'str',
        'machine_code3': 'str',
        'type': 'str',
        'side': 'str',
        'portrait_image': 'str',
        'portrait_location': 'list[list[int]]',
        'confidence': 'MainlandTravelPermitConfidence'
    }

    attribute_map = {
        'name': 'name',
        'name_en': 'name_en',
        'birth_date': 'birth_date',
        'sex': 'sex',
        'valid_period': 'valid_period',
        'issuing_authority': 'issuing_authority',
        'number': 'number',
        'issue_place': 'issue_place',
        'issue_times': 'issue_times',
        'id_name': 'id_name',
        'id_number': 'id_number',
        'machine_code1': 'machine_code1',
        'machine_code2': 'machine_code2',
        'machine_code3': 'machine_code3',
        'type': 'type',
        'side': 'side',
        'portrait_image': 'portrait_image',
        'portrait_location': 'portrait_location',
        'confidence': 'confidence'
    }

    def __init__(self, name=None, name_en=None, birth_date=None, sex=None, valid_period=None, issuing_authority=None, number=None, issue_place=None, issue_times=None, id_name=None, id_number=None, machine_code1=None, machine_code2=None, machine_code3=None, type=None, side=None, portrait_image=None, portrait_location=None, confidence=None):
        """MainlandTravelPermitResult

        The model defined in huaweicloud sdk

        :param name: 中文姓名。 
        :type name: str
        :param name_en: 英文姓名。 
        :type name_en: str
        :param birth_date: 出生日期。 
        :type birth_date: str
        :param sex: 性别。 
        :type sex: str
        :param valid_period: 有效期限。 
        :type valid_period: str
        :param issuing_authority: 签发机关。 
        :type issuing_authority: str
        :param number: 证件号。 
        :type number: str
        :param issue_place: 签发地点。 
        :type issue_place: str
        :param issue_times: 签发次数。 
        :type issue_times: str
        :param id_name: 回乡证背面的香港/澳门/台湾身份证姓名。 
        :type id_name: str
        :param id_number: 回乡证背面的香港/澳门/台湾身份证号码。 
        :type id_number: str
        :param machine_code1: 机读码第一行。 
        :type machine_code1: str
        :param machine_code2: 机读码第二行。 
        :type machine_code2: str
        :param machine_code3: 机读码第三行。 
        :type machine_code3: str
        :param type: 证件类别。可选值包括： - “港澳居民来往内地通行证” - “台湾居民来往大陆通行证” 
        :type type: str
        :param side: 证件图片正反面信息。可选值包括： - \&quot;front\&quot;：证件图片为正面 - \&quot;back\&quot;：证件图片为反面 
        :type side: str
        :param portrait_image: 头像的base64编码。当输入参数“return_portrait_image”为“true”时，才返回该参数。 
        :type portrait_image: str
        :param portrait_location: 头像在原图上的位置。 当输入参数“return_portrait_location”为“true”时，才返回该参数。以列表形式显示，包含头像区域四个顶点的二维坐标（x,y），坐标原点为图片左上角，x轴沿水平方向，y轴沿竖直方向。 
        :type portrait_location: list[list[int]]
        :param confidence: 
        :type confidence: :class:`huaweicloudsdkocr.v1.MainlandTravelPermitConfidence`
        """
        
        

        self._name = None
        self._name_en = None
        self._birth_date = None
        self._sex = None
        self._valid_period = None
        self._issuing_authority = None
        self._number = None
        self._issue_place = None
        self._issue_times = None
        self._id_name = None
        self._id_number = None
        self._machine_code1 = None
        self._machine_code2 = None
        self._machine_code3 = None
        self._type = None
        self._side = None
        self._portrait_image = None
        self._portrait_location = None
        self._confidence = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if name_en is not None:
            self.name_en = name_en
        if birth_date is not None:
            self.birth_date = birth_date
        if sex is not None:
            self.sex = sex
        if valid_period is not None:
            self.valid_period = valid_period
        if issuing_authority is not None:
            self.issuing_authority = issuing_authority
        if number is not None:
            self.number = number
        if issue_place is not None:
            self.issue_place = issue_place
        if issue_times is not None:
            self.issue_times = issue_times
        if id_name is not None:
            self.id_name = id_name
        if id_number is not None:
            self.id_number = id_number
        if machine_code1 is not None:
            self.machine_code1 = machine_code1
        if machine_code2 is not None:
            self.machine_code2 = machine_code2
        if machine_code3 is not None:
            self.machine_code3 = machine_code3
        if type is not None:
            self.type = type
        if side is not None:
            self.side = side
        if portrait_image is not None:
            self.portrait_image = portrait_image
        if portrait_location is not None:
            self.portrait_location = portrait_location
        if confidence is not None:
            self.confidence = confidence

    @property
    def name(self):
        """Gets the name of this MainlandTravelPermitResult.

        中文姓名。 

        :return: The name of this MainlandTravelPermitResult.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MainlandTravelPermitResult.

        中文姓名。 

        :param name: The name of this MainlandTravelPermitResult.
        :type name: str
        """
        self._name = name

    @property
    def name_en(self):
        """Gets the name_en of this MainlandTravelPermitResult.

        英文姓名。 

        :return: The name_en of this MainlandTravelPermitResult.
        :rtype: str
        """
        return self._name_en

    @name_en.setter
    def name_en(self, name_en):
        """Sets the name_en of this MainlandTravelPermitResult.

        英文姓名。 

        :param name_en: The name_en of this MainlandTravelPermitResult.
        :type name_en: str
        """
        self._name_en = name_en

    @property
    def birth_date(self):
        """Gets the birth_date of this MainlandTravelPermitResult.

        出生日期。 

        :return: The birth_date of this MainlandTravelPermitResult.
        :rtype: str
        """
        return self._birth_date

    @birth_date.setter
    def birth_date(self, birth_date):
        """Sets the birth_date of this MainlandTravelPermitResult.

        出生日期。 

        :param birth_date: The birth_date of this MainlandTravelPermitResult.
        :type birth_date: str
        """
        self._birth_date = birth_date

    @property
    def sex(self):
        """Gets the sex of this MainlandTravelPermitResult.

        性别。 

        :return: The sex of this MainlandTravelPermitResult.
        :rtype: str
        """
        return self._sex

    @sex.setter
    def sex(self, sex):
        """Sets the sex of this MainlandTravelPermitResult.

        性别。 

        :param sex: The sex of this MainlandTravelPermitResult.
        :type sex: str
        """
        self._sex = sex

    @property
    def valid_period(self):
        """Gets the valid_period of this MainlandTravelPermitResult.

        有效期限。 

        :return: The valid_period of this MainlandTravelPermitResult.
        :rtype: str
        """
        return self._valid_period

    @valid_period.setter
    def valid_period(self, valid_period):
        """Sets the valid_period of this MainlandTravelPermitResult.

        有效期限。 

        :param valid_period: The valid_period of this MainlandTravelPermitResult.
        :type valid_period: str
        """
        self._valid_period = valid_period

    @property
    def issuing_authority(self):
        """Gets the issuing_authority of this MainlandTravelPermitResult.

        签发机关。 

        :return: The issuing_authority of this MainlandTravelPermitResult.
        :rtype: str
        """
        return self._issuing_authority

    @issuing_authority.setter
    def issuing_authority(self, issuing_authority):
        """Sets the issuing_authority of this MainlandTravelPermitResult.

        签发机关。 

        :param issuing_authority: The issuing_authority of this MainlandTravelPermitResult.
        :type issuing_authority: str
        """
        self._issuing_authority = issuing_authority

    @property
    def number(self):
        """Gets the number of this MainlandTravelPermitResult.

        证件号。 

        :return: The number of this MainlandTravelPermitResult.
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this MainlandTravelPermitResult.

        证件号。 

        :param number: The number of this MainlandTravelPermitResult.
        :type number: str
        """
        self._number = number

    @property
    def issue_place(self):
        """Gets the issue_place of this MainlandTravelPermitResult.

        签发地点。 

        :return: The issue_place of this MainlandTravelPermitResult.
        :rtype: str
        """
        return self._issue_place

    @issue_place.setter
    def issue_place(self, issue_place):
        """Sets the issue_place of this MainlandTravelPermitResult.

        签发地点。 

        :param issue_place: The issue_place of this MainlandTravelPermitResult.
        :type issue_place: str
        """
        self._issue_place = issue_place

    @property
    def issue_times(self):
        """Gets the issue_times of this MainlandTravelPermitResult.

        签发次数。 

        :return: The issue_times of this MainlandTravelPermitResult.
        :rtype: str
        """
        return self._issue_times

    @issue_times.setter
    def issue_times(self, issue_times):
        """Sets the issue_times of this MainlandTravelPermitResult.

        签发次数。 

        :param issue_times: The issue_times of this MainlandTravelPermitResult.
        :type issue_times: str
        """
        self._issue_times = issue_times

    @property
    def id_name(self):
        """Gets the id_name of this MainlandTravelPermitResult.

        回乡证背面的香港/澳门/台湾身份证姓名。 

        :return: The id_name of this MainlandTravelPermitResult.
        :rtype: str
        """
        return self._id_name

    @id_name.setter
    def id_name(self, id_name):
        """Sets the id_name of this MainlandTravelPermitResult.

        回乡证背面的香港/澳门/台湾身份证姓名。 

        :param id_name: The id_name of this MainlandTravelPermitResult.
        :type id_name: str
        """
        self._id_name = id_name

    @property
    def id_number(self):
        """Gets the id_number of this MainlandTravelPermitResult.

        回乡证背面的香港/澳门/台湾身份证号码。 

        :return: The id_number of this MainlandTravelPermitResult.
        :rtype: str
        """
        return self._id_number

    @id_number.setter
    def id_number(self, id_number):
        """Sets the id_number of this MainlandTravelPermitResult.

        回乡证背面的香港/澳门/台湾身份证号码。 

        :param id_number: The id_number of this MainlandTravelPermitResult.
        :type id_number: str
        """
        self._id_number = id_number

    @property
    def machine_code1(self):
        """Gets the machine_code1 of this MainlandTravelPermitResult.

        机读码第一行。 

        :return: The machine_code1 of this MainlandTravelPermitResult.
        :rtype: str
        """
        return self._machine_code1

    @machine_code1.setter
    def machine_code1(self, machine_code1):
        """Sets the machine_code1 of this MainlandTravelPermitResult.

        机读码第一行。 

        :param machine_code1: The machine_code1 of this MainlandTravelPermitResult.
        :type machine_code1: str
        """
        self._machine_code1 = machine_code1

    @property
    def machine_code2(self):
        """Gets the machine_code2 of this MainlandTravelPermitResult.

        机读码第二行。 

        :return: The machine_code2 of this MainlandTravelPermitResult.
        :rtype: str
        """
        return self._machine_code2

    @machine_code2.setter
    def machine_code2(self, machine_code2):
        """Sets the machine_code2 of this MainlandTravelPermitResult.

        机读码第二行。 

        :param machine_code2: The machine_code2 of this MainlandTravelPermitResult.
        :type machine_code2: str
        """
        self._machine_code2 = machine_code2

    @property
    def machine_code3(self):
        """Gets the machine_code3 of this MainlandTravelPermitResult.

        机读码第三行。 

        :return: The machine_code3 of this MainlandTravelPermitResult.
        :rtype: str
        """
        return self._machine_code3

    @machine_code3.setter
    def machine_code3(self, machine_code3):
        """Sets the machine_code3 of this MainlandTravelPermitResult.

        机读码第三行。 

        :param machine_code3: The machine_code3 of this MainlandTravelPermitResult.
        :type machine_code3: str
        """
        self._machine_code3 = machine_code3

    @property
    def type(self):
        """Gets the type of this MainlandTravelPermitResult.

        证件类别。可选值包括： - “港澳居民来往内地通行证” - “台湾居民来往大陆通行证” 

        :return: The type of this MainlandTravelPermitResult.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this MainlandTravelPermitResult.

        证件类别。可选值包括： - “港澳居民来往内地通行证” - “台湾居民来往大陆通行证” 

        :param type: The type of this MainlandTravelPermitResult.
        :type type: str
        """
        self._type = type

    @property
    def side(self):
        """Gets the side of this MainlandTravelPermitResult.

        证件图片正反面信息。可选值包括： - \"front\"：证件图片为正面 - \"back\"：证件图片为反面 

        :return: The side of this MainlandTravelPermitResult.
        :rtype: str
        """
        return self._side

    @side.setter
    def side(self, side):
        """Sets the side of this MainlandTravelPermitResult.

        证件图片正反面信息。可选值包括： - \"front\"：证件图片为正面 - \"back\"：证件图片为反面 

        :param side: The side of this MainlandTravelPermitResult.
        :type side: str
        """
        self._side = side

    @property
    def portrait_image(self):
        """Gets the portrait_image of this MainlandTravelPermitResult.

        头像的base64编码。当输入参数“return_portrait_image”为“true”时，才返回该参数。 

        :return: The portrait_image of this MainlandTravelPermitResult.
        :rtype: str
        """
        return self._portrait_image

    @portrait_image.setter
    def portrait_image(self, portrait_image):
        """Sets the portrait_image of this MainlandTravelPermitResult.

        头像的base64编码。当输入参数“return_portrait_image”为“true”时，才返回该参数。 

        :param portrait_image: The portrait_image of this MainlandTravelPermitResult.
        :type portrait_image: str
        """
        self._portrait_image = portrait_image

    @property
    def portrait_location(self):
        """Gets the portrait_location of this MainlandTravelPermitResult.

        头像在原图上的位置。 当输入参数“return_portrait_location”为“true”时，才返回该参数。以列表形式显示，包含头像区域四个顶点的二维坐标（x,y），坐标原点为图片左上角，x轴沿水平方向，y轴沿竖直方向。 

        :return: The portrait_location of this MainlandTravelPermitResult.
        :rtype: list[list[int]]
        """
        return self._portrait_location

    @portrait_location.setter
    def portrait_location(self, portrait_location):
        """Sets the portrait_location of this MainlandTravelPermitResult.

        头像在原图上的位置。 当输入参数“return_portrait_location”为“true”时，才返回该参数。以列表形式显示，包含头像区域四个顶点的二维坐标（x,y），坐标原点为图片左上角，x轴沿水平方向，y轴沿竖直方向。 

        :param portrait_location: The portrait_location of this MainlandTravelPermitResult.
        :type portrait_location: list[list[int]]
        """
        self._portrait_location = portrait_location

    @property
    def confidence(self):
        """Gets the confidence of this MainlandTravelPermitResult.


        :return: The confidence of this MainlandTravelPermitResult.
        :rtype: :class:`huaweicloudsdkocr.v1.MainlandTravelPermitConfidence`
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        """Sets the confidence of this MainlandTravelPermitResult.


        :param confidence: The confidence of this MainlandTravelPermitResult.
        :type confidence: :class:`huaweicloudsdkocr.v1.MainlandTravelPermitConfidence`
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
        if not isinstance(other, MainlandTravelPermitResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
