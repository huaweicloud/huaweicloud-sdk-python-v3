# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VehicleLicenseback:

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
        'file_no': 'str',
        'approved_passengers': 'str',
        'gross_mass': 'str',
        'unladen_mass': 'str',
        'approved_load': 'str',
        'dimension': 'str',
        'traction_mass': 'str',
        'remarks': 'str',
        'inspection_record': 'str',
        'code_number': 'str',
        'energy_type': 'str',
        'text_location': 'object'
    }

    attribute_map = {
        'number': 'number',
        'file_no': 'file_no',
        'approved_passengers': 'approved_passengers',
        'gross_mass': 'gross_mass',
        'unladen_mass': 'unladen_mass',
        'approved_load': 'approved_load',
        'dimension': 'dimension',
        'traction_mass': 'traction_mass',
        'remarks': 'remarks',
        'inspection_record': 'inspection_record',
        'code_number': 'code_number',
        'energy_type': 'energy_type',
        'text_location': 'text_location'
    }

    def __init__(self, number=None, file_no=None, approved_passengers=None, gross_mass=None, unladen_mass=None, approved_load=None, dimension=None, traction_mass=None, remarks=None, inspection_record=None, code_number=None, energy_type=None, text_location=None):
        r"""VehicleLicenseback

        The model defined in huaweicloud sdk

        :param number: 号牌号码。 
        :type number: str
        :param file_no: 档案编码。 
        :type file_no: str
        :param approved_passengers: 核定载人数。 
        :type approved_passengers: str
        :param gross_mass: 总质量。 
        :type gross_mass: str
        :param unladen_mass: 整备质量。 
        :type unladen_mass: str
        :param approved_load: 核定载质量。 
        :type approved_load: str
        :param dimension: 外廓尺寸。 
        :type dimension: str
        :param traction_mass: 准牵引总质量。 
        :type traction_mass: str
        :param remarks: 备注。 
        :type remarks: str
        :param inspection_record: 检验记录。 
        :type inspection_record: str
        :param code_number: 条码号。           
        :type code_number: str
        :param energy_type: 能源类型。 
        :type energy_type: str
        :param text_location: 文本框在原图位置。输出左上、右上、右下、左下四个点坐标。  当“return_text_location”设置为“true”时才返回。 
        :type text_location: object
        """
        
        

        self._number = None
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
        self._energy_type = None
        self._text_location = None
        self.discriminator = None

        if number is not None:
            self.number = number
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
        if energy_type is not None:
            self.energy_type = energy_type
        if text_location is not None:
            self.text_location = text_location

    @property
    def number(self):
        r"""Gets the number of this VehicleLicenseback.

        号牌号码。 

        :return: The number of this VehicleLicenseback.
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        r"""Sets the number of this VehicleLicenseback.

        号牌号码。 

        :param number: The number of this VehicleLicenseback.
        :type number: str
        """
        self._number = number

    @property
    def file_no(self):
        r"""Gets the file_no of this VehicleLicenseback.

        档案编码。 

        :return: The file_no of this VehicleLicenseback.
        :rtype: str
        """
        return self._file_no

    @file_no.setter
    def file_no(self, file_no):
        r"""Sets the file_no of this VehicleLicenseback.

        档案编码。 

        :param file_no: The file_no of this VehicleLicenseback.
        :type file_no: str
        """
        self._file_no = file_no

    @property
    def approved_passengers(self):
        r"""Gets the approved_passengers of this VehicleLicenseback.

        核定载人数。 

        :return: The approved_passengers of this VehicleLicenseback.
        :rtype: str
        """
        return self._approved_passengers

    @approved_passengers.setter
    def approved_passengers(self, approved_passengers):
        r"""Sets the approved_passengers of this VehicleLicenseback.

        核定载人数。 

        :param approved_passengers: The approved_passengers of this VehicleLicenseback.
        :type approved_passengers: str
        """
        self._approved_passengers = approved_passengers

    @property
    def gross_mass(self):
        r"""Gets the gross_mass of this VehicleLicenseback.

        总质量。 

        :return: The gross_mass of this VehicleLicenseback.
        :rtype: str
        """
        return self._gross_mass

    @gross_mass.setter
    def gross_mass(self, gross_mass):
        r"""Sets the gross_mass of this VehicleLicenseback.

        总质量。 

        :param gross_mass: The gross_mass of this VehicleLicenseback.
        :type gross_mass: str
        """
        self._gross_mass = gross_mass

    @property
    def unladen_mass(self):
        r"""Gets the unladen_mass of this VehicleLicenseback.

        整备质量。 

        :return: The unladen_mass of this VehicleLicenseback.
        :rtype: str
        """
        return self._unladen_mass

    @unladen_mass.setter
    def unladen_mass(self, unladen_mass):
        r"""Sets the unladen_mass of this VehicleLicenseback.

        整备质量。 

        :param unladen_mass: The unladen_mass of this VehicleLicenseback.
        :type unladen_mass: str
        """
        self._unladen_mass = unladen_mass

    @property
    def approved_load(self):
        r"""Gets the approved_load of this VehicleLicenseback.

        核定载质量。 

        :return: The approved_load of this VehicleLicenseback.
        :rtype: str
        """
        return self._approved_load

    @approved_load.setter
    def approved_load(self, approved_load):
        r"""Sets the approved_load of this VehicleLicenseback.

        核定载质量。 

        :param approved_load: The approved_load of this VehicleLicenseback.
        :type approved_load: str
        """
        self._approved_load = approved_load

    @property
    def dimension(self):
        r"""Gets the dimension of this VehicleLicenseback.

        外廓尺寸。 

        :return: The dimension of this VehicleLicenseback.
        :rtype: str
        """
        return self._dimension

    @dimension.setter
    def dimension(self, dimension):
        r"""Sets the dimension of this VehicleLicenseback.

        外廓尺寸。 

        :param dimension: The dimension of this VehicleLicenseback.
        :type dimension: str
        """
        self._dimension = dimension

    @property
    def traction_mass(self):
        r"""Gets the traction_mass of this VehicleLicenseback.

        准牵引总质量。 

        :return: The traction_mass of this VehicleLicenseback.
        :rtype: str
        """
        return self._traction_mass

    @traction_mass.setter
    def traction_mass(self, traction_mass):
        r"""Sets the traction_mass of this VehicleLicenseback.

        准牵引总质量。 

        :param traction_mass: The traction_mass of this VehicleLicenseback.
        :type traction_mass: str
        """
        self._traction_mass = traction_mass

    @property
    def remarks(self):
        r"""Gets the remarks of this VehicleLicenseback.

        备注。 

        :return: The remarks of this VehicleLicenseback.
        :rtype: str
        """
        return self._remarks

    @remarks.setter
    def remarks(self, remarks):
        r"""Sets the remarks of this VehicleLicenseback.

        备注。 

        :param remarks: The remarks of this VehicleLicenseback.
        :type remarks: str
        """
        self._remarks = remarks

    @property
    def inspection_record(self):
        r"""Gets the inspection_record of this VehicleLicenseback.

        检验记录。 

        :return: The inspection_record of this VehicleLicenseback.
        :rtype: str
        """
        return self._inspection_record

    @inspection_record.setter
    def inspection_record(self, inspection_record):
        r"""Sets the inspection_record of this VehicleLicenseback.

        检验记录。 

        :param inspection_record: The inspection_record of this VehicleLicenseback.
        :type inspection_record: str
        """
        self._inspection_record = inspection_record

    @property
    def code_number(self):
        r"""Gets the code_number of this VehicleLicenseback.

        条码号。           

        :return: The code_number of this VehicleLicenseback.
        :rtype: str
        """
        return self._code_number

    @code_number.setter
    def code_number(self, code_number):
        r"""Sets the code_number of this VehicleLicenseback.

        条码号。           

        :param code_number: The code_number of this VehicleLicenseback.
        :type code_number: str
        """
        self._code_number = code_number

    @property
    def energy_type(self):
        r"""Gets the energy_type of this VehicleLicenseback.

        能源类型。 

        :return: The energy_type of this VehicleLicenseback.
        :rtype: str
        """
        return self._energy_type

    @energy_type.setter
    def energy_type(self, energy_type):
        r"""Sets the energy_type of this VehicleLicenseback.

        能源类型。 

        :param energy_type: The energy_type of this VehicleLicenseback.
        :type energy_type: str
        """
        self._energy_type = energy_type

    @property
    def text_location(self):
        r"""Gets the text_location of this VehicleLicenseback.

        文本框在原图位置。输出左上、右上、右下、左下四个点坐标。  当“return_text_location”设置为“true”时才返回。 

        :return: The text_location of this VehicleLicenseback.
        :rtype: object
        """
        return self._text_location

    @text_location.setter
    def text_location(self, text_location):
        r"""Sets the text_location of this VehicleLicenseback.

        文本框在原图位置。输出左上、右上、右下、左下四个点坐标。  当“return_text_location”设置为“true”时才返回。 

        :param text_location: The text_location of this VehicleLicenseback.
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
        if not isinstance(other, VehicleLicenseback):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
