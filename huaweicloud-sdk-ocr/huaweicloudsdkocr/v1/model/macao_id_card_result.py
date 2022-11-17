# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MacaoIdCardResult:

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
        'name': 'str',
        'name_en': 'str',
        'sex': 'str',
        'issue_date': 'str',
        'expiry_date': 'str',
        'birth_date': 'str',
        'initial_issue_date': 'str',
        'height': 'str',
        'number': 'str',
        'symbols': 'str',
        'machine_code1': 'str',
        'machine_code2': 'str',
        'machine_code3': 'str',
        'portrait_image': 'str',
        'confidence': 'object'
    }

    attribute_map = {
        'side': 'side',
        'name': 'name',
        'name_en': 'name_en',
        'sex': 'sex',
        'issue_date': 'issue_date',
        'expiry_date': 'expiry_date',
        'birth_date': 'birth_date',
        'initial_issue_date': 'initial_issue_date',
        'height': 'height',
        'number': 'number',
        'symbols': 'symbols',
        'machine_code1': 'machine_code1',
        'machine_code2': 'machine_code2',
        'machine_code3': 'machine_code3',
        'portrait_image': 'portrait_image',
        'confidence': 'confidence'
    }

    def __init__(self, side=None, name=None, name_en=None, sex=None, issue_date=None, expiry_date=None, birth_date=None, initial_issue_date=None, height=None, number=None, symbols=None, machine_code1=None, machine_code2=None, machine_code3=None, portrait_image=None, confidence=None):
        """MacaoIdCardResult

        The model defined in huaweicloud sdk

        :param side: 证件图片正反面信息。可选值包括： - \&quot;front\&quot;: 证件图片为正面 - \&quot;back\&quot;: 证件图片为反面 
        :type side: str
        :param name: 姓名。 
        :type name: str
        :param name_en: 英文姓名，姓名单词之间使用空格进行间隔。 
        :type name_en: str
        :param sex: 性别，返回“男”或“女”。 
        :type sex: str
        :param issue_date: 本次发证日期。 
        :type issue_date: str
        :param expiry_date: 证件有效期。 
        :type expiry_date: str
        :param birth_date: 出生日期。 
        :type birth_date: str
        :param initial_issue_date: 首次发证日期。 
        :type initial_issue_date: str
        :param height: 身高。 
        :type height: str
        :param number: 身份证号。 
        :type number: str
        :param symbols: 身份证上的字母代码，表示出生地等信息。 
        :type symbols: str
        :param machine_code1: 身份证背面第一行机器码。 
        :type machine_code1: str
        :param machine_code2: 身份证背面第二行机器码。 
        :type machine_code2: str
        :param machine_code3: 身份证背面第三行机器码。 
        :type machine_code3: str
        :param portrait_image: 身份证头像照片的Base64编码。 若入参“return_portrait_image”字段缺失时，则此字段不存在。 
        :type portrait_image: str
        :param confidence: 相关字段的置信度信息，置信度越大，表示本次识别的对应字段的可靠性越高，在统计意义上，置信度越大，准确率越高。注：置信度由算法给出，不直接等价于对应字段的准确率。 
        :type confidence: object
        """
        
        

        self._side = None
        self._name = None
        self._name_en = None
        self._sex = None
        self._issue_date = None
        self._expiry_date = None
        self._birth_date = None
        self._initial_issue_date = None
        self._height = None
        self._number = None
        self._symbols = None
        self._machine_code1 = None
        self._machine_code2 = None
        self._machine_code3 = None
        self._portrait_image = None
        self._confidence = None
        self.discriminator = None

        if side is not None:
            self.side = side
        if name is not None:
            self.name = name
        if name_en is not None:
            self.name_en = name_en
        if sex is not None:
            self.sex = sex
        if issue_date is not None:
            self.issue_date = issue_date
        if expiry_date is not None:
            self.expiry_date = expiry_date
        if birth_date is not None:
            self.birth_date = birth_date
        if initial_issue_date is not None:
            self.initial_issue_date = initial_issue_date
        if height is not None:
            self.height = height
        if number is not None:
            self.number = number
        if symbols is not None:
            self.symbols = symbols
        if machine_code1 is not None:
            self.machine_code1 = machine_code1
        if machine_code2 is not None:
            self.machine_code2 = machine_code2
        if machine_code3 is not None:
            self.machine_code3 = machine_code3
        if portrait_image is not None:
            self.portrait_image = portrait_image
        if confidence is not None:
            self.confidence = confidence

    @property
    def side(self):
        """Gets the side of this MacaoIdCardResult.

        证件图片正反面信息。可选值包括： - \"front\": 证件图片为正面 - \"back\": 证件图片为反面 

        :return: The side of this MacaoIdCardResult.
        :rtype: str
        """
        return self._side

    @side.setter
    def side(self, side):
        """Sets the side of this MacaoIdCardResult.

        证件图片正反面信息。可选值包括： - \"front\": 证件图片为正面 - \"back\": 证件图片为反面 

        :param side: The side of this MacaoIdCardResult.
        :type side: str
        """
        self._side = side

    @property
    def name(self):
        """Gets the name of this MacaoIdCardResult.

        姓名。 

        :return: The name of this MacaoIdCardResult.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MacaoIdCardResult.

        姓名。 

        :param name: The name of this MacaoIdCardResult.
        :type name: str
        """
        self._name = name

    @property
    def name_en(self):
        """Gets the name_en of this MacaoIdCardResult.

        英文姓名，姓名单词之间使用空格进行间隔。 

        :return: The name_en of this MacaoIdCardResult.
        :rtype: str
        """
        return self._name_en

    @name_en.setter
    def name_en(self, name_en):
        """Sets the name_en of this MacaoIdCardResult.

        英文姓名，姓名单词之间使用空格进行间隔。 

        :param name_en: The name_en of this MacaoIdCardResult.
        :type name_en: str
        """
        self._name_en = name_en

    @property
    def sex(self):
        """Gets the sex of this MacaoIdCardResult.

        性别，返回“男”或“女”。 

        :return: The sex of this MacaoIdCardResult.
        :rtype: str
        """
        return self._sex

    @sex.setter
    def sex(self, sex):
        """Sets the sex of this MacaoIdCardResult.

        性别，返回“男”或“女”。 

        :param sex: The sex of this MacaoIdCardResult.
        :type sex: str
        """
        self._sex = sex

    @property
    def issue_date(self):
        """Gets the issue_date of this MacaoIdCardResult.

        本次发证日期。 

        :return: The issue_date of this MacaoIdCardResult.
        :rtype: str
        """
        return self._issue_date

    @issue_date.setter
    def issue_date(self, issue_date):
        """Sets the issue_date of this MacaoIdCardResult.

        本次发证日期。 

        :param issue_date: The issue_date of this MacaoIdCardResult.
        :type issue_date: str
        """
        self._issue_date = issue_date

    @property
    def expiry_date(self):
        """Gets the expiry_date of this MacaoIdCardResult.

        证件有效期。 

        :return: The expiry_date of this MacaoIdCardResult.
        :rtype: str
        """
        return self._expiry_date

    @expiry_date.setter
    def expiry_date(self, expiry_date):
        """Sets the expiry_date of this MacaoIdCardResult.

        证件有效期。 

        :param expiry_date: The expiry_date of this MacaoIdCardResult.
        :type expiry_date: str
        """
        self._expiry_date = expiry_date

    @property
    def birth_date(self):
        """Gets the birth_date of this MacaoIdCardResult.

        出生日期。 

        :return: The birth_date of this MacaoIdCardResult.
        :rtype: str
        """
        return self._birth_date

    @birth_date.setter
    def birth_date(self, birth_date):
        """Sets the birth_date of this MacaoIdCardResult.

        出生日期。 

        :param birth_date: The birth_date of this MacaoIdCardResult.
        :type birth_date: str
        """
        self._birth_date = birth_date

    @property
    def initial_issue_date(self):
        """Gets the initial_issue_date of this MacaoIdCardResult.

        首次发证日期。 

        :return: The initial_issue_date of this MacaoIdCardResult.
        :rtype: str
        """
        return self._initial_issue_date

    @initial_issue_date.setter
    def initial_issue_date(self, initial_issue_date):
        """Sets the initial_issue_date of this MacaoIdCardResult.

        首次发证日期。 

        :param initial_issue_date: The initial_issue_date of this MacaoIdCardResult.
        :type initial_issue_date: str
        """
        self._initial_issue_date = initial_issue_date

    @property
    def height(self):
        """Gets the height of this MacaoIdCardResult.

        身高。 

        :return: The height of this MacaoIdCardResult.
        :rtype: str
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this MacaoIdCardResult.

        身高。 

        :param height: The height of this MacaoIdCardResult.
        :type height: str
        """
        self._height = height

    @property
    def number(self):
        """Gets the number of this MacaoIdCardResult.

        身份证号。 

        :return: The number of this MacaoIdCardResult.
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this MacaoIdCardResult.

        身份证号。 

        :param number: The number of this MacaoIdCardResult.
        :type number: str
        """
        self._number = number

    @property
    def symbols(self):
        """Gets the symbols of this MacaoIdCardResult.

        身份证上的字母代码，表示出生地等信息。 

        :return: The symbols of this MacaoIdCardResult.
        :rtype: str
        """
        return self._symbols

    @symbols.setter
    def symbols(self, symbols):
        """Sets the symbols of this MacaoIdCardResult.

        身份证上的字母代码，表示出生地等信息。 

        :param symbols: The symbols of this MacaoIdCardResult.
        :type symbols: str
        """
        self._symbols = symbols

    @property
    def machine_code1(self):
        """Gets the machine_code1 of this MacaoIdCardResult.

        身份证背面第一行机器码。 

        :return: The machine_code1 of this MacaoIdCardResult.
        :rtype: str
        """
        return self._machine_code1

    @machine_code1.setter
    def machine_code1(self, machine_code1):
        """Sets the machine_code1 of this MacaoIdCardResult.

        身份证背面第一行机器码。 

        :param machine_code1: The machine_code1 of this MacaoIdCardResult.
        :type machine_code1: str
        """
        self._machine_code1 = machine_code1

    @property
    def machine_code2(self):
        """Gets the machine_code2 of this MacaoIdCardResult.

        身份证背面第二行机器码。 

        :return: The machine_code2 of this MacaoIdCardResult.
        :rtype: str
        """
        return self._machine_code2

    @machine_code2.setter
    def machine_code2(self, machine_code2):
        """Sets the machine_code2 of this MacaoIdCardResult.

        身份证背面第二行机器码。 

        :param machine_code2: The machine_code2 of this MacaoIdCardResult.
        :type machine_code2: str
        """
        self._machine_code2 = machine_code2

    @property
    def machine_code3(self):
        """Gets the machine_code3 of this MacaoIdCardResult.

        身份证背面第三行机器码。 

        :return: The machine_code3 of this MacaoIdCardResult.
        :rtype: str
        """
        return self._machine_code3

    @machine_code3.setter
    def machine_code3(self, machine_code3):
        """Sets the machine_code3 of this MacaoIdCardResult.

        身份证背面第三行机器码。 

        :param machine_code3: The machine_code3 of this MacaoIdCardResult.
        :type machine_code3: str
        """
        self._machine_code3 = machine_code3

    @property
    def portrait_image(self):
        """Gets the portrait_image of this MacaoIdCardResult.

        身份证头像照片的Base64编码。 若入参“return_portrait_image”字段缺失时，则此字段不存在。 

        :return: The portrait_image of this MacaoIdCardResult.
        :rtype: str
        """
        return self._portrait_image

    @portrait_image.setter
    def portrait_image(self, portrait_image):
        """Sets the portrait_image of this MacaoIdCardResult.

        身份证头像照片的Base64编码。 若入参“return_portrait_image”字段缺失时，则此字段不存在。 

        :param portrait_image: The portrait_image of this MacaoIdCardResult.
        :type portrait_image: str
        """
        self._portrait_image = portrait_image

    @property
    def confidence(self):
        """Gets the confidence of this MacaoIdCardResult.

        相关字段的置信度信息，置信度越大，表示本次识别的对应字段的可靠性越高，在统计意义上，置信度越大，准确率越高。注：置信度由算法给出，不直接等价于对应字段的准确率。 

        :return: The confidence of this MacaoIdCardResult.
        :rtype: object
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        """Sets the confidence of this MacaoIdCardResult.

        相关字段的置信度信息，置信度越大，表示本次识别的对应字段的可靠性越高，在统计意义上，置信度越大，准确率越高。注：置信度由算法给出，不直接等价于对应字段的准确率。 

        :param confidence: The confidence of this MacaoIdCardResult.
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
        if not isinstance(other, MacaoIdCardResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
