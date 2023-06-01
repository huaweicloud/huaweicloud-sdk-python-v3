# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DetailItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'case_aw_id': 'str',
        'datum_type': 'int',
        'name': 'str',
        'transaction_id': 'str',
        'aw_list': 'list[DetailItem]'
    }

    attribute_map = {
        'case_aw_id': 'caseAwId',
        'datum_type': 'datumType',
        'name': 'name',
        'transaction_id': 'transactionId',
        'aw_list': 'awList'
    }

    def __init__(self, case_aw_id=None, datum_type=None, name=None, transaction_id=None, aw_list=None):
        """DetailItem

        The model defined in huaweicloud sdk

        :param case_aw_id: 数据库中dc_case_aw表中的主键ID
        :type case_aw_id: str
        :param datum_type: 数据类型（用例/aw/事务）
        :type datum_type: int
        :param name: 用例/aw/事务名
        :type name: str
        :param transaction_id: 事务ID
        :type transaction_id: str
        :param aw_list: aw列表
        :type aw_list: list[:class:`huaweicloudsdkcpts.v1.DetailItem`]
        """
        
        

        self._case_aw_id = None
        self._datum_type = None
        self._name = None
        self._transaction_id = None
        self._aw_list = None
        self.discriminator = None

        if case_aw_id is not None:
            self.case_aw_id = case_aw_id
        if datum_type is not None:
            self.datum_type = datum_type
        if name is not None:
            self.name = name
        if transaction_id is not None:
            self.transaction_id = transaction_id
        if aw_list is not None:
            self.aw_list = aw_list

    @property
    def case_aw_id(self):
        """Gets the case_aw_id of this DetailItem.

        数据库中dc_case_aw表中的主键ID

        :return: The case_aw_id of this DetailItem.
        :rtype: str
        """
        return self._case_aw_id

    @case_aw_id.setter
    def case_aw_id(self, case_aw_id):
        """Sets the case_aw_id of this DetailItem.

        数据库中dc_case_aw表中的主键ID

        :param case_aw_id: The case_aw_id of this DetailItem.
        :type case_aw_id: str
        """
        self._case_aw_id = case_aw_id

    @property
    def datum_type(self):
        """Gets the datum_type of this DetailItem.

        数据类型（用例/aw/事务）

        :return: The datum_type of this DetailItem.
        :rtype: int
        """
        return self._datum_type

    @datum_type.setter
    def datum_type(self, datum_type):
        """Sets the datum_type of this DetailItem.

        数据类型（用例/aw/事务）

        :param datum_type: The datum_type of this DetailItem.
        :type datum_type: int
        """
        self._datum_type = datum_type

    @property
    def name(self):
        """Gets the name of this DetailItem.

        用例/aw/事务名

        :return: The name of this DetailItem.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DetailItem.

        用例/aw/事务名

        :param name: The name of this DetailItem.
        :type name: str
        """
        self._name = name

    @property
    def transaction_id(self):
        """Gets the transaction_id of this DetailItem.

        事务ID

        :return: The transaction_id of this DetailItem.
        :rtype: str
        """
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, transaction_id):
        """Sets the transaction_id of this DetailItem.

        事务ID

        :param transaction_id: The transaction_id of this DetailItem.
        :type transaction_id: str
        """
        self._transaction_id = transaction_id

    @property
    def aw_list(self):
        """Gets the aw_list of this DetailItem.

        aw列表

        :return: The aw_list of this DetailItem.
        :rtype: list[:class:`huaweicloudsdkcpts.v1.DetailItem`]
        """
        return self._aw_list

    @aw_list.setter
    def aw_list(self, aw_list):
        """Sets the aw_list of this DetailItem.

        aw列表

        :param aw_list: The aw_list of this DetailItem.
        :type aw_list: list[:class:`huaweicloudsdkcpts.v1.DetailItem`]
        """
        self._aw_list = aw_list

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
        if not isinstance(other, DetailItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
