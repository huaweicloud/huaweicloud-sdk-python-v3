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
        'video_making_type': 'str',
        'human_image': 'str',
        'model_asset_id': 'str',
        'model_asset_type': 'str',
        'create_time': 'str',
        'update_time': 'str'
    }

    attribute_map = {
        'script_id': 'script_id',
        'script_name': 'script_name',
        'script_description': 'script_description',
        'video_making_type': 'video_making_type',
        'human_image': 'human_image',
        'model_asset_id': 'model_asset_id',
        'model_asset_type': 'model_asset_type',
        'create_time': 'create_time',
        'update_time': 'update_time'
    }

    def __init__(self, script_id=None, script_name=None, script_description=None, video_making_type=None, human_image=None, model_asset_id=None, model_asset_type=None, create_time=None, update_time=None):
        """VideoScriptBaseInfo

        The model defined in huaweicloud sdk

        :param script_id: 剧本ID。
        :type script_id: str
        :param script_name: 剧本名称。
        :type script_name: str
        :param script_description: 剧本描述。
        :type script_description: str
        :param video_making_type: 视频生成类型。该参数取值是MODEL时，model_asset_id必填；取值是PICTURE时，human_image必填。 * MODEL：通过分数数字人模型生成视频 * PICTURE： 通过单张照片生成视频
        :type video_making_type: str
        :param human_image: 人物照片，需要Base64编码。
        :type human_image: str
        :param model_asset_id: 数字人模型资产ID。
        :type model_asset_id: str
        :param model_asset_type: 数字人模型类型。  * HUMAN_MODEL_2D：分身数字人 * HUMAN_MODEL_3D：3D数字人
        :type model_asset_type: str
        :param create_time: 创建时间，格式遵循：RFC 3339 如\&quot;2021-01-10T08:43:17Z\&quot;。
        :type create_time: str
        :param update_time: 更新时间，格式遵循：RFC 3339 如\&quot;2021-01-10T08:43:17Z\&quot;。
        :type update_time: str
        """
        
        

        self._script_id = None
        self._script_name = None
        self._script_description = None
        self._video_making_type = None
        self._human_image = None
        self._model_asset_id = None
        self._model_asset_type = None
        self._create_time = None
        self._update_time = None
        self.discriminator = None

        self.script_id = script_id
        self.script_name = script_name
        if script_description is not None:
            self.script_description = script_description
        if video_making_type is not None:
            self.video_making_type = video_making_type
        if human_image is not None:
            self.human_image = human_image
        if model_asset_id is not None:
            self.model_asset_id = model_asset_id
        if model_asset_type is not None:
            self.model_asset_type = model_asset_type
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def script_id(self):
        """Gets the script_id of this VideoScriptBaseInfo.

        剧本ID。

        :return: The script_id of this VideoScriptBaseInfo.
        :rtype: str
        """
        return self._script_id

    @script_id.setter
    def script_id(self, script_id):
        """Sets the script_id of this VideoScriptBaseInfo.

        剧本ID。

        :param script_id: The script_id of this VideoScriptBaseInfo.
        :type script_id: str
        """
        self._script_id = script_id

    @property
    def script_name(self):
        """Gets the script_name of this VideoScriptBaseInfo.

        剧本名称。

        :return: The script_name of this VideoScriptBaseInfo.
        :rtype: str
        """
        return self._script_name

    @script_name.setter
    def script_name(self, script_name):
        """Sets the script_name of this VideoScriptBaseInfo.

        剧本名称。

        :param script_name: The script_name of this VideoScriptBaseInfo.
        :type script_name: str
        """
        self._script_name = script_name

    @property
    def script_description(self):
        """Gets the script_description of this VideoScriptBaseInfo.

        剧本描述。

        :return: The script_description of this VideoScriptBaseInfo.
        :rtype: str
        """
        return self._script_description

    @script_description.setter
    def script_description(self, script_description):
        """Sets the script_description of this VideoScriptBaseInfo.

        剧本描述。

        :param script_description: The script_description of this VideoScriptBaseInfo.
        :type script_description: str
        """
        self._script_description = script_description

    @property
    def video_making_type(self):
        """Gets the video_making_type of this VideoScriptBaseInfo.

        视频生成类型。该参数取值是MODEL时，model_asset_id必填；取值是PICTURE时，human_image必填。 * MODEL：通过分数数字人模型生成视频 * PICTURE： 通过单张照片生成视频

        :return: The video_making_type of this VideoScriptBaseInfo.
        :rtype: str
        """
        return self._video_making_type

    @video_making_type.setter
    def video_making_type(self, video_making_type):
        """Sets the video_making_type of this VideoScriptBaseInfo.

        视频生成类型。该参数取值是MODEL时，model_asset_id必填；取值是PICTURE时，human_image必填。 * MODEL：通过分数数字人模型生成视频 * PICTURE： 通过单张照片生成视频

        :param video_making_type: The video_making_type of this VideoScriptBaseInfo.
        :type video_making_type: str
        """
        self._video_making_type = video_making_type

    @property
    def human_image(self):
        """Gets the human_image of this VideoScriptBaseInfo.

        人物照片，需要Base64编码。

        :return: The human_image of this VideoScriptBaseInfo.
        :rtype: str
        """
        return self._human_image

    @human_image.setter
    def human_image(self, human_image):
        """Sets the human_image of this VideoScriptBaseInfo.

        人物照片，需要Base64编码。

        :param human_image: The human_image of this VideoScriptBaseInfo.
        :type human_image: str
        """
        self._human_image = human_image

    @property
    def model_asset_id(self):
        """Gets the model_asset_id of this VideoScriptBaseInfo.

        数字人模型资产ID。

        :return: The model_asset_id of this VideoScriptBaseInfo.
        :rtype: str
        """
        return self._model_asset_id

    @model_asset_id.setter
    def model_asset_id(self, model_asset_id):
        """Sets the model_asset_id of this VideoScriptBaseInfo.

        数字人模型资产ID。

        :param model_asset_id: The model_asset_id of this VideoScriptBaseInfo.
        :type model_asset_id: str
        """
        self._model_asset_id = model_asset_id

    @property
    def model_asset_type(self):
        """Gets the model_asset_type of this VideoScriptBaseInfo.

        数字人模型类型。  * HUMAN_MODEL_2D：分身数字人 * HUMAN_MODEL_3D：3D数字人

        :return: The model_asset_type of this VideoScriptBaseInfo.
        :rtype: str
        """
        return self._model_asset_type

    @model_asset_type.setter
    def model_asset_type(self, model_asset_type):
        """Sets the model_asset_type of this VideoScriptBaseInfo.

        数字人模型类型。  * HUMAN_MODEL_2D：分身数字人 * HUMAN_MODEL_3D：3D数字人

        :param model_asset_type: The model_asset_type of this VideoScriptBaseInfo.
        :type model_asset_type: str
        """
        self._model_asset_type = model_asset_type

    @property
    def create_time(self):
        """Gets the create_time of this VideoScriptBaseInfo.

        创建时间，格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :return: The create_time of this VideoScriptBaseInfo.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this VideoScriptBaseInfo.

        创建时间，格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :param create_time: The create_time of this VideoScriptBaseInfo.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this VideoScriptBaseInfo.

        更新时间，格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :return: The update_time of this VideoScriptBaseInfo.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this VideoScriptBaseInfo.

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
