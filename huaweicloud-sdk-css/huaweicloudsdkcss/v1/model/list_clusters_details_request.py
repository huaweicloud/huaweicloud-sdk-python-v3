# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListClustersDetailsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'offset': 'int',
        'limit': 'int',
        'datastore_type': 'str'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'datastore_type': 'datastoreType'
    }

    def __init__(self, offset=None, limit=None, datastore_type=None):
        r"""ListClustersDetailsRequest

        The model defined in huaweicloud sdk

        :param offset: 指定查询起始值，默认值为1，即从第1个集群开始查询。
        :type offset: int
        :param limit: 指定查询个数，默认值为10，即一次查询10个集群信息。
        :type limit: int
        :param datastore_type: 指定查询的集群引擎类型。
        :type datastore_type: str
        """
        
        

        self._offset = None
        self._limit = None
        self._datastore_type = None
        self.discriminator = None

        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if datastore_type is not None:
            self.datastore_type = datastore_type

    @property
    def offset(self):
        r"""Gets the offset of this ListClustersDetailsRequest.

        指定查询起始值，默认值为1，即从第1个集群开始查询。

        :return: The offset of this ListClustersDetailsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListClustersDetailsRequest.

        指定查询起始值，默认值为1，即从第1个集群开始查询。

        :param offset: The offset of this ListClustersDetailsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListClustersDetailsRequest.

        指定查询个数，默认值为10，即一次查询10个集群信息。

        :return: The limit of this ListClustersDetailsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListClustersDetailsRequest.

        指定查询个数，默认值为10，即一次查询10个集群信息。

        :param limit: The limit of this ListClustersDetailsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def datastore_type(self):
        r"""Gets the datastore_type of this ListClustersDetailsRequest.

        指定查询的集群引擎类型。

        :return: The datastore_type of this ListClustersDetailsRequest.
        :rtype: str
        """
        return self._datastore_type

    @datastore_type.setter
    def datastore_type(self, datastore_type):
        r"""Sets the datastore_type of this ListClustersDetailsRequest.

        指定查询的集群引擎类型。

        :param datastore_type: The datastore_type of this ListClustersDetailsRequest.
        :type datastore_type: str
        """
        self._datastore_type = datastore_type

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
        if not isinstance(other, ListClustersDetailsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
