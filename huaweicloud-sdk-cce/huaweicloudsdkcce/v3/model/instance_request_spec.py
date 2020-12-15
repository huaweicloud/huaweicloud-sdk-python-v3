# coding: utf-8

import pprint
import re

import six





class InstanceRequestSpec:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'addon_template_name': 'str',
        'cluster_id': 'str',
        'values': 'dict(str, object)',
        'version': 'str'
    }

    attribute_map = {
        'addon_template_name': 'addonTemplateName',
        'cluster_id': 'clusterID',
        'values': 'values',
        'version': 'version'
    }

    def __init__(self, addon_template_name=None, cluster_id=None, values=None, version=None):
        """InstanceRequestSpec - a model defined in huaweicloud sdk"""
        
        

        self._addon_template_name = None
        self._cluster_id = None
        self._values = None
        self._version = None
        self.discriminator = None

        self.addon_template_name = addon_template_name
        self.cluster_id = cluster_id
        self.values = values
        self.version = version

    @property
    def addon_template_name(self):
        """Gets the addon_template_name of this InstanceRequestSpec.

        待安装插件模板名称，如coredns

        :return: The addon_template_name of this InstanceRequestSpec.
        :rtype: str
        """
        return self._addon_template_name

    @addon_template_name.setter
    def addon_template_name(self, addon_template_name):
        """Sets the addon_template_name of this InstanceRequestSpec.

        待安装插件模板名称，如coredns

        :param addon_template_name: The addon_template_name of this InstanceRequestSpec.
        :type: str
        """
        self._addon_template_name = addon_template_name

    @property
    def cluster_id(self):
        """Gets the cluster_id of this InstanceRequestSpec.

        集群id

        :return: The cluster_id of this InstanceRequestSpec.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this InstanceRequestSpec.

        集群id

        :param cluster_id: The cluster_id of this InstanceRequestSpec.
        :type: str
        """
        self._cluster_id = cluster_id

    @property
    def values(self):
        """Gets the values of this InstanceRequestSpec.

        插件模板安装参数（各插件不同）

        :return: The values of this InstanceRequestSpec.
        :rtype: dict(str, object)
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this InstanceRequestSpec.

        插件模板安装参数（各插件不同）

        :param values: The values of this InstanceRequestSpec.
        :type: dict(str, object)
        """
        self._values = values

    @property
    def version(self):
        """Gets the version of this InstanceRequestSpec.

        待安装、升级插件的具体版本版本号，例如1.0.0

        :return: The version of this InstanceRequestSpec.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this InstanceRequestSpec.

        待安装、升级插件的具体版本版本号，例如1.0.0

        :param version: The version of this InstanceRequestSpec.
        :type: str
        """
        self._version = version

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InstanceRequestSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
