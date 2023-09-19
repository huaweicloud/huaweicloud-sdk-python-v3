# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VietnamIdCardResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'side': 'str',
        'number': 'str',
        'full_name': 'str',
        'birth_date': 'str',
        'sex': 'str',
        'nationality': 'str',
        'origin_place': 'str',
        'residence_place': 'str',
        'expiry_date': 'str',
        'personal_identification': 'str',
        'issue_date': 'str',
        'machine_code1': 'str',
        'machine_code2': 'str',
        'machine_code3': 'str',
        'confidence': 'object',
        'portrait_image': 'str',
        'portrait_location': 'list[list[int]]',
        'idcard_type': 'str',
        'text_location': 'object'
    }

    attribute_map = {
        'side': 'side',
        'number': 'number',
        'full_name': 'full_name',
        'birth_date': 'birth_date',
        'sex': 'sex',
        'nationality': 'nationality',
        'origin_place': 'origin_place',
        'residence_place': 'residence_place',
        'expiry_date': 'expiry_date',
        'personal_identification': 'personal_identification',
        'issue_date': 'issue_date',
        'machine_code1': 'machine_code1',
        'machine_code2': 'machine_code2',
        'machine_code3': 'machine_code3',
        'confidence': 'confidence',
        'portrait_image': 'portrait_image',
        'portrait_location': 'portrait_location',
        'idcard_type': 'idcard_type',
        'text_location': 'text_location'
    }

    def __init__(self, side=None, number=None, full_name=None, birth_date=None, sex=None, nationality=None, origin_place=None, residence_place=None, expiry_date=None, personal_identification=None, issue_date=None, machine_code1=None, machine_code2=None, machine_code3=None, confidence=None, portrait_image=None, portrait_location=None, idcard_type=None, text_location=None):
        """VietnamIdCardResult

        The model defined in huaweicloud sdk

        :param side: 返回证件正反面。字段值为“front”或“back” 
        :type side: str
        :param number: 卡证编号。 
        :type number: str
        :param full_name: 姓名。 
        :type full_name: str
        :param birth_date: 出生日期。 
        :type birth_date: str
        :param sex: 性别。 
        :type sex: str
        :param nationality: 国籍。 
        :type nationality: str
        :param origin_place: 籍贯。 
        :type origin_place: str
        :param residence_place: 居住地。 
        :type residence_place: str
        :param expiry_date: 有效日期。 
        :type expiry_date: str
        :param personal_identification: 个人识别。当参数“side”为back时，返回此字段。 
        :type personal_identification: str
        :param issue_date: 签发日期。当参数“side”为back时，返回此字段。 
        :type issue_date: str
        :param machine_code1: 身份证背面第一行机器码。当参数“side”为back时，返回此字段。 
        :type machine_code1: str
        :param machine_code2: 身份证背面第二行机器码。当参数“side”为back时，返回此字段。 
        :type machine_code2: str
        :param machine_code3: 身份证背面第三行机器码。当参数“side”为back时，返回此字段。 
        :type machine_code3: str
        :param confidence: 相关字段的置信度信息，置信度越大，表示本次识别的对应字段的可靠性越高，在统计意义上，置信度越大，准确率越高。注：置信度由算法给出，不直接等价于对应字段的准确率。 
        :type confidence: object
        :param portrait_image: 当参数return_portrait_image为true时，返回头像的base64编码。 
        :type portrait_image: str
        :param portrait_location: 当参数return_portrait_location为true时，返回头像在原图上的位置，以列表形式表示，包含头像区域四个顶点的二维坐标（x,y）；坐标原点为图片左上角，x轴沿水平方向，y轴沿竖直方向。 
        :type portrait_location: list[list[int]]
        :param idcard_type: 输入参数return_idcard_type为true时，返回身份证的类型：normal是身份证原件，copy是复印的身份证，screen是屏幕翻拍。 
        :type idcard_type: str
        :param text_location: 对应所有在原图上识别到的字段位置信息，包含所有文字区域四个顶点的二维坐标（x,y）。采用图像坐标系，坐标原点为图片左上角，x轴沿水平方向，y轴沿竖直方向。 
        :type text_location: object
        """
        
        

        self._side = None
        self._number = None
        self._full_name = None
        self._birth_date = None
        self._sex = None
        self._nationality = None
        self._origin_place = None
        self._residence_place = None
        self._expiry_date = None
        self._personal_identification = None
        self._issue_date = None
        self._machine_code1 = None
        self._machine_code2 = None
        self._machine_code3 = None
        self._confidence = None
        self._portrait_image = None
        self._portrait_location = None
        self._idcard_type = None
        self._text_location = None
        self.discriminator = None

        if side is not None:
            self.side = side
        if number is not None:
            self.number = number
        if full_name is not None:
            self.full_name = full_name
        if birth_date is not None:
            self.birth_date = birth_date
        if sex is not None:
            self.sex = sex
        if nationality is not None:
            self.nationality = nationality
        if origin_place is not None:
            self.origin_place = origin_place
        if residence_place is not None:
            self.residence_place = residence_place
        if expiry_date is not None:
            self.expiry_date = expiry_date
        if personal_identification is not None:
            self.personal_identification = personal_identification
        if issue_date is not None:
            self.issue_date = issue_date
        if machine_code1 is not None:
            self.machine_code1 = machine_code1
        if machine_code2 is not None:
            self.machine_code2 = machine_code2
        if machine_code3 is not None:
            self.machine_code3 = machine_code3
        if confidence is not None:
            self.confidence = confidence
        if portrait_image is not None:
            self.portrait_image = portrait_image
        if portrait_location is not None:
            self.portrait_location = portrait_location
        if idcard_type is not None:
            self.idcard_type = idcard_type
        if text_location is not None:
            self.text_location = text_location

    @property
    def side(self):
        """Gets the side of this VietnamIdCardResult.

        返回证件正反面。字段值为“front”或“back” 

        :return: The side of this VietnamIdCardResult.
        :rtype: str
        """
        return self._side

    @side.setter
    def side(self, side):
        """Sets the side of this VietnamIdCardResult.

        返回证件正反面。字段值为“front”或“back” 

        :param side: The side of this VietnamIdCardResult.
        :type side: str
        """
        self._side = side

    @property
    def number(self):
        """Gets the number of this VietnamIdCardResult.

        卡证编号。 

        :return: The number of this VietnamIdCardResult.
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this VietnamIdCardResult.

        卡证编号。 

        :param number: The number of this VietnamIdCardResult.
        :type number: str
        """
        self._number = number

    @property
    def full_name(self):
        """Gets the full_name of this VietnamIdCardResult.

        姓名。 

        :return: The full_name of this VietnamIdCardResult.
        :rtype: str
        """
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        """Sets the full_name of this VietnamIdCardResult.

        姓名。 

        :param full_name: The full_name of this VietnamIdCardResult.
        :type full_name: str
        """
        self._full_name = full_name

    @property
    def birth_date(self):
        """Gets the birth_date of this VietnamIdCardResult.

        出生日期。 

        :return: The birth_date of this VietnamIdCardResult.
        :rtype: str
        """
        return self._birth_date

    @birth_date.setter
    def birth_date(self, birth_date):
        """Sets the birth_date of this VietnamIdCardResult.

        出生日期。 

        :param birth_date: The birth_date of this VietnamIdCardResult.
        :type birth_date: str
        """
        self._birth_date = birth_date

    @property
    def sex(self):
        """Gets the sex of this VietnamIdCardResult.

        性别。 

        :return: The sex of this VietnamIdCardResult.
        :rtype: str
        """
        return self._sex

    @sex.setter
    def sex(self, sex):
        """Sets the sex of this VietnamIdCardResult.

        性别。 

        :param sex: The sex of this VietnamIdCardResult.
        :type sex: str
        """
        self._sex = sex

    @property
    def nationality(self):
        """Gets the nationality of this VietnamIdCardResult.

        国籍。 

        :return: The nationality of this VietnamIdCardResult.
        :rtype: str
        """
        return self._nationality

    @nationality.setter
    def nationality(self, nationality):
        """Sets the nationality of this VietnamIdCardResult.

        国籍。 

        :param nationality: The nationality of this VietnamIdCardResult.
        :type nationality: str
        """
        self._nationality = nationality

    @property
    def origin_place(self):
        """Gets the origin_place of this VietnamIdCardResult.

        籍贯。 

        :return: The origin_place of this VietnamIdCardResult.
        :rtype: str
        """
        return self._origin_place

    @origin_place.setter
    def origin_place(self, origin_place):
        """Sets the origin_place of this VietnamIdCardResult.

        籍贯。 

        :param origin_place: The origin_place of this VietnamIdCardResult.
        :type origin_place: str
        """
        self._origin_place = origin_place

    @property
    def residence_place(self):
        """Gets the residence_place of this VietnamIdCardResult.

        居住地。 

        :return: The residence_place of this VietnamIdCardResult.
        :rtype: str
        """
        return self._residence_place

    @residence_place.setter
    def residence_place(self, residence_place):
        """Sets the residence_place of this VietnamIdCardResult.

        居住地。 

        :param residence_place: The residence_place of this VietnamIdCardResult.
        :type residence_place: str
        """
        self._residence_place = residence_place

    @property
    def expiry_date(self):
        """Gets the expiry_date of this VietnamIdCardResult.

        有效日期。 

        :return: The expiry_date of this VietnamIdCardResult.
        :rtype: str
        """
        return self._expiry_date

    @expiry_date.setter
    def expiry_date(self, expiry_date):
        """Sets the expiry_date of this VietnamIdCardResult.

        有效日期。 

        :param expiry_date: The expiry_date of this VietnamIdCardResult.
        :type expiry_date: str
        """
        self._expiry_date = expiry_date

    @property
    def personal_identification(self):
        """Gets the personal_identification of this VietnamIdCardResult.

        个人识别。当参数“side”为back时，返回此字段。 

        :return: The personal_identification of this VietnamIdCardResult.
        :rtype: str
        """
        return self._personal_identification

    @personal_identification.setter
    def personal_identification(self, personal_identification):
        """Sets the personal_identification of this VietnamIdCardResult.

        个人识别。当参数“side”为back时，返回此字段。 

        :param personal_identification: The personal_identification of this VietnamIdCardResult.
        :type personal_identification: str
        """
        self._personal_identification = personal_identification

    @property
    def issue_date(self):
        """Gets the issue_date of this VietnamIdCardResult.

        签发日期。当参数“side”为back时，返回此字段。 

        :return: The issue_date of this VietnamIdCardResult.
        :rtype: str
        """
        return self._issue_date

    @issue_date.setter
    def issue_date(self, issue_date):
        """Sets the issue_date of this VietnamIdCardResult.

        签发日期。当参数“side”为back时，返回此字段。 

        :param issue_date: The issue_date of this VietnamIdCardResult.
        :type issue_date: str
        """
        self._issue_date = issue_date

    @property
    def machine_code1(self):
        """Gets the machine_code1 of this VietnamIdCardResult.

        身份证背面第一行机器码。当参数“side”为back时，返回此字段。 

        :return: The machine_code1 of this VietnamIdCardResult.
        :rtype: str
        """
        return self._machine_code1

    @machine_code1.setter
    def machine_code1(self, machine_code1):
        """Sets the machine_code1 of this VietnamIdCardResult.

        身份证背面第一行机器码。当参数“side”为back时，返回此字段。 

        :param machine_code1: The machine_code1 of this VietnamIdCardResult.
        :type machine_code1: str
        """
        self._machine_code1 = machine_code1

    @property
    def machine_code2(self):
        """Gets the machine_code2 of this VietnamIdCardResult.

        身份证背面第二行机器码。当参数“side”为back时，返回此字段。 

        :return: The machine_code2 of this VietnamIdCardResult.
        :rtype: str
        """
        return self._machine_code2

    @machine_code2.setter
    def machine_code2(self, machine_code2):
        """Sets the machine_code2 of this VietnamIdCardResult.

        身份证背面第二行机器码。当参数“side”为back时，返回此字段。 

        :param machine_code2: The machine_code2 of this VietnamIdCardResult.
        :type machine_code2: str
        """
        self._machine_code2 = machine_code2

    @property
    def machine_code3(self):
        """Gets the machine_code3 of this VietnamIdCardResult.

        身份证背面第三行机器码。当参数“side”为back时，返回此字段。 

        :return: The machine_code3 of this VietnamIdCardResult.
        :rtype: str
        """
        return self._machine_code3

    @machine_code3.setter
    def machine_code3(self, machine_code3):
        """Sets the machine_code3 of this VietnamIdCardResult.

        身份证背面第三行机器码。当参数“side”为back时，返回此字段。 

        :param machine_code3: The machine_code3 of this VietnamIdCardResult.
        :type machine_code3: str
        """
        self._machine_code3 = machine_code3

    @property
    def confidence(self):
        """Gets the confidence of this VietnamIdCardResult.

        相关字段的置信度信息，置信度越大，表示本次识别的对应字段的可靠性越高，在统计意义上，置信度越大，准确率越高。注：置信度由算法给出，不直接等价于对应字段的准确率。 

        :return: The confidence of this VietnamIdCardResult.
        :rtype: object
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        """Sets the confidence of this VietnamIdCardResult.

        相关字段的置信度信息，置信度越大，表示本次识别的对应字段的可靠性越高，在统计意义上，置信度越大，准确率越高。注：置信度由算法给出，不直接等价于对应字段的准确率。 

        :param confidence: The confidence of this VietnamIdCardResult.
        :type confidence: object
        """
        self._confidence = confidence

    @property
    def portrait_image(self):
        """Gets the portrait_image of this VietnamIdCardResult.

        当参数return_portrait_image为true时，返回头像的base64编码。 

        :return: The portrait_image of this VietnamIdCardResult.
        :rtype: str
        """
        return self._portrait_image

    @portrait_image.setter
    def portrait_image(self, portrait_image):
        """Sets the portrait_image of this VietnamIdCardResult.

        当参数return_portrait_image为true时，返回头像的base64编码。 

        :param portrait_image: The portrait_image of this VietnamIdCardResult.
        :type portrait_image: str
        """
        self._portrait_image = portrait_image

    @property
    def portrait_location(self):
        """Gets the portrait_location of this VietnamIdCardResult.

        当参数return_portrait_location为true时，返回头像在原图上的位置，以列表形式表示，包含头像区域四个顶点的二维坐标（x,y）；坐标原点为图片左上角，x轴沿水平方向，y轴沿竖直方向。 

        :return: The portrait_location of this VietnamIdCardResult.
        :rtype: list[list[int]]
        """
        return self._portrait_location

    @portrait_location.setter
    def portrait_location(self, portrait_location):
        """Sets the portrait_location of this VietnamIdCardResult.

        当参数return_portrait_location为true时，返回头像在原图上的位置，以列表形式表示，包含头像区域四个顶点的二维坐标（x,y）；坐标原点为图片左上角，x轴沿水平方向，y轴沿竖直方向。 

        :param portrait_location: The portrait_location of this VietnamIdCardResult.
        :type portrait_location: list[list[int]]
        """
        self._portrait_location = portrait_location

    @property
    def idcard_type(self):
        """Gets the idcard_type of this VietnamIdCardResult.

        输入参数return_idcard_type为true时，返回身份证的类型：normal是身份证原件，copy是复印的身份证，screen是屏幕翻拍。 

        :return: The idcard_type of this VietnamIdCardResult.
        :rtype: str
        """
        return self._idcard_type

    @idcard_type.setter
    def idcard_type(self, idcard_type):
        """Sets the idcard_type of this VietnamIdCardResult.

        输入参数return_idcard_type为true时，返回身份证的类型：normal是身份证原件，copy是复印的身份证，screen是屏幕翻拍。 

        :param idcard_type: The idcard_type of this VietnamIdCardResult.
        :type idcard_type: str
        """
        self._idcard_type = idcard_type

    @property
    def text_location(self):
        """Gets the text_location of this VietnamIdCardResult.

        对应所有在原图上识别到的字段位置信息，包含所有文字区域四个顶点的二维坐标（x,y）。采用图像坐标系，坐标原点为图片左上角，x轴沿水平方向，y轴沿竖直方向。 

        :return: The text_location of this VietnamIdCardResult.
        :rtype: object
        """
        return self._text_location

    @text_location.setter
    def text_location(self, text_location):
        """Sets the text_location of this VietnamIdCardResult.

        对应所有在原图上识别到的字段位置信息，包含所有文字区域四个顶点的二维坐标（x,y）。采用图像坐标系，坐标原点为图片左上角，x轴沿水平方向，y轴沿竖直方向。 

        :param text_location: The text_location of this VietnamIdCardResult.
        :type text_location: object
        """
        self._text_location = text_location

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
        if not isinstance(other, VietnamIdCardResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
