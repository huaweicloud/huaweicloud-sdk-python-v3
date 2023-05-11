# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListEventsResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'last_modified': 'float',
        'name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'last_modified': 'last_modified',
        'name': 'name'
    }

    def __init__(self, id=None, last_modified=None, name=None):
        """ListEventsResult

        The model defined in huaweicloud sdk

        :param id: 测试事件ID。
        :type id: str
        :param last_modified: 上次修改的时间。
        :type last_modified: float
        :param name: 测试事件名称。
        :type name: str
        """
        
        

        self._id = None
        self._last_modified = None
        self._name = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if last_modified is not None:
            self.last_modified = last_modified
        if name is not None:
            self.name = name

    @property
    def id(self):
        """Gets the id of this ListEventsResult.

        测试事件ID。

        :return: The id of this ListEventsResult.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListEventsResult.

        测试事件ID。

        :param id: The id of this ListEventsResult.
        :type id: str
        """
        self._id = id

    @property
    def last_modified(self):
        """Gets the last_modified of this ListEventsResult.

        上次修改的时间。

        :return: The last_modified of this ListEventsResult.
        :rtype: float
        """
        return self._last_modified

    @last_modified.setter
    def last_modified(self, last_modified):
        """Sets the last_modified of this ListEventsResult.

        上次修改的时间。

        :param last_modified: The last_modified of this ListEventsResult.
        :type last_modified: float
        """
        self._last_modified = last_modified

    @property
    def name(self):
        """Gets the name of this ListEventsResult.

        测试事件名称。

        :return: The name of this ListEventsResult.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListEventsResult.

        测试事件名称。

        :param name: The name of this ListEventsResult.
        :type name: str
        """
        self._name = name

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
        if not isinstance(other, ListEventsResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
