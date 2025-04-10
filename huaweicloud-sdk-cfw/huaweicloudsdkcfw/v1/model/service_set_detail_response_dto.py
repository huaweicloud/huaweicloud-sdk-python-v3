# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ServiceSetDetailResponseDto:

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
        'service_set_type': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'service_set_type': 'service_set_type'
    }

    def __init__(self, id=None, name=None, description=None, service_set_type=None):
        r"""ServiceSetDetailResponseDto

        The model defined in huaweicloud sdk

        :param id: 服务组id
        :type id: str
        :param name: 服务组名称
        :type name: str
        :param description: 服务组描述信息
        :type description: str
        :param service_set_type: 服务组类型，0表示自定义服务组，1表示常用WEB服务，2表示常用远程登录和PING，3表示常用数据库
        :type service_set_type: int
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._service_set_type = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.name = name
        if description is not None:
            self.description = description
        if service_set_type is not None:
            self.service_set_type = service_set_type

    @property
    def id(self):
        r"""Gets the id of this ServiceSetDetailResponseDto.

        服务组id

        :return: The id of this ServiceSetDetailResponseDto.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ServiceSetDetailResponseDto.

        服务组id

        :param id: The id of this ServiceSetDetailResponseDto.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ServiceSetDetailResponseDto.

        服务组名称

        :return: The name of this ServiceSetDetailResponseDto.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ServiceSetDetailResponseDto.

        服务组名称

        :param name: The name of this ServiceSetDetailResponseDto.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this ServiceSetDetailResponseDto.

        服务组描述信息

        :return: The description of this ServiceSetDetailResponseDto.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ServiceSetDetailResponseDto.

        服务组描述信息

        :param description: The description of this ServiceSetDetailResponseDto.
        :type description: str
        """
        self._description = description

    @property
    def service_set_type(self):
        r"""Gets the service_set_type of this ServiceSetDetailResponseDto.

        服务组类型，0表示自定义服务组，1表示常用WEB服务，2表示常用远程登录和PING，3表示常用数据库

        :return: The service_set_type of this ServiceSetDetailResponseDto.
        :rtype: int
        """
        return self._service_set_type

    @service_set_type.setter
    def service_set_type(self, service_set_type):
        r"""Sets the service_set_type of this ServiceSetDetailResponseDto.

        服务组类型，0表示自定义服务组，1表示常用WEB服务，2表示常用远程登录和PING，3表示常用数据库

        :param service_set_type: The service_set_type of this ServiceSetDetailResponseDto.
        :type service_set_type: int
        """
        self._service_set_type = service_set_type

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
        if not isinstance(other, ServiceSetDetailResponseDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
