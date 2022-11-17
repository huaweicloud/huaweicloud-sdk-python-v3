# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowEventResponse(SdkResponse):

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
        'name': 'str',
        'content': 'str',
        'last_modified': 'float'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'content': 'content',
        'last_modified': 'last_modified'
    }

    def __init__(self, id=None, name=None, content=None, last_modified=None):
        """ShowEventResponse

        The model defined in huaweicloud sdk

        :param id: 测试事件ID。
        :type id: str
        :param name: 测试事件名称。
        :type name: str
        :param content: 测试事件content。
        :type content: str
        :param last_modified: 上次修改的时间。
        :type last_modified: float
        """
        
        super(ShowEventResponse, self).__init__()

        self._id = None
        self._name = None
        self._content = None
        self._last_modified = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if content is not None:
            self.content = content
        if last_modified is not None:
            self.last_modified = last_modified

    @property
    def id(self):
        """Gets the id of this ShowEventResponse.

        测试事件ID。

        :return: The id of this ShowEventResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShowEventResponse.

        测试事件ID。

        :param id: The id of this ShowEventResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ShowEventResponse.

        测试事件名称。

        :return: The name of this ShowEventResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ShowEventResponse.

        测试事件名称。

        :param name: The name of this ShowEventResponse.
        :type name: str
        """
        self._name = name

    @property
    def content(self):
        """Gets the content of this ShowEventResponse.

        测试事件content。

        :return: The content of this ShowEventResponse.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this ShowEventResponse.

        测试事件content。

        :param content: The content of this ShowEventResponse.
        :type content: str
        """
        self._content = content

    @property
    def last_modified(self):
        """Gets the last_modified of this ShowEventResponse.

        上次修改的时间。

        :return: The last_modified of this ShowEventResponse.
        :rtype: float
        """
        return self._last_modified

    @last_modified.setter
    def last_modified(self, last_modified):
        """Sets the last_modified of this ShowEventResponse.

        上次修改的时间。

        :param last_modified: The last_modified of this ShowEventResponse.
        :type last_modified: float
        """
        self._last_modified = last_modified

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
        if not isinstance(other, ShowEventResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
