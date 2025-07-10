# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GetJobInfoResponseBodyJobEntities:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance': 'GetJobInfoResponseBodyJobEntitiesInstance',
        'resource_ids': 'list[str]',
        'volume': 'GetJobInfoResponseBodyJobEntitiesVolume',
        'public_ip': 'str',
        'switch_strategy': 'str'
    }

    attribute_map = {
        'instance': 'instance',
        'resource_ids': 'resource_ids',
        'volume': 'volume',
        'public_ip': 'public_ip',
        'switch_strategy': 'switch_strategy'
    }

    def __init__(self, instance=None, resource_ids=None, volume=None, public_ip=None, switch_strategy=None):
        r"""GetJobInfoResponseBodyJobEntities

        The model defined in huaweicloud sdk

        :param instance: 
        :type instance: :class:`huaweicloudsdkrds.v3.GetJobInfoResponseBodyJobEntitiesInstance`
        :param resource_ids: 创建实例，单转主备，创建只读实例，调整实例容量任务时等任务时返回。
        :type resource_ids: list[str]
        :param volume: 
        :type volume: :class:`huaweicloudsdkrds.v3.GetJobInfoResponseBodyJobEntitiesVolume`
        :param public_ip: 绑定/解绑弹性IP，开启远程连接等任务时返回。
        :type public_ip: str
        :param switch_strategy: 主备倒换任务时返回。
        :type switch_strategy: str
        """
        
        

        self._instance = None
        self._resource_ids = None
        self._volume = None
        self._public_ip = None
        self._switch_strategy = None
        self.discriminator = None

        if instance is not None:
            self.instance = instance
        if resource_ids is not None:
            self.resource_ids = resource_ids
        if volume is not None:
            self.volume = volume
        if public_ip is not None:
            self.public_ip = public_ip
        if switch_strategy is not None:
            self.switch_strategy = switch_strategy

    @property
    def instance(self):
        r"""Gets the instance of this GetJobInfoResponseBodyJobEntities.

        :return: The instance of this GetJobInfoResponseBodyJobEntities.
        :rtype: :class:`huaweicloudsdkrds.v3.GetJobInfoResponseBodyJobEntitiesInstance`
        """
        return self._instance

    @instance.setter
    def instance(self, instance):
        r"""Sets the instance of this GetJobInfoResponseBodyJobEntities.

        :param instance: The instance of this GetJobInfoResponseBodyJobEntities.
        :type instance: :class:`huaweicloudsdkrds.v3.GetJobInfoResponseBodyJobEntitiesInstance`
        """
        self._instance = instance

    @property
    def resource_ids(self):
        r"""Gets the resource_ids of this GetJobInfoResponseBodyJobEntities.

        创建实例，单转主备，创建只读实例，调整实例容量任务时等任务时返回。

        :return: The resource_ids of this GetJobInfoResponseBodyJobEntities.
        :rtype: list[str]
        """
        return self._resource_ids

    @resource_ids.setter
    def resource_ids(self, resource_ids):
        r"""Sets the resource_ids of this GetJobInfoResponseBodyJobEntities.

        创建实例，单转主备，创建只读实例，调整实例容量任务时等任务时返回。

        :param resource_ids: The resource_ids of this GetJobInfoResponseBodyJobEntities.
        :type resource_ids: list[str]
        """
        self._resource_ids = resource_ids

    @property
    def volume(self):
        r"""Gets the volume of this GetJobInfoResponseBodyJobEntities.

        :return: The volume of this GetJobInfoResponseBodyJobEntities.
        :rtype: :class:`huaweicloudsdkrds.v3.GetJobInfoResponseBodyJobEntitiesVolume`
        """
        return self._volume

    @volume.setter
    def volume(self, volume):
        r"""Sets the volume of this GetJobInfoResponseBodyJobEntities.

        :param volume: The volume of this GetJobInfoResponseBodyJobEntities.
        :type volume: :class:`huaweicloudsdkrds.v3.GetJobInfoResponseBodyJobEntitiesVolume`
        """
        self._volume = volume

    @property
    def public_ip(self):
        r"""Gets the public_ip of this GetJobInfoResponseBodyJobEntities.

        绑定/解绑弹性IP，开启远程连接等任务时返回。

        :return: The public_ip of this GetJobInfoResponseBodyJobEntities.
        :rtype: str
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        r"""Sets the public_ip of this GetJobInfoResponseBodyJobEntities.

        绑定/解绑弹性IP，开启远程连接等任务时返回。

        :param public_ip: The public_ip of this GetJobInfoResponseBodyJobEntities.
        :type public_ip: str
        """
        self._public_ip = public_ip

    @property
    def switch_strategy(self):
        r"""Gets the switch_strategy of this GetJobInfoResponseBodyJobEntities.

        主备倒换任务时返回。

        :return: The switch_strategy of this GetJobInfoResponseBodyJobEntities.
        :rtype: str
        """
        return self._switch_strategy

    @switch_strategy.setter
    def switch_strategy(self, switch_strategy):
        r"""Sets the switch_strategy of this GetJobInfoResponseBodyJobEntities.

        主备倒换任务时返回。

        :param switch_strategy: The switch_strategy of this GetJobInfoResponseBodyJobEntities.
        :type switch_strategy: str
        """
        self._switch_strategy = switch_strategy

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
        if not isinstance(other, GetJobInfoResponseBodyJobEntities):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
