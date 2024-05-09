# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CssClusterDto:

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
        'storage': 'int',
        'import_time': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'storage': 'storage',
        'import_time': 'import_time'
    }

    def __init__(self, id=None, name=None, storage=None, import_time=None):
        """CssClusterDto

        The model defined in huaweicloud sdk

        :param id: 已绑定的集群id
        :type id: str
        :param name: css集群名称
        :type name: str
        :param storage: css集群总存储
        :type storage: int
        :param import_time: css集群导入时间
        :type import_time: str
        """
        
        

        self._id = None
        self._name = None
        self._storage = None
        self._import_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if storage is not None:
            self.storage = storage
        if import_time is not None:
            self.import_time = import_time

    @property
    def id(self):
        """Gets the id of this CssClusterDto.

        已绑定的集群id

        :return: The id of this CssClusterDto.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CssClusterDto.

        已绑定的集群id

        :param id: The id of this CssClusterDto.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this CssClusterDto.

        css集群名称

        :return: The name of this CssClusterDto.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CssClusterDto.

        css集群名称

        :param name: The name of this CssClusterDto.
        :type name: str
        """
        self._name = name

    @property
    def storage(self):
        """Gets the storage of this CssClusterDto.

        css集群总存储

        :return: The storage of this CssClusterDto.
        :rtype: int
        """
        return self._storage

    @storage.setter
    def storage(self, storage):
        """Sets the storage of this CssClusterDto.

        css集群总存储

        :param storage: The storage of this CssClusterDto.
        :type storage: int
        """
        self._storage = storage

    @property
    def import_time(self):
        """Gets the import_time of this CssClusterDto.

        css集群导入时间

        :return: The import_time of this CssClusterDto.
        :rtype: str
        """
        return self._import_time

    @import_time.setter
    def import_time(self, import_time):
        """Sets the import_time of this CssClusterDto.

        css集群导入时间

        :param import_time: The import_time of this CssClusterDto.
        :type import_time: str
        """
        self._import_time = import_time

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
        if not isinstance(other, CssClusterDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
