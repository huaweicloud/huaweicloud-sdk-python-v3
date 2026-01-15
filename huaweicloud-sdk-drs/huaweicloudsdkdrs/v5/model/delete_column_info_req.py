# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteColumnInfoReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'table_ids': 'list[str]',
        'schema_ids': 'list[str]',
        'db_ids': 'list[str]'
    }

    attribute_map = {
        'table_ids': 'table_ids',
        'schema_ids': 'schema_ids',
        'db_ids': 'db_ids'
    }

    def __init__(self, table_ids=None, schema_ids=None, db_ids=None):
        r"""DeleteColumnInfoReq

        The model defined in huaweicloud sdk

        :param table_ids: 列所属表的id
        :type table_ids: list[str]
        :param schema_ids: 列所属schema的id
        :type schema_ids: list[str]
        :param db_ids: 列所属库的id
        :type db_ids: list[str]
        """
        
        

        self._table_ids = None
        self._schema_ids = None
        self._db_ids = None
        self.discriminator = None

        self.table_ids = table_ids
        self.schema_ids = schema_ids
        self.db_ids = db_ids

    @property
    def table_ids(self):
        r"""Gets the table_ids of this DeleteColumnInfoReq.

        列所属表的id

        :return: The table_ids of this DeleteColumnInfoReq.
        :rtype: list[str]
        """
        return self._table_ids

    @table_ids.setter
    def table_ids(self, table_ids):
        r"""Sets the table_ids of this DeleteColumnInfoReq.

        列所属表的id

        :param table_ids: The table_ids of this DeleteColumnInfoReq.
        :type table_ids: list[str]
        """
        self._table_ids = table_ids

    @property
    def schema_ids(self):
        r"""Gets the schema_ids of this DeleteColumnInfoReq.

        列所属schema的id

        :return: The schema_ids of this DeleteColumnInfoReq.
        :rtype: list[str]
        """
        return self._schema_ids

    @schema_ids.setter
    def schema_ids(self, schema_ids):
        r"""Sets the schema_ids of this DeleteColumnInfoReq.

        列所属schema的id

        :param schema_ids: The schema_ids of this DeleteColumnInfoReq.
        :type schema_ids: list[str]
        """
        self._schema_ids = schema_ids

    @property
    def db_ids(self):
        r"""Gets the db_ids of this DeleteColumnInfoReq.

        列所属库的id

        :return: The db_ids of this DeleteColumnInfoReq.
        :rtype: list[str]
        """
        return self._db_ids

    @db_ids.setter
    def db_ids(self, db_ids):
        r"""Sets the db_ids of this DeleteColumnInfoReq.

        列所属库的id

        :param db_ids: The db_ids of this DeleteColumnInfoReq.
        :type db_ids: list[str]
        """
        self._db_ids = db_ids

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DeleteColumnInfoReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
