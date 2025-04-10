# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TableInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'table_status': 'str'
    }

    attribute_map = {
        'table_status': 'table_status'
    }

    def __init__(self, table_status=None):
        r"""TableInfo

        The model defined in huaweicloud sdk

        :param table_status: 表状态。 - \&quot;creating\&quot; - \&quot;active\&quot; - \&quot;deleting\&quot;
        :type table_status: str
        """
        
        

        self._table_status = None
        self.discriminator = None

        if table_status is not None:
            self.table_status = table_status

    @property
    def table_status(self):
        r"""Gets the table_status of this TableInfo.

        表状态。 - \"creating\" - \"active\" - \"deleting\"

        :return: The table_status of this TableInfo.
        :rtype: str
        """
        return self._table_status

    @table_status.setter
    def table_status(self, table_status):
        r"""Sets the table_status of this TableInfo.

        表状态。 - \"creating\" - \"active\" - \"deleting\"

        :param table_status: The table_status of this TableInfo.
        :type table_status: str
        """
        self._table_status = table_status

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
        if not isinstance(other, TableInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
