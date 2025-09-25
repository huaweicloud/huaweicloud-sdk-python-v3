# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CCEClusterIdListRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cluster_id_list': 'list[str]',
        'detect_type': 'str'
    }

    attribute_map = {
        'cluster_id_list': 'cluster_id_list',
        'detect_type': 'detect_type'
    }

    def __init__(self, cluster_id_list=None, detect_type=None):
        r"""CCEClusterIdListRequestBody

        The model defined in huaweicloud sdk

        :param cluster_id_list: 集群id列表
        :type cluster_id_list: list[str]
        :param detect_type: 查询类型，包含如下:     - image : 镜像风险     - baseline : 基线风险     - vul : 漏洞风险     - event : 入侵风险
        :type detect_type: str
        """
        
        

        self._cluster_id_list = None
        self._detect_type = None
        self.discriminator = None

        self.cluster_id_list = cluster_id_list
        if detect_type is not None:
            self.detect_type = detect_type

    @property
    def cluster_id_list(self):
        r"""Gets the cluster_id_list of this CCEClusterIdListRequestBody.

        集群id列表

        :return: The cluster_id_list of this CCEClusterIdListRequestBody.
        :rtype: list[str]
        """
        return self._cluster_id_list

    @cluster_id_list.setter
    def cluster_id_list(self, cluster_id_list):
        r"""Sets the cluster_id_list of this CCEClusterIdListRequestBody.

        集群id列表

        :param cluster_id_list: The cluster_id_list of this CCEClusterIdListRequestBody.
        :type cluster_id_list: list[str]
        """
        self._cluster_id_list = cluster_id_list

    @property
    def detect_type(self):
        r"""Gets the detect_type of this CCEClusterIdListRequestBody.

        查询类型，包含如下:     - image : 镜像风险     - baseline : 基线风险     - vul : 漏洞风险     - event : 入侵风险

        :return: The detect_type of this CCEClusterIdListRequestBody.
        :rtype: str
        """
        return self._detect_type

    @detect_type.setter
    def detect_type(self, detect_type):
        r"""Sets the detect_type of this CCEClusterIdListRequestBody.

        查询类型，包含如下:     - image : 镜像风险     - baseline : 基线风险     - vul : 漏洞风险     - event : 入侵风险

        :param detect_type: The detect_type of this CCEClusterIdListRequestBody.
        :type detect_type: str
        """
        self._detect_type = detect_type

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
        if not isinstance(other, CCEClusterIdListRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
