# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListJarPackageInfoRequest:

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
        'host_id': 'str',
        'file_name': 'str',
        'category': 'str'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'host_id': 'host_id',
        'file_name': 'file_name',
        'category': 'category'
    }

    def __init__(self, enterprise_project_id=None, host_id=None, file_name=None, category=None):
        r"""ListJarPackageInfoRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 
        :type enterprise_project_id: str
        :param host_id: **参数解释**: 服务器ID **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 
        :type host_id: str
        :param file_name: **参数解释**: 文件名称 **约束限制**: 不涉及 **取值范围**: 字符长度1-256 **默认取值**: 不涉及 
        :type file_name: str
        :param category: **参数解释**: 类别 **约束限制**: 不涉及 **取值范围**: - host : 主机 - container : 容器  **默认取值**: 不涉及 
        :type category: str
        """
        
        

        self._enterprise_project_id = None
        self._host_id = None
        self._file_name = None
        self._category = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        self.host_id = host_id
        if file_name is not None:
            self.file_name = file_name
        self.category = category

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListJarPackageInfoRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :return: The enterprise_project_id of this ListJarPackageInfoRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListJarPackageInfoRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :param enterprise_project_id: The enterprise_project_id of this ListJarPackageInfoRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def host_id(self):
        r"""Gets the host_id of this ListJarPackageInfoRequest.

        **参数解释**: 服务器ID **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 

        :return: The host_id of this ListJarPackageInfoRequest.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        r"""Sets the host_id of this ListJarPackageInfoRequest.

        **参数解释**: 服务器ID **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 

        :param host_id: The host_id of this ListJarPackageInfoRequest.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def file_name(self):
        r"""Gets the file_name of this ListJarPackageInfoRequest.

        **参数解释**: 文件名称 **约束限制**: 不涉及 **取值范围**: 字符长度1-256 **默认取值**: 不涉及 

        :return: The file_name of this ListJarPackageInfoRequest.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        r"""Sets the file_name of this ListJarPackageInfoRequest.

        **参数解释**: 文件名称 **约束限制**: 不涉及 **取值范围**: 字符长度1-256 **默认取值**: 不涉及 

        :param file_name: The file_name of this ListJarPackageInfoRequest.
        :type file_name: str
        """
        self._file_name = file_name

    @property
    def category(self):
        r"""Gets the category of this ListJarPackageInfoRequest.

        **参数解释**: 类别 **约束限制**: 不涉及 **取值范围**: - host : 主机 - container : 容器  **默认取值**: 不涉及 

        :return: The category of this ListJarPackageInfoRequest.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this ListJarPackageInfoRequest.

        **参数解释**: 类别 **约束限制**: 不涉及 **取值范围**: - host : 主机 - container : 容器  **默认取值**: 不涉及 

        :param category: The category of this ListJarPackageInfoRequest.
        :type category: str
        """
        self._category = category

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
        if not isinstance(other, ListJarPackageInfoRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
