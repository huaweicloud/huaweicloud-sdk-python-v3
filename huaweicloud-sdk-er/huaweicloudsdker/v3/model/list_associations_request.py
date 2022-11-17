# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAssociationsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'er_id': 'str',
        'route_table_id': 'str',
        'limit': 'int',
        'marker': 'str',
        'attachment_id': 'list[str]',
        'resource_type': 'list[str]',
        'state': 'list[str]',
        'sort_key': 'list[str]',
        'sort_dir': 'list[str]'
    }

    attribute_map = {
        'er_id': 'er_id',
        'route_table_id': 'route_table_id',
        'limit': 'limit',
        'marker': 'marker',
        'attachment_id': 'attachment_id',
        'resource_type': 'resource_type',
        'state': 'state',
        'sort_key': 'sort_key',
        'sort_dir': 'sort_dir'
    }

    def __init__(self, er_id=None, route_table_id=None, limit=None, marker=None, attachment_id=None, resource_type=None, state=None, sort_key=None, sort_dir=None):
        """ListAssociationsRequest

        The model defined in huaweicloud sdk

        :param er_id: 企业路由器实例ID
        :type er_id: str
        :param route_table_id: 路由表ID
        :type route_table_id: str
        :param limit: 每页返回的个数。 取值范围：0~2000。
        :type limit: int
        :param marker: 上一页最后一条记录的企业路由器实例的id，为空时为查询第一页。 使用说明：必须与limit一起使用。
        :type marker: str
        :param attachment_id: 连接ID
        :type attachment_id: list[str]
        :param resource_type: 连接资源类型:vpc|vpn|vgw|peering|can|gdgw
        :type resource_type: list[str]
        :param state: 状态
        :type state: list[str]
        :param sort_key: 按关键字排序，默认按照id排序，可选值:id|name|state
        :type sort_key: list[str]
        :param sort_dir: 返回结果按照升序或降序排列，默认为asc,降序为desc
        :type sort_dir: list[str]
        """
        
        

        self._er_id = None
        self._route_table_id = None
        self._limit = None
        self._marker = None
        self._attachment_id = None
        self._resource_type = None
        self._state = None
        self._sort_key = None
        self._sort_dir = None
        self.discriminator = None

        self.er_id = er_id
        self.route_table_id = route_table_id
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if attachment_id is not None:
            self.attachment_id = attachment_id
        if resource_type is not None:
            self.resource_type = resource_type
        if state is not None:
            self.state = state
        if sort_key is not None:
            self.sort_key = sort_key
        if sort_dir is not None:
            self.sort_dir = sort_dir

    @property
    def er_id(self):
        """Gets the er_id of this ListAssociationsRequest.

        企业路由器实例ID

        :return: The er_id of this ListAssociationsRequest.
        :rtype: str
        """
        return self._er_id

    @er_id.setter
    def er_id(self, er_id):
        """Sets the er_id of this ListAssociationsRequest.

        企业路由器实例ID

        :param er_id: The er_id of this ListAssociationsRequest.
        :type er_id: str
        """
        self._er_id = er_id

    @property
    def route_table_id(self):
        """Gets the route_table_id of this ListAssociationsRequest.

        路由表ID

        :return: The route_table_id of this ListAssociationsRequest.
        :rtype: str
        """
        return self._route_table_id

    @route_table_id.setter
    def route_table_id(self, route_table_id):
        """Sets the route_table_id of this ListAssociationsRequest.

        路由表ID

        :param route_table_id: The route_table_id of this ListAssociationsRequest.
        :type route_table_id: str
        """
        self._route_table_id = route_table_id

    @property
    def limit(self):
        """Gets the limit of this ListAssociationsRequest.

        每页返回的个数。 取值范围：0~2000。

        :return: The limit of this ListAssociationsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListAssociationsRequest.

        每页返回的个数。 取值范围：0~2000。

        :param limit: The limit of this ListAssociationsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this ListAssociationsRequest.

        上一页最后一条记录的企业路由器实例的id，为空时为查询第一页。 使用说明：必须与limit一起使用。

        :return: The marker of this ListAssociationsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListAssociationsRequest.

        上一页最后一条记录的企业路由器实例的id，为空时为查询第一页。 使用说明：必须与limit一起使用。

        :param marker: The marker of this ListAssociationsRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def attachment_id(self):
        """Gets the attachment_id of this ListAssociationsRequest.

        连接ID

        :return: The attachment_id of this ListAssociationsRequest.
        :rtype: list[str]
        """
        return self._attachment_id

    @attachment_id.setter
    def attachment_id(self, attachment_id):
        """Sets the attachment_id of this ListAssociationsRequest.

        连接ID

        :param attachment_id: The attachment_id of this ListAssociationsRequest.
        :type attachment_id: list[str]
        """
        self._attachment_id = attachment_id

    @property
    def resource_type(self):
        """Gets the resource_type of this ListAssociationsRequest.

        连接资源类型:vpc|vpn|vgw|peering|can|gdgw

        :return: The resource_type of this ListAssociationsRequest.
        :rtype: list[str]
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this ListAssociationsRequest.

        连接资源类型:vpc|vpn|vgw|peering|can|gdgw

        :param resource_type: The resource_type of this ListAssociationsRequest.
        :type resource_type: list[str]
        """
        self._resource_type = resource_type

    @property
    def state(self):
        """Gets the state of this ListAssociationsRequest.

        状态

        :return: The state of this ListAssociationsRequest.
        :rtype: list[str]
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this ListAssociationsRequest.

        状态

        :param state: The state of this ListAssociationsRequest.
        :type state: list[str]
        """
        self._state = state

    @property
    def sort_key(self):
        """Gets the sort_key of this ListAssociationsRequest.

        按关键字排序，默认按照id排序，可选值:id|name|state

        :return: The sort_key of this ListAssociationsRequest.
        :rtype: list[str]
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        """Sets the sort_key of this ListAssociationsRequest.

        按关键字排序，默认按照id排序，可选值:id|name|state

        :param sort_key: The sort_key of this ListAssociationsRequest.
        :type sort_key: list[str]
        """
        self._sort_key = sort_key

    @property
    def sort_dir(self):
        """Gets the sort_dir of this ListAssociationsRequest.

        返回结果按照升序或降序排列，默认为asc,降序为desc

        :return: The sort_dir of this ListAssociationsRequest.
        :rtype: list[str]
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        """Sets the sort_dir of this ListAssociationsRequest.

        返回结果按照升序或降序排列，默认为asc,降序为desc

        :param sort_dir: The sort_dir of this ListAssociationsRequest.
        :type sort_dir: list[str]
        """
        self._sort_dir = sort_dir

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
        if not isinstance(other, ListAssociationsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
