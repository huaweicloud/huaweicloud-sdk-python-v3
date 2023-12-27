# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteResultDeleted:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    xml_name = "DeleteResultDeleted"

    sensitive_list = []

    openapi_types = {
        'key': 'str',
        'version_id': 'str',
        'delete_marker': 'bool',
        'delete_marker_version_id': 'bool'
    }

    attribute_map = {
        'key': 'Key',
        'version_id': 'VersionId',
        'delete_marker': 'DeleteMarker',
        'delete_marker_version_id': 'DeleteMarkerVersionId'
    }

    def __init__(self, key=None, version_id=None, delete_marker=None, delete_marker_version_id=None):
        """DeleteResultDeleted

        The model defined in huaweicloud sdk

        :param key: 每个删除结果的对象名。 
        :type key: str
        :param version_id: 删除对象的版本号 
        :type version_id: str
        :param delete_marker: 当批量删除请求访问的桶是多版本桶时，如果创建或删除一个删除标记，返回消息中该元素的值为true。 
        :type delete_marker: bool
        :param delete_marker_version_id: 请求创建或删除的删除标记版本号。  当批量删除请求访问的桶是多版本桶时，如果创建或删除一个删除标记，响应消息会返回该元素。该元素在以下两种情况中会出现：  用户发送不带版本删除请求，即请求只有对象名，无版本号。这种情况下，系统会创建一个删除标记，并在响应中返回该删除标记的版本号。 用户发送带版本删除请求，即请求同时包含对象名以及版本号，但是该版本号标识一个删除标记。这种情况下，系统会删除此删除标记，并在响应中返回该删除标记的版本号。 
        :type delete_marker_version_id: bool
        """
        
        

        self._key = None
        self._version_id = None
        self._delete_marker = None
        self._delete_marker_version_id = None
        self.discriminator = None

        if key is not None:
            self.key = key
        if version_id is not None:
            self.version_id = version_id
        if delete_marker is not None:
            self.delete_marker = delete_marker
        if delete_marker_version_id is not None:
            self.delete_marker_version_id = delete_marker_version_id

    @property
    def key(self):
        """Gets the key of this DeleteResultDeleted.

        每个删除结果的对象名。 

        :return: The key of this DeleteResultDeleted.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this DeleteResultDeleted.

        每个删除结果的对象名。 

        :param key: The key of this DeleteResultDeleted.
        :type key: str
        """
        self._key = key

    @property
    def version_id(self):
        """Gets the version_id of this DeleteResultDeleted.

        删除对象的版本号 

        :return: The version_id of this DeleteResultDeleted.
        :rtype: str
        """
        return self._version_id

    @version_id.setter
    def version_id(self, version_id):
        """Sets the version_id of this DeleteResultDeleted.

        删除对象的版本号 

        :param version_id: The version_id of this DeleteResultDeleted.
        :type version_id: str
        """
        self._version_id = version_id

    @property
    def delete_marker(self):
        """Gets the delete_marker of this DeleteResultDeleted.

        当批量删除请求访问的桶是多版本桶时，如果创建或删除一个删除标记，返回消息中该元素的值为true。 

        :return: The delete_marker of this DeleteResultDeleted.
        :rtype: bool
        """
        return self._delete_marker

    @delete_marker.setter
    def delete_marker(self, delete_marker):
        """Sets the delete_marker of this DeleteResultDeleted.

        当批量删除请求访问的桶是多版本桶时，如果创建或删除一个删除标记，返回消息中该元素的值为true。 

        :param delete_marker: The delete_marker of this DeleteResultDeleted.
        :type delete_marker: bool
        """
        self._delete_marker = delete_marker

    @property
    def delete_marker_version_id(self):
        """Gets the delete_marker_version_id of this DeleteResultDeleted.

        请求创建或删除的删除标记版本号。  当批量删除请求访问的桶是多版本桶时，如果创建或删除一个删除标记，响应消息会返回该元素。该元素在以下两种情况中会出现：  用户发送不带版本删除请求，即请求只有对象名，无版本号。这种情况下，系统会创建一个删除标记，并在响应中返回该删除标记的版本号。 用户发送带版本删除请求，即请求同时包含对象名以及版本号，但是该版本号标识一个删除标记。这种情况下，系统会删除此删除标记，并在响应中返回该删除标记的版本号。 

        :return: The delete_marker_version_id of this DeleteResultDeleted.
        :rtype: bool
        """
        return self._delete_marker_version_id

    @delete_marker_version_id.setter
    def delete_marker_version_id(self, delete_marker_version_id):
        """Sets the delete_marker_version_id of this DeleteResultDeleted.

        请求创建或删除的删除标记版本号。  当批量删除请求访问的桶是多版本桶时，如果创建或删除一个删除标记，响应消息会返回该元素。该元素在以下两种情况中会出现：  用户发送不带版本删除请求，即请求只有对象名，无版本号。这种情况下，系统会创建一个删除标记，并在响应中返回该删除标记的版本号。 用户发送带版本删除请求，即请求同时包含对象名以及版本号，但是该版本号标识一个删除标记。这种情况下，系统会删除此删除标记，并在响应中返回该删除标记的版本号。 

        :param delete_marker_version_id: The delete_marker_version_id of this DeleteResultDeleted.
        :type delete_marker_version_id: bool
        """
        self._delete_marker_version_id = delete_marker_version_id

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
        if not isinstance(other, DeleteResultDeleted):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
