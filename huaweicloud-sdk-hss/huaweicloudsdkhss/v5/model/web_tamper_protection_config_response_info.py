# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WebTamperProtectionConfigResponseInfo:

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
        'protect_mode': 'str',
        'monitor_process': 'bool',
        'privileged_process_list': 'list[str]',
        'privileged_child': 'bool',
        'protect_directory_info_list': 'list[ProtectDirectoryResponseInfo]',
        'exclude_file_types': 'list[str]',
        'status': 'str',
        'protected_container_nums': 'int',
        'protected_event_nums': 'int',
        'resource_id': 'str',
        'container_wtp_info': 'WebTamperProtectionConfigResponseInfoContainerWtpInfo'
    }

    attribute_map = {
        'id': 'id',
        'protect_mode': 'protect_mode',
        'monitor_process': 'monitor_process',
        'privileged_process_list': 'privileged_process_list',
        'privileged_child': 'privileged_child',
        'protect_directory_info_list': 'protect_directory_info_list',
        'exclude_file_types': 'exclude_file_types',
        'status': 'status',
        'protected_container_nums': 'protected_container_nums',
        'protected_event_nums': 'protected_event_nums',
        'resource_id': 'resource_id',
        'container_wtp_info': 'container_wtp_info'
    }

    def __init__(self, id=None, protect_mode=None, monitor_process=None, privileged_process_list=None, privileged_child=None, protect_directory_info_list=None, exclude_file_types=None, status=None, protected_container_nums=None, protected_event_nums=None, resource_id=None, container_wtp_info=None):
        r"""WebTamperProtectionConfigResponseInfo

        The model defined in huaweicloud sdk

        :param id: **参数解释**: 网页防篡改配置id **取值范围**: 字符长度1-64位 
        :type id: str
        :param protect_mode: **参数解释**: 防护模式 **取值范围**: - alarm：告警模式 - block：拦截模式 
        :type protect_mode: str
        :param monitor_process: **参数解释**: 是否对篡改行为进行进程监控 **取值范围**: - true：监控篡改进程 - false：不监控篡改进程 
        :type monitor_process: bool
        :param privileged_process_list: **参数解释**: 特权进程路径列表 **取值范围**: 最少0条，最多10条 
        :type privileged_process_list: list[str]
        :param privileged_child: **参数解释**: 特权进程的子进程是否仍享有特权 **取值范围**: - true：特权进程的子进程依然是特权进程 - false：特权进程的子进程不再是特权进程 
        :type privileged_child: bool
        :param protect_directory_info_list: **参数解释**： 防护目录信息 **取值范围**： 最少1条，最多50条 
        :type protect_directory_info_list: list[:class:`huaweicloudsdkhss.v5.ProtectDirectoryResponseInfo`]
        :param exclude_file_types: **参数解释**： 防护排除的文件类型列表 **取值范围**： 最少0条，最多10条 
        :type exclude_file_types: list[str]
        :param status: **参数解释**: 防护状态 **取值范围**: - not_protect：未防护 - protected：防护中 - partial_protected：部分防护 - protect_failed：防护失败 - redundant：防护冗余 
        :type status: str
        :param protected_container_nums: **参数解释**: 防护中的容器数量 **取值范围**: 最小值0，最大值2147483647 
        :type protected_container_nums: int
        :param protected_event_nums: **参数解释**: 当前防护配置产生的防护事件数量 **取值范围**: 最小值0，最大值2147483647 
        :type protected_event_nums: int
        :param resource_id: **参数解释**: 防护配置绑定的配额id **取值范围**: 字符长度1-64位 
        :type resource_id: str
        :param container_wtp_info: 
        :type container_wtp_info: :class:`huaweicloudsdkhss.v5.WebTamperProtectionConfigResponseInfoContainerWtpInfo`
        """
        
        

        self._id = None
        self._protect_mode = None
        self._monitor_process = None
        self._privileged_process_list = None
        self._privileged_child = None
        self._protect_directory_info_list = None
        self._exclude_file_types = None
        self._status = None
        self._protected_container_nums = None
        self._protected_event_nums = None
        self._resource_id = None
        self._container_wtp_info = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if protect_mode is not None:
            self.protect_mode = protect_mode
        if monitor_process is not None:
            self.monitor_process = monitor_process
        if privileged_process_list is not None:
            self.privileged_process_list = privileged_process_list
        if privileged_child is not None:
            self.privileged_child = privileged_child
        if protect_directory_info_list is not None:
            self.protect_directory_info_list = protect_directory_info_list
        if exclude_file_types is not None:
            self.exclude_file_types = exclude_file_types
        if status is not None:
            self.status = status
        if protected_container_nums is not None:
            self.protected_container_nums = protected_container_nums
        if protected_event_nums is not None:
            self.protected_event_nums = protected_event_nums
        if resource_id is not None:
            self.resource_id = resource_id
        if container_wtp_info is not None:
            self.container_wtp_info = container_wtp_info

    @property
    def id(self):
        r"""Gets the id of this WebTamperProtectionConfigResponseInfo.

        **参数解释**: 网页防篡改配置id **取值范围**: 字符长度1-64位 

        :return: The id of this WebTamperProtectionConfigResponseInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this WebTamperProtectionConfigResponseInfo.

        **参数解释**: 网页防篡改配置id **取值范围**: 字符长度1-64位 

        :param id: The id of this WebTamperProtectionConfigResponseInfo.
        :type id: str
        """
        self._id = id

    @property
    def protect_mode(self):
        r"""Gets the protect_mode of this WebTamperProtectionConfigResponseInfo.

        **参数解释**: 防护模式 **取值范围**: - alarm：告警模式 - block：拦截模式 

        :return: The protect_mode of this WebTamperProtectionConfigResponseInfo.
        :rtype: str
        """
        return self._protect_mode

    @protect_mode.setter
    def protect_mode(self, protect_mode):
        r"""Sets the protect_mode of this WebTamperProtectionConfigResponseInfo.

        **参数解释**: 防护模式 **取值范围**: - alarm：告警模式 - block：拦截模式 

        :param protect_mode: The protect_mode of this WebTamperProtectionConfigResponseInfo.
        :type protect_mode: str
        """
        self._protect_mode = protect_mode

    @property
    def monitor_process(self):
        r"""Gets the monitor_process of this WebTamperProtectionConfigResponseInfo.

        **参数解释**: 是否对篡改行为进行进程监控 **取值范围**: - true：监控篡改进程 - false：不监控篡改进程 

        :return: The monitor_process of this WebTamperProtectionConfigResponseInfo.
        :rtype: bool
        """
        return self._monitor_process

    @monitor_process.setter
    def monitor_process(self, monitor_process):
        r"""Sets the monitor_process of this WebTamperProtectionConfigResponseInfo.

        **参数解释**: 是否对篡改行为进行进程监控 **取值范围**: - true：监控篡改进程 - false：不监控篡改进程 

        :param monitor_process: The monitor_process of this WebTamperProtectionConfigResponseInfo.
        :type monitor_process: bool
        """
        self._monitor_process = monitor_process

    @property
    def privileged_process_list(self):
        r"""Gets the privileged_process_list of this WebTamperProtectionConfigResponseInfo.

        **参数解释**: 特权进程路径列表 **取值范围**: 最少0条，最多10条 

        :return: The privileged_process_list of this WebTamperProtectionConfigResponseInfo.
        :rtype: list[str]
        """
        return self._privileged_process_list

    @privileged_process_list.setter
    def privileged_process_list(self, privileged_process_list):
        r"""Sets the privileged_process_list of this WebTamperProtectionConfigResponseInfo.

        **参数解释**: 特权进程路径列表 **取值范围**: 最少0条，最多10条 

        :param privileged_process_list: The privileged_process_list of this WebTamperProtectionConfigResponseInfo.
        :type privileged_process_list: list[str]
        """
        self._privileged_process_list = privileged_process_list

    @property
    def privileged_child(self):
        r"""Gets the privileged_child of this WebTamperProtectionConfigResponseInfo.

        **参数解释**: 特权进程的子进程是否仍享有特权 **取值范围**: - true：特权进程的子进程依然是特权进程 - false：特权进程的子进程不再是特权进程 

        :return: The privileged_child of this WebTamperProtectionConfigResponseInfo.
        :rtype: bool
        """
        return self._privileged_child

    @privileged_child.setter
    def privileged_child(self, privileged_child):
        r"""Sets the privileged_child of this WebTamperProtectionConfigResponseInfo.

        **参数解释**: 特权进程的子进程是否仍享有特权 **取值范围**: - true：特权进程的子进程依然是特权进程 - false：特权进程的子进程不再是特权进程 

        :param privileged_child: The privileged_child of this WebTamperProtectionConfigResponseInfo.
        :type privileged_child: bool
        """
        self._privileged_child = privileged_child

    @property
    def protect_directory_info_list(self):
        r"""Gets the protect_directory_info_list of this WebTamperProtectionConfigResponseInfo.

        **参数解释**： 防护目录信息 **取值范围**： 最少1条，最多50条 

        :return: The protect_directory_info_list of this WebTamperProtectionConfigResponseInfo.
        :rtype: list[:class:`huaweicloudsdkhss.v5.ProtectDirectoryResponseInfo`]
        """
        return self._protect_directory_info_list

    @protect_directory_info_list.setter
    def protect_directory_info_list(self, protect_directory_info_list):
        r"""Sets the protect_directory_info_list of this WebTamperProtectionConfigResponseInfo.

        **参数解释**： 防护目录信息 **取值范围**： 最少1条，最多50条 

        :param protect_directory_info_list: The protect_directory_info_list of this WebTamperProtectionConfigResponseInfo.
        :type protect_directory_info_list: list[:class:`huaweicloudsdkhss.v5.ProtectDirectoryResponseInfo`]
        """
        self._protect_directory_info_list = protect_directory_info_list

    @property
    def exclude_file_types(self):
        r"""Gets the exclude_file_types of this WebTamperProtectionConfigResponseInfo.

        **参数解释**： 防护排除的文件类型列表 **取值范围**： 最少0条，最多10条 

        :return: The exclude_file_types of this WebTamperProtectionConfigResponseInfo.
        :rtype: list[str]
        """
        return self._exclude_file_types

    @exclude_file_types.setter
    def exclude_file_types(self, exclude_file_types):
        r"""Sets the exclude_file_types of this WebTamperProtectionConfigResponseInfo.

        **参数解释**： 防护排除的文件类型列表 **取值范围**： 最少0条，最多10条 

        :param exclude_file_types: The exclude_file_types of this WebTamperProtectionConfigResponseInfo.
        :type exclude_file_types: list[str]
        """
        self._exclude_file_types = exclude_file_types

    @property
    def status(self):
        r"""Gets the status of this WebTamperProtectionConfigResponseInfo.

        **参数解释**: 防护状态 **取值范围**: - not_protect：未防护 - protected：防护中 - partial_protected：部分防护 - protect_failed：防护失败 - redundant：防护冗余 

        :return: The status of this WebTamperProtectionConfigResponseInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this WebTamperProtectionConfigResponseInfo.

        **参数解释**: 防护状态 **取值范围**: - not_protect：未防护 - protected：防护中 - partial_protected：部分防护 - protect_failed：防护失败 - redundant：防护冗余 

        :param status: The status of this WebTamperProtectionConfigResponseInfo.
        :type status: str
        """
        self._status = status

    @property
    def protected_container_nums(self):
        r"""Gets the protected_container_nums of this WebTamperProtectionConfigResponseInfo.

        **参数解释**: 防护中的容器数量 **取值范围**: 最小值0，最大值2147483647 

        :return: The protected_container_nums of this WebTamperProtectionConfigResponseInfo.
        :rtype: int
        """
        return self._protected_container_nums

    @protected_container_nums.setter
    def protected_container_nums(self, protected_container_nums):
        r"""Sets the protected_container_nums of this WebTamperProtectionConfigResponseInfo.

        **参数解释**: 防护中的容器数量 **取值范围**: 最小值0，最大值2147483647 

        :param protected_container_nums: The protected_container_nums of this WebTamperProtectionConfigResponseInfo.
        :type protected_container_nums: int
        """
        self._protected_container_nums = protected_container_nums

    @property
    def protected_event_nums(self):
        r"""Gets the protected_event_nums of this WebTamperProtectionConfigResponseInfo.

        **参数解释**: 当前防护配置产生的防护事件数量 **取值范围**: 最小值0，最大值2147483647 

        :return: The protected_event_nums of this WebTamperProtectionConfigResponseInfo.
        :rtype: int
        """
        return self._protected_event_nums

    @protected_event_nums.setter
    def protected_event_nums(self, protected_event_nums):
        r"""Sets the protected_event_nums of this WebTamperProtectionConfigResponseInfo.

        **参数解释**: 当前防护配置产生的防护事件数量 **取值范围**: 最小值0，最大值2147483647 

        :param protected_event_nums: The protected_event_nums of this WebTamperProtectionConfigResponseInfo.
        :type protected_event_nums: int
        """
        self._protected_event_nums = protected_event_nums

    @property
    def resource_id(self):
        r"""Gets the resource_id of this WebTamperProtectionConfigResponseInfo.

        **参数解释**: 防护配置绑定的配额id **取值范围**: 字符长度1-64位 

        :return: The resource_id of this WebTamperProtectionConfigResponseInfo.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this WebTamperProtectionConfigResponseInfo.

        **参数解释**: 防护配置绑定的配额id **取值范围**: 字符长度1-64位 

        :param resource_id: The resource_id of this WebTamperProtectionConfigResponseInfo.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def container_wtp_info(self):
        r"""Gets the container_wtp_info of this WebTamperProtectionConfigResponseInfo.

        :return: The container_wtp_info of this WebTamperProtectionConfigResponseInfo.
        :rtype: :class:`huaweicloudsdkhss.v5.WebTamperProtectionConfigResponseInfoContainerWtpInfo`
        """
        return self._container_wtp_info

    @container_wtp_info.setter
    def container_wtp_info(self, container_wtp_info):
        r"""Sets the container_wtp_info of this WebTamperProtectionConfigResponseInfo.

        :param container_wtp_info: The container_wtp_info of this WebTamperProtectionConfigResponseInfo.
        :type container_wtp_info: :class:`huaweicloudsdkhss.v5.WebTamperProtectionConfigResponseInfoContainerWtpInfo`
        """
        self._container_wtp_info = container_wtp_info

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
        if not isinstance(other, WebTamperProtectionConfigResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
