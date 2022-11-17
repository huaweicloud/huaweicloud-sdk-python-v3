# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MatchFeaturePair:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'user_feature_name': 'str',
        'item_feature_name': 'str',
        'weight': 'float',
        'match_count': 'bool'
    }

    attribute_map = {
        'user_feature_name': 'user_feature_name',
        'item_feature_name': 'item_feature_name',
        'weight': 'weight',
        'match_count': 'match_count'
    }

    def __init__(self, user_feature_name=None, item_feature_name=None, weight=None, match_count=None):
        """MatchFeaturePair

        The model defined in huaweicloud sdk

        :param user_feature_name: 用户特征。
        :type user_feature_name: str
        :param item_feature_name: 物品特征。
        :type item_feature_name: str
        :param weight: 权重。
        :type weight: float
        :param match_count: 匹配个数度量。
        :type match_count: bool
        """
        
        

        self._user_feature_name = None
        self._item_feature_name = None
        self._weight = None
        self._match_count = None
        self.discriminator = None

        if user_feature_name is not None:
            self.user_feature_name = user_feature_name
        if item_feature_name is not None:
            self.item_feature_name = item_feature_name
        if weight is not None:
            self.weight = weight
        if match_count is not None:
            self.match_count = match_count

    @property
    def user_feature_name(self):
        """Gets the user_feature_name of this MatchFeaturePair.

        用户特征。

        :return: The user_feature_name of this MatchFeaturePair.
        :rtype: str
        """
        return self._user_feature_name

    @user_feature_name.setter
    def user_feature_name(self, user_feature_name):
        """Sets the user_feature_name of this MatchFeaturePair.

        用户特征。

        :param user_feature_name: The user_feature_name of this MatchFeaturePair.
        :type user_feature_name: str
        """
        self._user_feature_name = user_feature_name

    @property
    def item_feature_name(self):
        """Gets the item_feature_name of this MatchFeaturePair.

        物品特征。

        :return: The item_feature_name of this MatchFeaturePair.
        :rtype: str
        """
        return self._item_feature_name

    @item_feature_name.setter
    def item_feature_name(self, item_feature_name):
        """Sets the item_feature_name of this MatchFeaturePair.

        物品特征。

        :param item_feature_name: The item_feature_name of this MatchFeaturePair.
        :type item_feature_name: str
        """
        self._item_feature_name = item_feature_name

    @property
    def weight(self):
        """Gets the weight of this MatchFeaturePair.

        权重。

        :return: The weight of this MatchFeaturePair.
        :rtype: float
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this MatchFeaturePair.

        权重。

        :param weight: The weight of this MatchFeaturePair.
        :type weight: float
        """
        self._weight = weight

    @property
    def match_count(self):
        """Gets the match_count of this MatchFeaturePair.

        匹配个数度量。

        :return: The match_count of this MatchFeaturePair.
        :rtype: bool
        """
        return self._match_count

    @match_count.setter
    def match_count(self, match_count):
        """Sets the match_count of this MatchFeaturePair.

        匹配个数度量。

        :param match_count: The match_count of this MatchFeaturePair.
        :type match_count: bool
        """
        self._match_count = match_count

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
        if not isinstance(other, MatchFeaturePair):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
