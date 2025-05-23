# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CCEClusterInfoListRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cluster_info_list': 'list[CCEClusterInfoListRequestBodyClusterInfoList]',
        'cluster_id_list': 'list[str]'
    }

    attribute_map = {
        'cluster_info_list': 'cluster_info_list',
        'cluster_id_list': 'cluster_id_list'
    }

    def __init__(self, cluster_info_list=None, cluster_id_list=None):
        r"""CCEClusterInfoListRequestBody

        The model defined in huaweicloud sdk

        :param cluster_info_list: 集群id列表
        :type cluster_info_list: list[:class:`huaweicloudsdkhss.v5.CCEClusterInfoListRequestBodyClusterInfoList`]
        :param cluster_id_list: 集群id列表
        :type cluster_id_list: list[str]
        """
        
        

        self._cluster_info_list = None
        self._cluster_id_list = None
        self.discriminator = None

        self.cluster_info_list = cluster_info_list
        if cluster_id_list is not None:
            self.cluster_id_list = cluster_id_list

    @property
    def cluster_info_list(self):
        r"""Gets the cluster_info_list of this CCEClusterInfoListRequestBody.

        集群id列表

        :return: The cluster_info_list of this CCEClusterInfoListRequestBody.
        :rtype: list[:class:`huaweicloudsdkhss.v5.CCEClusterInfoListRequestBodyClusterInfoList`]
        """
        return self._cluster_info_list

    @cluster_info_list.setter
    def cluster_info_list(self, cluster_info_list):
        r"""Sets the cluster_info_list of this CCEClusterInfoListRequestBody.

        集群id列表

        :param cluster_info_list: The cluster_info_list of this CCEClusterInfoListRequestBody.
        :type cluster_info_list: list[:class:`huaweicloudsdkhss.v5.CCEClusterInfoListRequestBodyClusterInfoList`]
        """
        self._cluster_info_list = cluster_info_list

    @property
    def cluster_id_list(self):
        r"""Gets the cluster_id_list of this CCEClusterInfoListRequestBody.

        集群id列表

        :return: The cluster_id_list of this CCEClusterInfoListRequestBody.
        :rtype: list[str]
        """
        return self._cluster_id_list

    @cluster_id_list.setter
    def cluster_id_list(self, cluster_id_list):
        r"""Sets the cluster_id_list of this CCEClusterInfoListRequestBody.

        集群id列表

        :param cluster_id_list: The cluster_id_list of this CCEClusterInfoListRequestBody.
        :type cluster_id_list: list[str]
        """
        self._cluster_id_list = cluster_id_list

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
        if not isinstance(other, CCEClusterInfoListRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
