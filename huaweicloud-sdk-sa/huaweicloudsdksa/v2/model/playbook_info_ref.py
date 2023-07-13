# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PlaybookInfoRef:

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
        'version_id': 'str',
        'name': 'str',
        'version': 'str'
    }

    attribute_map = {
        'id': 'id',
        'version_id': 'version_id',
        'name': 'name',
        'version': 'version'
    }

    def __init__(self, id=None, version_id=None, name=None, version=None):
        """PlaybookInfoRef

        The model defined in huaweicloud sdk

        :param id: Id value
        :type id: str
        :param version_id: Id value
        :type version_id: str
        :param name: Id value
        :type name: str
        :param version: version
        :type version: str
        """
        
        

        self._id = None
        self._version_id = None
        self._name = None
        self._version = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if version_id is not None:
            self.version_id = version_id
        if name is not None:
            self.name = name
        if version is not None:
            self.version = version

    @property
    def id(self):
        """Gets the id of this PlaybookInfoRef.

        Id value

        :return: The id of this PlaybookInfoRef.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PlaybookInfoRef.

        Id value

        :param id: The id of this PlaybookInfoRef.
        :type id: str
        """
        self._id = id

    @property
    def version_id(self):
        """Gets the version_id of this PlaybookInfoRef.

        Id value

        :return: The version_id of this PlaybookInfoRef.
        :rtype: str
        """
        return self._version_id

    @version_id.setter
    def version_id(self, version_id):
        """Sets the version_id of this PlaybookInfoRef.

        Id value

        :param version_id: The version_id of this PlaybookInfoRef.
        :type version_id: str
        """
        self._version_id = version_id

    @property
    def name(self):
        """Gets the name of this PlaybookInfoRef.

        Id value

        :return: The name of this PlaybookInfoRef.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PlaybookInfoRef.

        Id value

        :param name: The name of this PlaybookInfoRef.
        :type name: str
        """
        self._name = name

    @property
    def version(self):
        """Gets the version of this PlaybookInfoRef.

        version

        :return: The version of this PlaybookInfoRef.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this PlaybookInfoRef.

        version

        :param version: The version of this PlaybookInfoRef.
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
        if not isinstance(other, PlaybookInfoRef):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
