# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPermissionCheckResultRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'migration_project_id': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'migration_project_id': 'migration_project_id',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, migration_project_id=None, offset=None, limit=None):
        """ListPermissionCheckResultRequest

        The model defined in huaweicloud sdk

        :param migration_project_id: 迁移项目ID。
        :type migration_project_id: str
        :param offset: 分页查询的偏移量。
        :type offset: int
        :param limit: 每页显示的条目数量。
        :type limit: int
        """
        
        

        self._migration_project_id = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.migration_project_id = migration_project_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def migration_project_id(self):
        """Gets the migration_project_id of this ListPermissionCheckResultRequest.

        迁移项目ID。

        :return: The migration_project_id of this ListPermissionCheckResultRequest.
        :rtype: str
        """
        return self._migration_project_id

    @migration_project_id.setter
    def migration_project_id(self, migration_project_id):
        """Sets the migration_project_id of this ListPermissionCheckResultRequest.

        迁移项目ID。

        :param migration_project_id: The migration_project_id of this ListPermissionCheckResultRequest.
        :type migration_project_id: str
        """
        self._migration_project_id = migration_project_id

    @property
    def offset(self):
        """Gets the offset of this ListPermissionCheckResultRequest.

        分页查询的偏移量。

        :return: The offset of this ListPermissionCheckResultRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListPermissionCheckResultRequest.

        分页查询的偏移量。

        :param offset: The offset of this ListPermissionCheckResultRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListPermissionCheckResultRequest.

        每页显示的条目数量。

        :return: The limit of this ListPermissionCheckResultRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListPermissionCheckResultRequest.

        每页显示的条目数量。

        :param limit: The limit of this ListPermissionCheckResultRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListPermissionCheckResultRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
