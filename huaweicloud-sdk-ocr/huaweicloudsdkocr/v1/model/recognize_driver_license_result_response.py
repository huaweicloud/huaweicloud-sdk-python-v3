# coding: utf-8

import pprint
import re

import six





class RecognizeDriverLicenseResultResponse:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'number': 'str',
        'name': 'str',
        'sex': 'str',
        'nationality': 'str',
        'address': 'str',
        'birth': 'str',
        'issue_date': 'str',
        '_class': 'str',
        'valid_from': 'str',
        'valid_to': 'str',
        'issuing_authority': 'str',
        'file_number': 'str',
        'record': 'str'
    }

    attribute_map = {
        'number': 'number',
        'name': 'name',
        'sex': 'sex',
        'nationality': 'nationality',
        'address': 'address',
        'birth': 'birth',
        'issue_date': 'issue_date',
        '_class': 'class',
        'valid_from': 'valid_from',
        'valid_to': 'valid_to',
        'issuing_authority': 'issuing_authority',
        'file_number': 'file_number',
        'record': 'record'
    }

    def __init__(self, number=None, name=None, sex=None, nationality=None, address=None, birth=None, issue_date=None, _class=None, valid_from=None, valid_to=None, issuing_authority=None, file_number=None, record=None):
        """RecognizeDriverLicenseResultResponse - a model defined in huaweicloud sdk"""
        
        

        self._number = None
        self._name = None
        self._sex = None
        self._nationality = None
        self._address = None
        self._birth = None
        self._issue_date = None
        self.__class = None
        self._valid_from = None
        self._valid_to = None
        self._issuing_authority = None
        self._file_number = None
        self._record = None
        self.discriminator = None

        if number is not None:
            self.number = number
        if name is not None:
            self.name = name
        if sex is not None:
            self.sex = sex
        if nationality is not None:
            self.nationality = nationality
        if address is not None:
            self.address = address
        if birth is not None:
            self.birth = birth
        if issue_date is not None:
            self.issue_date = issue_date
        if _class is not None:
            self._class = _class
        if valid_from is not None:
            self.valid_from = valid_from
        if valid_to is not None:
            self.valid_to = valid_to
        if issuing_authority is not None:
            self.issuing_authority = issuing_authority
        if file_number is not None:
            self.file_number = file_number
        if record is not None:
            self.record = record

    @property
    def number(self):
        """Gets the number of this RecognizeDriverLicenseResultResponse.

        驾驶证号。 

        :return: The number of this RecognizeDriverLicenseResultResponse.
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this RecognizeDriverLicenseResultResponse.

        驾驶证号。 

        :param number: The number of this RecognizeDriverLicenseResultResponse.
        :type: str
        """
        self._number = number

    @property
    def name(self):
        """Gets the name of this RecognizeDriverLicenseResultResponse.

        姓名。 

        :return: The name of this RecognizeDriverLicenseResultResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RecognizeDriverLicenseResultResponse.

        姓名。 

        :param name: The name of this RecognizeDriverLicenseResultResponse.
        :type: str
        """
        self._name = name

    @property
    def sex(self):
        """Gets the sex of this RecognizeDriverLicenseResultResponse.

        性别。 

        :return: The sex of this RecognizeDriverLicenseResultResponse.
        :rtype: str
        """
        return self._sex

    @sex.setter
    def sex(self, sex):
        """Sets the sex of this RecognizeDriverLicenseResultResponse.

        性别。 

        :param sex: The sex of this RecognizeDriverLicenseResultResponse.
        :type: str
        """
        self._sex = sex

    @property
    def nationality(self):
        """Gets the nationality of this RecognizeDriverLicenseResultResponse.

        国籍。 

        :return: The nationality of this RecognizeDriverLicenseResultResponse.
        :rtype: str
        """
        return self._nationality

    @nationality.setter
    def nationality(self, nationality):
        """Sets the nationality of this RecognizeDriverLicenseResultResponse.

        国籍。 

        :param nationality: The nationality of this RecognizeDriverLicenseResultResponse.
        :type: str
        """
        self._nationality = nationality

    @property
    def address(self):
        """Gets the address of this RecognizeDriverLicenseResultResponse.

        住址。 

        :return: The address of this RecognizeDriverLicenseResultResponse.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this RecognizeDriverLicenseResultResponse.

        住址。 

        :param address: The address of this RecognizeDriverLicenseResultResponse.
        :type: str
        """
        self._address = address

    @property
    def birth(self):
        """Gets the birth of this RecognizeDriverLicenseResultResponse.

        出生日期。 

        :return: The birth of this RecognizeDriverLicenseResultResponse.
        :rtype: str
        """
        return self._birth

    @birth.setter
    def birth(self, birth):
        """Sets the birth of this RecognizeDriverLicenseResultResponse.

        出生日期。 

        :param birth: The birth of this RecognizeDriverLicenseResultResponse.
        :type: str
        """
        self._birth = birth

    @property
    def issue_date(self):
        """Gets the issue_date of this RecognizeDriverLicenseResultResponse.

        初次领证日期。 

        :return: The issue_date of this RecognizeDriverLicenseResultResponse.
        :rtype: str
        """
        return self._issue_date

    @issue_date.setter
    def issue_date(self, issue_date):
        """Sets the issue_date of this RecognizeDriverLicenseResultResponse.

        初次领证日期。 

        :param issue_date: The issue_date of this RecognizeDriverLicenseResultResponse.
        :type: str
        """
        self._issue_date = issue_date

    @property
    def _class(self):
        """Gets the _class of this RecognizeDriverLicenseResultResponse.

        准驾类型。 

        :return: The _class of this RecognizeDriverLicenseResultResponse.
        :rtype: str
        """
        return self.__class

    @_class.setter
    def _class(self, _class):
        """Sets the _class of this RecognizeDriverLicenseResultResponse.

        准驾类型。 

        :param _class: The _class of this RecognizeDriverLicenseResultResponse.
        :type: str
        """
        self.__class = _class

    @property
    def valid_from(self):
        """Gets the valid_from of this RecognizeDriverLicenseResultResponse.

        有效起始日期。 

        :return: The valid_from of this RecognizeDriverLicenseResultResponse.
        :rtype: str
        """
        return self._valid_from

    @valid_from.setter
    def valid_from(self, valid_from):
        """Sets the valid_from of this RecognizeDriverLicenseResultResponse.

        有效起始日期。 

        :param valid_from: The valid_from of this RecognizeDriverLicenseResultResponse.
        :type: str
        """
        self._valid_from = valid_from

    @property
    def valid_to(self):
        """Gets the valid_to of this RecognizeDriverLicenseResultResponse.

        有效结束日期。 

        :return: The valid_to of this RecognizeDriverLicenseResultResponse.
        :rtype: str
        """
        return self._valid_to

    @valid_to.setter
    def valid_to(self, valid_to):
        """Sets the valid_to of this RecognizeDriverLicenseResultResponse.

        有效结束日期。 

        :param valid_to: The valid_to of this RecognizeDriverLicenseResultResponse.
        :type: str
        """
        self._valid_to = valid_to

    @property
    def issuing_authority(self):
        """Gets the issuing_authority of this RecognizeDriverLicenseResultResponse.

        发证机关。 

        :return: The issuing_authority of this RecognizeDriverLicenseResultResponse.
        :rtype: str
        """
        return self._issuing_authority

    @issuing_authority.setter
    def issuing_authority(self, issuing_authority):
        """Sets the issuing_authority of this RecognizeDriverLicenseResultResponse.

        发证机关。 

        :param issuing_authority: The issuing_authority of this RecognizeDriverLicenseResultResponse.
        :type: str
        """
        self._issuing_authority = issuing_authority

    @property
    def file_number(self):
        """Gets the file_number of this RecognizeDriverLicenseResultResponse.

        档案编号。 

        :return: The file_number of this RecognizeDriverLicenseResultResponse.
        :rtype: str
        """
        return self._file_number

    @file_number.setter
    def file_number(self, file_number):
        """Sets the file_number of this RecognizeDriverLicenseResultResponse.

        档案编号。 

        :param file_number: The file_number of this RecognizeDriverLicenseResultResponse.
        :type: str
        """
        self._file_number = file_number

    @property
    def record(self):
        """Gets the record of this RecognizeDriverLicenseResultResponse.

        记录。 

        :return: The record of this RecognizeDriverLicenseResultResponse.
        :rtype: str
        """
        return self._record

    @record.setter
    def record(self, record):
        """Sets the record of this RecognizeDriverLicenseResultResponse.

        记录。 

        :param record: The record of this RecognizeDriverLicenseResultResponse.
        :type: str
        """
        self._record = record

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, RecognizeDriverLicenseResultResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
