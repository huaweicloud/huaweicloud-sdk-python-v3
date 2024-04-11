# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RollUpgradeProgress:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'upgraded_dn_group_numbers': 'str',
        'total_dn_group_numbers': 'str',
        'not_fully_upgraded_az': 'str',
        'already_upgraded_az': 'str',
        'az_description_map': 'dict(str, str)'
    }

    attribute_map = {
        'upgraded_dn_group_numbers': 'upgraded_dn_group_numbers',
        'total_dn_group_numbers': 'total_dn_group_numbers',
        'not_fully_upgraded_az': 'not_fully_upgraded_az',
        'already_upgraded_az': 'already_upgraded_az',
        'az_description_map': 'az_description_map'
    }

    def __init__(self, upgraded_dn_group_numbers=None, total_dn_group_numbers=None, not_fully_upgraded_az=None, already_upgraded_az=None, az_description_map=None):
        """RollUpgradeProgress

        The model defined in huaweicloud sdk

        :param upgraded_dn_group_numbers: 已升级分片数，非独立部署返回null
        :type upgraded_dn_group_numbers: str
        :param total_dn_group_numbers: 总分片数，非独立部署返回null
        :type total_dn_group_numbers: str
        :param not_fully_upgraded_az: 未完成升级的az，以“,”隔开，独立部署返回null
        :type not_fully_upgraded_az: str
        :param already_upgraded_az: 已升级az，以“,”隔开，独立部署返回null
        :type already_upgraded_az: str
        :param az_description_map: az描述键值对Map&lt;String,String&gt;
        :type az_description_map: dict(str, str)
        """
        
        

        self._upgraded_dn_group_numbers = None
        self._total_dn_group_numbers = None
        self._not_fully_upgraded_az = None
        self._already_upgraded_az = None
        self._az_description_map = None
        self.discriminator = None

        if upgraded_dn_group_numbers is not None:
            self.upgraded_dn_group_numbers = upgraded_dn_group_numbers
        if total_dn_group_numbers is not None:
            self.total_dn_group_numbers = total_dn_group_numbers
        if not_fully_upgraded_az is not None:
            self.not_fully_upgraded_az = not_fully_upgraded_az
        if already_upgraded_az is not None:
            self.already_upgraded_az = already_upgraded_az
        if az_description_map is not None:
            self.az_description_map = az_description_map

    @property
    def upgraded_dn_group_numbers(self):
        """Gets the upgraded_dn_group_numbers of this RollUpgradeProgress.

        已升级分片数，非独立部署返回null

        :return: The upgraded_dn_group_numbers of this RollUpgradeProgress.
        :rtype: str
        """
        return self._upgraded_dn_group_numbers

    @upgraded_dn_group_numbers.setter
    def upgraded_dn_group_numbers(self, upgraded_dn_group_numbers):
        """Sets the upgraded_dn_group_numbers of this RollUpgradeProgress.

        已升级分片数，非独立部署返回null

        :param upgraded_dn_group_numbers: The upgraded_dn_group_numbers of this RollUpgradeProgress.
        :type upgraded_dn_group_numbers: str
        """
        self._upgraded_dn_group_numbers = upgraded_dn_group_numbers

    @property
    def total_dn_group_numbers(self):
        """Gets the total_dn_group_numbers of this RollUpgradeProgress.

        总分片数，非独立部署返回null

        :return: The total_dn_group_numbers of this RollUpgradeProgress.
        :rtype: str
        """
        return self._total_dn_group_numbers

    @total_dn_group_numbers.setter
    def total_dn_group_numbers(self, total_dn_group_numbers):
        """Sets the total_dn_group_numbers of this RollUpgradeProgress.

        总分片数，非独立部署返回null

        :param total_dn_group_numbers: The total_dn_group_numbers of this RollUpgradeProgress.
        :type total_dn_group_numbers: str
        """
        self._total_dn_group_numbers = total_dn_group_numbers

    @property
    def not_fully_upgraded_az(self):
        """Gets the not_fully_upgraded_az of this RollUpgradeProgress.

        未完成升级的az，以“,”隔开，独立部署返回null

        :return: The not_fully_upgraded_az of this RollUpgradeProgress.
        :rtype: str
        """
        return self._not_fully_upgraded_az

    @not_fully_upgraded_az.setter
    def not_fully_upgraded_az(self, not_fully_upgraded_az):
        """Sets the not_fully_upgraded_az of this RollUpgradeProgress.

        未完成升级的az，以“,”隔开，独立部署返回null

        :param not_fully_upgraded_az: The not_fully_upgraded_az of this RollUpgradeProgress.
        :type not_fully_upgraded_az: str
        """
        self._not_fully_upgraded_az = not_fully_upgraded_az

    @property
    def already_upgraded_az(self):
        """Gets the already_upgraded_az of this RollUpgradeProgress.

        已升级az，以“,”隔开，独立部署返回null

        :return: The already_upgraded_az of this RollUpgradeProgress.
        :rtype: str
        """
        return self._already_upgraded_az

    @already_upgraded_az.setter
    def already_upgraded_az(self, already_upgraded_az):
        """Sets the already_upgraded_az of this RollUpgradeProgress.

        已升级az，以“,”隔开，独立部署返回null

        :param already_upgraded_az: The already_upgraded_az of this RollUpgradeProgress.
        :type already_upgraded_az: str
        """
        self._already_upgraded_az = already_upgraded_az

    @property
    def az_description_map(self):
        """Gets the az_description_map of this RollUpgradeProgress.

        az描述键值对Map<String,String>

        :return: The az_description_map of this RollUpgradeProgress.
        :rtype: dict(str, str)
        """
        return self._az_description_map

    @az_description_map.setter
    def az_description_map(self, az_description_map):
        """Sets the az_description_map of this RollUpgradeProgress.

        az描述键值对Map<String,String>

        :param az_description_map: The az_description_map of this RollUpgradeProgress.
        :type az_description_map: dict(str, str)
        """
        self._az_description_map = az_description_map

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
        if not isinstance(other, RollUpgradeProgress):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
