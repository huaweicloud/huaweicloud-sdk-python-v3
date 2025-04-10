# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListMigprojectsResponse(SdkResponse):

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
        'migprojects': 'list[MigprojectsResponseBody]'
    }

    attribute_map = {
        'count': 'count',
        'migprojects': 'migprojects'
    }

    def __init__(self, count=None, migprojects=None):
        r"""ListMigprojectsResponse

        The model defined in huaweicloud sdk

        :param count: 查询到的迁移项目的数量
        :type count: int
        :param migprojects: 查询到的迁移项目详情
        :type migprojects: list[:class:`huaweicloudsdksms.v3.MigprojectsResponseBody`]
        """
        
        super(ListMigprojectsResponse, self).__init__()

        self._count = None
        self._migprojects = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if migprojects is not None:
            self.migprojects = migprojects

    @property
    def count(self):
        r"""Gets the count of this ListMigprojectsResponse.

        查询到的迁移项目的数量

        :return: The count of this ListMigprojectsResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ListMigprojectsResponse.

        查询到的迁移项目的数量

        :param count: The count of this ListMigprojectsResponse.
        :type count: int
        """
        self._count = count

    @property
    def migprojects(self):
        r"""Gets the migprojects of this ListMigprojectsResponse.

        查询到的迁移项目详情

        :return: The migprojects of this ListMigprojectsResponse.
        :rtype: list[:class:`huaweicloudsdksms.v3.MigprojectsResponseBody`]
        """
        return self._migprojects

    @migprojects.setter
    def migprojects(self, migprojects):
        r"""Sets the migprojects of this ListMigprojectsResponse.

        查询到的迁移项目详情

        :param migprojects: The migprojects of this ListMigprojectsResponse.
        :type migprojects: list[:class:`huaweicloudsdksms.v3.MigprojectsResponseBody`]
        """
        self._migprojects = migprojects

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
        if not isinstance(other, ListMigprojectsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
