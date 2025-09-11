# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InvocationInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'invocation_id': 'str',
        'instance_id': 'str',
        'instance_name': 'str',
        'instance_type': 'str',
        'intranet_ips': 'list[str]',
        'elastic_ips': 'list[str]',
        'invocation_type': 'str',
        'invocation_status': 'str',
        'invocation_target': 'str',
        'create_time': 'int',
        'update_time': 'int',
        'current_version': 'str',
        'target_version': 'str',
        'result_msg': 'str'
    }

    attribute_map = {
        'invocation_id': 'invocation_id',
        'instance_id': 'instance_id',
        'instance_name': 'instance_name',
        'instance_type': 'instance_type',
        'intranet_ips': 'intranet_ips',
        'elastic_ips': 'elastic_ips',
        'invocation_type': 'invocation_type',
        'invocation_status': 'invocation_status',
        'invocation_target': 'invocation_target',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'current_version': 'current_version',
        'target_version': 'target_version',
        'result_msg': 'result_msg'
    }

    def __init__(self, invocation_id=None, instance_id=None, instance_name=None, instance_type=None, intranet_ips=None, elastic_ips=None, invocation_type=None, invocation_status=None, invocation_target=None, create_time=None, update_time=None, current_version=None, target_version=None, result_msg=None):
        r"""InvocationInfo

        The model defined in huaweicloud sdk

        :param invocation_id: **参数解释**: 任务id **取值范围**: 以字母或数字开头，后续可以包含字母、数字、下划线（_）或连字符（-），长度至少为1，且不允许出现其他字符 
        :type invocation_id: str
        :param instance_id: **参数解释**: 主机id **取值范围**: 1到64个字符的字符串，且只包含字母、数字和连字符 
        :type instance_id: str
        :param instance_name: **参数解释**: 主机名称 **取值范围**: 字符串长度范围为[1,128] 
        :type instance_name: str
        :param instance_type: **参数解释**: 主机类型，仅支持ECS弹性云服务器和BMS裸金属服务器 **取值范围**: - ECS: 弹性云服务器 - BMS：裸金属服务器 
        :type instance_type: str
        :param intranet_ips: **参数解释**: 内网ip列表 **取值范围**: 返回数组长度为[0,10]，数组内元素格式为：长度为1到15个字符的字符串，其中每个字符可以是数字（0-9）或任意其他单个字符 
        :type intranet_ips: list[str]
        :param elastic_ips: **参数解释**: 弹性公网ip列表 **取值范围**: 返回数组长度为[0,10]，数组内元素格式为：长度为1到15个字符的字符串，其中每个字符可以是数字（0-9）或任意其他单个字符 
        :type elastic_ips: list[str]
        :param invocation_type: **参数解释**: 任务类型 **取值范围**: - INSTALL：安装 - UPDATE：升级 - ROLLBACK：回滚 - RETRY：重试 
        :type invocation_type: str
        :param invocation_status: **参数解释**: 任务状态 **取值范围**: - PENDING：待执行 - RUNNING：运行中 - TIMEOUT：超时 - FAILED：失败 - SUCCEEDED：成功 - CANCELED：取消 - ROLLBACKED：已回退 
        :type invocation_status: str
        :param invocation_target: **参数解释**: 任务对象, 支持telescope监控 **取值范围**: - telescope: 主机监控插件telescope 
        :type invocation_target: str
        :param create_time: **参数解释**: 任务创建时间 **取值范围**: 数字范围为[1111111111111,9999999999999] 
        :type create_time: int
        :param update_time: **参数解释**: 任务更新时间 **取值范围**: 数字范围为[1111111111111,9999999999999] 
        :type update_time: int
        :param current_version: **参数解释**: 当前版本 **取值范围**: 字符串长度范围为[1,64] 
        :type current_version: str
        :param target_version: **参数解释**: 目标版本 **取值范围**: 字符串长度范围为[1,64] 
        :type target_version: str
        :param result_msg: **参数解释**: 任务执行结果信息 **取值范围**: 字符串长度范围为[1,5000] 
        :type result_msg: str
        """
        
        

        self._invocation_id = None
        self._instance_id = None
        self._instance_name = None
        self._instance_type = None
        self._intranet_ips = None
        self._elastic_ips = None
        self._invocation_type = None
        self._invocation_status = None
        self._invocation_target = None
        self._create_time = None
        self._update_time = None
        self._current_version = None
        self._target_version = None
        self._result_msg = None
        self.discriminator = None

        if invocation_id is not None:
            self.invocation_id = invocation_id
        if instance_id is not None:
            self.instance_id = instance_id
        if instance_name is not None:
            self.instance_name = instance_name
        if instance_type is not None:
            self.instance_type = instance_type
        if intranet_ips is not None:
            self.intranet_ips = intranet_ips
        if elastic_ips is not None:
            self.elastic_ips = elastic_ips
        if invocation_type is not None:
            self.invocation_type = invocation_type
        if invocation_status is not None:
            self.invocation_status = invocation_status
        if invocation_target is not None:
            self.invocation_target = invocation_target
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if current_version is not None:
            self.current_version = current_version
        if target_version is not None:
            self.target_version = target_version
        if result_msg is not None:
            self.result_msg = result_msg

    @property
    def invocation_id(self):
        r"""Gets the invocation_id of this InvocationInfo.

        **参数解释**: 任务id **取值范围**: 以字母或数字开头，后续可以包含字母、数字、下划线（_）或连字符（-），长度至少为1，且不允许出现其他字符 

        :return: The invocation_id of this InvocationInfo.
        :rtype: str
        """
        return self._invocation_id

    @invocation_id.setter
    def invocation_id(self, invocation_id):
        r"""Sets the invocation_id of this InvocationInfo.

        **参数解释**: 任务id **取值范围**: 以字母或数字开头，后续可以包含字母、数字、下划线（_）或连字符（-），长度至少为1，且不允许出现其他字符 

        :param invocation_id: The invocation_id of this InvocationInfo.
        :type invocation_id: str
        """
        self._invocation_id = invocation_id

    @property
    def instance_id(self):
        r"""Gets the instance_id of this InvocationInfo.

        **参数解释**: 主机id **取值范围**: 1到64个字符的字符串，且只包含字母、数字和连字符 

        :return: The instance_id of this InvocationInfo.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this InvocationInfo.

        **参数解释**: 主机id **取值范围**: 1到64个字符的字符串，且只包含字母、数字和连字符 

        :param instance_id: The instance_id of this InvocationInfo.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def instance_name(self):
        r"""Gets the instance_name of this InvocationInfo.

        **参数解释**: 主机名称 **取值范围**: 字符串长度范围为[1,128] 

        :return: The instance_name of this InvocationInfo.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        r"""Sets the instance_name of this InvocationInfo.

        **参数解释**: 主机名称 **取值范围**: 字符串长度范围为[1,128] 

        :param instance_name: The instance_name of this InvocationInfo.
        :type instance_name: str
        """
        self._instance_name = instance_name

    @property
    def instance_type(self):
        r"""Gets the instance_type of this InvocationInfo.

        **参数解释**: 主机类型，仅支持ECS弹性云服务器和BMS裸金属服务器 **取值范围**: - ECS: 弹性云服务器 - BMS：裸金属服务器 

        :return: The instance_type of this InvocationInfo.
        :rtype: str
        """
        return self._instance_type

    @instance_type.setter
    def instance_type(self, instance_type):
        r"""Sets the instance_type of this InvocationInfo.

        **参数解释**: 主机类型，仅支持ECS弹性云服务器和BMS裸金属服务器 **取值范围**: - ECS: 弹性云服务器 - BMS：裸金属服务器 

        :param instance_type: The instance_type of this InvocationInfo.
        :type instance_type: str
        """
        self._instance_type = instance_type

    @property
    def intranet_ips(self):
        r"""Gets the intranet_ips of this InvocationInfo.

        **参数解释**: 内网ip列表 **取值范围**: 返回数组长度为[0,10]，数组内元素格式为：长度为1到15个字符的字符串，其中每个字符可以是数字（0-9）或任意其他单个字符 

        :return: The intranet_ips of this InvocationInfo.
        :rtype: list[str]
        """
        return self._intranet_ips

    @intranet_ips.setter
    def intranet_ips(self, intranet_ips):
        r"""Sets the intranet_ips of this InvocationInfo.

        **参数解释**: 内网ip列表 **取值范围**: 返回数组长度为[0,10]，数组内元素格式为：长度为1到15个字符的字符串，其中每个字符可以是数字（0-9）或任意其他单个字符 

        :param intranet_ips: The intranet_ips of this InvocationInfo.
        :type intranet_ips: list[str]
        """
        self._intranet_ips = intranet_ips

    @property
    def elastic_ips(self):
        r"""Gets the elastic_ips of this InvocationInfo.

        **参数解释**: 弹性公网ip列表 **取值范围**: 返回数组长度为[0,10]，数组内元素格式为：长度为1到15个字符的字符串，其中每个字符可以是数字（0-9）或任意其他单个字符 

        :return: The elastic_ips of this InvocationInfo.
        :rtype: list[str]
        """
        return self._elastic_ips

    @elastic_ips.setter
    def elastic_ips(self, elastic_ips):
        r"""Sets the elastic_ips of this InvocationInfo.

        **参数解释**: 弹性公网ip列表 **取值范围**: 返回数组长度为[0,10]，数组内元素格式为：长度为1到15个字符的字符串，其中每个字符可以是数字（0-9）或任意其他单个字符 

        :param elastic_ips: The elastic_ips of this InvocationInfo.
        :type elastic_ips: list[str]
        """
        self._elastic_ips = elastic_ips

    @property
    def invocation_type(self):
        r"""Gets the invocation_type of this InvocationInfo.

        **参数解释**: 任务类型 **取值范围**: - INSTALL：安装 - UPDATE：升级 - ROLLBACK：回滚 - RETRY：重试 

        :return: The invocation_type of this InvocationInfo.
        :rtype: str
        """
        return self._invocation_type

    @invocation_type.setter
    def invocation_type(self, invocation_type):
        r"""Sets the invocation_type of this InvocationInfo.

        **参数解释**: 任务类型 **取值范围**: - INSTALL：安装 - UPDATE：升级 - ROLLBACK：回滚 - RETRY：重试 

        :param invocation_type: The invocation_type of this InvocationInfo.
        :type invocation_type: str
        """
        self._invocation_type = invocation_type

    @property
    def invocation_status(self):
        r"""Gets the invocation_status of this InvocationInfo.

        **参数解释**: 任务状态 **取值范围**: - PENDING：待执行 - RUNNING：运行中 - TIMEOUT：超时 - FAILED：失败 - SUCCEEDED：成功 - CANCELED：取消 - ROLLBACKED：已回退 

        :return: The invocation_status of this InvocationInfo.
        :rtype: str
        """
        return self._invocation_status

    @invocation_status.setter
    def invocation_status(self, invocation_status):
        r"""Sets the invocation_status of this InvocationInfo.

        **参数解释**: 任务状态 **取值范围**: - PENDING：待执行 - RUNNING：运行中 - TIMEOUT：超时 - FAILED：失败 - SUCCEEDED：成功 - CANCELED：取消 - ROLLBACKED：已回退 

        :param invocation_status: The invocation_status of this InvocationInfo.
        :type invocation_status: str
        """
        self._invocation_status = invocation_status

    @property
    def invocation_target(self):
        r"""Gets the invocation_target of this InvocationInfo.

        **参数解释**: 任务对象, 支持telescope监控 **取值范围**: - telescope: 主机监控插件telescope 

        :return: The invocation_target of this InvocationInfo.
        :rtype: str
        """
        return self._invocation_target

    @invocation_target.setter
    def invocation_target(self, invocation_target):
        r"""Sets the invocation_target of this InvocationInfo.

        **参数解释**: 任务对象, 支持telescope监控 **取值范围**: - telescope: 主机监控插件telescope 

        :param invocation_target: The invocation_target of this InvocationInfo.
        :type invocation_target: str
        """
        self._invocation_target = invocation_target

    @property
    def create_time(self):
        r"""Gets the create_time of this InvocationInfo.

        **参数解释**: 任务创建时间 **取值范围**: 数字范围为[1111111111111,9999999999999] 

        :return: The create_time of this InvocationInfo.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this InvocationInfo.

        **参数解释**: 任务创建时间 **取值范围**: 数字范围为[1111111111111,9999999999999] 

        :param create_time: The create_time of this InvocationInfo.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this InvocationInfo.

        **参数解释**: 任务更新时间 **取值范围**: 数字范围为[1111111111111,9999999999999] 

        :return: The update_time of this InvocationInfo.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this InvocationInfo.

        **参数解释**: 任务更新时间 **取值范围**: 数字范围为[1111111111111,9999999999999] 

        :param update_time: The update_time of this InvocationInfo.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def current_version(self):
        r"""Gets the current_version of this InvocationInfo.

        **参数解释**: 当前版本 **取值范围**: 字符串长度范围为[1,64] 

        :return: The current_version of this InvocationInfo.
        :rtype: str
        """
        return self._current_version

    @current_version.setter
    def current_version(self, current_version):
        r"""Sets the current_version of this InvocationInfo.

        **参数解释**: 当前版本 **取值范围**: 字符串长度范围为[1,64] 

        :param current_version: The current_version of this InvocationInfo.
        :type current_version: str
        """
        self._current_version = current_version

    @property
    def target_version(self):
        r"""Gets the target_version of this InvocationInfo.

        **参数解释**: 目标版本 **取值范围**: 字符串长度范围为[1,64] 

        :return: The target_version of this InvocationInfo.
        :rtype: str
        """
        return self._target_version

    @target_version.setter
    def target_version(self, target_version):
        r"""Sets the target_version of this InvocationInfo.

        **参数解释**: 目标版本 **取值范围**: 字符串长度范围为[1,64] 

        :param target_version: The target_version of this InvocationInfo.
        :type target_version: str
        """
        self._target_version = target_version

    @property
    def result_msg(self):
        r"""Gets the result_msg of this InvocationInfo.

        **参数解释**: 任务执行结果信息 **取值范围**: 字符串长度范围为[1,5000] 

        :return: The result_msg of this InvocationInfo.
        :rtype: str
        """
        return self._result_msg

    @result_msg.setter
    def result_msg(self, result_msg):
        r"""Sets the result_msg of this InvocationInfo.

        **参数解释**: 任务执行结果信息 **取值范围**: 字符串长度范围为[1,5000] 

        :param result_msg: The result_msg of this InvocationInfo.
        :type result_msg: str
        """
        self._result_msg = result_msg

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
        if not isinstance(other, InvocationInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
