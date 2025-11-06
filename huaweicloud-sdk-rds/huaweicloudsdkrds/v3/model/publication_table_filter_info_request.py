# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PublicationTableFilterInfoRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'relation': 'str',
        'column': 'str',
        'condition': 'str',
        'value': 'str',
        'filters': 'list[PublicationTableFilterInfoRequest]'
    }

    attribute_map = {
        'relation': 'relation',
        'column': 'column',
        'condition': 'condition',
        'value': 'value',
        'filters': 'filters'
    }

    def __init__(self, relation=None, column=None, condition=None, value=None, filters=None):
        r"""PublicationTableFilterInfoRequest

        The model defined in huaweicloud sdk

        :param relation: 筛选关系。  为空时表示当前为最下级筛选器，不为空时表示当前项还有下级筛选器 不为空时取值范围：AND, OR
        :type relation: str
        :param column: 筛选字段（仅当筛选关系为空时生效，且筛选关系为空时必传）。
        :type column: str
        :param condition: 筛选条件（仅当筛选关系为空时生效，且筛选关系为空时必传）。 取值范围： &#x3D;, !&#x3D;, &gt;, &lt;, &gt;&#x3D;, &lt;&#x3D;, LIKE, NOT LIKE, IN
        :type condition: str
        :param value: 筛选值（仅当筛选关系为空时生效，且筛选关系为空时必传）。
        :type value: str
        :param filters: 下级筛选器（仅当筛选关系不为空时生效，且筛选关系不为空时必传）。
        :type filters: list[:class:`huaweicloudsdkrds.v3.PublicationTableFilterInfoRequest`]
        """
        
        

        self._relation = None
        self._column = None
        self._condition = None
        self._value = None
        self._filters = None
        self.discriminator = None

        if relation is not None:
            self.relation = relation
        if column is not None:
            self.column = column
        if condition is not None:
            self.condition = condition
        if value is not None:
            self.value = value
        if filters is not None:
            self.filters = filters

    @property
    def relation(self):
        r"""Gets the relation of this PublicationTableFilterInfoRequest.

        筛选关系。  为空时表示当前为最下级筛选器，不为空时表示当前项还有下级筛选器 不为空时取值范围：AND, OR

        :return: The relation of this PublicationTableFilterInfoRequest.
        :rtype: str
        """
        return self._relation

    @relation.setter
    def relation(self, relation):
        r"""Sets the relation of this PublicationTableFilterInfoRequest.

        筛选关系。  为空时表示当前为最下级筛选器，不为空时表示当前项还有下级筛选器 不为空时取值范围：AND, OR

        :param relation: The relation of this PublicationTableFilterInfoRequest.
        :type relation: str
        """
        self._relation = relation

    @property
    def column(self):
        r"""Gets the column of this PublicationTableFilterInfoRequest.

        筛选字段（仅当筛选关系为空时生效，且筛选关系为空时必传）。

        :return: The column of this PublicationTableFilterInfoRequest.
        :rtype: str
        """
        return self._column

    @column.setter
    def column(self, column):
        r"""Sets the column of this PublicationTableFilterInfoRequest.

        筛选字段（仅当筛选关系为空时生效，且筛选关系为空时必传）。

        :param column: The column of this PublicationTableFilterInfoRequest.
        :type column: str
        """
        self._column = column

    @property
    def condition(self):
        r"""Gets the condition of this PublicationTableFilterInfoRequest.

        筛选条件（仅当筛选关系为空时生效，且筛选关系为空时必传）。 取值范围： =, !=, >, <, >=, <=, LIKE, NOT LIKE, IN

        :return: The condition of this PublicationTableFilterInfoRequest.
        :rtype: str
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        r"""Sets the condition of this PublicationTableFilterInfoRequest.

        筛选条件（仅当筛选关系为空时生效，且筛选关系为空时必传）。 取值范围： =, !=, >, <, >=, <=, LIKE, NOT LIKE, IN

        :param condition: The condition of this PublicationTableFilterInfoRequest.
        :type condition: str
        """
        self._condition = condition

    @property
    def value(self):
        r"""Gets the value of this PublicationTableFilterInfoRequest.

        筛选值（仅当筛选关系为空时生效，且筛选关系为空时必传）。

        :return: The value of this PublicationTableFilterInfoRequest.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this PublicationTableFilterInfoRequest.

        筛选值（仅当筛选关系为空时生效，且筛选关系为空时必传）。

        :param value: The value of this PublicationTableFilterInfoRequest.
        :type value: str
        """
        self._value = value

    @property
    def filters(self):
        r"""Gets the filters of this PublicationTableFilterInfoRequest.

        下级筛选器（仅当筛选关系不为空时生效，且筛选关系不为空时必传）。

        :return: The filters of this PublicationTableFilterInfoRequest.
        :rtype: list[:class:`huaweicloudsdkrds.v3.PublicationTableFilterInfoRequest`]
        """
        return self._filters

    @filters.setter
    def filters(self, filters):
        r"""Sets the filters of this PublicationTableFilterInfoRequest.

        下级筛选器（仅当筛选关系不为空时生效，且筛选关系不为空时必传）。

        :param filters: The filters of this PublicationTableFilterInfoRequest.
        :type filters: list[:class:`huaweicloudsdkrds.v3.PublicationTableFilterInfoRequest`]
        """
        self._filters = filters

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
        if not isinstance(other, PublicationTableFilterInfoRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
