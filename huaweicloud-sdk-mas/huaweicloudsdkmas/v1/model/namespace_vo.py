# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NamespaceVo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'created_date': 'datetime',
        'data_sync_statistics': 'DataSyncStatistics',
        'datasource_statistics': 'DatasourceStatistics',
        'description': 'str',
        'enterprise_project_id': 'str',
        'id': 'str',
        'is_used': 'bool',
        'multi_active_zone': 'list[MultiActiveZoneVo]',
        'name': 'str',
        'project_id': 'str',
        'tenant_id': 'str',
        'type': 'int',
        'updated_date': 'datetime',
        'user_id': 'str'
    }

    attribute_map = {
        'created_date': 'created_date',
        'data_sync_statistics': 'data_sync_statistics',
        'datasource_statistics': 'datasource_statistics',
        'description': 'description',
        'enterprise_project_id': 'enterprise_project_id',
        'id': 'id',
        'is_used': 'is_used',
        'multi_active_zone': 'multi_active_zone',
        'name': 'name',
        'project_id': 'project_id',
        'tenant_id': 'tenant_id',
        'type': 'type',
        'updated_date': 'updated_date',
        'user_id': 'user_id'
    }

    def __init__(self, created_date=None, data_sync_statistics=None, datasource_statistics=None, description=None, enterprise_project_id=None, id=None, is_used=None, multi_active_zone=None, name=None, project_id=None, tenant_id=None, type=None, updated_date=None, user_id=None):
        r"""NamespaceVo

        The model defined in huaweicloud sdk

        :param created_date: 
        :type created_date: datetime
        :param data_sync_statistics: 
        :type data_sync_statistics: :class:`huaweicloudsdkmas.v1.DataSyncStatistics`
        :param datasource_statistics: 
        :type datasource_statistics: :class:`huaweicloudsdkmas.v1.DatasourceStatistics`
        :param description: 
        :type description: str
        :param enterprise_project_id: 
        :type enterprise_project_id: str
        :param id: 
        :type id: str
        :param is_used: 
        :type is_used: bool
        :param multi_active_zone: 
        :type multi_active_zone: list[:class:`huaweicloudsdkmas.v1.MultiActiveZoneVo`]
        :param name: 
        :type name: str
        :param project_id: 
        :type project_id: str
        :param tenant_id: 
        :type tenant_id: str
        :param type: 
        :type type: int
        :param updated_date: 
        :type updated_date: datetime
        :param user_id: 
        :type user_id: str
        """
        
        

        self._created_date = None
        self._data_sync_statistics = None
        self._datasource_statistics = None
        self._description = None
        self._enterprise_project_id = None
        self._id = None
        self._is_used = None
        self._multi_active_zone = None
        self._name = None
        self._project_id = None
        self._tenant_id = None
        self._type = None
        self._updated_date = None
        self._user_id = None
        self.discriminator = None

        if created_date is not None:
            self.created_date = created_date
        if data_sync_statistics is not None:
            self.data_sync_statistics = data_sync_statistics
        if datasource_statistics is not None:
            self.datasource_statistics = datasource_statistics
        if description is not None:
            self.description = description
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if id is not None:
            self.id = id
        if is_used is not None:
            self.is_used = is_used
        if multi_active_zone is not None:
            self.multi_active_zone = multi_active_zone
        if name is not None:
            self.name = name
        if project_id is not None:
            self.project_id = project_id
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if type is not None:
            self.type = type
        if updated_date is not None:
            self.updated_date = updated_date
        if user_id is not None:
            self.user_id = user_id

    @property
    def created_date(self):
        r"""Gets the created_date of this NamespaceVo.

        :return: The created_date of this NamespaceVo.
        :rtype: datetime
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        r"""Sets the created_date of this NamespaceVo.

        :param created_date: The created_date of this NamespaceVo.
        :type created_date: datetime
        """
        self._created_date = created_date

    @property
    def data_sync_statistics(self):
        r"""Gets the data_sync_statistics of this NamespaceVo.

        :return: The data_sync_statistics of this NamespaceVo.
        :rtype: :class:`huaweicloudsdkmas.v1.DataSyncStatistics`
        """
        return self._data_sync_statistics

    @data_sync_statistics.setter
    def data_sync_statistics(self, data_sync_statistics):
        r"""Sets the data_sync_statistics of this NamespaceVo.

        :param data_sync_statistics: The data_sync_statistics of this NamespaceVo.
        :type data_sync_statistics: :class:`huaweicloudsdkmas.v1.DataSyncStatistics`
        """
        self._data_sync_statistics = data_sync_statistics

    @property
    def datasource_statistics(self):
        r"""Gets the datasource_statistics of this NamespaceVo.

        :return: The datasource_statistics of this NamespaceVo.
        :rtype: :class:`huaweicloudsdkmas.v1.DatasourceStatistics`
        """
        return self._datasource_statistics

    @datasource_statistics.setter
    def datasource_statistics(self, datasource_statistics):
        r"""Sets the datasource_statistics of this NamespaceVo.

        :param datasource_statistics: The datasource_statistics of this NamespaceVo.
        :type datasource_statistics: :class:`huaweicloudsdkmas.v1.DatasourceStatistics`
        """
        self._datasource_statistics = datasource_statistics

    @property
    def description(self):
        r"""Gets the description of this NamespaceVo.

        :return: The description of this NamespaceVo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this NamespaceVo.

        :param description: The description of this NamespaceVo.
        :type description: str
        """
        self._description = description

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this NamespaceVo.

        :return: The enterprise_project_id of this NamespaceVo.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this NamespaceVo.

        :param enterprise_project_id: The enterprise_project_id of this NamespaceVo.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def id(self):
        r"""Gets the id of this NamespaceVo.

        :return: The id of this NamespaceVo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this NamespaceVo.

        :param id: The id of this NamespaceVo.
        :type id: str
        """
        self._id = id

    @property
    def is_used(self):
        r"""Gets the is_used of this NamespaceVo.

        :return: The is_used of this NamespaceVo.
        :rtype: bool
        """
        return self._is_used

    @is_used.setter
    def is_used(self, is_used):
        r"""Sets the is_used of this NamespaceVo.

        :param is_used: The is_used of this NamespaceVo.
        :type is_used: bool
        """
        self._is_used = is_used

    @property
    def multi_active_zone(self):
        r"""Gets the multi_active_zone of this NamespaceVo.

        :return: The multi_active_zone of this NamespaceVo.
        :rtype: list[:class:`huaweicloudsdkmas.v1.MultiActiveZoneVo`]
        """
        return self._multi_active_zone

    @multi_active_zone.setter
    def multi_active_zone(self, multi_active_zone):
        r"""Sets the multi_active_zone of this NamespaceVo.

        :param multi_active_zone: The multi_active_zone of this NamespaceVo.
        :type multi_active_zone: list[:class:`huaweicloudsdkmas.v1.MultiActiveZoneVo`]
        """
        self._multi_active_zone = multi_active_zone

    @property
    def name(self):
        r"""Gets the name of this NamespaceVo.

        :return: The name of this NamespaceVo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this NamespaceVo.

        :param name: The name of this NamespaceVo.
        :type name: str
        """
        self._name = name

    @property
    def project_id(self):
        r"""Gets the project_id of this NamespaceVo.

        :return: The project_id of this NamespaceVo.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this NamespaceVo.

        :param project_id: The project_id of this NamespaceVo.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def tenant_id(self):
        r"""Gets the tenant_id of this NamespaceVo.

        :return: The tenant_id of this NamespaceVo.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        r"""Sets the tenant_id of this NamespaceVo.

        :param tenant_id: The tenant_id of this NamespaceVo.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def type(self):
        r"""Gets the type of this NamespaceVo.

        :return: The type of this NamespaceVo.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this NamespaceVo.

        :param type: The type of this NamespaceVo.
        :type type: int
        """
        self._type = type

    @property
    def updated_date(self):
        r"""Gets the updated_date of this NamespaceVo.

        :return: The updated_date of this NamespaceVo.
        :rtype: datetime
        """
        return self._updated_date

    @updated_date.setter
    def updated_date(self, updated_date):
        r"""Sets the updated_date of this NamespaceVo.

        :param updated_date: The updated_date of this NamespaceVo.
        :type updated_date: datetime
        """
        self._updated_date = updated_date

    @property
    def user_id(self):
        r"""Gets the user_id of this NamespaceVo.

        :return: The user_id of this NamespaceVo.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this NamespaceVo.

        :param user_id: The user_id of this NamespaceVo.
        :type user_id: str
        """
        self._user_id = user_id

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
        if not isinstance(other, NamespaceVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
