# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAntivirusHandleHistoryRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'region': 'str',
        'enterprise_project_id': 'str',
        'offset': 'int',
        'limit': 'int',
        'malware_name': 'str',
        'file_path': 'str',
        'severity_list': 'list[str]',
        'host_name': 'str',
        'private_ip': 'str',
        'public_ip': 'str',
        'asset_value': 'str',
        'handle_method': 'str',
        'user_name': 'str',
        'event_type': 'int',
        'sort_dir': 'str',
        'sort_key': 'str'
    }

    attribute_map = {
        'region': 'region',
        'enterprise_project_id': 'enterprise_project_id',
        'offset': 'offset',
        'limit': 'limit',
        'malware_name': 'malware_name',
        'file_path': 'file_path',
        'severity_list': 'severity_list',
        'host_name': 'host_name',
        'private_ip': 'private_ip',
        'public_ip': 'public_ip',
        'asset_value': 'asset_value',
        'handle_method': 'handle_method',
        'user_name': 'user_name',
        'event_type': 'event_type',
        'sort_dir': 'sort_dir',
        'sort_key': 'sort_key'
    }

    def __init__(self, region=None, enterprise_project_id=None, offset=None, limit=None, malware_name=None, file_path=None, severity_list=None, host_name=None, private_ip=None, public_ip=None, asset_value=None, handle_method=None, user_name=None, event_type=None, sort_dir=None, sort_key=None):
        r"""ListAntivirusHandleHistoryRequest

        The model defined in huaweicloud sdk

        :param region: **参数解释**: 区域ID，用于查询目的区域内的资产。获取方式请参见[获取区域ID](hss_02_0026.xml)。 **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 
        :type region: str
        :param enterprise_project_id: **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 
        :type enterprise_project_id: str
        :param offset: **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 不涉及 
        :type offset: int
        :param limit: **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 
        :type limit: int
        :param malware_name: 病毒名称
        :type malware_name: str
        :param file_path: 文件路径
        :type file_path: str
        :param severity_list: 威胁等级，包含如下:   - Low：低危   - Medium：中危   - High：高危   - Critical：致命
        :type severity_list: list[str]
        :param host_name: **参数解释**: 服务器名称 **约束限制**: 不涉及 **取值范围**: 字符长度1-256位 **默认取值**: 不涉及 
        :type host_name: str
        :param private_ip: **参数解释**: 服务器私有IP **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 
        :type private_ip: str
        :param public_ip: 服务器公网IP
        :type public_ip: str
        :param asset_value: 资产重要性，包含如下3种   - important ：重要资产   - common ：一般资产   - test ：测试资产
        :type asset_value: str
        :param handle_method: 处理方式，包含如下:   - mark_as_handled：手动处理   - ignore：忽略   - add_to_alarm_whitelist：加入告警白名单   - isolate_and_kill：隔离文件   - unhandle：取消手动处理   - do_not_ignore：取消忽略   - remove_from_alarm_whitelist：删除告警白名单   - do_not_isolate_or_kill：取消隔离文件
        :type handle_method: str
        :param user_name: 用户名
        :type user_name: str
        :param event_type: 事件类型
        :type event_type: int
        :param sort_dir: 排序顺序，若sort_key不为空,设置返回结果按照sort_key升序或降序排序,默认降序排序，包含如下:   - asc : 升序   - desc : 降序
        :type sort_dir: str
        :param sort_key: 排序字段，包含如下:   - handle_time : 处置时间
        :type sort_key: str
        """
        
        

        self._region = None
        self._enterprise_project_id = None
        self._offset = None
        self._limit = None
        self._malware_name = None
        self._file_path = None
        self._severity_list = None
        self._host_name = None
        self._private_ip = None
        self._public_ip = None
        self._asset_value = None
        self._handle_method = None
        self._user_name = None
        self._event_type = None
        self._sort_dir = None
        self._sort_key = None
        self.discriminator = None

        if region is not None:
            self.region = region
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        self.offset = offset
        self.limit = limit
        if malware_name is not None:
            self.malware_name = malware_name
        if file_path is not None:
            self.file_path = file_path
        if severity_list is not None:
            self.severity_list = severity_list
        if host_name is not None:
            self.host_name = host_name
        if private_ip is not None:
            self.private_ip = private_ip
        if public_ip is not None:
            self.public_ip = public_ip
        if asset_value is not None:
            self.asset_value = asset_value
        if handle_method is not None:
            self.handle_method = handle_method
        if user_name is not None:
            self.user_name = user_name
        if event_type is not None:
            self.event_type = event_type
        if sort_dir is not None:
            self.sort_dir = sort_dir
        if sort_key is not None:
            self.sort_key = sort_key

    @property
    def region(self):
        r"""Gets the region of this ListAntivirusHandleHistoryRequest.

        **参数解释**: 区域ID，用于查询目的区域内的资产。获取方式请参见[获取区域ID](hss_02_0026.xml)。 **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 

        :return: The region of this ListAntivirusHandleHistoryRequest.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this ListAntivirusHandleHistoryRequest.

        **参数解释**: 区域ID，用于查询目的区域内的资产。获取方式请参见[获取区域ID](hss_02_0026.xml)。 **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 

        :param region: The region of this ListAntivirusHandleHistoryRequest.
        :type region: str
        """
        self._region = region

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListAntivirusHandleHistoryRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :return: The enterprise_project_id of this ListAntivirusHandleHistoryRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListAntivirusHandleHistoryRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :param enterprise_project_id: The enterprise_project_id of this ListAntivirusHandleHistoryRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def offset(self):
        r"""Gets the offset of this ListAntivirusHandleHistoryRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 不涉及 

        :return: The offset of this ListAntivirusHandleHistoryRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListAntivirusHandleHistoryRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 不涉及 

        :param offset: The offset of this ListAntivirusHandleHistoryRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListAntivirusHandleHistoryRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :return: The limit of this ListAntivirusHandleHistoryRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListAntivirusHandleHistoryRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :param limit: The limit of this ListAntivirusHandleHistoryRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def malware_name(self):
        r"""Gets the malware_name of this ListAntivirusHandleHistoryRequest.

        病毒名称

        :return: The malware_name of this ListAntivirusHandleHistoryRequest.
        :rtype: str
        """
        return self._malware_name

    @malware_name.setter
    def malware_name(self, malware_name):
        r"""Sets the malware_name of this ListAntivirusHandleHistoryRequest.

        病毒名称

        :param malware_name: The malware_name of this ListAntivirusHandleHistoryRequest.
        :type malware_name: str
        """
        self._malware_name = malware_name

    @property
    def file_path(self):
        r"""Gets the file_path of this ListAntivirusHandleHistoryRequest.

        文件路径

        :return: The file_path of this ListAntivirusHandleHistoryRequest.
        :rtype: str
        """
        return self._file_path

    @file_path.setter
    def file_path(self, file_path):
        r"""Sets the file_path of this ListAntivirusHandleHistoryRequest.

        文件路径

        :param file_path: The file_path of this ListAntivirusHandleHistoryRequest.
        :type file_path: str
        """
        self._file_path = file_path

    @property
    def severity_list(self):
        r"""Gets the severity_list of this ListAntivirusHandleHistoryRequest.

        威胁等级，包含如下:   - Low：低危   - Medium：中危   - High：高危   - Critical：致命

        :return: The severity_list of this ListAntivirusHandleHistoryRequest.
        :rtype: list[str]
        """
        return self._severity_list

    @severity_list.setter
    def severity_list(self, severity_list):
        r"""Sets the severity_list of this ListAntivirusHandleHistoryRequest.

        威胁等级，包含如下:   - Low：低危   - Medium：中危   - High：高危   - Critical：致命

        :param severity_list: The severity_list of this ListAntivirusHandleHistoryRequest.
        :type severity_list: list[str]
        """
        self._severity_list = severity_list

    @property
    def host_name(self):
        r"""Gets the host_name of this ListAntivirusHandleHistoryRequest.

        **参数解释**: 服务器名称 **约束限制**: 不涉及 **取值范围**: 字符长度1-256位 **默认取值**: 不涉及 

        :return: The host_name of this ListAntivirusHandleHistoryRequest.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this ListAntivirusHandleHistoryRequest.

        **参数解释**: 服务器名称 **约束限制**: 不涉及 **取值范围**: 字符长度1-256位 **默认取值**: 不涉及 

        :param host_name: The host_name of this ListAntivirusHandleHistoryRequest.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def private_ip(self):
        r"""Gets the private_ip of this ListAntivirusHandleHistoryRequest.

        **参数解释**: 服务器私有IP **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 

        :return: The private_ip of this ListAntivirusHandleHistoryRequest.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        r"""Sets the private_ip of this ListAntivirusHandleHistoryRequest.

        **参数解释**: 服务器私有IP **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 

        :param private_ip: The private_ip of this ListAntivirusHandleHistoryRequest.
        :type private_ip: str
        """
        self._private_ip = private_ip

    @property
    def public_ip(self):
        r"""Gets the public_ip of this ListAntivirusHandleHistoryRequest.

        服务器公网IP

        :return: The public_ip of this ListAntivirusHandleHistoryRequest.
        :rtype: str
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        r"""Sets the public_ip of this ListAntivirusHandleHistoryRequest.

        服务器公网IP

        :param public_ip: The public_ip of this ListAntivirusHandleHistoryRequest.
        :type public_ip: str
        """
        self._public_ip = public_ip

    @property
    def asset_value(self):
        r"""Gets the asset_value of this ListAntivirusHandleHistoryRequest.

        资产重要性，包含如下3种   - important ：重要资产   - common ：一般资产   - test ：测试资产

        :return: The asset_value of this ListAntivirusHandleHistoryRequest.
        :rtype: str
        """
        return self._asset_value

    @asset_value.setter
    def asset_value(self, asset_value):
        r"""Sets the asset_value of this ListAntivirusHandleHistoryRequest.

        资产重要性，包含如下3种   - important ：重要资产   - common ：一般资产   - test ：测试资产

        :param asset_value: The asset_value of this ListAntivirusHandleHistoryRequest.
        :type asset_value: str
        """
        self._asset_value = asset_value

    @property
    def handle_method(self):
        r"""Gets the handle_method of this ListAntivirusHandleHistoryRequest.

        处理方式，包含如下:   - mark_as_handled：手动处理   - ignore：忽略   - add_to_alarm_whitelist：加入告警白名单   - isolate_and_kill：隔离文件   - unhandle：取消手动处理   - do_not_ignore：取消忽略   - remove_from_alarm_whitelist：删除告警白名单   - do_not_isolate_or_kill：取消隔离文件

        :return: The handle_method of this ListAntivirusHandleHistoryRequest.
        :rtype: str
        """
        return self._handle_method

    @handle_method.setter
    def handle_method(self, handle_method):
        r"""Sets the handle_method of this ListAntivirusHandleHistoryRequest.

        处理方式，包含如下:   - mark_as_handled：手动处理   - ignore：忽略   - add_to_alarm_whitelist：加入告警白名单   - isolate_and_kill：隔离文件   - unhandle：取消手动处理   - do_not_ignore：取消忽略   - remove_from_alarm_whitelist：删除告警白名单   - do_not_isolate_or_kill：取消隔离文件

        :param handle_method: The handle_method of this ListAntivirusHandleHistoryRequest.
        :type handle_method: str
        """
        self._handle_method = handle_method

    @property
    def user_name(self):
        r"""Gets the user_name of this ListAntivirusHandleHistoryRequest.

        用户名

        :return: The user_name of this ListAntivirusHandleHistoryRequest.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this ListAntivirusHandleHistoryRequest.

        用户名

        :param user_name: The user_name of this ListAntivirusHandleHistoryRequest.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def event_type(self):
        r"""Gets the event_type of this ListAntivirusHandleHistoryRequest.

        事件类型

        :return: The event_type of this ListAntivirusHandleHistoryRequest.
        :rtype: int
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        r"""Sets the event_type of this ListAntivirusHandleHistoryRequest.

        事件类型

        :param event_type: The event_type of this ListAntivirusHandleHistoryRequest.
        :type event_type: int
        """
        self._event_type = event_type

    @property
    def sort_dir(self):
        r"""Gets the sort_dir of this ListAntivirusHandleHistoryRequest.

        排序顺序，若sort_key不为空,设置返回结果按照sort_key升序或降序排序,默认降序排序，包含如下:   - asc : 升序   - desc : 降序

        :return: The sort_dir of this ListAntivirusHandleHistoryRequest.
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        r"""Sets the sort_dir of this ListAntivirusHandleHistoryRequest.

        排序顺序，若sort_key不为空,设置返回结果按照sort_key升序或降序排序,默认降序排序，包含如下:   - asc : 升序   - desc : 降序

        :param sort_dir: The sort_dir of this ListAntivirusHandleHistoryRequest.
        :type sort_dir: str
        """
        self._sort_dir = sort_dir

    @property
    def sort_key(self):
        r"""Gets the sort_key of this ListAntivirusHandleHistoryRequest.

        排序字段，包含如下:   - handle_time : 处置时间

        :return: The sort_key of this ListAntivirusHandleHistoryRequest.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        r"""Sets the sort_key of this ListAntivirusHandleHistoryRequest.

        排序字段，包含如下:   - handle_time : 处置时间

        :param sort_key: The sort_key of this ListAntivirusHandleHistoryRequest.
        :type sort_key: str
        """
        self._sort_key = sort_key

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
        if not isinstance(other, ListAntivirusHandleHistoryRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
