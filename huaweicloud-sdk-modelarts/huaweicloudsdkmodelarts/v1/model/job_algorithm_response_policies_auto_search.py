# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class JobAlgorithmResponsePoliciesAutoSearch:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'skip_search_params': 'str',
        'reward_attrs': 'list[JobAlgorithmResponsePoliciesAutoSearchRewardAttrs]',
        'search_params': 'list[JobAlgorithmResponsePoliciesAutoSearchSearchParams]',
        'algo_configs': 'list[JobAlgorithmResponsePoliciesAutoSearchAlgoConfigs]'
    }

    attribute_map = {
        'skip_search_params': 'skip_search_params',
        'reward_attrs': 'reward_attrs',
        'search_params': 'search_params',
        'algo_configs': 'algo_configs'
    }

    def __init__(self, skip_search_params=None, reward_attrs=None, search_params=None, algo_configs=None):
        r"""JobAlgorithmResponsePoliciesAutoSearch

        The model defined in huaweicloud sdk

        :param skip_search_params: 需要排除的超参组合。
        :type skip_search_params: str
        :param reward_attrs: 搜索指标列表。
        :type reward_attrs: list[:class:`huaweicloudsdkmodelarts.v1.JobAlgorithmResponsePoliciesAutoSearchRewardAttrs`]
        :param search_params: 搜索参数。
        :type search_params: list[:class:`huaweicloudsdkmodelarts.v1.JobAlgorithmResponsePoliciesAutoSearchSearchParams`]
        :param algo_configs: 搜索算法配置。
        :type algo_configs: list[:class:`huaweicloudsdkmodelarts.v1.JobAlgorithmResponsePoliciesAutoSearchAlgoConfigs`]
        """
        
        

        self._skip_search_params = None
        self._reward_attrs = None
        self._search_params = None
        self._algo_configs = None
        self.discriminator = None

        if skip_search_params is not None:
            self.skip_search_params = skip_search_params
        if reward_attrs is not None:
            self.reward_attrs = reward_attrs
        if search_params is not None:
            self.search_params = search_params
        if algo_configs is not None:
            self.algo_configs = algo_configs

    @property
    def skip_search_params(self):
        r"""Gets the skip_search_params of this JobAlgorithmResponsePoliciesAutoSearch.

        需要排除的超参组合。

        :return: The skip_search_params of this JobAlgorithmResponsePoliciesAutoSearch.
        :rtype: str
        """
        return self._skip_search_params

    @skip_search_params.setter
    def skip_search_params(self, skip_search_params):
        r"""Sets the skip_search_params of this JobAlgorithmResponsePoliciesAutoSearch.

        需要排除的超参组合。

        :param skip_search_params: The skip_search_params of this JobAlgorithmResponsePoliciesAutoSearch.
        :type skip_search_params: str
        """
        self._skip_search_params = skip_search_params

    @property
    def reward_attrs(self):
        r"""Gets the reward_attrs of this JobAlgorithmResponsePoliciesAutoSearch.

        搜索指标列表。

        :return: The reward_attrs of this JobAlgorithmResponsePoliciesAutoSearch.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.JobAlgorithmResponsePoliciesAutoSearchRewardAttrs`]
        """
        return self._reward_attrs

    @reward_attrs.setter
    def reward_attrs(self, reward_attrs):
        r"""Sets the reward_attrs of this JobAlgorithmResponsePoliciesAutoSearch.

        搜索指标列表。

        :param reward_attrs: The reward_attrs of this JobAlgorithmResponsePoliciesAutoSearch.
        :type reward_attrs: list[:class:`huaweicloudsdkmodelarts.v1.JobAlgorithmResponsePoliciesAutoSearchRewardAttrs`]
        """
        self._reward_attrs = reward_attrs

    @property
    def search_params(self):
        r"""Gets the search_params of this JobAlgorithmResponsePoliciesAutoSearch.

        搜索参数。

        :return: The search_params of this JobAlgorithmResponsePoliciesAutoSearch.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.JobAlgorithmResponsePoliciesAutoSearchSearchParams`]
        """
        return self._search_params

    @search_params.setter
    def search_params(self, search_params):
        r"""Sets the search_params of this JobAlgorithmResponsePoliciesAutoSearch.

        搜索参数。

        :param search_params: The search_params of this JobAlgorithmResponsePoliciesAutoSearch.
        :type search_params: list[:class:`huaweicloudsdkmodelarts.v1.JobAlgorithmResponsePoliciesAutoSearchSearchParams`]
        """
        self._search_params = search_params

    @property
    def algo_configs(self):
        r"""Gets the algo_configs of this JobAlgorithmResponsePoliciesAutoSearch.

        搜索算法配置。

        :return: The algo_configs of this JobAlgorithmResponsePoliciesAutoSearch.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.JobAlgorithmResponsePoliciesAutoSearchAlgoConfigs`]
        """
        return self._algo_configs

    @algo_configs.setter
    def algo_configs(self, algo_configs):
        r"""Sets the algo_configs of this JobAlgorithmResponsePoliciesAutoSearch.

        搜索算法配置。

        :param algo_configs: The algo_configs of this JobAlgorithmResponsePoliciesAutoSearch.
        :type algo_configs: list[:class:`huaweicloudsdkmodelarts.v1.JobAlgorithmResponsePoliciesAutoSearchAlgoConfigs`]
        """
        self._algo_configs = algo_configs

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, JobAlgorithmResponsePoliciesAutoSearch):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
