# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ColombiaIdCardResult:

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
        'name': 'str',
        'last_name': 'str',
        'birth_date': 'str',
        'birth_place': 'str',
        'gender': 'str',
        'blood_type': 'str',
        'issue_date': 'str',
        'issue_authority': 'str',
        'height': 'str',
        'citizen_code1': 'str',
        'citizen_code2': 'str',
        'citizen_code3': 'str',
        'confidence': 'dict(str, float)'
    }

    attribute_map = {
        'side': 'side',
        'number': 'number',
        'name': 'name',
        'last_name': 'last_name',
        'birth_date': 'birth_date',
        'birth_place': 'birth_place',
        'gender': 'gender',
        'blood_type': 'blood_type',
        'issue_date': 'issue_date',
        'issue_authority': 'issue_authority',
        'height': 'height',
        'citizen_code1': 'citizen_code1',
        'citizen_code2': 'citizen_code2',
        'citizen_code3': 'citizen_code3',
        'confidence': 'confidence'
    }

    def __init__(self, side=None, number=None, name=None, last_name=None, birth_date=None, birth_place=None, gender=None, blood_type=None, issue_date=None, issue_authority=None, height=None, citizen_code1=None, citizen_code2=None, citizen_code3=None, confidence=None):
        """ColombiaIdCardResult

        The model defined in huaweicloud sdk

        :param side: 证件图片正反面信息。可选值包括： - front: 证件图片正面 - back:  证件图片反面
        :type side: str
        :param number: 卡证编号。当响应字段\&quot;side\&quot;为front时，返回此字段。
        :type number: str
        :param name: 名。当响应字段\&quot;side\&quot;为front时，返回此字段。
        :type name: str
        :param last_name: 姓。当响应字段\&quot;side\&quot;为front时，返回此字段。
        :type last_name: str
        :param birth_date: 出生日期。
        :type birth_date: str
        :param birth_place: 出生地。
        :type birth_place: str
        :param gender: 性别。
        :type gender: str
        :param blood_type: 血型。
        :type blood_type: str
        :param issue_date: 签发日期。
        :type issue_date: str
        :param issue_authority: 签发地区。
        :type issue_authority: str
        :param height: 身高。
        :type height: str
        :param citizen_code1: 公民编码一。
        :type citizen_code1: str
        :param citizen_code2: 公民编码二。
        :type citizen_code2: str
        :param citizen_code3: 公民编码三。
        :type citizen_code3: str
        :param confidence: 相关字段的置信度信息，置信度越大，表示本次识别的对应字段的可靠性越高，在统计意义上，置信度越大，准确率越高。注：置信度由算法给出，不直接等价于对应字段的准确率。
        :type confidence: dict(str, float)
        """
        
        

        self._side = None
        self._number = None
        self._name = None
        self._last_name = None
        self._birth_date = None
        self._birth_place = None
        self._gender = None
        self._blood_type = None
        self._issue_date = None
        self._issue_authority = None
        self._height = None
        self._citizen_code1 = None
        self._citizen_code2 = None
        self._citizen_code3 = None
        self._confidence = None
        self.discriminator = None

        if side is not None:
            self.side = side
        if number is not None:
            self.number = number
        if name is not None:
            self.name = name
        if last_name is not None:
            self.last_name = last_name
        if birth_date is not None:
            self.birth_date = birth_date
        if birth_place is not None:
            self.birth_place = birth_place
        if gender is not None:
            self.gender = gender
        if blood_type is not None:
            self.blood_type = blood_type
        if issue_date is not None:
            self.issue_date = issue_date
        if issue_authority is not None:
            self.issue_authority = issue_authority
        if height is not None:
            self.height = height
        if citizen_code1 is not None:
            self.citizen_code1 = citizen_code1
        if citizen_code2 is not None:
            self.citizen_code2 = citizen_code2
        if citizen_code3 is not None:
            self.citizen_code3 = citizen_code3
        if confidence is not None:
            self.confidence = confidence

    @property
    def side(self):
        """Gets the side of this ColombiaIdCardResult.

        证件图片正反面信息。可选值包括： - front: 证件图片正面 - back:  证件图片反面

        :return: The side of this ColombiaIdCardResult.
        :rtype: str
        """
        return self._side

    @side.setter
    def side(self, side):
        """Sets the side of this ColombiaIdCardResult.

        证件图片正反面信息。可选值包括： - front: 证件图片正面 - back:  证件图片反面

        :param side: The side of this ColombiaIdCardResult.
        :type side: str
        """
        self._side = side

    @property
    def number(self):
        """Gets the number of this ColombiaIdCardResult.

        卡证编号。当响应字段\"side\"为front时，返回此字段。

        :return: The number of this ColombiaIdCardResult.
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this ColombiaIdCardResult.

        卡证编号。当响应字段\"side\"为front时，返回此字段。

        :param number: The number of this ColombiaIdCardResult.
        :type number: str
        """
        self._number = number

    @property
    def name(self):
        """Gets the name of this ColombiaIdCardResult.

        名。当响应字段\"side\"为front时，返回此字段。

        :return: The name of this ColombiaIdCardResult.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ColombiaIdCardResult.

        名。当响应字段\"side\"为front时，返回此字段。

        :param name: The name of this ColombiaIdCardResult.
        :type name: str
        """
        self._name = name

    @property
    def last_name(self):
        """Gets the last_name of this ColombiaIdCardResult.

        姓。当响应字段\"side\"为front时，返回此字段。

        :return: The last_name of this ColombiaIdCardResult.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this ColombiaIdCardResult.

        姓。当响应字段\"side\"为front时，返回此字段。

        :param last_name: The last_name of this ColombiaIdCardResult.
        :type last_name: str
        """
        self._last_name = last_name

    @property
    def birth_date(self):
        """Gets the birth_date of this ColombiaIdCardResult.

        出生日期。

        :return: The birth_date of this ColombiaIdCardResult.
        :rtype: str
        """
        return self._birth_date

    @birth_date.setter
    def birth_date(self, birth_date):
        """Sets the birth_date of this ColombiaIdCardResult.

        出生日期。

        :param birth_date: The birth_date of this ColombiaIdCardResult.
        :type birth_date: str
        """
        self._birth_date = birth_date

    @property
    def birth_place(self):
        """Gets the birth_place of this ColombiaIdCardResult.

        出生地。

        :return: The birth_place of this ColombiaIdCardResult.
        :rtype: str
        """
        return self._birth_place

    @birth_place.setter
    def birth_place(self, birth_place):
        """Sets the birth_place of this ColombiaIdCardResult.

        出生地。

        :param birth_place: The birth_place of this ColombiaIdCardResult.
        :type birth_place: str
        """
        self._birth_place = birth_place

    @property
    def gender(self):
        """Gets the gender of this ColombiaIdCardResult.

        性别。

        :return: The gender of this ColombiaIdCardResult.
        :rtype: str
        """
        return self._gender

    @gender.setter
    def gender(self, gender):
        """Sets the gender of this ColombiaIdCardResult.

        性别。

        :param gender: The gender of this ColombiaIdCardResult.
        :type gender: str
        """
        self._gender = gender

    @property
    def blood_type(self):
        """Gets the blood_type of this ColombiaIdCardResult.

        血型。

        :return: The blood_type of this ColombiaIdCardResult.
        :rtype: str
        """
        return self._blood_type

    @blood_type.setter
    def blood_type(self, blood_type):
        """Sets the blood_type of this ColombiaIdCardResult.

        血型。

        :param blood_type: The blood_type of this ColombiaIdCardResult.
        :type blood_type: str
        """
        self._blood_type = blood_type

    @property
    def issue_date(self):
        """Gets the issue_date of this ColombiaIdCardResult.

        签发日期。

        :return: The issue_date of this ColombiaIdCardResult.
        :rtype: str
        """
        return self._issue_date

    @issue_date.setter
    def issue_date(self, issue_date):
        """Sets the issue_date of this ColombiaIdCardResult.

        签发日期。

        :param issue_date: The issue_date of this ColombiaIdCardResult.
        :type issue_date: str
        """
        self._issue_date = issue_date

    @property
    def issue_authority(self):
        """Gets the issue_authority of this ColombiaIdCardResult.

        签发地区。

        :return: The issue_authority of this ColombiaIdCardResult.
        :rtype: str
        """
        return self._issue_authority

    @issue_authority.setter
    def issue_authority(self, issue_authority):
        """Sets the issue_authority of this ColombiaIdCardResult.

        签发地区。

        :param issue_authority: The issue_authority of this ColombiaIdCardResult.
        :type issue_authority: str
        """
        self._issue_authority = issue_authority

    @property
    def height(self):
        """Gets the height of this ColombiaIdCardResult.

        身高。

        :return: The height of this ColombiaIdCardResult.
        :rtype: str
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this ColombiaIdCardResult.

        身高。

        :param height: The height of this ColombiaIdCardResult.
        :type height: str
        """
        self._height = height

    @property
    def citizen_code1(self):
        """Gets the citizen_code1 of this ColombiaIdCardResult.

        公民编码一。

        :return: The citizen_code1 of this ColombiaIdCardResult.
        :rtype: str
        """
        return self._citizen_code1

    @citizen_code1.setter
    def citizen_code1(self, citizen_code1):
        """Sets the citizen_code1 of this ColombiaIdCardResult.

        公民编码一。

        :param citizen_code1: The citizen_code1 of this ColombiaIdCardResult.
        :type citizen_code1: str
        """
        self._citizen_code1 = citizen_code1

    @property
    def citizen_code2(self):
        """Gets the citizen_code2 of this ColombiaIdCardResult.

        公民编码二。

        :return: The citizen_code2 of this ColombiaIdCardResult.
        :rtype: str
        """
        return self._citizen_code2

    @citizen_code2.setter
    def citizen_code2(self, citizen_code2):
        """Sets the citizen_code2 of this ColombiaIdCardResult.

        公民编码二。

        :param citizen_code2: The citizen_code2 of this ColombiaIdCardResult.
        :type citizen_code2: str
        """
        self._citizen_code2 = citizen_code2

    @property
    def citizen_code3(self):
        """Gets the citizen_code3 of this ColombiaIdCardResult.

        公民编码三。

        :return: The citizen_code3 of this ColombiaIdCardResult.
        :rtype: str
        """
        return self._citizen_code3

    @citizen_code3.setter
    def citizen_code3(self, citizen_code3):
        """Sets the citizen_code3 of this ColombiaIdCardResult.

        公民编码三。

        :param citizen_code3: The citizen_code3 of this ColombiaIdCardResult.
        :type citizen_code3: str
        """
        self._citizen_code3 = citizen_code3

    @property
    def confidence(self):
        """Gets the confidence of this ColombiaIdCardResult.

        相关字段的置信度信息，置信度越大，表示本次识别的对应字段的可靠性越高，在统计意义上，置信度越大，准确率越高。注：置信度由算法给出，不直接等价于对应字段的准确率。

        :return: The confidence of this ColombiaIdCardResult.
        :rtype: dict(str, float)
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        """Sets the confidence of this ColombiaIdCardResult.

        相关字段的置信度信息，置信度越大，表示本次识别的对应字段的可靠性越高，在统计意义上，置信度越大，准确率越高。注：置信度由算法给出，不直接等价于对应字段的准确率。

        :param confidence: The confidence of this ColombiaIdCardResult.
        :type confidence: dict(str, float)
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
        if not isinstance(other, ColombiaIdCardResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
