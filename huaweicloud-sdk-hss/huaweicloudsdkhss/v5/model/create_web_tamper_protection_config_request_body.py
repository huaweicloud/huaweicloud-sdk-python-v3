# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateWebTamperProtectionConfigRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'protect_mode': 'str',
        'monitor_process': 'bool',
        'privileged_process_list': 'list[str]',
        'privileged_child': 'bool',
        'container_wtp_info': 'CreateWebTamperProtectionConfigRequestBodyContainerWtpInfo',
        'open_protection_immediately': 'bool',
        'quota_info': 'CreateWebTamperProtectionConfigRequestBodyQuotaInfo'
    }

    attribute_map = {
        'type': 'type',
        'protect_mode': 'protect_mode',
        'monitor_process': 'monitor_process',
        'privileged_process_list': 'privileged_process_list',
        'privileged_child': 'privileged_child',
        'container_wtp_info': 'container_wtp_info',
        'open_protection_immediately': 'open_protection_immediately',
        'quota_info': 'quota_info'
    }

    def __init__(self, type=None, protect_mode=None, monitor_process=None, privileged_process_list=None, privileged_child=None, container_wtp_info=None, open_protection_immediately=None, quota_info=None):
        r"""CreateWebTamperProtectionConfigRequestBody

        The model defined in huaweicloud sdk

        :param type: **参数解释**: 网页防篡改的类型 **约束限制**: 不涉及 **取值范围**: - container_wtp：容器网页防篡改  **默认取值**: 不涉及 
        :type type: str
        :param protect_mode: **参数解释**: 防护模式 **约束限制**: 不涉及 **取值范围**: - alarm：告警模式 - block：拦截模式  **默认取值**: alarm 
        :type protect_mode: str
        :param monitor_process: **参数解释**: 是否对篡改行为进行进程监控 **约束限制**: 不涉及 **取值范围**: - true：监控篡改进程 - false：不监控篡改进程  **默认取值**: true 
        :type monitor_process: bool
        :param privileged_process_list: **参数解释**: 特权进程路径列表 **约束限制**: monitor_process值为true时生效（不进行进程监控无法判断特权进程） **取值范围**: 最少0条，最多10条 **默认取值**: 不涉及 
        :type privileged_process_list: list[str]
        :param privileged_child: **参数解释**: 特权进程的子进程是否仍享有特权 **约束限制**: monitor_process值为true时生效（不进行进程监控无法判断特权进程） **取值范围**: - true：特权进程的子进程依然是特权进程 - false：特权进程的子进程不再是特权进程  **默认取值**: false 
        :type privileged_child: bool
        :param container_wtp_info: 
        :type container_wtp_info: :class:`huaweicloudsdkhss.v5.CreateWebTamperProtectionConfigRequestBodyContainerWtpInfo`
        :param open_protection_immediately: **参数解释**: 是否立即开启防护 **约束限制**: 不涉及 **取值范围**: - true：立即开启防护 - false：只保存配置内容，暂不开启防护  **默认取值**: false 
        :type open_protection_immediately: bool
        :param quota_info: 
        :type quota_info: :class:`huaweicloudsdkhss.v5.CreateWebTamperProtectionConfigRequestBodyQuotaInfo`
        """
        
        

        self._type = None
        self._protect_mode = None
        self._monitor_process = None
        self._privileged_process_list = None
        self._privileged_child = None
        self._container_wtp_info = None
        self._open_protection_immediately = None
        self._quota_info = None
        self.discriminator = None

        self.type = type
        if protect_mode is not None:
            self.protect_mode = protect_mode
        if monitor_process is not None:
            self.monitor_process = monitor_process
        if privileged_process_list is not None:
            self.privileged_process_list = privileged_process_list
        if privileged_child is not None:
            self.privileged_child = privileged_child
        if container_wtp_info is not None:
            self.container_wtp_info = container_wtp_info
        if open_protection_immediately is not None:
            self.open_protection_immediately = open_protection_immediately
        if quota_info is not None:
            self.quota_info = quota_info

    @property
    def type(self):
        r"""Gets the type of this CreateWebTamperProtectionConfigRequestBody.

        **参数解释**: 网页防篡改的类型 **约束限制**: 不涉及 **取值范围**: - container_wtp：容器网页防篡改  **默认取值**: 不涉及 

        :return: The type of this CreateWebTamperProtectionConfigRequestBody.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this CreateWebTamperProtectionConfigRequestBody.

        **参数解释**: 网页防篡改的类型 **约束限制**: 不涉及 **取值范围**: - container_wtp：容器网页防篡改  **默认取值**: 不涉及 

        :param type: The type of this CreateWebTamperProtectionConfigRequestBody.
        :type type: str
        """
        self._type = type

    @property
    def protect_mode(self):
        r"""Gets the protect_mode of this CreateWebTamperProtectionConfigRequestBody.

        **参数解释**: 防护模式 **约束限制**: 不涉及 **取值范围**: - alarm：告警模式 - block：拦截模式  **默认取值**: alarm 

        :return: The protect_mode of this CreateWebTamperProtectionConfigRequestBody.
        :rtype: str
        """
        return self._protect_mode

    @protect_mode.setter
    def protect_mode(self, protect_mode):
        r"""Sets the protect_mode of this CreateWebTamperProtectionConfigRequestBody.

        **参数解释**: 防护模式 **约束限制**: 不涉及 **取值范围**: - alarm：告警模式 - block：拦截模式  **默认取值**: alarm 

        :param protect_mode: The protect_mode of this CreateWebTamperProtectionConfigRequestBody.
        :type protect_mode: str
        """
        self._protect_mode = protect_mode

    @property
    def monitor_process(self):
        r"""Gets the monitor_process of this CreateWebTamperProtectionConfigRequestBody.

        **参数解释**: 是否对篡改行为进行进程监控 **约束限制**: 不涉及 **取值范围**: - true：监控篡改进程 - false：不监控篡改进程  **默认取值**: true 

        :return: The monitor_process of this CreateWebTamperProtectionConfigRequestBody.
        :rtype: bool
        """
        return self._monitor_process

    @monitor_process.setter
    def monitor_process(self, monitor_process):
        r"""Sets the monitor_process of this CreateWebTamperProtectionConfigRequestBody.

        **参数解释**: 是否对篡改行为进行进程监控 **约束限制**: 不涉及 **取值范围**: - true：监控篡改进程 - false：不监控篡改进程  **默认取值**: true 

        :param monitor_process: The monitor_process of this CreateWebTamperProtectionConfigRequestBody.
        :type monitor_process: bool
        """
        self._monitor_process = monitor_process

    @property
    def privileged_process_list(self):
        r"""Gets the privileged_process_list of this CreateWebTamperProtectionConfigRequestBody.

        **参数解释**: 特权进程路径列表 **约束限制**: monitor_process值为true时生效（不进行进程监控无法判断特权进程） **取值范围**: 最少0条，最多10条 **默认取值**: 不涉及 

        :return: The privileged_process_list of this CreateWebTamperProtectionConfigRequestBody.
        :rtype: list[str]
        """
        return self._privileged_process_list

    @privileged_process_list.setter
    def privileged_process_list(self, privileged_process_list):
        r"""Sets the privileged_process_list of this CreateWebTamperProtectionConfigRequestBody.

        **参数解释**: 特权进程路径列表 **约束限制**: monitor_process值为true时生效（不进行进程监控无法判断特权进程） **取值范围**: 最少0条，最多10条 **默认取值**: 不涉及 

        :param privileged_process_list: The privileged_process_list of this CreateWebTamperProtectionConfigRequestBody.
        :type privileged_process_list: list[str]
        """
        self._privileged_process_list = privileged_process_list

    @property
    def privileged_child(self):
        r"""Gets the privileged_child of this CreateWebTamperProtectionConfigRequestBody.

        **参数解释**: 特权进程的子进程是否仍享有特权 **约束限制**: monitor_process值为true时生效（不进行进程监控无法判断特权进程） **取值范围**: - true：特权进程的子进程依然是特权进程 - false：特权进程的子进程不再是特权进程  **默认取值**: false 

        :return: The privileged_child of this CreateWebTamperProtectionConfigRequestBody.
        :rtype: bool
        """
        return self._privileged_child

    @privileged_child.setter
    def privileged_child(self, privileged_child):
        r"""Sets the privileged_child of this CreateWebTamperProtectionConfigRequestBody.

        **参数解释**: 特权进程的子进程是否仍享有特权 **约束限制**: monitor_process值为true时生效（不进行进程监控无法判断特权进程） **取值范围**: - true：特权进程的子进程依然是特权进程 - false：特权进程的子进程不再是特权进程  **默认取值**: false 

        :param privileged_child: The privileged_child of this CreateWebTamperProtectionConfigRequestBody.
        :type privileged_child: bool
        """
        self._privileged_child = privileged_child

    @property
    def container_wtp_info(self):
        r"""Gets the container_wtp_info of this CreateWebTamperProtectionConfigRequestBody.

        :return: The container_wtp_info of this CreateWebTamperProtectionConfigRequestBody.
        :rtype: :class:`huaweicloudsdkhss.v5.CreateWebTamperProtectionConfigRequestBodyContainerWtpInfo`
        """
        return self._container_wtp_info

    @container_wtp_info.setter
    def container_wtp_info(self, container_wtp_info):
        r"""Sets the container_wtp_info of this CreateWebTamperProtectionConfigRequestBody.

        :param container_wtp_info: The container_wtp_info of this CreateWebTamperProtectionConfigRequestBody.
        :type container_wtp_info: :class:`huaweicloudsdkhss.v5.CreateWebTamperProtectionConfigRequestBodyContainerWtpInfo`
        """
        self._container_wtp_info = container_wtp_info

    @property
    def open_protection_immediately(self):
        r"""Gets the open_protection_immediately of this CreateWebTamperProtectionConfigRequestBody.

        **参数解释**: 是否立即开启防护 **约束限制**: 不涉及 **取值范围**: - true：立即开启防护 - false：只保存配置内容，暂不开启防护  **默认取值**: false 

        :return: The open_protection_immediately of this CreateWebTamperProtectionConfigRequestBody.
        :rtype: bool
        """
        return self._open_protection_immediately

    @open_protection_immediately.setter
    def open_protection_immediately(self, open_protection_immediately):
        r"""Sets the open_protection_immediately of this CreateWebTamperProtectionConfigRequestBody.

        **参数解释**: 是否立即开启防护 **约束限制**: 不涉及 **取值范围**: - true：立即开启防护 - false：只保存配置内容，暂不开启防护  **默认取值**: false 

        :param open_protection_immediately: The open_protection_immediately of this CreateWebTamperProtectionConfigRequestBody.
        :type open_protection_immediately: bool
        """
        self._open_protection_immediately = open_protection_immediately

    @property
    def quota_info(self):
        r"""Gets the quota_info of this CreateWebTamperProtectionConfigRequestBody.

        :return: The quota_info of this CreateWebTamperProtectionConfigRequestBody.
        :rtype: :class:`huaweicloudsdkhss.v5.CreateWebTamperProtectionConfigRequestBodyQuotaInfo`
        """
        return self._quota_info

    @quota_info.setter
    def quota_info(self, quota_info):
        r"""Sets the quota_info of this CreateWebTamperProtectionConfigRequestBody.

        :param quota_info: The quota_info of this CreateWebTamperProtectionConfigRequestBody.
        :type quota_info: :class:`huaweicloudsdkhss.v5.CreateWebTamperProtectionConfigRequestBodyQuotaInfo`
        """
        self._quota_info = quota_info

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CreateWebTamperProtectionConfigRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
