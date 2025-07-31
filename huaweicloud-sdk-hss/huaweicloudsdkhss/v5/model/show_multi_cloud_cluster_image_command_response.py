# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowMultiCloudClusterImageCommandResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'image_command': 'str',
        'secret_command': 'str',
        'images_download_url': 'str'
    }

    attribute_map = {
        'image_command': 'image_command',
        'secret_command': 'secret_command',
        'images_download_url': 'images_download_url'
    }

    def __init__(self, image_command=None, secret_command=None, images_download_url=None):
        r"""ShowMultiCloudClusterImageCommandResponse

        The model defined in huaweicloud sdk

        :param image_command: 上传镜像指令
        :type image_command: str
        :param secret_command: 安装凭证指令
        :type secret_command: str
        :param images_download_url: 镜像下载链接
        :type images_download_url: str
        """
        
        super(ShowMultiCloudClusterImageCommandResponse, self).__init__()

        self._image_command = None
        self._secret_command = None
        self._images_download_url = None
        self.discriminator = None

        if image_command is not None:
            self.image_command = image_command
        if secret_command is not None:
            self.secret_command = secret_command
        if images_download_url is not None:
            self.images_download_url = images_download_url

    @property
    def image_command(self):
        r"""Gets the image_command of this ShowMultiCloudClusterImageCommandResponse.

        上传镜像指令

        :return: The image_command of this ShowMultiCloudClusterImageCommandResponse.
        :rtype: str
        """
        return self._image_command

    @image_command.setter
    def image_command(self, image_command):
        r"""Sets the image_command of this ShowMultiCloudClusterImageCommandResponse.

        上传镜像指令

        :param image_command: The image_command of this ShowMultiCloudClusterImageCommandResponse.
        :type image_command: str
        """
        self._image_command = image_command

    @property
    def secret_command(self):
        r"""Gets the secret_command of this ShowMultiCloudClusterImageCommandResponse.

        安装凭证指令

        :return: The secret_command of this ShowMultiCloudClusterImageCommandResponse.
        :rtype: str
        """
        return self._secret_command

    @secret_command.setter
    def secret_command(self, secret_command):
        r"""Sets the secret_command of this ShowMultiCloudClusterImageCommandResponse.

        安装凭证指令

        :param secret_command: The secret_command of this ShowMultiCloudClusterImageCommandResponse.
        :type secret_command: str
        """
        self._secret_command = secret_command

    @property
    def images_download_url(self):
        r"""Gets the images_download_url of this ShowMultiCloudClusterImageCommandResponse.

        镜像下载链接

        :return: The images_download_url of this ShowMultiCloudClusterImageCommandResponse.
        :rtype: str
        """
        return self._images_download_url

    @images_download_url.setter
    def images_download_url(self, images_download_url):
        r"""Sets the images_download_url of this ShowMultiCloudClusterImageCommandResponse.

        镜像下载链接

        :param images_download_url: The images_download_url of this ShowMultiCloudClusterImageCommandResponse.
        :type images_download_url: str
        """
        self._images_download_url = images_download_url

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
        if not isinstance(other, ShowMultiCloudClusterImageCommandResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
