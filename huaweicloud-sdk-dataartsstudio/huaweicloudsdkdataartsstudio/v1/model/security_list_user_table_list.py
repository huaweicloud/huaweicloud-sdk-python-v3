# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SecurityListUserTableList:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'table_list': 'list[SecurityListUserTableListTableList]',
        'proposer': 'SecurityListUserTableListProposer'
    }

    attribute_map = {
        'table_list': 'table_list',
        'proposer': 'proposer'
    }

    def __init__(self, table_list=None, proposer=None):
        r"""SecurityListUserTableList

        The model defined in huaweicloud sdk

        :param table_list: 需要查询的表
        :type table_list: list[:class:`huaweicloudsdkdataartsstudio.v1.SecurityListUserTableListTableList`]
        :param proposer: 
        :type proposer: :class:`huaweicloudsdkdataartsstudio.v1.SecurityListUserTableListProposer`
        """
        
        

        self._table_list = None
        self._proposer = None
        self.discriminator = None

        if table_list is not None:
            self.table_list = table_list
        self.proposer = proposer

    @property
    def table_list(self):
        r"""Gets the table_list of this SecurityListUserTableList.

        需要查询的表

        :return: The table_list of this SecurityListUserTableList.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.SecurityListUserTableListTableList`]
        """
        return self._table_list

    @table_list.setter
    def table_list(self, table_list):
        r"""Sets the table_list of this SecurityListUserTableList.

        需要查询的表

        :param table_list: The table_list of this SecurityListUserTableList.
        :type table_list: list[:class:`huaweicloudsdkdataartsstudio.v1.SecurityListUserTableListTableList`]
        """
        self._table_list = table_list

    @property
    def proposer(self):
        r"""Gets the proposer of this SecurityListUserTableList.

        :return: The proposer of this SecurityListUserTableList.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.SecurityListUserTableListProposer`
        """
        return self._proposer

    @proposer.setter
    def proposer(self, proposer):
        r"""Sets the proposer of this SecurityListUserTableList.

        :param proposer: The proposer of this SecurityListUserTableList.
        :type proposer: :class:`huaweicloudsdkdataartsstudio.v1.SecurityListUserTableListProposer`
        """
        self._proposer = proposer

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
        if not isinstance(other, SecurityListUserTableList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
