# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VideoScriptBaseInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'script_id': 'str',
        'script_name': 'str',
        'script_description': 'str',
        'model_asset_id': 'str',
        'model_asset_type': 'str',
        'script_cover_url': 'str',
        'script_type': 'str',
        'text': 'str',
        'create_time': 'str',
        'update_time': 'str'
    }

    attribute_map = {
        'script_id': 'script_id',
        'script_name': 'script_name',
        'script_description': 'script_description',
        'model_asset_id': 'model_asset_id',
        'model_asset_type': 'model_asset_type',
        'script_cover_url': 'script_cover_url',
        'script_type': 'script_type',
        'text': 'text',
        'create_time': 'create_time',
        'update_time': 'update_time'
    }

    def __init__(self, script_id=None, script_name=None, script_description=None, model_asset_id=None, model_asset_type=None, script_cover_url=None, script_type=None, text=None, create_time=None, update_time=None):
        r"""VideoScriptBaseInfo

        The model defined in huaweicloud sdk

        :param script_id: 剧本ID。
        :type script_id: str
        :param script_name: 剧本名称。
        :type script_name: str
        :param script_description: 剧本描述。
        :type script_description: str
        :param model_asset_id: 数字人模型资产ID，可以从资产库中查询。
        :type model_asset_id: str
        :param model_asset_type: 数字人模型类型。  * HUMAN_MODEL_2D：分身数字人
        :type model_asset_type: str
        :param script_cover_url: 剧本封面下载url。
        :type script_cover_url: str
        :param script_type: 脚本类型，即视频制作的驱动方式。默认TEXT * TEXT: 文本驱动，即通过TTS合成语音 * AUDIO: 语音驱动
        :type script_type: str
        :param text: 台词脚本。
        :type text: str
        :param create_time: 创建时间，格式遵循：RFC 3339 如\&quot;2021-01-10T08:43:17Z\&quot;。
        :type create_time: str
        :param update_time: 更新时间，格式遵循：RFC 3339 如\&quot;2021-01-10T08:43:17Z\&quot;。
        :type update_time: str
        """
        
        

        self._script_id = None
        self._script_name = None
        self._script_description = None
        self._model_asset_id = None
        self._model_asset_type = None
        self._script_cover_url = None
        self._script_type = None
        self._text = None
        self._create_time = None
        self._update_time = None
        self.discriminator = None

        self.script_id = script_id
        self.script_name = script_name
        if script_description is not None:
            self.script_description = script_description
        if model_asset_id is not None:
            self.model_asset_id = model_asset_id
        if model_asset_type is not None:
            self.model_asset_type = model_asset_type
        if script_cover_url is not None:
            self.script_cover_url = script_cover_url
        if script_type is not None:
            self.script_type = script_type
        if text is not None:
            self.text = text
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def script_id(self):
        r"""Gets the script_id of this VideoScriptBaseInfo.

        剧本ID。

        :return: The script_id of this VideoScriptBaseInfo.
        :rtype: str
        """
        return self._script_id

    @script_id.setter
    def script_id(self, script_id):
        r"""Sets the script_id of this VideoScriptBaseInfo.

        剧本ID。

        :param script_id: The script_id of this VideoScriptBaseInfo.
        :type script_id: str
        """
        self._script_id = script_id

    @property
    def script_name(self):
        r"""Gets the script_name of this VideoScriptBaseInfo.

        剧本名称。

        :return: The script_name of this VideoScriptBaseInfo.
        :rtype: str
        """
        return self._script_name

    @script_name.setter
    def script_name(self, script_name):
        r"""Sets the script_name of this VideoScriptBaseInfo.

        剧本名称。

        :param script_name: The script_name of this VideoScriptBaseInfo.
        :type script_name: str
        """
        self._script_name = script_name

    @property
    def script_description(self):
        r"""Gets the script_description of this VideoScriptBaseInfo.

        剧本描述。

        :return: The script_description of this VideoScriptBaseInfo.
        :rtype: str
        """
        return self._script_description

    @script_description.setter
    def script_description(self, script_description):
        r"""Sets the script_description of this VideoScriptBaseInfo.

        剧本描述。

        :param script_description: The script_description of this VideoScriptBaseInfo.
        :type script_description: str
        """
        self._script_description = script_description

    @property
    def model_asset_id(self):
        r"""Gets the model_asset_id of this VideoScriptBaseInfo.

        数字人模型资产ID，可以从资产库中查询。

        :return: The model_asset_id of this VideoScriptBaseInfo.
        :rtype: str
        """
        return self._model_asset_id

    @model_asset_id.setter
    def model_asset_id(self, model_asset_id):
        r"""Sets the model_asset_id of this VideoScriptBaseInfo.

        数字人模型资产ID，可以从资产库中查询。

        :param model_asset_id: The model_asset_id of this VideoScriptBaseInfo.
        :type model_asset_id: str
        """
        self._model_asset_id = model_asset_id

    @property
    def model_asset_type(self):
        r"""Gets the model_asset_type of this VideoScriptBaseInfo.

        数字人模型类型。  * HUMAN_MODEL_2D：分身数字人

        :return: The model_asset_type of this VideoScriptBaseInfo.
        :rtype: str
        """
        return self._model_asset_type

    @model_asset_type.setter
    def model_asset_type(self, model_asset_type):
        r"""Sets the model_asset_type of this VideoScriptBaseInfo.

        数字人模型类型。  * HUMAN_MODEL_2D：分身数字人

        :param model_asset_type: The model_asset_type of this VideoScriptBaseInfo.
        :type model_asset_type: str
        """
        self._model_asset_type = model_asset_type

    @property
    def script_cover_url(self):
        r"""Gets the script_cover_url of this VideoScriptBaseInfo.

        剧本封面下载url。

        :return: The script_cover_url of this VideoScriptBaseInfo.
        :rtype: str
        """
        return self._script_cover_url

    @script_cover_url.setter
    def script_cover_url(self, script_cover_url):
        r"""Sets the script_cover_url of this VideoScriptBaseInfo.

        剧本封面下载url。

        :param script_cover_url: The script_cover_url of this VideoScriptBaseInfo.
        :type script_cover_url: str
        """
        self._script_cover_url = script_cover_url

    @property
    def script_type(self):
        r"""Gets the script_type of this VideoScriptBaseInfo.

        脚本类型，即视频制作的驱动方式。默认TEXT * TEXT: 文本驱动，即通过TTS合成语音 * AUDIO: 语音驱动

        :return: The script_type of this VideoScriptBaseInfo.
        :rtype: str
        """
        return self._script_type

    @script_type.setter
    def script_type(self, script_type):
        r"""Sets the script_type of this VideoScriptBaseInfo.

        脚本类型，即视频制作的驱动方式。默认TEXT * TEXT: 文本驱动，即通过TTS合成语音 * AUDIO: 语音驱动

        :param script_type: The script_type of this VideoScriptBaseInfo.
        :type script_type: str
        """
        self._script_type = script_type

    @property
    def text(self):
        r"""Gets the text of this VideoScriptBaseInfo.

        台词脚本。

        :return: The text of this VideoScriptBaseInfo.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        r"""Sets the text of this VideoScriptBaseInfo.

        台词脚本。

        :param text: The text of this VideoScriptBaseInfo.
        :type text: str
        """
        self._text = text

    @property
    def create_time(self):
        r"""Gets the create_time of this VideoScriptBaseInfo.

        创建时间，格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :return: The create_time of this VideoScriptBaseInfo.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this VideoScriptBaseInfo.

        创建时间，格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :param create_time: The create_time of this VideoScriptBaseInfo.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this VideoScriptBaseInfo.

        更新时间，格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :return: The update_time of this VideoScriptBaseInfo.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this VideoScriptBaseInfo.

        更新时间，格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :param update_time: The update_time of this VideoScriptBaseInfo.
        :type update_time: str
        """
        self._update_time = update_time

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
        if not isinstance(other, VideoScriptBaseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
