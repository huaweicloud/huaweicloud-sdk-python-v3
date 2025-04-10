# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateScalingConfigOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'scaling_configuration_name': 'str',
        'instance_config': 'InstanceConfig',
        'source_scaling_configuration_id': 'str'
    }

    attribute_map = {
        'scaling_configuration_name': 'scaling_configuration_name',
        'instance_config': 'instance_config',
        'source_scaling_configuration_id': 'source_scaling_configuration_id'
    }

    def __init__(self, scaling_configuration_name=None, instance_config=None, source_scaling_configuration_id=None):
        r"""CreateScalingConfigOption

        The model defined in huaweicloud sdk

        :param scaling_configuration_name: 伸缩配置名称(1-64个字符)，只能包含中文、字母、数字、下划线或中划线。
        :type scaling_configuration_name: str
        :param instance_config: 
        :type instance_config: :class:`huaweicloudsdkas.v1.InstanceConfig`
        :param source_scaling_configuration_id: 源伸缩配置ID，通过该ID查询已有伸缩配置信息与instance_config中参数进行结合，创建新的伸缩配置。 说明：  - 若传入instance_config中的instance_id，则优先使用instance_id相关实例配置创建新的伸缩配置，source_scaling_configuration_id参数不生效。  - 若未传入instance_config中的instance_id，则使用source_scaling_configuration_id与instance_config中的参数相结合创建伸缩配置。         - 若instance_config中的参数值为null，则创建新伸缩配置时该字段不产生修改。         - 若instance_config中的参数值不为null，则创建新伸缩配置时该字段将覆盖原有值，其中值为空时，该字段会被清空。  - 若不指定source_scaling_configuration_id创建伸缩配置，则scaling_configuration_name和instance_config为必选。
        :type source_scaling_configuration_id: str
        """
        
        

        self._scaling_configuration_name = None
        self._instance_config = None
        self._source_scaling_configuration_id = None
        self.discriminator = None

        if scaling_configuration_name is not None:
            self.scaling_configuration_name = scaling_configuration_name
        if instance_config is not None:
            self.instance_config = instance_config
        if source_scaling_configuration_id is not None:
            self.source_scaling_configuration_id = source_scaling_configuration_id

    @property
    def scaling_configuration_name(self):
        r"""Gets the scaling_configuration_name of this CreateScalingConfigOption.

        伸缩配置名称(1-64个字符)，只能包含中文、字母、数字、下划线或中划线。

        :return: The scaling_configuration_name of this CreateScalingConfigOption.
        :rtype: str
        """
        return self._scaling_configuration_name

    @scaling_configuration_name.setter
    def scaling_configuration_name(self, scaling_configuration_name):
        r"""Sets the scaling_configuration_name of this CreateScalingConfigOption.

        伸缩配置名称(1-64个字符)，只能包含中文、字母、数字、下划线或中划线。

        :param scaling_configuration_name: The scaling_configuration_name of this CreateScalingConfigOption.
        :type scaling_configuration_name: str
        """
        self._scaling_configuration_name = scaling_configuration_name

    @property
    def instance_config(self):
        r"""Gets the instance_config of this CreateScalingConfigOption.

        :return: The instance_config of this CreateScalingConfigOption.
        :rtype: :class:`huaweicloudsdkas.v1.InstanceConfig`
        """
        return self._instance_config

    @instance_config.setter
    def instance_config(self, instance_config):
        r"""Sets the instance_config of this CreateScalingConfigOption.

        :param instance_config: The instance_config of this CreateScalingConfigOption.
        :type instance_config: :class:`huaweicloudsdkas.v1.InstanceConfig`
        """
        self._instance_config = instance_config

    @property
    def source_scaling_configuration_id(self):
        r"""Gets the source_scaling_configuration_id of this CreateScalingConfigOption.

        源伸缩配置ID，通过该ID查询已有伸缩配置信息与instance_config中参数进行结合，创建新的伸缩配置。 说明：  - 若传入instance_config中的instance_id，则优先使用instance_id相关实例配置创建新的伸缩配置，source_scaling_configuration_id参数不生效。  - 若未传入instance_config中的instance_id，则使用source_scaling_configuration_id与instance_config中的参数相结合创建伸缩配置。         - 若instance_config中的参数值为null，则创建新伸缩配置时该字段不产生修改。         - 若instance_config中的参数值不为null，则创建新伸缩配置时该字段将覆盖原有值，其中值为空时，该字段会被清空。  - 若不指定source_scaling_configuration_id创建伸缩配置，则scaling_configuration_name和instance_config为必选。

        :return: The source_scaling_configuration_id of this CreateScalingConfigOption.
        :rtype: str
        """
        return self._source_scaling_configuration_id

    @source_scaling_configuration_id.setter
    def source_scaling_configuration_id(self, source_scaling_configuration_id):
        r"""Sets the source_scaling_configuration_id of this CreateScalingConfigOption.

        源伸缩配置ID，通过该ID查询已有伸缩配置信息与instance_config中参数进行结合，创建新的伸缩配置。 说明：  - 若传入instance_config中的instance_id，则优先使用instance_id相关实例配置创建新的伸缩配置，source_scaling_configuration_id参数不生效。  - 若未传入instance_config中的instance_id，则使用source_scaling_configuration_id与instance_config中的参数相结合创建伸缩配置。         - 若instance_config中的参数值为null，则创建新伸缩配置时该字段不产生修改。         - 若instance_config中的参数值不为null，则创建新伸缩配置时该字段将覆盖原有值，其中值为空时，该字段会被清空。  - 若不指定source_scaling_configuration_id创建伸缩配置，则scaling_configuration_name和instance_config为必选。

        :param source_scaling_configuration_id: The source_scaling_configuration_id of this CreateScalingConfigOption.
        :type source_scaling_configuration_id: str
        """
        self._source_scaling_configuration_id = source_scaling_configuration_id

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
        if not isinstance(other, CreateScalingConfigOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
