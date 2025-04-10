# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DriverLicenseBack:

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
        'issuing_authority': 'str',
        'address': 'str',
        'file_number': 'str',
        'record': 'str',
        'text_location': 'object'
    }

    attribute_map = {
        'type': 'type',
        'number': 'number',
        'name': 'name',
        'issuing_authority': 'issuing_authority',
        'address': 'address',
        'file_number': 'file_number',
        'record': 'record',
        'text_location': 'text_location'
    }

    def __init__(self, type=None, number=None, name=None, issuing_authority=None, address=None, file_number=None, record=None, text_location=None):
        r"""DriverLicenseBack

        The model defined in huaweicloud sdk

        :param type: 驾驶证类型。 normal：纸质驾驶证 electronic：电子驾驶证 
        :type type: str
        :param number: 驾驶证号。 
        :type number: str
        :param name: 姓名。 
        :type name: str
        :param issuing_authority: 发证机关。 
        :type issuing_authority: str
        :param address: 住址。 
        :type address: str
        :param file_number: 档案编号。 &gt; 说明：当驾驶证类型为纸质驾驶证时才返回。 
        :type file_number: str
        :param record: 记录。 
        :type record: str
        :param text_location: 对应所有在原图上识别到的字段位置信息，包含所有文字区域四个顶点的二维坐标（x,y）。采用图像坐标系，坐标原点为图片左上角，x轴沿水平方向，y轴沿竖直方向。 
        :type text_location: object
        """
        
        

        self._type = None
        self._number = None
        self._name = None
        self._issuing_authority = None
        self._address = None
        self._file_number = None
        self._record = None
        self._text_location = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if number is not None:
            self.number = number
        if name is not None:
            self.name = name
        if issuing_authority is not None:
            self.issuing_authority = issuing_authority
        if address is not None:
            self.address = address
        if file_number is not None:
            self.file_number = file_number
        if record is not None:
            self.record = record
        if text_location is not None:
            self.text_location = text_location

    @property
    def type(self):
        r"""Gets the type of this DriverLicenseBack.

        驾驶证类型。 normal：纸质驾驶证 electronic：电子驾驶证 

        :return: The type of this DriverLicenseBack.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this DriverLicenseBack.

        驾驶证类型。 normal：纸质驾驶证 electronic：电子驾驶证 

        :param type: The type of this DriverLicenseBack.
        :type type: str
        """
        self._type = type

    @property
    def number(self):
        r"""Gets the number of this DriverLicenseBack.

        驾驶证号。 

        :return: The number of this DriverLicenseBack.
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        r"""Sets the number of this DriverLicenseBack.

        驾驶证号。 

        :param number: The number of this DriverLicenseBack.
        :type number: str
        """
        self._number = number

    @property
    def name(self):
        r"""Gets the name of this DriverLicenseBack.

        姓名。 

        :return: The name of this DriverLicenseBack.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this DriverLicenseBack.

        姓名。 

        :param name: The name of this DriverLicenseBack.
        :type name: str
        """
        self._name = name

    @property
    def issuing_authority(self):
        r"""Gets the issuing_authority of this DriverLicenseBack.

        发证机关。 

        :return: The issuing_authority of this DriverLicenseBack.
        :rtype: str
        """
        return self._issuing_authority

    @issuing_authority.setter
    def issuing_authority(self, issuing_authority):
        r"""Sets the issuing_authority of this DriverLicenseBack.

        发证机关。 

        :param issuing_authority: The issuing_authority of this DriverLicenseBack.
        :type issuing_authority: str
        """
        self._issuing_authority = issuing_authority

    @property
    def address(self):
        r"""Gets the address of this DriverLicenseBack.

        住址。 

        :return: The address of this DriverLicenseBack.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        r"""Sets the address of this DriverLicenseBack.

        住址。 

        :param address: The address of this DriverLicenseBack.
        :type address: str
        """
        self._address = address

    @property
    def file_number(self):
        r"""Gets the file_number of this DriverLicenseBack.

        档案编号。 > 说明：当驾驶证类型为纸质驾驶证时才返回。 

        :return: The file_number of this DriverLicenseBack.
        :rtype: str
        """
        return self._file_number

    @file_number.setter
    def file_number(self, file_number):
        r"""Sets the file_number of this DriverLicenseBack.

        档案编号。 > 说明：当驾驶证类型为纸质驾驶证时才返回。 

        :param file_number: The file_number of this DriverLicenseBack.
        :type file_number: str
        """
        self._file_number = file_number

    @property
    def record(self):
        r"""Gets the record of this DriverLicenseBack.

        记录。 

        :return: The record of this DriverLicenseBack.
        :rtype: str
        """
        return self._record

    @record.setter
    def record(self, record):
        r"""Sets the record of this DriverLicenseBack.

        记录。 

        :param record: The record of this DriverLicenseBack.
        :type record: str
        """
        self._record = record

    @property
    def text_location(self):
        r"""Gets the text_location of this DriverLicenseBack.

        对应所有在原图上识别到的字段位置信息，包含所有文字区域四个顶点的二维坐标（x,y）。采用图像坐标系，坐标原点为图片左上角，x轴沿水平方向，y轴沿竖直方向。 

        :return: The text_location of this DriverLicenseBack.
        :rtype: object
        """
        return self._text_location

    @text_location.setter
    def text_location(self, text_location):
        r"""Sets the text_location of this DriverLicenseBack.

        对应所有在原图上识别到的字段位置信息，包含所有文字区域四个顶点的二维坐标（x,y）。采用图像坐标系，坐标原点为图片左上角，x轴沿水平方向，y轴沿竖直方向。 

        :param text_location: The text_location of this DriverLicenseBack.
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
        if not isinstance(other, DriverLicenseBack):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
