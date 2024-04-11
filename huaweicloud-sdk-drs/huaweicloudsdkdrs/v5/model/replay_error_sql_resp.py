# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ReplayErrorSqlResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'object_type': 'str',
        'abnormal_sql': 'str',
        'abnormal_info': 'str'
    }

    attribute_map = {
        'object_type': 'object_type',
        'abnormal_sql': 'abnormal_sql',
        'abnormal_info': 'abnormal_info'
    }

    def __init__(self, object_type=None, abnormal_sql=None, abnormal_info=None):
        """ReplayErrorSqlResp

        The model defined in huaweicloud sdk

        :param object_type: SQL类型
        :type object_type: str
        :param abnormal_sql: SQL语句
        :type abnormal_sql: str
        :param abnormal_info: 异常原因描述
        :type abnormal_info: str
        """
        
        

        self._object_type = None
        self._abnormal_sql = None
        self._abnormal_info = None
        self.discriminator = None

        if object_type is not None:
            self.object_type = object_type
        if abnormal_sql is not None:
            self.abnormal_sql = abnormal_sql
        if abnormal_info is not None:
            self.abnormal_info = abnormal_info

    @property
    def object_type(self):
        """Gets the object_type of this ReplayErrorSqlResp.

        SQL类型

        :return: The object_type of this ReplayErrorSqlResp.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """Sets the object_type of this ReplayErrorSqlResp.

        SQL类型

        :param object_type: The object_type of this ReplayErrorSqlResp.
        :type object_type: str
        """
        self._object_type = object_type

    @property
    def abnormal_sql(self):
        """Gets the abnormal_sql of this ReplayErrorSqlResp.

        SQL语句

        :return: The abnormal_sql of this ReplayErrorSqlResp.
        :rtype: str
        """
        return self._abnormal_sql

    @abnormal_sql.setter
    def abnormal_sql(self, abnormal_sql):
        """Sets the abnormal_sql of this ReplayErrorSqlResp.

        SQL语句

        :param abnormal_sql: The abnormal_sql of this ReplayErrorSqlResp.
        :type abnormal_sql: str
        """
        self._abnormal_sql = abnormal_sql

    @property
    def abnormal_info(self):
        """Gets the abnormal_info of this ReplayErrorSqlResp.

        异常原因描述

        :return: The abnormal_info of this ReplayErrorSqlResp.
        :rtype: str
        """
        return self._abnormal_info

    @abnormal_info.setter
    def abnormal_info(self, abnormal_info):
        """Sets the abnormal_info of this ReplayErrorSqlResp.

        异常原因描述

        :param abnormal_info: The abnormal_info of this ReplayErrorSqlResp.
        :type abnormal_info: str
        """
        self._abnormal_info = abnormal_info

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
        if not isinstance(other, ReplayErrorSqlResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
