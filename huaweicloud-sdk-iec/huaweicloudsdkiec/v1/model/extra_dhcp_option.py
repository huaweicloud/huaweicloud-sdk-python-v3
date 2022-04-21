# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExtraDhcpOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'opt_name': 'str',
        'opt_value': 'str'
    }

    attribute_map = {
        'opt_name': 'opt_name',
        'opt_value': 'opt_value'
    }

    def __init__(self, opt_name=None, opt_value=None):
        """ExtraDhcpOption

        The model defined in huaweicloud sdk

        :param opt_name: Option名称
        :type opt_name: str
        :param opt_value: Option值
        :type opt_value: str
        """
        
        

        self._opt_name = None
        self._opt_value = None
        self.discriminator = None

        if opt_name is not None:
            self.opt_name = opt_name
        if opt_value is not None:
            self.opt_value = opt_value

    @property
    def opt_name(self):
        """Gets the opt_name of this ExtraDhcpOption.

        Option名称

        :return: The opt_name of this ExtraDhcpOption.
        :rtype: str
        """
        return self._opt_name

    @opt_name.setter
    def opt_name(self, opt_name):
        """Sets the opt_name of this ExtraDhcpOption.

        Option名称

        :param opt_name: The opt_name of this ExtraDhcpOption.
        :type opt_name: str
        """
        self._opt_name = opt_name

    @property
    def opt_value(self):
        """Gets the opt_value of this ExtraDhcpOption.

        Option值

        :return: The opt_value of this ExtraDhcpOption.
        :rtype: str
        """
        return self._opt_value

    @opt_value.setter
    def opt_value(self, opt_value):
        """Sets the opt_value of this ExtraDhcpOption.

        Option值

        :param opt_value: The opt_value of this ExtraDhcpOption.
        :type opt_value: str
        """
        self._opt_value = opt_value

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
        if not isinstance(other, ExtraDhcpOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
