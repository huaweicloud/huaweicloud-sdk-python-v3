# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowListOfEventSampleRequest:

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
        'sort': 'str',
        'name': 'str',
        'event_type_name': 'str',
        'event_source_id': 'str'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'sort': 'sort',
        'name': 'name',
        'event_type_name': 'event_type_name',
        'event_source_id': 'event_source_id'
    }

    def __init__(self, offset=None, limit=None, sort=None, name=None, event_type_name=None, event_source_id=None):
        r"""ShowListOfEventSampleRequest

        The model defined in huaweicloud sdk

        :param offset: 偏移量，表示从此偏移量开始查询，偏移量不能小于0
        :type offset: int
        :param limit: 每页显示的条目数量，不能小于1或大于1000
        :type limit: int
        :param sort: 指定查询排序
        :type sort: str
        :param name: 指定查询的事件示例名称，模糊匹配
        :type name: str
        :param event_type_name: 指定查询事件示例的事件类型名称
        :type event_type_name: str
        :param event_source_id: 指定查询事件示例的事件源
        :type event_source_id: str
        """
        
        

        self._offset = None
        self._limit = None
        self._sort = None
        self._name = None
        self._event_type_name = None
        self._event_source_id = None
        self.discriminator = None

        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if sort is not None:
            self.sort = sort
        if name is not None:
            self.name = name
        if event_type_name is not None:
            self.event_type_name = event_type_name
        if event_source_id is not None:
            self.event_source_id = event_source_id

    @property
    def offset(self):
        r"""Gets the offset of this ShowListOfEventSampleRequest.

        偏移量，表示从此偏移量开始查询，偏移量不能小于0

        :return: The offset of this ShowListOfEventSampleRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ShowListOfEventSampleRequest.

        偏移量，表示从此偏移量开始查询，偏移量不能小于0

        :param offset: The offset of this ShowListOfEventSampleRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ShowListOfEventSampleRequest.

        每页显示的条目数量，不能小于1或大于1000

        :return: The limit of this ShowListOfEventSampleRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ShowListOfEventSampleRequest.

        每页显示的条目数量，不能小于1或大于1000

        :param limit: The limit of this ShowListOfEventSampleRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def sort(self):
        r"""Gets the sort of this ShowListOfEventSampleRequest.

        指定查询排序

        :return: The sort of this ShowListOfEventSampleRequest.
        :rtype: str
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        r"""Sets the sort of this ShowListOfEventSampleRequest.

        指定查询排序

        :param sort: The sort of this ShowListOfEventSampleRequest.
        :type sort: str
        """
        self._sort = sort

    @property
    def name(self):
        r"""Gets the name of this ShowListOfEventSampleRequest.

        指定查询的事件示例名称，模糊匹配

        :return: The name of this ShowListOfEventSampleRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowListOfEventSampleRequest.

        指定查询的事件示例名称，模糊匹配

        :param name: The name of this ShowListOfEventSampleRequest.
        :type name: str
        """
        self._name = name

    @property
    def event_type_name(self):
        r"""Gets the event_type_name of this ShowListOfEventSampleRequest.

        指定查询事件示例的事件类型名称

        :return: The event_type_name of this ShowListOfEventSampleRequest.
        :rtype: str
        """
        return self._event_type_name

    @event_type_name.setter
    def event_type_name(self, event_type_name):
        r"""Sets the event_type_name of this ShowListOfEventSampleRequest.

        指定查询事件示例的事件类型名称

        :param event_type_name: The event_type_name of this ShowListOfEventSampleRequest.
        :type event_type_name: str
        """
        self._event_type_name = event_type_name

    @property
    def event_source_id(self):
        r"""Gets the event_source_id of this ShowListOfEventSampleRequest.

        指定查询事件示例的事件源

        :return: The event_source_id of this ShowListOfEventSampleRequest.
        :rtype: str
        """
        return self._event_source_id

    @event_source_id.setter
    def event_source_id(self, event_source_id):
        r"""Sets the event_source_id of this ShowListOfEventSampleRequest.

        指定查询事件示例的事件源

        :param event_source_id: The event_source_id of this ShowListOfEventSampleRequest.
        :type event_source_id: str
        """
        self._event_source_id = event_source_id

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
        if not isinstance(other, ShowListOfEventSampleRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
