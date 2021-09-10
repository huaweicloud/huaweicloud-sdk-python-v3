# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CustomerConfig:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'failure_remind': 'str',
        'cluster_name': 'str',
        'service_provider': 'str',
        'local_disk': 'str',
        'ssl': 'str'
    }

    attribute_map = {
        'failure_remind': 'failureRemind',
        'cluster_name': 'clusterName',
        'service_provider': 'serviceProvider',
        'local_disk': 'localDisk',
        'ssl': 'ssl'
    }

    def __init__(self, failure_remind=None, cluster_name=None, service_provider=None, local_disk=None, ssl=None):
        """CustomerConfig - a model defined in huaweicloud sdk"""
        
        

        self._failure_remind = None
        self._cluster_name = None
        self._service_provider = None
        self._local_disk = None
        self._ssl = None
        self.discriminator = None

        if failure_remind is not None:
            self.failure_remind = failure_remind
        if cluster_name is not None:
            self.cluster_name = cluster_name
        if service_provider is not None:
            self.service_provider = service_provider
        if local_disk is not None:
            self.local_disk = local_disk
        if ssl is not None:
            self.ssl = ssl

    @property
    def failure_remind(self):
        """Gets the failure_remind of this CustomerConfig.

        失败提醒。

        :return: The failure_remind of this CustomerConfig.
        :rtype: str
        """
        return self._failure_remind

    @failure_remind.setter
    def failure_remind(self, failure_remind):
        """Sets the failure_remind of this CustomerConfig.

        失败提醒。

        :param failure_remind: The failure_remind of this CustomerConfig.
        :type: str
        """
        self._failure_remind = failure_remind

    @property
    def cluster_name(self):
        """Gets the cluster_name of this CustomerConfig.

        集群类型。

        :return: The cluster_name of this CustomerConfig.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        """Sets the cluster_name of this CustomerConfig.

        集群类型。

        :param cluster_name: The cluster_name of this CustomerConfig.
        :type: str
        """
        self._cluster_name = cluster_name

    @property
    def service_provider(self):
        """Gets the service_provider of this CustomerConfig.

        服务提供

        :return: The service_provider of this CustomerConfig.
        :rtype: str
        """
        return self._service_provider

    @service_provider.setter
    def service_provider(self, service_provider):
        """Sets the service_provider of this CustomerConfig.

        服务提供

        :param service_provider: The service_provider of this CustomerConfig.
        :type: str
        """
        self._service_provider = service_provider

    @property
    def local_disk(self):
        """Gets the local_disk of this CustomerConfig.

        是否本地磁盘。

        :return: The local_disk of this CustomerConfig.
        :rtype: str
        """
        return self._local_disk

    @local_disk.setter
    def local_disk(self, local_disk):
        """Sets the local_disk of this CustomerConfig.

        是否本地磁盘。

        :param local_disk: The local_disk of this CustomerConfig.
        :type: str
        """
        self._local_disk = local_disk

    @property
    def ssl(self):
        """Gets the ssl of this CustomerConfig.

        是否使用ssl。

        :return: The ssl of this CustomerConfig.
        :rtype: str
        """
        return self._ssl

    @ssl.setter
    def ssl(self, ssl):
        """Sets the ssl of this CustomerConfig.

        是否使用ssl。

        :param ssl: The ssl of this CustomerConfig.
        :type: str
        """
        self._ssl = ssl

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
        if not isinstance(other, CustomerConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
