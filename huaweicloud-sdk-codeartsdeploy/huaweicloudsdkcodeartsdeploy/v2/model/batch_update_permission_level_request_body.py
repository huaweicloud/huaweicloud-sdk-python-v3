# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchUpdatePermissionLevelRequestBody:

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
        'permission_level': 'str',
        'application_ids': 'list[str]'
    }

    attribute_map = {
        'project_id': 'project_id',
        'permission_level': 'permission_level',
        'application_ids': 'application_ids'
    }

    def __init__(self, project_id=None, permission_level=None, application_ids=None):
        r"""BatchUpdatePermissionLevelRequestBody

        The model defined in huaweicloud sdk

        :param project_id: 项目id
        :type project_id: str
        :param permission_level: 应用鉴权级别，instance：实例级；project：项目级
        :type permission_level: str
        :param application_ids: 应用id列表
        :type application_ids: list[str]
        """
        
        

        self._project_id = None
        self._permission_level = None
        self._application_ids = None
        self.discriminator = None

        self.project_id = project_id
        self.permission_level = permission_level
        self.application_ids = application_ids

    @property
    def project_id(self):
        r"""Gets the project_id of this BatchUpdatePermissionLevelRequestBody.

        项目id

        :return: The project_id of this BatchUpdatePermissionLevelRequestBody.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this BatchUpdatePermissionLevelRequestBody.

        项目id

        :param project_id: The project_id of this BatchUpdatePermissionLevelRequestBody.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def permission_level(self):
        r"""Gets the permission_level of this BatchUpdatePermissionLevelRequestBody.

        应用鉴权级别，instance：实例级；project：项目级

        :return: The permission_level of this BatchUpdatePermissionLevelRequestBody.
        :rtype: str
        """
        return self._permission_level

    @permission_level.setter
    def permission_level(self, permission_level):
        r"""Sets the permission_level of this BatchUpdatePermissionLevelRequestBody.

        应用鉴权级别，instance：实例级；project：项目级

        :param permission_level: The permission_level of this BatchUpdatePermissionLevelRequestBody.
        :type permission_level: str
        """
        self._permission_level = permission_level

    @property
    def application_ids(self):
        r"""Gets the application_ids of this BatchUpdatePermissionLevelRequestBody.

        应用id列表

        :return: The application_ids of this BatchUpdatePermissionLevelRequestBody.
        :rtype: list[str]
        """
        return self._application_ids

    @application_ids.setter
    def application_ids(self, application_ids):
        r"""Sets the application_ids of this BatchUpdatePermissionLevelRequestBody.

        应用id列表

        :param application_ids: The application_ids of this BatchUpdatePermissionLevelRequestBody.
        :type application_ids: list[str]
        """
        self._application_ids = application_ids

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
        if not isinstance(other, BatchUpdatePermissionLevelRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
