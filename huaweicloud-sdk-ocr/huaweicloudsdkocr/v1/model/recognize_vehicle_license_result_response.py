# coding: utf-8

import pprint
import re

import six





class RecognizeVehicleLicenseResultResponse:


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
        'engine_no': 'str',
        'vin': 'str',
        'register_date': 'str',
        'issue_date': 'str',
        'issuing_authority': 'str',
        'file_no': 'str',
        'approved_passengers': 'str',
        'gross_mass': 'str',
        'unladen_mass': 'str',
        'approved_load': 'str',
        'dimension': 'str',
        'traction_mass': 'str',
        'remarks': 'str',
        'inspection_record': 'str',
        'code_number': 'str'
    }

    attribute_map = {
        'number': 'number',
        'vehicle_type': 'vehicle_type',
        'name': 'name',
        'address': 'address',
        'use_character': 'use_character',
        'model': 'model',
        'engine_no': 'engine_no',
        'vin': 'vin',
        'register_date': 'register_date',
        'issue_date': 'issue_date',
        'issuing_authority': 'issuing_authority',
        'file_no': 'file_no',
        'approved_passengers': 'approved_passengers',
        'gross_mass': 'gross_mass',
        'unladen_mass': 'unladen_mass',
        'approved_load': 'approved_load',
        'dimension': 'dimension',
        'traction_mass': 'traction_mass',
        'remarks': 'remarks',
        'inspection_record': 'inspection_record',
        'code_number': 'code_number'
    }

    def __init__(self, number=None, vehicle_type=None, name=None, address=None, use_character=None, model=None, engine_no=None, vin=None, register_date=None, issue_date=None, issuing_authority=None, file_no=None, approved_passengers=None, gross_mass=None, unladen_mass=None, approved_load=None, dimension=None, traction_mass=None, remarks=None, inspection_record=None, code_number=None):
        """RecognizeVehicleLicenseResultResponse - a model defined in huaweicloud sdk"""
        
        

        self._number = None
        self._vehicle_type = None
        self._name = None
        self._address = None
        self._use_character = None
        self._model = None
        self._engine_no = None
        self._vin = None
        self._register_date = None
        self._issue_date = None
        self._issuing_authority = None
        self._file_no = None
        self._approved_passengers = None
        self._gross_mass = None
        self._unladen_mass = None
        self._approved_load = None
        self._dimension = None
        self._traction_mass = None
        self._remarks = None
        self._inspection_record = None
        self._code_number = None
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
        if engine_no is not None:
            self.engine_no = engine_no
        if vin is not None:
            self.vin = vin
        if register_date is not None:
            self.register_date = register_date
        if issue_date is not None:
            self.issue_date = issue_date
        if issuing_authority is not None:
            self.issuing_authority = issuing_authority
        if file_no is not None:
            self.file_no = file_no
        if approved_passengers is not None:
            self.approved_passengers = approved_passengers
        if gross_mass is not None:
            self.gross_mass = gross_mass
        if unladen_mass is not None:
            self.unladen_mass = unladen_mass
        if approved_load is not None:
            self.approved_load = approved_load
        if dimension is not None:
            self.dimension = dimension
        if traction_mass is not None:
            self.traction_mass = traction_mass
        if remarks is not None:
            self.remarks = remarks
        if inspection_record is not None:
            self.inspection_record = inspection_record
        if code_number is not None:
            self.code_number = code_number

    @property
    def number(self):
        """Gets the number of this RecognizeVehicleLicenseResultResponse.

        号牌号码。 

        :return: The number of this RecognizeVehicleLicenseResultResponse.
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this RecognizeVehicleLicenseResultResponse.

        号牌号码。 

        :param number: The number of this RecognizeVehicleLicenseResultResponse.
        :type: str
        """
        self._number = number

    @property
    def vehicle_type(self):
        """Gets the vehicle_type of this RecognizeVehicleLicenseResultResponse.

        车辆类型。 

        :return: The vehicle_type of this RecognizeVehicleLicenseResultResponse.
        :rtype: str
        """
        return self._vehicle_type

    @vehicle_type.setter
    def vehicle_type(self, vehicle_type):
        """Sets the vehicle_type of this RecognizeVehicleLicenseResultResponse.

        车辆类型。 

        :param vehicle_type: The vehicle_type of this RecognizeVehicleLicenseResultResponse.
        :type: str
        """
        self._vehicle_type = vehicle_type

    @property
    def name(self):
        """Gets the name of this RecognizeVehicleLicenseResultResponse.

        所有人。 

        :return: The name of this RecognizeVehicleLicenseResultResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RecognizeVehicleLicenseResultResponse.

        所有人。 

        :param name: The name of this RecognizeVehicleLicenseResultResponse.
        :type: str
        """
        self._name = name

    @property
    def address(self):
        """Gets the address of this RecognizeVehicleLicenseResultResponse.

        住址。 

        :return: The address of this RecognizeVehicleLicenseResultResponse.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this RecognizeVehicleLicenseResultResponse.

        住址。 

        :param address: The address of this RecognizeVehicleLicenseResultResponse.
        :type: str
        """
        self._address = address

    @property
    def use_character(self):
        """Gets the use_character of this RecognizeVehicleLicenseResultResponse.

        使用性质。 

        :return: The use_character of this RecognizeVehicleLicenseResultResponse.
        :rtype: str
        """
        return self._use_character

    @use_character.setter
    def use_character(self, use_character):
        """Sets the use_character of this RecognizeVehicleLicenseResultResponse.

        使用性质。 

        :param use_character: The use_character of this RecognizeVehicleLicenseResultResponse.
        :type: str
        """
        self._use_character = use_character

    @property
    def model(self):
        """Gets the model of this RecognizeVehicleLicenseResultResponse.

        品牌型号。 

        :return: The model of this RecognizeVehicleLicenseResultResponse.
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this RecognizeVehicleLicenseResultResponse.

        品牌型号。 

        :param model: The model of this RecognizeVehicleLicenseResultResponse.
        :type: str
        """
        self._model = model

    @property
    def engine_no(self):
        """Gets the engine_no of this RecognizeVehicleLicenseResultResponse.

        发动机号码。 

        :return: The engine_no of this RecognizeVehicleLicenseResultResponse.
        :rtype: str
        """
        return self._engine_no

    @engine_no.setter
    def engine_no(self, engine_no):
        """Sets the engine_no of this RecognizeVehicleLicenseResultResponse.

        发动机号码。 

        :param engine_no: The engine_no of this RecognizeVehicleLicenseResultResponse.
        :type: str
        """
        self._engine_no = engine_no

    @property
    def vin(self):
        """Gets the vin of this RecognizeVehicleLicenseResultResponse.

        车辆识别代号。 

        :return: The vin of this RecognizeVehicleLicenseResultResponse.
        :rtype: str
        """
        return self._vin

    @vin.setter
    def vin(self, vin):
        """Sets the vin of this RecognizeVehicleLicenseResultResponse.

        车辆识别代号。 

        :param vin: The vin of this RecognizeVehicleLicenseResultResponse.
        :type: str
        """
        self._vin = vin

    @property
    def register_date(self):
        """Gets the register_date of this RecognizeVehicleLicenseResultResponse.

        注册日期。 

        :return: The register_date of this RecognizeVehicleLicenseResultResponse.
        :rtype: str
        """
        return self._register_date

    @register_date.setter
    def register_date(self, register_date):
        """Sets the register_date of this RecognizeVehicleLicenseResultResponse.

        注册日期。 

        :param register_date: The register_date of this RecognizeVehicleLicenseResultResponse.
        :type: str
        """
        self._register_date = register_date

    @property
    def issue_date(self):
        """Gets the issue_date of this RecognizeVehicleLicenseResultResponse.

        发证日期。 

        :return: The issue_date of this RecognizeVehicleLicenseResultResponse.
        :rtype: str
        """
        return self._issue_date

    @issue_date.setter
    def issue_date(self, issue_date):
        """Sets the issue_date of this RecognizeVehicleLicenseResultResponse.

        发证日期。 

        :param issue_date: The issue_date of this RecognizeVehicleLicenseResultResponse.
        :type: str
        """
        self._issue_date = issue_date

    @property
    def issuing_authority(self):
        """Gets the issuing_authority of this RecognizeVehicleLicenseResultResponse.

        发证机关。 

        :return: The issuing_authority of this RecognizeVehicleLicenseResultResponse.
        :rtype: str
        """
        return self._issuing_authority

    @issuing_authority.setter
    def issuing_authority(self, issuing_authority):
        """Sets the issuing_authority of this RecognizeVehicleLicenseResultResponse.

        发证机关。 

        :param issuing_authority: The issuing_authority of this RecognizeVehicleLicenseResultResponse.
        :type: str
        """
        self._issuing_authority = issuing_authority

    @property
    def file_no(self):
        """Gets the file_no of this RecognizeVehicleLicenseResultResponse.

        档案编码。 

        :return: The file_no of this RecognizeVehicleLicenseResultResponse.
        :rtype: str
        """
        return self._file_no

    @file_no.setter
    def file_no(self, file_no):
        """Sets the file_no of this RecognizeVehicleLicenseResultResponse.

        档案编码。 

        :param file_no: The file_no of this RecognizeVehicleLicenseResultResponse.
        :type: str
        """
        self._file_no = file_no

    @property
    def approved_passengers(self):
        """Gets the approved_passengers of this RecognizeVehicleLicenseResultResponse.

        核定载人数。 

        :return: The approved_passengers of this RecognizeVehicleLicenseResultResponse.
        :rtype: str
        """
        return self._approved_passengers

    @approved_passengers.setter
    def approved_passengers(self, approved_passengers):
        """Sets the approved_passengers of this RecognizeVehicleLicenseResultResponse.

        核定载人数。 

        :param approved_passengers: The approved_passengers of this RecognizeVehicleLicenseResultResponse.
        :type: str
        """
        self._approved_passengers = approved_passengers

    @property
    def gross_mass(self):
        """Gets the gross_mass of this RecognizeVehicleLicenseResultResponse.

        总质量。 

        :return: The gross_mass of this RecognizeVehicleLicenseResultResponse.
        :rtype: str
        """
        return self._gross_mass

    @gross_mass.setter
    def gross_mass(self, gross_mass):
        """Sets the gross_mass of this RecognizeVehicleLicenseResultResponse.

        总质量。 

        :param gross_mass: The gross_mass of this RecognizeVehicleLicenseResultResponse.
        :type: str
        """
        self._gross_mass = gross_mass

    @property
    def unladen_mass(self):
        """Gets the unladen_mass of this RecognizeVehicleLicenseResultResponse.

        整备质量。 

        :return: The unladen_mass of this RecognizeVehicleLicenseResultResponse.
        :rtype: str
        """
        return self._unladen_mass

    @unladen_mass.setter
    def unladen_mass(self, unladen_mass):
        """Sets the unladen_mass of this RecognizeVehicleLicenseResultResponse.

        整备质量。 

        :param unladen_mass: The unladen_mass of this RecognizeVehicleLicenseResultResponse.
        :type: str
        """
        self._unladen_mass = unladen_mass

    @property
    def approved_load(self):
        """Gets the approved_load of this RecognizeVehicleLicenseResultResponse.

        核定载质量。 

        :return: The approved_load of this RecognizeVehicleLicenseResultResponse.
        :rtype: str
        """
        return self._approved_load

    @approved_load.setter
    def approved_load(self, approved_load):
        """Sets the approved_load of this RecognizeVehicleLicenseResultResponse.

        核定载质量。 

        :param approved_load: The approved_load of this RecognizeVehicleLicenseResultResponse.
        :type: str
        """
        self._approved_load = approved_load

    @property
    def dimension(self):
        """Gets the dimension of this RecognizeVehicleLicenseResultResponse.

        外廓尺寸。 

        :return: The dimension of this RecognizeVehicleLicenseResultResponse.
        :rtype: str
        """
        return self._dimension

    @dimension.setter
    def dimension(self, dimension):
        """Sets the dimension of this RecognizeVehicleLicenseResultResponse.

        外廓尺寸。 

        :param dimension: The dimension of this RecognizeVehicleLicenseResultResponse.
        :type: str
        """
        self._dimension = dimension

    @property
    def traction_mass(self):
        """Gets the traction_mass of this RecognizeVehicleLicenseResultResponse.

        准牵引总质量。 

        :return: The traction_mass of this RecognizeVehicleLicenseResultResponse.
        :rtype: str
        """
        return self._traction_mass

    @traction_mass.setter
    def traction_mass(self, traction_mass):
        """Sets the traction_mass of this RecognizeVehicleLicenseResultResponse.

        准牵引总质量。 

        :param traction_mass: The traction_mass of this RecognizeVehicleLicenseResultResponse.
        :type: str
        """
        self._traction_mass = traction_mass

    @property
    def remarks(self):
        """Gets the remarks of this RecognizeVehicleLicenseResultResponse.

        备注。 

        :return: The remarks of this RecognizeVehicleLicenseResultResponse.
        :rtype: str
        """
        return self._remarks

    @remarks.setter
    def remarks(self, remarks):
        """Sets the remarks of this RecognizeVehicleLicenseResultResponse.

        备注。 

        :param remarks: The remarks of this RecognizeVehicleLicenseResultResponse.
        :type: str
        """
        self._remarks = remarks

    @property
    def inspection_record(self):
        """Gets the inspection_record of this RecognizeVehicleLicenseResultResponse.

        检验记录。 

        :return: The inspection_record of this RecognizeVehicleLicenseResultResponse.
        :rtype: str
        """
        return self._inspection_record

    @inspection_record.setter
    def inspection_record(self, inspection_record):
        """Sets the inspection_record of this RecognizeVehicleLicenseResultResponse.

        检验记录。 

        :param inspection_record: The inspection_record of this RecognizeVehicleLicenseResultResponse.
        :type: str
        """
        self._inspection_record = inspection_record

    @property
    def code_number(self):
        """Gets the code_number of this RecognizeVehicleLicenseResultResponse.

        条码号。 

        :return: The code_number of this RecognizeVehicleLicenseResultResponse.
        :rtype: str
        """
        return self._code_number

    @code_number.setter
    def code_number(self, code_number):
        """Sets the code_number of this RecognizeVehicleLicenseResultResponse.

        条码号。 

        :param code_number: The code_number of this RecognizeVehicleLicenseResultResponse.
        :type: str
        """
        self._code_number = code_number

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
        if not isinstance(other, RecognizeVehicleLicenseResultResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
