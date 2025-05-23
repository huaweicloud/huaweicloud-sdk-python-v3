# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAppsResponseBodyResult:

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
        'mark_for_delete': 'int',
        'create_by': 'str',
        'create_time': 'int',
        'update_by': 'str',
        'update_time': 'int',
        'name_cn': 'str',
        'name_en': 'str',
        'desc_cn': 'str',
        'desc_en': 'str',
        'database_type': 'str',
        'environment': 'str',
        'owners': 'list[str]',
        'app_type': 'str',
        'permission_control': 'str'
    }

    attribute_map = {
        'id': 'id',
        'project_id': 'project_id',
        'mark_for_delete': 'mark_for_delete',
        'create_by': 'create_by',
        'create_time': 'create_time',
        'update_by': 'update_by',
        'update_time': 'update_time',
        'name_cn': 'name_cn',
        'name_en': 'name_en',
        'desc_cn': 'desc_cn',
        'desc_en': 'desc_en',
        'database_type': 'database_type',
        'environment': 'environment',
        'owners': 'owners',
        'app_type': 'app_type',
        'permission_control': 'permission_control'
    }

    def __init__(self, id=None, project_id=None, mark_for_delete=None, create_by=None, create_time=None, update_by=None, update_time=None, name_cn=None, name_en=None, desc_cn=None, desc_en=None, database_type=None, environment=None, owners=None, app_type=None, permission_control=None):
        r"""ListAppsResponseBodyResult

        The model defined in huaweicloud sdk

        :param id: 应用ID。
        :type id: str
        :param project_id: 项目ID。
        :type project_id: str
        :param mark_for_delete: 删除标记。 - 0：未删除 - 1：删除
        :type mark_for_delete: int
        :param create_by: 创建人。
        :type create_by: str
        :param create_time: 创建时间。
        :type create_time: int
        :param update_by: 更新人。
        :type update_by: str
        :param update_time: 更新时间。
        :type update_time: int
        :param name_cn: 应用的中文名称。
        :type name_cn: str
        :param name_en: 应用的英文名称。
        :type name_en: str
        :param desc_cn: 应用的中文描述。
        :type desc_cn: str
        :param desc_en: 应用的英文描述。
        :type desc_en: str
        :param database_type: 应用的数据库类型。
        :type database_type: str
        :param environment: 运行服务的环境标识。
        :type environment: str
        :param owners: 应用责任人。
        :type owners: list[str]
        :param app_type: App类型。
        :type app_type: str
        :param permission_control: App权限控制。
        :type permission_control: str
        """
        
        

        self._id = None
        self._project_id = None
        self._mark_for_delete = None
        self._create_by = None
        self._create_time = None
        self._update_by = None
        self._update_time = None
        self._name_cn = None
        self._name_en = None
        self._desc_cn = None
        self._desc_en = None
        self._database_type = None
        self._environment = None
        self._owners = None
        self._app_type = None
        self._permission_control = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if project_id is not None:
            self.project_id = project_id
        if mark_for_delete is not None:
            self.mark_for_delete = mark_for_delete
        if create_by is not None:
            self.create_by = create_by
        if create_time is not None:
            self.create_time = create_time
        if update_by is not None:
            self.update_by = update_by
        if update_time is not None:
            self.update_time = update_time
        if name_cn is not None:
            self.name_cn = name_cn
        if name_en is not None:
            self.name_en = name_en
        if desc_cn is not None:
            self.desc_cn = desc_cn
        if desc_en is not None:
            self.desc_en = desc_en
        if database_type is not None:
            self.database_type = database_type
        if environment is not None:
            self.environment = environment
        if owners is not None:
            self.owners = owners
        if app_type is not None:
            self.app_type = app_type
        if permission_control is not None:
            self.permission_control = permission_control

    @property
    def id(self):
        r"""Gets the id of this ListAppsResponseBodyResult.

        应用ID。

        :return: The id of this ListAppsResponseBodyResult.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListAppsResponseBodyResult.

        应用ID。

        :param id: The id of this ListAppsResponseBodyResult.
        :type id: str
        """
        self._id = id

    @property
    def project_id(self):
        r"""Gets the project_id of this ListAppsResponseBodyResult.

        项目ID。

        :return: The project_id of this ListAppsResponseBodyResult.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ListAppsResponseBodyResult.

        项目ID。

        :param project_id: The project_id of this ListAppsResponseBodyResult.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def mark_for_delete(self):
        r"""Gets the mark_for_delete of this ListAppsResponseBodyResult.

        删除标记。 - 0：未删除 - 1：删除

        :return: The mark_for_delete of this ListAppsResponseBodyResult.
        :rtype: int
        """
        return self._mark_for_delete

    @mark_for_delete.setter
    def mark_for_delete(self, mark_for_delete):
        r"""Sets the mark_for_delete of this ListAppsResponseBodyResult.

        删除标记。 - 0：未删除 - 1：删除

        :param mark_for_delete: The mark_for_delete of this ListAppsResponseBodyResult.
        :type mark_for_delete: int
        """
        self._mark_for_delete = mark_for_delete

    @property
    def create_by(self):
        r"""Gets the create_by of this ListAppsResponseBodyResult.

        创建人。

        :return: The create_by of this ListAppsResponseBodyResult.
        :rtype: str
        """
        return self._create_by

    @create_by.setter
    def create_by(self, create_by):
        r"""Sets the create_by of this ListAppsResponseBodyResult.

        创建人。

        :param create_by: The create_by of this ListAppsResponseBodyResult.
        :type create_by: str
        """
        self._create_by = create_by

    @property
    def create_time(self):
        r"""Gets the create_time of this ListAppsResponseBodyResult.

        创建时间。

        :return: The create_time of this ListAppsResponseBodyResult.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ListAppsResponseBodyResult.

        创建时间。

        :param create_time: The create_time of this ListAppsResponseBodyResult.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def update_by(self):
        r"""Gets the update_by of this ListAppsResponseBodyResult.

        更新人。

        :return: The update_by of this ListAppsResponseBodyResult.
        :rtype: str
        """
        return self._update_by

    @update_by.setter
    def update_by(self, update_by):
        r"""Sets the update_by of this ListAppsResponseBodyResult.

        更新人。

        :param update_by: The update_by of this ListAppsResponseBodyResult.
        :type update_by: str
        """
        self._update_by = update_by

    @property
    def update_time(self):
        r"""Gets the update_time of this ListAppsResponseBodyResult.

        更新时间。

        :return: The update_time of this ListAppsResponseBodyResult.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this ListAppsResponseBodyResult.

        更新时间。

        :param update_time: The update_time of this ListAppsResponseBodyResult.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def name_cn(self):
        r"""Gets the name_cn of this ListAppsResponseBodyResult.

        应用的中文名称。

        :return: The name_cn of this ListAppsResponseBodyResult.
        :rtype: str
        """
        return self._name_cn

    @name_cn.setter
    def name_cn(self, name_cn):
        r"""Sets the name_cn of this ListAppsResponseBodyResult.

        应用的中文名称。

        :param name_cn: The name_cn of this ListAppsResponseBodyResult.
        :type name_cn: str
        """
        self._name_cn = name_cn

    @property
    def name_en(self):
        r"""Gets the name_en of this ListAppsResponseBodyResult.

        应用的英文名称。

        :return: The name_en of this ListAppsResponseBodyResult.
        :rtype: str
        """
        return self._name_en

    @name_en.setter
    def name_en(self, name_en):
        r"""Sets the name_en of this ListAppsResponseBodyResult.

        应用的英文名称。

        :param name_en: The name_en of this ListAppsResponseBodyResult.
        :type name_en: str
        """
        self._name_en = name_en

    @property
    def desc_cn(self):
        r"""Gets the desc_cn of this ListAppsResponseBodyResult.

        应用的中文描述。

        :return: The desc_cn of this ListAppsResponseBodyResult.
        :rtype: str
        """
        return self._desc_cn

    @desc_cn.setter
    def desc_cn(self, desc_cn):
        r"""Sets the desc_cn of this ListAppsResponseBodyResult.

        应用的中文描述。

        :param desc_cn: The desc_cn of this ListAppsResponseBodyResult.
        :type desc_cn: str
        """
        self._desc_cn = desc_cn

    @property
    def desc_en(self):
        r"""Gets the desc_en of this ListAppsResponseBodyResult.

        应用的英文描述。

        :return: The desc_en of this ListAppsResponseBodyResult.
        :rtype: str
        """
        return self._desc_en

    @desc_en.setter
    def desc_en(self, desc_en):
        r"""Sets the desc_en of this ListAppsResponseBodyResult.

        应用的英文描述。

        :param desc_en: The desc_en of this ListAppsResponseBodyResult.
        :type desc_en: str
        """
        self._desc_en = desc_en

    @property
    def database_type(self):
        r"""Gets the database_type of this ListAppsResponseBodyResult.

        应用的数据库类型。

        :return: The database_type of this ListAppsResponseBodyResult.
        :rtype: str
        """
        return self._database_type

    @database_type.setter
    def database_type(self, database_type):
        r"""Sets the database_type of this ListAppsResponseBodyResult.

        应用的数据库类型。

        :param database_type: The database_type of this ListAppsResponseBodyResult.
        :type database_type: str
        """
        self._database_type = database_type

    @property
    def environment(self):
        r"""Gets the environment of this ListAppsResponseBodyResult.

        运行服务的环境标识。

        :return: The environment of this ListAppsResponseBodyResult.
        :rtype: str
        """
        return self._environment

    @environment.setter
    def environment(self, environment):
        r"""Sets the environment of this ListAppsResponseBodyResult.

        运行服务的环境标识。

        :param environment: The environment of this ListAppsResponseBodyResult.
        :type environment: str
        """
        self._environment = environment

    @property
    def owners(self):
        r"""Gets the owners of this ListAppsResponseBodyResult.

        应用责任人。

        :return: The owners of this ListAppsResponseBodyResult.
        :rtype: list[str]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        r"""Sets the owners of this ListAppsResponseBodyResult.

        应用责任人。

        :param owners: The owners of this ListAppsResponseBodyResult.
        :type owners: list[str]
        """
        self._owners = owners

    @property
    def app_type(self):
        r"""Gets the app_type of this ListAppsResponseBodyResult.

        App类型。

        :return: The app_type of this ListAppsResponseBodyResult.
        :rtype: str
        """
        return self._app_type

    @app_type.setter
    def app_type(self, app_type):
        r"""Sets the app_type of this ListAppsResponseBodyResult.

        App类型。

        :param app_type: The app_type of this ListAppsResponseBodyResult.
        :type app_type: str
        """
        self._app_type = app_type

    @property
    def permission_control(self):
        r"""Gets the permission_control of this ListAppsResponseBodyResult.

        App权限控制。

        :return: The permission_control of this ListAppsResponseBodyResult.
        :rtype: str
        """
        return self._permission_control

    @permission_control.setter
    def permission_control(self, permission_control):
        r"""Sets the permission_control of this ListAppsResponseBodyResult.

        App权限控制。

        :param permission_control: The permission_control of this ListAppsResponseBodyResult.
        :type permission_control: str
        """
        self._permission_control = permission_control

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
        if not isinstance(other, ListAppsResponseBodyResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
