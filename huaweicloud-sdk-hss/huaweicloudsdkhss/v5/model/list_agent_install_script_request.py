# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAgentInstallScriptRequest:

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
        'os_type': 'str',
        'os_arch': 'str',
        'outside_host': 'bool',
        'outside_group_id': 'str',
        'batch_install': 'bool',
        'type': 'str'
    }

    attribute_map = {
        'region': 'region',
        'enterprise_project_id': 'enterprise_project_id',
        'os_type': 'os_type',
        'os_arch': 'os_arch',
        'outside_host': 'outside_host',
        'outside_group_id': 'outside_group_id',
        'batch_install': 'batch_install',
        'type': 'type'
    }

    def __init__(self, region=None, enterprise_project_id=None, os_type=None, os_arch=None, outside_host=None, outside_group_id=None, batch_install=None, type=None):
        r"""ListAgentInstallScriptRequest

        The model defined in huaweicloud sdk

        :param region: **参数解释**: 区域ID，用于查询目的区域内的资产。获取方式请参见[获取区域ID](hss_02_0026.xml)。 **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 
        :type region: str
        :param enterprise_project_id: **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 
        :type enterprise_project_id: str
        :param os_type: os类型：Windows和Linux
        :type os_type: str
        :param os_arch: 系统架构：x86_64和aarch64；当os_type为Windows时，只能选择x86_64
        :type os_arch: str
        :param outside_host: 是否非华为云
        :type outside_host: bool
        :param outside_group_id: 服务器组ID，此参数已废弃
        :type outside_group_id: str
        :param batch_install: 是否批量安装
        :type batch_install: bool
        :param type: 类型：password和ssh_key
        :type type: str
        """
        
        

        self._region = None
        self._enterprise_project_id = None
        self._os_type = None
        self._os_arch = None
        self._outside_host = None
        self._outside_group_id = None
        self._batch_install = None
        self._type = None
        self.discriminator = None

        if region is not None:
            self.region = region
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if os_type is not None:
            self.os_type = os_type
        self.os_arch = os_arch
        if outside_host is not None:
            self.outside_host = outside_host
        if outside_group_id is not None:
            self.outside_group_id = outside_group_id
        if batch_install is not None:
            self.batch_install = batch_install
        if type is not None:
            self.type = type

    @property
    def region(self):
        r"""Gets the region of this ListAgentInstallScriptRequest.

        **参数解释**: 区域ID，用于查询目的区域内的资产。获取方式请参见[获取区域ID](hss_02_0026.xml)。 **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 

        :return: The region of this ListAgentInstallScriptRequest.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this ListAgentInstallScriptRequest.

        **参数解释**: 区域ID，用于查询目的区域内的资产。获取方式请参见[获取区域ID](hss_02_0026.xml)。 **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 

        :param region: The region of this ListAgentInstallScriptRequest.
        :type region: str
        """
        self._region = region

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListAgentInstallScriptRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :return: The enterprise_project_id of this ListAgentInstallScriptRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListAgentInstallScriptRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :param enterprise_project_id: The enterprise_project_id of this ListAgentInstallScriptRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def os_type(self):
        r"""Gets the os_type of this ListAgentInstallScriptRequest.

        os类型：Windows和Linux

        :return: The os_type of this ListAgentInstallScriptRequest.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        r"""Sets the os_type of this ListAgentInstallScriptRequest.

        os类型：Windows和Linux

        :param os_type: The os_type of this ListAgentInstallScriptRequest.
        :type os_type: str
        """
        self._os_type = os_type

    @property
    def os_arch(self):
        r"""Gets the os_arch of this ListAgentInstallScriptRequest.

        系统架构：x86_64和aarch64；当os_type为Windows时，只能选择x86_64

        :return: The os_arch of this ListAgentInstallScriptRequest.
        :rtype: str
        """
        return self._os_arch

    @os_arch.setter
    def os_arch(self, os_arch):
        r"""Sets the os_arch of this ListAgentInstallScriptRequest.

        系统架构：x86_64和aarch64；当os_type为Windows时，只能选择x86_64

        :param os_arch: The os_arch of this ListAgentInstallScriptRequest.
        :type os_arch: str
        """
        self._os_arch = os_arch

    @property
    def outside_host(self):
        r"""Gets the outside_host of this ListAgentInstallScriptRequest.

        是否非华为云

        :return: The outside_host of this ListAgentInstallScriptRequest.
        :rtype: bool
        """
        return self._outside_host

    @outside_host.setter
    def outside_host(self, outside_host):
        r"""Sets the outside_host of this ListAgentInstallScriptRequest.

        是否非华为云

        :param outside_host: The outside_host of this ListAgentInstallScriptRequest.
        :type outside_host: bool
        """
        self._outside_host = outside_host

    @property
    def outside_group_id(self):
        r"""Gets the outside_group_id of this ListAgentInstallScriptRequest.

        服务器组ID，此参数已废弃

        :return: The outside_group_id of this ListAgentInstallScriptRequest.
        :rtype: str
        """
        return self._outside_group_id

    @outside_group_id.setter
    def outside_group_id(self, outside_group_id):
        r"""Sets the outside_group_id of this ListAgentInstallScriptRequest.

        服务器组ID，此参数已废弃

        :param outside_group_id: The outside_group_id of this ListAgentInstallScriptRequest.
        :type outside_group_id: str
        """
        self._outside_group_id = outside_group_id

    @property
    def batch_install(self):
        r"""Gets the batch_install of this ListAgentInstallScriptRequest.

        是否批量安装

        :return: The batch_install of this ListAgentInstallScriptRequest.
        :rtype: bool
        """
        return self._batch_install

    @batch_install.setter
    def batch_install(self, batch_install):
        r"""Sets the batch_install of this ListAgentInstallScriptRequest.

        是否批量安装

        :param batch_install: The batch_install of this ListAgentInstallScriptRequest.
        :type batch_install: bool
        """
        self._batch_install = batch_install

    @property
    def type(self):
        r"""Gets the type of this ListAgentInstallScriptRequest.

        类型：password和ssh_key

        :return: The type of this ListAgentInstallScriptRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ListAgentInstallScriptRequest.

        类型：password和ssh_key

        :param type: The type of this ListAgentInstallScriptRequest.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, ListAgentInstallScriptRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
