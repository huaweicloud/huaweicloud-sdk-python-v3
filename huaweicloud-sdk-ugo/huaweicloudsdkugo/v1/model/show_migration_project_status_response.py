# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowMigrationProjectStatusResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'migration_project_id': 'int',
        'migration_project_name': 'str',
        'evaluation_project_id': 'int',
        'evaluation_project_name': 'str',
        'migration_project_status': 'str',
        'permission_check_status': 'str',
        'resource_id': 'str',
        'created_time': 'str',
        'updated_time': 'str'
    }

    attribute_map = {
        'migration_project_id': 'migration_project_id',
        'migration_project_name': 'migration_project_name',
        'evaluation_project_id': 'evaluation_project_id',
        'evaluation_project_name': 'evaluation_project_name',
        'migration_project_status': 'migration_project_status',
        'permission_check_status': 'permission_check_status',
        'resource_id': 'resource_id',
        'created_time': 'created_time',
        'updated_time': 'updated_time'
    }

    def __init__(self, migration_project_id=None, migration_project_name=None, evaluation_project_id=None, evaluation_project_name=None, migration_project_status=None, permission_check_status=None, resource_id=None, created_time=None, updated_time=None):
        """ShowMigrationProjectStatusResponse

        The model defined in huaweicloud sdk

        :param migration_project_id: 迁移项目ID。
        :type migration_project_id: int
        :param migration_project_name: 迁移项目名称。
        :type migration_project_name: str
        :param evaluation_project_id: 评估项目ID。
        :type evaluation_project_id: int
        :param evaluation_project_name: 评估项目名称。
        :type evaluation_project_name: str
        :param migration_project_status: 迁移项目状态。
        :type migration_project_status: str
        :param permission_check_status: 目标库权限检查状态。
        :type permission_check_status: str
        :param resource_id: 资源ID。
        :type resource_id: str
        :param created_time: 创建时间。
        :type created_time: str
        :param updated_time: 更新时间。
        :type updated_time: str
        """
        
        super(ShowMigrationProjectStatusResponse, self).__init__()

        self._migration_project_id = None
        self._migration_project_name = None
        self._evaluation_project_id = None
        self._evaluation_project_name = None
        self._migration_project_status = None
        self._permission_check_status = None
        self._resource_id = None
        self._created_time = None
        self._updated_time = None
        self.discriminator = None

        if migration_project_id is not None:
            self.migration_project_id = migration_project_id
        if migration_project_name is not None:
            self.migration_project_name = migration_project_name
        if evaluation_project_id is not None:
            self.evaluation_project_id = evaluation_project_id
        if evaluation_project_name is not None:
            self.evaluation_project_name = evaluation_project_name
        if migration_project_status is not None:
            self.migration_project_status = migration_project_status
        if permission_check_status is not None:
            self.permission_check_status = permission_check_status
        if resource_id is not None:
            self.resource_id = resource_id
        if created_time is not None:
            self.created_time = created_time
        if updated_time is not None:
            self.updated_time = updated_time

    @property
    def migration_project_id(self):
        """Gets the migration_project_id of this ShowMigrationProjectStatusResponse.

        迁移项目ID。

        :return: The migration_project_id of this ShowMigrationProjectStatusResponse.
        :rtype: int
        """
        return self._migration_project_id

    @migration_project_id.setter
    def migration_project_id(self, migration_project_id):
        """Sets the migration_project_id of this ShowMigrationProjectStatusResponse.

        迁移项目ID。

        :param migration_project_id: The migration_project_id of this ShowMigrationProjectStatusResponse.
        :type migration_project_id: int
        """
        self._migration_project_id = migration_project_id

    @property
    def migration_project_name(self):
        """Gets the migration_project_name of this ShowMigrationProjectStatusResponse.

        迁移项目名称。

        :return: The migration_project_name of this ShowMigrationProjectStatusResponse.
        :rtype: str
        """
        return self._migration_project_name

    @migration_project_name.setter
    def migration_project_name(self, migration_project_name):
        """Sets the migration_project_name of this ShowMigrationProjectStatusResponse.

        迁移项目名称。

        :param migration_project_name: The migration_project_name of this ShowMigrationProjectStatusResponse.
        :type migration_project_name: str
        """
        self._migration_project_name = migration_project_name

    @property
    def evaluation_project_id(self):
        """Gets the evaluation_project_id of this ShowMigrationProjectStatusResponse.

        评估项目ID。

        :return: The evaluation_project_id of this ShowMigrationProjectStatusResponse.
        :rtype: int
        """
        return self._evaluation_project_id

    @evaluation_project_id.setter
    def evaluation_project_id(self, evaluation_project_id):
        """Sets the evaluation_project_id of this ShowMigrationProjectStatusResponse.

        评估项目ID。

        :param evaluation_project_id: The evaluation_project_id of this ShowMigrationProjectStatusResponse.
        :type evaluation_project_id: int
        """
        self._evaluation_project_id = evaluation_project_id

    @property
    def evaluation_project_name(self):
        """Gets the evaluation_project_name of this ShowMigrationProjectStatusResponse.

        评估项目名称。

        :return: The evaluation_project_name of this ShowMigrationProjectStatusResponse.
        :rtype: str
        """
        return self._evaluation_project_name

    @evaluation_project_name.setter
    def evaluation_project_name(self, evaluation_project_name):
        """Sets the evaluation_project_name of this ShowMigrationProjectStatusResponse.

        评估项目名称。

        :param evaluation_project_name: The evaluation_project_name of this ShowMigrationProjectStatusResponse.
        :type evaluation_project_name: str
        """
        self._evaluation_project_name = evaluation_project_name

    @property
    def migration_project_status(self):
        """Gets the migration_project_status of this ShowMigrationProjectStatusResponse.

        迁移项目状态。

        :return: The migration_project_status of this ShowMigrationProjectStatusResponse.
        :rtype: str
        """
        return self._migration_project_status

    @migration_project_status.setter
    def migration_project_status(self, migration_project_status):
        """Sets the migration_project_status of this ShowMigrationProjectStatusResponse.

        迁移项目状态。

        :param migration_project_status: The migration_project_status of this ShowMigrationProjectStatusResponse.
        :type migration_project_status: str
        """
        self._migration_project_status = migration_project_status

    @property
    def permission_check_status(self):
        """Gets the permission_check_status of this ShowMigrationProjectStatusResponse.

        目标库权限检查状态。

        :return: The permission_check_status of this ShowMigrationProjectStatusResponse.
        :rtype: str
        """
        return self._permission_check_status

    @permission_check_status.setter
    def permission_check_status(self, permission_check_status):
        """Sets the permission_check_status of this ShowMigrationProjectStatusResponse.

        目标库权限检查状态。

        :param permission_check_status: The permission_check_status of this ShowMigrationProjectStatusResponse.
        :type permission_check_status: str
        """
        self._permission_check_status = permission_check_status

    @property
    def resource_id(self):
        """Gets the resource_id of this ShowMigrationProjectStatusResponse.

        资源ID。

        :return: The resource_id of this ShowMigrationProjectStatusResponse.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this ShowMigrationProjectStatusResponse.

        资源ID。

        :param resource_id: The resource_id of this ShowMigrationProjectStatusResponse.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def created_time(self):
        """Gets the created_time of this ShowMigrationProjectStatusResponse.

        创建时间。

        :return: The created_time of this ShowMigrationProjectStatusResponse.
        :rtype: str
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this ShowMigrationProjectStatusResponse.

        创建时间。

        :param created_time: The created_time of this ShowMigrationProjectStatusResponse.
        :type created_time: str
        """
        self._created_time = created_time

    @property
    def updated_time(self):
        """Gets the updated_time of this ShowMigrationProjectStatusResponse.

        更新时间。

        :return: The updated_time of this ShowMigrationProjectStatusResponse.
        :rtype: str
        """
        return self._updated_time

    @updated_time.setter
    def updated_time(self, updated_time):
        """Sets the updated_time of this ShowMigrationProjectStatusResponse.

        更新时间。

        :param updated_time: The updated_time of this ShowMigrationProjectStatusResponse.
        :type updated_time: str
        """
        self._updated_time = updated_time

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
        if not isinstance(other, ShowMigrationProjectStatusResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
