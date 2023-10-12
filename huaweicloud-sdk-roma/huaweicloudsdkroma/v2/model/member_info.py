# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MemberInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'host': 'str',
        'weight': 'int',
        'is_backup': 'bool',
        'member_group_name': 'str',
        'status': 'int',
        'port': 'int',
        'ecs_id': 'str',
        'ecs_name': 'str'
    }

    attribute_map = {
        'host': 'host',
        'weight': 'weight',
        'is_backup': 'is_backup',
        'member_group_name': 'member_group_name',
        'status': 'status',
        'port': 'port',
        'ecs_id': 'ecs_id',
        'ecs_name': 'ecs_name'
    }

    def __init__(self, host=None, weight=None, is_backup=None, member_group_name=None, status=None, port=None, ecs_id=None, ecs_name=None):
        """MemberInfo

        The model defined in huaweicloud sdk

        :param host: 后端服务器地址  后端实例类型为ip时必填
        :type host: str
        :param weight: 权重值。  允许您对后端服务进行评级，权重值越大，转发到该云服务的请求数量越多。
        :type weight: int
        :param is_backup: 是否备用节点。  开启后对应后端服务为备用节点，仅当非备用节点全部故障时工作。  实例需要升级到对应版本才支持此功能，若不支持请联系技术支持。
        :type is_backup: bool
        :param member_group_name: 后端服务器组名称。为后端服务地址选择服务器组，便于统一修改对应服务器组的后端地址。
        :type member_group_name: str
        :param status: 后端服务器状态   - 1：可用   - 2：不可用
        :type status: int
        :param port: 后端服务器端口
        :type port: int
        :param ecs_id: [后端云服务器的编号。](tag:hws,hws_hk,hcs,hcs_sm,fcs,g42)  [后端实例类型为ecs时必填，支持英文，数字，“-”,“_”，1 ~ 64字符。](tag:hws,hws_hk,hcs,hcs_sm,fcs,g42)  [不支持后端云服务器类型](tag:Site)
        :type ecs_id: str
        :param ecs_name: [后端云服务器的名称。]  [后端实例类型为ecs时必填，支持汉字，英文，数字，“-”,“_”,“.”，1 ~ 64字符。](tag:hws,hws_hk,hcs,hcs_sm,fcs,g42)  [不支持后端云服务器类型](tag:Site)
        :type ecs_name: str
        """
        
        

        self._host = None
        self._weight = None
        self._is_backup = None
        self._member_group_name = None
        self._status = None
        self._port = None
        self._ecs_id = None
        self._ecs_name = None
        self.discriminator = None

        if host is not None:
            self.host = host
        if weight is not None:
            self.weight = weight
        if is_backup is not None:
            self.is_backup = is_backup
        if member_group_name is not None:
            self.member_group_name = member_group_name
        if status is not None:
            self.status = status
        if port is not None:
            self.port = port
        if ecs_id is not None:
            self.ecs_id = ecs_id
        if ecs_name is not None:
            self.ecs_name = ecs_name

    @property
    def host(self):
        """Gets the host of this MemberInfo.

        后端服务器地址  后端实例类型为ip时必填

        :return: The host of this MemberInfo.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this MemberInfo.

        后端服务器地址  后端实例类型为ip时必填

        :param host: The host of this MemberInfo.
        :type host: str
        """
        self._host = host

    @property
    def weight(self):
        """Gets the weight of this MemberInfo.

        权重值。  允许您对后端服务进行评级，权重值越大，转发到该云服务的请求数量越多。

        :return: The weight of this MemberInfo.
        :rtype: int
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this MemberInfo.

        权重值。  允许您对后端服务进行评级，权重值越大，转发到该云服务的请求数量越多。

        :param weight: The weight of this MemberInfo.
        :type weight: int
        """
        self._weight = weight

    @property
    def is_backup(self):
        """Gets the is_backup of this MemberInfo.

        是否备用节点。  开启后对应后端服务为备用节点，仅当非备用节点全部故障时工作。  实例需要升级到对应版本才支持此功能，若不支持请联系技术支持。

        :return: The is_backup of this MemberInfo.
        :rtype: bool
        """
        return self._is_backup

    @is_backup.setter
    def is_backup(self, is_backup):
        """Sets the is_backup of this MemberInfo.

        是否备用节点。  开启后对应后端服务为备用节点，仅当非备用节点全部故障时工作。  实例需要升级到对应版本才支持此功能，若不支持请联系技术支持。

        :param is_backup: The is_backup of this MemberInfo.
        :type is_backup: bool
        """
        self._is_backup = is_backup

    @property
    def member_group_name(self):
        """Gets the member_group_name of this MemberInfo.

        后端服务器组名称。为后端服务地址选择服务器组，便于统一修改对应服务器组的后端地址。

        :return: The member_group_name of this MemberInfo.
        :rtype: str
        """
        return self._member_group_name

    @member_group_name.setter
    def member_group_name(self, member_group_name):
        """Sets the member_group_name of this MemberInfo.

        后端服务器组名称。为后端服务地址选择服务器组，便于统一修改对应服务器组的后端地址。

        :param member_group_name: The member_group_name of this MemberInfo.
        :type member_group_name: str
        """
        self._member_group_name = member_group_name

    @property
    def status(self):
        """Gets the status of this MemberInfo.

        后端服务器状态   - 1：可用   - 2：不可用

        :return: The status of this MemberInfo.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this MemberInfo.

        后端服务器状态   - 1：可用   - 2：不可用

        :param status: The status of this MemberInfo.
        :type status: int
        """
        self._status = status

    @property
    def port(self):
        """Gets the port of this MemberInfo.

        后端服务器端口

        :return: The port of this MemberInfo.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this MemberInfo.

        后端服务器端口

        :param port: The port of this MemberInfo.
        :type port: int
        """
        self._port = port

    @property
    def ecs_id(self):
        """Gets the ecs_id of this MemberInfo.

        [后端云服务器的编号。](tag:hws,hws_hk,hcs,hcs_sm,fcs,g42)  [后端实例类型为ecs时必填，支持英文，数字，“-”,“_”，1 ~ 64字符。](tag:hws,hws_hk,hcs,hcs_sm,fcs,g42)  [不支持后端云服务器类型](tag:Site)

        :return: The ecs_id of this MemberInfo.
        :rtype: str
        """
        return self._ecs_id

    @ecs_id.setter
    def ecs_id(self, ecs_id):
        """Sets the ecs_id of this MemberInfo.

        [后端云服务器的编号。](tag:hws,hws_hk,hcs,hcs_sm,fcs,g42)  [后端实例类型为ecs时必填，支持英文，数字，“-”,“_”，1 ~ 64字符。](tag:hws,hws_hk,hcs,hcs_sm,fcs,g42)  [不支持后端云服务器类型](tag:Site)

        :param ecs_id: The ecs_id of this MemberInfo.
        :type ecs_id: str
        """
        self._ecs_id = ecs_id

    @property
    def ecs_name(self):
        """Gets the ecs_name of this MemberInfo.

        [后端云服务器的名称。]  [后端实例类型为ecs时必填，支持汉字，英文，数字，“-”,“_”,“.”，1 ~ 64字符。](tag:hws,hws_hk,hcs,hcs_sm,fcs,g42)  [不支持后端云服务器类型](tag:Site)

        :return: The ecs_name of this MemberInfo.
        :rtype: str
        """
        return self._ecs_name

    @ecs_name.setter
    def ecs_name(self, ecs_name):
        """Sets the ecs_name of this MemberInfo.

        [后端云服务器的名称。]  [后端实例类型为ecs时必填，支持汉字，英文，数字，“-”,“_”,“.”，1 ~ 64字符。](tag:hws,hws_hk,hcs,hcs_sm,fcs,g42)  [不支持后端云服务器类型](tag:Site)

        :param ecs_name: The ecs_name of this MemberInfo.
        :type ecs_name: str
        """
        self._ecs_name = ecs_name

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
        if not isinstance(other, MemberInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
