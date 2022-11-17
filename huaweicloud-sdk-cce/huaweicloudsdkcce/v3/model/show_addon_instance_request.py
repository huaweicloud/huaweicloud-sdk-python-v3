# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAddonInstanceRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'cluster_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'cluster_id': 'cluster_id'
    }

    def __init__(self, id=None, cluster_id=None):
        """ShowAddonInstanceRequest

        The model defined in huaweicloud sdk

        :param id: 插件实例id
        :type id: str
        :param cluster_id: 集群 ID，获取方式请参见[如何获取接口URI中参数](cce_02_0271.xml)
        :type cluster_id: str
        """
        
        

        self._id = None
        self._cluster_id = None
        self.discriminator = None

        self.id = id
        if cluster_id is not None:
            self.cluster_id = cluster_id

    @property
    def id(self):
        """Gets the id of this ShowAddonInstanceRequest.

        插件实例id

        :return: The id of this ShowAddonInstanceRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShowAddonInstanceRequest.

        插件实例id

        :param id: The id of this ShowAddonInstanceRequest.
        :type id: str
        """
        self._id = id

    @property
    def cluster_id(self):
        """Gets the cluster_id of this ShowAddonInstanceRequest.

        集群 ID，获取方式请参见[如何获取接口URI中参数](cce_02_0271.xml)

        :return: The cluster_id of this ShowAddonInstanceRequest.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this ShowAddonInstanceRequest.

        集群 ID，获取方式请参见[如何获取接口URI中参数](cce_02_0271.xml)

        :param cluster_id: The cluster_id of this ShowAddonInstanceRequest.
        :type cluster_id: str
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
        if not isinstance(other, ShowAddonInstanceRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
