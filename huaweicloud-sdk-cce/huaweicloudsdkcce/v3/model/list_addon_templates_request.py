# coding: utf-8

import pprint
import re

import six





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
        'addon_template_name': 'str',
        'base_update_addon_version': 'str',
        'cluster_id': 'str',
        'newest': 'str',
        'version': 'str'
    }

    attribute_map = {
        'addon_template_name': 'addon_template_name',
        'base_update_addon_version': 'base_update_addon_version',
        'cluster_id': 'cluster_id',
        'newest': 'newest',
        'version': 'version'
    }

    def __init__(self, addon_template_name=None, base_update_addon_version=None, cluster_id=None, newest=None, version=None):
        """ListAddonTemplatesRequest - a model defined in huaweicloud sdk"""
        
        

        self._addon_template_name = None
        self._base_update_addon_version = None
        self._cluster_id = None
        self._newest = None
        self._version = None
        self.discriminator = None

        if addon_template_name is not None:
            self.addon_template_name = addon_template_name
        if base_update_addon_version is not None:
            self.base_update_addon_version = base_update_addon_version
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if newest is not None:
            self.newest = newest
        if version is not None:
            self.version = version

    @property
    def addon_template_name(self):
        """Gets the addon_template_name of this ListAddonTemplatesRequest.

        指定的模板名称，不填写则查询列表。

        :return: The addon_template_name of this ListAddonTemplatesRequest.
        :rtype: str
        """
        return self._addon_template_name

    @addon_template_name.setter
    def addon_template_name(self, addon_template_name):
        """Sets the addon_template_name of this ListAddonTemplatesRequest.

        指定的模板名称，不填写则查询列表。

        :param addon_template_name: The addon_template_name of this ListAddonTemplatesRequest.
        :type: str
        """
        self._addon_template_name = addon_template_name

    @property
    def base_update_addon_version(self):
        """Gets the base_update_addon_version of this ListAddonTemplatesRequest.

        含义：可接受的最低升级版本  属性：隐藏参数

        :return: The base_update_addon_version of this ListAddonTemplatesRequest.
        :rtype: str
        """
        return self._base_update_addon_version

    @base_update_addon_version.setter
    def base_update_addon_version(self, base_update_addon_version):
        """Sets the base_update_addon_version of this ListAddonTemplatesRequest.

        含义：可接受的最低升级版本  属性：隐藏参数

        :param base_update_addon_version: The base_update_addon_version of this ListAddonTemplatesRequest.
        :type: str
        """
        self._base_update_addon_version = base_update_addon_version

    @property
    def cluster_id(self):
        """Gets the cluster_id of this ListAddonTemplatesRequest.

        含义：查询的集群  属性：隐藏参数

        :return: The cluster_id of this ListAddonTemplatesRequest.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this ListAddonTemplatesRequest.

        含义：查询的集群  属性：隐藏参数

        :param cluster_id: The cluster_id of this ListAddonTemplatesRequest.
        :type: str
        """
        self._cluster_id = cluster_id

    @property
    def newest(self):
        """Gets the newest of this ListAddonTemplatesRequest.

        含义：是否获取最新插件  属性：隐藏参数

        :return: The newest of this ListAddonTemplatesRequest.
        :rtype: str
        """
        return self._newest

    @newest.setter
    def newest(self, newest):
        """Sets the newest of this ListAddonTemplatesRequest.

        含义：是否获取最新插件  属性：隐藏参数

        :param newest: The newest of this ListAddonTemplatesRequest.
        :type: str
        """
        self._newest = newest

    @property
    def version(self):
        """Gets the version of this ListAddonTemplatesRequest.

        含义：筛选的插件版本  属性：隐藏参数

        :return: The version of this ListAddonTemplatesRequest.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ListAddonTemplatesRequest.

        含义：筛选的插件版本  属性：隐藏参数

        :param version: The version of this ListAddonTemplatesRequest.
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
        if not isinstance(other, ListAddonTemplatesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
