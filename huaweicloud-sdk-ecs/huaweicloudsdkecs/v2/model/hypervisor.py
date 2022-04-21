# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Hypervisor:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'hypervisor_type': 'str',
        'csd_hypervisor': 'str'
    }

    attribute_map = {
        'hypervisor_type': 'hypervisor_type',
        'csd_hypervisor': 'csd_hypervisor'
    }

    def __init__(self, hypervisor_type=None, csd_hypervisor=None):
        """Hypervisor

        The model defined in huaweicloud sdk

        :param hypervisor_type: hypervisor类型
        :type hypervisor_type: str
        :param csd_hypervisor: hypervisor csd信息
        :type csd_hypervisor: str
        """
        
        

        self._hypervisor_type = None
        self._csd_hypervisor = None
        self.discriminator = None

        if hypervisor_type is not None:
            self.hypervisor_type = hypervisor_type
        if csd_hypervisor is not None:
            self.csd_hypervisor = csd_hypervisor

    @property
    def hypervisor_type(self):
        """Gets the hypervisor_type of this Hypervisor.

        hypervisor类型

        :return: The hypervisor_type of this Hypervisor.
        :rtype: str
        """
        return self._hypervisor_type

    @hypervisor_type.setter
    def hypervisor_type(self, hypervisor_type):
        """Sets the hypervisor_type of this Hypervisor.

        hypervisor类型

        :param hypervisor_type: The hypervisor_type of this Hypervisor.
        :type hypervisor_type: str
        """
        self._hypervisor_type = hypervisor_type

    @property
    def csd_hypervisor(self):
        """Gets the csd_hypervisor of this Hypervisor.

        hypervisor csd信息

        :return: The csd_hypervisor of this Hypervisor.
        :rtype: str
        """
        return self._csd_hypervisor

    @csd_hypervisor.setter
    def csd_hypervisor(self, csd_hypervisor):
        """Sets the csd_hypervisor of this Hypervisor.

        hypervisor csd信息

        :param csd_hypervisor: The csd_hypervisor of this Hypervisor.
        :type csd_hypervisor: str
        """
        self._csd_hypervisor = csd_hypervisor

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
        if not isinstance(other, Hypervisor):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
