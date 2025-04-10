# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MicroServiceInfoNacosBase:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'namespace': 'str',
        'cluster_name': 'str',
        'group_name': 'str',
        'service_name': 'str',
        'server_config': 'list[NacosServerConfig]',
        'user_info': 'NacosUserInfo'
    }

    attribute_map = {
        'namespace': 'namespace',
        'cluster_name': 'cluster_name',
        'group_name': 'group_name',
        'service_name': 'service_name',
        'server_config': 'server_config',
        'user_info': 'user_info'
    }

    def __init__(self, namespace=None, cluster_name=None, group_name=None, service_name=None, server_config=None, user_info=None):
        r"""MicroServiceInfoNacosBase

        The model defined in huaweicloud sdk

        :param namespace: 命名空间ID，当选择默认命名空间public时，此项为空。由字母、数字、连接符(&#39;-&#39;)、下划线(&#39;_&#39;)组成且64个字符之内。 
        :type namespace: str
        :param cluster_name: 集群名称，默认为DEFAULT。由字母、数字、连接符(&#39;-&#39;)、下划线(&#39;_&#39;)组成且64个字符之内。
        :type cluster_name: str
        :param group_name: 分组名称，默认为DEFAULT_GROUP。由字母、数字、连接符(&#39;-&#39;)、下划线(&#39;_&#39;)、点号(&#39;.&#39;)、冒号(&#39;:&#39;)组成且128个字符之内。 
        :type group_name: str
        :param service_name: 微服务名称。不包含中文和@@，不得以@开头，512个字符以内。
        :type service_name: str
        :param server_config: nacos服务端配置信息。
        :type server_config: list[:class:`huaweicloudsdkapig.v2.NacosServerConfig`]
        :param user_info: 
        :type user_info: :class:`huaweicloudsdkapig.v2.NacosUserInfo`
        """
        
        

        self._namespace = None
        self._cluster_name = None
        self._group_name = None
        self._service_name = None
        self._server_config = None
        self._user_info = None
        self.discriminator = None

        if namespace is not None:
            self.namespace = namespace
        if cluster_name is not None:
            self.cluster_name = cluster_name
        if group_name is not None:
            self.group_name = group_name
        self.service_name = service_name
        self.server_config = server_config
        self.user_info = user_info

    @property
    def namespace(self):
        r"""Gets the namespace of this MicroServiceInfoNacosBase.

        命名空间ID，当选择默认命名空间public时，此项为空。由字母、数字、连接符('-')、下划线('_')组成且64个字符之内。 

        :return: The namespace of this MicroServiceInfoNacosBase.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this MicroServiceInfoNacosBase.

        命名空间ID，当选择默认命名空间public时，此项为空。由字母、数字、连接符('-')、下划线('_')组成且64个字符之内。 

        :param namespace: The namespace of this MicroServiceInfoNacosBase.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def cluster_name(self):
        r"""Gets the cluster_name of this MicroServiceInfoNacosBase.

        集群名称，默认为DEFAULT。由字母、数字、连接符('-')、下划线('_')组成且64个字符之内。

        :return: The cluster_name of this MicroServiceInfoNacosBase.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        r"""Sets the cluster_name of this MicroServiceInfoNacosBase.

        集群名称，默认为DEFAULT。由字母、数字、连接符('-')、下划线('_')组成且64个字符之内。

        :param cluster_name: The cluster_name of this MicroServiceInfoNacosBase.
        :type cluster_name: str
        """
        self._cluster_name = cluster_name

    @property
    def group_name(self):
        r"""Gets the group_name of this MicroServiceInfoNacosBase.

        分组名称，默认为DEFAULT_GROUP。由字母、数字、连接符('-')、下划线('_')、点号('.')、冒号(':')组成且128个字符之内。 

        :return: The group_name of this MicroServiceInfoNacosBase.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        r"""Sets the group_name of this MicroServiceInfoNacosBase.

        分组名称，默认为DEFAULT_GROUP。由字母、数字、连接符('-')、下划线('_')、点号('.')、冒号(':')组成且128个字符之内。 

        :param group_name: The group_name of this MicroServiceInfoNacosBase.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def service_name(self):
        r"""Gets the service_name of this MicroServiceInfoNacosBase.

        微服务名称。不包含中文和@@，不得以@开头，512个字符以内。

        :return: The service_name of this MicroServiceInfoNacosBase.
        :rtype: str
        """
        return self._service_name

    @service_name.setter
    def service_name(self, service_name):
        r"""Sets the service_name of this MicroServiceInfoNacosBase.

        微服务名称。不包含中文和@@，不得以@开头，512个字符以内。

        :param service_name: The service_name of this MicroServiceInfoNacosBase.
        :type service_name: str
        """
        self._service_name = service_name

    @property
    def server_config(self):
        r"""Gets the server_config of this MicroServiceInfoNacosBase.

        nacos服务端配置信息。

        :return: The server_config of this MicroServiceInfoNacosBase.
        :rtype: list[:class:`huaweicloudsdkapig.v2.NacosServerConfig`]
        """
        return self._server_config

    @server_config.setter
    def server_config(self, server_config):
        r"""Sets the server_config of this MicroServiceInfoNacosBase.

        nacos服务端配置信息。

        :param server_config: The server_config of this MicroServiceInfoNacosBase.
        :type server_config: list[:class:`huaweicloudsdkapig.v2.NacosServerConfig`]
        """
        self._server_config = server_config

    @property
    def user_info(self):
        r"""Gets the user_info of this MicroServiceInfoNacosBase.

        :return: The user_info of this MicroServiceInfoNacosBase.
        :rtype: :class:`huaweicloudsdkapig.v2.NacosUserInfo`
        """
        return self._user_info

    @user_info.setter
    def user_info(self, user_info):
        r"""Sets the user_info of this MicroServiceInfoNacosBase.

        :param user_info: The user_info of this MicroServiceInfoNacosBase.
        :type user_info: :class:`huaweicloudsdkapig.v2.NacosUserInfo`
        """
        self._user_info = user_info

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
        if not isinstance(other, MicroServiceInfoNacosBase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
