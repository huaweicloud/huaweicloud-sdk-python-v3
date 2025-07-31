# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OsStatisticsInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'os_name': 'str',
        'os_type': 'str',
        'number': 'int'
    }

    attribute_map = {
        'os_name': 'os_name',
        'os_type': 'os_type',
        'number': 'number'
    }

    def __init__(self, os_name=None, os_type=None, number=None):
        r"""OsStatisticsInfo

        The model defined in huaweicloud sdk

        :param os_name: os_name
        :type os_name: str
        :param os_type: os_type
        :type os_type: str
        :param number: os_number
        :type number: int
        """
        
        

        self._os_name = None
        self._os_type = None
        self._number = None
        self.discriminator = None

        if os_name is not None:
            self.os_name = os_name
        if os_type is not None:
            self.os_type = os_type
        if number is not None:
            self.number = number

    @property
    def os_name(self):
        r"""Gets the os_name of this OsStatisticsInfo.

        os_name

        :return: The os_name of this OsStatisticsInfo.
        :rtype: str
        """
        return self._os_name

    @os_name.setter
    def os_name(self, os_name):
        r"""Sets the os_name of this OsStatisticsInfo.

        os_name

        :param os_name: The os_name of this OsStatisticsInfo.
        :type os_name: str
        """
        self._os_name = os_name

    @property
    def os_type(self):
        r"""Gets the os_type of this OsStatisticsInfo.

        os_type

        :return: The os_type of this OsStatisticsInfo.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        r"""Sets the os_type of this OsStatisticsInfo.

        os_type

        :param os_type: The os_type of this OsStatisticsInfo.
        :type os_type: str
        """
        self._os_type = os_type

    @property
    def number(self):
        r"""Gets the number of this OsStatisticsInfo.

        os_number

        :return: The number of this OsStatisticsInfo.
        :rtype: int
        """
        return self._number

    @number.setter
    def number(self, number):
        r"""Sets the number of this OsStatisticsInfo.

        os_number

        :param number: The number of this OsStatisticsInfo.
        :type number: int
        """
        self._number = number

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
        if not isinstance(other, OsStatisticsInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
