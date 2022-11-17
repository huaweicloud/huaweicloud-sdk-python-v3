# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteTableResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'table_id': 'str',
        'table_name': 'str'
    }

    attribute_map = {
        'table_id': 'table_id',
        'table_name': 'table_name'
    }

    def __init__(self, table_id=None, table_name=None):
        """DeleteTableResponse

        The model defined in huaweicloud sdk

        :param table_id: 被删除表ID
        :type table_id: str
        :param table_name: 被删除表名。
        :type table_name: str
        """
        
        super(DeleteTableResponse, self).__init__()

        self._table_id = None
        self._table_name = None
        self.discriminator = None

        if table_id is not None:
            self.table_id = table_id
        if table_name is not None:
            self.table_name = table_name

    @property
    def table_id(self):
        """Gets the table_id of this DeleteTableResponse.

        被删除表ID

        :return: The table_id of this DeleteTableResponse.
        :rtype: str
        """
        return self._table_id

    @table_id.setter
    def table_id(self, table_id):
        """Sets the table_id of this DeleteTableResponse.

        被删除表ID

        :param table_id: The table_id of this DeleteTableResponse.
        :type table_id: str
        """
        self._table_id = table_id

    @property
    def table_name(self):
        """Gets the table_name of this DeleteTableResponse.

        被删除表名。

        :return: The table_name of this DeleteTableResponse.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        """Sets the table_name of this DeleteTableResponse.

        被删除表名。

        :param table_name: The table_name of this DeleteTableResponse.
        :type table_name: str
        """
        self._table_name = table_name

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
        if not isinstance(other, DeleteTableResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
