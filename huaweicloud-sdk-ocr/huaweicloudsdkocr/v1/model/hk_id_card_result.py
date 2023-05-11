# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HkIdCardResult:

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
        'symbols': 'str',
        'name_telegraph_code': 'str',
        'permanent': 'bool',
        'initial_issue_date': 'str',
        'issue_date': 'str',
        'portrait_location': 'list[list[int]]',
        'portrait_image': 'str',
        'confidence': 'object'
    }

    attribute_map = {
        'name': 'name',
        'name_en': 'name_en',
        'sex': 'sex',
        'birth_date': 'birth_date',
        'number': 'number',
        'symbols': 'symbols',
        'name_telegraph_code': 'name_telegraph_code',
        'permanent': 'permanent',
        'initial_issue_date': 'initial_issue_date',
        'issue_date': 'issue_date',
        'portrait_location': 'portrait_location',
        'portrait_image': 'portrait_image',
        'confidence': 'confidence'
    }

    def __init__(self, name=None, name_en=None, sex=None, birth_date=None, number=None, symbols=None, name_telegraph_code=None, permanent=None, initial_issue_date=None, issue_date=None, portrait_location=None, portrait_image=None, confidence=None):
        """HkIdCardResult

        The model defined in huaweicloud sdk

        :param name: 中文姓名。 
        :type name: str
        :param name_en: 英文姓名。 
        :type name_en: str
        :param sex: 性别。  男： value值为：M 女： value值为：F 
        :type sex: str
        :param birth_date: 出生日期。 
        :type birth_date: str
        :param number: 身份证号。 
        :type number: str
        :param symbols: 证件符号。 
        :type symbols: str
        :param name_telegraph_code: 中文姓名对应电码。 
        :type name_telegraph_code: str
        :param permanent: 是否永久性居民身份证。  永久：value值为true 非永久：value值为false 
        :type permanent: bool
        :param initial_issue_date: 首次领用日期。 
        :type initial_issue_date: str
        :param issue_date: 签发日期。 
        :type issue_date: str
        :param portrait_location: 头像在原图上的位置。 当输入参数“return_portrait_location”为“true”时，才返回该参数。以列表形式显示，包含头像区域四个顶点的二维坐标（x,y），坐标原点为图片左上角，x轴沿水平方向，y轴沿竖直方向。 
        :type portrait_location: list[list[int]]
        :param portrait_image: 头像的base64编码，默认返回尺寸较大的头像。 当输入参数“return_portrait_image”为true时，才返回该参数。 
        :type portrait_image: str
        :param confidence: 各个字段的置信度。 
        :type confidence: object
        """
        
        

        self._name = None
        self._name_en = None
        self._sex = None
        self._birth_date = None
        self._number = None
        self._symbols = None
        self._name_telegraph_code = None
        self._permanent = None
        self._initial_issue_date = None
        self._issue_date = None
        self._portrait_location = None
        self._portrait_image = None
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
        if symbols is not None:
            self.symbols = symbols
        if name_telegraph_code is not None:
            self.name_telegraph_code = name_telegraph_code
        if permanent is not None:
            self.permanent = permanent
        if initial_issue_date is not None:
            self.initial_issue_date = initial_issue_date
        if issue_date is not None:
            self.issue_date = issue_date
        if portrait_location is not None:
            self.portrait_location = portrait_location
        if portrait_image is not None:
            self.portrait_image = portrait_image
        if confidence is not None:
            self.confidence = confidence

    @property
    def name(self):
        """Gets the name of this HkIdCardResult.

        中文姓名。 

        :return: The name of this HkIdCardResult.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this HkIdCardResult.

        中文姓名。 

        :param name: The name of this HkIdCardResult.
        :type name: str
        """
        self._name = name

    @property
    def name_en(self):
        """Gets the name_en of this HkIdCardResult.

        英文姓名。 

        :return: The name_en of this HkIdCardResult.
        :rtype: str
        """
        return self._name_en

    @name_en.setter
    def name_en(self, name_en):
        """Sets the name_en of this HkIdCardResult.

        英文姓名。 

        :param name_en: The name_en of this HkIdCardResult.
        :type name_en: str
        """
        self._name_en = name_en

    @property
    def sex(self):
        """Gets the sex of this HkIdCardResult.

        性别。  男： value值为：M 女： value值为：F 

        :return: The sex of this HkIdCardResult.
        :rtype: str
        """
        return self._sex

    @sex.setter
    def sex(self, sex):
        """Sets the sex of this HkIdCardResult.

        性别。  男： value值为：M 女： value值为：F 

        :param sex: The sex of this HkIdCardResult.
        :type sex: str
        """
        self._sex = sex

    @property
    def birth_date(self):
        """Gets the birth_date of this HkIdCardResult.

        出生日期。 

        :return: The birth_date of this HkIdCardResult.
        :rtype: str
        """
        return self._birth_date

    @birth_date.setter
    def birth_date(self, birth_date):
        """Sets the birth_date of this HkIdCardResult.

        出生日期。 

        :param birth_date: The birth_date of this HkIdCardResult.
        :type birth_date: str
        """
        self._birth_date = birth_date

    @property
    def number(self):
        """Gets the number of this HkIdCardResult.

        身份证号。 

        :return: The number of this HkIdCardResult.
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this HkIdCardResult.

        身份证号。 

        :param number: The number of this HkIdCardResult.
        :type number: str
        """
        self._number = number

    @property
    def symbols(self):
        """Gets the symbols of this HkIdCardResult.

        证件符号。 

        :return: The symbols of this HkIdCardResult.
        :rtype: str
        """
        return self._symbols

    @symbols.setter
    def symbols(self, symbols):
        """Sets the symbols of this HkIdCardResult.

        证件符号。 

        :param symbols: The symbols of this HkIdCardResult.
        :type symbols: str
        """
        self._symbols = symbols

    @property
    def name_telegraph_code(self):
        """Gets the name_telegraph_code of this HkIdCardResult.

        中文姓名对应电码。 

        :return: The name_telegraph_code of this HkIdCardResult.
        :rtype: str
        """
        return self._name_telegraph_code

    @name_telegraph_code.setter
    def name_telegraph_code(self, name_telegraph_code):
        """Sets the name_telegraph_code of this HkIdCardResult.

        中文姓名对应电码。 

        :param name_telegraph_code: The name_telegraph_code of this HkIdCardResult.
        :type name_telegraph_code: str
        """
        self._name_telegraph_code = name_telegraph_code

    @property
    def permanent(self):
        """Gets the permanent of this HkIdCardResult.

        是否永久性居民身份证。  永久：value值为true 非永久：value值为false 

        :return: The permanent of this HkIdCardResult.
        :rtype: bool
        """
        return self._permanent

    @permanent.setter
    def permanent(self, permanent):
        """Sets the permanent of this HkIdCardResult.

        是否永久性居民身份证。  永久：value值为true 非永久：value值为false 

        :param permanent: The permanent of this HkIdCardResult.
        :type permanent: bool
        """
        self._permanent = permanent

    @property
    def initial_issue_date(self):
        """Gets the initial_issue_date of this HkIdCardResult.

        首次领用日期。 

        :return: The initial_issue_date of this HkIdCardResult.
        :rtype: str
        """
        return self._initial_issue_date

    @initial_issue_date.setter
    def initial_issue_date(self, initial_issue_date):
        """Sets the initial_issue_date of this HkIdCardResult.

        首次领用日期。 

        :param initial_issue_date: The initial_issue_date of this HkIdCardResult.
        :type initial_issue_date: str
        """
        self._initial_issue_date = initial_issue_date

    @property
    def issue_date(self):
        """Gets the issue_date of this HkIdCardResult.

        签发日期。 

        :return: The issue_date of this HkIdCardResult.
        :rtype: str
        """
        return self._issue_date

    @issue_date.setter
    def issue_date(self, issue_date):
        """Sets the issue_date of this HkIdCardResult.

        签发日期。 

        :param issue_date: The issue_date of this HkIdCardResult.
        :type issue_date: str
        """
        self._issue_date = issue_date

    @property
    def portrait_location(self):
        """Gets the portrait_location of this HkIdCardResult.

        头像在原图上的位置。 当输入参数“return_portrait_location”为“true”时，才返回该参数。以列表形式显示，包含头像区域四个顶点的二维坐标（x,y），坐标原点为图片左上角，x轴沿水平方向，y轴沿竖直方向。 

        :return: The portrait_location of this HkIdCardResult.
        :rtype: list[list[int]]
        """
        return self._portrait_location

    @portrait_location.setter
    def portrait_location(self, portrait_location):
        """Sets the portrait_location of this HkIdCardResult.

        头像在原图上的位置。 当输入参数“return_portrait_location”为“true”时，才返回该参数。以列表形式显示，包含头像区域四个顶点的二维坐标（x,y），坐标原点为图片左上角，x轴沿水平方向，y轴沿竖直方向。 

        :param portrait_location: The portrait_location of this HkIdCardResult.
        :type portrait_location: list[list[int]]
        """
        self._portrait_location = portrait_location

    @property
    def portrait_image(self):
        """Gets the portrait_image of this HkIdCardResult.

        头像的base64编码，默认返回尺寸较大的头像。 当输入参数“return_portrait_image”为true时，才返回该参数。 

        :return: The portrait_image of this HkIdCardResult.
        :rtype: str
        """
        return self._portrait_image

    @portrait_image.setter
    def portrait_image(self, portrait_image):
        """Sets the portrait_image of this HkIdCardResult.

        头像的base64编码，默认返回尺寸较大的头像。 当输入参数“return_portrait_image”为true时，才返回该参数。 

        :param portrait_image: The portrait_image of this HkIdCardResult.
        :type portrait_image: str
        """
        self._portrait_image = portrait_image

    @property
    def confidence(self):
        """Gets the confidence of this HkIdCardResult.

        各个字段的置信度。 

        :return: The confidence of this HkIdCardResult.
        :rtype: object
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        """Sets the confidence of this HkIdCardResult.

        各个字段的置信度。 

        :param confidence: The confidence of this HkIdCardResult.
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
        if not isinstance(other, HkIdCardResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
