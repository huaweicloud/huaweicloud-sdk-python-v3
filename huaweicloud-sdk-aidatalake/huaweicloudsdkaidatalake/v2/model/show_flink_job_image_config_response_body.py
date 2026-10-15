# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowFlinkJobImageConfigResponseBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'image_id': 'str',
        'image_version_id': 'str',
        'release_version': 'str',
        'image_version_type': 'str'
    }

    attribute_map = {
        'image_id': 'image_id',
        'image_version_id': 'image_version_id',
        'release_version': 'release_version',
        'image_version_type': 'image_version_type'
    }

    def __init__(self, image_id=None, image_version_id=None, release_version=None, image_version_type=None):
        r"""ShowFlinkJobImageConfigResponseBody

        The model defined in huaweicloud sdk

        :param image_id: **参数解释**：镜像ID，Flink作业运行所使用的镜像。 **取值范围**：长度为2~64个字符。
        :type image_id: str
        :param image_version_id: **参数解释**：镜像版本ID，Flink作业运行所使用的镜像版本。 **取值范围**：长度为2~64个字符。
        :type image_version_id: str
        :param release_version: **参数解释**：Flink作业的版本信息，格式为AIDataLake.&lt;平台版本&gt;(Flink&lt;Flink版本&gt;,JRE&lt;JRE版本&gt;)，例如AIDataLake.26.9.0(Flink1.20.0,JRE21)。 **取值范围**：长度为1~512个字符。
        :type release_version: str
        :param image_version_type: **参数解释**：Flink作业使用的镜像版本类型。 **取值范围**：   - STABLE：稳定版。   - RECOMMEND：推荐版。   - BETA：测试版。
        :type image_version_type: str
        """
        
        

        self._image_id = None
        self._image_version_id = None
        self._release_version = None
        self._image_version_type = None
        self.discriminator = None

        self.image_id = image_id
        self.image_version_id = image_version_id
        if release_version is not None:
            self.release_version = release_version
        if image_version_type is not None:
            self.image_version_type = image_version_type

    @property
    def image_id(self):
        r"""Gets the image_id of this ShowFlinkJobImageConfigResponseBody.

        **参数解释**：镜像ID，Flink作业运行所使用的镜像。 **取值范围**：长度为2~64个字符。

        :return: The image_id of this ShowFlinkJobImageConfigResponseBody.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        r"""Sets the image_id of this ShowFlinkJobImageConfigResponseBody.

        **参数解释**：镜像ID，Flink作业运行所使用的镜像。 **取值范围**：长度为2~64个字符。

        :param image_id: The image_id of this ShowFlinkJobImageConfigResponseBody.
        :type image_id: str
        """
        self._image_id = image_id

    @property
    def image_version_id(self):
        r"""Gets the image_version_id of this ShowFlinkJobImageConfigResponseBody.

        **参数解释**：镜像版本ID，Flink作业运行所使用的镜像版本。 **取值范围**：长度为2~64个字符。

        :return: The image_version_id of this ShowFlinkJobImageConfigResponseBody.
        :rtype: str
        """
        return self._image_version_id

    @image_version_id.setter
    def image_version_id(self, image_version_id):
        r"""Sets the image_version_id of this ShowFlinkJobImageConfigResponseBody.

        **参数解释**：镜像版本ID，Flink作业运行所使用的镜像版本。 **取值范围**：长度为2~64个字符。

        :param image_version_id: The image_version_id of this ShowFlinkJobImageConfigResponseBody.
        :type image_version_id: str
        """
        self._image_version_id = image_version_id

    @property
    def release_version(self):
        r"""Gets the release_version of this ShowFlinkJobImageConfigResponseBody.

        **参数解释**：Flink作业的版本信息，格式为AIDataLake.<平台版本>(Flink<Flink版本>,JRE<JRE版本>)，例如AIDataLake.26.9.0(Flink1.20.0,JRE21)。 **取值范围**：长度为1~512个字符。

        :return: The release_version of this ShowFlinkJobImageConfigResponseBody.
        :rtype: str
        """
        return self._release_version

    @release_version.setter
    def release_version(self, release_version):
        r"""Sets the release_version of this ShowFlinkJobImageConfigResponseBody.

        **参数解释**：Flink作业的版本信息，格式为AIDataLake.<平台版本>(Flink<Flink版本>,JRE<JRE版本>)，例如AIDataLake.26.9.0(Flink1.20.0,JRE21)。 **取值范围**：长度为1~512个字符。

        :param release_version: The release_version of this ShowFlinkJobImageConfigResponseBody.
        :type release_version: str
        """
        self._release_version = release_version

    @property
    def image_version_type(self):
        r"""Gets the image_version_type of this ShowFlinkJobImageConfigResponseBody.

        **参数解释**：Flink作业使用的镜像版本类型。 **取值范围**：   - STABLE：稳定版。   - RECOMMEND：推荐版。   - BETA：测试版。

        :return: The image_version_type of this ShowFlinkJobImageConfigResponseBody.
        :rtype: str
        """
        return self._image_version_type

    @image_version_type.setter
    def image_version_type(self, image_version_type):
        r"""Sets the image_version_type of this ShowFlinkJobImageConfigResponseBody.

        **参数解释**：Flink作业使用的镜像版本类型。 **取值范围**：   - STABLE：稳定版。   - RECOMMEND：推荐版。   - BETA：测试版。

        :param image_version_type: The image_version_type of this ShowFlinkJobImageConfigResponseBody.
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
        if not isinstance(other, ShowFlinkJobImageConfigResponseBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
