# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTenantVersionConfigRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'version_type': 'int',
        'version': 'str',
        'os_type': 'int',
        'version_status': 'str',
        'publish_time_begin': 'str',
        'publish_time_end': 'str',
        'release_note': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'version_type': 'version_type',
        'version': 'version',
        'os_type': 'os_type',
        'version_status': 'version_status',
        'publish_time_begin': 'publish_time_begin',
        'publish_time_end': 'publish_time_end',
        'release_note': 'release_note',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, version_type=None, version=None, os_type=None, version_status=None, publish_time_begin=None, publish_time_end=None, release_note=None, offset=None, limit=None):
        r"""ListTenantVersionConfigRequest

        The model defined in huaweicloud sdk

        :param version_type: 版本类型：0-服务端 1-客户端（必传）
        :type version_type: int
        :param version: 版本号（支持模糊查询）
        :type version: str
        :param os_type: 操作系统类型：0-windows 1-android 2-mac 3-linux_UOS 4-linux_ubuntu 5-linux_Kylin 6-linux
        :type os_type: int
        :param version_status: 版本状态：PREVIEW-预览 RELEASED-已发布 OFFLINE-已下线 OBSOLETE-已废弃
        :type version_status: str
        :param publish_time_begin: 发布时间开始（格式：yyyy-MM-dd HH:mm:ss）
        :type publish_time_begin: str
        :param publish_time_end: 发布时间结束（格式：yyyy-MM-dd HH:mm:ss）
        :type publish_time_end: str
        :param release_note: 版本说明（支持模糊查询，会同时搜索SRE配置的版本说明和租户自定义的版本说明）
        :type release_note: str
        :param offset: 偏移量，默认0
        :type offset: int
        :param limit: 每页数量，默认10，最大20000
        :type limit: int
        """
        
        

        self._version_type = None
        self._version = None
        self._os_type = None
        self._version_status = None
        self._publish_time_begin = None
        self._publish_time_end = None
        self._release_note = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.version_type = version_type
        if version is not None:
            self.version = version
        if os_type is not None:
            self.os_type = os_type
        if version_status is not None:
            self.version_status = version_status
        if publish_time_begin is not None:
            self.publish_time_begin = publish_time_begin
        if publish_time_end is not None:
            self.publish_time_end = publish_time_end
        if release_note is not None:
            self.release_note = release_note
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def version_type(self):
        r"""Gets the version_type of this ListTenantVersionConfigRequest.

        版本类型：0-服务端 1-客户端（必传）

        :return: The version_type of this ListTenantVersionConfigRequest.
        :rtype: int
        """
        return self._version_type

    @version_type.setter
    def version_type(self, version_type):
        r"""Sets the version_type of this ListTenantVersionConfigRequest.

        版本类型：0-服务端 1-客户端（必传）

        :param version_type: The version_type of this ListTenantVersionConfigRequest.
        :type version_type: int
        """
        self._version_type = version_type

    @property
    def version(self):
        r"""Gets the version of this ListTenantVersionConfigRequest.

        版本号（支持模糊查询）

        :return: The version of this ListTenantVersionConfigRequest.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this ListTenantVersionConfigRequest.

        版本号（支持模糊查询）

        :param version: The version of this ListTenantVersionConfigRequest.
        :type version: str
        """
        self._version = version

    @property
    def os_type(self):
        r"""Gets the os_type of this ListTenantVersionConfigRequest.

        操作系统类型：0-windows 1-android 2-mac 3-linux_UOS 4-linux_ubuntu 5-linux_Kylin 6-linux

        :return: The os_type of this ListTenantVersionConfigRequest.
        :rtype: int
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        r"""Sets the os_type of this ListTenantVersionConfigRequest.

        操作系统类型：0-windows 1-android 2-mac 3-linux_UOS 4-linux_ubuntu 5-linux_Kylin 6-linux

        :param os_type: The os_type of this ListTenantVersionConfigRequest.
        :type os_type: int
        """
        self._os_type = os_type

    @property
    def version_status(self):
        r"""Gets the version_status of this ListTenantVersionConfigRequest.

        版本状态：PREVIEW-预览 RELEASED-已发布 OFFLINE-已下线 OBSOLETE-已废弃

        :return: The version_status of this ListTenantVersionConfigRequest.
        :rtype: str
        """
        return self._version_status

    @version_status.setter
    def version_status(self, version_status):
        r"""Sets the version_status of this ListTenantVersionConfigRequest.

        版本状态：PREVIEW-预览 RELEASED-已发布 OFFLINE-已下线 OBSOLETE-已废弃

        :param version_status: The version_status of this ListTenantVersionConfigRequest.
        :type version_status: str
        """
        self._version_status = version_status

    @property
    def publish_time_begin(self):
        r"""Gets the publish_time_begin of this ListTenantVersionConfigRequest.

        发布时间开始（格式：yyyy-MM-dd HH:mm:ss）

        :return: The publish_time_begin of this ListTenantVersionConfigRequest.
        :rtype: str
        """
        return self._publish_time_begin

    @publish_time_begin.setter
    def publish_time_begin(self, publish_time_begin):
        r"""Sets the publish_time_begin of this ListTenantVersionConfigRequest.

        发布时间开始（格式：yyyy-MM-dd HH:mm:ss）

        :param publish_time_begin: The publish_time_begin of this ListTenantVersionConfigRequest.
        :type publish_time_begin: str
        """
        self._publish_time_begin = publish_time_begin

    @property
    def publish_time_end(self):
        r"""Gets the publish_time_end of this ListTenantVersionConfigRequest.

        发布时间结束（格式：yyyy-MM-dd HH:mm:ss）

        :return: The publish_time_end of this ListTenantVersionConfigRequest.
        :rtype: str
        """
        return self._publish_time_end

    @publish_time_end.setter
    def publish_time_end(self, publish_time_end):
        r"""Sets the publish_time_end of this ListTenantVersionConfigRequest.

        发布时间结束（格式：yyyy-MM-dd HH:mm:ss）

        :param publish_time_end: The publish_time_end of this ListTenantVersionConfigRequest.
        :type publish_time_end: str
        """
        self._publish_time_end = publish_time_end

    @property
    def release_note(self):
        r"""Gets the release_note of this ListTenantVersionConfigRequest.

        版本说明（支持模糊查询，会同时搜索SRE配置的版本说明和租户自定义的版本说明）

        :return: The release_note of this ListTenantVersionConfigRequest.
        :rtype: str
        """
        return self._release_note

    @release_note.setter
    def release_note(self, release_note):
        r"""Sets the release_note of this ListTenantVersionConfigRequest.

        版本说明（支持模糊查询，会同时搜索SRE配置的版本说明和租户自定义的版本说明）

        :param release_note: The release_note of this ListTenantVersionConfigRequest.
        :type release_note: str
        """
        self._release_note = release_note

    @property
    def offset(self):
        r"""Gets the offset of this ListTenantVersionConfigRequest.

        偏移量，默认0

        :return: The offset of this ListTenantVersionConfigRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListTenantVersionConfigRequest.

        偏移量，默认0

        :param offset: The offset of this ListTenantVersionConfigRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListTenantVersionConfigRequest.

        每页数量，默认10，最大20000

        :return: The limit of this ListTenantVersionConfigRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListTenantVersionConfigRequest.

        每页数量，默认10，最大20000

        :param limit: The limit of this ListTenantVersionConfigRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListTenantVersionConfigRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
