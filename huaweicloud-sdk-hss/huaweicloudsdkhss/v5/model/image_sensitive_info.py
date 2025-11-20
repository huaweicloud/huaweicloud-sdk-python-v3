# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImageSensitiveInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sensitive_info_id': 'str',
        'severity': 'str',
        'name': 'str',
        'description': 'str',
        'position': 'str',
        'file_path': 'str',
        'content': 'str',
        'latest_scan_time': 'int',
        'handle_status': 'str',
        'operate_accept': 'str'
    }

    attribute_map = {
        'sensitive_info_id': 'sensitive_info_id',
        'severity': 'severity',
        'name': 'name',
        'description': 'description',
        'position': 'position',
        'file_path': 'file_path',
        'content': 'content',
        'latest_scan_time': 'latest_scan_time',
        'handle_status': 'handle_status',
        'operate_accept': 'operate_accept'
    }

    def __init__(self, sensitive_info_id=None, severity=None, name=None, description=None, position=None, file_path=None, content=None, latest_scan_time=None, handle_status=None, operate_accept=None):
        r"""ImageSensitiveInfo

        The model defined in huaweicloud sdk

        :param sensitive_info_id: **参数解释**: 敏感事件编号 **取值范围**: 字符长度0-128位 
        :type sensitive_info_id: str
        :param severity: **参数解释**: 威胁等级 **取值范围**: - critical：致命。 - high：高危。 - medium：中危。 - low : 低危。 
        :type severity: str
        :param name: **参数解释**: 规则名称 **取值范围**: 字符长度0-128位 
        :type name: str
        :param description: **参数解释**: 规则描述 **取值范围**: 字符长度0-128位 
        :type description: str
        :param position: **参数解释**: 漏洞所在镜像层 **取值范围**: 字符长度0-128位 
        :type position: str
        :param file_path: **参数解释**: 文件路径 **取值范围**: 字符长度0-128位 
        :type file_path: str
        :param content: **参数解释**: 敏感信息内容 **取值范围**: 字符长度0-128位 
        :type content: str
        :param latest_scan_time: **参数解释**: 最后一次检测时间，时间单位 毫秒（ms） **取值范围**: 最小值0，最大值2147483647 
        :type latest_scan_time: int
        :param handle_status: **参数解释**: 是否已处理 **取值范围**: - unhandled：未处理。 - handled：已处理。 
        :type handle_status: str
        :param operate_accept: **参数解释**: 操作类型 **取值范围**: - ignore ：忽略。 - do_not_ignore ：取消忽略。 
        :type operate_accept: str
        """
        
        

        self._sensitive_info_id = None
        self._severity = None
        self._name = None
        self._description = None
        self._position = None
        self._file_path = None
        self._content = None
        self._latest_scan_time = None
        self._handle_status = None
        self._operate_accept = None
        self.discriminator = None

        if sensitive_info_id is not None:
            self.sensitive_info_id = sensitive_info_id
        if severity is not None:
            self.severity = severity
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if position is not None:
            self.position = position
        if file_path is not None:
            self.file_path = file_path
        if content is not None:
            self.content = content
        if latest_scan_time is not None:
            self.latest_scan_time = latest_scan_time
        if handle_status is not None:
            self.handle_status = handle_status
        if operate_accept is not None:
            self.operate_accept = operate_accept

    @property
    def sensitive_info_id(self):
        r"""Gets the sensitive_info_id of this ImageSensitiveInfo.

        **参数解释**: 敏感事件编号 **取值范围**: 字符长度0-128位 

        :return: The sensitive_info_id of this ImageSensitiveInfo.
        :rtype: str
        """
        return self._sensitive_info_id

    @sensitive_info_id.setter
    def sensitive_info_id(self, sensitive_info_id):
        r"""Sets the sensitive_info_id of this ImageSensitiveInfo.

        **参数解释**: 敏感事件编号 **取值范围**: 字符长度0-128位 

        :param sensitive_info_id: The sensitive_info_id of this ImageSensitiveInfo.
        :type sensitive_info_id: str
        """
        self._sensitive_info_id = sensitive_info_id

    @property
    def severity(self):
        r"""Gets the severity of this ImageSensitiveInfo.

        **参数解释**: 威胁等级 **取值范围**: - critical：致命。 - high：高危。 - medium：中危。 - low : 低危。 

        :return: The severity of this ImageSensitiveInfo.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        r"""Sets the severity of this ImageSensitiveInfo.

        **参数解释**: 威胁等级 **取值范围**: - critical：致命。 - high：高危。 - medium：中危。 - low : 低危。 

        :param severity: The severity of this ImageSensitiveInfo.
        :type severity: str
        """
        self._severity = severity

    @property
    def name(self):
        r"""Gets the name of this ImageSensitiveInfo.

        **参数解释**: 规则名称 **取值范围**: 字符长度0-128位 

        :return: The name of this ImageSensitiveInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ImageSensitiveInfo.

        **参数解释**: 规则名称 **取值范围**: 字符长度0-128位 

        :param name: The name of this ImageSensitiveInfo.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this ImageSensitiveInfo.

        **参数解释**: 规则描述 **取值范围**: 字符长度0-128位 

        :return: The description of this ImageSensitiveInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ImageSensitiveInfo.

        **参数解释**: 规则描述 **取值范围**: 字符长度0-128位 

        :param description: The description of this ImageSensitiveInfo.
        :type description: str
        """
        self._description = description

    @property
    def position(self):
        r"""Gets the position of this ImageSensitiveInfo.

        **参数解释**: 漏洞所在镜像层 **取值范围**: 字符长度0-128位 

        :return: The position of this ImageSensitiveInfo.
        :rtype: str
        """
        return self._position

    @position.setter
    def position(self, position):
        r"""Sets the position of this ImageSensitiveInfo.

        **参数解释**: 漏洞所在镜像层 **取值范围**: 字符长度0-128位 

        :param position: The position of this ImageSensitiveInfo.
        :type position: str
        """
        self._position = position

    @property
    def file_path(self):
        r"""Gets the file_path of this ImageSensitiveInfo.

        **参数解释**: 文件路径 **取值范围**: 字符长度0-128位 

        :return: The file_path of this ImageSensitiveInfo.
        :rtype: str
        """
        return self._file_path

    @file_path.setter
    def file_path(self, file_path):
        r"""Sets the file_path of this ImageSensitiveInfo.

        **参数解释**: 文件路径 **取值范围**: 字符长度0-128位 

        :param file_path: The file_path of this ImageSensitiveInfo.
        :type file_path: str
        """
        self._file_path = file_path

    @property
    def content(self):
        r"""Gets the content of this ImageSensitiveInfo.

        **参数解释**: 敏感信息内容 **取值范围**: 字符长度0-128位 

        :return: The content of this ImageSensitiveInfo.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        r"""Sets the content of this ImageSensitiveInfo.

        **参数解释**: 敏感信息内容 **取值范围**: 字符长度0-128位 

        :param content: The content of this ImageSensitiveInfo.
        :type content: str
        """
        self._content = content

    @property
    def latest_scan_time(self):
        r"""Gets the latest_scan_time of this ImageSensitiveInfo.

        **参数解释**: 最后一次检测时间，时间单位 毫秒（ms） **取值范围**: 最小值0，最大值2147483647 

        :return: The latest_scan_time of this ImageSensitiveInfo.
        :rtype: int
        """
        return self._latest_scan_time

    @latest_scan_time.setter
    def latest_scan_time(self, latest_scan_time):
        r"""Sets the latest_scan_time of this ImageSensitiveInfo.

        **参数解释**: 最后一次检测时间，时间单位 毫秒（ms） **取值范围**: 最小值0，最大值2147483647 

        :param latest_scan_time: The latest_scan_time of this ImageSensitiveInfo.
        :type latest_scan_time: int
        """
        self._latest_scan_time = latest_scan_time

    @property
    def handle_status(self):
        r"""Gets the handle_status of this ImageSensitiveInfo.

        **参数解释**: 是否已处理 **取值范围**: - unhandled：未处理。 - handled：已处理。 

        :return: The handle_status of this ImageSensitiveInfo.
        :rtype: str
        """
        return self._handle_status

    @handle_status.setter
    def handle_status(self, handle_status):
        r"""Sets the handle_status of this ImageSensitiveInfo.

        **参数解释**: 是否已处理 **取值范围**: - unhandled：未处理。 - handled：已处理。 

        :param handle_status: The handle_status of this ImageSensitiveInfo.
        :type handle_status: str
        """
        self._handle_status = handle_status

    @property
    def operate_accept(self):
        r"""Gets the operate_accept of this ImageSensitiveInfo.

        **参数解释**: 操作类型 **取值范围**: - ignore ：忽略。 - do_not_ignore ：取消忽略。 

        :return: The operate_accept of this ImageSensitiveInfo.
        :rtype: str
        """
        return self._operate_accept

    @operate_accept.setter
    def operate_accept(self, operate_accept):
        r"""Sets the operate_accept of this ImageSensitiveInfo.

        **参数解释**: 操作类型 **取值范围**: - ignore ：忽略。 - do_not_ignore ：取消忽略。 

        :param operate_accept: The operate_accept of this ImageSensitiveInfo.
        :type operate_accept: str
        """
        self._operate_accept = operate_accept

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
        if not isinstance(other, ImageSensitiveInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
