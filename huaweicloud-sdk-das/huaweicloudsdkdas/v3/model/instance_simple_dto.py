# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InstanceSimpleDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'instance_name': 'str',
        'engine_type': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'instance_name': 'instance_name',
        'engine_type': 'engine_type'
    }

    def __init__(self, instance_id=None, instance_name=None, engine_type=None):
        r"""InstanceSimpleDto

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID，实例的唯一标识
        :type instance_id: str
        :param instance_name: 实例名称
        :type instance_name: str
        :param engine_type: 数据库引擎类型。取值范围：mysql、sqlserver、postgresql、taurus、gaussdbv5、mongodb
        :type engine_type: str
        """
        
        

        self._instance_id = None
        self._instance_name = None
        self._engine_type = None
        self.discriminator = None

        if instance_id is not None:
            self.instance_id = instance_id
        if instance_name is not None:
            self.instance_name = instance_name
        if engine_type is not None:
            self.engine_type = engine_type

    @property
    def instance_id(self):
        r"""Gets the instance_id of this InstanceSimpleDto.

        实例ID，实例的唯一标识

        :return: The instance_id of this InstanceSimpleDto.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this InstanceSimpleDto.

        实例ID，实例的唯一标识

        :param instance_id: The instance_id of this InstanceSimpleDto.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def instance_name(self):
        r"""Gets the instance_name of this InstanceSimpleDto.

        实例名称

        :return: The instance_name of this InstanceSimpleDto.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        r"""Sets the instance_name of this InstanceSimpleDto.

        实例名称

        :param instance_name: The instance_name of this InstanceSimpleDto.
        :type instance_name: str
        """
        self._instance_name = instance_name

    @property
    def engine_type(self):
        r"""Gets the engine_type of this InstanceSimpleDto.

        数据库引擎类型。取值范围：mysql、sqlserver、postgresql、taurus、gaussdbv5、mongodb

        :return: The engine_type of this InstanceSimpleDto.
        :rtype: str
        """
        return self._engine_type

    @engine_type.setter
    def engine_type(self, engine_type):
        r"""Sets the engine_type of this InstanceSimpleDto.

        数据库引擎类型。取值范围：mysql、sqlserver、postgresql、taurus、gaussdbv5、mongodb

        :param engine_type: The engine_type of this InstanceSimpleDto.
        :type engine_type: str
        """
        self._engine_type = engine_type

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
        if not isinstance(other, InstanceSimpleDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
