# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListVpcAttachmentsRequest:

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
        'limit': 'int',
        'marker': 'str',
        'state': 'list[str]',
        'id': 'list[str]',
        'sort_key': 'list[str]',
        'sort_dir': 'list[str]',
        'vpc_id': 'list[str]'
    }

    attribute_map = {
        'er_id': 'er_id',
        'limit': 'limit',
        'marker': 'marker',
        'state': 'state',
        'id': 'id',
        'sort_key': 'sort_key',
        'sort_dir': 'sort_dir',
        'vpc_id': 'vpc_id'
    }

    def __init__(self, er_id=None, limit=None, marker=None, state=None, id=None, sort_key=None, sort_dir=None, vpc_id=None):
        """ListVpcAttachmentsRequest

        The model defined in huaweicloud sdk

        :param er_id: 企业路由器实例ID
        :type er_id: str
        :param limit: 每页返回的个数。 取值范围：0~2000。
        :type limit: int
        :param marker: 上一页最后一条记录的企业路由器实例的id，为空时为查询第一页。 使用说明：必须与limit一起使用。
        :type marker: str
        :param state: 连接状态:pending|available|modifying|deleting|deleted|failed|pending_acceptance|rejected|initiating_request
        :type state: list[str]
        :param id: 根据资源ID查询，可同时查询多个。
        :type id: list[str]
        :param sort_key: 按关键字排序，默认按照id排序，可选值:id|name|state
        :type sort_key: list[str]
        :param sort_dir: 返回结果按照升序或降序排列，默认为asc,降序为desc
        :type sort_dir: list[str]
        :param vpc_id: VPC id
        :type vpc_id: list[str]
        """
        
        

        self._er_id = None
        self._limit = None
        self._marker = None
        self._state = None
        self._id = None
        self._sort_key = None
        self._sort_dir = None
        self._vpc_id = None
        self.discriminator = None

        self.er_id = er_id
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if state is not None:
            self.state = state
        if id is not None:
            self.id = id
        if sort_key is not None:
            self.sort_key = sort_key
        if sort_dir is not None:
            self.sort_dir = sort_dir
        if vpc_id is not None:
            self.vpc_id = vpc_id

    @property
    def er_id(self):
        """Gets the er_id of this ListVpcAttachmentsRequest.

        企业路由器实例ID

        :return: The er_id of this ListVpcAttachmentsRequest.
        :rtype: str
        """
        return self._er_id

    @er_id.setter
    def er_id(self, er_id):
        """Sets the er_id of this ListVpcAttachmentsRequest.

        企业路由器实例ID

        :param er_id: The er_id of this ListVpcAttachmentsRequest.
        :type er_id: str
        """
        self._er_id = er_id

    @property
    def limit(self):
        """Gets the limit of this ListVpcAttachmentsRequest.

        每页返回的个数。 取值范围：0~2000。

        :return: The limit of this ListVpcAttachmentsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListVpcAttachmentsRequest.

        每页返回的个数。 取值范围：0~2000。

        :param limit: The limit of this ListVpcAttachmentsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this ListVpcAttachmentsRequest.

        上一页最后一条记录的企业路由器实例的id，为空时为查询第一页。 使用说明：必须与limit一起使用。

        :return: The marker of this ListVpcAttachmentsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListVpcAttachmentsRequest.

        上一页最后一条记录的企业路由器实例的id，为空时为查询第一页。 使用说明：必须与limit一起使用。

        :param marker: The marker of this ListVpcAttachmentsRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def state(self):
        """Gets the state of this ListVpcAttachmentsRequest.

        连接状态:pending|available|modifying|deleting|deleted|failed|pending_acceptance|rejected|initiating_request

        :return: The state of this ListVpcAttachmentsRequest.
        :rtype: list[str]
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this ListVpcAttachmentsRequest.

        连接状态:pending|available|modifying|deleting|deleted|failed|pending_acceptance|rejected|initiating_request

        :param state: The state of this ListVpcAttachmentsRequest.
        :type state: list[str]
        """
        self._state = state

    @property
    def id(self):
        """Gets the id of this ListVpcAttachmentsRequest.

        根据资源ID查询，可同时查询多个。

        :return: The id of this ListVpcAttachmentsRequest.
        :rtype: list[str]
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListVpcAttachmentsRequest.

        根据资源ID查询，可同时查询多个。

        :param id: The id of this ListVpcAttachmentsRequest.
        :type id: list[str]
        """
        self._id = id

    @property
    def sort_key(self):
        """Gets the sort_key of this ListVpcAttachmentsRequest.

        按关键字排序，默认按照id排序，可选值:id|name|state

        :return: The sort_key of this ListVpcAttachmentsRequest.
        :rtype: list[str]
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        """Sets the sort_key of this ListVpcAttachmentsRequest.

        按关键字排序，默认按照id排序，可选值:id|name|state

        :param sort_key: The sort_key of this ListVpcAttachmentsRequest.
        :type sort_key: list[str]
        """
        self._sort_key = sort_key

    @property
    def sort_dir(self):
        """Gets the sort_dir of this ListVpcAttachmentsRequest.

        返回结果按照升序或降序排列，默认为asc,降序为desc

        :return: The sort_dir of this ListVpcAttachmentsRequest.
        :rtype: list[str]
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        """Sets the sort_dir of this ListVpcAttachmentsRequest.

        返回结果按照升序或降序排列，默认为asc,降序为desc

        :param sort_dir: The sort_dir of this ListVpcAttachmentsRequest.
        :type sort_dir: list[str]
        """
        self._sort_dir = sort_dir

    @property
    def vpc_id(self):
        """Gets the vpc_id of this ListVpcAttachmentsRequest.

        VPC id

        :return: The vpc_id of this ListVpcAttachmentsRequest.
        :rtype: list[str]
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this ListVpcAttachmentsRequest.

        VPC id

        :param vpc_id: The vpc_id of this ListVpcAttachmentsRequest.
        :type vpc_id: list[str]
        """
        self._vpc_id = vpc_id

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
        if not isinstance(other, ListVpcAttachmentsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other