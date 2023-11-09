# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class JobReportPartnerVo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'agent_name': 'str',
        'data_output_cnt': 'int',
        'dataset_name': 'str',
        'partner_domain_alias': 'str',
        'partner_domain_name': 'str'
    }

    attribute_map = {
        'agent_name': 'agent_name',
        'data_output_cnt': 'data_output_cnt',
        'dataset_name': 'dataset_name',
        'partner_domain_alias': 'partner_domain_alias',
        'partner_domain_name': 'partner_domain_name'
    }

    def __init__(self, agent_name=None, data_output_cnt=None, dataset_name=None, partner_domain_alias=None, partner_domain_name=None):
        """JobReportPartnerVo

        The model defined in huaweicloud sdk

        :param agent_name: 数据集所在代理
        :type agent_name: str
        :param data_output_cnt: 代理输出数据总量
        :type data_output_cnt: int
        :param dataset_name: 数据集名
        :type dataset_name: str
        :param partner_domain_alias: 租户别名
        :type partner_domain_alias: str
        :param partner_domain_name: 租户名
        :type partner_domain_name: str
        """
        
        

        self._agent_name = None
        self._data_output_cnt = None
        self._dataset_name = None
        self._partner_domain_alias = None
        self._partner_domain_name = None
        self.discriminator = None

        if agent_name is not None:
            self.agent_name = agent_name
        if data_output_cnt is not None:
            self.data_output_cnt = data_output_cnt
        if dataset_name is not None:
            self.dataset_name = dataset_name
        if partner_domain_alias is not None:
            self.partner_domain_alias = partner_domain_alias
        if partner_domain_name is not None:
            self.partner_domain_name = partner_domain_name

    @property
    def agent_name(self):
        """Gets the agent_name of this JobReportPartnerVo.

        数据集所在代理

        :return: The agent_name of this JobReportPartnerVo.
        :rtype: str
        """
        return self._agent_name

    @agent_name.setter
    def agent_name(self, agent_name):
        """Sets the agent_name of this JobReportPartnerVo.

        数据集所在代理

        :param agent_name: The agent_name of this JobReportPartnerVo.
        :type agent_name: str
        """
        self._agent_name = agent_name

    @property
    def data_output_cnt(self):
        """Gets the data_output_cnt of this JobReportPartnerVo.

        代理输出数据总量

        :return: The data_output_cnt of this JobReportPartnerVo.
        :rtype: int
        """
        return self._data_output_cnt

    @data_output_cnt.setter
    def data_output_cnt(self, data_output_cnt):
        """Sets the data_output_cnt of this JobReportPartnerVo.

        代理输出数据总量

        :param data_output_cnt: The data_output_cnt of this JobReportPartnerVo.
        :type data_output_cnt: int
        """
        self._data_output_cnt = data_output_cnt

    @property
    def dataset_name(self):
        """Gets the dataset_name of this JobReportPartnerVo.

        数据集名

        :return: The dataset_name of this JobReportPartnerVo.
        :rtype: str
        """
        return self._dataset_name

    @dataset_name.setter
    def dataset_name(self, dataset_name):
        """Sets the dataset_name of this JobReportPartnerVo.

        数据集名

        :param dataset_name: The dataset_name of this JobReportPartnerVo.
        :type dataset_name: str
        """
        self._dataset_name = dataset_name

    @property
    def partner_domain_alias(self):
        """Gets the partner_domain_alias of this JobReportPartnerVo.

        租户别名

        :return: The partner_domain_alias of this JobReportPartnerVo.
        :rtype: str
        """
        return self._partner_domain_alias

    @partner_domain_alias.setter
    def partner_domain_alias(self, partner_domain_alias):
        """Sets the partner_domain_alias of this JobReportPartnerVo.

        租户别名

        :param partner_domain_alias: The partner_domain_alias of this JobReportPartnerVo.
        :type partner_domain_alias: str
        """
        self._partner_domain_alias = partner_domain_alias

    @property
    def partner_domain_name(self):
        """Gets the partner_domain_name of this JobReportPartnerVo.

        租户名

        :return: The partner_domain_name of this JobReportPartnerVo.
        :rtype: str
        """
        return self._partner_domain_name

    @partner_domain_name.setter
    def partner_domain_name(self, partner_domain_name):
        """Sets the partner_domain_name of this JobReportPartnerVo.

        租户名

        :param partner_domain_name: The partner_domain_name of this JobReportPartnerVo.
        :type partner_domain_name: str
        """
        self._partner_domain_name = partner_domain_name

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
        if not isinstance(other, JobReportPartnerVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
