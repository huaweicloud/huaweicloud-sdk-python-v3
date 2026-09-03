# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSparkSqlImageConfigResponse:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'release_version': 'str',
        'image_version_type': 'str'
    }

    attribute_map = {
        'release_version': 'release_version',
        'image_version_type': 'image_version_type'
    }

    def __init__(self, release_version=None, image_version_type=None):
        r"""ShowSparkSqlImageConfigResponse

        The model defined in huaweicloud sdk

        :param release_version: **参数解释**：SparkSql集群的版本信息(AIDalake.xxx(Sparkx.xx.x,JRExx.x))。 **取值范围**：长度为1~512个字符。
        :type release_version: str
        :param image_version_type: **参数解释**：SparkSql集群使用的镜像版本类型。 **取值范围**： - STABLE：稳定。 - RECOMMEND：推荐。 - BETA：测试。
        :type image_version_type: str
        """
        
        

        self._release_version = None
        self._image_version_type = None
        self.discriminator = None

        if release_version is not None:
            self.release_version = release_version
        if image_version_type is not None:
            self.image_version_type = image_version_type

    @property
    def release_version(self):
        r"""Gets the release_version of this ShowSparkSqlImageConfigResponse.

        **参数解释**：SparkSql集群的版本信息(AIDalake.xxx(Sparkx.xx.x,JRExx.x))。 **取值范围**：长度为1~512个字符。

        :return: The release_version of this ShowSparkSqlImageConfigResponse.
        :rtype: str
        """
        return self._release_version

    @release_version.setter
    def release_version(self, release_version):
        r"""Sets the release_version of this ShowSparkSqlImageConfigResponse.

        **参数解释**：SparkSql集群的版本信息(AIDalake.xxx(Sparkx.xx.x,JRExx.x))。 **取值范围**：长度为1~512个字符。

        :param release_version: The release_version of this ShowSparkSqlImageConfigResponse.
        :type release_version: str
        """
        self._release_version = release_version

    @property
    def image_version_type(self):
        r"""Gets the image_version_type of this ShowSparkSqlImageConfigResponse.

        **参数解释**：SparkSql集群使用的镜像版本类型。 **取值范围**： - STABLE：稳定。 - RECOMMEND：推荐。 - BETA：测试。

        :return: The image_version_type of this ShowSparkSqlImageConfigResponse.
        :rtype: str
        """
        return self._image_version_type

    @image_version_type.setter
    def image_version_type(self, image_version_type):
        r"""Sets the image_version_type of this ShowSparkSqlImageConfigResponse.

        **参数解释**：SparkSql集群使用的镜像版本类型。 **取值范围**： - STABLE：稳定。 - RECOMMEND：推荐。 - BETA：测试。

        :param image_version_type: The image_version_type of this ShowSparkSqlImageConfigResponse.
        :type image_version_type: str
        """
        self._image_version_type = image_version_type

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
        if not isinstance(other, ShowSparkSqlImageConfigResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
