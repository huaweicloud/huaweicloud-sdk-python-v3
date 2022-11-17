# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Metadata:

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
        'description': 'str',
        'status': 'str',
        'metadata_path': 'str',
        'create_timestamp': 'str',
        'last_update_timestamp': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'status': 'status',
        'metadata_path': 'metadataPath',
        'create_timestamp': 'createTimestamp',
        'last_update_timestamp': 'lastUpdateTimestamp'
    }

    def __init__(self, id=None, name=None, description=None, status=None, metadata_path=None, create_timestamp=None, last_update_timestamp=None):
        """Metadata

        The model defined in huaweicloud sdk

        :param id: 元数据 ID。
        :type id: str
        :param name: 元数据名称。
        :type name: str
        :param description: 元数据 描述。
        :type description: str
        :param status: 元数据是否可用。
        :type status: str
        :param metadata_path: 元数据对应路径。
        :type metadata_path: str
        :param create_timestamp: 元数据创建时间戳。
        :type create_timestamp: str
        :param last_update_timestamp: 元数据最后更新时间戳。
        :type last_update_timestamp: str
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._status = None
        self._metadata_path = None
        self._create_timestamp = None
        self._last_update_timestamp = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.description = description
        self.status = status
        self.metadata_path = metadata_path
        if create_timestamp is not None:
            self.create_timestamp = create_timestamp
        if last_update_timestamp is not None:
            self.last_update_timestamp = last_update_timestamp

    @property
    def id(self):
        """Gets the id of this Metadata.

        元数据 ID。

        :return: The id of this Metadata.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Metadata.

        元数据 ID。

        :param id: The id of this Metadata.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this Metadata.

        元数据名称。

        :return: The name of this Metadata.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Metadata.

        元数据名称。

        :param name: The name of this Metadata.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this Metadata.

        元数据 描述。

        :return: The description of this Metadata.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Metadata.

        元数据 描述。

        :param description: The description of this Metadata.
        :type description: str
        """
        self._description = description

    @property
    def status(self):
        """Gets the status of this Metadata.

        元数据是否可用。

        :return: The status of this Metadata.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Metadata.

        元数据是否可用。

        :param status: The status of this Metadata.
        :type status: str
        """
        self._status = status

    @property
    def metadata_path(self):
        """Gets the metadata_path of this Metadata.

        元数据对应路径。

        :return: The metadata_path of this Metadata.
        :rtype: str
        """
        return self._metadata_path

    @metadata_path.setter
    def metadata_path(self, metadata_path):
        """Sets the metadata_path of this Metadata.

        元数据对应路径。

        :param metadata_path: The metadata_path of this Metadata.
        :type metadata_path: str
        """
        self._metadata_path = metadata_path

    @property
    def create_timestamp(self):
        """Gets the create_timestamp of this Metadata.

        元数据创建时间戳。

        :return: The create_timestamp of this Metadata.
        :rtype: str
        """
        return self._create_timestamp

    @create_timestamp.setter
    def create_timestamp(self, create_timestamp):
        """Sets the create_timestamp of this Metadata.

        元数据创建时间戳。

        :param create_timestamp: The create_timestamp of this Metadata.
        :type create_timestamp: str
        """
        self._create_timestamp = create_timestamp

    @property
    def last_update_timestamp(self):
        """Gets the last_update_timestamp of this Metadata.

        元数据最后更新时间戳。

        :return: The last_update_timestamp of this Metadata.
        :rtype: str
        """
        return self._last_update_timestamp

    @last_update_timestamp.setter
    def last_update_timestamp(self, last_update_timestamp):
        """Sets the last_update_timestamp of this Metadata.

        元数据最后更新时间戳。

        :param last_update_timestamp: The last_update_timestamp of this Metadata.
        :type last_update_timestamp: str
        """
        self._last_update_timestamp = last_update_timestamp

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
        if not isinstance(other, Metadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
