# coding: utf-8

import pprint
import re

import six





class CinderExportToImageOption:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'container_format': 'str',
        'disk_format': 'str',
        'force': 'bool',
        'image_name': 'str',
        'os_type': 'str'
    }

    attribute_map = {
        'container_format': 'container_format',
        'disk_format': 'disk_format',
        'force': 'force',
        'image_name': 'image_name',
        'os_type': '__os_type'
    }

    def __init__(self, container_format='bare', disk_format='vhd', force=None, image_name=None, os_type='linux'):
        """CinderExportToImageOption - a model defined in huaweicloud sdk"""
        
        

        self._container_format = None
        self._disk_format = None
        self._force = None
        self._image_name = None
        self._os_type = None
        self.discriminator = None

        if container_format is not None:
            self.container_format = container_format
        if disk_format is not None:
            self.disk_format = disk_format
        if force is not None:
            self.force = force
        self.image_name = image_name
        if os_type is not None:
            self.os_type = os_type

    @property
    def container_format(self):
        """Gets the container_format of this CinderExportToImageOption.

        云硬盘导出镜像的容器类型。  目前支持ami、ari、aki、ovf、bare。默认是bare。

        :return: The container_format of this CinderExportToImageOption.
        :rtype: str
        """
        return self._container_format

    @container_format.setter
    def container_format(self, container_format):
        """Sets the container_format of this CinderExportToImageOption.

        云硬盘导出镜像的容器类型。  目前支持ami、ari、aki、ovf、bare。默认是bare。

        :param container_format: The container_format of this CinderExportToImageOption.
        :type: str
        """
        self._container_format = container_format

    @property
    def disk_format(self):
        """Gets the disk_format of this CinderExportToImageOption.

        云硬盘导出镜像的格式。  目前支持vhd、zvhd、zvhd2、raw、qcow2。默认是vhd。

        :return: The disk_format of this CinderExportToImageOption.
        :rtype: str
        """
        return self._disk_format

    @disk_format.setter
    def disk_format(self, disk_format):
        """Sets the disk_format of this CinderExportToImageOption.

        云硬盘导出镜像的格式。  目前支持vhd、zvhd、zvhd2、raw、qcow2。默认是vhd。

        :param disk_format: The disk_format of this CinderExportToImageOption.
        :type: str
        """
        self._disk_format = disk_format

    @property
    def force(self):
        """Gets the force of this CinderExportToImageOption.

        强制导出镜像的标示，默认值是false。  当force标记为false时，云硬盘处于正在使用状态时，不能强制导出镜像。 当force标记为true时，即使云硬盘处于正在使用状态时，仍可以导出镜像。

        :return: The force of this CinderExportToImageOption.
        :rtype: bool
        """
        return self._force

    @force.setter
    def force(self, force):
        """Sets the force of this CinderExportToImageOption.

        强制导出镜像的标示，默认值是false。  当force标记为false时，云硬盘处于正在使用状态时，不能强制导出镜像。 当force标记为true时，即使云硬盘处于正在使用状态时，仍可以导出镜像。

        :param force: The force of this CinderExportToImageOption.
        :type: bool
        """
        self._force = force

    @property
    def image_name(self):
        """Gets the image_name of this CinderExportToImageOption.

        云硬盘导出镜像的名称。  名称的长度范围为1～128位。 名称只能包含以下字符：大写字母、小写字母、中文、数字、特殊字符包含“-”、“.”、“_”和空格。

        :return: The image_name of this CinderExportToImageOption.
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        """Sets the image_name of this CinderExportToImageOption.

        云硬盘导出镜像的名称。  名称的长度范围为1～128位。 名称只能包含以下字符：大写字母、小写字母、中文、数字、特殊字符包含“-”、“.”、“_”和空格。

        :param image_name: The image_name of this CinderExportToImageOption.
        :type: str
        """
        self._image_name = image_name

    @property
    def os_type(self):
        """Gets the os_type of this CinderExportToImageOption.

        云硬盘导出镜像的系统类型。目前只支持“windows”和“linux”，默认值是“linux”。  说明： 只有云硬盘的volume_image_metadata信息中无“__os_type”字段且云硬盘状态为“available”时，设置的__os_type才会生效。 如果不传递该参数，则使用默认的“linux”值作为镜像的系统类型。

        :return: The os_type of this CinderExportToImageOption.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        """Sets the os_type of this CinderExportToImageOption.

        云硬盘导出镜像的系统类型。目前只支持“windows”和“linux”，默认值是“linux”。  说明： 只有云硬盘的volume_image_metadata信息中无“__os_type”字段且云硬盘状态为“available”时，设置的__os_type才会生效。 如果不传递该参数，则使用默认的“linux”值作为镜像的系统类型。

        :param os_type: The os_type of this CinderExportToImageOption.
        :type: str
        """
        self._os_type = os_type

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CinderExportToImageOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
