# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DatabaseSmallVersion:

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
        'favored': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'favored': 'favored'
    }

    def __init__(self, id=None, name=None, favored=None):
        r"""DatabaseSmallVersion

        The model defined in huaweicloud sdk

        :param id: 参数解释： 数据库版本ID，该字段不会有重复。
        :type id: str
        :param name: 参数解释： 数据库版本号。
        :type name: str
        :param favored: 参数解释： 是否优选版本。
        :type favored: bool
        """
        
        

        self._id = None
        self._name = None
        self._favored = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.favored = favored

    @property
    def id(self):
        r"""Gets the id of this DatabaseSmallVersion.

        参数解释： 数据库版本ID，该字段不会有重复。

        :return: The id of this DatabaseSmallVersion.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this DatabaseSmallVersion.

        参数解释： 数据库版本ID，该字段不会有重复。

        :param id: The id of this DatabaseSmallVersion.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this DatabaseSmallVersion.

        参数解释： 数据库版本号。

        :return: The name of this DatabaseSmallVersion.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this DatabaseSmallVersion.

        参数解释： 数据库版本号。

        :param name: The name of this DatabaseSmallVersion.
        :type name: str
        """
        self._name = name

    @property
    def favored(self):
        r"""Gets the favored of this DatabaseSmallVersion.

        参数解释： 是否优选版本。

        :return: The favored of this DatabaseSmallVersion.
        :rtype: bool
        """
        return self._favored

    @favored.setter
    def favored(self, favored):
        r"""Sets the favored of this DatabaseSmallVersion.

        参数解释： 是否优选版本。

        :param favored: The favored of this DatabaseSmallVersion.
        :type favored: bool
        """
        self._favored = favored

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DatabaseSmallVersion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
