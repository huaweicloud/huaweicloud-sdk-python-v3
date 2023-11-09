# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LeagueDatasetStatisticsVo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'dataset_domain_alias': 'str',
        'dataset_domain_name': 'str',
        'dataset_id': 'str',
        'dataset_intercept_cnt': 'int',
        'dataset_name': 'str',
        'dataset_use_cnt': 'int'
    }

    attribute_map = {
        'dataset_domain_alias': 'dataset_domain_alias',
        'dataset_domain_name': 'dataset_domain_name',
        'dataset_id': 'dataset_id',
        'dataset_intercept_cnt': 'dataset_intercept_cnt',
        'dataset_name': 'dataset_name',
        'dataset_use_cnt': 'dataset_use_cnt'
    }

    def __init__(self, dataset_domain_alias=None, dataset_domain_name=None, dataset_id=None, dataset_intercept_cnt=None, dataset_name=None, dataset_use_cnt=None):
        """LeagueDatasetStatisticsVo

        The model defined in huaweicloud sdk

        :param dataset_domain_alias: 参与方别名
        :type dataset_domain_alias: str
        :param dataset_domain_name: 参与方租户名称
        :type dataset_domain_name: str
        :param dataset_id: 数据集id
        :type dataset_id: str
        :param dataset_intercept_cnt: 数据集拦截次数
        :type dataset_intercept_cnt: int
        :param dataset_name: 数据集名称
        :type dataset_name: str
        :param dataset_use_cnt: 数据集使用次数
        :type dataset_use_cnt: int
        """
        
        

        self._dataset_domain_alias = None
        self._dataset_domain_name = None
        self._dataset_id = None
        self._dataset_intercept_cnt = None
        self._dataset_name = None
        self._dataset_use_cnt = None
        self.discriminator = None

        if dataset_domain_alias is not None:
            self.dataset_domain_alias = dataset_domain_alias
        if dataset_domain_name is not None:
            self.dataset_domain_name = dataset_domain_name
        if dataset_id is not None:
            self.dataset_id = dataset_id
        if dataset_intercept_cnt is not None:
            self.dataset_intercept_cnt = dataset_intercept_cnt
        if dataset_name is not None:
            self.dataset_name = dataset_name
        if dataset_use_cnt is not None:
            self.dataset_use_cnt = dataset_use_cnt

    @property
    def dataset_domain_alias(self):
        """Gets the dataset_domain_alias of this LeagueDatasetStatisticsVo.

        参与方别名

        :return: The dataset_domain_alias of this LeagueDatasetStatisticsVo.
        :rtype: str
        """
        return self._dataset_domain_alias

    @dataset_domain_alias.setter
    def dataset_domain_alias(self, dataset_domain_alias):
        """Sets the dataset_domain_alias of this LeagueDatasetStatisticsVo.

        参与方别名

        :param dataset_domain_alias: The dataset_domain_alias of this LeagueDatasetStatisticsVo.
        :type dataset_domain_alias: str
        """
        self._dataset_domain_alias = dataset_domain_alias

    @property
    def dataset_domain_name(self):
        """Gets the dataset_domain_name of this LeagueDatasetStatisticsVo.

        参与方租户名称

        :return: The dataset_domain_name of this LeagueDatasetStatisticsVo.
        :rtype: str
        """
        return self._dataset_domain_name

    @dataset_domain_name.setter
    def dataset_domain_name(self, dataset_domain_name):
        """Sets the dataset_domain_name of this LeagueDatasetStatisticsVo.

        参与方租户名称

        :param dataset_domain_name: The dataset_domain_name of this LeagueDatasetStatisticsVo.
        :type dataset_domain_name: str
        """
        self._dataset_domain_name = dataset_domain_name

    @property
    def dataset_id(self):
        """Gets the dataset_id of this LeagueDatasetStatisticsVo.

        数据集id

        :return: The dataset_id of this LeagueDatasetStatisticsVo.
        :rtype: str
        """
        return self._dataset_id

    @dataset_id.setter
    def dataset_id(self, dataset_id):
        """Sets the dataset_id of this LeagueDatasetStatisticsVo.

        数据集id

        :param dataset_id: The dataset_id of this LeagueDatasetStatisticsVo.
        :type dataset_id: str
        """
        self._dataset_id = dataset_id

    @property
    def dataset_intercept_cnt(self):
        """Gets the dataset_intercept_cnt of this LeagueDatasetStatisticsVo.

        数据集拦截次数

        :return: The dataset_intercept_cnt of this LeagueDatasetStatisticsVo.
        :rtype: int
        """
        return self._dataset_intercept_cnt

    @dataset_intercept_cnt.setter
    def dataset_intercept_cnt(self, dataset_intercept_cnt):
        """Sets the dataset_intercept_cnt of this LeagueDatasetStatisticsVo.

        数据集拦截次数

        :param dataset_intercept_cnt: The dataset_intercept_cnt of this LeagueDatasetStatisticsVo.
        :type dataset_intercept_cnt: int
        """
        self._dataset_intercept_cnt = dataset_intercept_cnt

    @property
    def dataset_name(self):
        """Gets the dataset_name of this LeagueDatasetStatisticsVo.

        数据集名称

        :return: The dataset_name of this LeagueDatasetStatisticsVo.
        :rtype: str
        """
        return self._dataset_name

    @dataset_name.setter
    def dataset_name(self, dataset_name):
        """Sets the dataset_name of this LeagueDatasetStatisticsVo.

        数据集名称

        :param dataset_name: The dataset_name of this LeagueDatasetStatisticsVo.
        :type dataset_name: str
        """
        self._dataset_name = dataset_name

    @property
    def dataset_use_cnt(self):
        """Gets the dataset_use_cnt of this LeagueDatasetStatisticsVo.

        数据集使用次数

        :return: The dataset_use_cnt of this LeagueDatasetStatisticsVo.
        :rtype: int
        """
        return self._dataset_use_cnt

    @dataset_use_cnt.setter
    def dataset_use_cnt(self, dataset_use_cnt):
        """Sets the dataset_use_cnt of this LeagueDatasetStatisticsVo.

        数据集使用次数

        :param dataset_use_cnt: The dataset_use_cnt of this LeagueDatasetStatisticsVo.
        :type dataset_use_cnt: int
        """
        self._dataset_use_cnt = dataset_use_cnt

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
        if not isinstance(other, LeagueDatasetStatisticsVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
