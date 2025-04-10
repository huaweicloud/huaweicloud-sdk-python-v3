# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InstanceSpc:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'org_peer_max_num': 'int',
        'orderer_max_num': 'int',
        'member_max_num': 'int'
    }

    attribute_map = {
        'org_peer_max_num': 'org_peer_max_num',
        'orderer_max_num': 'orderer_max_num',
        'member_max_num': 'member_max_num'
    }

    def __init__(self, org_peer_max_num=None, orderer_max_num=None, member_max_num=None):
        r"""InstanceSpc

        The model defined in huaweicloud sdk

        :param org_peer_max_num: 单个组织支持的最大peer节点数量
        :type org_peer_max_num: int
        :param orderer_max_num: 单个联盟链支持的最大order节点数量
        :type orderer_max_num: int
        :param member_max_num: 单个联盟链支持的最大租户数量
        :type member_max_num: int
        """
        
        

        self._org_peer_max_num = None
        self._orderer_max_num = None
        self._member_max_num = None
        self.discriminator = None

        if org_peer_max_num is not None:
            self.org_peer_max_num = org_peer_max_num
        if orderer_max_num is not None:
            self.orderer_max_num = orderer_max_num
        if member_max_num is not None:
            self.member_max_num = member_max_num

    @property
    def org_peer_max_num(self):
        r"""Gets the org_peer_max_num of this InstanceSpc.

        单个组织支持的最大peer节点数量

        :return: The org_peer_max_num of this InstanceSpc.
        :rtype: int
        """
        return self._org_peer_max_num

    @org_peer_max_num.setter
    def org_peer_max_num(self, org_peer_max_num):
        r"""Sets the org_peer_max_num of this InstanceSpc.

        单个组织支持的最大peer节点数量

        :param org_peer_max_num: The org_peer_max_num of this InstanceSpc.
        :type org_peer_max_num: int
        """
        self._org_peer_max_num = org_peer_max_num

    @property
    def orderer_max_num(self):
        r"""Gets the orderer_max_num of this InstanceSpc.

        单个联盟链支持的最大order节点数量

        :return: The orderer_max_num of this InstanceSpc.
        :rtype: int
        """
        return self._orderer_max_num

    @orderer_max_num.setter
    def orderer_max_num(self, orderer_max_num):
        r"""Sets the orderer_max_num of this InstanceSpc.

        单个联盟链支持的最大order节点数量

        :param orderer_max_num: The orderer_max_num of this InstanceSpc.
        :type orderer_max_num: int
        """
        self._orderer_max_num = orderer_max_num

    @property
    def member_max_num(self):
        r"""Gets the member_max_num of this InstanceSpc.

        单个联盟链支持的最大租户数量

        :return: The member_max_num of this InstanceSpc.
        :rtype: int
        """
        return self._member_max_num

    @member_max_num.setter
    def member_max_num(self, member_max_num):
        r"""Sets the member_max_num of this InstanceSpc.

        单个联盟链支持的最大租户数量

        :param member_max_num: The member_max_num of this InstanceSpc.
        :type member_max_num: int
        """
        self._member_max_num = member_max_num

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
        if not isinstance(other, InstanceSpc):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
