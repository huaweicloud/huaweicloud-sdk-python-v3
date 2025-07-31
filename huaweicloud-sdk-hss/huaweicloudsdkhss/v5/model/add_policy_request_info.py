# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddPolicyRequestInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'feature_list': 'list[ChkFeatureInfo]'
    }

    attribute_map = {
        'feature_list': 'feature_list'
    }

    def __init__(self, feature_list=None):
        r"""AddPolicyRequestInfo

        The model defined in huaweicloud sdk

        :param feature_list: 检测特性规则列表
        :type feature_list: list[:class:`huaweicloudsdkhss.v5.ChkFeatureInfo`]
        """
        
        

        self._feature_list = None
        self.discriminator = None

        if feature_list is not None:
            self.feature_list = feature_list

    @property
    def feature_list(self):
        r"""Gets the feature_list of this AddPolicyRequestInfo.

        检测特性规则列表

        :return: The feature_list of this AddPolicyRequestInfo.
        :rtype: list[:class:`huaweicloudsdkhss.v5.ChkFeatureInfo`]
        """
        return self._feature_list

    @feature_list.setter
    def feature_list(self, feature_list):
        r"""Sets the feature_list of this AddPolicyRequestInfo.

        检测特性规则列表

        :param feature_list: The feature_list of this AddPolicyRequestInfo.
        :type feature_list: list[:class:`huaweicloudsdkhss.v5.ChkFeatureInfo`]
        """
        self._feature_list = feature_list

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
        if not isinstance(other, AddPolicyRequestInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
