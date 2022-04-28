# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DriverLicenseResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'type': 'str',
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
        'record': 'str',
        'accumulated_scores': 'str',
        'status': 'list[str]',
        'generation_date': 'str',
        'current_time': 'str',
        'text_location': 'object'
    }

    attribute_map = {
        'type': 'type',
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
        'record': 'record',
        'accumulated_scores': 'accumulated_scores',
        'status': 'status',
        'generation_date': 'generation_date',
        'current_time': 'current_time',
        'text_location': 'text_location'
    }

    def __init__(self, type=None, number=None, name=None, sex=None, nationality=None, address=None, birth=None, issue_date=None, _class=None, valid_from=None, valid_to=None, issuing_authority=None, file_number=None, record=None, accumulated_scores=None, status=None, generation_date=None, current_time=None, text_location=None):
        """DriverLicenseResult

        The model defined in huaweicloud sdk

        :param type: 驾驶证类型。 normal：纸质驾驶证 electronic：电子驾驶证 
        :type type: str
        :param number: 驾驶证号。 
        :type number: str
        :param name: 姓名。 
        :type name: str
        :param sex: 性别。 
        :type sex: str
        :param nationality: 国籍。 
        :type nationality: str
        :param address: 住址。 
        :type address: str
        :param birth: 出生日期。 
        :type birth: str
        :param issue_date: 初次领证日期。 
        :type issue_date: str
        :param _class: 准驾类型。 
        :type _class: str
        :param valid_from: 有效起始日期。 
        :type valid_from: str
        :param valid_to: 有效结束日期。 
        :type valid_to: str
        :param issuing_authority: 发证机关。 
        :type issuing_authority: str
        :param file_number: 档案编号。 
        :type file_number: str
        :param record: 记录。 
        :type record: str
        :param accumulated_scores: 累积记分。 
        :type accumulated_scores: str
        :param status: 状态。
        :type status: list[str]
        :param generation_date: 生成时间。 
        :type generation_date: str
        :param current_time: 当前时间。 
        :type current_time: str
        :param text_location: 对应所有在原图上识别到的字段位置信息，包含所有文字区域四个顶点的二维坐标（x,y）。采用图像坐标系，坐标原点为图片左上角，x轴沿水平方向，y轴沿竖直方向。 
        :type text_location: object
        """
        
        

        self._type = None
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
        self._accumulated_scores = None
        self._status = None
        self._generation_date = None
        self._current_time = None
        self._text_location = None
        self.discriminator = None

        if type is not None:
            self.type = type
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
        if accumulated_scores is not None:
            self.accumulated_scores = accumulated_scores
        if status is not None:
            self.status = status
        if generation_date is not None:
            self.generation_date = generation_date
        if current_time is not None:
            self.current_time = current_time
        if text_location is not None:
            self.text_location = text_location

    @property
    def type(self):
        """Gets the type of this DriverLicenseResult.

        驾驶证类型。 normal：纸质驾驶证 electronic：电子驾驶证 

        :return: The type of this DriverLicenseResult.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DriverLicenseResult.

        驾驶证类型。 normal：纸质驾驶证 electronic：电子驾驶证 

        :param type: The type of this DriverLicenseResult.
        :type type: str
        """
        self._type = type

    @property
    def number(self):
        """Gets the number of this DriverLicenseResult.

        驾驶证号。 

        :return: The number of this DriverLicenseResult.
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this DriverLicenseResult.

        驾驶证号。 

        :param number: The number of this DriverLicenseResult.
        :type number: str
        """
        self._number = number

    @property
    def name(self):
        """Gets the name of this DriverLicenseResult.

        姓名。 

        :return: The name of this DriverLicenseResult.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DriverLicenseResult.

        姓名。 

        :param name: The name of this DriverLicenseResult.
        :type name: str
        """
        self._name = name

    @property
    def sex(self):
        """Gets the sex of this DriverLicenseResult.

        性别。 

        :return: The sex of this DriverLicenseResult.
        :rtype: str
        """
        return self._sex

    @sex.setter
    def sex(self, sex):
        """Sets the sex of this DriverLicenseResult.

        性别。 

        :param sex: The sex of this DriverLicenseResult.
        :type sex: str
        """
        self._sex = sex

    @property
    def nationality(self):
        """Gets the nationality of this DriverLicenseResult.

        国籍。 

        :return: The nationality of this DriverLicenseResult.
        :rtype: str
        """
        return self._nationality

    @nationality.setter
    def nationality(self, nationality):
        """Sets the nationality of this DriverLicenseResult.

        国籍。 

        :param nationality: The nationality of this DriverLicenseResult.
        :type nationality: str
        """
        self._nationality = nationality

    @property
    def address(self):
        """Gets the address of this DriverLicenseResult.

        住址。 

        :return: The address of this DriverLicenseResult.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this DriverLicenseResult.

        住址。 

        :param address: The address of this DriverLicenseResult.
        :type address: str
        """
        self._address = address

    @property
    def birth(self):
        """Gets the birth of this DriverLicenseResult.

        出生日期。 

        :return: The birth of this DriverLicenseResult.
        :rtype: str
        """
        return self._birth

    @birth.setter
    def birth(self, birth):
        """Sets the birth of this DriverLicenseResult.

        出生日期。 

        :param birth: The birth of this DriverLicenseResult.
        :type birth: str
        """
        self._birth = birth

    @property
    def issue_date(self):
        """Gets the issue_date of this DriverLicenseResult.

        初次领证日期。 

        :return: The issue_date of this DriverLicenseResult.
        :rtype: str
        """
        return self._issue_date

    @issue_date.setter
    def issue_date(self, issue_date):
        """Sets the issue_date of this DriverLicenseResult.

        初次领证日期。 

        :param issue_date: The issue_date of this DriverLicenseResult.
        :type issue_date: str
        """
        self._issue_date = issue_date

    @property
    def _class(self):
        """Gets the _class of this DriverLicenseResult.

        准驾类型。 

        :return: The _class of this DriverLicenseResult.
        :rtype: str
        """
        return self.__class

    @_class.setter
    def _class(self, _class):
        """Sets the _class of this DriverLicenseResult.

        准驾类型。 

        :param _class: The _class of this DriverLicenseResult.
        :type _class: str
        """
        self.__class = _class

    @property
    def valid_from(self):
        """Gets the valid_from of this DriverLicenseResult.

        有效起始日期。 

        :return: The valid_from of this DriverLicenseResult.
        :rtype: str
        """
        return self._valid_from

    @valid_from.setter
    def valid_from(self, valid_from):
        """Sets the valid_from of this DriverLicenseResult.

        有效起始日期。 

        :param valid_from: The valid_from of this DriverLicenseResult.
        :type valid_from: str
        """
        self._valid_from = valid_from

    @property
    def valid_to(self):
        """Gets the valid_to of this DriverLicenseResult.

        有效结束日期。 

        :return: The valid_to of this DriverLicenseResult.
        :rtype: str
        """
        return self._valid_to

    @valid_to.setter
    def valid_to(self, valid_to):
        """Sets the valid_to of this DriverLicenseResult.

        有效结束日期。 

        :param valid_to: The valid_to of this DriverLicenseResult.
        :type valid_to: str
        """
        self._valid_to = valid_to

    @property
    def issuing_authority(self):
        """Gets the issuing_authority of this DriverLicenseResult.

        发证机关。 

        :return: The issuing_authority of this DriverLicenseResult.
        :rtype: str
        """
        return self._issuing_authority

    @issuing_authority.setter
    def issuing_authority(self, issuing_authority):
        """Sets the issuing_authority of this DriverLicenseResult.

        发证机关。 

        :param issuing_authority: The issuing_authority of this DriverLicenseResult.
        :type issuing_authority: str
        """
        self._issuing_authority = issuing_authority

    @property
    def file_number(self):
        """Gets the file_number of this DriverLicenseResult.

        档案编号。 

        :return: The file_number of this DriverLicenseResult.
        :rtype: str
        """
        return self._file_number

    @file_number.setter
    def file_number(self, file_number):
        """Sets the file_number of this DriverLicenseResult.

        档案编号。 

        :param file_number: The file_number of this DriverLicenseResult.
        :type file_number: str
        """
        self._file_number = file_number

    @property
    def record(self):
        """Gets the record of this DriverLicenseResult.

        记录。 

        :return: The record of this DriverLicenseResult.
        :rtype: str
        """
        return self._record

    @record.setter
    def record(self, record):
        """Sets the record of this DriverLicenseResult.

        记录。 

        :param record: The record of this DriverLicenseResult.
        :type record: str
        """
        self._record = record

    @property
    def accumulated_scores(self):
        """Gets the accumulated_scores of this DriverLicenseResult.

        累积记分。 

        :return: The accumulated_scores of this DriverLicenseResult.
        :rtype: str
        """
        return self._accumulated_scores

    @accumulated_scores.setter
    def accumulated_scores(self, accumulated_scores):
        """Sets the accumulated_scores of this DriverLicenseResult.

        累积记分。 

        :param accumulated_scores: The accumulated_scores of this DriverLicenseResult.
        :type accumulated_scores: str
        """
        self._accumulated_scores = accumulated_scores

    @property
    def status(self):
        """Gets the status of this DriverLicenseResult.

        状态。

        :return: The status of this DriverLicenseResult.
        :rtype: list[str]
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DriverLicenseResult.

        状态。

        :param status: The status of this DriverLicenseResult.
        :type status: list[str]
        """
        self._status = status

    @property
    def generation_date(self):
        """Gets the generation_date of this DriverLicenseResult.

        生成时间。 

        :return: The generation_date of this DriverLicenseResult.
        :rtype: str
        """
        return self._generation_date

    @generation_date.setter
    def generation_date(self, generation_date):
        """Sets the generation_date of this DriverLicenseResult.

        生成时间。 

        :param generation_date: The generation_date of this DriverLicenseResult.
        :type generation_date: str
        """
        self._generation_date = generation_date

    @property
    def current_time(self):
        """Gets the current_time of this DriverLicenseResult.

        当前时间。 

        :return: The current_time of this DriverLicenseResult.
        :rtype: str
        """
        return self._current_time

    @current_time.setter
    def current_time(self, current_time):
        """Sets the current_time of this DriverLicenseResult.

        当前时间。 

        :param current_time: The current_time of this DriverLicenseResult.
        :type current_time: str
        """
        self._current_time = current_time

    @property
    def text_location(self):
        """Gets the text_location of this DriverLicenseResult.

        对应所有在原图上识别到的字段位置信息，包含所有文字区域四个顶点的二维坐标（x,y）。采用图像坐标系，坐标原点为图片左上角，x轴沿水平方向，y轴沿竖直方向。 

        :return: The text_location of this DriverLicenseResult.
        :rtype: object
        """
        return self._text_location

    @text_location.setter
    def text_location(self, text_location):
        """Sets the text_location of this DriverLicenseResult.

        对应所有在原图上识别到的字段位置信息，包含所有文字区域四个顶点的二维坐标（x,y）。采用图像坐标系，坐标原点为图片左上角，x轴沿水平方向，y轴沿竖直方向。 

        :param text_location: The text_location of this DriverLicenseResult.
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
        if not isinstance(other, DriverLicenseResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
