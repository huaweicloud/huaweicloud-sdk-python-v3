# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAddonTemplatesRequest:

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
        'newest': 'str',
        'cluster_id': 'str',
        'addon_template_name': 'str',
        'base_update_addon_version': 'str'
    }

    attribute_map = {
        'version': 'version',
        'newest': 'newest',
        'cluster_id': 'cluster_id',
        'addon_template_name': 'addon_template_name',
        'base_update_addon_version': 'base_update_addon_version'
    }

    def __init__(self, version=None, newest=None, cluster_id=None, addon_template_name=None, base_update_addon_version=None):
        r"""ListAddonTemplatesRequest

        The model defined in huaweicloud sdk

        :param version: 插件包版本号
        :type version: str
        :param newest: 是否获取集群内创建的最新状态
        :type newest: str
        :param cluster_id: 集群id
        :type cluster_id: str
        :param addon_template_name: 插件模板名称
        :type addon_template_name: str
        :param base_update_addon_version: 插件的最低版本
        :type base_update_addon_version: str
        """
        
        

        self._version = None
        self._newest = None
        self._cluster_id = None
        self._addon_template_name = None
        self._base_update_addon_version = None
        self.discriminator = None

        if version is not None:
            self.version = version
        if newest is not None:
            self.newest = newest
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if addon_template_name is not None:
            self.addon_template_name = addon_template_name
        if base_update_addon_version is not None:
            self.base_update_addon_version = base_update_addon_version

    @property
    def version(self):
        r"""Gets the version of this ListAddonTemplatesRequest.

        插件包版本号

        :return: The version of this ListAddonTemplatesRequest.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this ListAddonTemplatesRequest.

        插件包版本号

        :param version: The version of this ListAddonTemplatesRequest.
        :type version: str
        """
        self._version = version

    @property
    def newest(self):
        r"""Gets the newest of this ListAddonTemplatesRequest.

        是否获取集群内创建的最新状态

        :return: The newest of this ListAddonTemplatesRequest.
        :rtype: str
        """
        return self._newest

    @newest.setter
    def newest(self, newest):
        r"""Sets the newest of this ListAddonTemplatesRequest.

        是否获取集群内创建的最新状态

        :param newest: The newest of this ListAddonTemplatesRequest.
        :type newest: str
        """
        self._newest = newest

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this ListAddonTemplatesRequest.

        集群id

        :return: The cluster_id of this ListAddonTemplatesRequest.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this ListAddonTemplatesRequest.

        集群id

        :param cluster_id: The cluster_id of this ListAddonTemplatesRequest.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def addon_template_name(self):
        r"""Gets the addon_template_name of this ListAddonTemplatesRequest.

        插件模板名称

        :return: The addon_template_name of this ListAddonTemplatesRequest.
        :rtype: str
        """
        return self._addon_template_name

    @addon_template_name.setter
    def addon_template_name(self, addon_template_name):
        r"""Sets the addon_template_name of this ListAddonTemplatesRequest.

        插件模板名称

        :param addon_template_name: The addon_template_name of this ListAddonTemplatesRequest.
        :type addon_template_name: str
        """
        self._addon_template_name = addon_template_name

    @property
    def base_update_addon_version(self):
        r"""Gets the base_update_addon_version of this ListAddonTemplatesRequest.

        插件的最低版本

        :return: The base_update_addon_version of this ListAddonTemplatesRequest.
        :rtype: str
        """
        return self._base_update_addon_version

    @base_update_addon_version.setter
    def base_update_addon_version(self, base_update_addon_version):
        r"""Sets the base_update_addon_version of this ListAddonTemplatesRequest.

        插件的最低版本

        :param base_update_addon_version: The base_update_addon_version of this ListAddonTemplatesRequest.
        :type base_update_addon_version: str
        """
        self._base_update_addon_version = base_update_addon_version

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
        if not isinstance(other, ListAddonTemplatesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
