# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateScoresRequestModel:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'competition_id': 'str',
        'stage_id': 'str',
        'works_id': 'int',
        'name': 'str',
        'works_kind': 'str',
        'score': 'float',
        'status': 'str',
        'created_time': 'str',
        'note': 'str',
        'message': 'str',
        'domain_id': 'str',
        'user_id': 'str'
    }

    attribute_map = {
        'competition_id': 'competition_id',
        'stage_id': 'stage_id',
        'works_id': 'works_id',
        'name': 'name',
        'works_kind': 'works_kind',
        'score': 'score',
        'status': 'status',
        'created_time': 'created_time',
        'note': 'note',
        'message': 'message',
        'domain_id': 'domain_id',
        'user_id': 'user_id'
    }

    def __init__(self, competition_id=None, stage_id=None, works_id=None, name=None, works_kind=None, score=None, status=None, created_time=None, note=None, message=None, domain_id=None, user_id=None):
        r"""CreateScoresRequestModel

        The model defined in huaweicloud sdk

        :param competition_id: 大赛ID，大赛平台提供
        :type competition_id: str
        :param stage_id: 大赛阶段ID，大赛平台提供
        :type stage_id: str
        :param works_id: 第三方服务作品ID
        :type works_id: int
        :param name: 作品名称，名称最大字符数为75，并且不能有含有特殊符号
        :type name: str
        :param works_kind: 作品类型,例如docx、png、zip等
        :type works_kind: str
        :param score: 作品分数，作品状态为failed时传-1，计算长度时包括小数点，小数点后面最多保留四位
        :type score: float
        :param status: 作品状态success|failed。判题时，需要对上传作品进行检查，当作品不符合要求时，应该返回failed，并将提示信息通过 message显示出来
        :type status: str
        :param created_time: 作品创建时间
        :type created_time: str
        :param note: 作品备注信息
        :type note: str
        :param message: 作品描述信息
        :type message: str
        :param domain_id: 租户ID
        :type domain_id: str
        :param user_id: 用户ID
        :type user_id: str
        """
        
        

        self._competition_id = None
        self._stage_id = None
        self._works_id = None
        self._name = None
        self._works_kind = None
        self._score = None
        self._status = None
        self._created_time = None
        self._note = None
        self._message = None
        self._domain_id = None
        self._user_id = None
        self.discriminator = None

        self.competition_id = competition_id
        self.stage_id = stage_id
        self.works_id = works_id
        self.name = name
        if works_kind is not None:
            self.works_kind = works_kind
        self.score = score
        self.status = status
        self.created_time = created_time
        if note is not None:
            self.note = note
        if message is not None:
            self.message = message
        self.domain_id = domain_id
        if user_id is not None:
            self.user_id = user_id

    @property
    def competition_id(self):
        r"""Gets the competition_id of this CreateScoresRequestModel.

        大赛ID，大赛平台提供

        :return: The competition_id of this CreateScoresRequestModel.
        :rtype: str
        """
        return self._competition_id

    @competition_id.setter
    def competition_id(self, competition_id):
        r"""Sets the competition_id of this CreateScoresRequestModel.

        大赛ID，大赛平台提供

        :param competition_id: The competition_id of this CreateScoresRequestModel.
        :type competition_id: str
        """
        self._competition_id = competition_id

    @property
    def stage_id(self):
        r"""Gets the stage_id of this CreateScoresRequestModel.

        大赛阶段ID，大赛平台提供

        :return: The stage_id of this CreateScoresRequestModel.
        :rtype: str
        """
        return self._stage_id

    @stage_id.setter
    def stage_id(self, stage_id):
        r"""Sets the stage_id of this CreateScoresRequestModel.

        大赛阶段ID，大赛平台提供

        :param stage_id: The stage_id of this CreateScoresRequestModel.
        :type stage_id: str
        """
        self._stage_id = stage_id

    @property
    def works_id(self):
        r"""Gets the works_id of this CreateScoresRequestModel.

        第三方服务作品ID

        :return: The works_id of this CreateScoresRequestModel.
        :rtype: int
        """
        return self._works_id

    @works_id.setter
    def works_id(self, works_id):
        r"""Sets the works_id of this CreateScoresRequestModel.

        第三方服务作品ID

        :param works_id: The works_id of this CreateScoresRequestModel.
        :type works_id: int
        """
        self._works_id = works_id

    @property
    def name(self):
        r"""Gets the name of this CreateScoresRequestModel.

        作品名称，名称最大字符数为75，并且不能有含有特殊符号

        :return: The name of this CreateScoresRequestModel.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateScoresRequestModel.

        作品名称，名称最大字符数为75，并且不能有含有特殊符号

        :param name: The name of this CreateScoresRequestModel.
        :type name: str
        """
        self._name = name

    @property
    def works_kind(self):
        r"""Gets the works_kind of this CreateScoresRequestModel.

        作品类型,例如docx、png、zip等

        :return: The works_kind of this CreateScoresRequestModel.
        :rtype: str
        """
        return self._works_kind

    @works_kind.setter
    def works_kind(self, works_kind):
        r"""Sets the works_kind of this CreateScoresRequestModel.

        作品类型,例如docx、png、zip等

        :param works_kind: The works_kind of this CreateScoresRequestModel.
        :type works_kind: str
        """
        self._works_kind = works_kind

    @property
    def score(self):
        r"""Gets the score of this CreateScoresRequestModel.

        作品分数，作品状态为failed时传-1，计算长度时包括小数点，小数点后面最多保留四位

        :return: The score of this CreateScoresRequestModel.
        :rtype: float
        """
        return self._score

    @score.setter
    def score(self, score):
        r"""Sets the score of this CreateScoresRequestModel.

        作品分数，作品状态为failed时传-1，计算长度时包括小数点，小数点后面最多保留四位

        :param score: The score of this CreateScoresRequestModel.
        :type score: float
        """
        self._score = score

    @property
    def status(self):
        r"""Gets the status of this CreateScoresRequestModel.

        作品状态success|failed。判题时，需要对上传作品进行检查，当作品不符合要求时，应该返回failed，并将提示信息通过 message显示出来

        :return: The status of this CreateScoresRequestModel.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this CreateScoresRequestModel.

        作品状态success|failed。判题时，需要对上传作品进行检查，当作品不符合要求时，应该返回failed，并将提示信息通过 message显示出来

        :param status: The status of this CreateScoresRequestModel.
        :type status: str
        """
        self._status = status

    @property
    def created_time(self):
        r"""Gets the created_time of this CreateScoresRequestModel.

        作品创建时间

        :return: The created_time of this CreateScoresRequestModel.
        :rtype: str
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        r"""Sets the created_time of this CreateScoresRequestModel.

        作品创建时间

        :param created_time: The created_time of this CreateScoresRequestModel.
        :type created_time: str
        """
        self._created_time = created_time

    @property
    def note(self):
        r"""Gets the note of this CreateScoresRequestModel.

        作品备注信息

        :return: The note of this CreateScoresRequestModel.
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        r"""Sets the note of this CreateScoresRequestModel.

        作品备注信息

        :param note: The note of this CreateScoresRequestModel.
        :type note: str
        """
        self._note = note

    @property
    def message(self):
        r"""Gets the message of this CreateScoresRequestModel.

        作品描述信息

        :return: The message of this CreateScoresRequestModel.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this CreateScoresRequestModel.

        作品描述信息

        :param message: The message of this CreateScoresRequestModel.
        :type message: str
        """
        self._message = message

    @property
    def domain_id(self):
        r"""Gets the domain_id of this CreateScoresRequestModel.

        租户ID

        :return: The domain_id of this CreateScoresRequestModel.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this CreateScoresRequestModel.

        租户ID

        :param domain_id: The domain_id of this CreateScoresRequestModel.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def user_id(self):
        r"""Gets the user_id of this CreateScoresRequestModel.

        用户ID

        :return: The user_id of this CreateScoresRequestModel.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this CreateScoresRequestModel.

        用户ID

        :param user_id: The user_id of this CreateScoresRequestModel.
        :type user_id: str
        """
        self._user_id = user_id

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
        if not isinstance(other, CreateScoresRequestModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
