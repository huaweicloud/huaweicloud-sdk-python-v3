# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateEdgeModuleReqDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'app_version': 'str',
        'module_name': 'str',
        'container_settings': 'ContainerSettingsReqDTO',
        'desired_state': 'str'
    }

    attribute_map = {
        'app_version': 'app_version',
        'module_name': 'module_name',
        'container_settings': 'container_settings',
        'desired_state': 'desired_state'
    }

    def __init__(self, app_version=None, module_name=None, container_settings=None, desired_state=None):
        r"""UpdateEdgeModuleReqDTO

        The model defined in huaweicloud sdk

        :param app_version: 边缘应用版本
        :type app_version: str
        :param module_name: 边缘模块名称
        :type module_name: str
        :param container_settings: 
        :type container_settings: :class:`huaweicloudsdkiotedge.v2.ContainerSettingsReqDTO`
        :param desired_state: 模块期望状态: RUNNING(升级后期望模块运行)，STOPPED(升级后期望模块停止)，空值默认继承升级前模块期望状态
        :type desired_state: str
        """
        
        

        self._app_version = None
        self._module_name = None
        self._container_settings = None
        self._desired_state = None
        self.discriminator = None

        if app_version is not None:
            self.app_version = app_version
        if module_name is not None:
            self.module_name = module_name
        if container_settings is not None:
            self.container_settings = container_settings
        if desired_state is not None:
            self.desired_state = desired_state

    @property
    def app_version(self):
        r"""Gets the app_version of this UpdateEdgeModuleReqDTO.

        边缘应用版本

        :return: The app_version of this UpdateEdgeModuleReqDTO.
        :rtype: str
        """
        return self._app_version

    @app_version.setter
    def app_version(self, app_version):
        r"""Sets the app_version of this UpdateEdgeModuleReqDTO.

        边缘应用版本

        :param app_version: The app_version of this UpdateEdgeModuleReqDTO.
        :type app_version: str
        """
        self._app_version = app_version

    @property
    def module_name(self):
        r"""Gets the module_name of this UpdateEdgeModuleReqDTO.

        边缘模块名称

        :return: The module_name of this UpdateEdgeModuleReqDTO.
        :rtype: str
        """
        return self._module_name

    @module_name.setter
    def module_name(self, module_name):
        r"""Sets the module_name of this UpdateEdgeModuleReqDTO.

        边缘模块名称

        :param module_name: The module_name of this UpdateEdgeModuleReqDTO.
        :type module_name: str
        """
        self._module_name = module_name

    @property
    def container_settings(self):
        r"""Gets the container_settings of this UpdateEdgeModuleReqDTO.

        :return: The container_settings of this UpdateEdgeModuleReqDTO.
        :rtype: :class:`huaweicloudsdkiotedge.v2.ContainerSettingsReqDTO`
        """
        return self._container_settings

    @container_settings.setter
    def container_settings(self, container_settings):
        r"""Sets the container_settings of this UpdateEdgeModuleReqDTO.

        :param container_settings: The container_settings of this UpdateEdgeModuleReqDTO.
        :type container_settings: :class:`huaweicloudsdkiotedge.v2.ContainerSettingsReqDTO`
        """
        self._container_settings = container_settings

    @property
    def desired_state(self):
        r"""Gets the desired_state of this UpdateEdgeModuleReqDTO.

        模块期望状态: RUNNING(升级后期望模块运行)，STOPPED(升级后期望模块停止)，空值默认继承升级前模块期望状态

        :return: The desired_state of this UpdateEdgeModuleReqDTO.
        :rtype: str
        """
        return self._desired_state

    @desired_state.setter
    def desired_state(self, desired_state):
        r"""Sets the desired_state of this UpdateEdgeModuleReqDTO.

        模块期望状态: RUNNING(升级后期望模块运行)，STOPPED(升级后期望模块停止)，空值默认继承升级前模块期望状态

        :param desired_state: The desired_state of this UpdateEdgeModuleReqDTO.
        :type desired_state: str
        """
        self._desired_state = desired_state

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
        if not isinstance(other, UpdateEdgeModuleReqDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
