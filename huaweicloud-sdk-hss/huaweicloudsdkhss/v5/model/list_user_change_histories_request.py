# coding: utf-8

import re
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
        'user_name': 'str',
        'host_id': 'str',
        'root_permission': 'bool',
        'host_name': 'str',
        'private_ip': 'str',
        'change_type': 'str',
        'limit': 'int',
        'offset': 'int',
        'enterprise_project_id': 'str',
        'start_time': 'int',
        'end_time': 'int'
    }

    attribute_map = {
        'user_name': 'user_name',
        'host_id': 'host_id',
        'root_permission': 'root_permission',
        'host_name': 'host_name',
        'private_ip': 'private_ip',
        'change_type': 'change_type',
        'limit': 'limit',
        'offset': 'offset',
        'enterprise_project_id': 'enterprise_project_id',
        'start_time': 'start_time',
        'end_time': 'end_time'
    }

    def __init__(self, user_name=None, host_id=None, root_permission=None, host_name=None, private_ip=None, change_type=None, limit=None, offset=None, enterprise_project_id=None, start_time=None, end_time=None):
        """ListUserChangeHistoriesRequest

        The model defined in huaweicloud sdk

        :param user_name: 账号名
        :type user_name: str
        :param host_id: 主机id
        :type host_id: str
        :param root_permission: 是否有root权限
        :type root_permission: bool
        :param host_name: 主机名称
        :type host_name: str
        :param private_ip: 服务器私有IP
        :type private_ip: str
        :param change_type: 变更类型:   - ADD ：添加   - DELETE ：删除   - MODIFY ： 修改
        :type change_type: str
        :param limit: 默认10
        :type limit: int
        :param offset: 默认是0
        :type offset: int
        :param enterprise_project_id: 企业项目
        :type enterprise_project_id: str
        :param start_time: 变更开始时间，13位时间戳
        :type start_time: int
        :param end_time: 变更结束时间，13位时间戳
        :type end_time: int
        """
        
        

        self._user_name = None
        self._host_id = None
        self._root_permission = None
        self._host_name = None
        self._private_ip = None
        self._change_type = None
        self._limit = None
        self._offset = None
        self._enterprise_project_id = None
        self._start_time = None
        self._end_time = None
        self.discriminator = None

        if user_name is not None:
            self.user_name = user_name
        if host_id is not None:
            self.host_id = host_id
        if root_permission is not None:
            self.root_permission = root_permission
        if host_name is not None:
            self.host_name = host_name
        if private_ip is not None:
            self.private_ip = private_ip
        if change_type is not None:
            self.change_type = change_type
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time

    @property
    def user_name(self):
        """Gets the user_name of this ListUserChangeHistoriesRequest.

        账号名

        :return: The user_name of this ListUserChangeHistoriesRequest.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this ListUserChangeHistoriesRequest.

        账号名

        :param user_name: The user_name of this ListUserChangeHistoriesRequest.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def host_id(self):
        """Gets the host_id of this ListUserChangeHistoriesRequest.

        主机id

        :return: The host_id of this ListUserChangeHistoriesRequest.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        """Sets the host_id of this ListUserChangeHistoriesRequest.

        主机id

        :param host_id: The host_id of this ListUserChangeHistoriesRequest.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def root_permission(self):
        """Gets the root_permission of this ListUserChangeHistoriesRequest.

        是否有root权限

        :return: The root_permission of this ListUserChangeHistoriesRequest.
        :rtype: bool
        """
        return self._root_permission

    @root_permission.setter
    def root_permission(self, root_permission):
        """Sets the root_permission of this ListUserChangeHistoriesRequest.

        是否有root权限

        :param root_permission: The root_permission of this ListUserChangeHistoriesRequest.
        :type root_permission: bool
        """
        self._root_permission = root_permission

    @property
    def host_name(self):
        """Gets the host_name of this ListUserChangeHistoriesRequest.

        主机名称

        :return: The host_name of this ListUserChangeHistoriesRequest.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        """Sets the host_name of this ListUserChangeHistoriesRequest.

        主机名称

        :param host_name: The host_name of this ListUserChangeHistoriesRequest.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def private_ip(self):
        """Gets the private_ip of this ListUserChangeHistoriesRequest.

        服务器私有IP

        :return: The private_ip of this ListUserChangeHistoriesRequest.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        """Sets the private_ip of this ListUserChangeHistoriesRequest.

        服务器私有IP

        :param private_ip: The private_ip of this ListUserChangeHistoriesRequest.
        :type private_ip: str
        """
        self._private_ip = private_ip

    @property
    def change_type(self):
        """Gets the change_type of this ListUserChangeHistoriesRequest.

        变更类型:   - ADD ：添加   - DELETE ：删除   - MODIFY ： 修改

        :return: The change_type of this ListUserChangeHistoriesRequest.
        :rtype: str
        """
        return self._change_type

    @change_type.setter
    def change_type(self, change_type):
        """Sets the change_type of this ListUserChangeHistoriesRequest.

        变更类型:   - ADD ：添加   - DELETE ：删除   - MODIFY ： 修改

        :param change_type: The change_type of this ListUserChangeHistoriesRequest.
        :type change_type: str
        """
        self._change_type = change_type

    @property
    def limit(self):
        """Gets the limit of this ListUserChangeHistoriesRequest.

        默认10

        :return: The limit of this ListUserChangeHistoriesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListUserChangeHistoriesRequest.

        默认10

        :param limit: The limit of this ListUserChangeHistoriesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListUserChangeHistoriesRequest.

        默认是0

        :return: The offset of this ListUserChangeHistoriesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListUserChangeHistoriesRequest.

        默认是0

        :param offset: The offset of this ListUserChangeHistoriesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListUserChangeHistoriesRequest.

        企业项目

        :return: The enterprise_project_id of this ListUserChangeHistoriesRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListUserChangeHistoriesRequest.

        企业项目

        :param enterprise_project_id: The enterprise_project_id of this ListUserChangeHistoriesRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def start_time(self):
        """Gets the start_time of this ListUserChangeHistoriesRequest.

        变更开始时间，13位时间戳

        :return: The start_time of this ListUserChangeHistoriesRequest.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ListUserChangeHistoriesRequest.

        变更开始时间，13位时间戳

        :param start_time: The start_time of this ListUserChangeHistoriesRequest.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ListUserChangeHistoriesRequest.

        变更结束时间，13位时间戳

        :return: The end_time of this ListUserChangeHistoriesRequest.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ListUserChangeHistoriesRequest.

        变更结束时间，13位时间戳

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
