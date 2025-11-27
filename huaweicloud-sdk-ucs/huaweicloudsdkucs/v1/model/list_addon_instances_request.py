# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


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
        'cluster_id': 'str',
        'addon_template_name': 'str',
        'is_database_status': 'str'
    }

    attribute_map = {
        'cluster_id': 'cluster_id',
        'addon_template_name': 'addon_template_name',
        'is_database_status': 'is_database_status'
    }

    def __init__(self, cluster_id=None, addon_template_name=None, is_database_status=None):
        r"""ListAddonInstancesRequest

        The model defined in huaweicloud sdk

        :param cluster_id: 集群id
        :type cluster_id: str
        :param addon_template_name: 是否使用数据库存储的插件状态
        :type addon_template_name: str
        :param is_database_status: 插件包名字
        :type is_database_status: str
        """
        
        

        self._cluster_id = None
        self._addon_template_name = None
        self._is_database_status = None
        self.discriminator = None

        self.cluster_id = cluster_id
        if addon_template_name is not None:
            self.addon_template_name = addon_template_name
        if is_database_status is not None:
            self.is_database_status = is_database_status

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this ListAddonInstancesRequest.

        集群id

        :return: The cluster_id of this ListAddonInstancesRequest.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this ListAddonInstancesRequest.

        集群id

        :param cluster_id: The cluster_id of this ListAddonInstancesRequest.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def addon_template_name(self):
        r"""Gets the addon_template_name of this ListAddonInstancesRequest.

        是否使用数据库存储的插件状态

        :return: The addon_template_name of this ListAddonInstancesRequest.
        :rtype: str
        """
        return self._addon_template_name

    @addon_template_name.setter
    def addon_template_name(self, addon_template_name):
        r"""Sets the addon_template_name of this ListAddonInstancesRequest.

        是否使用数据库存储的插件状态

        :param addon_template_name: The addon_template_name of this ListAddonInstancesRequest.
        :type addon_template_name: str
        """
        self._addon_template_name = addon_template_name

    @property
    def is_database_status(self):
        r"""Gets the is_database_status of this ListAddonInstancesRequest.

        插件包名字

        :return: The is_database_status of this ListAddonInstancesRequest.
        :rtype: str
        """
        return self._is_database_status

    @is_database_status.setter
    def is_database_status(self, is_database_status):
        r"""Sets the is_database_status of this ListAddonInstancesRequest.

        插件包名字

        :param is_database_status: The is_database_status of this ListAddonInstancesRequest.
        :type is_database_status: str
        """
        self._is_database_status = is_database_status

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
        if not isinstance(other, ListAddonInstancesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
