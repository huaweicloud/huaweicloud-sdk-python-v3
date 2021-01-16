# coding: utf-8

import pprint
import re

import six





class MeasureUnitRest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'measure_id': 'int',
        'measure_name': 'str',
        'abbreviation': 'str',
        'measure_type': 'int'
    }

    attribute_map = {
        'measure_id': 'measure_id',
        'measure_name': 'measure_name',
        'abbreviation': 'abbreviation',
        'measure_type': 'measure_type'
    }

    def __init__(self, measure_id=None, measure_name=None, abbreviation=None, measure_type=None):
        """MeasureUnitRest - a model defined in huaweicloud sdk"""
        
        

        self._measure_id = None
        self._measure_name = None
        self._abbreviation = None
        self._measure_type = None
        self.discriminator = None

        if measure_id is not None:
            self.measure_id = measure_id
        if measure_name is not None:
            self.measure_name = measure_name
        if abbreviation is not None:
            self.abbreviation = abbreviation
        if measure_type is not None:
            self.measure_type = measure_type

    @property
    def measure_id(self):
        """Gets the measure_id of this MeasureUnitRest.

        |参数名称：度量单位ID| |参数的约束及描述：度量单位ID|

        :return: The measure_id of this MeasureUnitRest.
        :rtype: int
        """
        return self._measure_id

    @measure_id.setter
    def measure_id(self, measure_id):
        """Sets the measure_id of this MeasureUnitRest.

        |参数名称：度量单位ID| |参数的约束及描述：度量单位ID|

        :param measure_id: The measure_id of this MeasureUnitRest.
        :type: int
        """
        self._measure_id = measure_id

    @property
    def measure_name(self):
        """Gets the measure_name of this MeasureUnitRest.

        |参数名称：度量单位名称（默认语言或者要查询语言名称）| |参数约束及描述：度量单位名称（默认语言或者要查询语言名称）|

        :return: The measure_name of this MeasureUnitRest.
        :rtype: str
        """
        return self._measure_name

    @measure_name.setter
    def measure_name(self, measure_name):
        """Sets the measure_name of this MeasureUnitRest.

        |参数名称：度量单位名称（默认语言或者要查询语言名称）| |参数约束及描述：度量单位名称（默认语言或者要查询语言名称）|

        :param measure_name: The measure_name of this MeasureUnitRest.
        :type: str
        """
        self._measure_name = measure_name

    @property
    def abbreviation(self):
        """Gets the abbreviation of this MeasureUnitRest.

        |参数名称：英文缩写| |参数约束及描述：英文缩写|

        :return: The abbreviation of this MeasureUnitRest.
        :rtype: str
        """
        return self._abbreviation

    @abbreviation.setter
    def abbreviation(self, abbreviation):
        """Sets the abbreviation of this MeasureUnitRest.

        |参数名称：英文缩写| |参数约束及描述：英文缩写|

        :param abbreviation: The abbreviation of this MeasureUnitRest.
        :type: str
        """
        self._abbreviation = abbreviation

    @property
    def measure_type(self):
        """Gets the measure_type of this MeasureUnitRest.

        |参数名称：度量类型| |参数的约束及描述：度量类型|

        :return: The measure_type of this MeasureUnitRest.
        :rtype: int
        """
        return self._measure_type

    @measure_type.setter
    def measure_type(self, measure_type):
        """Sets the measure_type of this MeasureUnitRest.

        |参数名称：度量类型| |参数的约束及描述：度量类型|

        :param measure_type: The measure_type of this MeasureUnitRest.
        :type: int
        """
        self._measure_type = measure_type

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
        if not isinstance(other, MeasureUnitRest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
