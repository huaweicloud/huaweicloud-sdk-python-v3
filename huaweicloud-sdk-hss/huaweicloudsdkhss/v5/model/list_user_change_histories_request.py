# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListUserChangeHistoriesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'host_name': 'str',
        'host_id': 'str',
        'enterprise_project_id': 'str',
        'user_name': 'str',
        'root_permission': 'bool',
        'private_ip': 'str',
        'change_type': 'str',
        'limit': 'int',
        'offset': 'int',
        'start_time': 'int',
        'end_time': 'int'
    }

    attribute_map = {
        'host_name': 'host_name',
        'host_id': 'host_id',
        'enterprise_project_id': 'enterprise_project_id',
        'user_name': 'user_name',
        'root_permission': 'root_permission',
        'private_ip': 'private_ip',
        'change_type': 'change_type',
        'limit': 'limit',
        'offset': 'offset',
        'start_time': 'start_time',
        'end_time': 'end_time'
    }

    def __init__(self, host_name=None, host_id=None, enterprise_project_id=None, user_name=None, root_permission=None, private_ip=None, change_type=None, limit=None, offset=None, start_time=None, end_time=None):
        r"""ListUserChangeHistoriesRequest

        The model defined in huaweicloud sdk

        :param host_name: **参数解释**: 服务器名称 **约束限制**: 不涉及 **取值范围**: 字符长度1-256位 **默认取值**: 不涉及 
        :type host_name: str
        :param host_id: **参数解释**: 服务器ID **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 
        :type host_id: str
        :param enterprise_project_id: **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 
        :type enterprise_project_id: str
        :param user_name: **参数解释**: 用户名 **约束限制**: 不涉及 **取值范围**: 字符长度1-128位  **默认取值**: 不涉及 
        :type user_name: str
        :param root_permission: **参数解释**: 是否有root权限 **约束限制**: 不涉及 **取值范围**: true: 具有root权限 false: 不具有root权限  **默认取值**: 不涉及 
        :type root_permission: bool
        :param private_ip: **参数解释**: 服务器私有IP **约束限制**: 不涉及 **取值范围**: 字符长度1-256位  **默认取值**: 不涉及 
        :type private_ip: str
        :param change_type: **参数解释**: 账号变更类型 **约束限制**: 不涉及 **取值范围**: - ADD ：添加 - DELETE ：删除 - MODIFY ： 修改  **默认取值**: 不涉及 
        :type change_type: str
        :param limit: **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200  **默认取值**: 10 
        :type limit: int
        :param offset: **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值10000  **默认取值**: 不涉及 
        :type offset: int
        :param start_time: **参数解释**: 变更开始时间，13位时间戳 **约束限制**: 不涉及 **取值范围**: 取值0-4070880000000  **默认取值**: 不涉及 
        :type start_time: int
        :param end_time: **参数解释**: 变更结束时间，13位时间戳 **约束限制**: 不涉及 **取值范围**: 取值0-4070880000000  **默认取值**: 不涉及 
        :type end_time: int
        """
        
        

        self._host_name = None
        self._host_id = None
        self._enterprise_project_id = None
        self._user_name = None
        self._root_permission = None
        self._private_ip = None
        self._change_type = None
        self._limit = None
        self._offset = None
        self._start_time = None
        self._end_time = None
        self.discriminator = None

        if host_name is not None:
            self.host_name = host_name
        if host_id is not None:
            self.host_id = host_id
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if user_name is not None:
            self.user_name = user_name
        if root_permission is not None:
            self.root_permission = root_permission
        if private_ip is not None:
            self.private_ip = private_ip
        if change_type is not None:
            self.change_type = change_type
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time

    @property
    def host_name(self):
        r"""Gets the host_name of this ListUserChangeHistoriesRequest.

        **参数解释**: 服务器名称 **约束限制**: 不涉及 **取值范围**: 字符长度1-256位 **默认取值**: 不涉及 

        :return: The host_name of this ListUserChangeHistoriesRequest.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this ListUserChangeHistoriesRequest.

        **参数解释**: 服务器名称 **约束限制**: 不涉及 **取值范围**: 字符长度1-256位 **默认取值**: 不涉及 

        :param host_name: The host_name of this ListUserChangeHistoriesRequest.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def host_id(self):
        r"""Gets the host_id of this ListUserChangeHistoriesRequest.

        **参数解释**: 服务器ID **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 

        :return: The host_id of this ListUserChangeHistoriesRequest.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        r"""Sets the host_id of this ListUserChangeHistoriesRequest.

        **参数解释**: 服务器ID **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 

        :param host_id: The host_id of this ListUserChangeHistoriesRequest.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListUserChangeHistoriesRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :return: The enterprise_project_id of this ListUserChangeHistoriesRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListUserChangeHistoriesRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :param enterprise_project_id: The enterprise_project_id of this ListUserChangeHistoriesRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def user_name(self):
        r"""Gets the user_name of this ListUserChangeHistoriesRequest.

        **参数解释**: 用户名 **约束限制**: 不涉及 **取值范围**: 字符长度1-128位  **默认取值**: 不涉及 

        :return: The user_name of this ListUserChangeHistoriesRequest.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this ListUserChangeHistoriesRequest.

        **参数解释**: 用户名 **约束限制**: 不涉及 **取值范围**: 字符长度1-128位  **默认取值**: 不涉及 

        :param user_name: The user_name of this ListUserChangeHistoriesRequest.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def root_permission(self):
        r"""Gets the root_permission of this ListUserChangeHistoriesRequest.

        **参数解释**: 是否有root权限 **约束限制**: 不涉及 **取值范围**: true: 具有root权限 false: 不具有root权限  **默认取值**: 不涉及 

        :return: The root_permission of this ListUserChangeHistoriesRequest.
        :rtype: bool
        """
        return self._root_permission

    @root_permission.setter
    def root_permission(self, root_permission):
        r"""Sets the root_permission of this ListUserChangeHistoriesRequest.

        **参数解释**: 是否有root权限 **约束限制**: 不涉及 **取值范围**: true: 具有root权限 false: 不具有root权限  **默认取值**: 不涉及 

        :param root_permission: The root_permission of this ListUserChangeHistoriesRequest.
        :type root_permission: bool
        """
        self._root_permission = root_permission

    @property
    def private_ip(self):
        r"""Gets the private_ip of this ListUserChangeHistoriesRequest.

        **参数解释**: 服务器私有IP **约束限制**: 不涉及 **取值范围**: 字符长度1-256位  **默认取值**: 不涉及 

        :return: The private_ip of this ListUserChangeHistoriesRequest.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        r"""Sets the private_ip of this ListUserChangeHistoriesRequest.

        **参数解释**: 服务器私有IP **约束限制**: 不涉及 **取值范围**: 字符长度1-256位  **默认取值**: 不涉及 

        :param private_ip: The private_ip of this ListUserChangeHistoriesRequest.
        :type private_ip: str
        """
        self._private_ip = private_ip

    @property
    def change_type(self):
        r"""Gets the change_type of this ListUserChangeHistoriesRequest.

        **参数解释**: 账号变更类型 **约束限制**: 不涉及 **取值范围**: - ADD ：添加 - DELETE ：删除 - MODIFY ： 修改  **默认取值**: 不涉及 

        :return: The change_type of this ListUserChangeHistoriesRequest.
        :rtype: str
        """
        return self._change_type

    @change_type.setter
    def change_type(self, change_type):
        r"""Sets the change_type of this ListUserChangeHistoriesRequest.

        **参数解释**: 账号变更类型 **约束限制**: 不涉及 **取值范围**: - ADD ：添加 - DELETE ：删除 - MODIFY ： 修改  **默认取值**: 不涉及 

        :param change_type: The change_type of this ListUserChangeHistoriesRequest.
        :type change_type: str
        """
        self._change_type = change_type

    @property
    def limit(self):
        r"""Gets the limit of this ListUserChangeHistoriesRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200  **默认取值**: 10 

        :return: The limit of this ListUserChangeHistoriesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListUserChangeHistoriesRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200  **默认取值**: 10 

        :param limit: The limit of this ListUserChangeHistoriesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListUserChangeHistoriesRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值10000  **默认取值**: 不涉及 

        :return: The offset of this ListUserChangeHistoriesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListUserChangeHistoriesRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值10000  **默认取值**: 不涉及 

        :param offset: The offset of this ListUserChangeHistoriesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def start_time(self):
        r"""Gets the start_time of this ListUserChangeHistoriesRequest.

        **参数解释**: 变更开始时间，13位时间戳 **约束限制**: 不涉及 **取值范围**: 取值0-4070880000000  **默认取值**: 不涉及 

        :return: The start_time of this ListUserChangeHistoriesRequest.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ListUserChangeHistoriesRequest.

        **参数解释**: 变更开始时间，13位时间戳 **约束限制**: 不涉及 **取值范围**: 取值0-4070880000000  **默认取值**: 不涉及 

        :param start_time: The start_time of this ListUserChangeHistoriesRequest.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListUserChangeHistoriesRequest.

        **参数解释**: 变更结束时间，13位时间戳 **约束限制**: 不涉及 **取值范围**: 取值0-4070880000000  **默认取值**: 不涉及 

        :return: The end_time of this ListUserChangeHistoriesRequest.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListUserChangeHistoriesRequest.

        **参数解释**: 变更结束时间，13位时间戳 **约束限制**: 不涉及 **取值范围**: 取值0-4070880000000  **默认取值**: 不涉及 

        :param end_time: The end_time of this ListUserChangeHistoriesRequest.
        :type end_time: int
        """
        self._end_time = end_time

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
        if not isinstance(other, ListUserChangeHistoriesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
