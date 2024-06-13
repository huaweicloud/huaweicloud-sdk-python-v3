# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateRobotReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'app_type': 'int',
        'room_id': 'str',
        'language': 'LanguageEnum',
        'tail_silence_time': 'int',
        'enable_question_audit': 'bool',
        'huawei_ei_cbs': 'HuaweiEiCbs',
        'iflytek_aiui_config': 'IflytekAiuiConfig',
        'iflytek_spark': 'IflytekSpark',
        'third_party_model_config': 'ThirdPartyModelConfig',
        'mobvoi_config': 'MobvoiConfig'
    }

    attribute_map = {
        'name': 'name',
        'app_type': 'app_type',
        'room_id': 'room_id',
        'language': 'language',
        'tail_silence_time': 'tail_silence_time',
        'enable_question_audit': 'enable_question_audit',
        'huawei_ei_cbs': 'huawei_ei_cbs',
        'iflytek_aiui_config': 'iflytek_aiui_config',
        'iflytek_spark': 'iflytek_spark',
        'third_party_model_config': 'third_party_model_config',
        'mobvoi_config': 'mobvoi_config'
    }

    def __init__(self, name=None, app_type=None, room_id=None, language=None, tail_silence_time=None, enable_question_audit=None, huawei_ei_cbs=None, iflytek_aiui_config=None, iflytek_spark=None, third_party_model_config=None, mobvoi_config=None):
        """UpdateRobotReq

        The model defined in huaweicloud sdk

        :param name: 应用名称。
        :type name: str
        :param app_type: 对接第三方应用厂商类型。 &gt; 0：科大讯飞AIUI；1：华为云CBS；2：科大讯飞星火交互认知大模型；5：第三方驱动；6：第三方语言模型；8：奇妙问
        :type app_type: int
        :param room_id: 智能交互对话房间ID。
        :type room_id: str
        :param language: 
        :type language: :class:`huaweicloudsdkmetastudio.v1.LanguageEnum`
        :param tail_silence_time: 语音识别后端点静音时长默认500ms
        :type tail_silence_time: int
        :param enable_question_audit: 提问文本审核开关
        :type enable_question_audit: bool
        :param huawei_ei_cbs: 
        :type huawei_ei_cbs: :class:`huaweicloudsdkmetastudio.v1.HuaweiEiCbs`
        :param iflytek_aiui_config: 
        :type iflytek_aiui_config: :class:`huaweicloudsdkmetastudio.v1.IflytekAiuiConfig`
        :param iflytek_spark: 
        :type iflytek_spark: :class:`huaweicloudsdkmetastudio.v1.IflytekSpark`
        :param third_party_model_config: 
        :type third_party_model_config: :class:`huaweicloudsdkmetastudio.v1.ThirdPartyModelConfig`
        :param mobvoi_config: 
        :type mobvoi_config: :class:`huaweicloudsdkmetastudio.v1.MobvoiConfig`
        """
        
        

        self._name = None
        self._app_type = None
        self._room_id = None
        self._language = None
        self._tail_silence_time = None
        self._enable_question_audit = None
        self._huawei_ei_cbs = None
        self._iflytek_aiui_config = None
        self._iflytek_spark = None
        self._third_party_model_config = None
        self._mobvoi_config = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if app_type is not None:
            self.app_type = app_type
        if room_id is not None:
            self.room_id = room_id
        if language is not None:
            self.language = language
        if tail_silence_time is not None:
            self.tail_silence_time = tail_silence_time
        if enable_question_audit is not None:
            self.enable_question_audit = enable_question_audit
        if huawei_ei_cbs is not None:
            self.huawei_ei_cbs = huawei_ei_cbs
        if iflytek_aiui_config is not None:
            self.iflytek_aiui_config = iflytek_aiui_config
        if iflytek_spark is not None:
            self.iflytek_spark = iflytek_spark
        if third_party_model_config is not None:
            self.third_party_model_config = third_party_model_config
        if mobvoi_config is not None:
            self.mobvoi_config = mobvoi_config

    @property
    def name(self):
        """Gets the name of this UpdateRobotReq.

        应用名称。

        :return: The name of this UpdateRobotReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateRobotReq.

        应用名称。

        :param name: The name of this UpdateRobotReq.
        :type name: str
        """
        self._name = name

    @property
    def app_type(self):
        """Gets the app_type of this UpdateRobotReq.

        对接第三方应用厂商类型。 > 0：科大讯飞AIUI；1：华为云CBS；2：科大讯飞星火交互认知大模型；5：第三方驱动；6：第三方语言模型；8：奇妙问

        :return: The app_type of this UpdateRobotReq.
        :rtype: int
        """
        return self._app_type

    @app_type.setter
    def app_type(self, app_type):
        """Sets the app_type of this UpdateRobotReq.

        对接第三方应用厂商类型。 > 0：科大讯飞AIUI；1：华为云CBS；2：科大讯飞星火交互认知大模型；5：第三方驱动；6：第三方语言模型；8：奇妙问

        :param app_type: The app_type of this UpdateRobotReq.
        :type app_type: int
        """
        self._app_type = app_type

    @property
    def room_id(self):
        """Gets the room_id of this UpdateRobotReq.

        智能交互对话房间ID。

        :return: The room_id of this UpdateRobotReq.
        :rtype: str
        """
        return self._room_id

    @room_id.setter
    def room_id(self, room_id):
        """Sets the room_id of this UpdateRobotReq.

        智能交互对话房间ID。

        :param room_id: The room_id of this UpdateRobotReq.
        :type room_id: str
        """
        self._room_id = room_id

    @property
    def language(self):
        """Gets the language of this UpdateRobotReq.

        :return: The language of this UpdateRobotReq.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.LanguageEnum`
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this UpdateRobotReq.

        :param language: The language of this UpdateRobotReq.
        :type language: :class:`huaweicloudsdkmetastudio.v1.LanguageEnum`
        """
        self._language = language

    @property
    def tail_silence_time(self):
        """Gets the tail_silence_time of this UpdateRobotReq.

        语音识别后端点静音时长默认500ms

        :return: The tail_silence_time of this UpdateRobotReq.
        :rtype: int
        """
        return self._tail_silence_time

    @tail_silence_time.setter
    def tail_silence_time(self, tail_silence_time):
        """Sets the tail_silence_time of this UpdateRobotReq.

        语音识别后端点静音时长默认500ms

        :param tail_silence_time: The tail_silence_time of this UpdateRobotReq.
        :type tail_silence_time: int
        """
        self._tail_silence_time = tail_silence_time

    @property
    def enable_question_audit(self):
        """Gets the enable_question_audit of this UpdateRobotReq.

        提问文本审核开关

        :return: The enable_question_audit of this UpdateRobotReq.
        :rtype: bool
        """
        return self._enable_question_audit

    @enable_question_audit.setter
    def enable_question_audit(self, enable_question_audit):
        """Sets the enable_question_audit of this UpdateRobotReq.

        提问文本审核开关

        :param enable_question_audit: The enable_question_audit of this UpdateRobotReq.
        :type enable_question_audit: bool
        """
        self._enable_question_audit = enable_question_audit

    @property
    def huawei_ei_cbs(self):
        """Gets the huawei_ei_cbs of this UpdateRobotReq.

        :return: The huawei_ei_cbs of this UpdateRobotReq.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.HuaweiEiCbs`
        """
        return self._huawei_ei_cbs

    @huawei_ei_cbs.setter
    def huawei_ei_cbs(self, huawei_ei_cbs):
        """Sets the huawei_ei_cbs of this UpdateRobotReq.

        :param huawei_ei_cbs: The huawei_ei_cbs of this UpdateRobotReq.
        :type huawei_ei_cbs: :class:`huaweicloudsdkmetastudio.v1.HuaweiEiCbs`
        """
        self._huawei_ei_cbs = huawei_ei_cbs

    @property
    def iflytek_aiui_config(self):
        """Gets the iflytek_aiui_config of this UpdateRobotReq.

        :return: The iflytek_aiui_config of this UpdateRobotReq.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.IflytekAiuiConfig`
        """
        return self._iflytek_aiui_config

    @iflytek_aiui_config.setter
    def iflytek_aiui_config(self, iflytek_aiui_config):
        """Sets the iflytek_aiui_config of this UpdateRobotReq.

        :param iflytek_aiui_config: The iflytek_aiui_config of this UpdateRobotReq.
        :type iflytek_aiui_config: :class:`huaweicloudsdkmetastudio.v1.IflytekAiuiConfig`
        """
        self._iflytek_aiui_config = iflytek_aiui_config

    @property
    def iflytek_spark(self):
        """Gets the iflytek_spark of this UpdateRobotReq.

        :return: The iflytek_spark of this UpdateRobotReq.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.IflytekSpark`
        """
        return self._iflytek_spark

    @iflytek_spark.setter
    def iflytek_spark(self, iflytek_spark):
        """Sets the iflytek_spark of this UpdateRobotReq.

        :param iflytek_spark: The iflytek_spark of this UpdateRobotReq.
        :type iflytek_spark: :class:`huaweicloudsdkmetastudio.v1.IflytekSpark`
        """
        self._iflytek_spark = iflytek_spark

    @property
    def third_party_model_config(self):
        """Gets the third_party_model_config of this UpdateRobotReq.

        :return: The third_party_model_config of this UpdateRobotReq.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ThirdPartyModelConfig`
        """
        return self._third_party_model_config

    @third_party_model_config.setter
    def third_party_model_config(self, third_party_model_config):
        """Sets the third_party_model_config of this UpdateRobotReq.

        :param third_party_model_config: The third_party_model_config of this UpdateRobotReq.
        :type third_party_model_config: :class:`huaweicloudsdkmetastudio.v1.ThirdPartyModelConfig`
        """
        self._third_party_model_config = third_party_model_config

    @property
    def mobvoi_config(self):
        """Gets the mobvoi_config of this UpdateRobotReq.

        :return: The mobvoi_config of this UpdateRobotReq.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.MobvoiConfig`
        """
        return self._mobvoi_config

    @mobvoi_config.setter
    def mobvoi_config(self, mobvoi_config):
        """Sets the mobvoi_config of this UpdateRobotReq.

        :param mobvoi_config: The mobvoi_config of this UpdateRobotReq.
        :type mobvoi_config: :class:`huaweicloudsdkmetastudio.v1.MobvoiConfig`
        """
        self._mobvoi_config = mobvoi_config

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
        if not isinstance(other, UpdateRobotReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
