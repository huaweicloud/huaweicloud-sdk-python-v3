# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateClusterReqBodyClusterInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'feature_map': 'dict(str, str)',
        'cluster_instance_info': 'list[CreateClusterInstanceBody]'
    }

    attribute_map = {
        'feature_map': 'feature_map',
        'cluster_instance_info': 'cluster_instance_info'
    }

    def __init__(self, feature_map=None, cluster_instance_info=None):
        r"""CreateClusterReqBodyClusterInfo

        The model defined in huaweicloud sdk

        :param feature_map: 特性属性开关      * 属性开关必须以enable开头，value必须为true|false      * doris: enable_broker      * hbase: storage_io_type（COMMON，ULTRAHIGH，两种取值），enable_open_tsdb（默认false，若为true需要在集群节点信息列表中指定tsd节点个数），enable_broker      示例：      \&quot;feature_map\&quot;:{\&quot;enable_broker\&quot;:\&quot;false\&quot;}       \&quot;feature_map\&quot;:{\&quot;enable_lemon\&quot;:\&quot;false\&quot;,\&quot;enable_open_tsdb\&quot;:\&quot;false\&quot;,\&quot;storage_io_type\&quot;: \&quot;COMMON\&quot;}
        :type feature_map: dict(str, str)
        :param cluster_instance_info: 集群节点信息类
        :type cluster_instance_info: list[:class:`huaweicloudsdkcloudtable.v2.CreateClusterInstanceBody`]
        """
        
        

        self._feature_map = None
        self._cluster_instance_info = None
        self.discriminator = None

        self.feature_map = feature_map
        self.cluster_instance_info = cluster_instance_info

    @property
    def feature_map(self):
        r"""Gets the feature_map of this CreateClusterReqBodyClusterInfo.

        特性属性开关      * 属性开关必须以enable开头，value必须为true|false      * doris: enable_broker      * hbase: storage_io_type（COMMON，ULTRAHIGH，两种取值），enable_open_tsdb（默认false，若为true需要在集群节点信息列表中指定tsd节点个数），enable_broker      示例：      \"feature_map\":{\"enable_broker\":\"false\"}       \"feature_map\":{\"enable_lemon\":\"false\",\"enable_open_tsdb\":\"false\",\"storage_io_type\": \"COMMON\"}

        :return: The feature_map of this CreateClusterReqBodyClusterInfo.
        :rtype: dict(str, str)
        """
        return self._feature_map

    @feature_map.setter
    def feature_map(self, feature_map):
        r"""Sets the feature_map of this CreateClusterReqBodyClusterInfo.

        特性属性开关      * 属性开关必须以enable开头，value必须为true|false      * doris: enable_broker      * hbase: storage_io_type（COMMON，ULTRAHIGH，两种取值），enable_open_tsdb（默认false，若为true需要在集群节点信息列表中指定tsd节点个数），enable_broker      示例：      \"feature_map\":{\"enable_broker\":\"false\"}       \"feature_map\":{\"enable_lemon\":\"false\",\"enable_open_tsdb\":\"false\",\"storage_io_type\": \"COMMON\"}

        :param feature_map: The feature_map of this CreateClusterReqBodyClusterInfo.
        :type feature_map: dict(str, str)
        """
        self._feature_map = feature_map

    @property
    def cluster_instance_info(self):
        r"""Gets the cluster_instance_info of this CreateClusterReqBodyClusterInfo.

        集群节点信息类

        :return: The cluster_instance_info of this CreateClusterReqBodyClusterInfo.
        :rtype: list[:class:`huaweicloudsdkcloudtable.v2.CreateClusterInstanceBody`]
        """
        return self._cluster_instance_info

    @cluster_instance_info.setter
    def cluster_instance_info(self, cluster_instance_info):
        r"""Sets the cluster_instance_info of this CreateClusterReqBodyClusterInfo.

        集群节点信息类

        :param cluster_instance_info: The cluster_instance_info of this CreateClusterReqBodyClusterInfo.
        :type cluster_instance_info: list[:class:`huaweicloudsdkcloudtable.v2.CreateClusterInstanceBody`]
        """
        self._cluster_instance_info = cluster_instance_info

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
        if not isinstance(other, CreateClusterReqBodyClusterInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
