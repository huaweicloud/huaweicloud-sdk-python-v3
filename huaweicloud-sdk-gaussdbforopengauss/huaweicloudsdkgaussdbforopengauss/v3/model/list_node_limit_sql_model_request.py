# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListNodeLimitSqlModelRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'node_id': 'str',
        'sql_model': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'node_id': 'node_id',
        'sql_model': 'sql_model',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, instance_id=None, node_id=None, sql_model=None, offset=None, limit=None):
        r"""ListNodeLimitSqlModelRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID。
        :type instance_id: str
        :param node_id: 节点id。
        :type node_id: str
        :param sql_model: sql模板。
        :type sql_model: str
        :param offset: 索引位置，偏移量。从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。  取值范围：0 - 10000
        :type offset: int
        :param limit: 查询记录数。默认为10，不能为负数，最小值为1，最大值为100。
        :type limit: int
        """
        
        

        self._instance_id = None
        self._node_id = None
        self._sql_model = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.instance_id = instance_id
        self.node_id = node_id
        if sql_model is not None:
            self.sql_model = sql_model
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListNodeLimitSqlModelRequest.

        实例ID。

        :return: The instance_id of this ListNodeLimitSqlModelRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListNodeLimitSqlModelRequest.

        实例ID。

        :param instance_id: The instance_id of this ListNodeLimitSqlModelRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def node_id(self):
        r"""Gets the node_id of this ListNodeLimitSqlModelRequest.

        节点id。

        :return: The node_id of this ListNodeLimitSqlModelRequest.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this ListNodeLimitSqlModelRequest.

        节点id。

        :param node_id: The node_id of this ListNodeLimitSqlModelRequest.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def sql_model(self):
        r"""Gets the sql_model of this ListNodeLimitSqlModelRequest.

        sql模板。

        :return: The sql_model of this ListNodeLimitSqlModelRequest.
        :rtype: str
        """
        return self._sql_model

    @sql_model.setter
    def sql_model(self, sql_model):
        r"""Sets the sql_model of this ListNodeLimitSqlModelRequest.

        sql模板。

        :param sql_model: The sql_model of this ListNodeLimitSqlModelRequest.
        :type sql_model: str
        """
        self._sql_model = sql_model

    @property
    def offset(self):
        r"""Gets the offset of this ListNodeLimitSqlModelRequest.

        索引位置，偏移量。从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。  取值范围：0 - 10000

        :return: The offset of this ListNodeLimitSqlModelRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListNodeLimitSqlModelRequest.

        索引位置，偏移量。从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。  取值范围：0 - 10000

        :param offset: The offset of this ListNodeLimitSqlModelRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListNodeLimitSqlModelRequest.

        查询记录数。默认为10，不能为负数，最小值为1，最大值为100。

        :return: The limit of this ListNodeLimitSqlModelRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListNodeLimitSqlModelRequest.

        查询记录数。默认为10，不能为负数，最小值为1，最大值为100。

        :param limit: The limit of this ListNodeLimitSqlModelRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListNodeLimitSqlModelRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
