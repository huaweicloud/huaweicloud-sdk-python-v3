# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EngineCreateReqEnginestateInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cluster': 'bool',
        'twin_clusters': 'bool',
        'single_engine': 'bool'
    }

    attribute_map = {
        'cluster': 'cluster',
        'twin_clusters': 'twinClusters',
        'single_engine': 'singleEngine'
    }

    def __init__(self, cluster=None, twin_clusters=None, single_engine=None):
        """EngineCreateReqEnginestateInfo

        The model defined in huaweicloud sdk

        :param cluster: 集群
        :type cluster: bool
        :param twin_clusters: 双子集群
        :type twin_clusters: bool
        :param single_engine: 单引擎
        :type single_engine: bool
        """
        
        

        self._cluster = None
        self._twin_clusters = None
        self._single_engine = None
        self.discriminator = None

        if cluster is not None:
            self.cluster = cluster
        if twin_clusters is not None:
            self.twin_clusters = twin_clusters
        if single_engine is not None:
            self.single_engine = single_engine

    @property
    def cluster(self):
        """Gets the cluster of this EngineCreateReqEnginestateInfo.

        集群

        :return: The cluster of this EngineCreateReqEnginestateInfo.
        :rtype: bool
        """
        return self._cluster

    @cluster.setter
    def cluster(self, cluster):
        """Sets the cluster of this EngineCreateReqEnginestateInfo.

        集群

        :param cluster: The cluster of this EngineCreateReqEnginestateInfo.
        :type cluster: bool
        """
        self._cluster = cluster

    @property
    def twin_clusters(self):
        """Gets the twin_clusters of this EngineCreateReqEnginestateInfo.

        双子集群

        :return: The twin_clusters of this EngineCreateReqEnginestateInfo.
        :rtype: bool
        """
        return self._twin_clusters

    @twin_clusters.setter
    def twin_clusters(self, twin_clusters):
        """Sets the twin_clusters of this EngineCreateReqEnginestateInfo.

        双子集群

        :param twin_clusters: The twin_clusters of this EngineCreateReqEnginestateInfo.
        :type twin_clusters: bool
        """
        self._twin_clusters = twin_clusters

    @property
    def single_engine(self):
        """Gets the single_engine of this EngineCreateReqEnginestateInfo.

        单引擎

        :return: The single_engine of this EngineCreateReqEnginestateInfo.
        :rtype: bool
        """
        return self._single_engine

    @single_engine.setter
    def single_engine(self, single_engine):
        """Sets the single_engine of this EngineCreateReqEnginestateInfo.

        单引擎

        :param single_engine: The single_engine of this EngineCreateReqEnginestateInfo.
        :type single_engine: bool
        """
        self._single_engine = single_engine

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
        if not isinstance(other, EngineCreateReqEnginestateInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
