# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProxyInfoNodes:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'status': 'str',
        'role': 'str',
        'az_code': 'str',
        'frozen_flag': 'int'
    }

    attribute_map = {
        'id': 'id',
        'status': 'status',
        'role': 'role',
        'az_code': 'az_code',
        'frozen_flag': 'frozen_flag'
    }

    def __init__(self, id=None, status=None, role=None, az_code=None, frozen_flag=None):
        r"""ProxyInfoNodes

        The model defined in huaweicloud sdk

        :param id: 数据库代理节点ID。
        :type id: str
        :param status: 数据库代理节点状态。  取值范围： NORMAL: 表示节点正常。 ABNORMAL: 表示节点节点状态异常。 CREATING: 表示节点正在创建中。 CREATEFAIL: 表示节点创建失败。
        :type status: str
        :param role: 数据库代理节点角色：  master：主节点。  slave：备节点。
        :type role: str
        :param az_code: 数据库代理节点所在可用区。
        :type az_code: str
        :param frozen_flag: 数据库代理节点是否被冻结。  取值范围：  0：未冻结。  1：冻结。
        :type frozen_flag: int
        """
        
        

        self._id = None
        self._status = None
        self._role = None
        self._az_code = None
        self._frozen_flag = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if status is not None:
            self.status = status
        if role is not None:
            self.role = role
        if az_code is not None:
            self.az_code = az_code
        if frozen_flag is not None:
            self.frozen_flag = frozen_flag

    @property
    def id(self):
        r"""Gets the id of this ProxyInfoNodes.

        数据库代理节点ID。

        :return: The id of this ProxyInfoNodes.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ProxyInfoNodes.

        数据库代理节点ID。

        :param id: The id of this ProxyInfoNodes.
        :type id: str
        """
        self._id = id

    @property
    def status(self):
        r"""Gets the status of this ProxyInfoNodes.

        数据库代理节点状态。  取值范围： NORMAL: 表示节点正常。 ABNORMAL: 表示节点节点状态异常。 CREATING: 表示节点正在创建中。 CREATEFAIL: 表示节点创建失败。

        :return: The status of this ProxyInfoNodes.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ProxyInfoNodes.

        数据库代理节点状态。  取值范围： NORMAL: 表示节点正常。 ABNORMAL: 表示节点节点状态异常。 CREATING: 表示节点正在创建中。 CREATEFAIL: 表示节点创建失败。

        :param status: The status of this ProxyInfoNodes.
        :type status: str
        """
        self._status = status

    @property
    def role(self):
        r"""Gets the role of this ProxyInfoNodes.

        数据库代理节点角色：  master：主节点。  slave：备节点。

        :return: The role of this ProxyInfoNodes.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        r"""Sets the role of this ProxyInfoNodes.

        数据库代理节点角色：  master：主节点。  slave：备节点。

        :param role: The role of this ProxyInfoNodes.
        :type role: str
        """
        self._role = role

    @property
    def az_code(self):
        r"""Gets the az_code of this ProxyInfoNodes.

        数据库代理节点所在可用区。

        :return: The az_code of this ProxyInfoNodes.
        :rtype: str
        """
        return self._az_code

    @az_code.setter
    def az_code(self, az_code):
        r"""Sets the az_code of this ProxyInfoNodes.

        数据库代理节点所在可用区。

        :param az_code: The az_code of this ProxyInfoNodes.
        :type az_code: str
        """
        self._az_code = az_code

    @property
    def frozen_flag(self):
        r"""Gets the frozen_flag of this ProxyInfoNodes.

        数据库代理节点是否被冻结。  取值范围：  0：未冻结。  1：冻结。

        :return: The frozen_flag of this ProxyInfoNodes.
        :rtype: int
        """
        return self._frozen_flag

    @frozen_flag.setter
    def frozen_flag(self, frozen_flag):
        r"""Sets the frozen_flag of this ProxyInfoNodes.

        数据库代理节点是否被冻结。  取值范围：  0：未冻结。  1：冻结。

        :param frozen_flag: The frozen_flag of this ProxyInfoNodes.
        :type frozen_flag: int
        """
        self._frozen_flag = frozen_flag

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
        if not isinstance(other, ProxyInfoNodes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
