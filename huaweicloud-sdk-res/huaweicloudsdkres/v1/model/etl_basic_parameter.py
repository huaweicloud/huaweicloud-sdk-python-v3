# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EtlBasicParameter:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'user_features': 'list[FeatureTransformation]',
        'item_features': 'list[FeatureTransformation]',
        'rank_etl_filter': 'RankETLFilter'
    }

    attribute_map = {
        'user_features': 'user_features',
        'item_features': 'item_features',
        'rank_etl_filter': 'rank_etl_filter'
    }

    def __init__(self, user_features=None, item_features=None, rank_etl_filter=None):
        """EtlBasicParameter

        The model defined in huaweicloud sdk

        :param user_features: 用户特征。
        :type user_features: list[:class:`huaweicloudsdkres.v1.FeatureTransformation`]
        :param item_features: 物品特征。
        :type item_features: list[:class:`huaweicloudsdkres.v1.FeatureTransformation`]
        :param rank_etl_filter: 
        :type rank_etl_filter: :class:`huaweicloudsdkres.v1.RankETLFilter`
        """
        
        

        self._user_features = None
        self._item_features = None
        self._rank_etl_filter = None
        self.discriminator = None

        if user_features is not None:
            self.user_features = user_features
        if item_features is not None:
            self.item_features = item_features
        if rank_etl_filter is not None:
            self.rank_etl_filter = rank_etl_filter

    @property
    def user_features(self):
        """Gets the user_features of this EtlBasicParameter.

        用户特征。

        :return: The user_features of this EtlBasicParameter.
        :rtype: list[:class:`huaweicloudsdkres.v1.FeatureTransformation`]
        """
        return self._user_features

    @user_features.setter
    def user_features(self, user_features):
        """Sets the user_features of this EtlBasicParameter.

        用户特征。

        :param user_features: The user_features of this EtlBasicParameter.
        :type user_features: list[:class:`huaweicloudsdkres.v1.FeatureTransformation`]
        """
        self._user_features = user_features

    @property
    def item_features(self):
        """Gets the item_features of this EtlBasicParameter.

        物品特征。

        :return: The item_features of this EtlBasicParameter.
        :rtype: list[:class:`huaweicloudsdkres.v1.FeatureTransformation`]
        """
        return self._item_features

    @item_features.setter
    def item_features(self, item_features):
        """Sets the item_features of this EtlBasicParameter.

        物品特征。

        :param item_features: The item_features of this EtlBasicParameter.
        :type item_features: list[:class:`huaweicloudsdkres.v1.FeatureTransformation`]
        """
        self._item_features = item_features

    @property
    def rank_etl_filter(self):
        """Gets the rank_etl_filter of this EtlBasicParameter.


        :return: The rank_etl_filter of this EtlBasicParameter.
        :rtype: :class:`huaweicloudsdkres.v1.RankETLFilter`
        """
        return self._rank_etl_filter

    @rank_etl_filter.setter
    def rank_etl_filter(self, rank_etl_filter):
        """Sets the rank_etl_filter of this EtlBasicParameter.


        :param rank_etl_filter: The rank_etl_filter of this EtlBasicParameter.
        :type rank_etl_filter: :class:`huaweicloudsdkres.v1.RankETLFilter`
        """
        self._rank_etl_filter = rank_etl_filter

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
        if not isinstance(other, EtlBasicParameter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
