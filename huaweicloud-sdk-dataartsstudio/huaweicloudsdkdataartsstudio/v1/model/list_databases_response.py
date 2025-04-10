# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDatabasesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_count': 'int',
        'dw_id': 'str',
        'databases': 'list[DatabasesList]'
    }

    attribute_map = {
        'total_count': 'total_count',
        'dw_id': 'dw_id',
        'databases': 'databases'
    }

    def __init__(self, total_count=None, dw_id=None, databases=None):
        r"""ListDatabasesResponse

        The model defined in huaweicloud sdk

        :param total_count: 当前数据连接数据库记录数
        :type total_count: int
        :param dw_id: 数据连接id
        :type dw_id: str
        :param databases: 数据库列表
        :type databases: list[:class:`huaweicloudsdkdataartsstudio.v1.DatabasesList`]
        """
        
        super(ListDatabasesResponse, self).__init__()

        self._total_count = None
        self._dw_id = None
        self._databases = None
        self.discriminator = None

        if total_count is not None:
            self.total_count = total_count
        if dw_id is not None:
            self.dw_id = dw_id
        if databases is not None:
            self.databases = databases

    @property
    def total_count(self):
        r"""Gets the total_count of this ListDatabasesResponse.

        当前数据连接数据库记录数

        :return: The total_count of this ListDatabasesResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ListDatabasesResponse.

        当前数据连接数据库记录数

        :param total_count: The total_count of this ListDatabasesResponse.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def dw_id(self):
        r"""Gets the dw_id of this ListDatabasesResponse.

        数据连接id

        :return: The dw_id of this ListDatabasesResponse.
        :rtype: str
        """
        return self._dw_id

    @dw_id.setter
    def dw_id(self, dw_id):
        r"""Sets the dw_id of this ListDatabasesResponse.

        数据连接id

        :param dw_id: The dw_id of this ListDatabasesResponse.
        :type dw_id: str
        """
        self._dw_id = dw_id

    @property
    def databases(self):
        r"""Gets the databases of this ListDatabasesResponse.

        数据库列表

        :return: The databases of this ListDatabasesResponse.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.DatabasesList`]
        """
        return self._databases

    @databases.setter
    def databases(self, databases):
        r"""Sets the databases of this ListDatabasesResponse.

        数据库列表

        :param databases: The databases of this ListDatabasesResponse.
        :type databases: list[:class:`huaweicloudsdkdataartsstudio.v1.DatabasesList`]
        """
        self._databases = databases

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
        if not isinstance(other, ListDatabasesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
