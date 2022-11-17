# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateThumbReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'input': 'ObsObjInfo',
        'output': 'ObsObjInfo',
        'user_data': 'str',
        'thumbnail_para': 'ThumbnailPara',
        'tar': 'int',
        'sync': 'int',
        'original_dir': 'int'
    }

    attribute_map = {
        'input': 'input',
        'output': 'output',
        'user_data': 'user_data',
        'thumbnail_para': 'thumbnail_para',
        'tar': 'tar',
        'sync': 'sync',
        'original_dir': 'original_dir'
    }

    def __init__(self, input=None, output=None, user_data=None, thumbnail_para=None, tar=None, sync=None, original_dir=None):
        """CreateThumbReq

        The model defined in huaweicloud sdk

        :param input: 
        :type input: :class:`huaweicloudsdkmpc.v1.ObsObjInfo`
        :param output: 
        :type output: :class:`huaweicloudsdkmpc.v1.ObsObjInfo`
        :param user_data: 用户自定义数据。 
        :type user_data: str
        :param thumbnail_para: 
        :type thumbnail_para: :class:`huaweicloudsdkmpc.v1.ThumbnailPara`
        :param tar: 是否压缩抽帧图片生成tar包。  取值如下： - 0：压缩。 - 1：不压缩 默认值：1 
        :type tar: int
        :param sync: 是否同步处理，同步处理是指不下载全部文件，快速定位到截图位置进行截图。  取值如下： - 0：排队处理。 - 1：同步处理，暂只支持按时间点截单张图。 默认值：0 
        :type sync: int
        :param original_dir: 是否使用原始输出目录。  取值如下： - 0：不使用原始输出目录，下发的输出目录后面追加随机目录，防止截图文件outputUri相同被覆盖。 - 1：使用原始输出目录。 默认值：0 
        :type original_dir: int
        """
        
        

        self._input = None
        self._output = None
        self._user_data = None
        self._thumbnail_para = None
        self._tar = None
        self._sync = None
        self._original_dir = None
        self.discriminator = None

        self.input = input
        self.output = output
        if user_data is not None:
            self.user_data = user_data
        self.thumbnail_para = thumbnail_para
        if tar is not None:
            self.tar = tar
        if sync is not None:
            self.sync = sync
        if original_dir is not None:
            self.original_dir = original_dir

    @property
    def input(self):
        """Gets the input of this CreateThumbReq.

        :return: The input of this CreateThumbReq.
        :rtype: :class:`huaweicloudsdkmpc.v1.ObsObjInfo`
        """
        return self._input

    @input.setter
    def input(self, input):
        """Sets the input of this CreateThumbReq.

        :param input: The input of this CreateThumbReq.
        :type input: :class:`huaweicloudsdkmpc.v1.ObsObjInfo`
        """
        self._input = input

    @property
    def output(self):
        """Gets the output of this CreateThumbReq.

        :return: The output of this CreateThumbReq.
        :rtype: :class:`huaweicloudsdkmpc.v1.ObsObjInfo`
        """
        return self._output

    @output.setter
    def output(self, output):
        """Sets the output of this CreateThumbReq.

        :param output: The output of this CreateThumbReq.
        :type output: :class:`huaweicloudsdkmpc.v1.ObsObjInfo`
        """
        self._output = output

    @property
    def user_data(self):
        """Gets the user_data of this CreateThumbReq.

        用户自定义数据。 

        :return: The user_data of this CreateThumbReq.
        :rtype: str
        """
        return self._user_data

    @user_data.setter
    def user_data(self, user_data):
        """Sets the user_data of this CreateThumbReq.

        用户自定义数据。 

        :param user_data: The user_data of this CreateThumbReq.
        :type user_data: str
        """
        self._user_data = user_data

    @property
    def thumbnail_para(self):
        """Gets the thumbnail_para of this CreateThumbReq.

        :return: The thumbnail_para of this CreateThumbReq.
        :rtype: :class:`huaweicloudsdkmpc.v1.ThumbnailPara`
        """
        return self._thumbnail_para

    @thumbnail_para.setter
    def thumbnail_para(self, thumbnail_para):
        """Sets the thumbnail_para of this CreateThumbReq.

        :param thumbnail_para: The thumbnail_para of this CreateThumbReq.
        :type thumbnail_para: :class:`huaweicloudsdkmpc.v1.ThumbnailPara`
        """
        self._thumbnail_para = thumbnail_para

    @property
    def tar(self):
        """Gets the tar of this CreateThumbReq.

        是否压缩抽帧图片生成tar包。  取值如下： - 0：压缩。 - 1：不压缩 默认值：1 

        :return: The tar of this CreateThumbReq.
        :rtype: int
        """
        return self._tar

    @tar.setter
    def tar(self, tar):
        """Sets the tar of this CreateThumbReq.

        是否压缩抽帧图片生成tar包。  取值如下： - 0：压缩。 - 1：不压缩 默认值：1 

        :param tar: The tar of this CreateThumbReq.
        :type tar: int
        """
        self._tar = tar

    @property
    def sync(self):
        """Gets the sync of this CreateThumbReq.

        是否同步处理，同步处理是指不下载全部文件，快速定位到截图位置进行截图。  取值如下： - 0：排队处理。 - 1：同步处理，暂只支持按时间点截单张图。 默认值：0 

        :return: The sync of this CreateThumbReq.
        :rtype: int
        """
        return self._sync

    @sync.setter
    def sync(self, sync):
        """Sets the sync of this CreateThumbReq.

        是否同步处理，同步处理是指不下载全部文件，快速定位到截图位置进行截图。  取值如下： - 0：排队处理。 - 1：同步处理，暂只支持按时间点截单张图。 默认值：0 

        :param sync: The sync of this CreateThumbReq.
        :type sync: int
        """
        self._sync = sync

    @property
    def original_dir(self):
        """Gets the original_dir of this CreateThumbReq.

        是否使用原始输出目录。  取值如下： - 0：不使用原始输出目录，下发的输出目录后面追加随机目录，防止截图文件outputUri相同被覆盖。 - 1：使用原始输出目录。 默认值：0 

        :return: The original_dir of this CreateThumbReq.
        :rtype: int
        """
        return self._original_dir

    @original_dir.setter
    def original_dir(self, original_dir):
        """Sets the original_dir of this CreateThumbReq.

        是否使用原始输出目录。  取值如下： - 0：不使用原始输出目录，下发的输出目录后面追加随机目录，防止截图文件outputUri相同被覆盖。 - 1：使用原始输出目录。 默认值：0 

        :param original_dir: The original_dir of this CreateThumbReq.
        :type original_dir: int
        """
        self._original_dir = original_dir

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
        if not isinstance(other, CreateThumbReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
