# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ContainerSettingsDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'configs': 'ContainerConfigsDTO',
        'image_url': 'str',
        'envs': 'object',
        'volumes': 'list[VolumeDTO]',
        'resources': 'ResourceDTO',
        'ext_devices': 'list[ExtDevice]'
    }

    attribute_map = {
        'configs': 'configs',
        'image_url': 'image_url',
        'envs': 'envs',
        'volumes': 'volumes',
        'resources': 'resources',
        'ext_devices': 'ext_devices'
    }

    def __init__(self, configs=None, image_url=None, envs=None, volumes=None, resources=None, ext_devices=None):
        """ContainerSettingsDTO

        The model defined in huaweicloud sdk

        :param configs: 
        :type configs: :class:`huaweicloudsdkdris.v1.ContainerConfigsDTO`
        :param image_url: **参数说明**：镜像存储地址。
        :type image_url: str
        :param envs: **参数说明**：环境变量。
        :type envs: object
        :param volumes: **参数说明**：卷配置。
        :type volumes: list[:class:`huaweicloudsdkdris.v1.VolumeDTO`]
        :param resources: 
        :type resources: :class:`huaweicloudsdkdris.v1.ResourceDTO`
        :param ext_devices: **参数说明**：外挂设备配置。
        :type ext_devices: list[:class:`huaweicloudsdkdris.v1.ExtDevice`]
        """
        
        

        self._configs = None
        self._image_url = None
        self._envs = None
        self._volumes = None
        self._resources = None
        self._ext_devices = None
        self.discriminator = None

        if configs is not None:
            self.configs = configs
        self.image_url = image_url
        if envs is not None:
            self.envs = envs
        if volumes is not None:
            self.volumes = volumes
        if resources is not None:
            self.resources = resources
        if ext_devices is not None:
            self.ext_devices = ext_devices

    @property
    def configs(self):
        """Gets the configs of this ContainerSettingsDTO.

        :return: The configs of this ContainerSettingsDTO.
        :rtype: :class:`huaweicloudsdkdris.v1.ContainerConfigsDTO`
        """
        return self._configs

    @configs.setter
    def configs(self, configs):
        """Sets the configs of this ContainerSettingsDTO.

        :param configs: The configs of this ContainerSettingsDTO.
        :type configs: :class:`huaweicloudsdkdris.v1.ContainerConfigsDTO`
        """
        self._configs = configs

    @property
    def image_url(self):
        """Gets the image_url of this ContainerSettingsDTO.

        **参数说明**：镜像存储地址。

        :return: The image_url of this ContainerSettingsDTO.
        :rtype: str
        """
        return self._image_url

    @image_url.setter
    def image_url(self, image_url):
        """Sets the image_url of this ContainerSettingsDTO.

        **参数说明**：镜像存储地址。

        :param image_url: The image_url of this ContainerSettingsDTO.
        :type image_url: str
        """
        self._image_url = image_url

    @property
    def envs(self):
        """Gets the envs of this ContainerSettingsDTO.

        **参数说明**：环境变量。

        :return: The envs of this ContainerSettingsDTO.
        :rtype: object
        """
        return self._envs

    @envs.setter
    def envs(self, envs):
        """Sets the envs of this ContainerSettingsDTO.

        **参数说明**：环境变量。

        :param envs: The envs of this ContainerSettingsDTO.
        :type envs: object
        """
        self._envs = envs

    @property
    def volumes(self):
        """Gets the volumes of this ContainerSettingsDTO.

        **参数说明**：卷配置。

        :return: The volumes of this ContainerSettingsDTO.
        :rtype: list[:class:`huaweicloudsdkdris.v1.VolumeDTO`]
        """
        return self._volumes

    @volumes.setter
    def volumes(self, volumes):
        """Sets the volumes of this ContainerSettingsDTO.

        **参数说明**：卷配置。

        :param volumes: The volumes of this ContainerSettingsDTO.
        :type volumes: list[:class:`huaweicloudsdkdris.v1.VolumeDTO`]
        """
        self._volumes = volumes

    @property
    def resources(self):
        """Gets the resources of this ContainerSettingsDTO.

        :return: The resources of this ContainerSettingsDTO.
        :rtype: :class:`huaweicloudsdkdris.v1.ResourceDTO`
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this ContainerSettingsDTO.

        :param resources: The resources of this ContainerSettingsDTO.
        :type resources: :class:`huaweicloudsdkdris.v1.ResourceDTO`
        """
        self._resources = resources

    @property
    def ext_devices(self):
        """Gets the ext_devices of this ContainerSettingsDTO.

        **参数说明**：外挂设备配置。

        :return: The ext_devices of this ContainerSettingsDTO.
        :rtype: list[:class:`huaweicloudsdkdris.v1.ExtDevice`]
        """
        return self._ext_devices

    @ext_devices.setter
    def ext_devices(self, ext_devices):
        """Sets the ext_devices of this ContainerSettingsDTO.

        **参数说明**：外挂设备配置。

        :param ext_devices: The ext_devices of this ContainerSettingsDTO.
        :type ext_devices: list[:class:`huaweicloudsdkdris.v1.ExtDevice`]
        """
        self._ext_devices = ext_devices

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
        if not isinstance(other, ContainerSettingsDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
