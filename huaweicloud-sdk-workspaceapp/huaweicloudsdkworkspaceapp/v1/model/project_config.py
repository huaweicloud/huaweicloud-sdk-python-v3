# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProjectConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_config_id': 'str',
        'project_config_name': 'str',
        'storage_quota': 'int',
        'is_relevance': 'bool',
        'create_time': 'datetime'
    }

    attribute_map = {
        'project_config_id': 'project_config_id',
        'project_config_name': 'project_config_name',
        'storage_quota': 'storage_quota',
        'is_relevance': 'is_relevance',
        'create_time': 'create_time'
    }

    def __init__(self, project_config_id=None, project_config_name=None, storage_quota=None, is_relevance=None, create_time=None):
        r"""ProjectConfig

        The model defined in huaweicloud sdk

        :param project_config_id: 项目配置名称。
        :type project_config_id: str
        :param project_config_name: 项目名称。
        :type project_config_name: str
        :param storage_quota: 存储配额。
        :type storage_quota: int
        :param is_relevance: 是否已经关联
        :type is_relevance: bool
        :param create_time: 创建时间。
        :type create_time: datetime
        """
        
        

        self._project_config_id = None
        self._project_config_name = None
        self._storage_quota = None
        self._is_relevance = None
        self._create_time = None
        self.discriminator = None

        if project_config_id is not None:
            self.project_config_id = project_config_id
        if project_config_name is not None:
            self.project_config_name = project_config_name
        if storage_quota is not None:
            self.storage_quota = storage_quota
        if is_relevance is not None:
            self.is_relevance = is_relevance
        if create_time is not None:
            self.create_time = create_time

    @property
    def project_config_id(self):
        r"""Gets the project_config_id of this ProjectConfig.

        项目配置名称。

        :return: The project_config_id of this ProjectConfig.
        :rtype: str
        """
        return self._project_config_id

    @project_config_id.setter
    def project_config_id(self, project_config_id):
        r"""Sets the project_config_id of this ProjectConfig.

        项目配置名称。

        :param project_config_id: The project_config_id of this ProjectConfig.
        :type project_config_id: str
        """
        self._project_config_id = project_config_id

    @property
    def project_config_name(self):
        r"""Gets the project_config_name of this ProjectConfig.

        项目名称。

        :return: The project_config_name of this ProjectConfig.
        :rtype: str
        """
        return self._project_config_name

    @project_config_name.setter
    def project_config_name(self, project_config_name):
        r"""Sets the project_config_name of this ProjectConfig.

        项目名称。

        :param project_config_name: The project_config_name of this ProjectConfig.
        :type project_config_name: str
        """
        self._project_config_name = project_config_name

    @property
    def storage_quota(self):
        r"""Gets the storage_quota of this ProjectConfig.

        存储配额。

        :return: The storage_quota of this ProjectConfig.
        :rtype: int
        """
        return self._storage_quota

    @storage_quota.setter
    def storage_quota(self, storage_quota):
        r"""Sets the storage_quota of this ProjectConfig.

        存储配额。

        :param storage_quota: The storage_quota of this ProjectConfig.
        :type storage_quota: int
        """
        self._storage_quota = storage_quota

    @property
    def is_relevance(self):
        r"""Gets the is_relevance of this ProjectConfig.

        是否已经关联

        :return: The is_relevance of this ProjectConfig.
        :rtype: bool
        """
        return self._is_relevance

    @is_relevance.setter
    def is_relevance(self, is_relevance):
        r"""Sets the is_relevance of this ProjectConfig.

        是否已经关联

        :param is_relevance: The is_relevance of this ProjectConfig.
        :type is_relevance: bool
        """
        self._is_relevance = is_relevance

    @property
    def create_time(self):
        r"""Gets the create_time of this ProjectConfig.

        创建时间。

        :return: The create_time of this ProjectConfig.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ProjectConfig.

        创建时间。

        :param create_time: The create_time of this ProjectConfig.
        :type create_time: datetime
        """
        self._create_time = create_time

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
        if not isinstance(other, ProjectConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
