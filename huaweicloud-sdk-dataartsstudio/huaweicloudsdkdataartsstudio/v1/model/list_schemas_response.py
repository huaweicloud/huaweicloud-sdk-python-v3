# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSchemasResponse(SdkResponse):

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
        'database': 'str',
        'schemas': 'list[SchemasList]'
    }

    attribute_map = {
        'total_count': 'total_count',
        'dw_id': 'dw_id',
        'database': 'database',
        'schemas': 'schemas'
    }

    def __init__(self, total_count=None, dw_id=None, database=None, schemas=None):
        r"""ListSchemasResponse

        The model defined in huaweicloud sdk

        :param total_count: 当前数据连接schema记录数
        :type total_count: int
        :param dw_id: 数据连接id
        :type dw_id: str
        :param database: 数据库名称
        :type database: str
        :param schemas: schema列表
        :type schemas: list[:class:`huaweicloudsdkdataartsstudio.v1.SchemasList`]
        """
        
        super(ListSchemasResponse, self).__init__()

        self._total_count = None
        self._dw_id = None
        self._database = None
        self._schemas = None
        self.discriminator = None

        if total_count is not None:
            self.total_count = total_count
        if dw_id is not None:
            self.dw_id = dw_id
        if database is not None:
            self.database = database
        if schemas is not None:
            self.schemas = schemas

    @property
    def total_count(self):
        r"""Gets the total_count of this ListSchemasResponse.

        当前数据连接schema记录数

        :return: The total_count of this ListSchemasResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ListSchemasResponse.

        当前数据连接schema记录数

        :param total_count: The total_count of this ListSchemasResponse.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def dw_id(self):
        r"""Gets the dw_id of this ListSchemasResponse.

        数据连接id

        :return: The dw_id of this ListSchemasResponse.
        :rtype: str
        """
        return self._dw_id

    @dw_id.setter
    def dw_id(self, dw_id):
        r"""Sets the dw_id of this ListSchemasResponse.

        数据连接id

        :param dw_id: The dw_id of this ListSchemasResponse.
        :type dw_id: str
        """
        self._dw_id = dw_id

    @property
    def database(self):
        r"""Gets the database of this ListSchemasResponse.

        数据库名称

        :return: The database of this ListSchemasResponse.
        :rtype: str
        """
        return self._database

    @database.setter
    def database(self, database):
        r"""Sets the database of this ListSchemasResponse.

        数据库名称

        :param database: The database of this ListSchemasResponse.
        :type database: str
        """
        self._database = database

    @property
    def schemas(self):
        r"""Gets the schemas of this ListSchemasResponse.

        schema列表

        :return: The schemas of this ListSchemasResponse.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.SchemasList`]
        """
        return self._schemas

    @schemas.setter
    def schemas(self, schemas):
        r"""Sets the schemas of this ListSchemasResponse.

        schema列表

        :param schemas: The schemas of this ListSchemasResponse.
        :type schemas: list[:class:`huaweicloudsdkdataartsstudio.v1.SchemasList`]
        """
        self._schemas = schemas

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
        if not isinstance(other, ListSchemasResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
