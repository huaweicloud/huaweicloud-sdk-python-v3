# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BaselineWhiteListsResponseInfo:

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
        'rule_type': 'str',
        'os_type': 'str',
        'index_version': 'str',
        'check_type': 'str',
        'standard': 'str',
        'tag': 'str',
        'check_rule_name': 'str',
        'description': 'str'
    }

    attribute_map = {
        'id': 'id',
        'rule_type': 'rule_type',
        'os_type': 'os_type',
        'index_version': 'index_version',
        'check_type': 'check_type',
        'standard': 'standard',
        'tag': 'tag',
        'check_rule_name': 'check_rule_name',
        'description': 'description'
    }

    def __init__(self, id=None, rule_type=None, os_type=None, index_version=None, check_type=None, standard=None, tag=None, check_rule_name=None, description=None):
        r"""BaselineWhiteListsResponseInfo

        The model defined in huaweicloud sdk

        :param id: 基线白名单标识
        :type id: str
        :param rule_type: 基线检查白名单的规则范围 - specific_host：部分主机 - all_host：全部主机
        :type rule_type: str
        :param os_type: 基线检查的操作系统 - Linux - Windows
        :type os_type: str
        :param index_version: 基线检查的检查项标识
        :type index_version: str
        :param check_type: 基线检查的基线名称
        :type check_type: str
        :param standard: 标准类型，包含如下:   - cn_standard : 等保合规标准   - hw_standard : 云安全实践标准   - cis_standard : 通用安全标准
        :type standard: str
        :param tag: 基线检查中检查项的检查类型 - 访问控制 - 服务配置
        :type tag: str
        :param check_rule_name: 基线检查中检查项的名称
        :type check_rule_name: str
        :param description: 基线白名单备注
        :type description: str
        """
        
        

        self._id = None
        self._rule_type = None
        self._os_type = None
        self._index_version = None
        self._check_type = None
        self._standard = None
        self._tag = None
        self._check_rule_name = None
        self._description = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if rule_type is not None:
            self.rule_type = rule_type
        if os_type is not None:
            self.os_type = os_type
        if index_version is not None:
            self.index_version = index_version
        if check_type is not None:
            self.check_type = check_type
        if standard is not None:
            self.standard = standard
        if tag is not None:
            self.tag = tag
        if check_rule_name is not None:
            self.check_rule_name = check_rule_name
        if description is not None:
            self.description = description

    @property
    def id(self):
        r"""Gets the id of this BaselineWhiteListsResponseInfo.

        基线白名单标识

        :return: The id of this BaselineWhiteListsResponseInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this BaselineWhiteListsResponseInfo.

        基线白名单标识

        :param id: The id of this BaselineWhiteListsResponseInfo.
        :type id: str
        """
        self._id = id

    @property
    def rule_type(self):
        r"""Gets the rule_type of this BaselineWhiteListsResponseInfo.

        基线检查白名单的规则范围 - specific_host：部分主机 - all_host：全部主机

        :return: The rule_type of this BaselineWhiteListsResponseInfo.
        :rtype: str
        """
        return self._rule_type

    @rule_type.setter
    def rule_type(self, rule_type):
        r"""Sets the rule_type of this BaselineWhiteListsResponseInfo.

        基线检查白名单的规则范围 - specific_host：部分主机 - all_host：全部主机

        :param rule_type: The rule_type of this BaselineWhiteListsResponseInfo.
        :type rule_type: str
        """
        self._rule_type = rule_type

    @property
    def os_type(self):
        r"""Gets the os_type of this BaselineWhiteListsResponseInfo.

        基线检查的操作系统 - Linux - Windows

        :return: The os_type of this BaselineWhiteListsResponseInfo.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        r"""Sets the os_type of this BaselineWhiteListsResponseInfo.

        基线检查的操作系统 - Linux - Windows

        :param os_type: The os_type of this BaselineWhiteListsResponseInfo.
        :type os_type: str
        """
        self._os_type = os_type

    @property
    def index_version(self):
        r"""Gets the index_version of this BaselineWhiteListsResponseInfo.

        基线检查的检查项标识

        :return: The index_version of this BaselineWhiteListsResponseInfo.
        :rtype: str
        """
        return self._index_version

    @index_version.setter
    def index_version(self, index_version):
        r"""Sets the index_version of this BaselineWhiteListsResponseInfo.

        基线检查的检查项标识

        :param index_version: The index_version of this BaselineWhiteListsResponseInfo.
        :type index_version: str
        """
        self._index_version = index_version

    @property
    def check_type(self):
        r"""Gets the check_type of this BaselineWhiteListsResponseInfo.

        基线检查的基线名称

        :return: The check_type of this BaselineWhiteListsResponseInfo.
        :rtype: str
        """
        return self._check_type

    @check_type.setter
    def check_type(self, check_type):
        r"""Sets the check_type of this BaselineWhiteListsResponseInfo.

        基线检查的基线名称

        :param check_type: The check_type of this BaselineWhiteListsResponseInfo.
        :type check_type: str
        """
        self._check_type = check_type

    @property
    def standard(self):
        r"""Gets the standard of this BaselineWhiteListsResponseInfo.

        标准类型，包含如下:   - cn_standard : 等保合规标准   - hw_standard : 云安全实践标准   - cis_standard : 通用安全标准

        :return: The standard of this BaselineWhiteListsResponseInfo.
        :rtype: str
        """
        return self._standard

    @standard.setter
    def standard(self, standard):
        r"""Sets the standard of this BaselineWhiteListsResponseInfo.

        标准类型，包含如下:   - cn_standard : 等保合规标准   - hw_standard : 云安全实践标准   - cis_standard : 通用安全标准

        :param standard: The standard of this BaselineWhiteListsResponseInfo.
        :type standard: str
        """
        self._standard = standard

    @property
    def tag(self):
        r"""Gets the tag of this BaselineWhiteListsResponseInfo.

        基线检查中检查项的检查类型 - 访问控制 - 服务配置

        :return: The tag of this BaselineWhiteListsResponseInfo.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        r"""Sets the tag of this BaselineWhiteListsResponseInfo.

        基线检查中检查项的检查类型 - 访问控制 - 服务配置

        :param tag: The tag of this BaselineWhiteListsResponseInfo.
        :type tag: str
        """
        self._tag = tag

    @property
    def check_rule_name(self):
        r"""Gets the check_rule_name of this BaselineWhiteListsResponseInfo.

        基线检查中检查项的名称

        :return: The check_rule_name of this BaselineWhiteListsResponseInfo.
        :rtype: str
        """
        return self._check_rule_name

    @check_rule_name.setter
    def check_rule_name(self, check_rule_name):
        r"""Sets the check_rule_name of this BaselineWhiteListsResponseInfo.

        基线检查中检查项的名称

        :param check_rule_name: The check_rule_name of this BaselineWhiteListsResponseInfo.
        :type check_rule_name: str
        """
        self._check_rule_name = check_rule_name

    @property
    def description(self):
        r"""Gets the description of this BaselineWhiteListsResponseInfo.

        基线白名单备注

        :return: The description of this BaselineWhiteListsResponseInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this BaselineWhiteListsResponseInfo.

        基线白名单备注

        :param description: The description of this BaselineWhiteListsResponseInfo.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, BaselineWhiteListsResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
