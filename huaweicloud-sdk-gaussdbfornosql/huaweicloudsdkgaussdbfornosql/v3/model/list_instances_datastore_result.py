# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInstancesDatastoreResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'version': 'str',
        'patch_available': 'bool',
        'whole_version': 'str'
    }

    attribute_map = {
        'type': 'type',
        'version': 'version',
        'patch_available': 'patch_available',
        'whole_version': 'whole_version'
    }

    def __init__(self, type=None, version=None, patch_available=None, whole_version=None):
        """ListInstancesDatastoreResult

        The model defined in huaweicloud sdk

        :param type: 数据库引擎。
        :type type: str
        :param version: 数据库版本号。
        :type version: str
        :param patch_available: 是否有补丁版本的数据库支持升级，返回true时可以通过升级补丁接口进行数据库升级，否则不允许升级补丁。
        :type patch_available: bool
        :param whole_version: 数据库的完整版本号(目前只有GeminiDB Cassandra支持)。
        :type whole_version: str
        """
        
        

        self._type = None
        self._version = None
        self._patch_available = None
        self._whole_version = None
        self.discriminator = None

        self.type = type
        self.version = version
        self.patch_available = patch_available
        self.whole_version = whole_version

    @property
    def type(self):
        """Gets the type of this ListInstancesDatastoreResult.

        数据库引擎。

        :return: The type of this ListInstancesDatastoreResult.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ListInstancesDatastoreResult.

        数据库引擎。

        :param type: The type of this ListInstancesDatastoreResult.
        :type type: str
        """
        self._type = type

    @property
    def version(self):
        """Gets the version of this ListInstancesDatastoreResult.

        数据库版本号。

        :return: The version of this ListInstancesDatastoreResult.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ListInstancesDatastoreResult.

        数据库版本号。

        :param version: The version of this ListInstancesDatastoreResult.
        :type version: str
        """
        self._version = version

    @property
    def patch_available(self):
        """Gets the patch_available of this ListInstancesDatastoreResult.

        是否有补丁版本的数据库支持升级，返回true时可以通过升级补丁接口进行数据库升级，否则不允许升级补丁。

        :return: The patch_available of this ListInstancesDatastoreResult.
        :rtype: bool
        """
        return self._patch_available

    @patch_available.setter
    def patch_available(self, patch_available):
        """Sets the patch_available of this ListInstancesDatastoreResult.

        是否有补丁版本的数据库支持升级，返回true时可以通过升级补丁接口进行数据库升级，否则不允许升级补丁。

        :param patch_available: The patch_available of this ListInstancesDatastoreResult.
        :type patch_available: bool
        """
        self._patch_available = patch_available

    @property
    def whole_version(self):
        """Gets the whole_version of this ListInstancesDatastoreResult.

        数据库的完整版本号(目前只有GeminiDB Cassandra支持)。

        :return: The whole_version of this ListInstancesDatastoreResult.
        :rtype: str
        """
        return self._whole_version

    @whole_version.setter
    def whole_version(self, whole_version):
        """Sets the whole_version of this ListInstancesDatastoreResult.

        数据库的完整版本号(目前只有GeminiDB Cassandra支持)。

        :param whole_version: The whole_version of this ListInstancesDatastoreResult.
        :type whole_version: str
        """
        self._whole_version = whole_version

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
        if not isinstance(other, ListInstancesDatastoreResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
