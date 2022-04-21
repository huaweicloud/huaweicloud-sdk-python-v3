# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TempDetailInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'description': 'str',
        'id': 'int',
        'is_quoted': 'bool',
        'name': 'str',
        'temp_type': 'int',
        'update_time': 'str'
    }

    attribute_map = {
        'description': 'description',
        'id': 'id',
        'is_quoted': 'is_quoted',
        'name': 'name',
        'temp_type': 'temp_type',
        'update_time': 'update_time'
    }

    def __init__(self, description=None, id=None, is_quoted=None, name=None, temp_type=None, update_time=None):
        """TempDetailInfo

        The model defined in huaweicloud sdk

        :param description: description
        :type description: str
        :param id: id
        :type id: int
        :param is_quoted: 是否被引用
        :type is_quoted: bool
        :param name: name
        :type name: str
        :param temp_type: temp_type
        :type temp_type: int
        :param update_time: update_time
        :type update_time: str
        """
        
        

        self._description = None
        self._id = None
        self._is_quoted = None
        self._name = None
        self._temp_type = None
        self._update_time = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if id is not None:
            self.id = id
        if is_quoted is not None:
            self.is_quoted = is_quoted
        if name is not None:
            self.name = name
        if temp_type is not None:
            self.temp_type = temp_type
        if update_time is not None:
            self.update_time = update_time

    @property
    def description(self):
        """Gets the description of this TempDetailInfo.

        description

        :return: The description of this TempDetailInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TempDetailInfo.

        description

        :param description: The description of this TempDetailInfo.
        :type description: str
        """
        self._description = description

    @property
    def id(self):
        """Gets the id of this TempDetailInfo.

        id

        :return: The id of this TempDetailInfo.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TempDetailInfo.

        id

        :param id: The id of this TempDetailInfo.
        :type id: int
        """
        self._id = id

    @property
    def is_quoted(self):
        """Gets the is_quoted of this TempDetailInfo.

        是否被引用

        :return: The is_quoted of this TempDetailInfo.
        :rtype: bool
        """
        return self._is_quoted

    @is_quoted.setter
    def is_quoted(self, is_quoted):
        """Sets the is_quoted of this TempDetailInfo.

        是否被引用

        :param is_quoted: The is_quoted of this TempDetailInfo.
        :type is_quoted: bool
        """
        self._is_quoted = is_quoted

    @property
    def name(self):
        """Gets the name of this TempDetailInfo.

        name

        :return: The name of this TempDetailInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TempDetailInfo.

        name

        :param name: The name of this TempDetailInfo.
        :type name: str
        """
        self._name = name

    @property
    def temp_type(self):
        """Gets the temp_type of this TempDetailInfo.

        temp_type

        :return: The temp_type of this TempDetailInfo.
        :rtype: int
        """
        return self._temp_type

    @temp_type.setter
    def temp_type(self, temp_type):
        """Sets the temp_type of this TempDetailInfo.

        temp_type

        :param temp_type: The temp_type of this TempDetailInfo.
        :type temp_type: int
        """
        self._temp_type = temp_type

    @property
    def update_time(self):
        """Gets the update_time of this TempDetailInfo.

        update_time

        :return: The update_time of this TempDetailInfo.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this TempDetailInfo.

        update_time

        :param update_time: The update_time of this TempDetailInfo.
        :type update_time: str
        """
        self._update_time = update_time

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
        if not isinstance(other, TempDetailInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
