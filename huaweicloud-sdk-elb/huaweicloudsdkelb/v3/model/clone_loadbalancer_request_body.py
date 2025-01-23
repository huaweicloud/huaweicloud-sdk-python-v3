# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CloneLoadbalancerRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'count': 'int',
        'target_loadbalancer_param': 'TargetLoadbalancerParam'
    }

    attribute_map = {
        'count': 'count',
        'target_loadbalancer_param': 'target_loadbalancer_param'
    }

    def __init__(self, count=None, target_loadbalancer_param=None):
        """CloneLoadbalancerRequestBody

        The model defined in huaweicloud sdk

        :param count: 参数解释：单次最大复制数量。  取值范围：1-10  默认取值：1
        :type count: int
        :param target_loadbalancer_param: 
        :type target_loadbalancer_param: :class:`huaweicloudsdkelb.v3.TargetLoadbalancerParam`
        """
        
        

        self._count = None
        self._target_loadbalancer_param = None
        self.discriminator = None

        if count is not None:
            self.count = count
        self.target_loadbalancer_param = target_loadbalancer_param

    @property
    def count(self):
        """Gets the count of this CloneLoadbalancerRequestBody.

        参数解释：单次最大复制数量。  取值范围：1-10  默认取值：1

        :return: The count of this CloneLoadbalancerRequestBody.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this CloneLoadbalancerRequestBody.

        参数解释：单次最大复制数量。  取值范围：1-10  默认取值：1

        :param count: The count of this CloneLoadbalancerRequestBody.
        :type count: int
        """
        self._count = count

    @property
    def target_loadbalancer_param(self):
        """Gets the target_loadbalancer_param of this CloneLoadbalancerRequestBody.

        :return: The target_loadbalancer_param of this CloneLoadbalancerRequestBody.
        :rtype: :class:`huaweicloudsdkelb.v3.TargetLoadbalancerParam`
        """
        return self._target_loadbalancer_param

    @target_loadbalancer_param.setter
    def target_loadbalancer_param(self, target_loadbalancer_param):
        """Sets the target_loadbalancer_param of this CloneLoadbalancerRequestBody.

        :param target_loadbalancer_param: The target_loadbalancer_param of this CloneLoadbalancerRequestBody.
        :type target_loadbalancer_param: :class:`huaweicloudsdkelb.v3.TargetLoadbalancerParam`
        """
        self._target_loadbalancer_param = target_loadbalancer_param

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
        if not isinstance(other, CloneLoadbalancerRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
