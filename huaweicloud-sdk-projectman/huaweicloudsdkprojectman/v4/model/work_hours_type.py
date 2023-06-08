# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WorkHoursType:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'name': 'str',
        'status': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'status': 'status'
    }

    def __init__(self, id=None, name=None, status=None):
        """WorkHoursType

        The model defined in huaweicloud sdk

        :param id: 工时类型id
        :type id: int
        :param name: 工时类型名称
        :type name: str
        :param status: 工时类型状态，1表示启用中，2表示未启用
        :type status: int
        """
        
        

        self._id = None
        self._name = None
        self._status = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if status is not None:
            self.status = status

    @property
    def id(self):
        """Gets the id of this WorkHoursType.

        工时类型id

        :return: The id of this WorkHoursType.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this WorkHoursType.

        工时类型id

        :param id: The id of this WorkHoursType.
        :type id: int
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this WorkHoursType.

        工时类型名称

        :return: The name of this WorkHoursType.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this WorkHoursType.

        工时类型名称

        :param name: The name of this WorkHoursType.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        """Gets the status of this WorkHoursType.

        工时类型状态，1表示启用中，2表示未启用

        :return: The status of this WorkHoursType.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this WorkHoursType.

        工时类型状态，1表示启用中，2表示未启用

        :param status: The status of this WorkHoursType.
        :type status: int
        """
        self._status = status

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
        if not isinstance(other, WorkHoursType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
