# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ClusterDetailDatastore:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'version': 'str',
        'sub_version': 'str',
        'is_eos_cluster': 'bool',
        'support_securitymode': 'bool'
    }

    attribute_map = {
        'type': 'type',
        'version': 'version',
        'sub_version': 'subVersion',
        'is_eos_cluster': 'isEosCluster',
        'support_securitymode': 'supportSecuritymode'
    }

    def __init__(self, type=None, version=None, sub_version=None, is_eos_cluster=None, support_securitymode=None):
        r"""ClusterDetailDatastore

        The model defined in huaweicloud sdk

        :param type: 引擎类型，目前只支持elasticsearch。
        :type type: str
        :param version: CSS集群引擎版本号。详细请参考CSS[支持的集群版本](css_03_0056.xml)。
        :type version: str
        :param sub_version: 集群发布版本号。
        :type sub_version: str
        :param is_eos_cluster: 表示集群发布版本是否EOS。
        :type is_eos_cluster: bool
        :param support_securitymode: 集群认证是否支持安全模式。
        :type support_securitymode: bool
        """
        
        

        self._type = None
        self._version = None
        self._sub_version = None
        self._is_eos_cluster = None
        self._support_securitymode = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if version is not None:
            self.version = version
        if sub_version is not None:
            self.sub_version = sub_version
        if is_eos_cluster is not None:
            self.is_eos_cluster = is_eos_cluster
        if support_securitymode is not None:
            self.support_securitymode = support_securitymode

    @property
    def type(self):
        r"""Gets the type of this ClusterDetailDatastore.

        引擎类型，目前只支持elasticsearch。

        :return: The type of this ClusterDetailDatastore.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ClusterDetailDatastore.

        引擎类型，目前只支持elasticsearch。

        :param type: The type of this ClusterDetailDatastore.
        :type type: str
        """
        self._type = type

    @property
    def version(self):
        r"""Gets the version of this ClusterDetailDatastore.

        CSS集群引擎版本号。详细请参考CSS[支持的集群版本](css_03_0056.xml)。

        :return: The version of this ClusterDetailDatastore.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this ClusterDetailDatastore.

        CSS集群引擎版本号。详细请参考CSS[支持的集群版本](css_03_0056.xml)。

        :param version: The version of this ClusterDetailDatastore.
        :type version: str
        """
        self._version = version

    @property
    def sub_version(self):
        r"""Gets the sub_version of this ClusterDetailDatastore.

        集群发布版本号。

        :return: The sub_version of this ClusterDetailDatastore.
        :rtype: str
        """
        return self._sub_version

    @sub_version.setter
    def sub_version(self, sub_version):
        r"""Sets the sub_version of this ClusterDetailDatastore.

        集群发布版本号。

        :param sub_version: The sub_version of this ClusterDetailDatastore.
        :type sub_version: str
        """
        self._sub_version = sub_version

    @property
    def is_eos_cluster(self):
        r"""Gets the is_eos_cluster of this ClusterDetailDatastore.

        表示集群发布版本是否EOS。

        :return: The is_eos_cluster of this ClusterDetailDatastore.
        :rtype: bool
        """
        return self._is_eos_cluster

    @is_eos_cluster.setter
    def is_eos_cluster(self, is_eos_cluster):
        r"""Sets the is_eos_cluster of this ClusterDetailDatastore.

        表示集群发布版本是否EOS。

        :param is_eos_cluster: The is_eos_cluster of this ClusterDetailDatastore.
        :type is_eos_cluster: bool
        """
        self._is_eos_cluster = is_eos_cluster

    @property
    def support_securitymode(self):
        r"""Gets the support_securitymode of this ClusterDetailDatastore.

        集群认证是否支持安全模式。

        :return: The support_securitymode of this ClusterDetailDatastore.
        :rtype: bool
        """
        return self._support_securitymode

    @support_securitymode.setter
    def support_securitymode(self, support_securitymode):
        r"""Sets the support_securitymode of this ClusterDetailDatastore.

        集群认证是否支持安全模式。

        :param support_securitymode: The support_securitymode of this ClusterDetailDatastore.
        :type support_securitymode: bool
        """
        self._support_securitymode = support_securitymode

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
        if not isinstance(other, ClusterDetailDatastore):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
