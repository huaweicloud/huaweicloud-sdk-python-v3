# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreatePeriodElasticResourcePoolSpecChangeOrderRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'elastic_resource_pool_name': 'str',
        'target_cu': 'int'
    }

    attribute_map = {
        'elastic_resource_pool_name': 'elastic_resource_pool_name',
        'target_cu': 'target_cu'
    }

    def __init__(self, elastic_resource_pool_name=None, target_cu=None):
        r"""CreatePeriodElasticResourcePoolSpecChangeOrderRequestBody

        The model defined in huaweicloud sdk

        :param elastic_resource_pool_name: 弹性资源池名称，名称只能包含数字、小写英文字母和下划线，但不能是纯数字，且不能以下划线开头。长度限制：1~128个字符。
        :type elastic_resource_pool_name: str
        :param target_cu: 包周期目标CU大小
        :type target_cu: int
        """
        
        

        self._elastic_resource_pool_name = None
        self._target_cu = None
        self.discriminator = None

        self.elastic_resource_pool_name = elastic_resource_pool_name
        self.target_cu = target_cu

    @property
    def elastic_resource_pool_name(self):
        r"""Gets the elastic_resource_pool_name of this CreatePeriodElasticResourcePoolSpecChangeOrderRequestBody.

        弹性资源池名称，名称只能包含数字、小写英文字母和下划线，但不能是纯数字，且不能以下划线开头。长度限制：1~128个字符。

        :return: The elastic_resource_pool_name of this CreatePeriodElasticResourcePoolSpecChangeOrderRequestBody.
        :rtype: str
        """
        return self._elastic_resource_pool_name

    @elastic_resource_pool_name.setter
    def elastic_resource_pool_name(self, elastic_resource_pool_name):
        r"""Sets the elastic_resource_pool_name of this CreatePeriodElasticResourcePoolSpecChangeOrderRequestBody.

        弹性资源池名称，名称只能包含数字、小写英文字母和下划线，但不能是纯数字，且不能以下划线开头。长度限制：1~128个字符。

        :param elastic_resource_pool_name: The elastic_resource_pool_name of this CreatePeriodElasticResourcePoolSpecChangeOrderRequestBody.
        :type elastic_resource_pool_name: str
        """
        self._elastic_resource_pool_name = elastic_resource_pool_name

    @property
    def target_cu(self):
        r"""Gets the target_cu of this CreatePeriodElasticResourcePoolSpecChangeOrderRequestBody.

        包周期目标CU大小

        :return: The target_cu of this CreatePeriodElasticResourcePoolSpecChangeOrderRequestBody.
        :rtype: int
        """
        return self._target_cu

    @target_cu.setter
    def target_cu(self, target_cu):
        r"""Sets the target_cu of this CreatePeriodElasticResourcePoolSpecChangeOrderRequestBody.

        包周期目标CU大小

        :param target_cu: The target_cu of this CreatePeriodElasticResourcePoolSpecChangeOrderRequestBody.
        :type target_cu: int
        """
        self._target_cu = target_cu

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
        if not isinstance(other, CreatePeriodElasticResourcePoolSpecChangeOrderRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
