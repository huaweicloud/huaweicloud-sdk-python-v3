# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Output:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'play_type': 'str',
        'url': 'str',
        'group_id': 'str',
        'group_name': 'str',
        'encrypted': 'int',
        'quality': 'str',
        'meta_data': 'MetaData'
    }

    attribute_map = {
        'play_type': 'play_type',
        'url': 'url',
        'group_id': 'group_id',
        'group_name': 'group_name',
        'encrypted': 'encrypted',
        'quality': 'quality',
        'meta_data': 'meta_data'
    }

    def __init__(self, play_type=None, url=None, group_id=None, group_name=None, encrypted=None, quality=None, meta_data=None):
        r"""Output

        The model defined in huaweicloud sdk

        :param play_type: 协议类型。  取值如下： - hls - dash - mp4
        :type play_type: str
        :param url: 播放URL。
        :type url: str
        :param group_id: 所属转码组Id
        :type group_id: str
        :param group_name: 所属转码组名称
        :type group_name: str
        :param encrypted: 标记流是否已被加密。  取值如下： - 0：表示未加密。 - 1：表示已被加密。
        :type encrypted: int
        :param quality: 清晰度。  取值如下： - FLUENT：流畅 - SD：标清 - HD：高清 - FULL_HD：超清
        :type quality: str
        :param meta_data: 
        :type meta_data: :class:`huaweicloudsdkvod.v1.MetaData`
        """
        
        

        self._play_type = None
        self._url = None
        self._group_id = None
        self._group_name = None
        self._encrypted = None
        self._quality = None
        self._meta_data = None
        self.discriminator = None

        self.play_type = play_type
        self.url = url
        if group_id is not None:
            self.group_id = group_id
        if group_name is not None:
            self.group_name = group_name
        if encrypted is not None:
            self.encrypted = encrypted
        if quality is not None:
            self.quality = quality
        self.meta_data = meta_data

    @property
    def play_type(self):
        r"""Gets the play_type of this Output.

        协议类型。  取值如下： - hls - dash - mp4

        :return: The play_type of this Output.
        :rtype: str
        """
        return self._play_type

    @play_type.setter
    def play_type(self, play_type):
        r"""Sets the play_type of this Output.

        协议类型。  取值如下： - hls - dash - mp4

        :param play_type: The play_type of this Output.
        :type play_type: str
        """
        self._play_type = play_type

    @property
    def url(self):
        r"""Gets the url of this Output.

        播放URL。

        :return: The url of this Output.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this Output.

        播放URL。

        :param url: The url of this Output.
        :type url: str
        """
        self._url = url

    @property
    def group_id(self):
        r"""Gets the group_id of this Output.

        所属转码组Id

        :return: The group_id of this Output.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this Output.

        所属转码组Id

        :param group_id: The group_id of this Output.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def group_name(self):
        r"""Gets the group_name of this Output.

        所属转码组名称

        :return: The group_name of this Output.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        r"""Sets the group_name of this Output.

        所属转码组名称

        :param group_name: The group_name of this Output.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def encrypted(self):
        r"""Gets the encrypted of this Output.

        标记流是否已被加密。  取值如下： - 0：表示未加密。 - 1：表示已被加密。

        :return: The encrypted of this Output.
        :rtype: int
        """
        return self._encrypted

    @encrypted.setter
    def encrypted(self, encrypted):
        r"""Sets the encrypted of this Output.

        标记流是否已被加密。  取值如下： - 0：表示未加密。 - 1：表示已被加密。

        :param encrypted: The encrypted of this Output.
        :type encrypted: int
        """
        self._encrypted = encrypted

    @property
    def quality(self):
        r"""Gets the quality of this Output.

        清晰度。  取值如下： - FLUENT：流畅 - SD：标清 - HD：高清 - FULL_HD：超清

        :return: The quality of this Output.
        :rtype: str
        """
        return self._quality

    @quality.setter
    def quality(self, quality):
        r"""Sets the quality of this Output.

        清晰度。  取值如下： - FLUENT：流畅 - SD：标清 - HD：高清 - FULL_HD：超清

        :param quality: The quality of this Output.
        :type quality: str
        """
        self._quality = quality

    @property
    def meta_data(self):
        r"""Gets the meta_data of this Output.

        :return: The meta_data of this Output.
        :rtype: :class:`huaweicloudsdkvod.v1.MetaData`
        """
        return self._meta_data

    @meta_data.setter
    def meta_data(self, meta_data):
        r"""Sets the meta_data of this Output.

        :param meta_data: The meta_data of this Output.
        :type meta_data: :class:`huaweicloudsdkvod.v1.MetaData`
        """
        self._meta_data = meta_data

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
        if not isinstance(other, Output):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
