# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowLogConvergeConfigResponse(SdkResponse):

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
        'member_account_id': 'str',
        'member_project_id': 'str',
        'create_time': 'int',
        'update_time': 'int',
        'status': 'str',
        'organization_id': 'str',
        'management_account_id': 'str',
        'management_project_id': 'str',
        'version': 'str',
        'log_mapping_config': 'list[LogMappingConfig]'
    }

    attribute_map = {
        'id': 'id',
        'member_account_id': 'member_account_id',
        'member_project_id': 'member_project_id',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'status': 'status',
        'organization_id': 'organization_id',
        'management_account_id': 'management_account_id',
        'management_project_id': 'management_project_id',
        'version': 'version',
        'log_mapping_config': 'log_mapping_config'
    }

    def __init__(self, id=None, member_account_id=None, member_project_id=None, create_time=None, update_time=None, status=None, organization_id=None, management_account_id=None, management_project_id=None, version=None, log_mapping_config=None):
        """ShowLogConvergeConfigResponse

        The model defined in huaweicloud sdk

        :param id: ID
        :type id: str
        :param member_account_id: 组织成员账号id
        :type member_account_id: str
        :param member_project_id: 管理员或者委托管理员项目id
        :type member_project_id: str
        :param create_time: 创建时间
        :type create_time: int
        :param update_time: 更新时间
        :type update_time: int
        :param status: creating: 配置创建中   done：配置创建完成
        :type status: str
        :param organization_id: 组织id
        :type organization_id: str
        :param management_account_id: 管理员或者委托管理员账号id
        :type management_account_id: str
        :param management_project_id: 管理员项目id
        :type management_project_id: str
        :param version: 版本
        :type version: str
        :param log_mapping_config: 日志汇聚配置
        :type log_mapping_config: list[:class:`huaweicloudsdklts.v2.LogMappingConfig`]
        """
        
        super(ShowLogConvergeConfigResponse, self).__init__()

        self._id = None
        self._member_account_id = None
        self._member_project_id = None
        self._create_time = None
        self._update_time = None
        self._status = None
        self._organization_id = None
        self._management_account_id = None
        self._management_project_id = None
        self._version = None
        self._log_mapping_config = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if member_account_id is not None:
            self.member_account_id = member_account_id
        if member_project_id is not None:
            self.member_project_id = member_project_id
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if status is not None:
            self.status = status
        if organization_id is not None:
            self.organization_id = organization_id
        if management_account_id is not None:
            self.management_account_id = management_account_id
        if management_project_id is not None:
            self.management_project_id = management_project_id
        if version is not None:
            self.version = version
        if log_mapping_config is not None:
            self.log_mapping_config = log_mapping_config

    @property
    def id(self):
        """Gets the id of this ShowLogConvergeConfigResponse.

        ID

        :return: The id of this ShowLogConvergeConfigResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShowLogConvergeConfigResponse.

        ID

        :param id: The id of this ShowLogConvergeConfigResponse.
        :type id: str
        """
        self._id = id

    @property
    def member_account_id(self):
        """Gets the member_account_id of this ShowLogConvergeConfigResponse.

        组织成员账号id

        :return: The member_account_id of this ShowLogConvergeConfigResponse.
        :rtype: str
        """
        return self._member_account_id

    @member_account_id.setter
    def member_account_id(self, member_account_id):
        """Sets the member_account_id of this ShowLogConvergeConfigResponse.

        组织成员账号id

        :param member_account_id: The member_account_id of this ShowLogConvergeConfigResponse.
        :type member_account_id: str
        """
        self._member_account_id = member_account_id

    @property
    def member_project_id(self):
        """Gets the member_project_id of this ShowLogConvergeConfigResponse.

        管理员或者委托管理员项目id

        :return: The member_project_id of this ShowLogConvergeConfigResponse.
        :rtype: str
        """
        return self._member_project_id

    @member_project_id.setter
    def member_project_id(self, member_project_id):
        """Sets the member_project_id of this ShowLogConvergeConfigResponse.

        管理员或者委托管理员项目id

        :param member_project_id: The member_project_id of this ShowLogConvergeConfigResponse.
        :type member_project_id: str
        """
        self._member_project_id = member_project_id

    @property
    def create_time(self):
        """Gets the create_time of this ShowLogConvergeConfigResponse.

        创建时间

        :return: The create_time of this ShowLogConvergeConfigResponse.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ShowLogConvergeConfigResponse.

        创建时间

        :param create_time: The create_time of this ShowLogConvergeConfigResponse.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this ShowLogConvergeConfigResponse.

        更新时间

        :return: The update_time of this ShowLogConvergeConfigResponse.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this ShowLogConvergeConfigResponse.

        更新时间

        :param update_time: The update_time of this ShowLogConvergeConfigResponse.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def status(self):
        """Gets the status of this ShowLogConvergeConfigResponse.

        creating: 配置创建中   done：配置创建完成

        :return: The status of this ShowLogConvergeConfigResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShowLogConvergeConfigResponse.

        creating: 配置创建中   done：配置创建完成

        :param status: The status of this ShowLogConvergeConfigResponse.
        :type status: str
        """
        self._status = status

    @property
    def organization_id(self):
        """Gets the organization_id of this ShowLogConvergeConfigResponse.

        组织id

        :return: The organization_id of this ShowLogConvergeConfigResponse.
        :rtype: str
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """Sets the organization_id of this ShowLogConvergeConfigResponse.

        组织id

        :param organization_id: The organization_id of this ShowLogConvergeConfigResponse.
        :type organization_id: str
        """
        self._organization_id = organization_id

    @property
    def management_account_id(self):
        """Gets the management_account_id of this ShowLogConvergeConfigResponse.

        管理员或者委托管理员账号id

        :return: The management_account_id of this ShowLogConvergeConfigResponse.
        :rtype: str
        """
        return self._management_account_id

    @management_account_id.setter
    def management_account_id(self, management_account_id):
        """Sets the management_account_id of this ShowLogConvergeConfigResponse.

        管理员或者委托管理员账号id

        :param management_account_id: The management_account_id of this ShowLogConvergeConfigResponse.
        :type management_account_id: str
        """
        self._management_account_id = management_account_id

    @property
    def management_project_id(self):
        """Gets the management_project_id of this ShowLogConvergeConfigResponse.

        管理员项目id

        :return: The management_project_id of this ShowLogConvergeConfigResponse.
        :rtype: str
        """
        return self._management_project_id

    @management_project_id.setter
    def management_project_id(self, management_project_id):
        """Sets the management_project_id of this ShowLogConvergeConfigResponse.

        管理员项目id

        :param management_project_id: The management_project_id of this ShowLogConvergeConfigResponse.
        :type management_project_id: str
        """
        self._management_project_id = management_project_id

    @property
    def version(self):
        """Gets the version of this ShowLogConvergeConfigResponse.

        版本

        :return: The version of this ShowLogConvergeConfigResponse.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ShowLogConvergeConfigResponse.

        版本

        :param version: The version of this ShowLogConvergeConfigResponse.
        :type version: str
        """
        self._version = version

    @property
    def log_mapping_config(self):
        """Gets the log_mapping_config of this ShowLogConvergeConfigResponse.

        日志汇聚配置

        :return: The log_mapping_config of this ShowLogConvergeConfigResponse.
        :rtype: list[:class:`huaweicloudsdklts.v2.LogMappingConfig`]
        """
        return self._log_mapping_config

    @log_mapping_config.setter
    def log_mapping_config(self, log_mapping_config):
        """Sets the log_mapping_config of this ShowLogConvergeConfigResponse.

        日志汇聚配置

        :param log_mapping_config: The log_mapping_config of this ShowLogConvergeConfigResponse.
        :type log_mapping_config: list[:class:`huaweicloudsdklts.v2.LogMappingConfig`]
        """
        self._log_mapping_config = log_mapping_config

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
        if not isinstance(other, ShowLogConvergeConfigResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
