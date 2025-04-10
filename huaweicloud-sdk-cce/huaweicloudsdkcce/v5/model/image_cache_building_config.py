# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImageCacheBuildingConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cluster': 'str',
        'image_pull_secrets': 'list[str]'
    }

    attribute_map = {
        'cluster': 'cluster',
        'image_pull_secrets': 'image_pull_secrets'
    }

    def __init__(self, cluster=None, image_pull_secrets=None):
        r"""ImageCacheBuildingConfig

        The model defined in huaweicloud sdk

        :param cluster: **参数解释：** 构建镜像缓存所启动的临时Pod所在的Autopilot集群的UID。 **约束限制：** 要求使用的Autopilot集群版本为v1.28.8-r0或v1.31.4-r0以上版本。 **取值范围：** 不涉及 **默认取值：** 不涉及 
        :type cluster: str
        :param image_pull_secrets: 下载所需缓存镜像的访问凭证列表，不填写或无有效凭证时仅支持下载公共镜像。
        :type image_pull_secrets: list[str]
        """
        
        

        self._cluster = None
        self._image_pull_secrets = None
        self.discriminator = None

        self.cluster = cluster
        if image_pull_secrets is not None:
            self.image_pull_secrets = image_pull_secrets

    @property
    def cluster(self):
        r"""Gets the cluster of this ImageCacheBuildingConfig.

        **参数解释：** 构建镜像缓存所启动的临时Pod所在的Autopilot集群的UID。 **约束限制：** 要求使用的Autopilot集群版本为v1.28.8-r0或v1.31.4-r0以上版本。 **取值范围：** 不涉及 **默认取值：** 不涉及 

        :return: The cluster of this ImageCacheBuildingConfig.
        :rtype: str
        """
        return self._cluster

    @cluster.setter
    def cluster(self, cluster):
        r"""Sets the cluster of this ImageCacheBuildingConfig.

        **参数解释：** 构建镜像缓存所启动的临时Pod所在的Autopilot集群的UID。 **约束限制：** 要求使用的Autopilot集群版本为v1.28.8-r0或v1.31.4-r0以上版本。 **取值范围：** 不涉及 **默认取值：** 不涉及 

        :param cluster: The cluster of this ImageCacheBuildingConfig.
        :type cluster: str
        """
        self._cluster = cluster

    @property
    def image_pull_secrets(self):
        r"""Gets the image_pull_secrets of this ImageCacheBuildingConfig.

        下载所需缓存镜像的访问凭证列表，不填写或无有效凭证时仅支持下载公共镜像。

        :return: The image_pull_secrets of this ImageCacheBuildingConfig.
        :rtype: list[str]
        """
        return self._image_pull_secrets

    @image_pull_secrets.setter
    def image_pull_secrets(self, image_pull_secrets):
        r"""Sets the image_pull_secrets of this ImageCacheBuildingConfig.

        下载所需缓存镜像的访问凭证列表，不填写或无有效凭证时仅支持下载公共镜像。

        :param image_pull_secrets: The image_pull_secrets of this ImageCacheBuildingConfig.
        :type image_pull_secrets: list[str]
        """
        self._image_pull_secrets = image_pull_secrets

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
        if not isinstance(other, ImageCacheBuildingConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
