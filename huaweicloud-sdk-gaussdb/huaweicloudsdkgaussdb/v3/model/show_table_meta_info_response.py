# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTableMetaInfoResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'table_meta_infos': 'list[TableMetaInfo]',
        'table_names': 'list[str]',
        'database_names': 'list[str]'
    }

    attribute_map = {
        'table_meta_infos': 'table_meta_infos',
        'table_names': 'table_names',
        'database_names': 'database_names'
    }

    def __init__(self, table_meta_infos=None, table_names=None, database_names=None):
        r"""ShowTableMetaInfoResponse

        The model defined in huaweicloud sdk

        :param table_meta_infos: 要版本升级的批量实例。
        :type table_meta_infos: list[:class:`huaweicloudsdkgaussdb.v3.TableMetaInfo`]
        :param table_names: 数据表名称
        :type table_names: list[str]
        :param database_names: 数据库名称
        :type database_names: list[str]
        """
        
        super(ShowTableMetaInfoResponse, self).__init__()

        self._table_meta_infos = None
        self._table_names = None
        self._database_names = None
        self.discriminator = None

        if table_meta_infos is not None:
            self.table_meta_infos = table_meta_infos
        if table_names is not None:
            self.table_names = table_names
        if database_names is not None:
            self.database_names = database_names

    @property
    def table_meta_infos(self):
        r"""Gets the table_meta_infos of this ShowTableMetaInfoResponse.

        要版本升级的批量实例。

        :return: The table_meta_infos of this ShowTableMetaInfoResponse.
        :rtype: list[:class:`huaweicloudsdkgaussdb.v3.TableMetaInfo`]
        """
        return self._table_meta_infos

    @table_meta_infos.setter
    def table_meta_infos(self, table_meta_infos):
        r"""Sets the table_meta_infos of this ShowTableMetaInfoResponse.

        要版本升级的批量实例。

        :param table_meta_infos: The table_meta_infos of this ShowTableMetaInfoResponse.
        :type table_meta_infos: list[:class:`huaweicloudsdkgaussdb.v3.TableMetaInfo`]
        """
        self._table_meta_infos = table_meta_infos

    @property
    def table_names(self):
        r"""Gets the table_names of this ShowTableMetaInfoResponse.

        数据表名称

        :return: The table_names of this ShowTableMetaInfoResponse.
        :rtype: list[str]
        """
        return self._table_names

    @table_names.setter
    def table_names(self, table_names):
        r"""Sets the table_names of this ShowTableMetaInfoResponse.

        数据表名称

        :param table_names: The table_names of this ShowTableMetaInfoResponse.
        :type table_names: list[str]
        """
        self._table_names = table_names

    @property
    def database_names(self):
        r"""Gets the database_names of this ShowTableMetaInfoResponse.

        数据库名称

        :return: The database_names of this ShowTableMetaInfoResponse.
        :rtype: list[str]
        """
        return self._database_names

    @database_names.setter
    def database_names(self, database_names):
        r"""Sets the database_names of this ShowTableMetaInfoResponse.

        数据库名称

        :param database_names: The database_names of this ShowTableMetaInfoResponse.
        :type database_names: list[str]
        """
        self._database_names = database_names

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
        if not isinstance(other, ShowTableMetaInfoResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
