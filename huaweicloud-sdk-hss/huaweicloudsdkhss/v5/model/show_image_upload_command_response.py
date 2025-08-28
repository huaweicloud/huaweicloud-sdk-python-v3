# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowImageUploadCommandResponse(SdkResponse):

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
        'images_download_url': 'str',
        'swr_image_pull_command': 'str'
    }

    attribute_map = {
        'image_command': 'image_command',
        'images_download_url': 'images_download_url',
        'swr_image_pull_command': 'swr_image_pull_command'
    }

    def __init__(self, image_command=None, images_download_url=None, swr_image_pull_command=None):
        r"""ShowImageUploadCommandResponse

        The model defined in huaweicloud sdk

        :param image_command: **参数解释**： 上传镜像指令 **取值范围**： 字符长度1-1024位 
        :type image_command: str
        :param images_download_url: **参数解释**： 镜像下载链接 **取值范围**： 字符长度1-256位 
        :type images_download_url: str
        :param swr_image_pull_command: **参数解释**： SWR镜像获取指令 **取值范围**： 字符长度1-1024位 
        :type swr_image_pull_command: str
        """
        
        super(ShowImageUploadCommandResponse, self).__init__()

        self._image_command = None
        self._images_download_url = None
        self._swr_image_pull_command = None
        self.discriminator = None

        if image_command is not None:
            self.image_command = image_command
        if images_download_url is not None:
            self.images_download_url = images_download_url
        if swr_image_pull_command is not None:
            self.swr_image_pull_command = swr_image_pull_command

    @property
    def image_command(self):
        r"""Gets the image_command of this ShowImageUploadCommandResponse.

        **参数解释**： 上传镜像指令 **取值范围**： 字符长度1-1024位 

        :return: The image_command of this ShowImageUploadCommandResponse.
        :rtype: str
        """
        return self._image_command

    @image_command.setter
    def image_command(self, image_command):
        r"""Sets the image_command of this ShowImageUploadCommandResponse.

        **参数解释**： 上传镜像指令 **取值范围**： 字符长度1-1024位 

        :param image_command: The image_command of this ShowImageUploadCommandResponse.
        :type image_command: str
        """
        self._image_command = image_command

    @property
    def images_download_url(self):
        r"""Gets the images_download_url of this ShowImageUploadCommandResponse.

        **参数解释**： 镜像下载链接 **取值范围**： 字符长度1-256位 

        :return: The images_download_url of this ShowImageUploadCommandResponse.
        :rtype: str
        """
        return self._images_download_url

    @images_download_url.setter
    def images_download_url(self, images_download_url):
        r"""Sets the images_download_url of this ShowImageUploadCommandResponse.

        **参数解释**： 镜像下载链接 **取值范围**： 字符长度1-256位 

        :param images_download_url: The images_download_url of this ShowImageUploadCommandResponse.
        :type images_download_url: str
        """
        self._images_download_url = images_download_url

    @property
    def swr_image_pull_command(self):
        r"""Gets the swr_image_pull_command of this ShowImageUploadCommandResponse.

        **参数解释**： SWR镜像获取指令 **取值范围**： 字符长度1-1024位 

        :return: The swr_image_pull_command of this ShowImageUploadCommandResponse.
        :rtype: str
        """
        return self._swr_image_pull_command

    @swr_image_pull_command.setter
    def swr_image_pull_command(self, swr_image_pull_command):
        r"""Sets the swr_image_pull_command of this ShowImageUploadCommandResponse.

        **参数解释**： SWR镜像获取指令 **取值范围**： 字符长度1-1024位 

        :param swr_image_pull_command: The swr_image_pull_command of this ShowImageUploadCommandResponse.
        :type swr_image_pull_command: str
        """
        self._swr_image_pull_command = swr_image_pull_command

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
        if not isinstance(other, ShowImageUploadCommandResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
