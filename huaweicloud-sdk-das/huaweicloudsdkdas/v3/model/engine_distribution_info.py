# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EngineDistributionInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'engine_type': 'str',
        'total': 'int',
        'instance_infos': 'list[DistributionInstanceInfo]'
    }

    attribute_map = {
        'engine_type': 'engine_type',
        'total': 'total',
        'instance_infos': 'instance_infos'
    }

    def __init__(self, engine_type=None, total=None, instance_infos=None):
        r"""EngineDistributionInfo

        The model defined in huaweicloud sdk

        :param engine_type: 数据库类型
        :type engine_type: str
        :param total: 总数
        :type total: int
        :param instance_infos: 实例信息
        :type instance_infos: list[:class:`huaweicloudsdkdas.v3.DistributionInstanceInfo`]
        """
        
        

        self._engine_type = None
        self._total = None
        self._instance_infos = None
        self.discriminator = None

        if engine_type is not None:
            self.engine_type = engine_type
        if total is not None:
            self.total = total
        if instance_infos is not None:
            self.instance_infos = instance_infos

    @property
    def engine_type(self):
        r"""Gets the engine_type of this EngineDistributionInfo.

        数据库类型

        :return: The engine_type of this EngineDistributionInfo.
        :rtype: str
        """
        return self._engine_type

    @engine_type.setter
    def engine_type(self, engine_type):
        r"""Sets the engine_type of this EngineDistributionInfo.

        数据库类型

        :param engine_type: The engine_type of this EngineDistributionInfo.
        :type engine_type: str
        """
        self._engine_type = engine_type

    @property
    def total(self):
        r"""Gets the total of this EngineDistributionInfo.

        总数

        :return: The total of this EngineDistributionInfo.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this EngineDistributionInfo.

        总数

        :param total: The total of this EngineDistributionInfo.
        :type total: int
        """
        self._total = total

    @property
    def instance_infos(self):
        r"""Gets the instance_infos of this EngineDistributionInfo.

        实例信息

        :return: The instance_infos of this EngineDistributionInfo.
        :rtype: list[:class:`huaweicloudsdkdas.v3.DistributionInstanceInfo`]
        """
        return self._instance_infos

    @instance_infos.setter
    def instance_infos(self, instance_infos):
        r"""Sets the instance_infos of this EngineDistributionInfo.

        实例信息

        :param instance_infos: The instance_infos of this EngineDistributionInfo.
        :type instance_infos: list[:class:`huaweicloudsdkdas.v3.DistributionInstanceInfo`]
        """
        self._instance_infos = instance_infos

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
        if not isinstance(other, EngineDistributionInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
