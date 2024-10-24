# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EngineGroupInfo:

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
        'version': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'version': 'version'
    }

    def __init__(self, id=None, name=None, version=None):
        """EngineGroupInfo

        The model defined in huaweicloud sdk

        :param id: 引擎id。
        :type id: str
        :param name: 引擎名称。
        :type name: str
        :param version: 引擎版本。
        :type version: str
        """
        
        

        self._id = None
        self._name = None
        self._version = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.version = version

    @property
    def id(self):
        """Gets the id of this EngineGroupInfo.

        引擎id。

        :return: The id of this EngineGroupInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EngineGroupInfo.

        引擎id。

        :param id: The id of this EngineGroupInfo.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this EngineGroupInfo.

        引擎名称。

        :return: The name of this EngineGroupInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EngineGroupInfo.

        引擎名称。

        :param name: The name of this EngineGroupInfo.
        :type name: str
        """
        self._name = name

    @property
    def version(self):
        """Gets the version of this EngineGroupInfo.

        引擎版本。

        :return: The version of this EngineGroupInfo.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this EngineGroupInfo.

        引擎版本。

        :param version: The version of this EngineGroupInfo.
        :type version: str
        """
        self._version = version

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
        if not isinstance(other, EngineGroupInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
