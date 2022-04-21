# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListErrorServersResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'count': 'int',
        'migration_errors': 'list[MigrationErrors]'
    }

    attribute_map = {
        'count': 'count',
        'migration_errors': 'migration_errors'
    }

    def __init__(self, count=None, migration_errors=None):
        """ListErrorServersResponse

        The model defined in huaweicloud sdk

        :param count: 迁移过程中发生错误的源端数量
        :type count: int
        :param migration_errors: 迁移过程中发生的错误详情
        :type migration_errors: list[:class:`huaweicloudsdksms.v3.MigrationErrors`]
        """
        
        super(ListErrorServersResponse, self).__init__()

        self._count = None
        self._migration_errors = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if migration_errors is not None:
            self.migration_errors = migration_errors

    @property
    def count(self):
        """Gets the count of this ListErrorServersResponse.

        迁移过程中发生错误的源端数量

        :return: The count of this ListErrorServersResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListErrorServersResponse.

        迁移过程中发生错误的源端数量

        :param count: The count of this ListErrorServersResponse.
        :type count: int
        """
        self._count = count

    @property
    def migration_errors(self):
        """Gets the migration_errors of this ListErrorServersResponse.

        迁移过程中发生的错误详情

        :return: The migration_errors of this ListErrorServersResponse.
        :rtype: list[:class:`huaweicloudsdksms.v3.MigrationErrors`]
        """
        return self._migration_errors

    @migration_errors.setter
    def migration_errors(self, migration_errors):
        """Sets the migration_errors of this ListErrorServersResponse.

        迁移过程中发生的错误详情

        :param migration_errors: The migration_errors of this ListErrorServersResponse.
        :type migration_errors: list[:class:`huaweicloudsdksms.v3.MigrationErrors`]
        """
        self._migration_errors = migration_errors

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
        if not isinstance(other, ListErrorServersResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
