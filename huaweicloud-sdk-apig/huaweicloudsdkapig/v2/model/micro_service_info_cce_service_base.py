# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MicroServiceInfoCCEServiceBase:

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
        'service_name': 'str'
    }

    attribute_map = {
        'cluster_id': 'cluster_id',
        'namespace': 'namespace',
        'service_name': 'service_name'
    }

    def __init__(self, cluster_id=None, namespace=None, service_name=None):
        r"""MicroServiceInfoCCEServiceBase

        The model defined in huaweicloud sdk

        :param cluster_id: 云容器引擎集群编号
        :type cluster_id: str
        :param namespace: 命名空间。1-63字符。只能包含小写字母、数字，以及 &#39;-&#39;，必须以字母开头，必须以字母数字结尾。
        :type namespace: str
        :param service_name: Service名称。支持汉字，英文，数字，点，中划线，下划线，且只能以英文和汉字开头，1-64字符。 &gt; 中文字符必须为UTF-8或者unicode编码。
        :type service_name: str
        """
        
        

        self._cluster_id = None
        self._namespace = None
        self._service_name = None
        self.discriminator = None

        self.cluster_id = cluster_id
        self.namespace = namespace
        self.service_name = service_name

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this MicroServiceInfoCCEServiceBase.

        云容器引擎集群编号

        :return: The cluster_id of this MicroServiceInfoCCEServiceBase.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this MicroServiceInfoCCEServiceBase.

        云容器引擎集群编号

        :param cluster_id: The cluster_id of this MicroServiceInfoCCEServiceBase.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def namespace(self):
        r"""Gets the namespace of this MicroServiceInfoCCEServiceBase.

        命名空间。1-63字符。只能包含小写字母、数字，以及 '-'，必须以字母开头，必须以字母数字结尾。

        :return: The namespace of this MicroServiceInfoCCEServiceBase.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this MicroServiceInfoCCEServiceBase.

        命名空间。1-63字符。只能包含小写字母、数字，以及 '-'，必须以字母开头，必须以字母数字结尾。

        :param namespace: The namespace of this MicroServiceInfoCCEServiceBase.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def service_name(self):
        r"""Gets the service_name of this MicroServiceInfoCCEServiceBase.

        Service名称。支持汉字，英文，数字，点，中划线，下划线，且只能以英文和汉字开头，1-64字符。 > 中文字符必须为UTF-8或者unicode编码。

        :return: The service_name of this MicroServiceInfoCCEServiceBase.
        :rtype: str
        """
        return self._service_name

    @service_name.setter
    def service_name(self, service_name):
        r"""Sets the service_name of this MicroServiceInfoCCEServiceBase.

        Service名称。支持汉字，英文，数字，点，中划线，下划线，且只能以英文和汉字开头，1-64字符。 > 中文字符必须为UTF-8或者unicode编码。

        :param service_name: The service_name of this MicroServiceInfoCCEServiceBase.
        :type service_name: str
        """
        self._service_name = service_name

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
        if not isinstance(other, MicroServiceInfoCCEServiceBase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
