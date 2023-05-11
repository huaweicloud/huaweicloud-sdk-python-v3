# coding: utf-8

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
        'affinity': 'PodAffinity',
        'apps': 'list[AppDef]',
        'configs': 'PodConfig',
        'init_containers': 'list[AppDef]'
    }

    attribute_map = {
        'affinity': 'affinity',
        'apps': 'apps',
        'configs': 'configs',
        'init_containers': 'init_containers'
    }

    def __init__(self, affinity=None, apps=None, configs=None, init_containers=None):
        """PodRequest

        The model defined in huaweicloud sdk

        :param affinity: 
        :type affinity: :class:`huaweicloudsdkhilens.v3.PodAffinity`
        :param apps: 应用部署业务容器或RPM程序包
        :type apps: list[:class:`huaweicloudsdkhilens.v3.AppDef`]
        :param configs: 
        :type configs: :class:`huaweicloudsdkhilens.v3.PodConfig`
        :param init_containers: 应用部署初始化业务容器，容器部署有效。预留，暂不支持
        :type init_containers: list[:class:`huaweicloudsdkhilens.v3.AppDef`]
        """
        
        

        self._affinity = None
        self._apps = None
        self._configs = None
        self._init_containers = None
        self.discriminator = None

        if affinity is not None:
            self.affinity = affinity
        self.apps = apps
        self.configs = configs
        if init_containers is not None:
            self.init_containers = init_containers

    @property
    def affinity(self):
        """Gets the affinity of this PodRequest.

        :return: The affinity of this PodRequest.
        :rtype: :class:`huaweicloudsdkhilens.v3.PodAffinity`
        """
        return self._affinity

    @affinity.setter
    def affinity(self, affinity):
        """Sets the affinity of this PodRequest.

        :param affinity: The affinity of this PodRequest.
        :type affinity: :class:`huaweicloudsdkhilens.v3.PodAffinity`
        """
        self._affinity = affinity

    @property
    def apps(self):
        """Gets the apps of this PodRequest.

        应用部署业务容器或RPM程序包

        :return: The apps of this PodRequest.
        :rtype: list[:class:`huaweicloudsdkhilens.v3.AppDef`]
        """
        return self._apps

    @apps.setter
    def apps(self, apps):
        """Sets the apps of this PodRequest.

        应用部署业务容器或RPM程序包

        :param apps: The apps of this PodRequest.
        :type apps: list[:class:`huaweicloudsdkhilens.v3.AppDef`]
        """
        self._apps = apps

    @property
    def configs(self):
        """Gets the configs of this PodRequest.

        :return: The configs of this PodRequest.
        :rtype: :class:`huaweicloudsdkhilens.v3.PodConfig`
        """
        return self._configs

    @configs.setter
    def configs(self, configs):
        """Sets the configs of this PodRequest.

        :param configs: The configs of this PodRequest.
        :type configs: :class:`huaweicloudsdkhilens.v3.PodConfig`
        """
        self._configs = configs

    @property
    def init_containers(self):
        """Gets the init_containers of this PodRequest.

        应用部署初始化业务容器，容器部署有效。预留，暂不支持

        :return: The init_containers of this PodRequest.
        :rtype: list[:class:`huaweicloudsdkhilens.v3.AppDef`]
        """
        return self._init_containers

    @init_containers.setter
    def init_containers(self, init_containers):
        """Sets the init_containers of this PodRequest.

        应用部署初始化业务容器，容器部署有效。预留，暂不支持

        :param init_containers: The init_containers of this PodRequest.
        :type init_containers: list[:class:`huaweicloudsdkhilens.v3.AppDef`]
        """
        self._init_containers = init_containers

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
