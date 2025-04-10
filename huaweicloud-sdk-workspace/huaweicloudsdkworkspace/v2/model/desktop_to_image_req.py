# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DesktopToImageReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'image_name': 'str',
        'image_description': 'str',
        'desktop_id': 'str',
        'execute_sysprep': 'bool',
        'image_tags': 'list[TagKeyValue]',
        'enterprise_project_id': 'str',
        'max_ram': 'str',
        'min_ram': 'str'
    }

    attribute_map = {
        'image_name': 'image_name',
        'image_description': 'image_description',
        'desktop_id': 'desktop_id',
        'execute_sysprep': 'execute_sysprep',
        'image_tags': 'image_tags',
        'enterprise_project_id': 'enterprise_project_id',
        'max_ram': 'max_ram',
        'min_ram': 'min_ram'
    }

    def __init__(self, image_name=None, image_description=None, desktop_id=None, execute_sysprep=None, image_tags=None, enterprise_project_id=None, max_ram=None, min_ram=None):
        r"""DesktopToImageReq

        The model defined in huaweicloud sdk

        :param image_name: 镜像名称。
        :type image_name: str
        :param image_description: 镜像描述信息。
        :type image_description: str
        :param desktop_id: 用于制作镜像的云桌面的InstanceID。
        :type desktop_id: str
        :param execute_sysprep: 是否执行系统封装步骤。
        :type execute_sysprep: bool
        :param image_tags: 镜像标签列表。
        :type image_tags: list[:class:`huaweicloudsdkworkspace.v2.TagKeyValue`]
        :param enterprise_project_id: 表示当前镜像所属的企业项目。取值为0或无该值，表示属于default企业项目。取值为UUID，表示属于该UUID对应的企业项目。
        :type enterprise_project_id: str
        :param max_ram: 表示镜像支持的最大内存，单位为MB。
        :type max_ram: str
        :param min_ram: 表示镜像支持的最小内存，单位为MB，默认为0，表示不受限制。
        :type min_ram: str
        """
        
        

        self._image_name = None
        self._image_description = None
        self._desktop_id = None
        self._execute_sysprep = None
        self._image_tags = None
        self._enterprise_project_id = None
        self._max_ram = None
        self._min_ram = None
        self.discriminator = None

        self.image_name = image_name
        if image_description is not None:
            self.image_description = image_description
        self.desktop_id = desktop_id
        if execute_sysprep is not None:
            self.execute_sysprep = execute_sysprep
        if image_tags is not None:
            self.image_tags = image_tags
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if max_ram is not None:
            self.max_ram = max_ram
        if min_ram is not None:
            self.min_ram = min_ram

    @property
    def image_name(self):
        r"""Gets the image_name of this DesktopToImageReq.

        镜像名称。

        :return: The image_name of this DesktopToImageReq.
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        r"""Sets the image_name of this DesktopToImageReq.

        镜像名称。

        :param image_name: The image_name of this DesktopToImageReq.
        :type image_name: str
        """
        self._image_name = image_name

    @property
    def image_description(self):
        r"""Gets the image_description of this DesktopToImageReq.

        镜像描述信息。

        :return: The image_description of this DesktopToImageReq.
        :rtype: str
        """
        return self._image_description

    @image_description.setter
    def image_description(self, image_description):
        r"""Sets the image_description of this DesktopToImageReq.

        镜像描述信息。

        :param image_description: The image_description of this DesktopToImageReq.
        :type image_description: str
        """
        self._image_description = image_description

    @property
    def desktop_id(self):
        r"""Gets the desktop_id of this DesktopToImageReq.

        用于制作镜像的云桌面的InstanceID。

        :return: The desktop_id of this DesktopToImageReq.
        :rtype: str
        """
        return self._desktop_id

    @desktop_id.setter
    def desktop_id(self, desktop_id):
        r"""Sets the desktop_id of this DesktopToImageReq.

        用于制作镜像的云桌面的InstanceID。

        :param desktop_id: The desktop_id of this DesktopToImageReq.
        :type desktop_id: str
        """
        self._desktop_id = desktop_id

    @property
    def execute_sysprep(self):
        r"""Gets the execute_sysprep of this DesktopToImageReq.

        是否执行系统封装步骤。

        :return: The execute_sysprep of this DesktopToImageReq.
        :rtype: bool
        """
        return self._execute_sysprep

    @execute_sysprep.setter
    def execute_sysprep(self, execute_sysprep):
        r"""Sets the execute_sysprep of this DesktopToImageReq.

        是否执行系统封装步骤。

        :param execute_sysprep: The execute_sysprep of this DesktopToImageReq.
        :type execute_sysprep: bool
        """
        self._execute_sysprep = execute_sysprep

    @property
    def image_tags(self):
        r"""Gets the image_tags of this DesktopToImageReq.

        镜像标签列表。

        :return: The image_tags of this DesktopToImageReq.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.TagKeyValue`]
        """
        return self._image_tags

    @image_tags.setter
    def image_tags(self, image_tags):
        r"""Sets the image_tags of this DesktopToImageReq.

        镜像标签列表。

        :param image_tags: The image_tags of this DesktopToImageReq.
        :type image_tags: list[:class:`huaweicloudsdkworkspace.v2.TagKeyValue`]
        """
        self._image_tags = image_tags

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this DesktopToImageReq.

        表示当前镜像所属的企业项目。取值为0或无该值，表示属于default企业项目。取值为UUID，表示属于该UUID对应的企业项目。

        :return: The enterprise_project_id of this DesktopToImageReq.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this DesktopToImageReq.

        表示当前镜像所属的企业项目。取值为0或无该值，表示属于default企业项目。取值为UUID，表示属于该UUID对应的企业项目。

        :param enterprise_project_id: The enterprise_project_id of this DesktopToImageReq.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def max_ram(self):
        r"""Gets the max_ram of this DesktopToImageReq.

        表示镜像支持的最大内存，单位为MB。

        :return: The max_ram of this DesktopToImageReq.
        :rtype: str
        """
        return self._max_ram

    @max_ram.setter
    def max_ram(self, max_ram):
        r"""Sets the max_ram of this DesktopToImageReq.

        表示镜像支持的最大内存，单位为MB。

        :param max_ram: The max_ram of this DesktopToImageReq.
        :type max_ram: str
        """
        self._max_ram = max_ram

    @property
    def min_ram(self):
        r"""Gets the min_ram of this DesktopToImageReq.

        表示镜像支持的最小内存，单位为MB，默认为0，表示不受限制。

        :return: The min_ram of this DesktopToImageReq.
        :rtype: str
        """
        return self._min_ram

    @min_ram.setter
    def min_ram(self, min_ram):
        r"""Sets the min_ram of this DesktopToImageReq.

        表示镜像支持的最小内存，单位为MB，默认为0，表示不受限制。

        :param min_ram: The min_ram of this DesktopToImageReq.
        :type min_ram: str
        """
        self._min_ram = min_ram

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
        if not isinstance(other, DesktopToImageReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
