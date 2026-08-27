# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTenantVersionConfigResponse(SdkResponse):

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
        'project_id': 'str',
        'version_config_id': 'str',
        'custom_release_note': 'str',
        'release_note': 'str',
        'version_download_url': 'str',
        'created_at': 'str',
        'updated_at': 'str'
    }

    attribute_map = {
        'id': 'id',
        'project_id': 'project_id',
        'version_config_id': 'version_config_id',
        'custom_release_note': 'custom_release_note',
        'release_note': 'release_note',
        'version_download_url': 'version_download_url',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, id=None, project_id=None, version_config_id=None, custom_release_note=None, release_note=None, version_download_url=None, created_at=None, updated_at=None):
        r"""ShowTenantVersionConfigResponse

        The model defined in huaweicloud sdk

        :param id: 租户版本配置ID
        :type id: str
        :param project_id: 项目ID
        :type project_id: str
        :param version_config_id: 关联版本配置表ID
        :type version_config_id: str
        :param custom_release_note: 自定义版本说明
        :type custom_release_note: str
        :param release_note: 更新说明
        :type release_note: str
        :param version_download_url: 版本下载地址
        :type version_download_url: str
        :param created_at: 创建时间
        :type created_at: str
        :param updated_at: 更新时间
        :type updated_at: str
        """
        
        super().__init__()

        self._id = None
        self._project_id = None
        self._version_config_id = None
        self._custom_release_note = None
        self._release_note = None
        self._version_download_url = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if project_id is not None:
            self.project_id = project_id
        if version_config_id is not None:
            self.version_config_id = version_config_id
        if custom_release_note is not None:
            self.custom_release_note = custom_release_note
        if release_note is not None:
            self.release_note = release_note
        if version_download_url is not None:
            self.version_download_url = version_download_url
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def id(self):
        r"""Gets the id of this ShowTenantVersionConfigResponse.

        租户版本配置ID

        :return: The id of this ShowTenantVersionConfigResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowTenantVersionConfigResponse.

        租户版本配置ID

        :param id: The id of this ShowTenantVersionConfigResponse.
        :type id: str
        """
        self._id = id

    @property
    def project_id(self):
        r"""Gets the project_id of this ShowTenantVersionConfigResponse.

        项目ID

        :return: The project_id of this ShowTenantVersionConfigResponse.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ShowTenantVersionConfigResponse.

        项目ID

        :param project_id: The project_id of this ShowTenantVersionConfigResponse.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def version_config_id(self):
        r"""Gets the version_config_id of this ShowTenantVersionConfigResponse.

        关联版本配置表ID

        :return: The version_config_id of this ShowTenantVersionConfigResponse.
        :rtype: str
        """
        return self._version_config_id

    @version_config_id.setter
    def version_config_id(self, version_config_id):
        r"""Sets the version_config_id of this ShowTenantVersionConfigResponse.

        关联版本配置表ID

        :param version_config_id: The version_config_id of this ShowTenantVersionConfigResponse.
        :type version_config_id: str
        """
        self._version_config_id = version_config_id

    @property
    def custom_release_note(self):
        r"""Gets the custom_release_note of this ShowTenantVersionConfigResponse.

        自定义版本说明

        :return: The custom_release_note of this ShowTenantVersionConfigResponse.
        :rtype: str
        """
        return self._custom_release_note

    @custom_release_note.setter
    def custom_release_note(self, custom_release_note):
        r"""Sets the custom_release_note of this ShowTenantVersionConfigResponse.

        自定义版本说明

        :param custom_release_note: The custom_release_note of this ShowTenantVersionConfigResponse.
        :type custom_release_note: str
        """
        self._custom_release_note = custom_release_note

    @property
    def release_note(self):
        r"""Gets the release_note of this ShowTenantVersionConfigResponse.

        更新说明

        :return: The release_note of this ShowTenantVersionConfigResponse.
        :rtype: str
        """
        return self._release_note

    @release_note.setter
    def release_note(self, release_note):
        r"""Sets the release_note of this ShowTenantVersionConfigResponse.

        更新说明

        :param release_note: The release_note of this ShowTenantVersionConfigResponse.
        :type release_note: str
        """
        self._release_note = release_note

    @property
    def version_download_url(self):
        r"""Gets the version_download_url of this ShowTenantVersionConfigResponse.

        版本下载地址

        :return: The version_download_url of this ShowTenantVersionConfigResponse.
        :rtype: str
        """
        return self._version_download_url

    @version_download_url.setter
    def version_download_url(self, version_download_url):
        r"""Sets the version_download_url of this ShowTenantVersionConfigResponse.

        版本下载地址

        :param version_download_url: The version_download_url of this ShowTenantVersionConfigResponse.
        :type version_download_url: str
        """
        self._version_download_url = version_download_url

    @property
    def created_at(self):
        r"""Gets the created_at of this ShowTenantVersionConfigResponse.

        创建时间

        :return: The created_at of this ShowTenantVersionConfigResponse.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this ShowTenantVersionConfigResponse.

        创建时间

        :param created_at: The created_at of this ShowTenantVersionConfigResponse.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this ShowTenantVersionConfigResponse.

        更新时间

        :return: The updated_at of this ShowTenantVersionConfigResponse.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this ShowTenantVersionConfigResponse.

        更新时间

        :param updated_at: The updated_at of this ShowTenantVersionConfigResponse.
        :type updated_at: str
        """
        self._updated_at = updated_at

    def to_dict(self):
        import warnings
        warnings.warn("ShowTenantVersionConfigResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ShowTenantVersionConfigResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
