# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FeatureRuleInfo:

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
        'chk_feature_name': 'str',
        'chk_feature_desc': 'str',
        'os_type': 'str',
        'feature_configure': 'str',
        'optional_protective_action': 'int',
        'protective_action': 'int',
        'editable': 'int'
    }

    attribute_map = {
        'chk_feature_id': 'chk_feature_id',
        'chk_feature_name': 'chk_feature_name',
        'chk_feature_desc': 'chk_feature_desc',
        'os_type': 'os_type',
        'feature_configure': 'feature_configure',
        'optional_protective_action': 'optional_protective_action',
        'protective_action': 'protective_action',
        'editable': 'editable'
    }

    def __init__(self, chk_feature_id=None, chk_feature_name=None, chk_feature_desc=None, os_type=None, feature_configure=None, optional_protective_action=None, protective_action=None, editable=None):
        r"""FeatureRuleInfo

        The model defined in huaweicloud sdk

        :param chk_feature_id: 检测特性规则ID
        :type chk_feature_id: int
        :param chk_feature_name: 检测特性规则标识
        :type chk_feature_name: str
        :param chk_feature_desc: 检测特性规则描述
        :type chk_feature_desc: str
        :param os_type: 操作系统类型
        :type os_type: str
        :param feature_configure: 检测特性规则配置信息
        :type feature_configure: str
        :param optional_protective_action: 可选防护动作，包含如下 -1 检测   -2 检测并阻断/拦截   -3 都可以
        :type optional_protective_action: int
        :param protective_action: 默认防护动作，包含如下 -1 检测   -2 检测并阻断/拦截
        :type protective_action: int
        :param editable: 是否可编辑配置信息，包含如下 -0 否   -1 是
        :type editable: int
        """
        
        

        self._chk_feature_id = None
        self._chk_feature_name = None
        self._chk_feature_desc = None
        self._os_type = None
        self._feature_configure = None
        self._optional_protective_action = None
        self._protective_action = None
        self._editable = None
        self.discriminator = None

        if chk_feature_id is not None:
            self.chk_feature_id = chk_feature_id
        if chk_feature_name is not None:
            self.chk_feature_name = chk_feature_name
        if chk_feature_desc is not None:
            self.chk_feature_desc = chk_feature_desc
        if os_type is not None:
            self.os_type = os_type
        if feature_configure is not None:
            self.feature_configure = feature_configure
        if optional_protective_action is not None:
            self.optional_protective_action = optional_protective_action
        if protective_action is not None:
            self.protective_action = protective_action
        if editable is not None:
            self.editable = editable

    @property
    def chk_feature_id(self):
        r"""Gets the chk_feature_id of this FeatureRuleInfo.

        检测特性规则ID

        :return: The chk_feature_id of this FeatureRuleInfo.
        :rtype: int
        """
        return self._chk_feature_id

    @chk_feature_id.setter
    def chk_feature_id(self, chk_feature_id):
        r"""Sets the chk_feature_id of this FeatureRuleInfo.

        检测特性规则ID

        :param chk_feature_id: The chk_feature_id of this FeatureRuleInfo.
        :type chk_feature_id: int
        """
        self._chk_feature_id = chk_feature_id

    @property
    def chk_feature_name(self):
        r"""Gets the chk_feature_name of this FeatureRuleInfo.

        检测特性规则标识

        :return: The chk_feature_name of this FeatureRuleInfo.
        :rtype: str
        """
        return self._chk_feature_name

    @chk_feature_name.setter
    def chk_feature_name(self, chk_feature_name):
        r"""Sets the chk_feature_name of this FeatureRuleInfo.

        检测特性规则标识

        :param chk_feature_name: The chk_feature_name of this FeatureRuleInfo.
        :type chk_feature_name: str
        """
        self._chk_feature_name = chk_feature_name

    @property
    def chk_feature_desc(self):
        r"""Gets the chk_feature_desc of this FeatureRuleInfo.

        检测特性规则描述

        :return: The chk_feature_desc of this FeatureRuleInfo.
        :rtype: str
        """
        return self._chk_feature_desc

    @chk_feature_desc.setter
    def chk_feature_desc(self, chk_feature_desc):
        r"""Sets the chk_feature_desc of this FeatureRuleInfo.

        检测特性规则描述

        :param chk_feature_desc: The chk_feature_desc of this FeatureRuleInfo.
        :type chk_feature_desc: str
        """
        self._chk_feature_desc = chk_feature_desc

    @property
    def os_type(self):
        r"""Gets the os_type of this FeatureRuleInfo.

        操作系统类型

        :return: The os_type of this FeatureRuleInfo.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        r"""Sets the os_type of this FeatureRuleInfo.

        操作系统类型

        :param os_type: The os_type of this FeatureRuleInfo.
        :type os_type: str
        """
        self._os_type = os_type

    @property
    def feature_configure(self):
        r"""Gets the feature_configure of this FeatureRuleInfo.

        检测特性规则配置信息

        :return: The feature_configure of this FeatureRuleInfo.
        :rtype: str
        """
        return self._feature_configure

    @feature_configure.setter
    def feature_configure(self, feature_configure):
        r"""Sets the feature_configure of this FeatureRuleInfo.

        检测特性规则配置信息

        :param feature_configure: The feature_configure of this FeatureRuleInfo.
        :type feature_configure: str
        """
        self._feature_configure = feature_configure

    @property
    def optional_protective_action(self):
        r"""Gets the optional_protective_action of this FeatureRuleInfo.

        可选防护动作，包含如下 -1 检测   -2 检测并阻断/拦截   -3 都可以

        :return: The optional_protective_action of this FeatureRuleInfo.
        :rtype: int
        """
        return self._optional_protective_action

    @optional_protective_action.setter
    def optional_protective_action(self, optional_protective_action):
        r"""Sets the optional_protective_action of this FeatureRuleInfo.

        可选防护动作，包含如下 -1 检测   -2 检测并阻断/拦截   -3 都可以

        :param optional_protective_action: The optional_protective_action of this FeatureRuleInfo.
        :type optional_protective_action: int
        """
        self._optional_protective_action = optional_protective_action

    @property
    def protective_action(self):
        r"""Gets the protective_action of this FeatureRuleInfo.

        默认防护动作，包含如下 -1 检测   -2 检测并阻断/拦截

        :return: The protective_action of this FeatureRuleInfo.
        :rtype: int
        """
        return self._protective_action

    @protective_action.setter
    def protective_action(self, protective_action):
        r"""Sets the protective_action of this FeatureRuleInfo.

        默认防护动作，包含如下 -1 检测   -2 检测并阻断/拦截

        :param protective_action: The protective_action of this FeatureRuleInfo.
        :type protective_action: int
        """
        self._protective_action = protective_action

    @property
    def editable(self):
        r"""Gets the editable of this FeatureRuleInfo.

        是否可编辑配置信息，包含如下 -0 否   -1 是

        :return: The editable of this FeatureRuleInfo.
        :rtype: int
        """
        return self._editable

    @editable.setter
    def editable(self, editable):
        r"""Sets the editable of this FeatureRuleInfo.

        是否可编辑配置信息，包含如下 -0 否   -1 是

        :param editable: The editable of this FeatureRuleInfo.
        :type editable: int
        """
        self._editable = editable

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
        if not isinstance(other, FeatureRuleInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
