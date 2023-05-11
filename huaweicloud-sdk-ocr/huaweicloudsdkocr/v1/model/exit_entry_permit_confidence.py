# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExitEntryPermitConfidence:

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
        'number': 'float',
        'valid_period': 'float',
        'issuing_authority': 'float',
        'issue_place': 'float',
        'machine_code': 'float',
        'type': 'float',
        'side': 'float',
        'endorsement_info_hk': 'object',
        'endorsement_info_mo': 'object',
        'endorsement_info_tw': 'object'
    }

    attribute_map = {
        'name': 'name',
        'name_en': 'name_en',
        'birth_date': 'birth_date',
        'sex': 'sex',
        'number': 'number',
        'valid_period': 'valid_period',
        'issuing_authority': 'issuing_authority',
        'issue_place': 'issue_place',
        'machine_code': 'machine_code',
        'type': 'type',
        'side': 'side',
        'endorsement_info_hk': 'endorsement_info_hk',
        'endorsement_info_mo': 'endorsement_info_mo',
        'endorsement_info_tw': 'endorsement_info_tw'
    }

    def __init__(self, name=None, name_en=None, birth_date=None, sex=None, number=None, valid_period=None, issuing_authority=None, issue_place=None, machine_code=None, type=None, side=None, endorsement_info_hk=None, endorsement_info_mo=None, endorsement_info_tw=None):
        """ExitEntryPermitConfidence

        The model defined in huaweicloud sdk

        :param name: 姓名的置信度。 
        :type name: float
        :param name_en: 英文姓名的置信度。 
        :type name_en: float
        :param birth_date: 出生日期的置信度。 
        :type birth_date: float
        :param sex: 性别的置信度 
        :type sex: float
        :param number: 证件号的置信度。 
        :type number: float
        :param valid_period: 有效期限的置信度。 
        :type valid_period: float
        :param issuing_authority: 签发机关的置信度。 
        :type issuing_authority: float
        :param issue_place: 签发地点的置信度。 
        :type issue_place: float
        :param machine_code: 机器码的置信度。 
        :type machine_code: float
        :param type: 证件类型的置信度。 
        :type type: float
        :param side: 证件图片正反面信息的置信度。 
        :type side: float
        :param endorsement_info_hk: 香港签注信息的置信度。 
        :type endorsement_info_hk: object
        :param endorsement_info_mo: 澳门签注信息的置信度。 
        :type endorsement_info_mo: object
        :param endorsement_info_tw: 台湾签注信息的置信度。 
        :type endorsement_info_tw: object
        """
        
        

        self._name = None
        self._name_en = None
        self._birth_date = None
        self._sex = None
        self._number = None
        self._valid_period = None
        self._issuing_authority = None
        self._issue_place = None
        self._machine_code = None
        self._type = None
        self._side = None
        self._endorsement_info_hk = None
        self._endorsement_info_mo = None
        self._endorsement_info_tw = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if name_en is not None:
            self.name_en = name_en
        if birth_date is not None:
            self.birth_date = birth_date
        if sex is not None:
            self.sex = sex
        if number is not None:
            self.number = number
        if valid_period is not None:
            self.valid_period = valid_period
        if issuing_authority is not None:
            self.issuing_authority = issuing_authority
        if issue_place is not None:
            self.issue_place = issue_place
        if machine_code is not None:
            self.machine_code = machine_code
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

    @property
    def name(self):
        """Gets the name of this ExitEntryPermitConfidence.

        姓名的置信度。 

        :return: The name of this ExitEntryPermitConfidence.
        :rtype: float
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ExitEntryPermitConfidence.

        姓名的置信度。 

        :param name: The name of this ExitEntryPermitConfidence.
        :type name: float
        """
        self._name = name

    @property
    def name_en(self):
        """Gets the name_en of this ExitEntryPermitConfidence.

        英文姓名的置信度。 

        :return: The name_en of this ExitEntryPermitConfidence.
        :rtype: float
        """
        return self._name_en

    @name_en.setter
    def name_en(self, name_en):
        """Sets the name_en of this ExitEntryPermitConfidence.

        英文姓名的置信度。 

        :param name_en: The name_en of this ExitEntryPermitConfidence.
        :type name_en: float
        """
        self._name_en = name_en

    @property
    def birth_date(self):
        """Gets the birth_date of this ExitEntryPermitConfidence.

        出生日期的置信度。 

        :return: The birth_date of this ExitEntryPermitConfidence.
        :rtype: float
        """
        return self._birth_date

    @birth_date.setter
    def birth_date(self, birth_date):
        """Sets the birth_date of this ExitEntryPermitConfidence.

        出生日期的置信度。 

        :param birth_date: The birth_date of this ExitEntryPermitConfidence.
        :type birth_date: float
        """
        self._birth_date = birth_date

    @property
    def sex(self):
        """Gets the sex of this ExitEntryPermitConfidence.

        性别的置信度 

        :return: The sex of this ExitEntryPermitConfidence.
        :rtype: float
        """
        return self._sex

    @sex.setter
    def sex(self, sex):
        """Sets the sex of this ExitEntryPermitConfidence.

        性别的置信度 

        :param sex: The sex of this ExitEntryPermitConfidence.
        :type sex: float
        """
        self._sex = sex

    @property
    def number(self):
        """Gets the number of this ExitEntryPermitConfidence.

        证件号的置信度。 

        :return: The number of this ExitEntryPermitConfidence.
        :rtype: float
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this ExitEntryPermitConfidence.

        证件号的置信度。 

        :param number: The number of this ExitEntryPermitConfidence.
        :type number: float
        """
        self._number = number

    @property
    def valid_period(self):
        """Gets the valid_period of this ExitEntryPermitConfidence.

        有效期限的置信度。 

        :return: The valid_period of this ExitEntryPermitConfidence.
        :rtype: float
        """
        return self._valid_period

    @valid_period.setter
    def valid_period(self, valid_period):
        """Sets the valid_period of this ExitEntryPermitConfidence.

        有效期限的置信度。 

        :param valid_period: The valid_period of this ExitEntryPermitConfidence.
        :type valid_period: float
        """
        self._valid_period = valid_period

    @property
    def issuing_authority(self):
        """Gets the issuing_authority of this ExitEntryPermitConfidence.

        签发机关的置信度。 

        :return: The issuing_authority of this ExitEntryPermitConfidence.
        :rtype: float
        """
        return self._issuing_authority

    @issuing_authority.setter
    def issuing_authority(self, issuing_authority):
        """Sets the issuing_authority of this ExitEntryPermitConfidence.

        签发机关的置信度。 

        :param issuing_authority: The issuing_authority of this ExitEntryPermitConfidence.
        :type issuing_authority: float
        """
        self._issuing_authority = issuing_authority

    @property
    def issue_place(self):
        """Gets the issue_place of this ExitEntryPermitConfidence.

        签发地点的置信度。 

        :return: The issue_place of this ExitEntryPermitConfidence.
        :rtype: float
        """
        return self._issue_place

    @issue_place.setter
    def issue_place(self, issue_place):
        """Sets the issue_place of this ExitEntryPermitConfidence.

        签发地点的置信度。 

        :param issue_place: The issue_place of this ExitEntryPermitConfidence.
        :type issue_place: float
        """
        self._issue_place = issue_place

    @property
    def machine_code(self):
        """Gets the machine_code of this ExitEntryPermitConfidence.

        机器码的置信度。 

        :return: The machine_code of this ExitEntryPermitConfidence.
        :rtype: float
        """
        return self._machine_code

    @machine_code.setter
    def machine_code(self, machine_code):
        """Sets the machine_code of this ExitEntryPermitConfidence.

        机器码的置信度。 

        :param machine_code: The machine_code of this ExitEntryPermitConfidence.
        :type machine_code: float
        """
        self._machine_code = machine_code

    @property
    def type(self):
        """Gets the type of this ExitEntryPermitConfidence.

        证件类型的置信度。 

        :return: The type of this ExitEntryPermitConfidence.
        :rtype: float
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ExitEntryPermitConfidence.

        证件类型的置信度。 

        :param type: The type of this ExitEntryPermitConfidence.
        :type type: float
        """
        self._type = type

    @property
    def side(self):
        """Gets the side of this ExitEntryPermitConfidence.

        证件图片正反面信息的置信度。 

        :return: The side of this ExitEntryPermitConfidence.
        :rtype: float
        """
        return self._side

    @side.setter
    def side(self, side):
        """Sets the side of this ExitEntryPermitConfidence.

        证件图片正反面信息的置信度。 

        :param side: The side of this ExitEntryPermitConfidence.
        :type side: float
        """
        self._side = side

    @property
    def endorsement_info_hk(self):
        """Gets the endorsement_info_hk of this ExitEntryPermitConfidence.

        香港签注信息的置信度。 

        :return: The endorsement_info_hk of this ExitEntryPermitConfidence.
        :rtype: object
        """
        return self._endorsement_info_hk

    @endorsement_info_hk.setter
    def endorsement_info_hk(self, endorsement_info_hk):
        """Sets the endorsement_info_hk of this ExitEntryPermitConfidence.

        香港签注信息的置信度。 

        :param endorsement_info_hk: The endorsement_info_hk of this ExitEntryPermitConfidence.
        :type endorsement_info_hk: object
        """
        self._endorsement_info_hk = endorsement_info_hk

    @property
    def endorsement_info_mo(self):
        """Gets the endorsement_info_mo of this ExitEntryPermitConfidence.

        澳门签注信息的置信度。 

        :return: The endorsement_info_mo of this ExitEntryPermitConfidence.
        :rtype: object
        """
        return self._endorsement_info_mo

    @endorsement_info_mo.setter
    def endorsement_info_mo(self, endorsement_info_mo):
        """Sets the endorsement_info_mo of this ExitEntryPermitConfidence.

        澳门签注信息的置信度。 

        :param endorsement_info_mo: The endorsement_info_mo of this ExitEntryPermitConfidence.
        :type endorsement_info_mo: object
        """
        self._endorsement_info_mo = endorsement_info_mo

    @property
    def endorsement_info_tw(self):
        """Gets the endorsement_info_tw of this ExitEntryPermitConfidence.

        台湾签注信息的置信度。 

        :return: The endorsement_info_tw of this ExitEntryPermitConfidence.
        :rtype: object
        """
        return self._endorsement_info_tw

    @endorsement_info_tw.setter
    def endorsement_info_tw(self, endorsement_info_tw):
        """Sets the endorsement_info_tw of this ExitEntryPermitConfidence.

        台湾签注信息的置信度。 

        :param endorsement_info_tw: The endorsement_info_tw of this ExitEntryPermitConfidence.
        :type endorsement_info_tw: object
        """
        self._endorsement_info_tw = endorsement_info_tw

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
        if not isinstance(other, ExitEntryPermitConfidence):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
