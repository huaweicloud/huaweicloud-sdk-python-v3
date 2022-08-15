# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MainlandTravelPermitConfidence:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'name': 'float',
        'name_en': 'float',
        'birth_date': 'float',
        'sex': 'float',
        'valid_period': 'float',
        'issuing_authority': 'float',
        'number': 'float',
        'issue_place': 'float',
        'issue_times': 'float',
        'type': 'float',
        'side': 'float',
        'id_name': 'float',
        'id_number': 'float',
        'machine_code1': 'float',
        'machine_code2': 'float',
        'machine_code3': 'float'
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
        'type': 'type',
        'side': 'side',
        'id_name': 'id_name',
        'id_number': 'id_number',
        'machine_code1': 'machine_code1',
        'machine_code2': 'machine_code2',
        'machine_code3': 'machine_code3'
    }

    def __init__(self, name=None, name_en=None, birth_date=None, sex=None, valid_period=None, issuing_authority=None, number=None, issue_place=None, issue_times=None, type=None, side=None, id_name=None, id_number=None, machine_code1=None, machine_code2=None, machine_code3=None):
        """MainlandTravelPermitConfidence

        The model defined in huaweicloud sdk

        :param name: 中文姓名的置信度。 
        :type name: float
        :param name_en: 英文姓名的置信度。 
        :type name_en: float
        :param birth_date: 出生日期的置信度。 
        :type birth_date: float
        :param sex: 性别的置信度。 
        :type sex: float
        :param valid_period: 有效期限的置信度。 
        :type valid_period: float
        :param issuing_authority: 签发机关的置信度。 
        :type issuing_authority: float
        :param number: 证件号的置信度。 
        :type number: float
        :param issue_place: 签发地点的置信度。 
        :type issue_place: float
        :param issue_times: 签发次数的置信度。 
        :type issue_times: float
        :param type: 证件类别的置信度。 
        :type type: float
        :param side: 证件图片正反面信息的置信度。 
        :type side: float
        :param id_name: 回乡证背面的香港/澳门/台湾身份证姓名的置信度。 
        :type id_name: float
        :param id_number: 回乡证背面的香港/澳门/台湾身份证号码的置信度。 
        :type id_number: float
        :param machine_code1: 机读码第一行的置信度。 
        :type machine_code1: float
        :param machine_code2: 机读码第二行的置信度。 
        :type machine_code2: float
        :param machine_code3: 机读码第三行的置信度。 
        :type machine_code3: float
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
        self._type = None
        self._side = None
        self._id_name = None
        self._id_number = None
        self._machine_code1 = None
        self._machine_code2 = None
        self._machine_code3 = None
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
        if type is not None:
            self.type = type
        if side is not None:
            self.side = side
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

    @property
    def name(self):
        """Gets the name of this MainlandTravelPermitConfidence.

        中文姓名的置信度。 

        :return: The name of this MainlandTravelPermitConfidence.
        :rtype: float
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MainlandTravelPermitConfidence.

        中文姓名的置信度。 

        :param name: The name of this MainlandTravelPermitConfidence.
        :type name: float
        """
        self._name = name

    @property
    def name_en(self):
        """Gets the name_en of this MainlandTravelPermitConfidence.

        英文姓名的置信度。 

        :return: The name_en of this MainlandTravelPermitConfidence.
        :rtype: float
        """
        return self._name_en

    @name_en.setter
    def name_en(self, name_en):
        """Sets the name_en of this MainlandTravelPermitConfidence.

        英文姓名的置信度。 

        :param name_en: The name_en of this MainlandTravelPermitConfidence.
        :type name_en: float
        """
        self._name_en = name_en

    @property
    def birth_date(self):
        """Gets the birth_date of this MainlandTravelPermitConfidence.

        出生日期的置信度。 

        :return: The birth_date of this MainlandTravelPermitConfidence.
        :rtype: float
        """
        return self._birth_date

    @birth_date.setter
    def birth_date(self, birth_date):
        """Sets the birth_date of this MainlandTravelPermitConfidence.

        出生日期的置信度。 

        :param birth_date: The birth_date of this MainlandTravelPermitConfidence.
        :type birth_date: float
        """
        self._birth_date = birth_date

    @property
    def sex(self):
        """Gets the sex of this MainlandTravelPermitConfidence.

        性别的置信度。 

        :return: The sex of this MainlandTravelPermitConfidence.
        :rtype: float
        """
        return self._sex

    @sex.setter
    def sex(self, sex):
        """Sets the sex of this MainlandTravelPermitConfidence.

        性别的置信度。 

        :param sex: The sex of this MainlandTravelPermitConfidence.
        :type sex: float
        """
        self._sex = sex

    @property
    def valid_period(self):
        """Gets the valid_period of this MainlandTravelPermitConfidence.

        有效期限的置信度。 

        :return: The valid_period of this MainlandTravelPermitConfidence.
        :rtype: float
        """
        return self._valid_period

    @valid_period.setter
    def valid_period(self, valid_period):
        """Sets the valid_period of this MainlandTravelPermitConfidence.

        有效期限的置信度。 

        :param valid_period: The valid_period of this MainlandTravelPermitConfidence.
        :type valid_period: float
        """
        self._valid_period = valid_period

    @property
    def issuing_authority(self):
        """Gets the issuing_authority of this MainlandTravelPermitConfidence.

        签发机关的置信度。 

        :return: The issuing_authority of this MainlandTravelPermitConfidence.
        :rtype: float
        """
        return self._issuing_authority

    @issuing_authority.setter
    def issuing_authority(self, issuing_authority):
        """Sets the issuing_authority of this MainlandTravelPermitConfidence.

        签发机关的置信度。 

        :param issuing_authority: The issuing_authority of this MainlandTravelPermitConfidence.
        :type issuing_authority: float
        """
        self._issuing_authority = issuing_authority

    @property
    def number(self):
        """Gets the number of this MainlandTravelPermitConfidence.

        证件号的置信度。 

        :return: The number of this MainlandTravelPermitConfidence.
        :rtype: float
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this MainlandTravelPermitConfidence.

        证件号的置信度。 

        :param number: The number of this MainlandTravelPermitConfidence.
        :type number: float
        """
        self._number = number

    @property
    def issue_place(self):
        """Gets the issue_place of this MainlandTravelPermitConfidence.

        签发地点的置信度。 

        :return: The issue_place of this MainlandTravelPermitConfidence.
        :rtype: float
        """
        return self._issue_place

    @issue_place.setter
    def issue_place(self, issue_place):
        """Sets the issue_place of this MainlandTravelPermitConfidence.

        签发地点的置信度。 

        :param issue_place: The issue_place of this MainlandTravelPermitConfidence.
        :type issue_place: float
        """
        self._issue_place = issue_place

    @property
    def issue_times(self):
        """Gets the issue_times of this MainlandTravelPermitConfidence.

        签发次数的置信度。 

        :return: The issue_times of this MainlandTravelPermitConfidence.
        :rtype: float
        """
        return self._issue_times

    @issue_times.setter
    def issue_times(self, issue_times):
        """Sets the issue_times of this MainlandTravelPermitConfidence.

        签发次数的置信度。 

        :param issue_times: The issue_times of this MainlandTravelPermitConfidence.
        :type issue_times: float
        """
        self._issue_times = issue_times

    @property
    def type(self):
        """Gets the type of this MainlandTravelPermitConfidence.

        证件类别的置信度。 

        :return: The type of this MainlandTravelPermitConfidence.
        :rtype: float
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this MainlandTravelPermitConfidence.

        证件类别的置信度。 

        :param type: The type of this MainlandTravelPermitConfidence.
        :type type: float
        """
        self._type = type

    @property
    def side(self):
        """Gets the side of this MainlandTravelPermitConfidence.

        证件图片正反面信息的置信度。 

        :return: The side of this MainlandTravelPermitConfidence.
        :rtype: float
        """
        return self._side

    @side.setter
    def side(self, side):
        """Sets the side of this MainlandTravelPermitConfidence.

        证件图片正反面信息的置信度。 

        :param side: The side of this MainlandTravelPermitConfidence.
        :type side: float
        """
        self._side = side

    @property
    def id_name(self):
        """Gets the id_name of this MainlandTravelPermitConfidence.

        回乡证背面的香港/澳门/台湾身份证姓名的置信度。 

        :return: The id_name of this MainlandTravelPermitConfidence.
        :rtype: float
        """
        return self._id_name

    @id_name.setter
    def id_name(self, id_name):
        """Sets the id_name of this MainlandTravelPermitConfidence.

        回乡证背面的香港/澳门/台湾身份证姓名的置信度。 

        :param id_name: The id_name of this MainlandTravelPermitConfidence.
        :type id_name: float
        """
        self._id_name = id_name

    @property
    def id_number(self):
        """Gets the id_number of this MainlandTravelPermitConfidence.

        回乡证背面的香港/澳门/台湾身份证号码的置信度。 

        :return: The id_number of this MainlandTravelPermitConfidence.
        :rtype: float
        """
        return self._id_number

    @id_number.setter
    def id_number(self, id_number):
        """Sets the id_number of this MainlandTravelPermitConfidence.

        回乡证背面的香港/澳门/台湾身份证号码的置信度。 

        :param id_number: The id_number of this MainlandTravelPermitConfidence.
        :type id_number: float
        """
        self._id_number = id_number

    @property
    def machine_code1(self):
        """Gets the machine_code1 of this MainlandTravelPermitConfidence.

        机读码第一行的置信度。 

        :return: The machine_code1 of this MainlandTravelPermitConfidence.
        :rtype: float
        """
        return self._machine_code1

    @machine_code1.setter
    def machine_code1(self, machine_code1):
        """Sets the machine_code1 of this MainlandTravelPermitConfidence.

        机读码第一行的置信度。 

        :param machine_code1: The machine_code1 of this MainlandTravelPermitConfidence.
        :type machine_code1: float
        """
        self._machine_code1 = machine_code1

    @property
    def machine_code2(self):
        """Gets the machine_code2 of this MainlandTravelPermitConfidence.

        机读码第二行的置信度。 

        :return: The machine_code2 of this MainlandTravelPermitConfidence.
        :rtype: float
        """
        return self._machine_code2

    @machine_code2.setter
    def machine_code2(self, machine_code2):
        """Sets the machine_code2 of this MainlandTravelPermitConfidence.

        机读码第二行的置信度。 

        :param machine_code2: The machine_code2 of this MainlandTravelPermitConfidence.
        :type machine_code2: float
        """
        self._machine_code2 = machine_code2

    @property
    def machine_code3(self):
        """Gets the machine_code3 of this MainlandTravelPermitConfidence.

        机读码第三行的置信度。 

        :return: The machine_code3 of this MainlandTravelPermitConfidence.
        :rtype: float
        """
        return self._machine_code3

    @machine_code3.setter
    def machine_code3(self, machine_code3):
        """Sets the machine_code3 of this MainlandTravelPermitConfidence.

        机读码第三行的置信度。 

        :param machine_code3: The machine_code3 of this MainlandTravelPermitConfidence.
        :type machine_code3: float
        """
        self._machine_code3 = machine_code3

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
        if not isinstance(other, MainlandTravelPermitConfidence):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
