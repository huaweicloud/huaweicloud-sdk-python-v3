# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListNodeLimitSqlModelResponseResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sql_id': 'str',
        'sql_model': 'str'
    }

    attribute_map = {
        'sql_id': 'sql_id',
        'sql_model': 'sql_model'
    }

    def __init__(self, sql_id=None, sql_model=None):
        r"""ListNodeLimitSqlModelResponseResult

        The model defined in huaweicloud sdk

        :param sql_id: 限流任务SQL_ID。
        :type sql_id: str
        :param sql_model: 限流任务SQL模板。
        :type sql_model: str
        """
        
        

        self._sql_id = None
        self._sql_model = None
        self.discriminator = None

        if sql_id is not None:
            self.sql_id = sql_id
        if sql_model is not None:
            self.sql_model = sql_model

    @property
    def sql_id(self):
        r"""Gets the sql_id of this ListNodeLimitSqlModelResponseResult.

        限流任务SQL_ID。

        :return: The sql_id of this ListNodeLimitSqlModelResponseResult.
        :rtype: str
        """
        return self._sql_id

    @sql_id.setter
    def sql_id(self, sql_id):
        r"""Sets the sql_id of this ListNodeLimitSqlModelResponseResult.

        限流任务SQL_ID。

        :param sql_id: The sql_id of this ListNodeLimitSqlModelResponseResult.
        :type sql_id: str
        """
        self._sql_id = sql_id

    @property
    def sql_model(self):
        r"""Gets the sql_model of this ListNodeLimitSqlModelResponseResult.

        限流任务SQL模板。

        :return: The sql_model of this ListNodeLimitSqlModelResponseResult.
        :rtype: str
        """
        return self._sql_model

    @sql_model.setter
    def sql_model(self, sql_model):
        r"""Sets the sql_model of this ListNodeLimitSqlModelResponseResult.

        限流任务SQL模板。

        :param sql_model: The sql_model of this ListNodeLimitSqlModelResponseResult.
        :type sql_model: str
        """
        self._sql_model = sql_model

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
        if not isinstance(other, ListNodeLimitSqlModelResponseResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
