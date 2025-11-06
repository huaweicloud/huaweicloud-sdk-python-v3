# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EventForensicInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'occur_time': 'int',
        'file_forensic_list': 'list[FileForensicInfo]',
        'process_chain_forensic': 'list[list[ProcessForensicInfo]]',
        'network_forensic': 'EventForensicInfoNetworkForensic',
        'user_forensic': 'EventForensicInfoUserForensic',
        'registry_forensic': 'EventForensicInfoRegistryForensic',
        'abnormal_login_forensic': 'EventForensicInfoAbnormalLoginForensic',
        'container_forensic': 'EventForensicInfoContainerForensic',
        'malware_forensic': 'EventForensicInfoMalwareForensic',
        'auto_launch_forensic': 'EventForensicInfoAutoLaunchForensic',
        'kernel_forensic_list': 'list[KernelForensicInfo]',
        'geo_forensic': 'EventForensicInfoGeoForensic',
        'stack_forensic': 'EventForensicInfoStackForensic',
        'image_block_forensic': 'EventForensicInfoImageBlockForensic',
        'honey_forensic': 'list[HoneyForensicInfo]'
    }

    attribute_map = {
        'occur_time': 'occur_time',
        'file_forensic_list': 'file_forensic_list',
        'process_chain_forensic': 'process_chain_forensic',
        'network_forensic': 'network_forensic',
        'user_forensic': 'user_forensic',
        'registry_forensic': 'registry_forensic',
        'abnormal_login_forensic': 'abnormal_login_forensic',
        'container_forensic': 'container_forensic',
        'malware_forensic': 'malware_forensic',
        'auto_launch_forensic': 'auto_launch_forensic',
        'kernel_forensic_list': 'kernel_forensic_list',
        'geo_forensic': 'geo_forensic',
        'stack_forensic': 'stack_forensic',
        'image_block_forensic': 'image_block_forensic',
        'honey_forensic': 'honey_forensic'
    }

    def __init__(self, occur_time=None, file_forensic_list=None, process_chain_forensic=None, network_forensic=None, user_forensic=None, registry_forensic=None, abnormal_login_forensic=None, container_forensic=None, malware_forensic=None, auto_launch_forensic=None, kernel_forensic_list=None, geo_forensic=None, stack_forensic=None, image_block_forensic=None, honey_forensic=None):
        r"""EventForensicInfo

        The model defined in huaweicloud sdk

        :param occur_time: **参数解释**： 发生时间，毫秒 **取值范围**： 不涉及
        :type occur_time: int
        :param file_forensic_list: **参数解释**： 文件取证信息列表 **取值范围**： 不涉及
        :type file_forensic_list: list[:class:`huaweicloudsdkhss.v5.FileForensicInfo`]
        :param process_chain_forensic: **参数解释**： 进程链取证信息 **取值范围**： 不涉及
        :type process_chain_forensic: list[list[ProcessForensicInfo]]
        :param network_forensic: 
        :type network_forensic: :class:`huaweicloudsdkhss.v5.EventForensicInfoNetworkForensic`
        :param user_forensic: 
        :type user_forensic: :class:`huaweicloudsdkhss.v5.EventForensicInfoUserForensic`
        :param registry_forensic: 
        :type registry_forensic: :class:`huaweicloudsdkhss.v5.EventForensicInfoRegistryForensic`
        :param abnormal_login_forensic: 
        :type abnormal_login_forensic: :class:`huaweicloudsdkhss.v5.EventForensicInfoAbnormalLoginForensic`
        :param container_forensic: 
        :type container_forensic: :class:`huaweicloudsdkhss.v5.EventForensicInfoContainerForensic`
        :param malware_forensic: 
        :type malware_forensic: :class:`huaweicloudsdkhss.v5.EventForensicInfoMalwareForensic`
        :param auto_launch_forensic: 
        :type auto_launch_forensic: :class:`huaweicloudsdkhss.v5.EventForensicInfoAutoLaunchForensic`
        :param kernel_forensic_list: **参数解释**： 内核取证信息 **取值范围**： 不涉及
        :type kernel_forensic_list: list[:class:`huaweicloudsdkhss.v5.KernelForensicInfo`]
        :param geo_forensic: 
        :type geo_forensic: :class:`huaweicloudsdkhss.v5.EventForensicInfoGeoForensic`
        :param stack_forensic: 
        :type stack_forensic: :class:`huaweicloudsdkhss.v5.EventForensicInfoStackForensic`
        :param image_block_forensic: 
        :type image_block_forensic: :class:`huaweicloudsdkhss.v5.EventForensicInfoImageBlockForensic`
        :param honey_forensic: **参数解释**： 蜜罐相关取证信息 **取值范围**： 不涉及
        :type honey_forensic: list[:class:`huaweicloudsdkhss.v5.HoneyForensicInfo`]
        """
        
        

        self._occur_time = None
        self._file_forensic_list = None
        self._process_chain_forensic = None
        self._network_forensic = None
        self._user_forensic = None
        self._registry_forensic = None
        self._abnormal_login_forensic = None
        self._container_forensic = None
        self._malware_forensic = None
        self._auto_launch_forensic = None
        self._kernel_forensic_list = None
        self._geo_forensic = None
        self._stack_forensic = None
        self._image_block_forensic = None
        self._honey_forensic = None
        self.discriminator = None

        if occur_time is not None:
            self.occur_time = occur_time
        if file_forensic_list is not None:
            self.file_forensic_list = file_forensic_list
        if process_chain_forensic is not None:
            self.process_chain_forensic = process_chain_forensic
        if network_forensic is not None:
            self.network_forensic = network_forensic
        if user_forensic is not None:
            self.user_forensic = user_forensic
        if registry_forensic is not None:
            self.registry_forensic = registry_forensic
        if abnormal_login_forensic is not None:
            self.abnormal_login_forensic = abnormal_login_forensic
        if container_forensic is not None:
            self.container_forensic = container_forensic
        if malware_forensic is not None:
            self.malware_forensic = malware_forensic
        if auto_launch_forensic is not None:
            self.auto_launch_forensic = auto_launch_forensic
        if kernel_forensic_list is not None:
            self.kernel_forensic_list = kernel_forensic_list
        if geo_forensic is not None:
            self.geo_forensic = geo_forensic
        if stack_forensic is not None:
            self.stack_forensic = stack_forensic
        if image_block_forensic is not None:
            self.image_block_forensic = image_block_forensic
        if honey_forensic is not None:
            self.honey_forensic = honey_forensic

    @property
    def occur_time(self):
        r"""Gets the occur_time of this EventForensicInfo.

        **参数解释**： 发生时间，毫秒 **取值范围**： 不涉及

        :return: The occur_time of this EventForensicInfo.
        :rtype: int
        """
        return self._occur_time

    @occur_time.setter
    def occur_time(self, occur_time):
        r"""Sets the occur_time of this EventForensicInfo.

        **参数解释**： 发生时间，毫秒 **取值范围**： 不涉及

        :param occur_time: The occur_time of this EventForensicInfo.
        :type occur_time: int
        """
        self._occur_time = occur_time

    @property
    def file_forensic_list(self):
        r"""Gets the file_forensic_list of this EventForensicInfo.

        **参数解释**： 文件取证信息列表 **取值范围**： 不涉及

        :return: The file_forensic_list of this EventForensicInfo.
        :rtype: list[:class:`huaweicloudsdkhss.v5.FileForensicInfo`]
        """
        return self._file_forensic_list

    @file_forensic_list.setter
    def file_forensic_list(self, file_forensic_list):
        r"""Sets the file_forensic_list of this EventForensicInfo.

        **参数解释**： 文件取证信息列表 **取值范围**： 不涉及

        :param file_forensic_list: The file_forensic_list of this EventForensicInfo.
        :type file_forensic_list: list[:class:`huaweicloudsdkhss.v5.FileForensicInfo`]
        """
        self._file_forensic_list = file_forensic_list

    @property
    def process_chain_forensic(self):
        r"""Gets the process_chain_forensic of this EventForensicInfo.

        **参数解释**： 进程链取证信息 **取值范围**： 不涉及

        :return: The process_chain_forensic of this EventForensicInfo.
        :rtype: list[list[ProcessForensicInfo]]
        """
        return self._process_chain_forensic

    @process_chain_forensic.setter
    def process_chain_forensic(self, process_chain_forensic):
        r"""Sets the process_chain_forensic of this EventForensicInfo.

        **参数解释**： 进程链取证信息 **取值范围**： 不涉及

        :param process_chain_forensic: The process_chain_forensic of this EventForensicInfo.
        :type process_chain_forensic: list[list[ProcessForensicInfo]]
        """
        self._process_chain_forensic = process_chain_forensic

    @property
    def network_forensic(self):
        r"""Gets the network_forensic of this EventForensicInfo.

        :return: The network_forensic of this EventForensicInfo.
        :rtype: :class:`huaweicloudsdkhss.v5.EventForensicInfoNetworkForensic`
        """
        return self._network_forensic

    @network_forensic.setter
    def network_forensic(self, network_forensic):
        r"""Sets the network_forensic of this EventForensicInfo.

        :param network_forensic: The network_forensic of this EventForensicInfo.
        :type network_forensic: :class:`huaweicloudsdkhss.v5.EventForensicInfoNetworkForensic`
        """
        self._network_forensic = network_forensic

    @property
    def user_forensic(self):
        r"""Gets the user_forensic of this EventForensicInfo.

        :return: The user_forensic of this EventForensicInfo.
        :rtype: :class:`huaweicloudsdkhss.v5.EventForensicInfoUserForensic`
        """
        return self._user_forensic

    @user_forensic.setter
    def user_forensic(self, user_forensic):
        r"""Sets the user_forensic of this EventForensicInfo.

        :param user_forensic: The user_forensic of this EventForensicInfo.
        :type user_forensic: :class:`huaweicloudsdkhss.v5.EventForensicInfoUserForensic`
        """
        self._user_forensic = user_forensic

    @property
    def registry_forensic(self):
        r"""Gets the registry_forensic of this EventForensicInfo.

        :return: The registry_forensic of this EventForensicInfo.
        :rtype: :class:`huaweicloudsdkhss.v5.EventForensicInfoRegistryForensic`
        """
        return self._registry_forensic

    @registry_forensic.setter
    def registry_forensic(self, registry_forensic):
        r"""Sets the registry_forensic of this EventForensicInfo.

        :param registry_forensic: The registry_forensic of this EventForensicInfo.
        :type registry_forensic: :class:`huaweicloudsdkhss.v5.EventForensicInfoRegistryForensic`
        """
        self._registry_forensic = registry_forensic

    @property
    def abnormal_login_forensic(self):
        r"""Gets the abnormal_login_forensic of this EventForensicInfo.

        :return: The abnormal_login_forensic of this EventForensicInfo.
        :rtype: :class:`huaweicloudsdkhss.v5.EventForensicInfoAbnormalLoginForensic`
        """
        return self._abnormal_login_forensic

    @abnormal_login_forensic.setter
    def abnormal_login_forensic(self, abnormal_login_forensic):
        r"""Sets the abnormal_login_forensic of this EventForensicInfo.

        :param abnormal_login_forensic: The abnormal_login_forensic of this EventForensicInfo.
        :type abnormal_login_forensic: :class:`huaweicloudsdkhss.v5.EventForensicInfoAbnormalLoginForensic`
        """
        self._abnormal_login_forensic = abnormal_login_forensic

    @property
    def container_forensic(self):
        r"""Gets the container_forensic of this EventForensicInfo.

        :return: The container_forensic of this EventForensicInfo.
        :rtype: :class:`huaweicloudsdkhss.v5.EventForensicInfoContainerForensic`
        """
        return self._container_forensic

    @container_forensic.setter
    def container_forensic(self, container_forensic):
        r"""Sets the container_forensic of this EventForensicInfo.

        :param container_forensic: The container_forensic of this EventForensicInfo.
        :type container_forensic: :class:`huaweicloudsdkhss.v5.EventForensicInfoContainerForensic`
        """
        self._container_forensic = container_forensic

    @property
    def malware_forensic(self):
        r"""Gets the malware_forensic of this EventForensicInfo.

        :return: The malware_forensic of this EventForensicInfo.
        :rtype: :class:`huaweicloudsdkhss.v5.EventForensicInfoMalwareForensic`
        """
        return self._malware_forensic

    @malware_forensic.setter
    def malware_forensic(self, malware_forensic):
        r"""Sets the malware_forensic of this EventForensicInfo.

        :param malware_forensic: The malware_forensic of this EventForensicInfo.
        :type malware_forensic: :class:`huaweicloudsdkhss.v5.EventForensicInfoMalwareForensic`
        """
        self._malware_forensic = malware_forensic

    @property
    def auto_launch_forensic(self):
        r"""Gets the auto_launch_forensic of this EventForensicInfo.

        :return: The auto_launch_forensic of this EventForensicInfo.
        :rtype: :class:`huaweicloudsdkhss.v5.EventForensicInfoAutoLaunchForensic`
        """
        return self._auto_launch_forensic

    @auto_launch_forensic.setter
    def auto_launch_forensic(self, auto_launch_forensic):
        r"""Sets the auto_launch_forensic of this EventForensicInfo.

        :param auto_launch_forensic: The auto_launch_forensic of this EventForensicInfo.
        :type auto_launch_forensic: :class:`huaweicloudsdkhss.v5.EventForensicInfoAutoLaunchForensic`
        """
        self._auto_launch_forensic = auto_launch_forensic

    @property
    def kernel_forensic_list(self):
        r"""Gets the kernel_forensic_list of this EventForensicInfo.

        **参数解释**： 内核取证信息 **取值范围**： 不涉及

        :return: The kernel_forensic_list of this EventForensicInfo.
        :rtype: list[:class:`huaweicloudsdkhss.v5.KernelForensicInfo`]
        """
        return self._kernel_forensic_list

    @kernel_forensic_list.setter
    def kernel_forensic_list(self, kernel_forensic_list):
        r"""Sets the kernel_forensic_list of this EventForensicInfo.

        **参数解释**： 内核取证信息 **取值范围**： 不涉及

        :param kernel_forensic_list: The kernel_forensic_list of this EventForensicInfo.
        :type kernel_forensic_list: list[:class:`huaweicloudsdkhss.v5.KernelForensicInfo`]
        """
        self._kernel_forensic_list = kernel_forensic_list

    @property
    def geo_forensic(self):
        r"""Gets the geo_forensic of this EventForensicInfo.

        :return: The geo_forensic of this EventForensicInfo.
        :rtype: :class:`huaweicloudsdkhss.v5.EventForensicInfoGeoForensic`
        """
        return self._geo_forensic

    @geo_forensic.setter
    def geo_forensic(self, geo_forensic):
        r"""Sets the geo_forensic of this EventForensicInfo.

        :param geo_forensic: The geo_forensic of this EventForensicInfo.
        :type geo_forensic: :class:`huaweicloudsdkhss.v5.EventForensicInfoGeoForensic`
        """
        self._geo_forensic = geo_forensic

    @property
    def stack_forensic(self):
        r"""Gets the stack_forensic of this EventForensicInfo.

        :return: The stack_forensic of this EventForensicInfo.
        :rtype: :class:`huaweicloudsdkhss.v5.EventForensicInfoStackForensic`
        """
        return self._stack_forensic

    @stack_forensic.setter
    def stack_forensic(self, stack_forensic):
        r"""Sets the stack_forensic of this EventForensicInfo.

        :param stack_forensic: The stack_forensic of this EventForensicInfo.
        :type stack_forensic: :class:`huaweicloudsdkhss.v5.EventForensicInfoStackForensic`
        """
        self._stack_forensic = stack_forensic

    @property
    def image_block_forensic(self):
        r"""Gets the image_block_forensic of this EventForensicInfo.

        :return: The image_block_forensic of this EventForensicInfo.
        :rtype: :class:`huaweicloudsdkhss.v5.EventForensicInfoImageBlockForensic`
        """
        return self._image_block_forensic

    @image_block_forensic.setter
    def image_block_forensic(self, image_block_forensic):
        r"""Sets the image_block_forensic of this EventForensicInfo.

        :param image_block_forensic: The image_block_forensic of this EventForensicInfo.
        :type image_block_forensic: :class:`huaweicloudsdkhss.v5.EventForensicInfoImageBlockForensic`
        """
        self._image_block_forensic = image_block_forensic

    @property
    def honey_forensic(self):
        r"""Gets the honey_forensic of this EventForensicInfo.

        **参数解释**： 蜜罐相关取证信息 **取值范围**： 不涉及

        :return: The honey_forensic of this EventForensicInfo.
        :rtype: list[:class:`huaweicloudsdkhss.v5.HoneyForensicInfo`]
        """
        return self._honey_forensic

    @honey_forensic.setter
    def honey_forensic(self, honey_forensic):
        r"""Sets the honey_forensic of this EventForensicInfo.

        **参数解释**： 蜜罐相关取证信息 **取值范围**： 不涉及

        :param honey_forensic: The honey_forensic of this EventForensicInfo.
        :type honey_forensic: list[:class:`huaweicloudsdkhss.v5.HoneyForensicInfo`]
        """
        self._honey_forensic = honey_forensic

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
        if not isinstance(other, EventForensicInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
