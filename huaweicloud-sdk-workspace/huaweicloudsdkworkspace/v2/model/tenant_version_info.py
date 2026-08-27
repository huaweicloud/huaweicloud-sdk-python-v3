# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TenantVersionInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'version': 'str',
        'version_type': 'int',
        'os_type': 'int',
        'release_note': 'str',
        'custom_release_note': 'str',
        'version_download_url': 'str',
        'description': 'str',
        'version_status': 'str',
        'publish_time': 'str',
        'stop_time': 'str'
    }

    attribute_map = {
        'id': 'id',
        'version': 'version',
        'version_type': 'version_type',
        'os_type': 'os_type',
        'release_note': 'release_note',
        'custom_release_note': 'custom_release_note',
        'version_download_url': 'version_download_url',
        'description': 'description',
        'version_status': 'version_status',
        'publish_time': 'publish_time',
        'stop_time': 'stop_time'
    }

    def __init__(self, id=None, version=None, version_type=None, os_type=None, release_note=None, custom_release_note=None, version_download_url=None, description=None, version_status=None, publish_time=None, stop_time=None):
        r"""TenantVersionInfo

        The model defined in huaweicloud sdk

        :param id: 版本ID
        :type id: str
        :param version: 版本号
        :type version: str
        :param version_type: 版本类型：0-服务端 1-客户端
        :type version_type: int
        :param os_type: 操作系统类型：0-windows 1-android 2-mac 3-linux_UOS 4-linux_ubuntu 5-linux_Kylin 6-linux 7-linux_ubuntu_soft 8-linux_kylin_v10
        :type os_type: int
        :param release_note: 更新说明
        :type release_note: str
        :param custom_release_note: 租户自定义更新说明
        :type custom_release_note: str
        :param version_download_url: 版本下载地址
        :type version_download_url: str
        :param description: 描述
        :type description: str
        :param version_status: 版本状态：PREVIEW-预览 RELEASED-已发布 OFFLINE-已下线 OBSOLETE-已废弃
        :type version_status: str
        :param publish_time: 发布时间
        :type publish_time: str
        :param stop_time: 停止服务时间
        :type stop_time: str
        """
        
        

        self._id = None
        self._version = None
        self._version_type = None
        self._os_type = None
        self._release_note = None
        self._custom_release_note = None
        self._version_download_url = None
        self._description = None
        self._version_status = None
        self._publish_time = None
        self._stop_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if version is not None:
            self.version = version
        if version_type is not None:
            self.version_type = version_type
        if os_type is not None:
            self.os_type = os_type
        if release_note is not None:
            self.release_note = release_note
        if custom_release_note is not None:
            self.custom_release_note = custom_release_note
        if version_download_url is not None:
            self.version_download_url = version_download_url
        if description is not None:
            self.description = description
        if version_status is not None:
            self.version_status = version_status
        if publish_time is not None:
            self.publish_time = publish_time
        if stop_time is not None:
            self.stop_time = stop_time

    @property
    def id(self):
        r"""Gets the id of this TenantVersionInfo.

        版本ID

        :return: The id of this TenantVersionInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this TenantVersionInfo.

        版本ID

        :param id: The id of this TenantVersionInfo.
        :type id: str
        """
        self._id = id

    @property
    def version(self):
        r"""Gets the version of this TenantVersionInfo.

        版本号

        :return: The version of this TenantVersionInfo.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this TenantVersionInfo.

        版本号

        :param version: The version of this TenantVersionInfo.
        :type version: str
        """
        self._version = version

    @property
    def version_type(self):
        r"""Gets the version_type of this TenantVersionInfo.

        版本类型：0-服务端 1-客户端

        :return: The version_type of this TenantVersionInfo.
        :rtype: int
        """
        return self._version_type

    @version_type.setter
    def version_type(self, version_type):
        r"""Sets the version_type of this TenantVersionInfo.

        版本类型：0-服务端 1-客户端

        :param version_type: The version_type of this TenantVersionInfo.
        :type version_type: int
        """
        self._version_type = version_type

    @property
    def os_type(self):
        r"""Gets the os_type of this TenantVersionInfo.

        操作系统类型：0-windows 1-android 2-mac 3-linux_UOS 4-linux_ubuntu 5-linux_Kylin 6-linux 7-linux_ubuntu_soft 8-linux_kylin_v10

        :return: The os_type of this TenantVersionInfo.
        :rtype: int
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        r"""Sets the os_type of this TenantVersionInfo.

        操作系统类型：0-windows 1-android 2-mac 3-linux_UOS 4-linux_ubuntu 5-linux_Kylin 6-linux 7-linux_ubuntu_soft 8-linux_kylin_v10

        :param os_type: The os_type of this TenantVersionInfo.
        :type os_type: int
        """
        self._os_type = os_type

    @property
    def release_note(self):
        r"""Gets the release_note of this TenantVersionInfo.

        更新说明

        :return: The release_note of this TenantVersionInfo.
        :rtype: str
        """
        return self._release_note

    @release_note.setter
    def release_note(self, release_note):
        r"""Sets the release_note of this TenantVersionInfo.

        更新说明

        :param release_note: The release_note of this TenantVersionInfo.
        :type release_note: str
        """
        self._release_note = release_note

    @property
    def custom_release_note(self):
        r"""Gets the custom_release_note of this TenantVersionInfo.

        租户自定义更新说明

        :return: The custom_release_note of this TenantVersionInfo.
        :rtype: str
        """
        return self._custom_release_note

    @custom_release_note.setter
    def custom_release_note(self, custom_release_note):
        r"""Sets the custom_release_note of this TenantVersionInfo.

        租户自定义更新说明

        :param custom_release_note: The custom_release_note of this TenantVersionInfo.
        :type custom_release_note: str
        """
        self._custom_release_note = custom_release_note

    @property
    def version_download_url(self):
        r"""Gets the version_download_url of this TenantVersionInfo.

        版本下载地址

        :return: The version_download_url of this TenantVersionInfo.
        :rtype: str
        """
        return self._version_download_url

    @version_download_url.setter
    def version_download_url(self, version_download_url):
        r"""Sets the version_download_url of this TenantVersionInfo.

        版本下载地址

        :param version_download_url: The version_download_url of this TenantVersionInfo.
        :type version_download_url: str
        """
        self._version_download_url = version_download_url

    @property
    def description(self):
        r"""Gets the description of this TenantVersionInfo.

        描述

        :return: The description of this TenantVersionInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this TenantVersionInfo.

        描述

        :param description: The description of this TenantVersionInfo.
        :type description: str
        """
        self._description = description

    @property
    def version_status(self):
        r"""Gets the version_status of this TenantVersionInfo.

        版本状态：PREVIEW-预览 RELEASED-已发布 OFFLINE-已下线 OBSOLETE-已废弃

        :return: The version_status of this TenantVersionInfo.
        :rtype: str
        """
        return self._version_status

    @version_status.setter
    def version_status(self, version_status):
        r"""Sets the version_status of this TenantVersionInfo.

        版本状态：PREVIEW-预览 RELEASED-已发布 OFFLINE-已下线 OBSOLETE-已废弃

        :param version_status: The version_status of this TenantVersionInfo.
        :type version_status: str
        """
        self._version_status = version_status

    @property
    def publish_time(self):
        r"""Gets the publish_time of this TenantVersionInfo.

        发布时间

        :return: The publish_time of this TenantVersionInfo.
        :rtype: str
        """
        return self._publish_time

    @publish_time.setter
    def publish_time(self, publish_time):
        r"""Sets the publish_time of this TenantVersionInfo.

        发布时间

        :param publish_time: The publish_time of this TenantVersionInfo.
        :type publish_time: str
        """
        self._publish_time = publish_time

    @property
    def stop_time(self):
        r"""Gets the stop_time of this TenantVersionInfo.

        停止服务时间

        :return: The stop_time of this TenantVersionInfo.
        :rtype: str
        """
        return self._stop_time

    @stop_time.setter
    def stop_time(self, stop_time):
        r"""Sets the stop_time of this TenantVersionInfo.

        停止服务时间

        :param stop_time: The stop_time of this TenantVersionInfo.
        :type stop_time: str
        """
        self._stop_time = stop_time

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
        if not isinstance(other, TenantVersionInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
