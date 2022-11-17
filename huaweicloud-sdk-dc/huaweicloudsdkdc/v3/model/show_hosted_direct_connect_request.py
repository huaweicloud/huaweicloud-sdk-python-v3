# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowHostedDirectConnectRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'hosted_connect_id': 'str',
        'limit': 'int',
        'marker': 'str',
        'fields': 'list[str]',
        'sort_dir': 'list[str]',
        'sort_key': 'str',
        'hosting_id': 'list[str]'
    }

    attribute_map = {
        'hosted_connect_id': 'hosted_connect_id',
        'limit': 'limit',
        'marker': 'marker',
        'fields': 'fields',
        'sort_dir': 'sort_dir',
        'sort_key': 'sort_key',
        'hosting_id': 'hosting_id'
    }

    def __init__(self, hosted_connect_id=None, limit=None, marker=None, fields=None, sort_dir=None, sort_key=None, hosting_id=None):
        """ShowHostedDirectConnectRequest

        The model defined in huaweicloud sdk

        :param hosted_connect_id: 托管专线连接ID。
        :type hosted_connect_id: str
        :param limit: 每页返回的个数。 取值范围：1~2000。
        :type limit: int
        :param marker: 上一页最后一条资源记录的ID，为空时为查询第一页。 使用说明：必须与limit一起使用。
        :type marker: str
        :param fields: 显示字段列表
        :type fields: list[str]
        :param sort_dir: 返回结果按照升序(asc)或降序(desc)排列，默认为asc
        :type sort_dir: list[str]
        :param sort_key: 排序字段。
        :type sort_key: str
        :param hosting_id: 根椐运营专线ID过滤托管专线列表
        :type hosting_id: list[str]
        """
        
        

        self._hosted_connect_id = None
        self._limit = None
        self._marker = None
        self._fields = None
        self._sort_dir = None
        self._sort_key = None
        self._hosting_id = None
        self.discriminator = None

        self.hosted_connect_id = hosted_connect_id
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if fields is not None:
            self.fields = fields
        if sort_dir is not None:
            self.sort_dir = sort_dir
        if sort_key is not None:
            self.sort_key = sort_key
        if hosting_id is not None:
            self.hosting_id = hosting_id

    @property
    def hosted_connect_id(self):
        """Gets the hosted_connect_id of this ShowHostedDirectConnectRequest.

        托管专线连接ID。

        :return: The hosted_connect_id of this ShowHostedDirectConnectRequest.
        :rtype: str
        """
        return self._hosted_connect_id

    @hosted_connect_id.setter
    def hosted_connect_id(self, hosted_connect_id):
        """Sets the hosted_connect_id of this ShowHostedDirectConnectRequest.

        托管专线连接ID。

        :param hosted_connect_id: The hosted_connect_id of this ShowHostedDirectConnectRequest.
        :type hosted_connect_id: str
        """
        self._hosted_connect_id = hosted_connect_id

    @property
    def limit(self):
        """Gets the limit of this ShowHostedDirectConnectRequest.

        每页返回的个数。 取值范围：1~2000。

        :return: The limit of this ShowHostedDirectConnectRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ShowHostedDirectConnectRequest.

        每页返回的个数。 取值范围：1~2000。

        :param limit: The limit of this ShowHostedDirectConnectRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this ShowHostedDirectConnectRequest.

        上一页最后一条资源记录的ID，为空时为查询第一页。 使用说明：必须与limit一起使用。

        :return: The marker of this ShowHostedDirectConnectRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ShowHostedDirectConnectRequest.

        上一页最后一条资源记录的ID，为空时为查询第一页。 使用说明：必须与limit一起使用。

        :param marker: The marker of this ShowHostedDirectConnectRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def fields(self):
        """Gets the fields of this ShowHostedDirectConnectRequest.

        显示字段列表

        :return: The fields of this ShowHostedDirectConnectRequest.
        :rtype: list[str]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        """Sets the fields of this ShowHostedDirectConnectRequest.

        显示字段列表

        :param fields: The fields of this ShowHostedDirectConnectRequest.
        :type fields: list[str]
        """
        self._fields = fields

    @property
    def sort_dir(self):
        """Gets the sort_dir of this ShowHostedDirectConnectRequest.

        返回结果按照升序(asc)或降序(desc)排列，默认为asc

        :return: The sort_dir of this ShowHostedDirectConnectRequest.
        :rtype: list[str]
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        """Sets the sort_dir of this ShowHostedDirectConnectRequest.

        返回结果按照升序(asc)或降序(desc)排列，默认为asc

        :param sort_dir: The sort_dir of this ShowHostedDirectConnectRequest.
        :type sort_dir: list[str]
        """
        self._sort_dir = sort_dir

    @property
    def sort_key(self):
        """Gets the sort_key of this ShowHostedDirectConnectRequest.

        排序字段。

        :return: The sort_key of this ShowHostedDirectConnectRequest.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        """Sets the sort_key of this ShowHostedDirectConnectRequest.

        排序字段。

        :param sort_key: The sort_key of this ShowHostedDirectConnectRequest.
        :type sort_key: str
        """
        self._sort_key = sort_key

    @property
    def hosting_id(self):
        """Gets the hosting_id of this ShowHostedDirectConnectRequest.

        根椐运营专线ID过滤托管专线列表

        :return: The hosting_id of this ShowHostedDirectConnectRequest.
        :rtype: list[str]
        """
        return self._hosting_id

    @hosting_id.setter
    def hosting_id(self, hosting_id):
        """Sets the hosting_id of this ShowHostedDirectConnectRequest.

        根椐运营专线ID过滤托管专线列表

        :param hosting_id: The hosting_id of this ShowHostedDirectConnectRequest.
        :type hosting_id: list[str]
        """
        self._hosting_id = hosting_id

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
        if not isinstance(other, ShowHostedDirectConnectRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
