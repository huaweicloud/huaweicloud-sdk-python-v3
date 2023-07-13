# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExecuteGetCharacterInfoByIdResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'create_time': 'str',
        'update_time': 'str',
        'character_name': 'str',
        'gender': 'int',
        'id': 'str',
        'name': 'str',
        'photo_url': 'str',
        'posture': 'int',
        'train_finish_time_estimate': 'str',
        'train_start_time': 'str',
        'train_status': 'int',
        'type': 'int',
        'center_photo_url': 'str',
        'error_msg': 'str',
        'left_photo_url': 'str',
        'preview_video_url': 'str',
        'right_photo_url': 'str',
        'best_img_quality_preview_url': 'str',
        'best_lip_sync_preview_url': 'str',
        'best_mouth_rec_preview_url': 'str',
        'have_segment_data': 'bool',
        'initial_video_url': 'str',
        'background_url': 'str',
        'model': 'int',
        'charater_position': 'CharacterPosition',
        'charater_dimension': 'CharacterDimension'
    }

    attribute_map = {
        'create_time': 'create_time',
        'update_time': 'update_time',
        'character_name': 'character_name',
        'gender': 'gender',
        'id': 'id',
        'name': 'name',
        'photo_url': 'photo_url',
        'posture': 'posture',
        'train_finish_time_estimate': 'train_finish_time_estimate',
        'train_start_time': 'train_start_time',
        'train_status': 'train_status',
        'type': 'type',
        'center_photo_url': 'center_photo_url',
        'error_msg': 'error_msg',
        'left_photo_url': 'left_photo_url',
        'preview_video_url': 'preview_video_url',
        'right_photo_url': 'right_photo_url',
        'best_img_quality_preview_url': 'best_img_quality_preview_url',
        'best_lip_sync_preview_url': 'best_lip_sync_preview_url',
        'best_mouth_rec_preview_url': 'best_mouth_rec_preview_url',
        'have_segment_data': 'have_segment_data',
        'initial_video_url': 'initial_video_url',
        'background_url': 'background_url',
        'model': 'model',
        'charater_position': 'charater_position',
        'charater_dimension': 'charater_dimension'
    }

    def __init__(self, create_time=None, update_time=None, character_name=None, gender=None, id=None, name=None, photo_url=None, posture=None, train_finish_time_estimate=None, train_start_time=None, train_status=None, type=None, center_photo_url=None, error_msg=None, left_photo_url=None, preview_video_url=None, right_photo_url=None, best_img_quality_preview_url=None, best_lip_sync_preview_url=None, best_mouth_rec_preview_url=None, have_segment_data=None, initial_video_url=None, background_url=None, model=None, charater_position=None, charater_dimension=None):
        """ExecuteGetCharacterInfoByIdResponse

        The model defined in huaweicloud sdk

        :param create_time: 创建时间
        :type create_time: str
        :param update_time: 更新时间
        :type update_time: str
        :param character_name: 形象的个人姓名
        :type character_name: str
        :param gender: 
        :type gender: int
        :param id: 形象id
        :type id: str
        :param name: 形象名
        :type name: str
        :param photo_url: 形象obs地址
        :type photo_url: str
        :param posture: 姿态： 0：站姿全身 1：站姿半身 2：坐姿全身 3：坐姿半身
        :type posture: int
        :param train_finish_time_estimate: 估算的训练结束时间
        :type train_finish_time_estimate: str
        :param train_start_time: 训练开始时间
        :type train_start_time: str
        :param train_status: 训练状态： 0：预处理 1：训练中 2：训练成功 3：训练失败 4：预览视频生成中
        :type train_status: int
        :param type: 形象类型： 0：预制形象 1：用户自定义形象
        :type type: int
        :param center_photo_url: 形象在中心时的图片obs 地址
        :type center_photo_url: str
        :param error_msg: 合成错误信息
        :type error_msg: str
        :param left_photo_url: 形象在左时的图片obs 地址 考虑兼容性：如果为null，形象无法使用左右配置
        :type left_photo_url: str
        :param preview_video_url: 预览视频
        :type preview_video_url: str
        :param right_photo_url: 形象在右时的图片obs 地址 考虑兼容性：如果为null，形象无法使用左右配置
        :type right_photo_url: str
        :param best_img_quality_preview_url: 显示效果最佳预览
        :type best_img_quality_preview_url: str
        :param best_lip_sync_preview_url: 音唇同步最佳预览
        :type best_lip_sync_preview_url: str
        :param best_mouth_rec_preview_url: 嘴巴部分效果最佳
        :type best_mouth_rec_preview_url: str
        :param have_segment_data: 是否有人像分割数据
        :type have_segment_data: bool
        :param initial_video_url: 合成原始视频地址
        :type initial_video_url: str
        :param background_url: 抠图背景地址
        :type background_url: str
        :param model: 0: best img quality 1: best lip sync 2: best mouth rec
        :type model: int
        :param charater_position: 
        :type charater_position: :class:`huaweicloudsdkcbs.v1.CharacterPosition`
        :param charater_dimension: 
        :type charater_dimension: :class:`huaweicloudsdkcbs.v1.CharacterDimension`
        """
        
        super(ExecuteGetCharacterInfoByIdResponse, self).__init__()

        self._create_time = None
        self._update_time = None
        self._character_name = None
        self._gender = None
        self._id = None
        self._name = None
        self._photo_url = None
        self._posture = None
        self._train_finish_time_estimate = None
        self._train_start_time = None
        self._train_status = None
        self._type = None
        self._center_photo_url = None
        self._error_msg = None
        self._left_photo_url = None
        self._preview_video_url = None
        self._right_photo_url = None
        self._best_img_quality_preview_url = None
        self._best_lip_sync_preview_url = None
        self._best_mouth_rec_preview_url = None
        self._have_segment_data = None
        self._initial_video_url = None
        self._background_url = None
        self._model = None
        self._charater_position = None
        self._charater_dimension = None
        self.discriminator = None

        self.create_time = create_time
        self.update_time = update_time
        self.character_name = character_name
        if gender is not None:
            self.gender = gender
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if photo_url is not None:
            self.photo_url = photo_url
        if posture is not None:
            self.posture = posture
        if train_finish_time_estimate is not None:
            self.train_finish_time_estimate = train_finish_time_estimate
        if train_start_time is not None:
            self.train_start_time = train_start_time
        if train_status is not None:
            self.train_status = train_status
        if type is not None:
            self.type = type
        self.center_photo_url = center_photo_url
        if error_msg is not None:
            self.error_msg = error_msg
        if left_photo_url is not None:
            self.left_photo_url = left_photo_url
        if preview_video_url is not None:
            self.preview_video_url = preview_video_url
        if right_photo_url is not None:
            self.right_photo_url = right_photo_url
        if best_img_quality_preview_url is not None:
            self.best_img_quality_preview_url = best_img_quality_preview_url
        if best_lip_sync_preview_url is not None:
            self.best_lip_sync_preview_url = best_lip_sync_preview_url
        if best_mouth_rec_preview_url is not None:
            self.best_mouth_rec_preview_url = best_mouth_rec_preview_url
        self.have_segment_data = have_segment_data
        if initial_video_url is not None:
            self.initial_video_url = initial_video_url
        if background_url is not None:
            self.background_url = background_url
        if model is not None:
            self.model = model
        if charater_position is not None:
            self.charater_position = charater_position
        if charater_dimension is not None:
            self.charater_dimension = charater_dimension

    @property
    def create_time(self):
        """Gets the create_time of this ExecuteGetCharacterInfoByIdResponse.

        创建时间

        :return: The create_time of this ExecuteGetCharacterInfoByIdResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ExecuteGetCharacterInfoByIdResponse.

        创建时间

        :param create_time: The create_time of this ExecuteGetCharacterInfoByIdResponse.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this ExecuteGetCharacterInfoByIdResponse.

        更新时间

        :return: The update_time of this ExecuteGetCharacterInfoByIdResponse.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this ExecuteGetCharacterInfoByIdResponse.

        更新时间

        :param update_time: The update_time of this ExecuteGetCharacterInfoByIdResponse.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def character_name(self):
        """Gets the character_name of this ExecuteGetCharacterInfoByIdResponse.

        形象的个人姓名

        :return: The character_name of this ExecuteGetCharacterInfoByIdResponse.
        :rtype: str
        """
        return self._character_name

    @character_name.setter
    def character_name(self, character_name):
        """Sets the character_name of this ExecuteGetCharacterInfoByIdResponse.

        形象的个人姓名

        :param character_name: The character_name of this ExecuteGetCharacterInfoByIdResponse.
        :type character_name: str
        """
        self._character_name = character_name

    @property
    def gender(self):
        """Gets the gender of this ExecuteGetCharacterInfoByIdResponse.

        :return: The gender of this ExecuteGetCharacterInfoByIdResponse.
        :rtype: int
        """
        return self._gender

    @gender.setter
    def gender(self, gender):
        """Sets the gender of this ExecuteGetCharacterInfoByIdResponse.

        :param gender: The gender of this ExecuteGetCharacterInfoByIdResponse.
        :type gender: int
        """
        self._gender = gender

    @property
    def id(self):
        """Gets the id of this ExecuteGetCharacterInfoByIdResponse.

        形象id

        :return: The id of this ExecuteGetCharacterInfoByIdResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ExecuteGetCharacterInfoByIdResponse.

        形象id

        :param id: The id of this ExecuteGetCharacterInfoByIdResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ExecuteGetCharacterInfoByIdResponse.

        形象名

        :return: The name of this ExecuteGetCharacterInfoByIdResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ExecuteGetCharacterInfoByIdResponse.

        形象名

        :param name: The name of this ExecuteGetCharacterInfoByIdResponse.
        :type name: str
        """
        self._name = name

    @property
    def photo_url(self):
        """Gets the photo_url of this ExecuteGetCharacterInfoByIdResponse.

        形象obs地址

        :return: The photo_url of this ExecuteGetCharacterInfoByIdResponse.
        :rtype: str
        """
        return self._photo_url

    @photo_url.setter
    def photo_url(self, photo_url):
        """Sets the photo_url of this ExecuteGetCharacterInfoByIdResponse.

        形象obs地址

        :param photo_url: The photo_url of this ExecuteGetCharacterInfoByIdResponse.
        :type photo_url: str
        """
        self._photo_url = photo_url

    @property
    def posture(self):
        """Gets the posture of this ExecuteGetCharacterInfoByIdResponse.

        姿态： 0：站姿全身 1：站姿半身 2：坐姿全身 3：坐姿半身

        :return: The posture of this ExecuteGetCharacterInfoByIdResponse.
        :rtype: int
        """
        return self._posture

    @posture.setter
    def posture(self, posture):
        """Sets the posture of this ExecuteGetCharacterInfoByIdResponse.

        姿态： 0：站姿全身 1：站姿半身 2：坐姿全身 3：坐姿半身

        :param posture: The posture of this ExecuteGetCharacterInfoByIdResponse.
        :type posture: int
        """
        self._posture = posture

    @property
    def train_finish_time_estimate(self):
        """Gets the train_finish_time_estimate of this ExecuteGetCharacterInfoByIdResponse.

        估算的训练结束时间

        :return: The train_finish_time_estimate of this ExecuteGetCharacterInfoByIdResponse.
        :rtype: str
        """
        return self._train_finish_time_estimate

    @train_finish_time_estimate.setter
    def train_finish_time_estimate(self, train_finish_time_estimate):
        """Sets the train_finish_time_estimate of this ExecuteGetCharacterInfoByIdResponse.

        估算的训练结束时间

        :param train_finish_time_estimate: The train_finish_time_estimate of this ExecuteGetCharacterInfoByIdResponse.
        :type train_finish_time_estimate: str
        """
        self._train_finish_time_estimate = train_finish_time_estimate

    @property
    def train_start_time(self):
        """Gets the train_start_time of this ExecuteGetCharacterInfoByIdResponse.

        训练开始时间

        :return: The train_start_time of this ExecuteGetCharacterInfoByIdResponse.
        :rtype: str
        """
        return self._train_start_time

    @train_start_time.setter
    def train_start_time(self, train_start_time):
        """Sets the train_start_time of this ExecuteGetCharacterInfoByIdResponse.

        训练开始时间

        :param train_start_time: The train_start_time of this ExecuteGetCharacterInfoByIdResponse.
        :type train_start_time: str
        """
        self._train_start_time = train_start_time

    @property
    def train_status(self):
        """Gets the train_status of this ExecuteGetCharacterInfoByIdResponse.

        训练状态： 0：预处理 1：训练中 2：训练成功 3：训练失败 4：预览视频生成中

        :return: The train_status of this ExecuteGetCharacterInfoByIdResponse.
        :rtype: int
        """
        return self._train_status

    @train_status.setter
    def train_status(self, train_status):
        """Sets the train_status of this ExecuteGetCharacterInfoByIdResponse.

        训练状态： 0：预处理 1：训练中 2：训练成功 3：训练失败 4：预览视频生成中

        :param train_status: The train_status of this ExecuteGetCharacterInfoByIdResponse.
        :type train_status: int
        """
        self._train_status = train_status

    @property
    def type(self):
        """Gets the type of this ExecuteGetCharacterInfoByIdResponse.

        形象类型： 0：预制形象 1：用户自定义形象

        :return: The type of this ExecuteGetCharacterInfoByIdResponse.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ExecuteGetCharacterInfoByIdResponse.

        形象类型： 0：预制形象 1：用户自定义形象

        :param type: The type of this ExecuteGetCharacterInfoByIdResponse.
        :type type: int
        """
        self._type = type

    @property
    def center_photo_url(self):
        """Gets the center_photo_url of this ExecuteGetCharacterInfoByIdResponse.

        形象在中心时的图片obs 地址

        :return: The center_photo_url of this ExecuteGetCharacterInfoByIdResponse.
        :rtype: str
        """
        return self._center_photo_url

    @center_photo_url.setter
    def center_photo_url(self, center_photo_url):
        """Sets the center_photo_url of this ExecuteGetCharacterInfoByIdResponse.

        形象在中心时的图片obs 地址

        :param center_photo_url: The center_photo_url of this ExecuteGetCharacterInfoByIdResponse.
        :type center_photo_url: str
        """
        self._center_photo_url = center_photo_url

    @property
    def error_msg(self):
        """Gets the error_msg of this ExecuteGetCharacterInfoByIdResponse.

        合成错误信息

        :return: The error_msg of this ExecuteGetCharacterInfoByIdResponse.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        """Sets the error_msg of this ExecuteGetCharacterInfoByIdResponse.

        合成错误信息

        :param error_msg: The error_msg of this ExecuteGetCharacterInfoByIdResponse.
        :type error_msg: str
        """
        self._error_msg = error_msg

    @property
    def left_photo_url(self):
        """Gets the left_photo_url of this ExecuteGetCharacterInfoByIdResponse.

        形象在左时的图片obs 地址 考虑兼容性：如果为null，形象无法使用左右配置

        :return: The left_photo_url of this ExecuteGetCharacterInfoByIdResponse.
        :rtype: str
        """
        return self._left_photo_url

    @left_photo_url.setter
    def left_photo_url(self, left_photo_url):
        """Sets the left_photo_url of this ExecuteGetCharacterInfoByIdResponse.

        形象在左时的图片obs 地址 考虑兼容性：如果为null，形象无法使用左右配置

        :param left_photo_url: The left_photo_url of this ExecuteGetCharacterInfoByIdResponse.
        :type left_photo_url: str
        """
        self._left_photo_url = left_photo_url

    @property
    def preview_video_url(self):
        """Gets the preview_video_url of this ExecuteGetCharacterInfoByIdResponse.

        预览视频

        :return: The preview_video_url of this ExecuteGetCharacterInfoByIdResponse.
        :rtype: str
        """
        return self._preview_video_url

    @preview_video_url.setter
    def preview_video_url(self, preview_video_url):
        """Sets the preview_video_url of this ExecuteGetCharacterInfoByIdResponse.

        预览视频

        :param preview_video_url: The preview_video_url of this ExecuteGetCharacterInfoByIdResponse.
        :type preview_video_url: str
        """
        self._preview_video_url = preview_video_url

    @property
    def right_photo_url(self):
        """Gets the right_photo_url of this ExecuteGetCharacterInfoByIdResponse.

        形象在右时的图片obs 地址 考虑兼容性：如果为null，形象无法使用左右配置

        :return: The right_photo_url of this ExecuteGetCharacterInfoByIdResponse.
        :rtype: str
        """
        return self._right_photo_url

    @right_photo_url.setter
    def right_photo_url(self, right_photo_url):
        """Sets the right_photo_url of this ExecuteGetCharacterInfoByIdResponse.

        形象在右时的图片obs 地址 考虑兼容性：如果为null，形象无法使用左右配置

        :param right_photo_url: The right_photo_url of this ExecuteGetCharacterInfoByIdResponse.
        :type right_photo_url: str
        """
        self._right_photo_url = right_photo_url

    @property
    def best_img_quality_preview_url(self):
        """Gets the best_img_quality_preview_url of this ExecuteGetCharacterInfoByIdResponse.

        显示效果最佳预览

        :return: The best_img_quality_preview_url of this ExecuteGetCharacterInfoByIdResponse.
        :rtype: str
        """
        return self._best_img_quality_preview_url

    @best_img_quality_preview_url.setter
    def best_img_quality_preview_url(self, best_img_quality_preview_url):
        """Sets the best_img_quality_preview_url of this ExecuteGetCharacterInfoByIdResponse.

        显示效果最佳预览

        :param best_img_quality_preview_url: The best_img_quality_preview_url of this ExecuteGetCharacterInfoByIdResponse.
        :type best_img_quality_preview_url: str
        """
        self._best_img_quality_preview_url = best_img_quality_preview_url

    @property
    def best_lip_sync_preview_url(self):
        """Gets the best_lip_sync_preview_url of this ExecuteGetCharacterInfoByIdResponse.

        音唇同步最佳预览

        :return: The best_lip_sync_preview_url of this ExecuteGetCharacterInfoByIdResponse.
        :rtype: str
        """
        return self._best_lip_sync_preview_url

    @best_lip_sync_preview_url.setter
    def best_lip_sync_preview_url(self, best_lip_sync_preview_url):
        """Sets the best_lip_sync_preview_url of this ExecuteGetCharacterInfoByIdResponse.

        音唇同步最佳预览

        :param best_lip_sync_preview_url: The best_lip_sync_preview_url of this ExecuteGetCharacterInfoByIdResponse.
        :type best_lip_sync_preview_url: str
        """
        self._best_lip_sync_preview_url = best_lip_sync_preview_url

    @property
    def best_mouth_rec_preview_url(self):
        """Gets the best_mouth_rec_preview_url of this ExecuteGetCharacterInfoByIdResponse.

        嘴巴部分效果最佳

        :return: The best_mouth_rec_preview_url of this ExecuteGetCharacterInfoByIdResponse.
        :rtype: str
        """
        return self._best_mouth_rec_preview_url

    @best_mouth_rec_preview_url.setter
    def best_mouth_rec_preview_url(self, best_mouth_rec_preview_url):
        """Sets the best_mouth_rec_preview_url of this ExecuteGetCharacterInfoByIdResponse.

        嘴巴部分效果最佳

        :param best_mouth_rec_preview_url: The best_mouth_rec_preview_url of this ExecuteGetCharacterInfoByIdResponse.
        :type best_mouth_rec_preview_url: str
        """
        self._best_mouth_rec_preview_url = best_mouth_rec_preview_url

    @property
    def have_segment_data(self):
        """Gets the have_segment_data of this ExecuteGetCharacterInfoByIdResponse.

        是否有人像分割数据

        :return: The have_segment_data of this ExecuteGetCharacterInfoByIdResponse.
        :rtype: bool
        """
        return self._have_segment_data

    @have_segment_data.setter
    def have_segment_data(self, have_segment_data):
        """Sets the have_segment_data of this ExecuteGetCharacterInfoByIdResponse.

        是否有人像分割数据

        :param have_segment_data: The have_segment_data of this ExecuteGetCharacterInfoByIdResponse.
        :type have_segment_data: bool
        """
        self._have_segment_data = have_segment_data

    @property
    def initial_video_url(self):
        """Gets the initial_video_url of this ExecuteGetCharacterInfoByIdResponse.

        合成原始视频地址

        :return: The initial_video_url of this ExecuteGetCharacterInfoByIdResponse.
        :rtype: str
        """
        return self._initial_video_url

    @initial_video_url.setter
    def initial_video_url(self, initial_video_url):
        """Sets the initial_video_url of this ExecuteGetCharacterInfoByIdResponse.

        合成原始视频地址

        :param initial_video_url: The initial_video_url of this ExecuteGetCharacterInfoByIdResponse.
        :type initial_video_url: str
        """
        self._initial_video_url = initial_video_url

    @property
    def background_url(self):
        """Gets the background_url of this ExecuteGetCharacterInfoByIdResponse.

        抠图背景地址

        :return: The background_url of this ExecuteGetCharacterInfoByIdResponse.
        :rtype: str
        """
        return self._background_url

    @background_url.setter
    def background_url(self, background_url):
        """Sets the background_url of this ExecuteGetCharacterInfoByIdResponse.

        抠图背景地址

        :param background_url: The background_url of this ExecuteGetCharacterInfoByIdResponse.
        :type background_url: str
        """
        self._background_url = background_url

    @property
    def model(self):
        """Gets the model of this ExecuteGetCharacterInfoByIdResponse.

        0: best img quality 1: best lip sync 2: best mouth rec

        :return: The model of this ExecuteGetCharacterInfoByIdResponse.
        :rtype: int
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this ExecuteGetCharacterInfoByIdResponse.

        0: best img quality 1: best lip sync 2: best mouth rec

        :param model: The model of this ExecuteGetCharacterInfoByIdResponse.
        :type model: int
        """
        self._model = model

    @property
    def charater_position(self):
        """Gets the charater_position of this ExecuteGetCharacterInfoByIdResponse.

        :return: The charater_position of this ExecuteGetCharacterInfoByIdResponse.
        :rtype: :class:`huaweicloudsdkcbs.v1.CharacterPosition`
        """
        return self._charater_position

    @charater_position.setter
    def charater_position(self, charater_position):
        """Sets the charater_position of this ExecuteGetCharacterInfoByIdResponse.

        :param charater_position: The charater_position of this ExecuteGetCharacterInfoByIdResponse.
        :type charater_position: :class:`huaweicloudsdkcbs.v1.CharacterPosition`
        """
        self._charater_position = charater_position

    @property
    def charater_dimension(self):
        """Gets the charater_dimension of this ExecuteGetCharacterInfoByIdResponse.

        :return: The charater_dimension of this ExecuteGetCharacterInfoByIdResponse.
        :rtype: :class:`huaweicloudsdkcbs.v1.CharacterDimension`
        """
        return self._charater_dimension

    @charater_dimension.setter
    def charater_dimension(self, charater_dimension):
        """Sets the charater_dimension of this ExecuteGetCharacterInfoByIdResponse.

        :param charater_dimension: The charater_dimension of this ExecuteGetCharacterInfoByIdResponse.
        :type charater_dimension: :class:`huaweicloudsdkcbs.v1.CharacterDimension`
        """
        self._charater_dimension = charater_dimension

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
        if not isinstance(other, ExecuteGetCharacterInfoByIdResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
