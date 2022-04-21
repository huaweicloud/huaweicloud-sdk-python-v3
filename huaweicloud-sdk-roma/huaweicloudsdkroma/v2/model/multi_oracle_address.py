# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MultiOracleAddress:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'oracle_address': 'str',
        'oracle_port': 'str'
    }

    attribute_map = {
        'oracle_address': 'oracle_address',
        'oracle_port': 'oracle_port'
    }

    def __init__(self, oracle_address=None, oracle_port=None):
        """MultiOracleAddress

        The model defined in huaweicloud sdk

        :param oracle_address: ORACLE地址
        :type oracle_address: str
        :param oracle_port: ORACLE端口
        :type oracle_port: str
        """
        
        

        self._oracle_address = None
        self._oracle_port = None
        self.discriminator = None

        if oracle_address is not None:
            self.oracle_address = oracle_address
        if oracle_port is not None:
            self.oracle_port = oracle_port

    @property
    def oracle_address(self):
        """Gets the oracle_address of this MultiOracleAddress.

        ORACLE地址

        :return: The oracle_address of this MultiOracleAddress.
        :rtype: str
        """
        return self._oracle_address

    @oracle_address.setter
    def oracle_address(self, oracle_address):
        """Sets the oracle_address of this MultiOracleAddress.

        ORACLE地址

        :param oracle_address: The oracle_address of this MultiOracleAddress.
        :type oracle_address: str
        """
        self._oracle_address = oracle_address

    @property
    def oracle_port(self):
        """Gets the oracle_port of this MultiOracleAddress.

        ORACLE端口

        :return: The oracle_port of this MultiOracleAddress.
        :rtype: str
        """
        return self._oracle_port

    @oracle_port.setter
    def oracle_port(self, oracle_port):
        """Sets the oracle_port of this MultiOracleAddress.

        ORACLE端口

        :param oracle_port: The oracle_port of this MultiOracleAddress.
        :type oracle_port: str
        """
        self._oracle_port = oracle_port

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
        if not isinstance(other, MultiOracleAddress):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
