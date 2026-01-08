# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExportUserConnectionNewRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'start_time': 'str',
        'end_time': 'str',
        'user_name': 'str',
        'computer_name': 'str',
        'terminal_type': 'str',
        'language': 'str',
        'min_e2e_rtt': 'int',
        'max_e2e_rtt': 'int',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'start_time': 'start_time',
        'end_time': 'end_time',
        'user_name': 'user_name',
        'computer_name': 'computer_name',
        'terminal_type': 'terminal_type',
        'language': 'language',
        'min_e2e_rtt': 'min_e2e_rtt',
        'max_e2e_rtt': 'max_e2e_rtt',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, start_time=None, end_time=None, user_name=None, computer_name=None, terminal_type=None, language=None, min_e2e_rtt=None, max_e2e_rtt=None, enterprise_project_id=None):
        r"""ExportUserConnectionNewRequest

        The model defined in huaweicloud sdk

        :param start_time: 查询的起始时间。指定该参数后，返回的结果为此时间之后的所有登录记录。时间格式如：“2016-08-20T21:11:11Z”。终止时间不为空时，起始时间为非必填项。开始时间要在最近30天内。
        :type start_time: str
        :param end_time: 查询的终止时间。指定该参数后，返回的结果为此时间之前的所有登录记录。时间格式如：“2016-08-20T21:11:11Z”。起始时间不为空时，起始时间为非必填项。结束时间要在最近30天内。
        :type end_time: str
        :param user_name: 登录桌面的用户名。
        :type user_name: str
        :param computer_name: 计算机名（操作系统信息中可见）。
        :type computer_name: str
        :param terminal_type: 登录桌面的终端系统类型，该字段支持模糊查询，例如：Windows 10。
        :type terminal_type: str
        :param language: 导出语言，默认英文。 - zh_CN：中文 - en_US：英文
        :type language: str
        :param min_e2e_rtt: 查询端到端时延的最小值。
        :type min_e2e_rtt: int
        :param max_e2e_rtt: 查询端到端时延的最大值。
        :type max_e2e_rtt: int
        :param enterprise_project_id: 企业项目ID。
        :type enterprise_project_id: str
        """
        
        

        self._start_time = None
        self._end_time = None
        self._user_name = None
        self._computer_name = None
        self._terminal_type = None
        self._language = None
        self._min_e2e_rtt = None
        self._max_e2e_rtt = None
        self._enterprise_project_id = None
        self.discriminator = None

        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if user_name is not None:
            self.user_name = user_name
        if computer_name is not None:
            self.computer_name = computer_name
        if terminal_type is not None:
            self.terminal_type = terminal_type
        if language is not None:
            self.language = language
        if min_e2e_rtt is not None:
            self.min_e2e_rtt = min_e2e_rtt
        if max_e2e_rtt is not None:
            self.max_e2e_rtt = max_e2e_rtt
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def start_time(self):
        r"""Gets the start_time of this ExportUserConnectionNewRequest.

        查询的起始时间。指定该参数后，返回的结果为此时间之后的所有登录记录。时间格式如：“2016-08-20T21:11:11Z”。终止时间不为空时，起始时间为非必填项。开始时间要在最近30天内。

        :return: The start_time of this ExportUserConnectionNewRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ExportUserConnectionNewRequest.

        查询的起始时间。指定该参数后，返回的结果为此时间之后的所有登录记录。时间格式如：“2016-08-20T21:11:11Z”。终止时间不为空时，起始时间为非必填项。开始时间要在最近30天内。

        :param start_time: The start_time of this ExportUserConnectionNewRequest.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ExportUserConnectionNewRequest.

        查询的终止时间。指定该参数后，返回的结果为此时间之前的所有登录记录。时间格式如：“2016-08-20T21:11:11Z”。起始时间不为空时，起始时间为非必填项。结束时间要在最近30天内。

        :return: The end_time of this ExportUserConnectionNewRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ExportUserConnectionNewRequest.

        查询的终止时间。指定该参数后，返回的结果为此时间之前的所有登录记录。时间格式如：“2016-08-20T21:11:11Z”。起始时间不为空时，起始时间为非必填项。结束时间要在最近30天内。

        :param end_time: The end_time of this ExportUserConnectionNewRequest.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def user_name(self):
        r"""Gets the user_name of this ExportUserConnectionNewRequest.

        登录桌面的用户名。

        :return: The user_name of this ExportUserConnectionNewRequest.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this ExportUserConnectionNewRequest.

        登录桌面的用户名。

        :param user_name: The user_name of this ExportUserConnectionNewRequest.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def computer_name(self):
        r"""Gets the computer_name of this ExportUserConnectionNewRequest.

        计算机名（操作系统信息中可见）。

        :return: The computer_name of this ExportUserConnectionNewRequest.
        :rtype: str
        """
        return self._computer_name

    @computer_name.setter
    def computer_name(self, computer_name):
        r"""Sets the computer_name of this ExportUserConnectionNewRequest.

        计算机名（操作系统信息中可见）。

        :param computer_name: The computer_name of this ExportUserConnectionNewRequest.
        :type computer_name: str
        """
        self._computer_name = computer_name

    @property
    def terminal_type(self):
        r"""Gets the terminal_type of this ExportUserConnectionNewRequest.

        登录桌面的终端系统类型，该字段支持模糊查询，例如：Windows 10。

        :return: The terminal_type of this ExportUserConnectionNewRequest.
        :rtype: str
        """
        return self._terminal_type

    @terminal_type.setter
    def terminal_type(self, terminal_type):
        r"""Sets the terminal_type of this ExportUserConnectionNewRequest.

        登录桌面的终端系统类型，该字段支持模糊查询，例如：Windows 10。

        :param terminal_type: The terminal_type of this ExportUserConnectionNewRequest.
        :type terminal_type: str
        """
        self._terminal_type = terminal_type

    @property
    def language(self):
        r"""Gets the language of this ExportUserConnectionNewRequest.

        导出语言，默认英文。 - zh_CN：中文 - en_US：英文

        :return: The language of this ExportUserConnectionNewRequest.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        r"""Sets the language of this ExportUserConnectionNewRequest.

        导出语言，默认英文。 - zh_CN：中文 - en_US：英文

        :param language: The language of this ExportUserConnectionNewRequest.
        :type language: str
        """
        self._language = language

    @property
    def min_e2e_rtt(self):
        r"""Gets the min_e2e_rtt of this ExportUserConnectionNewRequest.

        查询端到端时延的最小值。

        :return: The min_e2e_rtt of this ExportUserConnectionNewRequest.
        :rtype: int
        """
        return self._min_e2e_rtt

    @min_e2e_rtt.setter
    def min_e2e_rtt(self, min_e2e_rtt):
        r"""Sets the min_e2e_rtt of this ExportUserConnectionNewRequest.

        查询端到端时延的最小值。

        :param min_e2e_rtt: The min_e2e_rtt of this ExportUserConnectionNewRequest.
        :type min_e2e_rtt: int
        """
        self._min_e2e_rtt = min_e2e_rtt

    @property
    def max_e2e_rtt(self):
        r"""Gets the max_e2e_rtt of this ExportUserConnectionNewRequest.

        查询端到端时延的最大值。

        :return: The max_e2e_rtt of this ExportUserConnectionNewRequest.
        :rtype: int
        """
        return self._max_e2e_rtt

    @max_e2e_rtt.setter
    def max_e2e_rtt(self, max_e2e_rtt):
        r"""Sets the max_e2e_rtt of this ExportUserConnectionNewRequest.

        查询端到端时延的最大值。

        :param max_e2e_rtt: The max_e2e_rtt of this ExportUserConnectionNewRequest.
        :type max_e2e_rtt: int
        """
        self._max_e2e_rtt = max_e2e_rtt

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ExportUserConnectionNewRequest.

        企业项目ID。

        :return: The enterprise_project_id of this ExportUserConnectionNewRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ExportUserConnectionNewRequest.

        企业项目ID。

        :param enterprise_project_id: The enterprise_project_id of this ExportUserConnectionNewRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

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
        if not isinstance(other, ExportUserConnectionNewRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
