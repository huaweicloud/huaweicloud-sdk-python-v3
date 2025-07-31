# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPasswordComplexityRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enterprise_project_id': 'str',
        'host_name': 'str',
        'host_ip': 'str',
        'host_id': 'str',
        'result_type': 'str',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'host_name': 'host_name',
        'host_ip': 'host_ip',
        'host_id': 'host_id',
        'result_type': 'result_type',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, enterprise_project_id=None, host_name=None, host_ip=None, host_id=None, result_type=None, limit=None, offset=None):
        r"""ListPasswordComplexityRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 
        :type enterprise_project_id: str
        :param host_name: **参数解释**: 服务器名称 **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 0 
        :type host_name: str
        :param host_ip: **参数解释**: 服务器IP地址 **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 0 
        :type host_ip: str
        :param host_id: **参数解释**: 主机id，不赋值时，查租户所有主机 **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 0 
        :type host_id: str
        :param result_type: **参数解释**: 结果类型 **约束限制**: 不涉及 **取值范围**: - unhandled : 未忽略的 - ignored   : 已忽略的 **默认取值**: unhandled 
        :type result_type: str
        :param limit: **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 
        :type limit: int
        :param offset: **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 
        :type offset: int
        """
        
        

        self._enterprise_project_id = None
        self._host_name = None
        self._host_ip = None
        self._host_id = None
        self._result_type = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if host_name is not None:
            self.host_name = host_name
        if host_ip is not None:
            self.host_ip = host_ip
        if host_id is not None:
            self.host_id = host_id
        if result_type is not None:
            self.result_type = result_type
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListPasswordComplexityRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :return: The enterprise_project_id of this ListPasswordComplexityRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListPasswordComplexityRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :param enterprise_project_id: The enterprise_project_id of this ListPasswordComplexityRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def host_name(self):
        r"""Gets the host_name of this ListPasswordComplexityRequest.

        **参数解释**: 服务器名称 **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 0 

        :return: The host_name of this ListPasswordComplexityRequest.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this ListPasswordComplexityRequest.

        **参数解释**: 服务器名称 **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 0 

        :param host_name: The host_name of this ListPasswordComplexityRequest.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def host_ip(self):
        r"""Gets the host_ip of this ListPasswordComplexityRequest.

        **参数解释**: 服务器IP地址 **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 0 

        :return: The host_ip of this ListPasswordComplexityRequest.
        :rtype: str
        """
        return self._host_ip

    @host_ip.setter
    def host_ip(self, host_ip):
        r"""Sets the host_ip of this ListPasswordComplexityRequest.

        **参数解释**: 服务器IP地址 **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 0 

        :param host_ip: The host_ip of this ListPasswordComplexityRequest.
        :type host_ip: str
        """
        self._host_ip = host_ip

    @property
    def host_id(self):
        r"""Gets the host_id of this ListPasswordComplexityRequest.

        **参数解释**: 主机id，不赋值时，查租户所有主机 **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 0 

        :return: The host_id of this ListPasswordComplexityRequest.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        r"""Sets the host_id of this ListPasswordComplexityRequest.

        **参数解释**: 主机id，不赋值时，查租户所有主机 **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 0 

        :param host_id: The host_id of this ListPasswordComplexityRequest.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def result_type(self):
        r"""Gets the result_type of this ListPasswordComplexityRequest.

        **参数解释**: 结果类型 **约束限制**: 不涉及 **取值范围**: - unhandled : 未忽略的 - ignored   : 已忽略的 **默认取值**: unhandled 

        :return: The result_type of this ListPasswordComplexityRequest.
        :rtype: str
        """
        return self._result_type

    @result_type.setter
    def result_type(self, result_type):
        r"""Sets the result_type of this ListPasswordComplexityRequest.

        **参数解释**: 结果类型 **约束限制**: 不涉及 **取值范围**: - unhandled : 未忽略的 - ignored   : 已忽略的 **默认取值**: unhandled 

        :param result_type: The result_type of this ListPasswordComplexityRequest.
        :type result_type: str
        """
        self._result_type = result_type

    @property
    def limit(self):
        r"""Gets the limit of this ListPasswordComplexityRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :return: The limit of this ListPasswordComplexityRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListPasswordComplexityRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :param limit: The limit of this ListPasswordComplexityRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListPasswordComplexityRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 

        :return: The offset of this ListPasswordComplexityRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListPasswordComplexityRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 

        :param offset: The offset of this ListPasswordComplexityRequest.
        :type offset: int
        """
        self._offset = offset

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
        if not isinstance(other, ListPasswordComplexityRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
