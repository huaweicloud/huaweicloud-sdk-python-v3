# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddonInstanceSpec:

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
        'values': 'dict(str, object)',
        'parameters': 'ReleaseParams',
        'namespace': 'str'
    }

    attribute_map = {
        'cluster_id': 'clusterID',
        'version': 'version',
        'addon_template_name': 'addonTemplateName',
        'addon_template_type': 'addonTemplateType',
        'addon_template_logo': 'addonTemplateLogo',
        'addon_template_labels': 'addonTemplateLabels',
        'description': 'description',
        'values': 'values',
        'parameters': 'parameters',
        'namespace': 'namespace'
    }

    def __init__(self, cluster_id=None, version=None, addon_template_name=None, addon_template_type=None, addon_template_logo=None, addon_template_labels=None, description=None, values=None, parameters=None, namespace=None):
        r"""AddonInstanceSpec

        The model defined in huaweicloud sdk

        :param cluster_id: cluster ID信息
        :type cluster_id: str
        :param version: 插件版本信息
        :type version: str
        :param addon_template_name: 插件模板名称
        :type addon_template_name: str
        :param addon_template_type: 插件模板类型
        :type addon_template_type: str
        :param addon_template_logo: 插件模板Logo
        :type addon_template_logo: str
        :param addon_template_labels: 插件模板标签
        :type addon_template_labels: list[str]
        :param description: 信息说明
        :type description: str
        :param values: 插件实例的配置参数
        :type values: dict(str, object)
        :param parameters: 
        :type parameters: :class:`huaweicloudsdkucs.v1.ReleaseParams`
        :param namespace: 命名空间
        :type namespace: str
        """
        
        

        self._cluster_id = None
        self._version = None
        self._addon_template_name = None
        self._addon_template_type = None
        self._addon_template_logo = None
        self._addon_template_labels = None
        self._description = None
        self._values = None
        self._parameters = None
        self._namespace = None
        self.discriminator = None

        if cluster_id is not None:
            self.cluster_id = cluster_id
        if version is not None:
            self.version = version
        if addon_template_name is not None:
            self.addon_template_name = addon_template_name
        if addon_template_type is not None:
            self.addon_template_type = addon_template_type
        if addon_template_logo is not None:
            self.addon_template_logo = addon_template_logo
        if addon_template_labels is not None:
            self.addon_template_labels = addon_template_labels
        if description is not None:
            self.description = description
        if values is not None:
            self.values = values
        if parameters is not None:
            self.parameters = parameters
        if namespace is not None:
            self.namespace = namespace

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this AddonInstanceSpec.

        cluster ID信息

        :return: The cluster_id of this AddonInstanceSpec.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this AddonInstanceSpec.

        cluster ID信息

        :param cluster_id: The cluster_id of this AddonInstanceSpec.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def version(self):
        r"""Gets the version of this AddonInstanceSpec.

        插件版本信息

        :return: The version of this AddonInstanceSpec.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this AddonInstanceSpec.

        插件版本信息

        :param version: The version of this AddonInstanceSpec.
        :type version: str
        """
        self._version = version

    @property
    def addon_template_name(self):
        r"""Gets the addon_template_name of this AddonInstanceSpec.

        插件模板名称

        :return: The addon_template_name of this AddonInstanceSpec.
        :rtype: str
        """
        return self._addon_template_name

    @addon_template_name.setter
    def addon_template_name(self, addon_template_name):
        r"""Sets the addon_template_name of this AddonInstanceSpec.

        插件模板名称

        :param addon_template_name: The addon_template_name of this AddonInstanceSpec.
        :type addon_template_name: str
        """
        self._addon_template_name = addon_template_name

    @property
    def addon_template_type(self):
        r"""Gets the addon_template_type of this AddonInstanceSpec.

        插件模板类型

        :return: The addon_template_type of this AddonInstanceSpec.
        :rtype: str
        """
        return self._addon_template_type

    @addon_template_type.setter
    def addon_template_type(self, addon_template_type):
        r"""Sets the addon_template_type of this AddonInstanceSpec.

        插件模板类型

        :param addon_template_type: The addon_template_type of this AddonInstanceSpec.
        :type addon_template_type: str
        """
        self._addon_template_type = addon_template_type

    @property
    def addon_template_logo(self):
        r"""Gets the addon_template_logo of this AddonInstanceSpec.

        插件模板Logo

        :return: The addon_template_logo of this AddonInstanceSpec.
        :rtype: str
        """
        return self._addon_template_logo

    @addon_template_logo.setter
    def addon_template_logo(self, addon_template_logo):
        r"""Sets the addon_template_logo of this AddonInstanceSpec.

        插件模板Logo

        :param addon_template_logo: The addon_template_logo of this AddonInstanceSpec.
        :type addon_template_logo: str
        """
        self._addon_template_logo = addon_template_logo

    @property
    def addon_template_labels(self):
        r"""Gets the addon_template_labels of this AddonInstanceSpec.

        插件模板标签

        :return: The addon_template_labels of this AddonInstanceSpec.
        :rtype: list[str]
        """
        return self._addon_template_labels

    @addon_template_labels.setter
    def addon_template_labels(self, addon_template_labels):
        r"""Sets the addon_template_labels of this AddonInstanceSpec.

        插件模板标签

        :param addon_template_labels: The addon_template_labels of this AddonInstanceSpec.
        :type addon_template_labels: list[str]
        """
        self._addon_template_labels = addon_template_labels

    @property
    def description(self):
        r"""Gets the description of this AddonInstanceSpec.

        信息说明

        :return: The description of this AddonInstanceSpec.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this AddonInstanceSpec.

        信息说明

        :param description: The description of this AddonInstanceSpec.
        :type description: str
        """
        self._description = description

    @property
    def values(self):
        r"""Gets the values of this AddonInstanceSpec.

        插件实例的配置参数

        :return: The values of this AddonInstanceSpec.
        :rtype: dict(str, object)
        """
        return self._values

    @values.setter
    def values(self, values):
        r"""Sets the values of this AddonInstanceSpec.

        插件实例的配置参数

        :param values: The values of this AddonInstanceSpec.
        :type values: dict(str, object)
        """
        self._values = values

    @property
    def parameters(self):
        r"""Gets the parameters of this AddonInstanceSpec.

        :return: The parameters of this AddonInstanceSpec.
        :rtype: :class:`huaweicloudsdkucs.v1.ReleaseParams`
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        r"""Sets the parameters of this AddonInstanceSpec.

        :param parameters: The parameters of this AddonInstanceSpec.
        :type parameters: :class:`huaweicloudsdkucs.v1.ReleaseParams`
        """
        self._parameters = parameters

    @property
    def namespace(self):
        r"""Gets the namespace of this AddonInstanceSpec.

        命名空间

        :return: The namespace of this AddonInstanceSpec.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this AddonInstanceSpec.

        命名空间

        :param namespace: The namespace of this AddonInstanceSpec.
        :type namespace: str
        """
        self._namespace = namespace

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AddonInstanceSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
