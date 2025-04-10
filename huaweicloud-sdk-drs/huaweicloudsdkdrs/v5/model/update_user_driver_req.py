# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateUserDriverReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'driver_name': 'str',
        'driver_type': 'str'
    }

    attribute_map = {
        'driver_name': 'driver_name',
        'driver_type': 'driver_type'
    }

    def __init__(self, driver_name=None, driver_type=None):
        r"""UpdateUserDriverReq

        The model defined in huaweicloud sdk

        :param driver_name: JDBC驱动文件名称，name的长度5-64，结尾以.jar结尾。
        :type driver_name: str
        :param driver_type: 指定待同步的驱动文件类型。取值范围： - db2：DB2 for LUW - informix：Informix
        :type driver_type: str
        """
        
        

        self._driver_name = None
        self._driver_type = None
        self.discriminator = None

        self.driver_name = driver_name
        self.driver_type = driver_type

    @property
    def driver_name(self):
        r"""Gets the driver_name of this UpdateUserDriverReq.

        JDBC驱动文件名称，name的长度5-64，结尾以.jar结尾。

        :return: The driver_name of this UpdateUserDriverReq.
        :rtype: str
        """
        return self._driver_name

    @driver_name.setter
    def driver_name(self, driver_name):
        r"""Sets the driver_name of this UpdateUserDriverReq.

        JDBC驱动文件名称，name的长度5-64，结尾以.jar结尾。

        :param driver_name: The driver_name of this UpdateUserDriverReq.
        :type driver_name: str
        """
        self._driver_name = driver_name

    @property
    def driver_type(self):
        r"""Gets the driver_type of this UpdateUserDriverReq.

        指定待同步的驱动文件类型。取值范围： - db2：DB2 for LUW - informix：Informix

        :return: The driver_type of this UpdateUserDriverReq.
        :rtype: str
        """
        return self._driver_type

    @driver_type.setter
    def driver_type(self, driver_type):
        r"""Sets the driver_type of this UpdateUserDriverReq.

        指定待同步的驱动文件类型。取值范围： - db2：DB2 for LUW - informix：Informix

        :param driver_type: The driver_type of this UpdateUserDriverReq.
        :type driver_type: str
        """
        self._driver_type = driver_type

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
        if not isinstance(other, UpdateUserDriverReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
