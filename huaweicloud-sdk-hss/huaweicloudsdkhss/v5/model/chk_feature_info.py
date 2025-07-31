# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChkFeatureInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'chk_feature_id': 'int',
        'protective_action': 'int',
        'enabled': 'int',
        'feature_configure': 'str'
    }

    attribute_map = {
        'chk_feature_id': 'chk_feature_id',
        'protective_action': 'protective_action',
        'enabled': 'enabled',
        'feature_configure': 'feature_configure'
    }

    def __init__(self, chk_feature_id=None, protective_action=None, enabled=None, feature_configure=None):
        r"""ChkFeatureInfo

        The model defined in huaweicloud sdk

        :param chk_feature_id: 检测特性规则ID
        :type chk_feature_id: int
        :param protective_action: 防护动作 1 检测  2 检测并阻断/拦截
        :type protective_action: int
        :param enabled: 开启状态 0 关闭 1 开启
        :type enabled: int
        :param feature_configure: 检测特性规则配置信息
        :type feature_configure: str
        """
        
        

        self._chk_feature_id = None
        self._protective_action = None
        self._enabled = None
        self._feature_configure = None
        self.discriminator = None

        self.chk_feature_id = chk_feature_id
        self.protective_action = protective_action
        self.enabled = enabled
        self.feature_configure = feature_configure

    @property
    def chk_feature_id(self):
        r"""Gets the chk_feature_id of this ChkFeatureInfo.

        检测特性规则ID

        :return: The chk_feature_id of this ChkFeatureInfo.
        :rtype: int
        """
        return self._chk_feature_id

    @chk_feature_id.setter
    def chk_feature_id(self, chk_feature_id):
        r"""Sets the chk_feature_id of this ChkFeatureInfo.

        检测特性规则ID

        :param chk_feature_id: The chk_feature_id of this ChkFeatureInfo.
        :type chk_feature_id: int
        """
        self._chk_feature_id = chk_feature_id

    @property
    def protective_action(self):
        r"""Gets the protective_action of this ChkFeatureInfo.

        防护动作 1 检测  2 检测并阻断/拦截

        :return: The protective_action of this ChkFeatureInfo.
        :rtype: int
        """
        return self._protective_action

    @protective_action.setter
    def protective_action(self, protective_action):
        r"""Sets the protective_action of this ChkFeatureInfo.

        防护动作 1 检测  2 检测并阻断/拦截

        :param protective_action: The protective_action of this ChkFeatureInfo.
        :type protective_action: int
        """
        self._protective_action = protective_action

    @property
    def enabled(self):
        r"""Gets the enabled of this ChkFeatureInfo.

        开启状态 0 关闭 1 开启

        :return: The enabled of this ChkFeatureInfo.
        :rtype: int
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        r"""Sets the enabled of this ChkFeatureInfo.

        开启状态 0 关闭 1 开启

        :param enabled: The enabled of this ChkFeatureInfo.
        :type enabled: int
        """
        self._enabled = enabled

    @property
    def feature_configure(self):
        r"""Gets the feature_configure of this ChkFeatureInfo.

        检测特性规则配置信息

        :return: The feature_configure of this ChkFeatureInfo.
        :rtype: str
        """
        return self._feature_configure

    @feature_configure.setter
    def feature_configure(self, feature_configure):
        r"""Sets the feature_configure of this ChkFeatureInfo.

        检测特性规则配置信息

        :param feature_configure: The feature_configure of this ChkFeatureInfo.
        :type feature_configure: str
        """
        self._feature_configure = feature_configure

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
        if not isinstance(other, ChkFeatureInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
