# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PodRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'configs': 'PodConfigs',
        'affinity': 'Affinity',
        'init_containers': 'list[ContainerDef]',
        'containers': 'list[ContainerDef]'
    }

    attribute_map = {
        'configs': 'configs',
        'affinity': 'affinity',
        'init_containers': 'init_containers',
        'containers': 'containers'
    }

    def __init__(self, configs=None, affinity=None, init_containers=None, containers=None):
        """PodRequest

        The model defined in huaweicloud sdk

        :param configs: 
        :type configs: :class:`huaweicloudsdkief.v1.PodConfigs`
        :param affinity: 
        :type affinity: :class:`huaweicloudsdkief.v1.Affinity`
        :param init_containers: 应用部署init业务容器
        :type init_containers: list[:class:`huaweicloudsdkief.v1.ContainerDef`]
        :param containers: 应用部署业务容器
        :type containers: list[:class:`huaweicloudsdkief.v1.ContainerDef`]
        """
        
        

        self._configs = None
        self._affinity = None
        self._init_containers = None
        self._containers = None
        self.discriminator = None

        self.configs = configs
        if affinity is not None:
            self.affinity = affinity
        if init_containers is not None:
            self.init_containers = init_containers
        self.containers = containers

    @property
    def configs(self):
        """Gets the configs of this PodRequest.


        :return: The configs of this PodRequest.
        :rtype: :class:`huaweicloudsdkief.v1.PodConfigs`
        """
        return self._configs

    @configs.setter
    def configs(self, configs):
        """Sets the configs of this PodRequest.


        :param configs: The configs of this PodRequest.
        :type configs: :class:`huaweicloudsdkief.v1.PodConfigs`
        """
        self._configs = configs

    @property
    def affinity(self):
        """Gets the affinity of this PodRequest.


        :return: The affinity of this PodRequest.
        :rtype: :class:`huaweicloudsdkief.v1.Affinity`
        """
        return self._affinity

    @affinity.setter
    def affinity(self, affinity):
        """Sets the affinity of this PodRequest.


        :param affinity: The affinity of this PodRequest.
        :type affinity: :class:`huaweicloudsdkief.v1.Affinity`
        """
        self._affinity = affinity

    @property
    def init_containers(self):
        """Gets the init_containers of this PodRequest.

        应用部署init业务容器

        :return: The init_containers of this PodRequest.
        :rtype: list[:class:`huaweicloudsdkief.v1.ContainerDef`]
        """
        return self._init_containers

    @init_containers.setter
    def init_containers(self, init_containers):
        """Sets the init_containers of this PodRequest.

        应用部署init业务容器

        :param init_containers: The init_containers of this PodRequest.
        :type init_containers: list[:class:`huaweicloudsdkief.v1.ContainerDef`]
        """
        self._init_containers = init_containers

    @property
    def containers(self):
        """Gets the containers of this PodRequest.

        应用部署业务容器

        :return: The containers of this PodRequest.
        :rtype: list[:class:`huaweicloudsdkief.v1.ContainerDef`]
        """
        return self._containers

    @containers.setter
    def containers(self, containers):
        """Sets the containers of this PodRequest.

        应用部署业务容器

        :param containers: The containers of this PodRequest.
        :type containers: list[:class:`huaweicloudsdkief.v1.ContainerDef`]
        """
        self._containers = containers

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
        if not isinstance(other, PodRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
