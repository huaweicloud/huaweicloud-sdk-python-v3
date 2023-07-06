# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HostGroupItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'group_id': 'str',
        'group_name': 'str',
        'host_num': 'int',
        'risk_host_num': 'int',
        'unprotect_host_num': 'int',
        'host_id_list': 'list[str]',
        'is_outside': 'bool'
    }

    attribute_map = {
        'group_id': 'group_id',
        'group_name': 'group_name',
        'host_num': 'host_num',
        'risk_host_num': 'risk_host_num',
        'unprotect_host_num': 'unprotect_host_num',
        'host_id_list': 'host_id_list',
        'is_outside': 'is_outside'
    }

    def __init__(self, group_id=None, group_name=None, host_num=None, risk_host_num=None, unprotect_host_num=None, host_id_list=None, is_outside=None):
        """HostGroupItem

        The model defined in huaweicloud sdk

        :param group_id: 服务器组ID
        :type group_id: str
        :param group_name: 服务器组名称
        :type group_name: str
        :param host_num: 关联服务器数
        :type host_num: int
        :param risk_host_num: 有风险服务器数
        :type risk_host_num: int
        :param unprotect_host_num: 未防护服务器数
        :type unprotect_host_num: int
        :param host_id_list: 服务器ID列表
        :type host_id_list: list[str]
        :param is_outside: 是否是线下数据中心服务器组
        :type is_outside: bool
        """
        
        

        self._group_id = None
        self._group_name = None
        self._host_num = None
        self._risk_host_num = None
        self._unprotect_host_num = None
        self._host_id_list = None
        self._is_outside = None
        self.discriminator = None

        if group_id is not None:
            self.group_id = group_id
        if group_name is not None:
            self.group_name = group_name
        if host_num is not None:
            self.host_num = host_num
        if risk_host_num is not None:
            self.risk_host_num = risk_host_num
        if unprotect_host_num is not None:
            self.unprotect_host_num = unprotect_host_num
        if host_id_list is not None:
            self.host_id_list = host_id_list
        if is_outside is not None:
            self.is_outside = is_outside

    @property
    def group_id(self):
        """Gets the group_id of this HostGroupItem.

        服务器组ID

        :return: The group_id of this HostGroupItem.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this HostGroupItem.

        服务器组ID

        :param group_id: The group_id of this HostGroupItem.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def group_name(self):
        """Gets the group_name of this HostGroupItem.

        服务器组名称

        :return: The group_name of this HostGroupItem.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        """Sets the group_name of this HostGroupItem.

        服务器组名称

        :param group_name: The group_name of this HostGroupItem.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def host_num(self):
        """Gets the host_num of this HostGroupItem.

        关联服务器数

        :return: The host_num of this HostGroupItem.
        :rtype: int
        """
        return self._host_num

    @host_num.setter
    def host_num(self, host_num):
        """Sets the host_num of this HostGroupItem.

        关联服务器数

        :param host_num: The host_num of this HostGroupItem.
        :type host_num: int
        """
        self._host_num = host_num

    @property
    def risk_host_num(self):
        """Gets the risk_host_num of this HostGroupItem.

        有风险服务器数

        :return: The risk_host_num of this HostGroupItem.
        :rtype: int
        """
        return self._risk_host_num

    @risk_host_num.setter
    def risk_host_num(self, risk_host_num):
        """Sets the risk_host_num of this HostGroupItem.

        有风险服务器数

        :param risk_host_num: The risk_host_num of this HostGroupItem.
        :type risk_host_num: int
        """
        self._risk_host_num = risk_host_num

    @property
    def unprotect_host_num(self):
        """Gets the unprotect_host_num of this HostGroupItem.

        未防护服务器数

        :return: The unprotect_host_num of this HostGroupItem.
        :rtype: int
        """
        return self._unprotect_host_num

    @unprotect_host_num.setter
    def unprotect_host_num(self, unprotect_host_num):
        """Sets the unprotect_host_num of this HostGroupItem.

        未防护服务器数

        :param unprotect_host_num: The unprotect_host_num of this HostGroupItem.
        :type unprotect_host_num: int
        """
        self._unprotect_host_num = unprotect_host_num

    @property
    def host_id_list(self):
        """Gets the host_id_list of this HostGroupItem.

        服务器ID列表

        :return: The host_id_list of this HostGroupItem.
        :rtype: list[str]
        """
        return self._host_id_list

    @host_id_list.setter
    def host_id_list(self, host_id_list):
        """Sets the host_id_list of this HostGroupItem.

        服务器ID列表

        :param host_id_list: The host_id_list of this HostGroupItem.
        :type host_id_list: list[str]
        """
        self._host_id_list = host_id_list

    @property
    def is_outside(self):
        """Gets the is_outside of this HostGroupItem.

        是否是线下数据中心服务器组

        :return: The is_outside of this HostGroupItem.
        :rtype: bool
        """
        return self._is_outside

    @is_outside.setter
    def is_outside(self, is_outside):
        """Sets the is_outside of this HostGroupItem.

        是否是线下数据中心服务器组

        :param is_outside: The is_outside of this HostGroupItem.
        :type is_outside: bool
        """
        self._is_outside = is_outside

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
        if not isinstance(other, HostGroupItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
