# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


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
        'cluster_id': 'str',
        'version': 'str',
        'addon_template_name': 'str',
        'addon_template_type': 'str',
        'addon_template_logo': 'str',
        'addon_template_labels': 'list[str]',
        'description': 'str',
        'values': 'dict(str, object)'
    }

    attribute_map = {
        'cluster_id': 'clusterID',
        'version': 'version',
        'addon_template_name': 'addonTemplateName',
        'addon_template_type': 'addonTemplateType',
        'addon_template_logo': 'addonTemplateLogo',
        'addon_template_labels': 'addonTemplateLabels',
        'description': 'description',
        'values': 'values'
    }

    def __init__(self, cluster_id=None, version=None, addon_template_name=None, addon_template_type=None, addon_template_logo=None, addon_template_labels=None, description=None, values=None):
        r"""InstanceSpec

        The model defined in huaweicloud sdk

        :param cluster_id: 集群id
        :type cluster_id: str
        :param version: 插件模板版本号，如1.0.0
        :type version: str
        :param addon_template_name: 插件模板名称，如coredns
        :type addon_template_name: str
        :param addon_template_type: 插件模板类型
        :type addon_template_type: str
        :param addon_template_logo: 插件模板logo图片的地址
        :type addon_template_logo: str
        :param addon_template_labels: 插件模板所属类型
        :type addon_template_labels: list[str]
        :param description: 插件模板描述
        :type description: str
        :param values: 插件模板安装参数（各插件不同），请根据具体插件模板信息填写安装参数。
        :type values: dict(str, object)
        """
        
        

        self._cluster_id = None
        self._version = None
        self._addon_template_name = None
        self._addon_template_type = None
        self._addon_template_logo = None
        self._addon_template_labels = None
        self._description = None
        self._values = None
        self.discriminator = None

        self.cluster_id = cluster_id
        self.version = version
        self.addon_template_name = addon_template_name
        self.addon_template_type = addon_template_type
        if addon_template_logo is not None:
            self.addon_template_logo = addon_template_logo
        if addon_template_labels is not None:
            self.addon_template_labels = addon_template_labels
        self.description = description
        self.values = values

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this InstanceSpec.

        集群id

        :return: The cluster_id of this InstanceSpec.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this InstanceSpec.

        集群id

        :param cluster_id: The cluster_id of this InstanceSpec.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def version(self):
        r"""Gets the version of this InstanceSpec.

        插件模板版本号，如1.0.0

        :return: The version of this InstanceSpec.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this InstanceSpec.

        插件模板版本号，如1.0.0

        :param version: The version of this InstanceSpec.
        :type version: str
        """
        self._version = version

    @property
    def addon_template_name(self):
        r"""Gets the addon_template_name of this InstanceSpec.

        插件模板名称，如coredns

        :return: The addon_template_name of this InstanceSpec.
        :rtype: str
        """
        return self._addon_template_name

    @addon_template_name.setter
    def addon_template_name(self, addon_template_name):
        r"""Sets the addon_template_name of this InstanceSpec.

        插件模板名称，如coredns

        :param addon_template_name: The addon_template_name of this InstanceSpec.
        :type addon_template_name: str
        """
        self._addon_template_name = addon_template_name

    @property
    def addon_template_type(self):
        r"""Gets the addon_template_type of this InstanceSpec.

        插件模板类型

        :return: The addon_template_type of this InstanceSpec.
        :rtype: str
        """
        return self._addon_template_type

    @addon_template_type.setter
    def addon_template_type(self, addon_template_type):
        r"""Sets the addon_template_type of this InstanceSpec.

        插件模板类型

        :param addon_template_type: The addon_template_type of this InstanceSpec.
        :type addon_template_type: str
        """
        self._addon_template_type = addon_template_type

    @property
    def addon_template_logo(self):
        r"""Gets the addon_template_logo of this InstanceSpec.

        插件模板logo图片的地址

        :return: The addon_template_logo of this InstanceSpec.
        :rtype: str
        """
        return self._addon_template_logo

    @addon_template_logo.setter
    def addon_template_logo(self, addon_template_logo):
        r"""Sets the addon_template_logo of this InstanceSpec.

        插件模板logo图片的地址

        :param addon_template_logo: The addon_template_logo of this InstanceSpec.
        :type addon_template_logo: str
        """
        self._addon_template_logo = addon_template_logo

    @property
    def addon_template_labels(self):
        r"""Gets the addon_template_labels of this InstanceSpec.

        插件模板所属类型

        :return: The addon_template_labels of this InstanceSpec.
        :rtype: list[str]
        """
        return self._addon_template_labels

    @addon_template_labels.setter
    def addon_template_labels(self, addon_template_labels):
        r"""Sets the addon_template_labels of this InstanceSpec.

        插件模板所属类型

        :param addon_template_labels: The addon_template_labels of this InstanceSpec.
        :type addon_template_labels: list[str]
        """
        self._addon_template_labels = addon_template_labels

    @property
    def description(self):
        r"""Gets the description of this InstanceSpec.

        插件模板描述

        :return: The description of this InstanceSpec.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this InstanceSpec.

        插件模板描述

        :param description: The description of this InstanceSpec.
        :type description: str
        """
        self._description = description

    @property
    def values(self):
        r"""Gets the values of this InstanceSpec.

        插件模板安装参数（各插件不同），请根据具体插件模板信息填写安装参数。

        :return: The values of this InstanceSpec.
        :rtype: dict(str, object)
        """
        return self._values

    @values.setter
    def values(self, values):
        r"""Sets the values of this InstanceSpec.

        插件模板安装参数（各插件不同），请根据具体插件模板信息填写安装参数。

        :param values: The values of this InstanceSpec.
        :type values: dict(str, object)
        """
        self._values = values

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
        if not isinstance(other, InstanceSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
