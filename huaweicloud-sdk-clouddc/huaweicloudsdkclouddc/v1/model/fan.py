# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Fan:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'model': 'str',
        'reading': 'str',
        'reading_units': 'str',
        'part_number': 'str',
        'speed_ratio': 'str',
        'status': 'Status'
    }

    attribute_map = {
        'name': 'name',
        'model': 'model',
        'reading': 'reading',
        'reading_units': 'reading_units',
        'part_number': 'part_number',
        'speed_ratio': 'speed_ratio',
        'status': 'status'
    }

    def __init__(self, name=None, model=None, reading=None, reading_units=None, part_number=None, speed_ratio=None, status=None):
        r"""Fan

        The model defined in huaweicloud sdk

        :param name: 名称
        :type name: str
        :param model: 型号
        :type model: str
        :param reading: 转速
        :type reading: str
        :param reading_units: 转速单位
        :type reading_units: str
        :param part_number: 固件编码
        :type part_number: str
        :param speed_ratio: 速率比
        :type speed_ratio: str
        :param status: 
        :type status: :class:`huaweicloudsdkclouddc.v1.Status`
        """
        
        

        self._name = None
        self._model = None
        self._reading = None
        self._reading_units = None
        self._part_number = None
        self._speed_ratio = None
        self._status = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if model is not None:
            self.model = model
        if reading is not None:
            self.reading = reading
        if reading_units is not None:
            self.reading_units = reading_units
        if part_number is not None:
            self.part_number = part_number
        if speed_ratio is not None:
            self.speed_ratio = speed_ratio
        if status is not None:
            self.status = status

    @property
    def name(self):
        r"""Gets the name of this Fan.

        名称

        :return: The name of this Fan.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this Fan.

        名称

        :param name: The name of this Fan.
        :type name: str
        """
        self._name = name

    @property
    def model(self):
        r"""Gets the model of this Fan.

        型号

        :return: The model of this Fan.
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        r"""Sets the model of this Fan.

        型号

        :param model: The model of this Fan.
        :type model: str
        """
        self._model = model

    @property
    def reading(self):
        r"""Gets the reading of this Fan.

        转速

        :return: The reading of this Fan.
        :rtype: str
        """
        return self._reading

    @reading.setter
    def reading(self, reading):
        r"""Sets the reading of this Fan.

        转速

        :param reading: The reading of this Fan.
        :type reading: str
        """
        self._reading = reading

    @property
    def reading_units(self):
        r"""Gets the reading_units of this Fan.

        转速单位

        :return: The reading_units of this Fan.
        :rtype: str
        """
        return self._reading_units

    @reading_units.setter
    def reading_units(self, reading_units):
        r"""Sets the reading_units of this Fan.

        转速单位

        :param reading_units: The reading_units of this Fan.
        :type reading_units: str
        """
        self._reading_units = reading_units

    @property
    def part_number(self):
        r"""Gets the part_number of this Fan.

        固件编码

        :return: The part_number of this Fan.
        :rtype: str
        """
        return self._part_number

    @part_number.setter
    def part_number(self, part_number):
        r"""Sets the part_number of this Fan.

        固件编码

        :param part_number: The part_number of this Fan.
        :type part_number: str
        """
        self._part_number = part_number

    @property
    def speed_ratio(self):
        r"""Gets the speed_ratio of this Fan.

        速率比

        :return: The speed_ratio of this Fan.
        :rtype: str
        """
        return self._speed_ratio

    @speed_ratio.setter
    def speed_ratio(self, speed_ratio):
        r"""Sets the speed_ratio of this Fan.

        速率比

        :param speed_ratio: The speed_ratio of this Fan.
        :type speed_ratio: str
        """
        self._speed_ratio = speed_ratio

    @property
    def status(self):
        r"""Gets the status of this Fan.

        :return: The status of this Fan.
        :rtype: :class:`huaweicloudsdkclouddc.v1.Status`
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this Fan.

        :param status: The status of this Fan.
        :type status: :class:`huaweicloudsdkclouddc.v1.Status`
        """
        self._status = status

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
        if not isinstance(other, Fan):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
