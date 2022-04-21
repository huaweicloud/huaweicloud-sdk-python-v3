# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CancelSqlRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'cluster_id': 'str',
        'sql_id': 'str'
    }

    attribute_map = {
        'cluster_id': 'cluster_id',
        'sql_id': 'sql_id'
    }

    def __init__(self, cluster_id=None, sql_id=None):
        """CancelSqlRequest

        The model defined in huaweicloud sdk

        :param cluster_id: 集群ID。获取方法，请参见[获取集群ID](https://support.huaweicloud.com/api-mrs/mrs_02_9001.html)。
        :type cluster_id: str
        :param sql_id: SQL的执行ID，即提交SQL语句返回结果中的sql_id。
        :type sql_id: str
        """
        
        

        self._cluster_id = None
        self._sql_id = None
        self.discriminator = None

        self.cluster_id = cluster_id
        self.sql_id = sql_id

    @property
    def cluster_id(self):
        """Gets the cluster_id of this CancelSqlRequest.

        集群ID。获取方法，请参见[获取集群ID](https://support.huaweicloud.com/api-mrs/mrs_02_9001.html)。

        :return: The cluster_id of this CancelSqlRequest.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this CancelSqlRequest.

        集群ID。获取方法，请参见[获取集群ID](https://support.huaweicloud.com/api-mrs/mrs_02_9001.html)。

        :param cluster_id: The cluster_id of this CancelSqlRequest.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def sql_id(self):
        """Gets the sql_id of this CancelSqlRequest.

        SQL的执行ID，即提交SQL语句返回结果中的sql_id。

        :return: The sql_id of this CancelSqlRequest.
        :rtype: str
        """
        return self._sql_id

    @sql_id.setter
    def sql_id(self, sql_id):
        """Sets the sql_id of this CancelSqlRequest.

        SQL的执行ID，即提交SQL语句返回结果中的sql_id。

        :param sql_id: The sql_id of this CancelSqlRequest.
        :type sql_id: str
        """
        self._sql_id = sql_id

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
        if not isinstance(other, CancelSqlRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
