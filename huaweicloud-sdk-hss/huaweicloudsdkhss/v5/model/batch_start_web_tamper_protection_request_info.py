# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchStartWebTamperProtectionRequestInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'host_id_list': 'list[str]',
        'charging_mode': 'str',
        'resource_id': 'str',
        'tags': 'list[TagInfo]',
        'protect_dir_info': 'WebTamperProtectDirRequestInfo',
        'enable_timing_off': 'bool',
        'timing_off_config_info': 'WebTamperTimingOffConfigInfoRequestInfo',
        'enable_rasp_protect': 'bool',
        'rasp_path': 'str',
        'enable_privileged_process': 'bool',
        'privileged_process_info': 'WebTamperPrivilegedProcessRequestInfo'
    }

    attribute_map = {
        'host_id_list': 'host_id_list',
        'charging_mode': 'charging_mode',
        'resource_id': 'resource_id',
        'tags': 'tags',
        'protect_dir_info': 'protect_dir_info',
        'enable_timing_off': 'enable_timing_off',
        'timing_off_config_info': 'timing_off_config_info',
        'enable_rasp_protect': 'enable_rasp_protect',
        'rasp_path': 'rasp_path',
        'enable_privileged_process': 'enable_privileged_process',
        'privileged_process_info': 'privileged_process_info'
    }

    def __init__(self, host_id_list=None, charging_mode=None, resource_id=None, tags=None, protect_dir_info=None, enable_timing_off=None, timing_off_config_info=None, enable_rasp_protect=None, rasp_path=None, enable_privileged_process=None, privileged_process_info=None):
        r"""BatchStartWebTamperProtectionRequestInfo

        The model defined in huaweicloud sdk

        :param host_id_list: **参数解释**: 需要开启防护的服务器ID列表，仅支持填写未开启网页防篡改防护的服务器ID，已开启网页防篡改防护的服务器可使用UpdateWebTamperHostPolicy接口进行修改策略。 **约束限制** : 仅支持填写未开启网页防篡改防护的服务器ID，且Linux服务器和Windows服务器不可同时填写，需分批开启。 **取值范围**: 最少1条，最多20000条 **默认取值** : 不涉及 
        :type host_id_list: list[str]
        :param charging_mode: **参数解释**: 计费模式 **约束限制**: 不涉及 **取值范围**: - packet_cycle: 包年/包月，可填写resource_id。 - on_demand: 按需计费，无需填写resource_id。  **默认取值**: on_demand 
        :type charging_mode: str
        :param resource_id: **参数解释**: 资源ID，即网页防篡改配额的配额ID，当charging_mode选择packet_cycle时可填写该字段，表示使用一个指定配额，也可不填写该字段，表示随机选择符合的配额。 **约束限制** : 不涉及 **取值范围**: 字符长度0-64位 **默认取值** : 不涉及 
        :type resource_id: str
        :param tags: **参数解释**： 资源标签列表，仅计费模式选择按需计费时支持填写。 **约束限制**: 仅计费模式选择按需计费时支持填写。 **取值范围**: 最少0条，最多2097152条 **默认取值**: 不涉及
        :type tags: list[:class:`huaweicloudsdkhss.v5.TagInfo`]
        :param protect_dir_info: 
        :type protect_dir_info: :class:`huaweicloudsdkhss.v5.WebTamperProtectDirRequestInfo`
        :param enable_timing_off: **参数解释**: 定时开关设置状态 **约束限制**: 不涉及 **取值范围**: - True ：开启定时关闭防护功能，必须填写timing_off_config_info。 - False ：关闭定时关闭防护功能，无需填写timing_off_config_info。  **默认取值**: False 
        :type enable_timing_off: bool
        :param timing_off_config_info: 
        :type timing_off_config_info: :class:`huaweicloudsdkhss.v5.WebTamperTimingOffConfigInfoRequestInfo`
        :param enable_rasp_protect: **参数解释**: 动态网页防篡改开启状态，仅Linux服务器支持。 **约束限制**: 仅Linux服务器支持开启动态网页防篡改，Windows服务器不可填写该字段。 **取值范围**: - True ：开启动态网页防篡改，必须填写rasp_path。 - False ：关闭动态网页防篡改，无需填写rasp_path。  **默认取值**: False 
        :type enable_rasp_protect: bool
        :param rasp_path: **参数解释**: 动态网页防篡改的Tomcat bin目录，仅Linux服务器支持。 **约束限制**: 仅Linux服务器支持配置动态网页防篡改的Tomcat bin目录，Windows服务器不可填写该字段。 **取值范围**: 字符长度1-256位，必须以/开头，不能以/结尾，只能包含英文大小写字母，数字，下划线，中划线和点。 **默认取值**: 不涉及 
        :type rasp_path: str
        :param enable_privileged_process: **参数解释**: 特权进程开启状态 **约束限制**: 不涉及 **取值范围**: - True ：开启特权进程，必须填写privileged_process_info。 - False ：关闭特权进程，无需填写privileged_process_info。  **默认取值**: False 
        :type enable_privileged_process: bool
        :param privileged_process_info: 
        :type privileged_process_info: :class:`huaweicloudsdkhss.v5.WebTamperPrivilegedProcessRequestInfo`
        """
        
        

        self._host_id_list = None
        self._charging_mode = None
        self._resource_id = None
        self._tags = None
        self._protect_dir_info = None
        self._enable_timing_off = None
        self._timing_off_config_info = None
        self._enable_rasp_protect = None
        self._rasp_path = None
        self._enable_privileged_process = None
        self._privileged_process_info = None
        self.discriminator = None

        self.host_id_list = host_id_list
        if charging_mode is not None:
            self.charging_mode = charging_mode
        if resource_id is not None:
            self.resource_id = resource_id
        if tags is not None:
            self.tags = tags
        self.protect_dir_info = protect_dir_info
        if enable_timing_off is not None:
            self.enable_timing_off = enable_timing_off
        if timing_off_config_info is not None:
            self.timing_off_config_info = timing_off_config_info
        if enable_rasp_protect is not None:
            self.enable_rasp_protect = enable_rasp_protect
        if rasp_path is not None:
            self.rasp_path = rasp_path
        if enable_privileged_process is not None:
            self.enable_privileged_process = enable_privileged_process
        if privileged_process_info is not None:
            self.privileged_process_info = privileged_process_info

    @property
    def host_id_list(self):
        r"""Gets the host_id_list of this BatchStartWebTamperProtectionRequestInfo.

        **参数解释**: 需要开启防护的服务器ID列表，仅支持填写未开启网页防篡改防护的服务器ID，已开启网页防篡改防护的服务器可使用UpdateWebTamperHostPolicy接口进行修改策略。 **约束限制** : 仅支持填写未开启网页防篡改防护的服务器ID，且Linux服务器和Windows服务器不可同时填写，需分批开启。 **取值范围**: 最少1条，最多20000条 **默认取值** : 不涉及 

        :return: The host_id_list of this BatchStartWebTamperProtectionRequestInfo.
        :rtype: list[str]
        """
        return self._host_id_list

    @host_id_list.setter
    def host_id_list(self, host_id_list):
        r"""Sets the host_id_list of this BatchStartWebTamperProtectionRequestInfo.

        **参数解释**: 需要开启防护的服务器ID列表，仅支持填写未开启网页防篡改防护的服务器ID，已开启网页防篡改防护的服务器可使用UpdateWebTamperHostPolicy接口进行修改策略。 **约束限制** : 仅支持填写未开启网页防篡改防护的服务器ID，且Linux服务器和Windows服务器不可同时填写，需分批开启。 **取值范围**: 最少1条，最多20000条 **默认取值** : 不涉及 

        :param host_id_list: The host_id_list of this BatchStartWebTamperProtectionRequestInfo.
        :type host_id_list: list[str]
        """
        self._host_id_list = host_id_list

    @property
    def charging_mode(self):
        r"""Gets the charging_mode of this BatchStartWebTamperProtectionRequestInfo.

        **参数解释**: 计费模式 **约束限制**: 不涉及 **取值范围**: - packet_cycle: 包年/包月，可填写resource_id。 - on_demand: 按需计费，无需填写resource_id。  **默认取值**: on_demand 

        :return: The charging_mode of this BatchStartWebTamperProtectionRequestInfo.
        :rtype: str
        """
        return self._charging_mode

    @charging_mode.setter
    def charging_mode(self, charging_mode):
        r"""Sets the charging_mode of this BatchStartWebTamperProtectionRequestInfo.

        **参数解释**: 计费模式 **约束限制**: 不涉及 **取值范围**: - packet_cycle: 包年/包月，可填写resource_id。 - on_demand: 按需计费，无需填写resource_id。  **默认取值**: on_demand 

        :param charging_mode: The charging_mode of this BatchStartWebTamperProtectionRequestInfo.
        :type charging_mode: str
        """
        self._charging_mode = charging_mode

    @property
    def resource_id(self):
        r"""Gets the resource_id of this BatchStartWebTamperProtectionRequestInfo.

        **参数解释**: 资源ID，即网页防篡改配额的配额ID，当charging_mode选择packet_cycle时可填写该字段，表示使用一个指定配额，也可不填写该字段，表示随机选择符合的配额。 **约束限制** : 不涉及 **取值范围**: 字符长度0-64位 **默认取值** : 不涉及 

        :return: The resource_id of this BatchStartWebTamperProtectionRequestInfo.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this BatchStartWebTamperProtectionRequestInfo.

        **参数解释**: 资源ID，即网页防篡改配额的配额ID，当charging_mode选择packet_cycle时可填写该字段，表示使用一个指定配额，也可不填写该字段，表示随机选择符合的配额。 **约束限制** : 不涉及 **取值范围**: 字符长度0-64位 **默认取值** : 不涉及 

        :param resource_id: The resource_id of this BatchStartWebTamperProtectionRequestInfo.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def tags(self):
        r"""Gets the tags of this BatchStartWebTamperProtectionRequestInfo.

        **参数解释**： 资源标签列表，仅计费模式选择按需计费时支持填写。 **约束限制**: 仅计费模式选择按需计费时支持填写。 **取值范围**: 最少0条，最多2097152条 **默认取值**: 不涉及

        :return: The tags of this BatchStartWebTamperProtectionRequestInfo.
        :rtype: list[:class:`huaweicloudsdkhss.v5.TagInfo`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this BatchStartWebTamperProtectionRequestInfo.

        **参数解释**： 资源标签列表，仅计费模式选择按需计费时支持填写。 **约束限制**: 仅计费模式选择按需计费时支持填写。 **取值范围**: 最少0条，最多2097152条 **默认取值**: 不涉及

        :param tags: The tags of this BatchStartWebTamperProtectionRequestInfo.
        :type tags: list[:class:`huaweicloudsdkhss.v5.TagInfo`]
        """
        self._tags = tags

    @property
    def protect_dir_info(self):
        r"""Gets the protect_dir_info of this BatchStartWebTamperProtectionRequestInfo.

        :return: The protect_dir_info of this BatchStartWebTamperProtectionRequestInfo.
        :rtype: :class:`huaweicloudsdkhss.v5.WebTamperProtectDirRequestInfo`
        """
        return self._protect_dir_info

    @protect_dir_info.setter
    def protect_dir_info(self, protect_dir_info):
        r"""Sets the protect_dir_info of this BatchStartWebTamperProtectionRequestInfo.

        :param protect_dir_info: The protect_dir_info of this BatchStartWebTamperProtectionRequestInfo.
        :type protect_dir_info: :class:`huaweicloudsdkhss.v5.WebTamperProtectDirRequestInfo`
        """
        self._protect_dir_info = protect_dir_info

    @property
    def enable_timing_off(self):
        r"""Gets the enable_timing_off of this BatchStartWebTamperProtectionRequestInfo.

        **参数解释**: 定时开关设置状态 **约束限制**: 不涉及 **取值范围**: - True ：开启定时关闭防护功能，必须填写timing_off_config_info。 - False ：关闭定时关闭防护功能，无需填写timing_off_config_info。  **默认取值**: False 

        :return: The enable_timing_off of this BatchStartWebTamperProtectionRequestInfo.
        :rtype: bool
        """
        return self._enable_timing_off

    @enable_timing_off.setter
    def enable_timing_off(self, enable_timing_off):
        r"""Sets the enable_timing_off of this BatchStartWebTamperProtectionRequestInfo.

        **参数解释**: 定时开关设置状态 **约束限制**: 不涉及 **取值范围**: - True ：开启定时关闭防护功能，必须填写timing_off_config_info。 - False ：关闭定时关闭防护功能，无需填写timing_off_config_info。  **默认取值**: False 

        :param enable_timing_off: The enable_timing_off of this BatchStartWebTamperProtectionRequestInfo.
        :type enable_timing_off: bool
        """
        self._enable_timing_off = enable_timing_off

    @property
    def timing_off_config_info(self):
        r"""Gets the timing_off_config_info of this BatchStartWebTamperProtectionRequestInfo.

        :return: The timing_off_config_info of this BatchStartWebTamperProtectionRequestInfo.
        :rtype: :class:`huaweicloudsdkhss.v5.WebTamperTimingOffConfigInfoRequestInfo`
        """
        return self._timing_off_config_info

    @timing_off_config_info.setter
    def timing_off_config_info(self, timing_off_config_info):
        r"""Sets the timing_off_config_info of this BatchStartWebTamperProtectionRequestInfo.

        :param timing_off_config_info: The timing_off_config_info of this BatchStartWebTamperProtectionRequestInfo.
        :type timing_off_config_info: :class:`huaweicloudsdkhss.v5.WebTamperTimingOffConfigInfoRequestInfo`
        """
        self._timing_off_config_info = timing_off_config_info

    @property
    def enable_rasp_protect(self):
        r"""Gets the enable_rasp_protect of this BatchStartWebTamperProtectionRequestInfo.

        **参数解释**: 动态网页防篡改开启状态，仅Linux服务器支持。 **约束限制**: 仅Linux服务器支持开启动态网页防篡改，Windows服务器不可填写该字段。 **取值范围**: - True ：开启动态网页防篡改，必须填写rasp_path。 - False ：关闭动态网页防篡改，无需填写rasp_path。  **默认取值**: False 

        :return: The enable_rasp_protect of this BatchStartWebTamperProtectionRequestInfo.
        :rtype: bool
        """
        return self._enable_rasp_protect

    @enable_rasp_protect.setter
    def enable_rasp_protect(self, enable_rasp_protect):
        r"""Sets the enable_rasp_protect of this BatchStartWebTamperProtectionRequestInfo.

        **参数解释**: 动态网页防篡改开启状态，仅Linux服务器支持。 **约束限制**: 仅Linux服务器支持开启动态网页防篡改，Windows服务器不可填写该字段。 **取值范围**: - True ：开启动态网页防篡改，必须填写rasp_path。 - False ：关闭动态网页防篡改，无需填写rasp_path。  **默认取值**: False 

        :param enable_rasp_protect: The enable_rasp_protect of this BatchStartWebTamperProtectionRequestInfo.
        :type enable_rasp_protect: bool
        """
        self._enable_rasp_protect = enable_rasp_protect

    @property
    def rasp_path(self):
        r"""Gets the rasp_path of this BatchStartWebTamperProtectionRequestInfo.

        **参数解释**: 动态网页防篡改的Tomcat bin目录，仅Linux服务器支持。 **约束限制**: 仅Linux服务器支持配置动态网页防篡改的Tomcat bin目录，Windows服务器不可填写该字段。 **取值范围**: 字符长度1-256位，必须以/开头，不能以/结尾，只能包含英文大小写字母，数字，下划线，中划线和点。 **默认取值**: 不涉及 

        :return: The rasp_path of this BatchStartWebTamperProtectionRequestInfo.
        :rtype: str
        """
        return self._rasp_path

    @rasp_path.setter
    def rasp_path(self, rasp_path):
        r"""Sets the rasp_path of this BatchStartWebTamperProtectionRequestInfo.

        **参数解释**: 动态网页防篡改的Tomcat bin目录，仅Linux服务器支持。 **约束限制**: 仅Linux服务器支持配置动态网页防篡改的Tomcat bin目录，Windows服务器不可填写该字段。 **取值范围**: 字符长度1-256位，必须以/开头，不能以/结尾，只能包含英文大小写字母，数字，下划线，中划线和点。 **默认取值**: 不涉及 

        :param rasp_path: The rasp_path of this BatchStartWebTamperProtectionRequestInfo.
        :type rasp_path: str
        """
        self._rasp_path = rasp_path

    @property
    def enable_privileged_process(self):
        r"""Gets the enable_privileged_process of this BatchStartWebTamperProtectionRequestInfo.

        **参数解释**: 特权进程开启状态 **约束限制**: 不涉及 **取值范围**: - True ：开启特权进程，必须填写privileged_process_info。 - False ：关闭特权进程，无需填写privileged_process_info。  **默认取值**: False 

        :return: The enable_privileged_process of this BatchStartWebTamperProtectionRequestInfo.
        :rtype: bool
        """
        return self._enable_privileged_process

    @enable_privileged_process.setter
    def enable_privileged_process(self, enable_privileged_process):
        r"""Sets the enable_privileged_process of this BatchStartWebTamperProtectionRequestInfo.

        **参数解释**: 特权进程开启状态 **约束限制**: 不涉及 **取值范围**: - True ：开启特权进程，必须填写privileged_process_info。 - False ：关闭特权进程，无需填写privileged_process_info。  **默认取值**: False 

        :param enable_privileged_process: The enable_privileged_process of this BatchStartWebTamperProtectionRequestInfo.
        :type enable_privileged_process: bool
        """
        self._enable_privileged_process = enable_privileged_process

    @property
    def privileged_process_info(self):
        r"""Gets the privileged_process_info of this BatchStartWebTamperProtectionRequestInfo.

        :return: The privileged_process_info of this BatchStartWebTamperProtectionRequestInfo.
        :rtype: :class:`huaweicloudsdkhss.v5.WebTamperPrivilegedProcessRequestInfo`
        """
        return self._privileged_process_info

    @privileged_process_info.setter
    def privileged_process_info(self, privileged_process_info):
        r"""Sets the privileged_process_info of this BatchStartWebTamperProtectionRequestInfo.

        :param privileged_process_info: The privileged_process_info of this BatchStartWebTamperProtectionRequestInfo.
        :type privileged_process_info: :class:`huaweicloudsdkhss.v5.WebTamperPrivilegedProcessRequestInfo`
        """
        self._privileged_process_info = privileged_process_info

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
        if not isinstance(other, BatchStartWebTamperProtectionRequestInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
