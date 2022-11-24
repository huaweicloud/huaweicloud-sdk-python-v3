# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTransactionDetailResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tx_node_list': 'list[TxNode]',
        'tx_line_list': 'list[TxLine]'
    }

    attribute_map = {
        'tx_node_list': 'tx_node_list',
        'tx_line_list': 'tx_line_list'
    }

    def __init__(self, tx_node_list=None, tx_line_list=None):
        """ShowTransactionDetailResponse

        The model defined in huaweicloud sdk

        :param tx_node_list: 组件节点列表。
        :type tx_node_list: list[:class:`huaweicloudsdkapm.v1.TxNode`]
        :param tx_line_list: 组件之间调用指向线列表。
        :type tx_line_list: list[:class:`huaweicloudsdkapm.v1.TxLine`]
        """
        
        super(ShowTransactionDetailResponse, self).__init__()

        self._tx_node_list = None
        self._tx_line_list = None
        self.discriminator = None

        if tx_node_list is not None:
            self.tx_node_list = tx_node_list
        if tx_line_list is not None:
            self.tx_line_list = tx_line_list

    @property
    def tx_node_list(self):
        """Gets the tx_node_list of this ShowTransactionDetailResponse.

        组件节点列表。

        :return: The tx_node_list of this ShowTransactionDetailResponse.
        :rtype: list[:class:`huaweicloudsdkapm.v1.TxNode`]
        """
        return self._tx_node_list

    @tx_node_list.setter
    def tx_node_list(self, tx_node_list):
        """Sets the tx_node_list of this ShowTransactionDetailResponse.

        组件节点列表。

        :param tx_node_list: The tx_node_list of this ShowTransactionDetailResponse.
        :type tx_node_list: list[:class:`huaweicloudsdkapm.v1.TxNode`]
        """
        self._tx_node_list = tx_node_list

    @property
    def tx_line_list(self):
        """Gets the tx_line_list of this ShowTransactionDetailResponse.

        组件之间调用指向线列表。

        :return: The tx_line_list of this ShowTransactionDetailResponse.
        :rtype: list[:class:`huaweicloudsdkapm.v1.TxLine`]
        """
        return self._tx_line_list

    @tx_line_list.setter
    def tx_line_list(self, tx_line_list):
        """Sets the tx_line_list of this ShowTransactionDetailResponse.

        组件之间调用指向线列表。

        :param tx_line_list: The tx_line_list of this ShowTransactionDetailResponse.
        :type tx_line_list: list[:class:`huaweicloudsdkapm.v1.TxLine`]
        """
        self._tx_line_list = tx_line_list

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
        if not isinstance(other, ShowTransactionDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
