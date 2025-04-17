# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ValidateRobotReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'app_type': 'int',
        'huawei_ei_cbs': 'HuaweiEiCbs',
        'iflytek_aiui_config': 'IflytekAiuiConfig',
        'iflytek_spark': 'IflytekSpark',
        'third_party_model_config': 'ThirdPartyModelConfig',
        'mobvoi_config': 'MobvoiConfig',
        'wise_brain_config': 'WiseBrainConfig'
    }

    attribute_map = {
        'app_type': 'app_type',
        'huawei_ei_cbs': 'huawei_ei_cbs',
        'iflytek_aiui_config': 'iflytek_aiui_config',
        'iflytek_spark': 'iflytek_spark',
        'third_party_model_config': 'third_party_model_config',
        'mobvoi_config': 'mobvoi_config',
        'wise_brain_config': 'wise_brain_config'
    }

    def __init__(self, app_type=None, huawei_ei_cbs=None, iflytek_aiui_config=None, iflytek_spark=None, third_party_model_config=None, mobvoi_config=None, wise_brain_config=None):
        r"""ValidateRobotReq

        The model defined in huaweicloud sdk

        :param app_type: 对接第三方应用厂商类型。 &gt; 0：科大讯飞AIUI；1：华为云CBS；2：科大讯飞星火交互认知大模型；6：第三方语言模型；7：交互助手；8：奇妙问
        :type app_type: int
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
        :param wise_brain_config: 
        :type wise_brain_config: :class:`huaweicloudsdkmetastudio.v1.WiseBrainConfig`
        """
        
        

        self._app_type = None
        self._huawei_ei_cbs = None
        self._iflytek_aiui_config = None
        self._iflytek_spark = None
        self._third_party_model_config = None
        self._mobvoi_config = None
        self._wise_brain_config = None
        self.discriminator = None

        self.app_type = app_type
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
        if wise_brain_config is not None:
            self.wise_brain_config = wise_brain_config

    @property
    def app_type(self):
        r"""Gets the app_type of this ValidateRobotReq.

        对接第三方应用厂商类型。 > 0：科大讯飞AIUI；1：华为云CBS；2：科大讯飞星火交互认知大模型；6：第三方语言模型；7：交互助手；8：奇妙问

        :return: The app_type of this ValidateRobotReq.
        :rtype: int
        """
        return self._app_type

    @app_type.setter
    def app_type(self, app_type):
        r"""Sets the app_type of this ValidateRobotReq.

        对接第三方应用厂商类型。 > 0：科大讯飞AIUI；1：华为云CBS；2：科大讯飞星火交互认知大模型；6：第三方语言模型；7：交互助手；8：奇妙问

        :param app_type: The app_type of this ValidateRobotReq.
        :type app_type: int
        """
        self._app_type = app_type

    @property
    def huawei_ei_cbs(self):
        r"""Gets the huawei_ei_cbs of this ValidateRobotReq.

        :return: The huawei_ei_cbs of this ValidateRobotReq.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.HuaweiEiCbs`
        """
        return self._huawei_ei_cbs

    @huawei_ei_cbs.setter
    def huawei_ei_cbs(self, huawei_ei_cbs):
        r"""Sets the huawei_ei_cbs of this ValidateRobotReq.

        :param huawei_ei_cbs: The huawei_ei_cbs of this ValidateRobotReq.
        :type huawei_ei_cbs: :class:`huaweicloudsdkmetastudio.v1.HuaweiEiCbs`
        """
        self._huawei_ei_cbs = huawei_ei_cbs

    @property
    def iflytek_aiui_config(self):
        r"""Gets the iflytek_aiui_config of this ValidateRobotReq.

        :return: The iflytek_aiui_config of this ValidateRobotReq.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.IflytekAiuiConfig`
        """
        return self._iflytek_aiui_config

    @iflytek_aiui_config.setter
    def iflytek_aiui_config(self, iflytek_aiui_config):
        r"""Sets the iflytek_aiui_config of this ValidateRobotReq.

        :param iflytek_aiui_config: The iflytek_aiui_config of this ValidateRobotReq.
        :type iflytek_aiui_config: :class:`huaweicloudsdkmetastudio.v1.IflytekAiuiConfig`
        """
        self._iflytek_aiui_config = iflytek_aiui_config

    @property
    def iflytek_spark(self):
        r"""Gets the iflytek_spark of this ValidateRobotReq.

        :return: The iflytek_spark of this ValidateRobotReq.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.IflytekSpark`
        """
        return self._iflytek_spark

    @iflytek_spark.setter
    def iflytek_spark(self, iflytek_spark):
        r"""Sets the iflytek_spark of this ValidateRobotReq.

        :param iflytek_spark: The iflytek_spark of this ValidateRobotReq.
        :type iflytek_spark: :class:`huaweicloudsdkmetastudio.v1.IflytekSpark`
        """
        self._iflytek_spark = iflytek_spark

    @property
    def third_party_model_config(self):
        r"""Gets the third_party_model_config of this ValidateRobotReq.

        :return: The third_party_model_config of this ValidateRobotReq.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ThirdPartyModelConfig`
        """
        return self._third_party_model_config

    @third_party_model_config.setter
    def third_party_model_config(self, third_party_model_config):
        r"""Sets the third_party_model_config of this ValidateRobotReq.

        :param third_party_model_config: The third_party_model_config of this ValidateRobotReq.
        :type third_party_model_config: :class:`huaweicloudsdkmetastudio.v1.ThirdPartyModelConfig`
        """
        self._third_party_model_config = third_party_model_config

    @property
    def mobvoi_config(self):
        r"""Gets the mobvoi_config of this ValidateRobotReq.

        :return: The mobvoi_config of this ValidateRobotReq.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.MobvoiConfig`
        """
        return self._mobvoi_config

    @mobvoi_config.setter
    def mobvoi_config(self, mobvoi_config):
        r"""Sets the mobvoi_config of this ValidateRobotReq.

        :param mobvoi_config: The mobvoi_config of this ValidateRobotReq.
        :type mobvoi_config: :class:`huaweicloudsdkmetastudio.v1.MobvoiConfig`
        """
        self._mobvoi_config = mobvoi_config

    @property
    def wise_brain_config(self):
        r"""Gets the wise_brain_config of this ValidateRobotReq.

        :return: The wise_brain_config of this ValidateRobotReq.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.WiseBrainConfig`
        """
        return self._wise_brain_config

    @wise_brain_config.setter
    def wise_brain_config(self, wise_brain_config):
        r"""Sets the wise_brain_config of this ValidateRobotReq.

        :param wise_brain_config: The wise_brain_config of this ValidateRobotReq.
        :type wise_brain_config: :class:`huaweicloudsdkmetastudio.v1.WiseBrainConfig`
        """
        self._wise_brain_config = wise_brain_config

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
        if not isinstance(other, ValidateRobotReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
