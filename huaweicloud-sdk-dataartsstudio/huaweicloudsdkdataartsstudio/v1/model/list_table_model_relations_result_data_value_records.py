# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTableModelRelationsResultDataValueRecords:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tables': 'list[TableModelVO]',
        'inheritances': 'list[object]',
        'relations': 'list[RelationVO]'
    }

    attribute_map = {
        'tables': 'tables',
        'inheritances': 'inheritances',
        'relations': 'relations'
    }

    def __init__(self, tables=None, inheritances=None, relations=None):
        r"""ListTableModelRelationsResultDataValueRecords

        The model defined in huaweicloud sdk

        :param tables: TableModelVO信息。
        :type tables: list[:class:`huaweicloudsdkdataartsstudio.v1.TableModelVO`]
        :param inheritances: 层级信息信息。
        :type inheritances: list[object]
        :param relations: RelationVO信息。
        :type relations: list[:class:`huaweicloudsdkdataartsstudio.v1.RelationVO`]
        """
        
        

        self._tables = None
        self._inheritances = None
        self._relations = None
        self.discriminator = None

        if tables is not None:
            self.tables = tables
        if inheritances is not None:
            self.inheritances = inheritances
        if relations is not None:
            self.relations = relations

    @property
    def tables(self):
        r"""Gets the tables of this ListTableModelRelationsResultDataValueRecords.

        TableModelVO信息。

        :return: The tables of this ListTableModelRelationsResultDataValueRecords.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.TableModelVO`]
        """
        return self._tables

    @tables.setter
    def tables(self, tables):
        r"""Sets the tables of this ListTableModelRelationsResultDataValueRecords.

        TableModelVO信息。

        :param tables: The tables of this ListTableModelRelationsResultDataValueRecords.
        :type tables: list[:class:`huaweicloudsdkdataartsstudio.v1.TableModelVO`]
        """
        self._tables = tables

    @property
    def inheritances(self):
        r"""Gets the inheritances of this ListTableModelRelationsResultDataValueRecords.

        层级信息信息。

        :return: The inheritances of this ListTableModelRelationsResultDataValueRecords.
        :rtype: list[object]
        """
        return self._inheritances

    @inheritances.setter
    def inheritances(self, inheritances):
        r"""Sets the inheritances of this ListTableModelRelationsResultDataValueRecords.

        层级信息信息。

        :param inheritances: The inheritances of this ListTableModelRelationsResultDataValueRecords.
        :type inheritances: list[object]
        """
        self._inheritances = inheritances

    @property
    def relations(self):
        r"""Gets the relations of this ListTableModelRelationsResultDataValueRecords.

        RelationVO信息。

        :return: The relations of this ListTableModelRelationsResultDataValueRecords.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.RelationVO`]
        """
        return self._relations

    @relations.setter
    def relations(self, relations):
        r"""Sets the relations of this ListTableModelRelationsResultDataValueRecords.

        RelationVO信息。

        :param relations: The relations of this ListTableModelRelationsResultDataValueRecords.
        :type relations: list[:class:`huaweicloudsdkdataartsstudio.v1.RelationVO`]
        """
        self._relations = relations

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
        if not isinstance(other, ListTableModelRelationsResultDataValueRecords):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
