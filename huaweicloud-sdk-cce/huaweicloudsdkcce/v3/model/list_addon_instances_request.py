# coding: utf-8

import pprint
import re

import six





class ListAddonInstancesRequest:


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
        'cluster_id': 'str'
    }

    attribute_map = {
        'addon_template_name': 'addon_template_name',
        'cluster_id': 'cluster_id'
    }

    def __init__(self, addon_template_name=None, cluster_id=None):
        """ListAddonInstancesRequest - a model defined in huaweicloud sdk"""
        
        

        self._addon_template_name = None
        self._cluster_id = None
        self.discriminator = None

        if addon_template_name is not None:
            self.addon_template_name = addon_template_name
        self.cluster_id = cluster_id

    @property
    def addon_template_name(self):
        """Gets the addon_template_name of this ListAddonInstancesRequest.

        含义：想要筛选的插件名称  属性：隐藏参数

        :return: The addon_template_name of this ListAddonInstancesRequest.
        :rtype: str
        """
        return self._addon_template_name

    @addon_template_name.setter
    def addon_template_name(self, addon_template_name):
        """Sets the addon_template_name of this ListAddonInstancesRequest.

        含义：想要筛选的插件名称  属性：隐藏参数

        :param addon_template_name: The addon_template_name of this ListAddonInstancesRequest.
        :type: str
        """
        self._addon_template_name = addon_template_name

    @property
    def cluster_id(self):
        """Gets the cluster_id of this ListAddonInstancesRequest.

        集群 ID，获取方式请参见[[如何获取接口URI中参数](https://support.huaweicloud.com/api-cce/cce_02_0271.html)](tag:hws)[[如何获取接口URI中参数](https://support.huaweicloud.com/intl/zh-cn/api-cce/cce_02_0271.html)](tag:hws_hk)

        :return: The cluster_id of this ListAddonInstancesRequest.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this ListAddonInstancesRequest.

        集群 ID，获取方式请参见[[如何获取接口URI中参数](https://support.huaweicloud.com/api-cce/cce_02_0271.html)](tag:hws)[[如何获取接口URI中参数](https://support.huaweicloud.com/intl/zh-cn/api-cce/cce_02_0271.html)](tag:hws_hk)

        :param cluster_id: The cluster_id of this ListAddonInstancesRequest.
        :type: str
        """
        self._cluster_id = cluster_id

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
        if not isinstance(other, ListAddonInstancesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
