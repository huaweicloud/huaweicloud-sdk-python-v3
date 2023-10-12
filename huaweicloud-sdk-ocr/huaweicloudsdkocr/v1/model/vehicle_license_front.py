# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VehicleLicenseFront:

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
        'vehicle_type': 'str',
        'name': 'str',
        'address': 'str',
        'use_character': 'str',
        'model': 'str',
        'vin': 'str',
        'engine_no': 'str',
        'register_date': 'str',
        'issue_date': 'str',
        'issuing_authority': 'str',
        'text_location': 'object'
    }

    attribute_map = {
        'number': 'number',
        'vehicle_type': 'vehicle_type',
        'name': 'name',
        'address': 'address',
        'use_character': 'use_character',
        'model': 'model',
        'vin': 'vin',
        'engine_no': 'engine_no',
        'register_date': 'register_date',
        'issue_date': 'issue_date',
        'issuing_authority': 'issuing_authority',
        'text_location': 'text_location'
    }

    def __init__(self, number=None, vehicle_type=None, name=None, address=None, use_character=None, model=None, vin=None, engine_no=None, register_date=None, issue_date=None, issuing_authority=None, text_location=None):
        """VehicleLicenseFront

        The model defined in huaweicloud sdk

        :param number: 号牌号码。
        :type number: str
        :param vehicle_type: 车辆类型。
        :type vehicle_type: str
        :param name: 所有人。
        :type name: str
        :param address: 住址。
        :type address: str
        :param use_character: 使用性质。
        :type use_character: str
        :param model: 品牌型号。
        :type model: str
        :param vin: 车辆识别代号。
        :type vin: str
        :param engine_no: 发动机号码。
        :type engine_no: str
        :param register_date: 注册日期。
        :type register_date: str
        :param issue_date: 发证日期。
        :type issue_date: str
        :param issuing_authority: 发证机关。
        :type issuing_authority: str
        :param text_location: 文本框在原图位置。输出左上、右上、右下、左下四个点坐标。  当“return_text_location”设置为“true”时才返回。
        :type text_location: object
        """
        
        

        self._number = None
        self._vehicle_type = None
        self._name = None
        self._address = None
        self._use_character = None
        self._model = None
        self._vin = None
        self._engine_no = None
        self._register_date = None
        self._issue_date = None
        self._issuing_authority = None
        self._text_location = None
        self.discriminator = None

        if number is not None:
            self.number = number
        if vehicle_type is not None:
            self.vehicle_type = vehicle_type
        if name is not None:
            self.name = name
        if address is not None:
            self.address = address
        if use_character is not None:
            self.use_character = use_character
        if model is not None:
            self.model = model
        if vin is not None:
            self.vin = vin
        if engine_no is not None:
            self.engine_no = engine_no
        if register_date is not None:
            self.register_date = register_date
        if issue_date is not None:
            self.issue_date = issue_date
        if issuing_authority is not None:
            self.issuing_authority = issuing_authority
        if text_location is not None:
            self.text_location = text_location

    @property
    def number(self):
        """Gets the number of this VehicleLicenseFront.

        号牌号码。

        :return: The number of this VehicleLicenseFront.
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this VehicleLicenseFront.

        号牌号码。

        :param number: The number of this VehicleLicenseFront.
        :type number: str
        """
        self._number = number

    @property
    def vehicle_type(self):
        """Gets the vehicle_type of this VehicleLicenseFront.

        车辆类型。

        :return: The vehicle_type of this VehicleLicenseFront.
        :rtype: str
        """
        return self._vehicle_type

    @vehicle_type.setter
    def vehicle_type(self, vehicle_type):
        """Sets the vehicle_type of this VehicleLicenseFront.

        车辆类型。

        :param vehicle_type: The vehicle_type of this VehicleLicenseFront.
        :type vehicle_type: str
        """
        self._vehicle_type = vehicle_type

    @property
    def name(self):
        """Gets the name of this VehicleLicenseFront.

        所有人。

        :return: The name of this VehicleLicenseFront.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VehicleLicenseFront.

        所有人。

        :param name: The name of this VehicleLicenseFront.
        :type name: str
        """
        self._name = name

    @property
    def address(self):
        """Gets the address of this VehicleLicenseFront.

        住址。

        :return: The address of this VehicleLicenseFront.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this VehicleLicenseFront.

        住址。

        :param address: The address of this VehicleLicenseFront.
        :type address: str
        """
        self._address = address

    @property
    def use_character(self):
        """Gets the use_character of this VehicleLicenseFront.

        使用性质。

        :return: The use_character of this VehicleLicenseFront.
        :rtype: str
        """
        return self._use_character

    @use_character.setter
    def use_character(self, use_character):
        """Sets the use_character of this VehicleLicenseFront.

        使用性质。

        :param use_character: The use_character of this VehicleLicenseFront.
        :type use_character: str
        """
        self._use_character = use_character

    @property
    def model(self):
        """Gets the model of this VehicleLicenseFront.

        品牌型号。

        :return: The model of this VehicleLicenseFront.
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this VehicleLicenseFront.

        品牌型号。

        :param model: The model of this VehicleLicenseFront.
        :type model: str
        """
        self._model = model

    @property
    def vin(self):
        """Gets the vin of this VehicleLicenseFront.

        车辆识别代号。

        :return: The vin of this VehicleLicenseFront.
        :rtype: str
        """
        return self._vin

    @vin.setter
    def vin(self, vin):
        """Sets the vin of this VehicleLicenseFront.

        车辆识别代号。

        :param vin: The vin of this VehicleLicenseFront.
        :type vin: str
        """
        self._vin = vin

    @property
    def engine_no(self):
        """Gets the engine_no of this VehicleLicenseFront.

        发动机号码。

        :return: The engine_no of this VehicleLicenseFront.
        :rtype: str
        """
        return self._engine_no

    @engine_no.setter
    def engine_no(self, engine_no):
        """Sets the engine_no of this VehicleLicenseFront.

        发动机号码。

        :param engine_no: The engine_no of this VehicleLicenseFront.
        :type engine_no: str
        """
        self._engine_no = engine_no

    @property
    def register_date(self):
        """Gets the register_date of this VehicleLicenseFront.

        注册日期。

        :return: The register_date of this VehicleLicenseFront.
        :rtype: str
        """
        return self._register_date

    @register_date.setter
    def register_date(self, register_date):
        """Sets the register_date of this VehicleLicenseFront.

        注册日期。

        :param register_date: The register_date of this VehicleLicenseFront.
        :type register_date: str
        """
        self._register_date = register_date

    @property
    def issue_date(self):
        """Gets the issue_date of this VehicleLicenseFront.

        发证日期。

        :return: The issue_date of this VehicleLicenseFront.
        :rtype: str
        """
        return self._issue_date

    @issue_date.setter
    def issue_date(self, issue_date):
        """Sets the issue_date of this VehicleLicenseFront.

        发证日期。

        :param issue_date: The issue_date of this VehicleLicenseFront.
        :type issue_date: str
        """
        self._issue_date = issue_date

    @property
    def issuing_authority(self):
        """Gets the issuing_authority of this VehicleLicenseFront.

        发证机关。

        :return: The issuing_authority of this VehicleLicenseFront.
        :rtype: str
        """
        return self._issuing_authority

    @issuing_authority.setter
    def issuing_authority(self, issuing_authority):
        """Sets the issuing_authority of this VehicleLicenseFront.

        发证机关。

        :param issuing_authority: The issuing_authority of this VehicleLicenseFront.
        :type issuing_authority: str
        """
        self._issuing_authority = issuing_authority

    @property
    def text_location(self):
        """Gets the text_location of this VehicleLicenseFront.

        文本框在原图位置。输出左上、右上、右下、左下四个点坐标。  当“return_text_location”设置为“true”时才返回。

        :return: The text_location of this VehicleLicenseFront.
        :rtype: object
        """
        return self._text_location

    @text_location.setter
    def text_location(self, text_location):
        """Sets the text_location of this VehicleLicenseFront.

        文本框在原图位置。输出左上、右上、右下、左下四个点坐标。  当“return_text_location”设置为“true”时才返回。

        :param text_location: The text_location of this VehicleLicenseFront.
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
        if not isinstance(other, VehicleLicenseFront):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
