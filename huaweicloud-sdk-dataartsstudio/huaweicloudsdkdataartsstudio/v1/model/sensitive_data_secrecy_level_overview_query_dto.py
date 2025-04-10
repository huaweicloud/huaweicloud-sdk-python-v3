# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SensitiveDataSecrecyLevelOverviewQueryDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'secrecy_level_id': 'str',
        'secrecy_level_name': 'str',
        'secrecy_level_number': 'int',
        'count': 'int'
    }

    attribute_map = {
        'secrecy_level_id': 'secrecy_level_id',
        'secrecy_level_name': 'secrecy_level_name',
        'secrecy_level_number': 'secrecy_level_number',
        'count': 'count'
    }

    def __init__(self, secrecy_level_id=None, secrecy_level_name=None, secrecy_level_number=None, count=None):
        r"""SensitiveDataSecrecyLevelOverviewQueryDTO

        The model defined in huaweicloud sdk

        :param secrecy_level_id: 密级ID
        :type secrecy_level_id: str
        :param secrecy_level_name: 密级名称
        :type secrecy_level_name: str
        :param secrecy_level_number: 密级的等级
        :type secrecy_level_number: int
        :param count: 当前密级下的敏感字段数量
        :type count: int
        """
        
        

        self._secrecy_level_id = None
        self._secrecy_level_name = None
        self._secrecy_level_number = None
        self._count = None
        self.discriminator = None

        if secrecy_level_id is not None:
            self.secrecy_level_id = secrecy_level_id
        if secrecy_level_name is not None:
            self.secrecy_level_name = secrecy_level_name
        if secrecy_level_number is not None:
            self.secrecy_level_number = secrecy_level_number
        if count is not None:
            self.count = count

    @property
    def secrecy_level_id(self):
        r"""Gets the secrecy_level_id of this SensitiveDataSecrecyLevelOverviewQueryDTO.

        密级ID

        :return: The secrecy_level_id of this SensitiveDataSecrecyLevelOverviewQueryDTO.
        :rtype: str
        """
        return self._secrecy_level_id

    @secrecy_level_id.setter
    def secrecy_level_id(self, secrecy_level_id):
        r"""Sets the secrecy_level_id of this SensitiveDataSecrecyLevelOverviewQueryDTO.

        密级ID

        :param secrecy_level_id: The secrecy_level_id of this SensitiveDataSecrecyLevelOverviewQueryDTO.
        :type secrecy_level_id: str
        """
        self._secrecy_level_id = secrecy_level_id

    @property
    def secrecy_level_name(self):
        r"""Gets the secrecy_level_name of this SensitiveDataSecrecyLevelOverviewQueryDTO.

        密级名称

        :return: The secrecy_level_name of this SensitiveDataSecrecyLevelOverviewQueryDTO.
        :rtype: str
        """
        return self._secrecy_level_name

    @secrecy_level_name.setter
    def secrecy_level_name(self, secrecy_level_name):
        r"""Sets the secrecy_level_name of this SensitiveDataSecrecyLevelOverviewQueryDTO.

        密级名称

        :param secrecy_level_name: The secrecy_level_name of this SensitiveDataSecrecyLevelOverviewQueryDTO.
        :type secrecy_level_name: str
        """
        self._secrecy_level_name = secrecy_level_name

    @property
    def secrecy_level_number(self):
        r"""Gets the secrecy_level_number of this SensitiveDataSecrecyLevelOverviewQueryDTO.

        密级的等级

        :return: The secrecy_level_number of this SensitiveDataSecrecyLevelOverviewQueryDTO.
        :rtype: int
        """
        return self._secrecy_level_number

    @secrecy_level_number.setter
    def secrecy_level_number(self, secrecy_level_number):
        r"""Sets the secrecy_level_number of this SensitiveDataSecrecyLevelOverviewQueryDTO.

        密级的等级

        :param secrecy_level_number: The secrecy_level_number of this SensitiveDataSecrecyLevelOverviewQueryDTO.
        :type secrecy_level_number: int
        """
        self._secrecy_level_number = secrecy_level_number

    @property
    def count(self):
        r"""Gets the count of this SensitiveDataSecrecyLevelOverviewQueryDTO.

        当前密级下的敏感字段数量

        :return: The count of this SensitiveDataSecrecyLevelOverviewQueryDTO.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this SensitiveDataSecrecyLevelOverviewQueryDTO.

        当前密级下的敏感字段数量

        :param count: The count of this SensitiveDataSecrecyLevelOverviewQueryDTO.
        :type count: int
        """
        self._count = count

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
        if not isinstance(other, SensitiveDataSecrecyLevelOverviewQueryDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
