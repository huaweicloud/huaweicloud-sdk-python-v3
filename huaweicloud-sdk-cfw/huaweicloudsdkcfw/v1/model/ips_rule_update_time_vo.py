# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IpsRuleUpdateTimeVO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ips_type': 'int',
        'ips_version': 'str',
        'update_time': 'int'
    }

    attribute_map = {
        'ips_type': 'ips_type',
        'ips_version': 'ips_version',
        'update_time': 'update_time'
    }

    def __init__(self, ips_type=None, ips_version=None, update_time=None):
        r"""IpsRuleUpdateTimeVO

        The model defined in huaweicloud sdk

        :param ips_type: 
        :type ips_type: int
        :param ips_version: 
        :type ips_version: str
        :param update_time: 
        :type update_time: int
        """
        
        

        self._ips_type = None
        self._ips_version = None
        self._update_time = None
        self.discriminator = None

        if ips_type is not None:
            self.ips_type = ips_type
        if ips_version is not None:
            self.ips_version = ips_version
        if update_time is not None:
            self.update_time = update_time

    @property
    def ips_type(self):
        r"""Gets the ips_type of this IpsRuleUpdateTimeVO.

        :return: The ips_type of this IpsRuleUpdateTimeVO.
        :rtype: int
        """
        return self._ips_type

    @ips_type.setter
    def ips_type(self, ips_type):
        r"""Sets the ips_type of this IpsRuleUpdateTimeVO.

        :param ips_type: The ips_type of this IpsRuleUpdateTimeVO.
        :type ips_type: int
        """
        self._ips_type = ips_type

    @property
    def ips_version(self):
        r"""Gets the ips_version of this IpsRuleUpdateTimeVO.

        :return: The ips_version of this IpsRuleUpdateTimeVO.
        :rtype: str
        """
        return self._ips_version

    @ips_version.setter
    def ips_version(self, ips_version):
        r"""Sets the ips_version of this IpsRuleUpdateTimeVO.

        :param ips_version: The ips_version of this IpsRuleUpdateTimeVO.
        :type ips_version: str
        """
        self._ips_version = ips_version

    @property
    def update_time(self):
        r"""Gets the update_time of this IpsRuleUpdateTimeVO.

        :return: The update_time of this IpsRuleUpdateTimeVO.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this IpsRuleUpdateTimeVO.

        :param update_time: The update_time of this IpsRuleUpdateTimeVO.
        :type update_time: int
        """
        self._update_time = update_time

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
        if not isinstance(other, IpsRuleUpdateTimeVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
