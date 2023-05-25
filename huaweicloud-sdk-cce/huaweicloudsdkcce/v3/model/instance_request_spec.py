# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


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
        'version': 'str',
        'cluster_id': 'str',
        'values': 'dict(str, object)',
        'addon_template_name': 'str'
    }

    attribute_map = {
        'version': 'version',
        'cluster_id': 'clusterID',
        'values': 'values',
        'addon_template_name': 'addonTemplateName'
    }

    def __init__(self, version=None, cluster_id=None, values=None, addon_template_name=None):
        """InstanceRequestSpec

        The model defined in huaweicloud sdk

        :param version: 待安装、升级插件的版本号，例如1.0.0 - 安装：该参数非必传，如果不传，匹配集群支持的最新版本 - 升级：该参数必传，需指定版本号 
        :type version: str
        :param cluster_id: 集群id
        :type cluster_id: str
        :param values: 插件模板安装参数（各插件不同），升级插件时需要填写全量安装参数，未填写参数将使用插件模板中的默认值，当前插件安装参数可通过查询插件实例接口获取。 
        :type values: dict(str, object)
        :param addon_template_name: 待安装插件模板名称，如coredns
        :type addon_template_name: str
        """
        
        

        self._version = None
        self._cluster_id = None
        self._values = None
        self._addon_template_name = None
        self.discriminator = None

        if version is not None:
            self.version = version
        self.cluster_id = cluster_id
        self.values = values
        self.addon_template_name = addon_template_name

    @property
    def version(self):
        """Gets the version of this InstanceRequestSpec.

        待安装、升级插件的版本号，例如1.0.0 - 安装：该参数非必传，如果不传，匹配集群支持的最新版本 - 升级：该参数必传，需指定版本号 

        :return: The version of this InstanceRequestSpec.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this InstanceRequestSpec.

        待安装、升级插件的版本号，例如1.0.0 - 安装：该参数非必传，如果不传，匹配集群支持的最新版本 - 升级：该参数必传，需指定版本号 

        :param version: The version of this InstanceRequestSpec.
        :type version: str
        """
        self._version = version

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
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def values(self):
        """Gets the values of this InstanceRequestSpec.

        插件模板安装参数（各插件不同），升级插件时需要填写全量安装参数，未填写参数将使用插件模板中的默认值，当前插件安装参数可通过查询插件实例接口获取。 

        :return: The values of this InstanceRequestSpec.
        :rtype: dict(str, object)
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this InstanceRequestSpec.

        插件模板安装参数（各插件不同），升级插件时需要填写全量安装参数，未填写参数将使用插件模板中的默认值，当前插件安装参数可通过查询插件实例接口获取。 

        :param values: The values of this InstanceRequestSpec.
        :type values: dict(str, object)
        """
        self._values = values

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
        :type addon_template_name: str
        """
        self._addon_template_name = addon_template_name

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
        if not isinstance(other, InstanceRequestSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
