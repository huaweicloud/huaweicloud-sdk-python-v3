# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NodeOrgs:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'node_count': 'int',
        'pvc_name': 'str'
    }

    attribute_map = {
        'name': 'name',
        'node_count': 'node_count',
        'pvc_name': 'pvc_name'
    }

    def __init__(self, name=None, node_count=None, pvc_name=None):
        """NodeOrgs

        The model defined in huaweicloud sdk

        :param name: 组织名称，IEF节点绑定模式下组织名与IEF节点名称保持一致。支持英文，数字，中文字符和中划线(-), 不能以中划线(-)开头，长度4-24个字符
        :type name: str
        :param node_count: 组织目标节点数, 1-2的正整数
        :type node_count: int
        :param pvc_name: pvc名称，添加组织时需要提供pvc_name。CCE模式必填
        :type pvc_name: str
        """
        
        

        self._name = None
        self._node_count = None
        self._pvc_name = None
        self.discriminator = None

        self.name = name
        self.node_count = node_count
        if pvc_name is not None:
            self.pvc_name = pvc_name

    @property
    def name(self):
        """Gets the name of this NodeOrgs.

        组织名称，IEF节点绑定模式下组织名与IEF节点名称保持一致。支持英文，数字，中文字符和中划线(-), 不能以中划线(-)开头，长度4-24个字符

        :return: The name of this NodeOrgs.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NodeOrgs.

        组织名称，IEF节点绑定模式下组织名与IEF节点名称保持一致。支持英文，数字，中文字符和中划线(-), 不能以中划线(-)开头，长度4-24个字符

        :param name: The name of this NodeOrgs.
        :type name: str
        """
        self._name = name

    @property
    def node_count(self):
        """Gets the node_count of this NodeOrgs.

        组织目标节点数, 1-2的正整数

        :return: The node_count of this NodeOrgs.
        :rtype: int
        """
        return self._node_count

    @node_count.setter
    def node_count(self, node_count):
        """Sets the node_count of this NodeOrgs.

        组织目标节点数, 1-2的正整数

        :param node_count: The node_count of this NodeOrgs.
        :type node_count: int
        """
        self._node_count = node_count

    @property
    def pvc_name(self):
        """Gets the pvc_name of this NodeOrgs.

        pvc名称，添加组织时需要提供pvc_name。CCE模式必填

        :return: The pvc_name of this NodeOrgs.
        :rtype: str
        """
        return self._pvc_name

    @pvc_name.setter
    def pvc_name(self, pvc_name):
        """Sets the pvc_name of this NodeOrgs.

        pvc名称，添加组织时需要提供pvc_name。CCE模式必填

        :param pvc_name: The pvc_name of this NodeOrgs.
        :type pvc_name: str
        """
        self._pvc_name = pvc_name

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
        if not isinstance(other, NodeOrgs):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
