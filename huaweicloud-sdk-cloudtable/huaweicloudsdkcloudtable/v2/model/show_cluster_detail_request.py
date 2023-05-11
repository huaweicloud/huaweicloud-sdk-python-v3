# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowClusterDetailRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_language': 'str',
        'cluster_id': 'str'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'cluster_id': 'cluster_id'
    }

    def __init__(self, x_language=None, cluster_id=None):
        """ShowClusterDetailRequest

        The model defined in huaweicloud sdk

        :param x_language: 语言类型
        :type x_language: str
        :param cluster_id: 集群ID。  获取方法：在ClooudTable控制台，单击要查询的集群名称进入集群详情页，获取“集群ID\&quot;。
        :type cluster_id: str
        """
        
        

        self._x_language = None
        self._cluster_id = None
        self.discriminator = None

        self.x_language = x_language
        self.cluster_id = cluster_id

    @property
    def x_language(self):
        """Gets the x_language of this ShowClusterDetailRequest.

        语言类型

        :return: The x_language of this ShowClusterDetailRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        """Sets the x_language of this ShowClusterDetailRequest.

        语言类型

        :param x_language: The x_language of this ShowClusterDetailRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def cluster_id(self):
        """Gets the cluster_id of this ShowClusterDetailRequest.

        集群ID。  获取方法：在ClooudTable控制台，单击要查询的集群名称进入集群详情页，获取“集群ID\"。

        :return: The cluster_id of this ShowClusterDetailRequest.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this ShowClusterDetailRequest.

        集群ID。  获取方法：在ClooudTable控制台，单击要查询的集群名称进入集群详情页，获取“集群ID\"。

        :param cluster_id: The cluster_id of this ShowClusterDetailRequest.
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
        if not isinstance(other, ShowClusterDetailRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
