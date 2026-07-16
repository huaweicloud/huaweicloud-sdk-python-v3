# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListEnginesImageInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cpu_image_url': 'str',
        'gpu_image_url': 'str',
        'image_version': 'str'
    }

    attribute_map = {
        'cpu_image_url': 'cpu_image_url',
        'gpu_image_url': 'gpu_image_url',
        'image_version': 'image_version'
    }

    def __init__(self, cpu_image_url=None, gpu_image_url=None, image_version=None):
        r"""ListEnginesImageInfo

        The model defined in huaweicloud sdk

        :param cpu_image_url: cpu规格下对应镜像。
        :type cpu_image_url: str
        :param gpu_image_url: gpu[或者Ascend](tag:hc,hk,fcs_super)规格下对应镜像。
        :type gpu_image_url: str
        :param image_version: 镜像版本。
        :type image_version: str
        """
        
        

        self._cpu_image_url = None
        self._gpu_image_url = None
        self._image_version = None
        self.discriminator = None

        if cpu_image_url is not None:
            self.cpu_image_url = cpu_image_url
        if gpu_image_url is not None:
            self.gpu_image_url = gpu_image_url
        if image_version is not None:
            self.image_version = image_version

    @property
    def cpu_image_url(self):
        r"""Gets the cpu_image_url of this ListEnginesImageInfo.

        cpu规格下对应镜像。

        :return: The cpu_image_url of this ListEnginesImageInfo.
        :rtype: str
        """
        return self._cpu_image_url

    @cpu_image_url.setter
    def cpu_image_url(self, cpu_image_url):
        r"""Sets the cpu_image_url of this ListEnginesImageInfo.

        cpu规格下对应镜像。

        :param cpu_image_url: The cpu_image_url of this ListEnginesImageInfo.
        :type cpu_image_url: str
        """
        self._cpu_image_url = cpu_image_url

    @property
    def gpu_image_url(self):
        r"""Gets the gpu_image_url of this ListEnginesImageInfo.

        gpu[或者Ascend](tag:hc,hk,fcs_super)规格下对应镜像。

        :return: The gpu_image_url of this ListEnginesImageInfo.
        :rtype: str
        """
        return self._gpu_image_url

    @gpu_image_url.setter
    def gpu_image_url(self, gpu_image_url):
        r"""Sets the gpu_image_url of this ListEnginesImageInfo.

        gpu[或者Ascend](tag:hc,hk,fcs_super)规格下对应镜像。

        :param gpu_image_url: The gpu_image_url of this ListEnginesImageInfo.
        :type gpu_image_url: str
        """
        self._gpu_image_url = gpu_image_url

    @property
    def image_version(self):
        r"""Gets the image_version of this ListEnginesImageInfo.

        镜像版本。

        :return: The image_version of this ListEnginesImageInfo.
        :rtype: str
        """
        return self._image_version

    @image_version.setter
    def image_version(self, image_version):
        r"""Sets the image_version of this ListEnginesImageInfo.

        镜像版本。

        :param image_version: The image_version of this ListEnginesImageInfo.
        :type image_version: str
        """
        self._image_version = image_version

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
        if not isinstance(other, ListEnginesImageInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
