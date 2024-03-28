# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCentralNetworkErRouteTableAttachmentsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'limit': 'int',
        'marker': 'str',
        'sort_key': 'str',
        'sort_dir': 'SortDir',
        'id': 'list[str]',
        'name': 'list[str]',
        'state': 'list[CentralNetworkConnectionStateEnum]',
        'central_network_id': 'str',
        'attachment_instance_id': 'list[str]'
    }

    attribute_map = {
        'limit': 'limit',
        'marker': 'marker',
        'sort_key': 'sort_key',
        'sort_dir': 'sort_dir',
        'id': 'id',
        'name': 'name',
        'state': 'state',
        'central_network_id': 'central_network_id',
        'attachment_instance_id': 'attachment_instance_id'
    }

    def __init__(self, limit=None, marker=None, sort_key=None, sort_dir=None, id=None, name=None, state=None, central_network_id=None, attachment_instance_id=None):
        """ListCentralNetworkErRouteTableAttachmentsRequest

        The model defined in huaweicloud sdk

        :param limit: 每页返回的个数。 取值范围：1~1000。
        :type limit: int
        :param marker: 翻页信息，从上次API调用返回的翻页数据中获取，可填写前一页marker或者后一页marker，填入前一页previous_marker就向前翻页，后一页next_marker就向翻页。 翻页过程中，查询条件不能修改，包括过滤条件，排序条件，limit。
        :type marker: str
        :param sort_key: 排序字段。
        :type sort_key: str
        :param sort_dir: 指定排序是升序还是降序(asc为升序，desc为降序)。
        :type sort_dir: :class:`huaweicloudsdkcc.v3.SortDir`
        :param id: 根据id查询，可查询多个id。
        :type id: list[str]
        :param name: 根据名字查询，可查询多个名字。
        :type name: list[str]
        :param state: 根据状态查询，可查询多个状态。
        :type state: list[:class:`huaweicloudsdkcc.v3.CentralNetworkConnectionStateEnum`]
        :param central_network_id: 中心网络的ID。
        :type central_network_id: str
        :param attachment_instance_id: Attachment实例的ID。
        :type attachment_instance_id: list[str]
        """
        
        

        self._limit = None
        self._marker = None
        self._sort_key = None
        self._sort_dir = None
        self._id = None
        self._name = None
        self._state = None
        self._central_network_id = None
        self._attachment_instance_id = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if sort_key is not None:
            self.sort_key = sort_key
        if sort_dir is not None:
            self.sort_dir = sort_dir
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if state is not None:
            self.state = state
        self.central_network_id = central_network_id
        if attachment_instance_id is not None:
            self.attachment_instance_id = attachment_instance_id

    @property
    def limit(self):
        """Gets the limit of this ListCentralNetworkErRouteTableAttachmentsRequest.

        每页返回的个数。 取值范围：1~1000。

        :return: The limit of this ListCentralNetworkErRouteTableAttachmentsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListCentralNetworkErRouteTableAttachmentsRequest.

        每页返回的个数。 取值范围：1~1000。

        :param limit: The limit of this ListCentralNetworkErRouteTableAttachmentsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this ListCentralNetworkErRouteTableAttachmentsRequest.

        翻页信息，从上次API调用返回的翻页数据中获取，可填写前一页marker或者后一页marker，填入前一页previous_marker就向前翻页，后一页next_marker就向翻页。 翻页过程中，查询条件不能修改，包括过滤条件，排序条件，limit。

        :return: The marker of this ListCentralNetworkErRouteTableAttachmentsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListCentralNetworkErRouteTableAttachmentsRequest.

        翻页信息，从上次API调用返回的翻页数据中获取，可填写前一页marker或者后一页marker，填入前一页previous_marker就向前翻页，后一页next_marker就向翻页。 翻页过程中，查询条件不能修改，包括过滤条件，排序条件，limit。

        :param marker: The marker of this ListCentralNetworkErRouteTableAttachmentsRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def sort_key(self):
        """Gets the sort_key of this ListCentralNetworkErRouteTableAttachmentsRequest.

        排序字段。

        :return: The sort_key of this ListCentralNetworkErRouteTableAttachmentsRequest.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        """Sets the sort_key of this ListCentralNetworkErRouteTableAttachmentsRequest.

        排序字段。

        :param sort_key: The sort_key of this ListCentralNetworkErRouteTableAttachmentsRequest.
        :type sort_key: str
        """
        self._sort_key = sort_key

    @property
    def sort_dir(self):
        """Gets the sort_dir of this ListCentralNetworkErRouteTableAttachmentsRequest.

        指定排序是升序还是降序(asc为升序，desc为降序)。

        :return: The sort_dir of this ListCentralNetworkErRouteTableAttachmentsRequest.
        :rtype: :class:`huaweicloudsdkcc.v3.SortDir`
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        """Sets the sort_dir of this ListCentralNetworkErRouteTableAttachmentsRequest.

        指定排序是升序还是降序(asc为升序，desc为降序)。

        :param sort_dir: The sort_dir of this ListCentralNetworkErRouteTableAttachmentsRequest.
        :type sort_dir: :class:`huaweicloudsdkcc.v3.SortDir`
        """
        self._sort_dir = sort_dir

    @property
    def id(self):
        """Gets the id of this ListCentralNetworkErRouteTableAttachmentsRequest.

        根据id查询，可查询多个id。

        :return: The id of this ListCentralNetworkErRouteTableAttachmentsRequest.
        :rtype: list[str]
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListCentralNetworkErRouteTableAttachmentsRequest.

        根据id查询，可查询多个id。

        :param id: The id of this ListCentralNetworkErRouteTableAttachmentsRequest.
        :type id: list[str]
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ListCentralNetworkErRouteTableAttachmentsRequest.

        根据名字查询，可查询多个名字。

        :return: The name of this ListCentralNetworkErRouteTableAttachmentsRequest.
        :rtype: list[str]
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListCentralNetworkErRouteTableAttachmentsRequest.

        根据名字查询，可查询多个名字。

        :param name: The name of this ListCentralNetworkErRouteTableAttachmentsRequest.
        :type name: list[str]
        """
        self._name = name

    @property
    def state(self):
        """Gets the state of this ListCentralNetworkErRouteTableAttachmentsRequest.

        根据状态查询，可查询多个状态。

        :return: The state of this ListCentralNetworkErRouteTableAttachmentsRequest.
        :rtype: list[:class:`huaweicloudsdkcc.v3.CentralNetworkConnectionStateEnum`]
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this ListCentralNetworkErRouteTableAttachmentsRequest.

        根据状态查询，可查询多个状态。

        :param state: The state of this ListCentralNetworkErRouteTableAttachmentsRequest.
        :type state: list[:class:`huaweicloudsdkcc.v3.CentralNetworkConnectionStateEnum`]
        """
        self._state = state

    @property
    def central_network_id(self):
        """Gets the central_network_id of this ListCentralNetworkErRouteTableAttachmentsRequest.

        中心网络的ID。

        :return: The central_network_id of this ListCentralNetworkErRouteTableAttachmentsRequest.
        :rtype: str
        """
        return self._central_network_id

    @central_network_id.setter
    def central_network_id(self, central_network_id):
        """Sets the central_network_id of this ListCentralNetworkErRouteTableAttachmentsRequest.

        中心网络的ID。

        :param central_network_id: The central_network_id of this ListCentralNetworkErRouteTableAttachmentsRequest.
        :type central_network_id: str
        """
        self._central_network_id = central_network_id

    @property
    def attachment_instance_id(self):
        """Gets the attachment_instance_id of this ListCentralNetworkErRouteTableAttachmentsRequest.

        Attachment实例的ID。

        :return: The attachment_instance_id of this ListCentralNetworkErRouteTableAttachmentsRequest.
        :rtype: list[str]
        """
        return self._attachment_instance_id

    @attachment_instance_id.setter
    def attachment_instance_id(self, attachment_instance_id):
        """Sets the attachment_instance_id of this ListCentralNetworkErRouteTableAttachmentsRequest.

        Attachment实例的ID。

        :param attachment_instance_id: The attachment_instance_id of this ListCentralNetworkErRouteTableAttachmentsRequest.
        :type attachment_instance_id: list[str]
        """
        self._attachment_instance_id = attachment_instance_id

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
        if not isinstance(other, ListCentralNetworkErRouteTableAttachmentsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
