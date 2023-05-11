# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MigrateResource:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'region_id': 'str',
        'project_id': 'str',
        'resource_id': 'str',
        'resource_type': 'str',
        'associated': 'bool'
    }

    attribute_map = {
        'region_id': 'region_id',
        'project_id': 'project_id',
        'resource_id': 'resource_id',
        'resource_type': 'resource_type',
        'associated': 'associated'
    }

    def __init__(self, region_id=None, project_id=None, resource_id=None, resource_type=None, associated=None):
        """MigrateResource

        The model defined in huaweicloud sdk

        :param region_id: 资源所属RegionID。迁移OBS服务资源时为必选项。
        :type region_id: str
        :param project_id: 项目ID。resource_type为region级别服务时为必选项。
        :type project_id: str
        :param resource_id: 资源ID
        :type resource_id: str
        :param resource_type: 资源类型
        :type resource_type: str
        :param associated: 是否关联迁移。目前仅支持ECS关联资源EVS、EIP迁移。
        :type associated: bool
        """
        
        

        self._region_id = None
        self._project_id = None
        self._resource_id = None
        self._resource_type = None
        self._associated = None
        self.discriminator = None

        if region_id is not None:
            self.region_id = region_id
        if project_id is not None:
            self.project_id = project_id
        self.resource_id = resource_id
        self.resource_type = resource_type
        if associated is not None:
            self.associated = associated

    @property
    def region_id(self):
        """Gets the region_id of this MigrateResource.

        资源所属RegionID。迁移OBS服务资源时为必选项。

        :return: The region_id of this MigrateResource.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this MigrateResource.

        资源所属RegionID。迁移OBS服务资源时为必选项。

        :param region_id: The region_id of this MigrateResource.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def project_id(self):
        """Gets the project_id of this MigrateResource.

        项目ID。resource_type为region级别服务时为必选项。

        :return: The project_id of this MigrateResource.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this MigrateResource.

        项目ID。resource_type为region级别服务时为必选项。

        :param project_id: The project_id of this MigrateResource.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def resource_id(self):
        """Gets the resource_id of this MigrateResource.

        资源ID

        :return: The resource_id of this MigrateResource.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this MigrateResource.

        资源ID

        :param resource_id: The resource_id of this MigrateResource.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def resource_type(self):
        """Gets the resource_type of this MigrateResource.

        资源类型

        :return: The resource_type of this MigrateResource.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this MigrateResource.

        资源类型

        :param resource_type: The resource_type of this MigrateResource.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def associated(self):
        """Gets the associated of this MigrateResource.

        是否关联迁移。目前仅支持ECS关联资源EVS、EIP迁移。

        :return: The associated of this MigrateResource.
        :rtype: bool
        """
        return self._associated

    @associated.setter
    def associated(self, associated):
        """Sets the associated of this MigrateResource.

        是否关联迁移。目前仅支持ECS关联资源EVS、EIP迁移。

        :param associated: The associated of this MigrateResource.
        :type associated: bool
        """
        self._associated = associated

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
        if not isinstance(other, MigrateResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
