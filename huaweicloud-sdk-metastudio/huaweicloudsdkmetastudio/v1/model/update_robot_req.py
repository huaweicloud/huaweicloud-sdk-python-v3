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
        'concurrency': 'int',
        'language': 'LanguageEnum',
        'huawei_ei_cbs': 'HuaweiEiCbs',
        'iflytek_aiui_config': 'IflytekAiuiConfig',
        'iflytek_spark': 'IflytekSpark',
        'third_party_model_config': 'ThirdPartyModelConfig'
    }

    attribute_map = {
        'name': 'name',
        'app_type': 'app_type',
        'concurrency': 'concurrency',
        'language': 'language',
        'huawei_ei_cbs': 'huawei_ei_cbs',
        'iflytek_aiui_config': 'iflytek_aiui_config',
        'iflytek_spark': 'iflytek_spark',
        'third_party_model_config': 'third_party_model_config'
    }

    def __init__(self, name=None, app_type=None, concurrency=None, language=None, huawei_ei_cbs=None, iflytek_aiui_config=None, iflytek_spark=None, third_party_model_config=None):
        """UpdateRobotReq

        The model defined in huaweicloud sdk

        :param name: 应用名称。
        :type name: str
        :param app_type: 对接第三方应用厂商类型。 &gt; 0：科大讯飞AIUI；1：华为云CBS；2：科大讯飞星火交互认知大模型；5：第三方驱动；6：第三方语言模型
        :type app_type: int
        :param concurrency: 对话的并发数
        :type concurrency: int
        :param language: 
        :type language: :class:`huaweicloudsdkmetastudio.v1.LanguageEnum`
        :param huawei_ei_cbs: 
        :type huawei_ei_cbs: :class:`huaweicloudsdkmetastudio.v1.HuaweiEiCbs`
        :param iflytek_aiui_config: 
        :type iflytek_aiui_config: :class:`huaweicloudsdkmetastudio.v1.IflytekAiuiConfig`
        :param iflytek_spark: 
        :type iflytek_spark: :class:`huaweicloudsdkmetastudio.v1.IflytekSpark`
        :param third_party_model_config: 
        :type third_party_model_config: :class:`huaweicloudsdkmetastudio.v1.ThirdPartyModelConfig`
        """
        
        

        self._name = None
        self._app_type = None
        self._concurrency = None
        self._language = None
        self._huawei_ei_cbs = None
        self._iflytek_aiui_config = None
        self._iflytek_spark = None
        self._third_party_model_config = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if app_type is not None:
            self.app_type = app_type
        if concurrency is not None:
            self.concurrency = concurrency
        if language is not None:
            self.language = language
        if huawei_ei_cbs is not None:
            self.huawei_ei_cbs = huawei_ei_cbs
        if iflytek_aiui_config is not None:
            self.iflytek_aiui_config = iflytek_aiui_config
        if iflytek_spark is not None:
            self.iflytek_spark = iflytek_spark
        if third_party_model_config is not None:
            self.third_party_model_config = third_party_model_config

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

        对接第三方应用厂商类型。 > 0：科大讯飞AIUI；1：华为云CBS；2：科大讯飞星火交互认知大模型；5：第三方驱动；6：第三方语言模型

        :return: The app_type of this UpdateRobotReq.
        :rtype: int
        """
        return self._app_type

    @app_type.setter
    def app_type(self, app_type):
        """Sets the app_type of this UpdateRobotReq.

        对接第三方应用厂商类型。 > 0：科大讯飞AIUI；1：华为云CBS；2：科大讯飞星火交互认知大模型；5：第三方驱动；6：第三方语言模型

        :param app_type: The app_type of this UpdateRobotReq.
        :type app_type: int
        """
        self._app_type = app_type

    @property
    def concurrency(self):
        """Gets the concurrency of this UpdateRobotReq.

        对话的并发数

        :return: The concurrency of this UpdateRobotReq.
        :rtype: int
        """
        return self._concurrency

    @concurrency.setter
    def concurrency(self, concurrency):
        """Sets the concurrency of this UpdateRobotReq.

        对话的并发数

        :param concurrency: The concurrency of this UpdateRobotReq.
        :type concurrency: int
        """
        self._concurrency = concurrency

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
