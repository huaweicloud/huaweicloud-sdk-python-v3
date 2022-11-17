# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EdgeContentRsp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'iotda_instance_id': 'str',
        'rules': 'list[EdgeContentRuleRsp]'
    }

    attribute_map = {
        'iotda_instance_id': 'iotda_instance_id',
        'rules': 'rules'
    }

    def __init__(self, iotda_instance_id=None, rules=None):
        """EdgeContentRsp

        The model defined in huaweicloud sdk

        :param iotda_instance_id: Edge实例Id
        :type iotda_instance_id: str
        :param rules: 在Edge实例中要配置的转发规则，包含推送数据的资源空间和产品列表
        :type rules: list[:class:`huaweicloudsdkiotanalytics.v1.EdgeContentRuleRsp`]
        """
        
        

        self._iotda_instance_id = None
        self._rules = None
        self.discriminator = None

        self.iotda_instance_id = iotda_instance_id
        self.rules = rules

    @property
    def iotda_instance_id(self):
        """Gets the iotda_instance_id of this EdgeContentRsp.

        Edge实例Id

        :return: The iotda_instance_id of this EdgeContentRsp.
        :rtype: str
        """
        return self._iotda_instance_id

    @iotda_instance_id.setter
    def iotda_instance_id(self, iotda_instance_id):
        """Sets the iotda_instance_id of this EdgeContentRsp.

        Edge实例Id

        :param iotda_instance_id: The iotda_instance_id of this EdgeContentRsp.
        :type iotda_instance_id: str
        """
        self._iotda_instance_id = iotda_instance_id

    @property
    def rules(self):
        """Gets the rules of this EdgeContentRsp.

        在Edge实例中要配置的转发规则，包含推送数据的资源空间和产品列表

        :return: The rules of this EdgeContentRsp.
        :rtype: list[:class:`huaweicloudsdkiotanalytics.v1.EdgeContentRuleRsp`]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        """Sets the rules of this EdgeContentRsp.

        在Edge实例中要配置的转发规则，包含推送数据的资源空间和产品列表

        :param rules: The rules of this EdgeContentRsp.
        :type rules: list[:class:`huaweicloudsdkiotanalytics.v1.EdgeContentRuleRsp`]
        """
        self._rules = rules

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
        if not isinstance(other, EdgeContentRsp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
