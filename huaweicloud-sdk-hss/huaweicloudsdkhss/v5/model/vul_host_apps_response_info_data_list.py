# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VulHostAppsResponseInfoDataList:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'app_name': 'str',
        'path': 'str',
        'paths': 'list[VulHostAppsResponseInfoPaths]',
        'rule': 'str'
    }

    attribute_map = {
        'app_name': 'app_name',
        'path': 'path',
        'paths': 'paths',
        'rule': 'rule'
    }

    def __init__(self, app_name=None, path=None, paths=None, rule=None):
        r"""VulHostAppsResponseInfoDataList

        The model defined in huaweicloud sdk

        :param app_name: **参数解释**: app名称 **取值范围**: 字符长度1-128位 
        :type app_name: str
        :param path: **参数解释**: 存在漏洞的软件路径，仅应用漏洞、应急漏洞等存在软件路径的漏洞类型查询时存在该字段（注：该字段即将弃用，请使用paths字段获取软件路径相关信息） **取值范围**: 字符长度1-512位 
        :type path: str
        :param paths: **参数解释**: 存在漏洞的软件路径列表，仅应用漏洞、应急漏洞等存在软件路径的漏洞类型查询时存在该字段 **取值范围**: 不涉及 
        :type paths: list[:class:`huaweicloudsdkhss.v5.VulHostAppsResponseInfoPaths`]
        :param rule: **参数解释**: 软件命中的漏洞匹配规则 **取值范围**: 字符长度1-512位 
        :type rule: str
        """
        
        

        self._app_name = None
        self._path = None
        self._paths = None
        self._rule = None
        self.discriminator = None

        if app_name is not None:
            self.app_name = app_name
        if path is not None:
            self.path = path
        if paths is not None:
            self.paths = paths
        if rule is not None:
            self.rule = rule

    @property
    def app_name(self):
        r"""Gets the app_name of this VulHostAppsResponseInfoDataList.

        **参数解释**: app名称 **取值范围**: 字符长度1-128位 

        :return: The app_name of this VulHostAppsResponseInfoDataList.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        r"""Sets the app_name of this VulHostAppsResponseInfoDataList.

        **参数解释**: app名称 **取值范围**: 字符长度1-128位 

        :param app_name: The app_name of this VulHostAppsResponseInfoDataList.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def path(self):
        r"""Gets the path of this VulHostAppsResponseInfoDataList.

        **参数解释**: 存在漏洞的软件路径，仅应用漏洞、应急漏洞等存在软件路径的漏洞类型查询时存在该字段（注：该字段即将弃用，请使用paths字段获取软件路径相关信息） **取值范围**: 字符长度1-512位 

        :return: The path of this VulHostAppsResponseInfoDataList.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        r"""Sets the path of this VulHostAppsResponseInfoDataList.

        **参数解释**: 存在漏洞的软件路径，仅应用漏洞、应急漏洞等存在软件路径的漏洞类型查询时存在该字段（注：该字段即将弃用，请使用paths字段获取软件路径相关信息） **取值范围**: 字符长度1-512位 

        :param path: The path of this VulHostAppsResponseInfoDataList.
        :type path: str
        """
        self._path = path

    @property
    def paths(self):
        r"""Gets the paths of this VulHostAppsResponseInfoDataList.

        **参数解释**: 存在漏洞的软件路径列表，仅应用漏洞、应急漏洞等存在软件路径的漏洞类型查询时存在该字段 **取值范围**: 不涉及 

        :return: The paths of this VulHostAppsResponseInfoDataList.
        :rtype: list[:class:`huaweicloudsdkhss.v5.VulHostAppsResponseInfoPaths`]
        """
        return self._paths

    @paths.setter
    def paths(self, paths):
        r"""Sets the paths of this VulHostAppsResponseInfoDataList.

        **参数解释**: 存在漏洞的软件路径列表，仅应用漏洞、应急漏洞等存在软件路径的漏洞类型查询时存在该字段 **取值范围**: 不涉及 

        :param paths: The paths of this VulHostAppsResponseInfoDataList.
        :type paths: list[:class:`huaweicloudsdkhss.v5.VulHostAppsResponseInfoPaths`]
        """
        self._paths = paths

    @property
    def rule(self):
        r"""Gets the rule of this VulHostAppsResponseInfoDataList.

        **参数解释**: 软件命中的漏洞匹配规则 **取值范围**: 字符长度1-512位 

        :return: The rule of this VulHostAppsResponseInfoDataList.
        :rtype: str
        """
        return self._rule

    @rule.setter
    def rule(self, rule):
        r"""Sets the rule of this VulHostAppsResponseInfoDataList.

        **参数解释**: 软件命中的漏洞匹配规则 **取值范围**: 字符长度1-512位 

        :param rule: The rule of this VulHostAppsResponseInfoDataList.
        :type rule: str
        """
        self._rule = rule

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
        if not isinstance(other, VulHostAppsResponseInfoDataList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
