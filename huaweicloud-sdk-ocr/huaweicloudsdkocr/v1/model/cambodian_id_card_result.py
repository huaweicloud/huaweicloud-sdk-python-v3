# coding: utf-8

import re
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
        'confidence': 'confidence'
    }

    def __init__(self, id_number=None, name_kh=None, name_en=None, birth_date=None, sex=None, height=None, birth_place=None, address=None, issue_date=None, expiry_date=None, description=None, machine_code1=None, machine_code2=None, machine_code3=None, portrait_image=None, portrait_location=None, idcard_type=None, confidence=None):
        """CambodianIdCardResult

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
        :param idcard_type: 身份证的类型。当输入参数“ idcard_type ”为“true”时，才返回该参数。取值如下所示： - normal：身份证原件 - copy：复印的身份证 
        :type idcard_type: str
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
        if confidence is not None:
            self.confidence = confidence

    @property
    def id_number(self):
        """Gets the id_number of this CambodianIdCardResult.

        身份证号码。 

        :return: The id_number of this CambodianIdCardResult.
        :rtype: str
        """
        return self._id_number

    @id_number.setter
    def id_number(self, id_number):
        """Sets the id_number of this CambodianIdCardResult.

        身份证号码。 

        :param id_number: The id_number of this CambodianIdCardResult.
        :type id_number: str
        """
        self._id_number = id_number

    @property
    def name_kh(self):
        """Gets the name_kh of this CambodianIdCardResult.

        高棉语版姓名。 

        :return: The name_kh of this CambodianIdCardResult.
        :rtype: str
        """
        return self._name_kh

    @name_kh.setter
    def name_kh(self, name_kh):
        """Sets the name_kh of this CambodianIdCardResult.

        高棉语版姓名。 

        :param name_kh: The name_kh of this CambodianIdCardResult.
        :type name_kh: str
        """
        self._name_kh = name_kh

    @property
    def name_en(self):
        """Gets the name_en of this CambodianIdCardResult.

        英文姓名。 

        :return: The name_en of this CambodianIdCardResult.
        :rtype: str
        """
        return self._name_en

    @name_en.setter
    def name_en(self, name_en):
        """Sets the name_en of this CambodianIdCardResult.

        英文姓名。 

        :param name_en: The name_en of this CambodianIdCardResult.
        :type name_en: str
        """
        self._name_en = name_en

    @property
    def birth_date(self):
        """Gets the birth_date of this CambodianIdCardResult.

        出生日期。 

        :return: The birth_date of this CambodianIdCardResult.
        :rtype: str
        """
        return self._birth_date

    @birth_date.setter
    def birth_date(self, birth_date):
        """Sets the birth_date of this CambodianIdCardResult.

        出生日期。 

        :param birth_date: The birth_date of this CambodianIdCardResult.
        :type birth_date: str
        """
        self._birth_date = birth_date

    @property
    def sex(self):
        """Gets the sex of this CambodianIdCardResult.

        性别。 

        :return: The sex of this CambodianIdCardResult.
        :rtype: str
        """
        return self._sex

    @sex.setter
    def sex(self, sex):
        """Sets the sex of this CambodianIdCardResult.

        性别。 

        :param sex: The sex of this CambodianIdCardResult.
        :type sex: str
        """
        self._sex = sex

    @property
    def height(self):
        """Gets the height of this CambodianIdCardResult.

        身高。 

        :return: The height of this CambodianIdCardResult.
        :rtype: str
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this CambodianIdCardResult.

        身高。 

        :param height: The height of this CambodianIdCardResult.
        :type height: str
        """
        self._height = height

    @property
    def birth_place(self):
        """Gets the birth_place of this CambodianIdCardResult.

        出生地。 

        :return: The birth_place of this CambodianIdCardResult.
        :rtype: str
        """
        return self._birth_place

    @birth_place.setter
    def birth_place(self, birth_place):
        """Sets the birth_place of this CambodianIdCardResult.

        出生地。 

        :param birth_place: The birth_place of this CambodianIdCardResult.
        :type birth_place: str
        """
        self._birth_place = birth_place

    @property
    def address(self):
        """Gets the address of this CambodianIdCardResult.

        地址，以空格分隔。 

        :return: The address of this CambodianIdCardResult.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this CambodianIdCardResult.

        地址，以空格分隔。 

        :param address: The address of this CambodianIdCardResult.
        :type address: str
        """
        self._address = address

    @property
    def issue_date(self):
        """Gets the issue_date of this CambodianIdCardResult.

        签发起始日期。 

        :return: The issue_date of this CambodianIdCardResult.
        :rtype: str
        """
        return self._issue_date

    @issue_date.setter
    def issue_date(self, issue_date):
        """Sets the issue_date of this CambodianIdCardResult.

        签发起始日期。 

        :param issue_date: The issue_date of this CambodianIdCardResult.
        :type issue_date: str
        """
        self._issue_date = issue_date

    @property
    def expiry_date(self):
        """Gets the expiry_date of this CambodianIdCardResult.

        签发结束日期。 

        :return: The expiry_date of this CambodianIdCardResult.
        :rtype: str
        """
        return self._expiry_date

    @expiry_date.setter
    def expiry_date(self, expiry_date):
        """Sets the expiry_date of this CambodianIdCardResult.

        签发结束日期。 

        :param expiry_date: The expiry_date of this CambodianIdCardResult.
        :type expiry_date: str
        """
        self._expiry_date = expiry_date

    @property
    def description(self):
        """Gets the description of this CambodianIdCardResult.

        图片中的个人特征。 

        :return: The description of this CambodianIdCardResult.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CambodianIdCardResult.

        图片中的个人特征。 

        :param description: The description of this CambodianIdCardResult.
        :type description: str
        """
        self._description = description

    @property
    def machine_code1(self):
        """Gets the machine_code1 of this CambodianIdCardResult.

        机器码第一行。 

        :return: The machine_code1 of this CambodianIdCardResult.
        :rtype: str
        """
        return self._machine_code1

    @machine_code1.setter
    def machine_code1(self, machine_code1):
        """Sets the machine_code1 of this CambodianIdCardResult.

        机器码第一行。 

        :param machine_code1: The machine_code1 of this CambodianIdCardResult.
        :type machine_code1: str
        """
        self._machine_code1 = machine_code1

    @property
    def machine_code2(self):
        """Gets the machine_code2 of this CambodianIdCardResult.

        机器码第二行。 

        :return: The machine_code2 of this CambodianIdCardResult.
        :rtype: str
        """
        return self._machine_code2

    @machine_code2.setter
    def machine_code2(self, machine_code2):
        """Sets the machine_code2 of this CambodianIdCardResult.

        机器码第二行。 

        :param machine_code2: The machine_code2 of this CambodianIdCardResult.
        :type machine_code2: str
        """
        self._machine_code2 = machine_code2

    @property
    def machine_code3(self):
        """Gets the machine_code3 of this CambodianIdCardResult.

        机器码第三行。 

        :return: The machine_code3 of this CambodianIdCardResult.
        :rtype: str
        """
        return self._machine_code3

    @machine_code3.setter
    def machine_code3(self, machine_code3):
        """Sets the machine_code3 of this CambodianIdCardResult.

        机器码第三行。 

        :param machine_code3: The machine_code3 of this CambodianIdCardResult.
        :type machine_code3: str
        """
        self._machine_code3 = machine_code3

    @property
    def portrait_image(self):
        """Gets the portrait_image of this CambodianIdCardResult.

        头像的base64编码。 当输入参数“return_portrait_image”为“true”时，才返回该参数。 

        :return: The portrait_image of this CambodianIdCardResult.
        :rtype: str
        """
        return self._portrait_image

    @portrait_image.setter
    def portrait_image(self, portrait_image):
        """Sets the portrait_image of this CambodianIdCardResult.

        头像的base64编码。 当输入参数“return_portrait_image”为“true”时，才返回该参数。 

        :param portrait_image: The portrait_image of this CambodianIdCardResult.
        :type portrait_image: str
        """
        self._portrait_image = portrait_image

    @property
    def portrait_location(self):
        """Gets the portrait_location of this CambodianIdCardResult.

        头像在原图上的位置。 当输入参数“return_portrait_location”为“true”时，才返回该参数。以列表形式显示，包含头像区域四个顶点的二维坐标（x,y），坐标原点为图片左上角，x轴沿水平方向，y轴沿竖直方向。 

        :return: The portrait_location of this CambodianIdCardResult.
        :rtype: list[list[int]]
        """
        return self._portrait_location

    @portrait_location.setter
    def portrait_location(self, portrait_location):
        """Sets the portrait_location of this CambodianIdCardResult.

        头像在原图上的位置。 当输入参数“return_portrait_location”为“true”时，才返回该参数。以列表形式显示，包含头像区域四个顶点的二维坐标（x,y），坐标原点为图片左上角，x轴沿水平方向，y轴沿竖直方向。 

        :param portrait_location: The portrait_location of this CambodianIdCardResult.
        :type portrait_location: list[list[int]]
        """
        self._portrait_location = portrait_location

    @property
    def idcard_type(self):
        """Gets the idcard_type of this CambodianIdCardResult.

        身份证的类型。当输入参数“ idcard_type ”为“true”时，才返回该参数。取值如下所示： - normal：身份证原件 - copy：复印的身份证 

        :return: The idcard_type of this CambodianIdCardResult.
        :rtype: str
        """
        return self._idcard_type

    @idcard_type.setter
    def idcard_type(self, idcard_type):
        """Sets the idcard_type of this CambodianIdCardResult.

        身份证的类型。当输入参数“ idcard_type ”为“true”时，才返回该参数。取值如下所示： - normal：身份证原件 - copy：复印的身份证 

        :param idcard_type: The idcard_type of this CambodianIdCardResult.
        :type idcard_type: str
        """
        self._idcard_type = idcard_type

    @property
    def confidence(self):
        """Gets the confidence of this CambodianIdCardResult.

        相关字段的置信度信息，置信度越大，表示本次识别的对应字段的可靠性越高，在统计意义上，置信度越大，准确率越高。 置信度由算法给出，不直接等价于对应字段的准确率。 

        :return: The confidence of this CambodianIdCardResult.
        :rtype: object
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        """Sets the confidence of this CambodianIdCardResult.

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
