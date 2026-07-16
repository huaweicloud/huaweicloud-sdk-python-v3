# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VolumeResponse:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'category': 'str',
        'mount_path': 'str',
        'url': 'str',
        'status': 'str',
        'mount_type': 'str'
    }

    attribute_map = {
        'category': 'category',
        'mount_path': 'mount_path',
        'url': 'url',
        'status': 'status',
        'mount_type': 'mount_type'
    }

    def __init__(self, category=None, mount_path=None, url=None, status=None, mount_type=None):
        r"""VolumeResponse

        The model defined in huaweicloud sdk

        :param category: **参数解释**：notebook返回的扩展存储类型 **参数约束**：不涉及 - OBS：对象存储服务 - OBSFS：并行文件存储 - EFS：弹性文件服务
        :type category: str
        :param mount_path: **参数解释**：存储挂载至Notebook实例的目录 **参数约束**：不涉及
        :type mount_path: str
        :param url: **参数解释**：当category为OBS、OBSFS时，挂载存储源路径。 **参数约束**：不涉及
        :type url: str
        :param status: **参数解释**：存储状态 - MOUNTING: 正在挂载中； - MOUNTED: 已挂载成功； - UNMOUNTING: 正在卸载中； - UNMOUNTED: 已卸载完成； - MOUNT_FAILED: 挂载失败 - UNMOUNT_FAILED：卸载失败； **参数约束**：不涉及
        :type status: str
        :param mount_type: **参数解释**：存储挂载类型，枚举类。 **约束限制**：无限制。 - STATIC:不支持在实例运行期间挂载以及卸载的存储 - DYNAMIC:支持在实例运行期间挂载以及卸载的存储
        :type mount_type: str
        """
        
        

        self._category = None
        self._mount_path = None
        self._url = None
        self._status = None
        self._mount_type = None
        self.discriminator = None

        if category is not None:
            self.category = category
        if mount_path is not None:
            self.mount_path = mount_path
        if url is not None:
            self.url = url
        if status is not None:
            self.status = status
        if mount_type is not None:
            self.mount_type = mount_type

    @property
    def category(self):
        r"""Gets the category of this VolumeResponse.

        **参数解释**：notebook返回的扩展存储类型 **参数约束**：不涉及 - OBS：对象存储服务 - OBSFS：并行文件存储 - EFS：弹性文件服务

        :return: The category of this VolumeResponse.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this VolumeResponse.

        **参数解释**：notebook返回的扩展存储类型 **参数约束**：不涉及 - OBS：对象存储服务 - OBSFS：并行文件存储 - EFS：弹性文件服务

        :param category: The category of this VolumeResponse.
        :type category: str
        """
        self._category = category

    @property
    def mount_path(self):
        r"""Gets the mount_path of this VolumeResponse.

        **参数解释**：存储挂载至Notebook实例的目录 **参数约束**：不涉及

        :return: The mount_path of this VolumeResponse.
        :rtype: str
        """
        return self._mount_path

    @mount_path.setter
    def mount_path(self, mount_path):
        r"""Sets the mount_path of this VolumeResponse.

        **参数解释**：存储挂载至Notebook实例的目录 **参数约束**：不涉及

        :param mount_path: The mount_path of this VolumeResponse.
        :type mount_path: str
        """
        self._mount_path = mount_path

    @property
    def url(self):
        r"""Gets the url of this VolumeResponse.

        **参数解释**：当category为OBS、OBSFS时，挂载存储源路径。 **参数约束**：不涉及

        :return: The url of this VolumeResponse.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this VolumeResponse.

        **参数解释**：当category为OBS、OBSFS时，挂载存储源路径。 **参数约束**：不涉及

        :param url: The url of this VolumeResponse.
        :type url: str
        """
        self._url = url

    @property
    def status(self):
        r"""Gets the status of this VolumeResponse.

        **参数解释**：存储状态 - MOUNTING: 正在挂载中； - MOUNTED: 已挂载成功； - UNMOUNTING: 正在卸载中； - UNMOUNTED: 已卸载完成； - MOUNT_FAILED: 挂载失败 - UNMOUNT_FAILED：卸载失败； **参数约束**：不涉及

        :return: The status of this VolumeResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this VolumeResponse.

        **参数解释**：存储状态 - MOUNTING: 正在挂载中； - MOUNTED: 已挂载成功； - UNMOUNTING: 正在卸载中； - UNMOUNTED: 已卸载完成； - MOUNT_FAILED: 挂载失败 - UNMOUNT_FAILED：卸载失败； **参数约束**：不涉及

        :param status: The status of this VolumeResponse.
        :type status: str
        """
        self._status = status

    @property
    def mount_type(self):
        r"""Gets the mount_type of this VolumeResponse.

        **参数解释**：存储挂载类型，枚举类。 **约束限制**：无限制。 - STATIC:不支持在实例运行期间挂载以及卸载的存储 - DYNAMIC:支持在实例运行期间挂载以及卸载的存储

        :return: The mount_type of this VolumeResponse.
        :rtype: str
        """
        return self._mount_type

    @mount_type.setter
    def mount_type(self, mount_type):
        r"""Sets the mount_type of this VolumeResponse.

        **参数解释**：存储挂载类型，枚举类。 **约束限制**：无限制。 - STATIC:不支持在实例运行期间挂载以及卸载的存储 - DYNAMIC:支持在实例运行期间挂载以及卸载的存储

        :param mount_type: The mount_type of this VolumeResponse.
        :type mount_type: str
        """
        self._mount_type = mount_type

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, VolumeResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
