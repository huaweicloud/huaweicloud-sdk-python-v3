# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDatabaseVersionsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'database_versions': 'list[DatabaseVersionResult]',
        'total': 'int'
    }

    attribute_map = {
        'database_versions': 'database_versions',
        'total': 'total'
    }

    def __init__(self, database_versions=None, total=None):
        r"""ListDatabaseVersionsResponse

        The model defined in huaweicloud sdk

        :param database_versions: **参数解释**： 数据库版本列表。
        :type database_versions: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.DatabaseVersionResult`]
        :param total: **参数解释**： 数据库三位引擎版本总个数。 **取值范围**： 不涉及。
        :type total: int
        """
        
        super(ListDatabaseVersionsResponse, self).__init__()

        self._database_versions = None
        self._total = None
        self.discriminator = None

        if database_versions is not None:
            self.database_versions = database_versions
        if total is not None:
            self.total = total

    @property
    def database_versions(self):
        r"""Gets the database_versions of this ListDatabaseVersionsResponse.

        **参数解释**： 数据库版本列表。

        :return: The database_versions of this ListDatabaseVersionsResponse.
        :rtype: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.DatabaseVersionResult`]
        """
        return self._database_versions

    @database_versions.setter
    def database_versions(self, database_versions):
        r"""Sets the database_versions of this ListDatabaseVersionsResponse.

        **参数解释**： 数据库版本列表。

        :param database_versions: The database_versions of this ListDatabaseVersionsResponse.
        :type database_versions: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.DatabaseVersionResult`]
        """
        self._database_versions = database_versions

    @property
    def total(self):
        r"""Gets the total of this ListDatabaseVersionsResponse.

        **参数解释**： 数据库三位引擎版本总个数。 **取值范围**： 不涉及。

        :return: The total of this ListDatabaseVersionsResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListDatabaseVersionsResponse.

        **参数解释**： 数据库三位引擎版本总个数。 **取值范围**： 不涉及。

        :param total: The total of this ListDatabaseVersionsResponse.
        :type total: int
        """
        self._total = total

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
        if not isinstance(other, ListDatabaseVersionsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
