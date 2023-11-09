# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAgentDetailResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'agent_deploy': 'TicsAgentDeploy',
        'agent_deploy_bcs': 'TicsAgentDeployBcs',
        'agent_deploy_detail': 'TicsAgentDeployDetail',
        'agent_deploy_nat': 'TicsAgentNatCommonInfo',
        'agent_deploy_node': 'TicsAgentNodeInfo'
    }

    attribute_map = {
        'agent_deploy': 'agent_deploy',
        'agent_deploy_bcs': 'agent_deploy_bcs',
        'agent_deploy_detail': 'agent_deploy_detail',
        'agent_deploy_nat': 'agent_deploy_nat',
        'agent_deploy_node': 'agent_deploy_node'
    }

    def __init__(self, agent_deploy=None, agent_deploy_bcs=None, agent_deploy_detail=None, agent_deploy_nat=None, agent_deploy_node=None):
        """ShowAgentDetailResponse

        The model defined in huaweicloud sdk

        :param agent_deploy: 
        :type agent_deploy: :class:`huaweicloudsdktics.v1.TicsAgentDeploy`
        :param agent_deploy_bcs: 
        :type agent_deploy_bcs: :class:`huaweicloudsdktics.v1.TicsAgentDeployBcs`
        :param agent_deploy_detail: 
        :type agent_deploy_detail: :class:`huaweicloudsdktics.v1.TicsAgentDeployDetail`
        :param agent_deploy_nat: 
        :type agent_deploy_nat: :class:`huaweicloudsdktics.v1.TicsAgentNatCommonInfo`
        :param agent_deploy_node: 
        :type agent_deploy_node: :class:`huaweicloudsdktics.v1.TicsAgentNodeInfo`
        """
        
        super(ShowAgentDetailResponse, self).__init__()

        self._agent_deploy = None
        self._agent_deploy_bcs = None
        self._agent_deploy_detail = None
        self._agent_deploy_nat = None
        self._agent_deploy_node = None
        self.discriminator = None

        if agent_deploy is not None:
            self.agent_deploy = agent_deploy
        if agent_deploy_bcs is not None:
            self.agent_deploy_bcs = agent_deploy_bcs
        if agent_deploy_detail is not None:
            self.agent_deploy_detail = agent_deploy_detail
        if agent_deploy_nat is not None:
            self.agent_deploy_nat = agent_deploy_nat
        if agent_deploy_node is not None:
            self.agent_deploy_node = agent_deploy_node

    @property
    def agent_deploy(self):
        """Gets the agent_deploy of this ShowAgentDetailResponse.

        :return: The agent_deploy of this ShowAgentDetailResponse.
        :rtype: :class:`huaweicloudsdktics.v1.TicsAgentDeploy`
        """
        return self._agent_deploy

    @agent_deploy.setter
    def agent_deploy(self, agent_deploy):
        """Sets the agent_deploy of this ShowAgentDetailResponse.

        :param agent_deploy: The agent_deploy of this ShowAgentDetailResponse.
        :type agent_deploy: :class:`huaweicloudsdktics.v1.TicsAgentDeploy`
        """
        self._agent_deploy = agent_deploy

    @property
    def agent_deploy_bcs(self):
        """Gets the agent_deploy_bcs of this ShowAgentDetailResponse.

        :return: The agent_deploy_bcs of this ShowAgentDetailResponse.
        :rtype: :class:`huaweicloudsdktics.v1.TicsAgentDeployBcs`
        """
        return self._agent_deploy_bcs

    @agent_deploy_bcs.setter
    def agent_deploy_bcs(self, agent_deploy_bcs):
        """Sets the agent_deploy_bcs of this ShowAgentDetailResponse.

        :param agent_deploy_bcs: The agent_deploy_bcs of this ShowAgentDetailResponse.
        :type agent_deploy_bcs: :class:`huaweicloudsdktics.v1.TicsAgentDeployBcs`
        """
        self._agent_deploy_bcs = agent_deploy_bcs

    @property
    def agent_deploy_detail(self):
        """Gets the agent_deploy_detail of this ShowAgentDetailResponse.

        :return: The agent_deploy_detail of this ShowAgentDetailResponse.
        :rtype: :class:`huaweicloudsdktics.v1.TicsAgentDeployDetail`
        """
        return self._agent_deploy_detail

    @agent_deploy_detail.setter
    def agent_deploy_detail(self, agent_deploy_detail):
        """Sets the agent_deploy_detail of this ShowAgentDetailResponse.

        :param agent_deploy_detail: The agent_deploy_detail of this ShowAgentDetailResponse.
        :type agent_deploy_detail: :class:`huaweicloudsdktics.v1.TicsAgentDeployDetail`
        """
        self._agent_deploy_detail = agent_deploy_detail

    @property
    def agent_deploy_nat(self):
        """Gets the agent_deploy_nat of this ShowAgentDetailResponse.

        :return: The agent_deploy_nat of this ShowAgentDetailResponse.
        :rtype: :class:`huaweicloudsdktics.v1.TicsAgentNatCommonInfo`
        """
        return self._agent_deploy_nat

    @agent_deploy_nat.setter
    def agent_deploy_nat(self, agent_deploy_nat):
        """Sets the agent_deploy_nat of this ShowAgentDetailResponse.

        :param agent_deploy_nat: The agent_deploy_nat of this ShowAgentDetailResponse.
        :type agent_deploy_nat: :class:`huaweicloudsdktics.v1.TicsAgentNatCommonInfo`
        """
        self._agent_deploy_nat = agent_deploy_nat

    @property
    def agent_deploy_node(self):
        """Gets the agent_deploy_node of this ShowAgentDetailResponse.

        :return: The agent_deploy_node of this ShowAgentDetailResponse.
        :rtype: :class:`huaweicloudsdktics.v1.TicsAgentNodeInfo`
        """
        return self._agent_deploy_node

    @agent_deploy_node.setter
    def agent_deploy_node(self, agent_deploy_node):
        """Sets the agent_deploy_node of this ShowAgentDetailResponse.

        :param agent_deploy_node: The agent_deploy_node of this ShowAgentDetailResponse.
        :type agent_deploy_node: :class:`huaweicloudsdktics.v1.TicsAgentNodeInfo`
        """
        self._agent_deploy_node = agent_deploy_node

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
        if not isinstance(other, ShowAgentDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
