# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AccessAreaFilter:

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
        'content_type': 'str',
        'content_value': 'str',
        'area': 'str',
        'exception_ip': 'str'
    }

    attribute_map = {
        'type': 'type',
        'content_type': 'content_type',
        'content_value': 'content_value',
        'area': 'area',
        'exception_ip': 'exception_ip'
    }

    def __init__(self, type=None, content_type=None, content_value=None, area=None, exception_ip=None):
        r"""AccessAreaFilter

        The model defined in huaweicloud sdk

        :param type: 规则类型，黑、白名单二选一。   - black: 黑名单，如果匹配到黑名单规则，则黑名单所选区域内的用户将无法访问当前资源，返回403状态码。   - white: 白名单，白名单所选区域以外的用户均无法访问当前资源，返回403状态码。
        :type type: str
        :param content_type: 生效类型。   - all: 所有文件，所有文件均遵循配置的规则。   - file_directory: 目录路径，指定目录路径的资源遵循配置的规则。   - file_path: 全路径，指定路径的资源遵循配置的规则。
        :type content_type: str
        :param content_value: 生效规则。当content_type为all时，为空或不传。 当content_type为file_directory时，输入要求以“/”作为首字符，多个目录以“,”进行分隔，如/test/folder01,/test/folder02，并且输入的目录路径总数不超过100个。 当content_type为file_path时，输入要求以“/”或“\\*”作为首字符，支持配置通配符“\\*”，通配符不能连续出现且不能超过两个。多个路径以“,”进行分割，如/test/a.txt,/test/b.txt，并且输出的总数不能超过100个。   &gt; - 不允许配置两条完全一样的白名单或黑名单规则。   &gt; - 仅允许配置一条生效类型为“所有文件”的规则。
        :type content_value: str
        :param area: 配置规则适用的区域，多个区域以“,”进行分隔，支持的区域如：CN_IN：中国大陆，AF：阿富汗，IE：爱尔兰，EG：埃及，AU：澳大利亚等。具体的位置编码参见《附录-地理位置编码》查询。
        :type area: str
        :param exception_ip: 例外IP，配置指定IP不执行当前规则。
        :type exception_ip: str
        """
        
        

        self._type = None
        self._content_type = None
        self._content_value = None
        self._area = None
        self._exception_ip = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if content_type is not None:
            self.content_type = content_type
        if content_value is not None:
            self.content_value = content_value
        if area is not None:
            self.area = area
        if exception_ip is not None:
            self.exception_ip = exception_ip

    @property
    def type(self):
        r"""Gets the type of this AccessAreaFilter.

        规则类型，黑、白名单二选一。   - black: 黑名单，如果匹配到黑名单规则，则黑名单所选区域内的用户将无法访问当前资源，返回403状态码。   - white: 白名单，白名单所选区域以外的用户均无法访问当前资源，返回403状态码。

        :return: The type of this AccessAreaFilter.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this AccessAreaFilter.

        规则类型，黑、白名单二选一。   - black: 黑名单，如果匹配到黑名单规则，则黑名单所选区域内的用户将无法访问当前资源，返回403状态码。   - white: 白名单，白名单所选区域以外的用户均无法访问当前资源，返回403状态码。

        :param type: The type of this AccessAreaFilter.
        :type type: str
        """
        self._type = type

    @property
    def content_type(self):
        r"""Gets the content_type of this AccessAreaFilter.

        生效类型。   - all: 所有文件，所有文件均遵循配置的规则。   - file_directory: 目录路径，指定目录路径的资源遵循配置的规则。   - file_path: 全路径，指定路径的资源遵循配置的规则。

        :return: The content_type of this AccessAreaFilter.
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        r"""Sets the content_type of this AccessAreaFilter.

        生效类型。   - all: 所有文件，所有文件均遵循配置的规则。   - file_directory: 目录路径，指定目录路径的资源遵循配置的规则。   - file_path: 全路径，指定路径的资源遵循配置的规则。

        :param content_type: The content_type of this AccessAreaFilter.
        :type content_type: str
        """
        self._content_type = content_type

    @property
    def content_value(self):
        r"""Gets the content_value of this AccessAreaFilter.

        生效规则。当content_type为all时，为空或不传。 当content_type为file_directory时，输入要求以“/”作为首字符，多个目录以“,”进行分隔，如/test/folder01,/test/folder02，并且输入的目录路径总数不超过100个。 当content_type为file_path时，输入要求以“/”或“\\*”作为首字符，支持配置通配符“\\*”，通配符不能连续出现且不能超过两个。多个路径以“,”进行分割，如/test/a.txt,/test/b.txt，并且输出的总数不能超过100个。   > - 不允许配置两条完全一样的白名单或黑名单规则。   > - 仅允许配置一条生效类型为“所有文件”的规则。

        :return: The content_value of this AccessAreaFilter.
        :rtype: str
        """
        return self._content_value

    @content_value.setter
    def content_value(self, content_value):
        r"""Sets the content_value of this AccessAreaFilter.

        生效规则。当content_type为all时，为空或不传。 当content_type为file_directory时，输入要求以“/”作为首字符，多个目录以“,”进行分隔，如/test/folder01,/test/folder02，并且输入的目录路径总数不超过100个。 当content_type为file_path时，输入要求以“/”或“\\*”作为首字符，支持配置通配符“\\*”，通配符不能连续出现且不能超过两个。多个路径以“,”进行分割，如/test/a.txt,/test/b.txt，并且输出的总数不能超过100个。   > - 不允许配置两条完全一样的白名单或黑名单规则。   > - 仅允许配置一条生效类型为“所有文件”的规则。

        :param content_value: The content_value of this AccessAreaFilter.
        :type content_value: str
        """
        self._content_value = content_value

    @property
    def area(self):
        r"""Gets the area of this AccessAreaFilter.

        配置规则适用的区域，多个区域以“,”进行分隔，支持的区域如：CN_IN：中国大陆，AF：阿富汗，IE：爱尔兰，EG：埃及，AU：澳大利亚等。具体的位置编码参见《附录-地理位置编码》查询。

        :return: The area of this AccessAreaFilter.
        :rtype: str
        """
        return self._area

    @area.setter
    def area(self, area):
        r"""Sets the area of this AccessAreaFilter.

        配置规则适用的区域，多个区域以“,”进行分隔，支持的区域如：CN_IN：中国大陆，AF：阿富汗，IE：爱尔兰，EG：埃及，AU：澳大利亚等。具体的位置编码参见《附录-地理位置编码》查询。

        :param area: The area of this AccessAreaFilter.
        :type area: str
        """
        self._area = area

    @property
    def exception_ip(self):
        r"""Gets the exception_ip of this AccessAreaFilter.

        例外IP，配置指定IP不执行当前规则。

        :return: The exception_ip of this AccessAreaFilter.
        :rtype: str
        """
        return self._exception_ip

    @exception_ip.setter
    def exception_ip(self, exception_ip):
        r"""Sets the exception_ip of this AccessAreaFilter.

        例外IP，配置指定IP不执行当前规则。

        :param exception_ip: The exception_ip of this AccessAreaFilter.
        :type exception_ip: str
        """
        self._exception_ip = exception_ip

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
        if not isinstance(other, AccessAreaFilter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
