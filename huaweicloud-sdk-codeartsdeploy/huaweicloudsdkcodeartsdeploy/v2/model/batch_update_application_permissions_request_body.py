# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchUpdateApplicationPermissionsRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_id': 'str',
        'application_ids': 'list[str]',
        'roles': 'list[AppPermission]'
    }

    attribute_map = {
        'project_id': 'project_id',
        'application_ids': 'application_ids',
        'roles': 'roles'
    }

    def __init__(self, project_id=None, application_ids=None, roles=None):
        r"""BatchUpdateApplicationPermissionsRequestBody

        The model defined in huaweicloud sdk

        :param project_id: 项目id
        :type project_id: str
        :param application_ids: 应用列表
        :type application_ids: list[str]
        :param roles: 角色权限
        :type roles: list[:class:`huaweicloudsdkcodeartsdeploy.v2.AppPermission`]
        """
        
        

        self._project_id = None
        self._application_ids = None
        self._roles = None
        self.discriminator = None

        self.project_id = project_id
        self.application_ids = application_ids
        self.roles = roles

    @property
    def project_id(self):
        r"""Gets the project_id of this BatchUpdateApplicationPermissionsRequestBody.

        项目id

        :return: The project_id of this BatchUpdateApplicationPermissionsRequestBody.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this BatchUpdateApplicationPermissionsRequestBody.

        项目id

        :param project_id: The project_id of this BatchUpdateApplicationPermissionsRequestBody.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def application_ids(self):
        r"""Gets the application_ids of this BatchUpdateApplicationPermissionsRequestBody.

        应用列表

        :return: The application_ids of this BatchUpdateApplicationPermissionsRequestBody.
        :rtype: list[str]
        """
        return self._application_ids

    @application_ids.setter
    def application_ids(self, application_ids):
        r"""Sets the application_ids of this BatchUpdateApplicationPermissionsRequestBody.

        应用列表

        :param application_ids: The application_ids of this BatchUpdateApplicationPermissionsRequestBody.
        :type application_ids: list[str]
        """
        self._application_ids = application_ids

    @property
    def roles(self):
        r"""Gets the roles of this BatchUpdateApplicationPermissionsRequestBody.

        角色权限

        :return: The roles of this BatchUpdateApplicationPermissionsRequestBody.
        :rtype: list[:class:`huaweicloudsdkcodeartsdeploy.v2.AppPermission`]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        r"""Sets the roles of this BatchUpdateApplicationPermissionsRequestBody.

        角色权限

        :param roles: The roles of this BatchUpdateApplicationPermissionsRequestBody.
        :type roles: list[:class:`huaweicloudsdkcodeartsdeploy.v2.AppPermission`]
        """
        self._roles = roles

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
        if not isinstance(other, BatchUpdateApplicationPermissionsRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
