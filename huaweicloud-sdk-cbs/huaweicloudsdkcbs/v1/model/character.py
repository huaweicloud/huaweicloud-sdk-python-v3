# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Character:

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
        'type': 'int'
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
        'type': 'type'
    }

    def __init__(self, create_time=None, update_time=None, character_name=None, gender=None, id=None, name=None, photo_url=None, posture=None, train_finish_time_estimate=None, train_start_time=None, train_status=None, type=None):
        r"""Character

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
        """
        
        

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

    @property
    def create_time(self):
        r"""Gets the create_time of this Character.

        创建时间

        :return: The create_time of this Character.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this Character.

        创建时间

        :param create_time: The create_time of this Character.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this Character.

        更新时间

        :return: The update_time of this Character.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this Character.

        更新时间

        :param update_time: The update_time of this Character.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def character_name(self):
        r"""Gets the character_name of this Character.

        形象的个人姓名

        :return: The character_name of this Character.
        :rtype: str
        """
        return self._character_name

    @character_name.setter
    def character_name(self, character_name):
        r"""Sets the character_name of this Character.

        形象的个人姓名

        :param character_name: The character_name of this Character.
        :type character_name: str
        """
        self._character_name = character_name

    @property
    def gender(self):
        r"""Gets the gender of this Character.

        :return: The gender of this Character.
        :rtype: int
        """
        return self._gender

    @gender.setter
    def gender(self, gender):
        r"""Sets the gender of this Character.

        :param gender: The gender of this Character.
        :type gender: int
        """
        self._gender = gender

    @property
    def id(self):
        r"""Gets the id of this Character.

        形象id

        :return: The id of this Character.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this Character.

        形象id

        :param id: The id of this Character.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this Character.

        形象名

        :return: The name of this Character.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this Character.

        形象名

        :param name: The name of this Character.
        :type name: str
        """
        self._name = name

    @property
    def photo_url(self):
        r"""Gets the photo_url of this Character.

        形象obs地址

        :return: The photo_url of this Character.
        :rtype: str
        """
        return self._photo_url

    @photo_url.setter
    def photo_url(self, photo_url):
        r"""Sets the photo_url of this Character.

        形象obs地址

        :param photo_url: The photo_url of this Character.
        :type photo_url: str
        """
        self._photo_url = photo_url

    @property
    def posture(self):
        r"""Gets the posture of this Character.

        姿态： 0：站姿全身 1：站姿半身 2：坐姿全身 3：坐姿半身

        :return: The posture of this Character.
        :rtype: int
        """
        return self._posture

    @posture.setter
    def posture(self, posture):
        r"""Sets the posture of this Character.

        姿态： 0：站姿全身 1：站姿半身 2：坐姿全身 3：坐姿半身

        :param posture: The posture of this Character.
        :type posture: int
        """
        self._posture = posture

    @property
    def train_finish_time_estimate(self):
        r"""Gets the train_finish_time_estimate of this Character.

        估算的训练结束时间

        :return: The train_finish_time_estimate of this Character.
        :rtype: str
        """
        return self._train_finish_time_estimate

    @train_finish_time_estimate.setter
    def train_finish_time_estimate(self, train_finish_time_estimate):
        r"""Sets the train_finish_time_estimate of this Character.

        估算的训练结束时间

        :param train_finish_time_estimate: The train_finish_time_estimate of this Character.
        :type train_finish_time_estimate: str
        """
        self._train_finish_time_estimate = train_finish_time_estimate

    @property
    def train_start_time(self):
        r"""Gets the train_start_time of this Character.

        训练开始时间

        :return: The train_start_time of this Character.
        :rtype: str
        """
        return self._train_start_time

    @train_start_time.setter
    def train_start_time(self, train_start_time):
        r"""Sets the train_start_time of this Character.

        训练开始时间

        :param train_start_time: The train_start_time of this Character.
        :type train_start_time: str
        """
        self._train_start_time = train_start_time

    @property
    def train_status(self):
        r"""Gets the train_status of this Character.

        训练状态： 0：预处理 1：训练中 2：训练成功 3：训练失败 4：预览视频生成中

        :return: The train_status of this Character.
        :rtype: int
        """
        return self._train_status

    @train_status.setter
    def train_status(self, train_status):
        r"""Sets the train_status of this Character.

        训练状态： 0：预处理 1：训练中 2：训练成功 3：训练失败 4：预览视频生成中

        :param train_status: The train_status of this Character.
        :type train_status: int
        """
        self._train_status = train_status

    @property
    def type(self):
        r"""Gets the type of this Character.

        形象类型： 0：预制形象 1：用户自定义形象

        :return: The type of this Character.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this Character.

        形象类型： 0：预制形象 1：用户自定义形象

        :param type: The type of this Character.
        :type type: int
        """
        self._type = type

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
        if not isinstance(other, Character):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
