# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BaseModelDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'id': 'str',
        'create_time': 'str',
        'description': 'str'
    }

    attribute_map = {
        'name': 'name',
        'id': 'id',
        'create_time': 'create_time',
        'description': 'description'
    }

    def __init__(self, name=None, id=None, create_time=None, description=None):
        r"""BaseModelDto

        The model defined in huaweicloud sdk

        :param name: 模型名称
        :type name: str
        :param id: 模型ID
        :type id: str
        :param create_time: 模型创建时间
        :type create_time: str
        :param description: 模型描述信息
        :type description: str
        """
        
        

        self._name = None
        self._id = None
        self._create_time = None
        self._description = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if create_time is not None:
            self.create_time = create_time
        if description is not None:
            self.description = description

    @property
    def name(self):
        r"""Gets the name of this BaseModelDto.

        模型名称

        :return: The name of this BaseModelDto.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this BaseModelDto.

        模型名称

        :param name: The name of this BaseModelDto.
        :type name: str
        """
        self._name = name

    @property
    def id(self):
        r"""Gets the id of this BaseModelDto.

        模型ID

        :return: The id of this BaseModelDto.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this BaseModelDto.

        模型ID

        :param id: The id of this BaseModelDto.
        :type id: str
        """
        self._id = id

    @property
    def create_time(self):
        r"""Gets the create_time of this BaseModelDto.

        模型创建时间

        :return: The create_time of this BaseModelDto.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this BaseModelDto.

        模型创建时间

        :param create_time: The create_time of this BaseModelDto.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def description(self):
        r"""Gets the description of this BaseModelDto.

        模型描述信息

        :return: The description of this BaseModelDto.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this BaseModelDto.

        模型描述信息

        :param description: The description of this BaseModelDto.
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
        if not isinstance(other, BaseModelDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
