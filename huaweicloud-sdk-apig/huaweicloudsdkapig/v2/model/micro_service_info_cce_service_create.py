# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MicroServiceInfoCCEServiceCreate:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cluster_id': 'str',
        'namespace': 'str',
        'service_name': 'str',
        'port': 'int'
    }

    attribute_map = {
        'cluster_id': 'cluster_id',
        'namespace': 'namespace',
        'service_name': 'service_name',
        'port': 'port'
    }

    def __init__(self, cluster_id=None, namespace=None, service_name=None, port=None):
        r"""MicroServiceInfoCCEServiceCreate

        The model defined in huaweicloud sdk

        :param cluster_id: 云容器引擎集群编号
        :type cluster_id: str
        :param namespace: 命名空间。1-63字符。只能包含小写字母、数字，以及 &#39;-&#39;，必须以字母开头，必须以字母数字结尾。
        :type namespace: str
        :param service_name: Service名称。支持汉字，英文，数字，点，中划线，下划线，且只能以英文和汉字开头，1-64字符。 &gt; 中文字符必须为UTF-8或者unicode编码。
        :type service_name: str
        :param port: Service的监听端口号。如果是多端口Service，用户需填写一个端口。
        :type port: int
        """
        
        

        self._cluster_id = None
        self._namespace = None
        self._service_name = None
        self._port = None
        self.discriminator = None

        self.cluster_id = cluster_id
        self.namespace = namespace
        self.service_name = service_name
        if port is not None:
            self.port = port

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this MicroServiceInfoCCEServiceCreate.

        云容器引擎集群编号

        :return: The cluster_id of this MicroServiceInfoCCEServiceCreate.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this MicroServiceInfoCCEServiceCreate.

        云容器引擎集群编号

        :param cluster_id: The cluster_id of this MicroServiceInfoCCEServiceCreate.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def namespace(self):
        r"""Gets the namespace of this MicroServiceInfoCCEServiceCreate.

        命名空间。1-63字符。只能包含小写字母、数字，以及 '-'，必须以字母开头，必须以字母数字结尾。

        :return: The namespace of this MicroServiceInfoCCEServiceCreate.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this MicroServiceInfoCCEServiceCreate.

        命名空间。1-63字符。只能包含小写字母、数字，以及 '-'，必须以字母开头，必须以字母数字结尾。

        :param namespace: The namespace of this MicroServiceInfoCCEServiceCreate.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def service_name(self):
        r"""Gets the service_name of this MicroServiceInfoCCEServiceCreate.

        Service名称。支持汉字，英文，数字，点，中划线，下划线，且只能以英文和汉字开头，1-64字符。 > 中文字符必须为UTF-8或者unicode编码。

        :return: The service_name of this MicroServiceInfoCCEServiceCreate.
        :rtype: str
        """
        return self._service_name

    @service_name.setter
    def service_name(self, service_name):
        r"""Sets the service_name of this MicroServiceInfoCCEServiceCreate.

        Service名称。支持汉字，英文，数字，点，中划线，下划线，且只能以英文和汉字开头，1-64字符。 > 中文字符必须为UTF-8或者unicode编码。

        :param service_name: The service_name of this MicroServiceInfoCCEServiceCreate.
        :type service_name: str
        """
        self._service_name = service_name

    @property
    def port(self):
        r"""Gets the port of this MicroServiceInfoCCEServiceCreate.

        Service的监听端口号。如果是多端口Service，用户需填写一个端口。

        :return: The port of this MicroServiceInfoCCEServiceCreate.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        r"""Sets the port of this MicroServiceInfoCCEServiceCreate.

        Service的监听端口号。如果是多端口Service，用户需填写一个端口。

        :param port: The port of this MicroServiceInfoCCEServiceCreate.
        :type port: int
        """
        self._port = port

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
        if not isinstance(other, MicroServiceInfoCCEServiceCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
