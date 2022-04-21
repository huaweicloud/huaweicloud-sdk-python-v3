# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowStructTemplateclusterInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'cluster_name': 'str',
        'kafka_bootstrap_servers': 'str',
        'kafka_ssl_enable': 'bool'
    }

    attribute_map = {
        'cluster_name': 'cluster_name',
        'kafka_bootstrap_servers': 'kafka_bootstrap_servers',
        'kafka_ssl_enable': 'kafka_ssl_enable'
    }

    def __init__(self, cluster_name=None, kafka_bootstrap_servers=None, kafka_ssl_enable=None):
        """ShowStructTemplateclusterInfo

        The model defined in huaweicloud sdk

        :param cluster_name: 测试
        :type cluster_name: str
        :param kafka_bootstrap_servers: 测试
        :type kafka_bootstrap_servers: str
        :param kafka_ssl_enable: 测试
        :type kafka_ssl_enable: bool
        """
        
        

        self._cluster_name = None
        self._kafka_bootstrap_servers = None
        self._kafka_ssl_enable = None
        self.discriminator = None

        if cluster_name is not None:
            self.cluster_name = cluster_name
        if kafka_bootstrap_servers is not None:
            self.kafka_bootstrap_servers = kafka_bootstrap_servers
        if kafka_ssl_enable is not None:
            self.kafka_ssl_enable = kafka_ssl_enable

    @property
    def cluster_name(self):
        """Gets the cluster_name of this ShowStructTemplateclusterInfo.

        测试

        :return: The cluster_name of this ShowStructTemplateclusterInfo.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        """Sets the cluster_name of this ShowStructTemplateclusterInfo.

        测试

        :param cluster_name: The cluster_name of this ShowStructTemplateclusterInfo.
        :type cluster_name: str
        """
        self._cluster_name = cluster_name

    @property
    def kafka_bootstrap_servers(self):
        """Gets the kafka_bootstrap_servers of this ShowStructTemplateclusterInfo.

        测试

        :return: The kafka_bootstrap_servers of this ShowStructTemplateclusterInfo.
        :rtype: str
        """
        return self._kafka_bootstrap_servers

    @kafka_bootstrap_servers.setter
    def kafka_bootstrap_servers(self, kafka_bootstrap_servers):
        """Sets the kafka_bootstrap_servers of this ShowStructTemplateclusterInfo.

        测试

        :param kafka_bootstrap_servers: The kafka_bootstrap_servers of this ShowStructTemplateclusterInfo.
        :type kafka_bootstrap_servers: str
        """
        self._kafka_bootstrap_servers = kafka_bootstrap_servers

    @property
    def kafka_ssl_enable(self):
        """Gets the kafka_ssl_enable of this ShowStructTemplateclusterInfo.

        测试

        :return: The kafka_ssl_enable of this ShowStructTemplateclusterInfo.
        :rtype: bool
        """
        return self._kafka_ssl_enable

    @kafka_ssl_enable.setter
    def kafka_ssl_enable(self, kafka_ssl_enable):
        """Sets the kafka_ssl_enable of this ShowStructTemplateclusterInfo.

        测试

        :param kafka_ssl_enable: The kafka_ssl_enable of this ShowStructTemplateclusterInfo.
        :type kafka_ssl_enable: bool
        """
        self._kafka_ssl_enable = kafka_ssl_enable

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
        if not isinstance(other, ShowStructTemplateclusterInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
