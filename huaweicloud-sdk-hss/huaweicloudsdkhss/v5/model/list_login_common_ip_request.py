# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListLoginCommonIpRequest:

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
        'ip_addr': 'str'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'ip_addr': 'ip_addr'
    }

    def __init__(self, enterprise_project_id=None, ip_addr=None):
        r"""ListLoginCommonIpRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: **参数解释**: 主机所属的企业项目ID。 企业项目ID默认取值为“0”，表示默认企业项目。如果需要查询所有企业项目下的主机，请传参“all_granted_eps”。如果您只有某个企业项目的权限，则需要传递该企业项目ID，查询该企业项目下的主机，否则会因权限不足而报错。 **约束限制**: 开通企业项目功能后才需要配置企业项目。 **取值范围**: 字符长度1-256位 **默认取值**: 0 
        :type enterprise_project_id: str
        :param ip_addr: 登录IP地址+掩码
        :type ip_addr: str
        """
        
        

        self._enterprise_project_id = None
        self._ip_addr = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if ip_addr is not None:
            self.ip_addr = ip_addr

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListLoginCommonIpRequest.

        **参数解释**: 主机所属的企业项目ID。 企业项目ID默认取值为“0”，表示默认企业项目。如果需要查询所有企业项目下的主机，请传参“all_granted_eps”。如果您只有某个企业项目的权限，则需要传递该企业项目ID，查询该企业项目下的主机，否则会因权限不足而报错。 **约束限制**: 开通企业项目功能后才需要配置企业项目。 **取值范围**: 字符长度1-256位 **默认取值**: 0 

        :return: The enterprise_project_id of this ListLoginCommonIpRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListLoginCommonIpRequest.

        **参数解释**: 主机所属的企业项目ID。 企业项目ID默认取值为“0”，表示默认企业项目。如果需要查询所有企业项目下的主机，请传参“all_granted_eps”。如果您只有某个企业项目的权限，则需要传递该企业项目ID，查询该企业项目下的主机，否则会因权限不足而报错。 **约束限制**: 开通企业项目功能后才需要配置企业项目。 **取值范围**: 字符长度1-256位 **默认取值**: 0 

        :param enterprise_project_id: The enterprise_project_id of this ListLoginCommonIpRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def ip_addr(self):
        r"""Gets the ip_addr of this ListLoginCommonIpRequest.

        登录IP地址+掩码

        :return: The ip_addr of this ListLoginCommonIpRequest.
        :rtype: str
        """
        return self._ip_addr

    @ip_addr.setter
    def ip_addr(self, ip_addr):
        r"""Sets the ip_addr of this ListLoginCommonIpRequest.

        登录IP地址+掩码

        :param ip_addr: The ip_addr of this ListLoginCommonIpRequest.
        :type ip_addr: str
        """
        self._ip_addr = ip_addr

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
        if not isinstance(other, ListLoginCommonIpRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
