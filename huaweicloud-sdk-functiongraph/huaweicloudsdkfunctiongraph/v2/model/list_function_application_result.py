# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListFunctionApplicationResult:

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
        'status': 'str',
        'last_modified_time': 'int',
        'description': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'status': 'status',
        'last_modified_time': 'last_modified_time',
        'description': 'description'
    }

    def __init__(self, id=None, name=None, status=None, last_modified_time=None, description=None):
        """ListFunctionApplicationResult

        The model defined in huaweicloud sdk

        :param id: 应用id
        :type id: str
        :param name: 应用名称
        :type name: str
        :param status: 应用状态
        :type status: str
        :param last_modified_time: 最后修改时间
        :type last_modified_time: int
        :param description: 应用描述
        :type description: str
        """
        
        

        self._id = None
        self._name = None
        self._status = None
        self._last_modified_time = None
        self._description = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if last_modified_time is not None:
            self.last_modified_time = last_modified_time
        if description is not None:
            self.description = description

    @property
    def id(self):
        """Gets the id of this ListFunctionApplicationResult.

        应用id

        :return: The id of this ListFunctionApplicationResult.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListFunctionApplicationResult.

        应用id

        :param id: The id of this ListFunctionApplicationResult.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ListFunctionApplicationResult.

        应用名称

        :return: The name of this ListFunctionApplicationResult.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListFunctionApplicationResult.

        应用名称

        :param name: The name of this ListFunctionApplicationResult.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        """Gets the status of this ListFunctionApplicationResult.

        应用状态

        :return: The status of this ListFunctionApplicationResult.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListFunctionApplicationResult.

        应用状态

        :param status: The status of this ListFunctionApplicationResult.
        :type status: str
        """
        self._status = status

    @property
    def last_modified_time(self):
        """Gets the last_modified_time of this ListFunctionApplicationResult.

        最后修改时间

        :return: The last_modified_time of this ListFunctionApplicationResult.
        :rtype: int
        """
        return self._last_modified_time

    @last_modified_time.setter
    def last_modified_time(self, last_modified_time):
        """Sets the last_modified_time of this ListFunctionApplicationResult.

        最后修改时间

        :param last_modified_time: The last_modified_time of this ListFunctionApplicationResult.
        :type last_modified_time: int
        """
        self._last_modified_time = last_modified_time

    @property
    def description(self):
        """Gets the description of this ListFunctionApplicationResult.

        应用描述

        :return: The description of this ListFunctionApplicationResult.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ListFunctionApplicationResult.

        应用描述

        :param description: The description of this ListFunctionApplicationResult.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, ListFunctionApplicationResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
