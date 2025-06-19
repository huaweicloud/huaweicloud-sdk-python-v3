# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IpBlacklistImportDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'add_type': 'int',
        'ip_blacklist': 'str',
        'effect_scope': 'list[int]'
    }

    attribute_map = {
        'add_type': 'add_type',
        'ip_blacklist': 'ip_blacklist',
        'effect_scope': 'effect_scope'
    }

    def __init__(self, add_type=None, ip_blacklist=None, effect_scope=None):
        r"""IpBlacklistImportDto

        The model defined in huaweicloud sdk

        :param add_type: IP黑名单导入的方式，0表示增量导入，在原来的基础上追加；1表示全量导入，新导入的IP黑名单会覆盖已有的IP黑名单
        :type add_type: int
        :param ip_blacklist: IP列表，当前支持不同的IP地址之间使用“,” 、“ ”、“;”、“\\r\\n”、“\\n”、“\\t”等分割符进行分割。
        :type ip_blacklist: str
        :param effect_scope: 生效范围，1表示生效范围为eip, 2表示生效范围为nat, [1 2]表示 生效范围为eip和nat
        :type effect_scope: list[int]
        """
        
        

        self._add_type = None
        self._ip_blacklist = None
        self._effect_scope = None
        self.discriminator = None

        if add_type is not None:
            self.add_type = add_type
        if ip_blacklist is not None:
            self.ip_blacklist = ip_blacklist
        if effect_scope is not None:
            self.effect_scope = effect_scope

    @property
    def add_type(self):
        r"""Gets the add_type of this IpBlacklistImportDto.

        IP黑名单导入的方式，0表示增量导入，在原来的基础上追加；1表示全量导入，新导入的IP黑名单会覆盖已有的IP黑名单

        :return: The add_type of this IpBlacklistImportDto.
        :rtype: int
        """
        return self._add_type

    @add_type.setter
    def add_type(self, add_type):
        r"""Sets the add_type of this IpBlacklistImportDto.

        IP黑名单导入的方式，0表示增量导入，在原来的基础上追加；1表示全量导入，新导入的IP黑名单会覆盖已有的IP黑名单

        :param add_type: The add_type of this IpBlacklistImportDto.
        :type add_type: int
        """
        self._add_type = add_type

    @property
    def ip_blacklist(self):
        r"""Gets the ip_blacklist of this IpBlacklistImportDto.

        IP列表，当前支持不同的IP地址之间使用“,” 、“ ”、“;”、“\\r\\n”、“\\n”、“\\t”等分割符进行分割。

        :return: The ip_blacklist of this IpBlacklistImportDto.
        :rtype: str
        """
        return self._ip_blacklist

    @ip_blacklist.setter
    def ip_blacklist(self, ip_blacklist):
        r"""Sets the ip_blacklist of this IpBlacklistImportDto.

        IP列表，当前支持不同的IP地址之间使用“,” 、“ ”、“;”、“\\r\\n”、“\\n”、“\\t”等分割符进行分割。

        :param ip_blacklist: The ip_blacklist of this IpBlacklistImportDto.
        :type ip_blacklist: str
        """
        self._ip_blacklist = ip_blacklist

    @property
    def effect_scope(self):
        r"""Gets the effect_scope of this IpBlacklistImportDto.

        生效范围，1表示生效范围为eip, 2表示生效范围为nat, [1 2]表示 生效范围为eip和nat

        :return: The effect_scope of this IpBlacklistImportDto.
        :rtype: list[int]
        """
        return self._effect_scope

    @effect_scope.setter
    def effect_scope(self, effect_scope):
        r"""Sets the effect_scope of this IpBlacklistImportDto.

        生效范围，1表示生效范围为eip, 2表示生效范围为nat, [1 2]表示 生效范围为eip和nat

        :param effect_scope: The effect_scope of this IpBlacklistImportDto.
        :type effect_scope: list[int]
        """
        self._effect_scope = effect_scope

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
        if not isinstance(other, IpBlacklistImportDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
