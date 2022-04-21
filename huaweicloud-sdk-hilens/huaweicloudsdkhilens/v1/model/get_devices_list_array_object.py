# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GetDevicesListArrayObject:

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
        'name': 'str',
        'type': 'str',
        'status': 'int',
        'cpu': 'int',
        'memory': 'int',
        'os': 'str',
        'firmware_name': 'str',
        'firmware_version': 'str',
        'firmware_status': 'int',
        'firmware_cause': 'str',
        'path': 'str',
        'path_update_status': 'int',
        'path_update_cause': 'str',
        'create_time': 'int',
        'update_time': 'int',
        'user_time': 'str',
        'resource_spec_code': 'str',
        'cloud_service_type': 'str',
        'active_content': 'str',
        'active_flag': 'int',
        'topic_urn': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'type': 'type',
        'status': 'status',
        'cpu': 'cpu',
        'memory': 'memory',
        'os': 'os',
        'firmware_name': 'firmware_name',
        'firmware_version': 'firmware_version',
        'firmware_status': 'firmware_status',
        'firmware_cause': 'firmware_cause',
        'path': 'path',
        'path_update_status': 'path_update_status',
        'path_update_cause': 'path_update_cause',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'user_time': 'user_time',
        'resource_spec_code': 'resource_spec_code',
        'cloud_service_type': 'cloud_service_type',
        'active_content': 'active_content',
        'active_flag': 'active_flag',
        'topic_urn': 'topic_urn'
    }

    def __init__(self, id=None, name=None, type=None, status=None, cpu=None, memory=None, os=None, firmware_name=None, firmware_version=None, firmware_status=None, firmware_cause=None, path=None, path_update_status=None, path_update_cause=None, create_time=None, update_time=None, user_time=None, resource_spec_code=None, cloud_service_type=None, active_content=None, active_flag=None, topic_urn=None):
        """GetDevicesListArrayObject

        The model defined in huaweicloud sdk

        :param id: 设备ID
        :type id: str
        :param name: 设备名称
        :type name: str
        :param type: 设备类型
        :type type: str
        :param status: 设备状态(0:离线;1:在线)
        :type status: int
        :param cpu: cpu核数
        :type cpu: int
        :param memory: 内存大小
        :type memory: int
        :param os: 操作系统
        :type os: str
        :param firmware_name: 固件名称
        :type firmware_name: str
        :param firmware_version: 固件版本
        :type firmware_version: str
        :param firmware_status: 固件状态(1:更新中，2：更新失败，3：更新成功)
        :type firmware_status: int
        :param firmware_cause: 固件更新失败原因
        :type firmware_cause: str
        :param path: 设备数据存储路径，该桶需要和当前region匹配
        :type path: str
        :param path_update_status: 设备数据存储路径更新状态(0:更新成功，1：更新中)
        :type path_update_status: int
        :param path_update_cause: 设备数据存储路径更新失败原因
        :type path_update_cause: str
        :param create_time: 创建时间（时间戳）
        :type create_time: int
        :param update_time: 更新时间（时间戳）
        :type update_time: int
        :param user_time: IAM用户名
        :type user_time: str
        :param resource_spec_code: 计费资源码
        :type resource_spec_code: str
        :param cloud_service_type: 云服务计费类型
        :type cloud_service_type: str
        :param active_content: 激活内容
        :type active_content: str
        :param active_flag: 激活状态(0:未激活，1：已激活且付费，2：已激活且免费，3：付费到期，4：已激活使用SN码，5：已激活30天免费，6：免费到期)
        :type active_flag: int
        :param topic_urn: 关联设备的主题消息推送的URN地址
        :type topic_urn: str
        """
        
        

        self._id = None
        self._name = None
        self._type = None
        self._status = None
        self._cpu = None
        self._memory = None
        self._os = None
        self._firmware_name = None
        self._firmware_version = None
        self._firmware_status = None
        self._firmware_cause = None
        self._path = None
        self._path_update_status = None
        self._path_update_cause = None
        self._create_time = None
        self._update_time = None
        self._user_time = None
        self._resource_spec_code = None
        self._cloud_service_type = None
        self._active_content = None
        self._active_flag = None
        self._topic_urn = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if status is not None:
            self.status = status
        if cpu is not None:
            self.cpu = cpu
        if memory is not None:
            self.memory = memory
        if os is not None:
            self.os = os
        if firmware_name is not None:
            self.firmware_name = firmware_name
        if firmware_version is not None:
            self.firmware_version = firmware_version
        if firmware_status is not None:
            self.firmware_status = firmware_status
        if firmware_cause is not None:
            self.firmware_cause = firmware_cause
        if path is not None:
            self.path = path
        if path_update_status is not None:
            self.path_update_status = path_update_status
        if path_update_cause is not None:
            self.path_update_cause = path_update_cause
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if user_time is not None:
            self.user_time = user_time
        if resource_spec_code is not None:
            self.resource_spec_code = resource_spec_code
        if cloud_service_type is not None:
            self.cloud_service_type = cloud_service_type
        if active_content is not None:
            self.active_content = active_content
        if active_flag is not None:
            self.active_flag = active_flag
        if topic_urn is not None:
            self.topic_urn = topic_urn

    @property
    def id(self):
        """Gets the id of this GetDevicesListArrayObject.

        设备ID

        :return: The id of this GetDevicesListArrayObject.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GetDevicesListArrayObject.

        设备ID

        :param id: The id of this GetDevicesListArrayObject.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this GetDevicesListArrayObject.

        设备名称

        :return: The name of this GetDevicesListArrayObject.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GetDevicesListArrayObject.

        设备名称

        :param name: The name of this GetDevicesListArrayObject.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        """Gets the type of this GetDevicesListArrayObject.

        设备类型

        :return: The type of this GetDevicesListArrayObject.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this GetDevicesListArrayObject.

        设备类型

        :param type: The type of this GetDevicesListArrayObject.
        :type type: str
        """
        self._type = type

    @property
    def status(self):
        """Gets the status of this GetDevicesListArrayObject.

        设备状态(0:离线;1:在线)

        :return: The status of this GetDevicesListArrayObject.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this GetDevicesListArrayObject.

        设备状态(0:离线;1:在线)

        :param status: The status of this GetDevicesListArrayObject.
        :type status: int
        """
        self._status = status

    @property
    def cpu(self):
        """Gets the cpu of this GetDevicesListArrayObject.

        cpu核数

        :return: The cpu of this GetDevicesListArrayObject.
        :rtype: int
        """
        return self._cpu

    @cpu.setter
    def cpu(self, cpu):
        """Sets the cpu of this GetDevicesListArrayObject.

        cpu核数

        :param cpu: The cpu of this GetDevicesListArrayObject.
        :type cpu: int
        """
        self._cpu = cpu

    @property
    def memory(self):
        """Gets the memory of this GetDevicesListArrayObject.

        内存大小

        :return: The memory of this GetDevicesListArrayObject.
        :rtype: int
        """
        return self._memory

    @memory.setter
    def memory(self, memory):
        """Sets the memory of this GetDevicesListArrayObject.

        内存大小

        :param memory: The memory of this GetDevicesListArrayObject.
        :type memory: int
        """
        self._memory = memory

    @property
    def os(self):
        """Gets the os of this GetDevicesListArrayObject.

        操作系统

        :return: The os of this GetDevicesListArrayObject.
        :rtype: str
        """
        return self._os

    @os.setter
    def os(self, os):
        """Sets the os of this GetDevicesListArrayObject.

        操作系统

        :param os: The os of this GetDevicesListArrayObject.
        :type os: str
        """
        self._os = os

    @property
    def firmware_name(self):
        """Gets the firmware_name of this GetDevicesListArrayObject.

        固件名称

        :return: The firmware_name of this GetDevicesListArrayObject.
        :rtype: str
        """
        return self._firmware_name

    @firmware_name.setter
    def firmware_name(self, firmware_name):
        """Sets the firmware_name of this GetDevicesListArrayObject.

        固件名称

        :param firmware_name: The firmware_name of this GetDevicesListArrayObject.
        :type firmware_name: str
        """
        self._firmware_name = firmware_name

    @property
    def firmware_version(self):
        """Gets the firmware_version of this GetDevicesListArrayObject.

        固件版本

        :return: The firmware_version of this GetDevicesListArrayObject.
        :rtype: str
        """
        return self._firmware_version

    @firmware_version.setter
    def firmware_version(self, firmware_version):
        """Sets the firmware_version of this GetDevicesListArrayObject.

        固件版本

        :param firmware_version: The firmware_version of this GetDevicesListArrayObject.
        :type firmware_version: str
        """
        self._firmware_version = firmware_version

    @property
    def firmware_status(self):
        """Gets the firmware_status of this GetDevicesListArrayObject.

        固件状态(1:更新中，2：更新失败，3：更新成功)

        :return: The firmware_status of this GetDevicesListArrayObject.
        :rtype: int
        """
        return self._firmware_status

    @firmware_status.setter
    def firmware_status(self, firmware_status):
        """Sets the firmware_status of this GetDevicesListArrayObject.

        固件状态(1:更新中，2：更新失败，3：更新成功)

        :param firmware_status: The firmware_status of this GetDevicesListArrayObject.
        :type firmware_status: int
        """
        self._firmware_status = firmware_status

    @property
    def firmware_cause(self):
        """Gets the firmware_cause of this GetDevicesListArrayObject.

        固件更新失败原因

        :return: The firmware_cause of this GetDevicesListArrayObject.
        :rtype: str
        """
        return self._firmware_cause

    @firmware_cause.setter
    def firmware_cause(self, firmware_cause):
        """Sets the firmware_cause of this GetDevicesListArrayObject.

        固件更新失败原因

        :param firmware_cause: The firmware_cause of this GetDevicesListArrayObject.
        :type firmware_cause: str
        """
        self._firmware_cause = firmware_cause

    @property
    def path(self):
        """Gets the path of this GetDevicesListArrayObject.

        设备数据存储路径，该桶需要和当前region匹配

        :return: The path of this GetDevicesListArrayObject.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this GetDevicesListArrayObject.

        设备数据存储路径，该桶需要和当前region匹配

        :param path: The path of this GetDevicesListArrayObject.
        :type path: str
        """
        self._path = path

    @property
    def path_update_status(self):
        """Gets the path_update_status of this GetDevicesListArrayObject.

        设备数据存储路径更新状态(0:更新成功，1：更新中)

        :return: The path_update_status of this GetDevicesListArrayObject.
        :rtype: int
        """
        return self._path_update_status

    @path_update_status.setter
    def path_update_status(self, path_update_status):
        """Sets the path_update_status of this GetDevicesListArrayObject.

        设备数据存储路径更新状态(0:更新成功，1：更新中)

        :param path_update_status: The path_update_status of this GetDevicesListArrayObject.
        :type path_update_status: int
        """
        self._path_update_status = path_update_status

    @property
    def path_update_cause(self):
        """Gets the path_update_cause of this GetDevicesListArrayObject.

        设备数据存储路径更新失败原因

        :return: The path_update_cause of this GetDevicesListArrayObject.
        :rtype: str
        """
        return self._path_update_cause

    @path_update_cause.setter
    def path_update_cause(self, path_update_cause):
        """Sets the path_update_cause of this GetDevicesListArrayObject.

        设备数据存储路径更新失败原因

        :param path_update_cause: The path_update_cause of this GetDevicesListArrayObject.
        :type path_update_cause: str
        """
        self._path_update_cause = path_update_cause

    @property
    def create_time(self):
        """Gets the create_time of this GetDevicesListArrayObject.

        创建时间（时间戳）

        :return: The create_time of this GetDevicesListArrayObject.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this GetDevicesListArrayObject.

        创建时间（时间戳）

        :param create_time: The create_time of this GetDevicesListArrayObject.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this GetDevicesListArrayObject.

        更新时间（时间戳）

        :return: The update_time of this GetDevicesListArrayObject.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this GetDevicesListArrayObject.

        更新时间（时间戳）

        :param update_time: The update_time of this GetDevicesListArrayObject.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def user_time(self):
        """Gets the user_time of this GetDevicesListArrayObject.

        IAM用户名

        :return: The user_time of this GetDevicesListArrayObject.
        :rtype: str
        """
        return self._user_time

    @user_time.setter
    def user_time(self, user_time):
        """Sets the user_time of this GetDevicesListArrayObject.

        IAM用户名

        :param user_time: The user_time of this GetDevicesListArrayObject.
        :type user_time: str
        """
        self._user_time = user_time

    @property
    def resource_spec_code(self):
        """Gets the resource_spec_code of this GetDevicesListArrayObject.

        计费资源码

        :return: The resource_spec_code of this GetDevicesListArrayObject.
        :rtype: str
        """
        return self._resource_spec_code

    @resource_spec_code.setter
    def resource_spec_code(self, resource_spec_code):
        """Sets the resource_spec_code of this GetDevicesListArrayObject.

        计费资源码

        :param resource_spec_code: The resource_spec_code of this GetDevicesListArrayObject.
        :type resource_spec_code: str
        """
        self._resource_spec_code = resource_spec_code

    @property
    def cloud_service_type(self):
        """Gets the cloud_service_type of this GetDevicesListArrayObject.

        云服务计费类型

        :return: The cloud_service_type of this GetDevicesListArrayObject.
        :rtype: str
        """
        return self._cloud_service_type

    @cloud_service_type.setter
    def cloud_service_type(self, cloud_service_type):
        """Sets the cloud_service_type of this GetDevicesListArrayObject.

        云服务计费类型

        :param cloud_service_type: The cloud_service_type of this GetDevicesListArrayObject.
        :type cloud_service_type: str
        """
        self._cloud_service_type = cloud_service_type

    @property
    def active_content(self):
        """Gets the active_content of this GetDevicesListArrayObject.

        激活内容

        :return: The active_content of this GetDevicesListArrayObject.
        :rtype: str
        """
        return self._active_content

    @active_content.setter
    def active_content(self, active_content):
        """Sets the active_content of this GetDevicesListArrayObject.

        激活内容

        :param active_content: The active_content of this GetDevicesListArrayObject.
        :type active_content: str
        """
        self._active_content = active_content

    @property
    def active_flag(self):
        """Gets the active_flag of this GetDevicesListArrayObject.

        激活状态(0:未激活，1：已激活且付费，2：已激活且免费，3：付费到期，4：已激活使用SN码，5：已激活30天免费，6：免费到期)

        :return: The active_flag of this GetDevicesListArrayObject.
        :rtype: int
        """
        return self._active_flag

    @active_flag.setter
    def active_flag(self, active_flag):
        """Sets the active_flag of this GetDevicesListArrayObject.

        激活状态(0:未激活，1：已激活且付费，2：已激活且免费，3：付费到期，4：已激活使用SN码，5：已激活30天免费，6：免费到期)

        :param active_flag: The active_flag of this GetDevicesListArrayObject.
        :type active_flag: int
        """
        self._active_flag = active_flag

    @property
    def topic_urn(self):
        """Gets the topic_urn of this GetDevicesListArrayObject.

        关联设备的主题消息推送的URN地址

        :return: The topic_urn of this GetDevicesListArrayObject.
        :rtype: str
        """
        return self._topic_urn

    @topic_urn.setter
    def topic_urn(self, topic_urn):
        """Sets the topic_urn of this GetDevicesListArrayObject.

        关联设备的主题消息推送的URN地址

        :param topic_urn: The topic_urn of this GetDevicesListArrayObject.
        :type topic_urn: str
        """
        self._topic_urn = topic_urn

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
        if not isinstance(other, GetDevicesListArrayObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
