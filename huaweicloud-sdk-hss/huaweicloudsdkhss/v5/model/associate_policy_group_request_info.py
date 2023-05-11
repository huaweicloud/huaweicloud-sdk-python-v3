# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AssociatePolicyGroupRequestInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'target_policy_group_id': 'str',
        'operate_all': 'bool',
        'host_id_list': 'list[str]'
    }

    attribute_map = {
        'target_policy_group_id': 'target_policy_group_id',
        'operate_all': 'operate_all',
        'host_id_list': 'host_id_list'
    }

    def __init__(self, target_policy_group_id=None, operate_all=None, host_id_list=None):
        """AssociatePolicyGroupRequestInfo

        The model defined in huaweicloud sdk

        :param target_policy_group_id: 部署的目标策略组ID
        :type target_policy_group_id: str
        :param operate_all: 是否要对全量主机部署策略，如果为true的话，不需填写host_id_list，如果为false的话，需要填写host_id_list
        :type operate_all: bool
        :param host_id_list: 服务器ID列表
        :type host_id_list: list[str]
        """
        
        

        self._target_policy_group_id = None
        self._operate_all = None
        self._host_id_list = None
        self.discriminator = None

        self.target_policy_group_id = target_policy_group_id
        if operate_all is not None:
            self.operate_all = operate_all
        if host_id_list is not None:
            self.host_id_list = host_id_list

    @property
    def target_policy_group_id(self):
        """Gets the target_policy_group_id of this AssociatePolicyGroupRequestInfo.

        部署的目标策略组ID

        :return: The target_policy_group_id of this AssociatePolicyGroupRequestInfo.
        :rtype: str
        """
        return self._target_policy_group_id

    @target_policy_group_id.setter
    def target_policy_group_id(self, target_policy_group_id):
        """Sets the target_policy_group_id of this AssociatePolicyGroupRequestInfo.

        部署的目标策略组ID

        :param target_policy_group_id: The target_policy_group_id of this AssociatePolicyGroupRequestInfo.
        :type target_policy_group_id: str
        """
        self._target_policy_group_id = target_policy_group_id

    @property
    def operate_all(self):
        """Gets the operate_all of this AssociatePolicyGroupRequestInfo.

        是否要对全量主机部署策略，如果为true的话，不需填写host_id_list，如果为false的话，需要填写host_id_list

        :return: The operate_all of this AssociatePolicyGroupRequestInfo.
        :rtype: bool
        """
        return self._operate_all

    @operate_all.setter
    def operate_all(self, operate_all):
        """Sets the operate_all of this AssociatePolicyGroupRequestInfo.

        是否要对全量主机部署策略，如果为true的话，不需填写host_id_list，如果为false的话，需要填写host_id_list

        :param operate_all: The operate_all of this AssociatePolicyGroupRequestInfo.
        :type operate_all: bool
        """
        self._operate_all = operate_all

    @property
    def host_id_list(self):
        """Gets the host_id_list of this AssociatePolicyGroupRequestInfo.

        服务器ID列表

        :return: The host_id_list of this AssociatePolicyGroupRequestInfo.
        :rtype: list[str]
        """
        return self._host_id_list

    @host_id_list.setter
    def host_id_list(self, host_id_list):
        """Sets the host_id_list of this AssociatePolicyGroupRequestInfo.

        服务器ID列表

        :param host_id_list: The host_id_list of this AssociatePolicyGroupRequestInfo.
        :type host_id_list: list[str]
        """
        self._host_id_list = host_id_list

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
        if not isinstance(other, AssociatePolicyGroupRequestInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
