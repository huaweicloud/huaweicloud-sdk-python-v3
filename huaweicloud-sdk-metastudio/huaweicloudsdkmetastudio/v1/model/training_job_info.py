# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TrainingJobInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'job_type': 'JobType',
        'job_id': 'str',
        'app_user_id': 'str',
        'voice_name': 'str',
        'sex': 'str',
        'language': 'str',
        'state': 'JobState',
        'asset_id': 'str',
        'job_failed_code': 'str',
        'job_failed_reason': 'str',
        'create_time': 'int',
        'lastupdate_time': 'int',
        'voice_authorization_url': 'str',
        'create_type': 'CreateType',
        'tag': 'JobTag'
    }

    attribute_map = {
        'job_type': 'job_type',
        'job_id': 'job_id',
        'app_user_id': 'app_user_id',
        'voice_name': 'voice_name',
        'sex': 'sex',
        'language': 'language',
        'state': 'state',
        'asset_id': 'asset_id',
        'job_failed_code': 'job_failed_code',
        'job_failed_reason': 'job_failed_reason',
        'create_time': 'create_time',
        'lastupdate_time': 'lastupdate_time',
        'voice_authorization_url': 'voice_authorization_url',
        'create_type': 'create_type',
        'tag': 'tag'
    }

    def __init__(self, job_type=None, job_id=None, app_user_id=None, voice_name=None, sex=None, language=None, state=None, asset_id=None, job_failed_code=None, job_failed_reason=None, create_time=None, lastupdate_time=None, voice_authorization_url=None, create_type=None, tag=None):
        """TrainingJobInfo

        The model defined in huaweicloud sdk

        :param job_type: 
        :type job_type: :class:`huaweicloudsdkmetastudio.v1.JobType`
        :param job_id: 任务id。
        :type job_id: str
        :param app_user_id: 用户id。
        :type app_user_id: str
        :param voice_name: 音色名称。该名称会作为资产库中音色模型资产名称。
        :type voice_name: str
        :param sex: 性别。 * FEMALE: 女性 * MALE: 是男性
        :type sex: str
        :param language: 语言。
        :type language: str
        :param state: 
        :type state: :class:`huaweicloudsdkmetastudio.v1.JobState`
        :param asset_id: 当任务状态为成功时呈现,音色模型在资产库中的id。
        :type asset_id: str
        :param job_failed_code: 当任务失败时呈现,失败错误码。
        :type job_failed_code: str
        :param job_failed_reason: 当任务失败时呈现,失败原因。
        :type job_failed_reason: str
        :param create_time: 任务创建时间。
        :type create_time: int
        :param lastupdate_time: 任务状态更新时间。
        :type lastupdate_time: int
        :param voice_authorization_url: 用户授权书连接。
        :type voice_authorization_url: str
        :param create_type: 
        :type create_type: :class:`huaweicloudsdkmetastudio.v1.CreateType`
        :param tag: 
        :type tag: :class:`huaweicloudsdkmetastudio.v1.JobTag`
        """
        
        

        self._job_type = None
        self._job_id = None
        self._app_user_id = None
        self._voice_name = None
        self._sex = None
        self._language = None
        self._state = None
        self._asset_id = None
        self._job_failed_code = None
        self._job_failed_reason = None
        self._create_time = None
        self._lastupdate_time = None
        self._voice_authorization_url = None
        self._create_type = None
        self._tag = None
        self.discriminator = None

        if job_type is not None:
            self.job_type = job_type
        if job_id is not None:
            self.job_id = job_id
        if app_user_id is not None:
            self.app_user_id = app_user_id
        if voice_name is not None:
            self.voice_name = voice_name
        if sex is not None:
            self.sex = sex
        if language is not None:
            self.language = language
        if state is not None:
            self.state = state
        if asset_id is not None:
            self.asset_id = asset_id
        if job_failed_code is not None:
            self.job_failed_code = job_failed_code
        if job_failed_reason is not None:
            self.job_failed_reason = job_failed_reason
        if create_time is not None:
            self.create_time = create_time
        if lastupdate_time is not None:
            self.lastupdate_time = lastupdate_time
        if voice_authorization_url is not None:
            self.voice_authorization_url = voice_authorization_url
        if create_type is not None:
            self.create_type = create_type
        if tag is not None:
            self.tag = tag

    @property
    def job_type(self):
        """Gets the job_type of this TrainingJobInfo.

        :return: The job_type of this TrainingJobInfo.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.JobType`
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        """Sets the job_type of this TrainingJobInfo.

        :param job_type: The job_type of this TrainingJobInfo.
        :type job_type: :class:`huaweicloudsdkmetastudio.v1.JobType`
        """
        self._job_type = job_type

    @property
    def job_id(self):
        """Gets the job_id of this TrainingJobInfo.

        任务id。

        :return: The job_id of this TrainingJobInfo.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this TrainingJobInfo.

        任务id。

        :param job_id: The job_id of this TrainingJobInfo.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def app_user_id(self):
        """Gets the app_user_id of this TrainingJobInfo.

        用户id。

        :return: The app_user_id of this TrainingJobInfo.
        :rtype: str
        """
        return self._app_user_id

    @app_user_id.setter
    def app_user_id(self, app_user_id):
        """Sets the app_user_id of this TrainingJobInfo.

        用户id。

        :param app_user_id: The app_user_id of this TrainingJobInfo.
        :type app_user_id: str
        """
        self._app_user_id = app_user_id

    @property
    def voice_name(self):
        """Gets the voice_name of this TrainingJobInfo.

        音色名称。该名称会作为资产库中音色模型资产名称。

        :return: The voice_name of this TrainingJobInfo.
        :rtype: str
        """
        return self._voice_name

    @voice_name.setter
    def voice_name(self, voice_name):
        """Sets the voice_name of this TrainingJobInfo.

        音色名称。该名称会作为资产库中音色模型资产名称。

        :param voice_name: The voice_name of this TrainingJobInfo.
        :type voice_name: str
        """
        self._voice_name = voice_name

    @property
    def sex(self):
        """Gets the sex of this TrainingJobInfo.

        性别。 * FEMALE: 女性 * MALE: 是男性

        :return: The sex of this TrainingJobInfo.
        :rtype: str
        """
        return self._sex

    @sex.setter
    def sex(self, sex):
        """Sets the sex of this TrainingJobInfo.

        性别。 * FEMALE: 女性 * MALE: 是男性

        :param sex: The sex of this TrainingJobInfo.
        :type sex: str
        """
        self._sex = sex

    @property
    def language(self):
        """Gets the language of this TrainingJobInfo.

        语言。

        :return: The language of this TrainingJobInfo.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this TrainingJobInfo.

        语言。

        :param language: The language of this TrainingJobInfo.
        :type language: str
        """
        self._language = language

    @property
    def state(self):
        """Gets the state of this TrainingJobInfo.

        :return: The state of this TrainingJobInfo.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.JobState`
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this TrainingJobInfo.

        :param state: The state of this TrainingJobInfo.
        :type state: :class:`huaweicloudsdkmetastudio.v1.JobState`
        """
        self._state = state

    @property
    def asset_id(self):
        """Gets the asset_id of this TrainingJobInfo.

        当任务状态为成功时呈现,音色模型在资产库中的id。

        :return: The asset_id of this TrainingJobInfo.
        :rtype: str
        """
        return self._asset_id

    @asset_id.setter
    def asset_id(self, asset_id):
        """Sets the asset_id of this TrainingJobInfo.

        当任务状态为成功时呈现,音色模型在资产库中的id。

        :param asset_id: The asset_id of this TrainingJobInfo.
        :type asset_id: str
        """
        self._asset_id = asset_id

    @property
    def job_failed_code(self):
        """Gets the job_failed_code of this TrainingJobInfo.

        当任务失败时呈现,失败错误码。

        :return: The job_failed_code of this TrainingJobInfo.
        :rtype: str
        """
        return self._job_failed_code

    @job_failed_code.setter
    def job_failed_code(self, job_failed_code):
        """Sets the job_failed_code of this TrainingJobInfo.

        当任务失败时呈现,失败错误码。

        :param job_failed_code: The job_failed_code of this TrainingJobInfo.
        :type job_failed_code: str
        """
        self._job_failed_code = job_failed_code

    @property
    def job_failed_reason(self):
        """Gets the job_failed_reason of this TrainingJobInfo.

        当任务失败时呈现,失败原因。

        :return: The job_failed_reason of this TrainingJobInfo.
        :rtype: str
        """
        return self._job_failed_reason

    @job_failed_reason.setter
    def job_failed_reason(self, job_failed_reason):
        """Sets the job_failed_reason of this TrainingJobInfo.

        当任务失败时呈现,失败原因。

        :param job_failed_reason: The job_failed_reason of this TrainingJobInfo.
        :type job_failed_reason: str
        """
        self._job_failed_reason = job_failed_reason

    @property
    def create_time(self):
        """Gets the create_time of this TrainingJobInfo.

        任务创建时间。

        :return: The create_time of this TrainingJobInfo.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this TrainingJobInfo.

        任务创建时间。

        :param create_time: The create_time of this TrainingJobInfo.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def lastupdate_time(self):
        """Gets the lastupdate_time of this TrainingJobInfo.

        任务状态更新时间。

        :return: The lastupdate_time of this TrainingJobInfo.
        :rtype: int
        """
        return self._lastupdate_time

    @lastupdate_time.setter
    def lastupdate_time(self, lastupdate_time):
        """Sets the lastupdate_time of this TrainingJobInfo.

        任务状态更新时间。

        :param lastupdate_time: The lastupdate_time of this TrainingJobInfo.
        :type lastupdate_time: int
        """
        self._lastupdate_time = lastupdate_time

    @property
    def voice_authorization_url(self):
        """Gets the voice_authorization_url of this TrainingJobInfo.

        用户授权书连接。

        :return: The voice_authorization_url of this TrainingJobInfo.
        :rtype: str
        """
        return self._voice_authorization_url

    @voice_authorization_url.setter
    def voice_authorization_url(self, voice_authorization_url):
        """Sets the voice_authorization_url of this TrainingJobInfo.

        用户授权书连接。

        :param voice_authorization_url: The voice_authorization_url of this TrainingJobInfo.
        :type voice_authorization_url: str
        """
        self._voice_authorization_url = voice_authorization_url

    @property
    def create_type(self):
        """Gets the create_type of this TrainingJobInfo.

        :return: The create_type of this TrainingJobInfo.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.CreateType`
        """
        return self._create_type

    @create_type.setter
    def create_type(self, create_type):
        """Sets the create_type of this TrainingJobInfo.

        :param create_type: The create_type of this TrainingJobInfo.
        :type create_type: :class:`huaweicloudsdkmetastudio.v1.CreateType`
        """
        self._create_type = create_type

    @property
    def tag(self):
        """Gets the tag of this TrainingJobInfo.

        :return: The tag of this TrainingJobInfo.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.JobTag`
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this TrainingJobInfo.

        :param tag: The tag of this TrainingJobInfo.
        :type tag: :class:`huaweicloudsdkmetastudio.v1.JobTag`
        """
        self._tag = tag

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
        if not isinstance(other, TrainingJobInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
