# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowIfTaskNameRepeatRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'service_id': 'str',
        'id': 'str',
        'name': 'str'
    }

    attribute_map = {
        'service_id': 'service_id',
        'id': 'id',
        'name': 'name'
    }

    def __init__(self, service_id=None, id=None, name=None):
        """ShowIfTaskNameRepeatRequest

        The model defined in huaweicloud sdk

        :param service_id: 服务id
        :type service_id: str
        :param id: UUID
        :type id: str
        :param name: 查询的模板名称
        :type name: str
        """
        
        

        self._service_id = None
        self._id = None
        self._name = None
        self.discriminator = None

        self.service_id = service_id
        if id is not None:
            self.id = id
        self.name = name

    @property
    def service_id(self):
        """Gets the service_id of this ShowIfTaskNameRepeatRequest.

        服务id

        :return: The service_id of this ShowIfTaskNameRepeatRequest.
        :rtype: str
        """
        return self._service_id

    @service_id.setter
    def service_id(self, service_id):
        """Sets the service_id of this ShowIfTaskNameRepeatRequest.

        服务id

        :param service_id: The service_id of this ShowIfTaskNameRepeatRequest.
        :type service_id: str
        """
        self._service_id = service_id

    @property
    def id(self):
        """Gets the id of this ShowIfTaskNameRepeatRequest.

        UUID

        :return: The id of this ShowIfTaskNameRepeatRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShowIfTaskNameRepeatRequest.

        UUID

        :param id: The id of this ShowIfTaskNameRepeatRequest.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ShowIfTaskNameRepeatRequest.

        查询的模板名称

        :return: The name of this ShowIfTaskNameRepeatRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ShowIfTaskNameRepeatRequest.

        查询的模板名称

        :param name: The name of this ShowIfTaskNameRepeatRequest.
        :type name: str
        """
        self._name = name

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
        if not isinstance(other, ShowIfTaskNameRepeatRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
