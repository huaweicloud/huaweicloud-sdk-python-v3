# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HostVulnItemComponentList:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'component_name': 'str',
        'component_install_version': 'str',
        'component_fixed_version': 'str'
    }

    attribute_map = {
        'component_name': 'componentName',
        'component_install_version': 'componentInstallVersion',
        'component_fixed_version': 'componentFixedVersion'
    }

    def __init__(self, component_name=None, component_install_version=None, component_fixed_version=None):
        r"""HostVulnItemComponentList

        The model defined in huaweicloud sdk

        :param component_name: 内容名称
        :type component_name: str
        :param component_install_version: 安装版本
        :type component_install_version: str
        :param component_fixed_version: 已经修复版本
        :type component_fixed_version: str
        """
        
        

        self._component_name = None
        self._component_install_version = None
        self._component_fixed_version = None
        self.discriminator = None

        if component_name is not None:
            self.component_name = component_name
        if component_install_version is not None:
            self.component_install_version = component_install_version
        if component_fixed_version is not None:
            self.component_fixed_version = component_fixed_version

    @property
    def component_name(self):
        r"""Gets the component_name of this HostVulnItemComponentList.

        内容名称

        :return: The component_name of this HostVulnItemComponentList.
        :rtype: str
        """
        return self._component_name

    @component_name.setter
    def component_name(self, component_name):
        r"""Sets the component_name of this HostVulnItemComponentList.

        内容名称

        :param component_name: The component_name of this HostVulnItemComponentList.
        :type component_name: str
        """
        self._component_name = component_name

    @property
    def component_install_version(self):
        r"""Gets the component_install_version of this HostVulnItemComponentList.

        安装版本

        :return: The component_install_version of this HostVulnItemComponentList.
        :rtype: str
        """
        return self._component_install_version

    @component_install_version.setter
    def component_install_version(self, component_install_version):
        r"""Sets the component_install_version of this HostVulnItemComponentList.

        安装版本

        :param component_install_version: The component_install_version of this HostVulnItemComponentList.
        :type component_install_version: str
        """
        self._component_install_version = component_install_version

    @property
    def component_fixed_version(self):
        r"""Gets the component_fixed_version of this HostVulnItemComponentList.

        已经修复版本

        :return: The component_fixed_version of this HostVulnItemComponentList.
        :rtype: str
        """
        return self._component_fixed_version

    @component_fixed_version.setter
    def component_fixed_version(self, component_fixed_version):
        r"""Sets the component_fixed_version of this HostVulnItemComponentList.

        已经修复版本

        :param component_fixed_version: The component_fixed_version of this HostVulnItemComponentList.
        :type component_fixed_version: str
        """
        self._component_fixed_version = component_fixed_version

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
        if not isinstance(other, HostVulnItemComponentList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
