# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPublishedAppRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'app_group_id': 'str',
        'limit': 'int',
        'offset': 'int',
        'name': 'str',
        'state': 'str',
        'app_id': 'str'
    }

    attribute_map = {
        'app_group_id': 'app_group_id',
        'limit': 'limit',
        'offset': 'offset',
        'name': 'name',
        'state': 'state',
        'app_id': 'app_id'
    }

    def __init__(self, app_group_id=None, limit=None, offset=None, name=None, state=None, app_id=None):
        """ListPublishedAppRequest

        The model defined in huaweicloud sdk

        :param app_group_id: 应用组ID
        :type app_group_id: str
        :param limit: 单次查询的大小[1-100]
        :type limit: int
        :param offset: 查询的偏移量
        :type offset: int
        :param name: 应用名称
        :type name: str
        :param state: 应用状态正常、禁用(NORMAL、FORBIDDEN)
        :type state: str
        :param app_id: 应用ID
        :type app_id: str
        """
        
        

        self._app_group_id = None
        self._limit = None
        self._offset = None
        self._name = None
        self._state = None
        self._app_id = None
        self.discriminator = None

        self.app_group_id = app_group_id
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if name is not None:
            self.name = name
        if state is not None:
            self.state = state
        if app_id is not None:
            self.app_id = app_id

    @property
    def app_group_id(self):
        """Gets the app_group_id of this ListPublishedAppRequest.

        应用组ID

        :return: The app_group_id of this ListPublishedAppRequest.
        :rtype: str
        """
        return self._app_group_id

    @app_group_id.setter
    def app_group_id(self, app_group_id):
        """Sets the app_group_id of this ListPublishedAppRequest.

        应用组ID

        :param app_group_id: The app_group_id of this ListPublishedAppRequest.
        :type app_group_id: str
        """
        self._app_group_id = app_group_id

    @property
    def limit(self):
        """Gets the limit of this ListPublishedAppRequest.

        单次查询的大小[1-100]

        :return: The limit of this ListPublishedAppRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListPublishedAppRequest.

        单次查询的大小[1-100]

        :param limit: The limit of this ListPublishedAppRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListPublishedAppRequest.

        查询的偏移量

        :return: The offset of this ListPublishedAppRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListPublishedAppRequest.

        查询的偏移量

        :param offset: The offset of this ListPublishedAppRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def name(self):
        """Gets the name of this ListPublishedAppRequest.

        应用名称

        :return: The name of this ListPublishedAppRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListPublishedAppRequest.

        应用名称

        :param name: The name of this ListPublishedAppRequest.
        :type name: str
        """
        self._name = name

    @property
    def state(self):
        """Gets the state of this ListPublishedAppRequest.

        应用状态正常、禁用(NORMAL、FORBIDDEN)

        :return: The state of this ListPublishedAppRequest.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this ListPublishedAppRequest.

        应用状态正常、禁用(NORMAL、FORBIDDEN)

        :param state: The state of this ListPublishedAppRequest.
        :type state: str
        """
        self._state = state

    @property
    def app_id(self):
        """Gets the app_id of this ListPublishedAppRequest.

        应用ID

        :return: The app_id of this ListPublishedAppRequest.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this ListPublishedAppRequest.

        应用ID

        :param app_id: The app_id of this ListPublishedAppRequest.
        :type app_id: str
        """
        self._app_id = app_id

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
        if not isinstance(other, ListPublishedAppRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
