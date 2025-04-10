# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ReadConfigResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'image_read_configs': 'list[ImageReadConfigResp]',
        'ppt_read_configs': 'list[PPTReadConfigResp]',
        'read_type': 'int',
        'read_content': 'str',
        'character_position': 'int',
        'read_content_paragragh_times': 'list[int]'
    }

    attribute_map = {
        'image_read_configs': 'image_read_configs',
        'ppt_read_configs': 'ppt_read_configs',
        'read_type': 'read_type',
        'read_content': 'read_content',
        'character_position': 'character_position',
        'read_content_paragragh_times': 'read_content_paragragh_times'
    }

    def __init__(self, image_read_configs=None, ppt_read_configs=None, read_type=None, read_content=None, character_position=None, read_content_paragragh_times=None):
        r"""ReadConfigResp

        The model defined in huaweicloud sdk

        :param image_read_configs: 图片播报配置
        :type image_read_configs: list[:class:`huaweicloudsdkcbs.v1.ImageReadConfigResp`]
        :param ppt_read_configs: ppt播报配置
        :type ppt_read_configs: list[:class:`huaweicloudsdkcbs.v1.PPTReadConfigResp`]
        :param read_type: 播报选项： 0：纯文本播报 1：图片播报 2：ppt播报 默认：0 配置哪项会校验哪项是否为空 
        :type read_type: int
        :param read_content: 纯文本播报内容。 换行符会按400ms的静音进行分割
        :type read_content: str
        :param character_position: 0：左 1：中 2：右
        :type character_position: int
        :param read_content_paragragh_times: read_content 每段播报时间
        :type read_content_paragragh_times: list[int]
        """
        
        

        self._image_read_configs = None
        self._ppt_read_configs = None
        self._read_type = None
        self._read_content = None
        self._character_position = None
        self._read_content_paragragh_times = None
        self.discriminator = None

        if image_read_configs is not None:
            self.image_read_configs = image_read_configs
        if ppt_read_configs is not None:
            self.ppt_read_configs = ppt_read_configs
        self.read_type = read_type
        if read_content is not None:
            self.read_content = read_content
        self.character_position = character_position
        if read_content_paragragh_times is not None:
            self.read_content_paragragh_times = read_content_paragragh_times

    @property
    def image_read_configs(self):
        r"""Gets the image_read_configs of this ReadConfigResp.

        图片播报配置

        :return: The image_read_configs of this ReadConfigResp.
        :rtype: list[:class:`huaweicloudsdkcbs.v1.ImageReadConfigResp`]
        """
        return self._image_read_configs

    @image_read_configs.setter
    def image_read_configs(self, image_read_configs):
        r"""Sets the image_read_configs of this ReadConfigResp.

        图片播报配置

        :param image_read_configs: The image_read_configs of this ReadConfigResp.
        :type image_read_configs: list[:class:`huaweicloudsdkcbs.v1.ImageReadConfigResp`]
        """
        self._image_read_configs = image_read_configs

    @property
    def ppt_read_configs(self):
        r"""Gets the ppt_read_configs of this ReadConfigResp.

        ppt播报配置

        :return: The ppt_read_configs of this ReadConfigResp.
        :rtype: list[:class:`huaweicloudsdkcbs.v1.PPTReadConfigResp`]
        """
        return self._ppt_read_configs

    @ppt_read_configs.setter
    def ppt_read_configs(self, ppt_read_configs):
        r"""Sets the ppt_read_configs of this ReadConfigResp.

        ppt播报配置

        :param ppt_read_configs: The ppt_read_configs of this ReadConfigResp.
        :type ppt_read_configs: list[:class:`huaweicloudsdkcbs.v1.PPTReadConfigResp`]
        """
        self._ppt_read_configs = ppt_read_configs

    @property
    def read_type(self):
        r"""Gets the read_type of this ReadConfigResp.

        播报选项： 0：纯文本播报 1：图片播报 2：ppt播报 默认：0 配置哪项会校验哪项是否为空 

        :return: The read_type of this ReadConfigResp.
        :rtype: int
        """
        return self._read_type

    @read_type.setter
    def read_type(self, read_type):
        r"""Sets the read_type of this ReadConfigResp.

        播报选项： 0：纯文本播报 1：图片播报 2：ppt播报 默认：0 配置哪项会校验哪项是否为空 

        :param read_type: The read_type of this ReadConfigResp.
        :type read_type: int
        """
        self._read_type = read_type

    @property
    def read_content(self):
        r"""Gets the read_content of this ReadConfigResp.

        纯文本播报内容。 换行符会按400ms的静音进行分割

        :return: The read_content of this ReadConfigResp.
        :rtype: str
        """
        return self._read_content

    @read_content.setter
    def read_content(self, read_content):
        r"""Sets the read_content of this ReadConfigResp.

        纯文本播报内容。 换行符会按400ms的静音进行分割

        :param read_content: The read_content of this ReadConfigResp.
        :type read_content: str
        """
        self._read_content = read_content

    @property
    def character_position(self):
        r"""Gets the character_position of this ReadConfigResp.

        0：左 1：中 2：右

        :return: The character_position of this ReadConfigResp.
        :rtype: int
        """
        return self._character_position

    @character_position.setter
    def character_position(self, character_position):
        r"""Sets the character_position of this ReadConfigResp.

        0：左 1：中 2：右

        :param character_position: The character_position of this ReadConfigResp.
        :type character_position: int
        """
        self._character_position = character_position

    @property
    def read_content_paragragh_times(self):
        r"""Gets the read_content_paragragh_times of this ReadConfigResp.

        read_content 每段播报时间

        :return: The read_content_paragragh_times of this ReadConfigResp.
        :rtype: list[int]
        """
        return self._read_content_paragragh_times

    @read_content_paragragh_times.setter
    def read_content_paragragh_times(self, read_content_paragragh_times):
        r"""Sets the read_content_paragragh_times of this ReadConfigResp.

        read_content 每段播报时间

        :param read_content_paragragh_times: The read_content_paragragh_times of this ReadConfigResp.
        :type read_content_paragragh_times: list[int]
        """
        self._read_content_paragragh_times = read_content_paragragh_times

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
        if not isinstance(other, ReadConfigResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
