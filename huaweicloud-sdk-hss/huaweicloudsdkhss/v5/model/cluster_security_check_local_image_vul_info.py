# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ClusterSecurityCheckLocalImageVulInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'local_image_name': 'str',
        'local_image_version': 'str',
        'local_image_size': 'int',
        'vul_name': 'str',
        'app_name': 'str',
        'app_version': 'str',
        'severity_level': 'str',
        'solution': 'str',
        'vul_description': 'str'
    }

    attribute_map = {
        'local_image_name': 'local_image_name',
        'local_image_version': 'local_image_version',
        'local_image_size': 'local_image_size',
        'vul_name': 'vul_name',
        'app_name': 'app_name',
        'app_version': 'app_version',
        'severity_level': 'severity_level',
        'solution': 'solution',
        'vul_description': 'vul_description'
    }

    def __init__(self, local_image_name=None, local_image_version=None, local_image_size=None, vul_name=None, app_name=None, app_version=None, severity_level=None, solution=None, vul_description=None):
        r"""ClusterSecurityCheckLocalImageVulInfo

        The model defined in huaweicloud sdk

        :param local_image_name: **参数解释**： 本地镜像名称 **取值范围**： 不涉及 
        :type local_image_name: str
        :param local_image_version: **参数解释**： 本地镜像版本 **取值范围**： 不涉及 
        :type local_image_version: str
        :param local_image_size: **参数解释**： 本地镜像大小 **取值范围**： 不涉及 
        :type local_image_size: int
        :param vul_name: **参数解释**： 漏洞名称 **取值范围**： 不涉及 
        :type vul_name: str
        :param app_name: **参数解释**： 软件名称 **取值范围**： 不涉及 
        :type app_name: str
        :param app_version: **参数解释**： 软件版本 **取值范围**： 不涉及 
        :type app_version: str
        :param severity_level: **参数解释**： 漏洞危险程度 **取值范围**： - High：高危漏洞 - Medium：中危漏洞 - Low：低危漏洞 
        :type severity_level: str
        :param solution: **参数解释**： 漏洞解决方案 **取值范围**： 不涉及 
        :type solution: str
        :param vul_description: **参数解释**： 漏洞描述 **取值范围**： 不涉及 
        :type vul_description: str
        """
        
        

        self._local_image_name = None
        self._local_image_version = None
        self._local_image_size = None
        self._vul_name = None
        self._app_name = None
        self._app_version = None
        self._severity_level = None
        self._solution = None
        self._vul_description = None
        self.discriminator = None

        if local_image_name is not None:
            self.local_image_name = local_image_name
        if local_image_version is not None:
            self.local_image_version = local_image_version
        if local_image_size is not None:
            self.local_image_size = local_image_size
        if vul_name is not None:
            self.vul_name = vul_name
        if app_name is not None:
            self.app_name = app_name
        if app_version is not None:
            self.app_version = app_version
        if severity_level is not None:
            self.severity_level = severity_level
        if solution is not None:
            self.solution = solution
        if vul_description is not None:
            self.vul_description = vul_description

    @property
    def local_image_name(self):
        r"""Gets the local_image_name of this ClusterSecurityCheckLocalImageVulInfo.

        **参数解释**： 本地镜像名称 **取值范围**： 不涉及 

        :return: The local_image_name of this ClusterSecurityCheckLocalImageVulInfo.
        :rtype: str
        """
        return self._local_image_name

    @local_image_name.setter
    def local_image_name(self, local_image_name):
        r"""Sets the local_image_name of this ClusterSecurityCheckLocalImageVulInfo.

        **参数解释**： 本地镜像名称 **取值范围**： 不涉及 

        :param local_image_name: The local_image_name of this ClusterSecurityCheckLocalImageVulInfo.
        :type local_image_name: str
        """
        self._local_image_name = local_image_name

    @property
    def local_image_version(self):
        r"""Gets the local_image_version of this ClusterSecurityCheckLocalImageVulInfo.

        **参数解释**： 本地镜像版本 **取值范围**： 不涉及 

        :return: The local_image_version of this ClusterSecurityCheckLocalImageVulInfo.
        :rtype: str
        """
        return self._local_image_version

    @local_image_version.setter
    def local_image_version(self, local_image_version):
        r"""Sets the local_image_version of this ClusterSecurityCheckLocalImageVulInfo.

        **参数解释**： 本地镜像版本 **取值范围**： 不涉及 

        :param local_image_version: The local_image_version of this ClusterSecurityCheckLocalImageVulInfo.
        :type local_image_version: str
        """
        self._local_image_version = local_image_version

    @property
    def local_image_size(self):
        r"""Gets the local_image_size of this ClusterSecurityCheckLocalImageVulInfo.

        **参数解释**： 本地镜像大小 **取值范围**： 不涉及 

        :return: The local_image_size of this ClusterSecurityCheckLocalImageVulInfo.
        :rtype: int
        """
        return self._local_image_size

    @local_image_size.setter
    def local_image_size(self, local_image_size):
        r"""Sets the local_image_size of this ClusterSecurityCheckLocalImageVulInfo.

        **参数解释**： 本地镜像大小 **取值范围**： 不涉及 

        :param local_image_size: The local_image_size of this ClusterSecurityCheckLocalImageVulInfo.
        :type local_image_size: int
        """
        self._local_image_size = local_image_size

    @property
    def vul_name(self):
        r"""Gets the vul_name of this ClusterSecurityCheckLocalImageVulInfo.

        **参数解释**： 漏洞名称 **取值范围**： 不涉及 

        :return: The vul_name of this ClusterSecurityCheckLocalImageVulInfo.
        :rtype: str
        """
        return self._vul_name

    @vul_name.setter
    def vul_name(self, vul_name):
        r"""Sets the vul_name of this ClusterSecurityCheckLocalImageVulInfo.

        **参数解释**： 漏洞名称 **取值范围**： 不涉及 

        :param vul_name: The vul_name of this ClusterSecurityCheckLocalImageVulInfo.
        :type vul_name: str
        """
        self._vul_name = vul_name

    @property
    def app_name(self):
        r"""Gets the app_name of this ClusterSecurityCheckLocalImageVulInfo.

        **参数解释**： 软件名称 **取值范围**： 不涉及 

        :return: The app_name of this ClusterSecurityCheckLocalImageVulInfo.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        r"""Sets the app_name of this ClusterSecurityCheckLocalImageVulInfo.

        **参数解释**： 软件名称 **取值范围**： 不涉及 

        :param app_name: The app_name of this ClusterSecurityCheckLocalImageVulInfo.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def app_version(self):
        r"""Gets the app_version of this ClusterSecurityCheckLocalImageVulInfo.

        **参数解释**： 软件版本 **取值范围**： 不涉及 

        :return: The app_version of this ClusterSecurityCheckLocalImageVulInfo.
        :rtype: str
        """
        return self._app_version

    @app_version.setter
    def app_version(self, app_version):
        r"""Sets the app_version of this ClusterSecurityCheckLocalImageVulInfo.

        **参数解释**： 软件版本 **取值范围**： 不涉及 

        :param app_version: The app_version of this ClusterSecurityCheckLocalImageVulInfo.
        :type app_version: str
        """
        self._app_version = app_version

    @property
    def severity_level(self):
        r"""Gets the severity_level of this ClusterSecurityCheckLocalImageVulInfo.

        **参数解释**： 漏洞危险程度 **取值范围**： - High：高危漏洞 - Medium：中危漏洞 - Low：低危漏洞 

        :return: The severity_level of this ClusterSecurityCheckLocalImageVulInfo.
        :rtype: str
        """
        return self._severity_level

    @severity_level.setter
    def severity_level(self, severity_level):
        r"""Sets the severity_level of this ClusterSecurityCheckLocalImageVulInfo.

        **参数解释**： 漏洞危险程度 **取值范围**： - High：高危漏洞 - Medium：中危漏洞 - Low：低危漏洞 

        :param severity_level: The severity_level of this ClusterSecurityCheckLocalImageVulInfo.
        :type severity_level: str
        """
        self._severity_level = severity_level

    @property
    def solution(self):
        r"""Gets the solution of this ClusterSecurityCheckLocalImageVulInfo.

        **参数解释**： 漏洞解决方案 **取值范围**： 不涉及 

        :return: The solution of this ClusterSecurityCheckLocalImageVulInfo.
        :rtype: str
        """
        return self._solution

    @solution.setter
    def solution(self, solution):
        r"""Sets the solution of this ClusterSecurityCheckLocalImageVulInfo.

        **参数解释**： 漏洞解决方案 **取值范围**： 不涉及 

        :param solution: The solution of this ClusterSecurityCheckLocalImageVulInfo.
        :type solution: str
        """
        self._solution = solution

    @property
    def vul_description(self):
        r"""Gets the vul_description of this ClusterSecurityCheckLocalImageVulInfo.

        **参数解释**： 漏洞描述 **取值范围**： 不涉及 

        :return: The vul_description of this ClusterSecurityCheckLocalImageVulInfo.
        :rtype: str
        """
        return self._vul_description

    @vul_description.setter
    def vul_description(self, vul_description):
        r"""Sets the vul_description of this ClusterSecurityCheckLocalImageVulInfo.

        **参数解释**： 漏洞描述 **取值范围**： 不涉及 

        :param vul_description: The vul_description of this ClusterSecurityCheckLocalImageVulInfo.
        :type vul_description: str
        """
        self._vul_description = vul_description

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
        if not isinstance(other, ClusterSecurityCheckLocalImageVulInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
