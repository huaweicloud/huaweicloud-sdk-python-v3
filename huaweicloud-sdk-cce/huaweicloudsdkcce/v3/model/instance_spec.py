# coding: utf-8

import pprint
import re

import six





class InstanceSpec:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'addon_template_labels': 'list[str]',
        'addon_template_logo': 'str',
        'addon_template_name': 'str',
        'addon_template_type': 'str',
        'cluster_id': 'str',
        'description': 'str',
        'values': 'dict(str, object)',
        'version': 'str'
    }

    attribute_map = {
        'addon_template_labels': 'addonTemplateLabels',
        'addon_template_logo': 'addonTemplateLogo',
        'addon_template_name': 'addonTemplateName',
        'addon_template_type': 'addonTemplateType',
        'cluster_id': 'clusterID',
        'description': 'description',
        'values': 'values',
        'version': 'version'
    }

    def __init__(self, addon_template_labels=None, addon_template_logo=None, addon_template_name=None, addon_template_type=None, cluster_id=None, description=None, values=None, version=None):
        """InstanceSpec - a model defined in huaweicloud sdk"""
        
        

        self._addon_template_labels = None
        self._addon_template_logo = None
        self._addon_template_name = None
        self._addon_template_type = None
        self._cluster_id = None
        self._description = None
        self._values = None
        self._version = None
        self.discriminator = None

        if addon_template_labels is not None:
            self.addon_template_labels = addon_template_labels
        if addon_template_logo is not None:
            self.addon_template_logo = addon_template_logo
        self.addon_template_name = addon_template_name
        self.addon_template_type = addon_template_type
        self.cluster_id = cluster_id
        self.description = description
        self.values = values
        self.version = version

    @property
    def addon_template_labels(self):
        """Gets the addon_template_labels of this InstanceSpec.

        插件模板所属类型

        :return: The addon_template_labels of this InstanceSpec.
        :rtype: list[str]
        """
        return self._addon_template_labels

    @addon_template_labels.setter
    def addon_template_labels(self, addon_template_labels):
        """Sets the addon_template_labels of this InstanceSpec.

        插件模板所属类型

        :param addon_template_labels: The addon_template_labels of this InstanceSpec.
        :type: list[str]
        """
        self._addon_template_labels = addon_template_labels

    @property
    def addon_template_logo(self):
        """Gets the addon_template_logo of this InstanceSpec.

        插件logo

        :return: The addon_template_logo of this InstanceSpec.
        :rtype: str
        """
        return self._addon_template_logo

    @addon_template_logo.setter
    def addon_template_logo(self, addon_template_logo):
        """Sets the addon_template_logo of this InstanceSpec.

        插件logo

        :param addon_template_logo: The addon_template_logo of this InstanceSpec.
        :type: str
        """
        self._addon_template_logo = addon_template_logo

    @property
    def addon_template_name(self):
        """Gets the addon_template_name of this InstanceSpec.

        插件模板名称，如coredns

        :return: The addon_template_name of this InstanceSpec.
        :rtype: str
        """
        return self._addon_template_name

    @addon_template_name.setter
    def addon_template_name(self, addon_template_name):
        """Sets the addon_template_name of this InstanceSpec.

        插件模板名称，如coredns

        :param addon_template_name: The addon_template_name of this InstanceSpec.
        :type: str
        """
        self._addon_template_name = addon_template_name

    @property
    def addon_template_type(self):
        """Gets the addon_template_type of this InstanceSpec.

        插件模板类型

        :return: The addon_template_type of this InstanceSpec.
        :rtype: str
        """
        return self._addon_template_type

    @addon_template_type.setter
    def addon_template_type(self, addon_template_type):
        """Sets the addon_template_type of this InstanceSpec.

        插件模板类型

        :param addon_template_type: The addon_template_type of this InstanceSpec.
        :type: str
        """
        self._addon_template_type = addon_template_type

    @property
    def cluster_id(self):
        """Gets the cluster_id of this InstanceSpec.

        集群id

        :return: The cluster_id of this InstanceSpec.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this InstanceSpec.

        集群id

        :param cluster_id: The cluster_id of this InstanceSpec.
        :type: str
        """
        self._cluster_id = cluster_id

    @property
    def description(self):
        """Gets the description of this InstanceSpec.

        插件模板描述

        :return: The description of this InstanceSpec.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this InstanceSpec.

        插件模板描述

        :param description: The description of this InstanceSpec.
        :type: str
        """
        self._description = description

    @property
    def values(self):
        """Gets the values of this InstanceSpec.

        插件模板安装参数（各插件不同）

        :return: The values of this InstanceSpec.
        :rtype: dict(str, object)
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this InstanceSpec.

        插件模板安装参数（各插件不同）

        :param values: The values of this InstanceSpec.
        :type: dict(str, object)
        """
        self._values = values

    @property
    def version(self):
        """Gets the version of this InstanceSpec.

        插件模板版本号，如1.0.0

        :return: The version of this InstanceSpec.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this InstanceSpec.

        插件模板版本号，如1.0.0

        :param version: The version of this InstanceSpec.
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
        if not isinstance(other, InstanceSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
