# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListClusterProtectionItemResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_num': 'int',
        'vuls': 'list[str]',
        'baselines': 'list[ClusterBaselineResponseInfo]',
        'malwares': 'list[ClusterMalwareResponseInfo]',
        'images': 'list[ClusterImageResponseInfo]',
        'clusters': 'list[ClusterItemResponseInfo]'
    }

    attribute_map = {
        'total_num': 'total_num',
        'vuls': 'vuls',
        'baselines': 'baselines',
        'malwares': 'malwares',
        'images': 'images',
        'clusters': 'clusters'
    }

    def __init__(self, total_num=None, vuls=None, baselines=None, malwares=None, images=None, clusters=None):
        r"""ListClusterProtectionItemResponse

        The model defined in huaweicloud sdk

        :param total_num: 总数
        :type total_num: int
        :param vuls: 漏洞信息
        :type vuls: list[str]
        :param baselines: 基线信息
        :type baselines: list[:class:`huaweicloudsdkhss.v5.ClusterBaselineResponseInfo`]
        :param malwares: 恶意文件信息
        :type malwares: list[:class:`huaweicloudsdkhss.v5.ClusterMalwareResponseInfo`]
        :param images: 镜像信息
        :type images: list[:class:`huaweicloudsdkhss.v5.ClusterImageResponseInfo`]
        :param clusters: 集群信息
        :type clusters: list[:class:`huaweicloudsdkhss.v5.ClusterItemResponseInfo`]
        """
        
        super(ListClusterProtectionItemResponse, self).__init__()

        self._total_num = None
        self._vuls = None
        self._baselines = None
        self._malwares = None
        self._images = None
        self._clusters = None
        self.discriminator = None

        if total_num is not None:
            self.total_num = total_num
        if vuls is not None:
            self.vuls = vuls
        if baselines is not None:
            self.baselines = baselines
        if malwares is not None:
            self.malwares = malwares
        if images is not None:
            self.images = images
        if clusters is not None:
            self.clusters = clusters

    @property
    def total_num(self):
        r"""Gets the total_num of this ListClusterProtectionItemResponse.

        总数

        :return: The total_num of this ListClusterProtectionItemResponse.
        :rtype: int
        """
        return self._total_num

    @total_num.setter
    def total_num(self, total_num):
        r"""Sets the total_num of this ListClusterProtectionItemResponse.

        总数

        :param total_num: The total_num of this ListClusterProtectionItemResponse.
        :type total_num: int
        """
        self._total_num = total_num

    @property
    def vuls(self):
        r"""Gets the vuls of this ListClusterProtectionItemResponse.

        漏洞信息

        :return: The vuls of this ListClusterProtectionItemResponse.
        :rtype: list[str]
        """
        return self._vuls

    @vuls.setter
    def vuls(self, vuls):
        r"""Sets the vuls of this ListClusterProtectionItemResponse.

        漏洞信息

        :param vuls: The vuls of this ListClusterProtectionItemResponse.
        :type vuls: list[str]
        """
        self._vuls = vuls

    @property
    def baselines(self):
        r"""Gets the baselines of this ListClusterProtectionItemResponse.

        基线信息

        :return: The baselines of this ListClusterProtectionItemResponse.
        :rtype: list[:class:`huaweicloudsdkhss.v5.ClusterBaselineResponseInfo`]
        """
        return self._baselines

    @baselines.setter
    def baselines(self, baselines):
        r"""Sets the baselines of this ListClusterProtectionItemResponse.

        基线信息

        :param baselines: The baselines of this ListClusterProtectionItemResponse.
        :type baselines: list[:class:`huaweicloudsdkhss.v5.ClusterBaselineResponseInfo`]
        """
        self._baselines = baselines

    @property
    def malwares(self):
        r"""Gets the malwares of this ListClusterProtectionItemResponse.

        恶意文件信息

        :return: The malwares of this ListClusterProtectionItemResponse.
        :rtype: list[:class:`huaweicloudsdkhss.v5.ClusterMalwareResponseInfo`]
        """
        return self._malwares

    @malwares.setter
    def malwares(self, malwares):
        r"""Sets the malwares of this ListClusterProtectionItemResponse.

        恶意文件信息

        :param malwares: The malwares of this ListClusterProtectionItemResponse.
        :type malwares: list[:class:`huaweicloudsdkhss.v5.ClusterMalwareResponseInfo`]
        """
        self._malwares = malwares

    @property
    def images(self):
        r"""Gets the images of this ListClusterProtectionItemResponse.

        镜像信息

        :return: The images of this ListClusterProtectionItemResponse.
        :rtype: list[:class:`huaweicloudsdkhss.v5.ClusterImageResponseInfo`]
        """
        return self._images

    @images.setter
    def images(self, images):
        r"""Sets the images of this ListClusterProtectionItemResponse.

        镜像信息

        :param images: The images of this ListClusterProtectionItemResponse.
        :type images: list[:class:`huaweicloudsdkhss.v5.ClusterImageResponseInfo`]
        """
        self._images = images

    @property
    def clusters(self):
        r"""Gets the clusters of this ListClusterProtectionItemResponse.

        集群信息

        :return: The clusters of this ListClusterProtectionItemResponse.
        :rtype: list[:class:`huaweicloudsdkhss.v5.ClusterItemResponseInfo`]
        """
        return self._clusters

    @clusters.setter
    def clusters(self, clusters):
        r"""Sets the clusters of this ListClusterProtectionItemResponse.

        集群信息

        :param clusters: The clusters of this ListClusterProtectionItemResponse.
        :type clusters: list[:class:`huaweicloudsdkhss.v5.ClusterItemResponseInfo`]
        """
        self._clusters = clusters

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
        if not isinstance(other, ListClusterProtectionItemResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
