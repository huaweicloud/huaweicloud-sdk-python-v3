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
        'cloud_service_console_url': 'str',
        'promotion_info': 'str',
        'target_cu': 'int'
    }

    attribute_map = {
        'elastic_resource_pool_name': 'elastic_resource_pool_name',
        'cloud_service_console_url': 'cloud_service_console_url',
        'promotion_info': 'promotion_info',
        'target_cu': 'target_cu'
    }

    def __init__(self, elastic_resource_pool_name=None, cloud_service_console_url=None, promotion_info=None, target_cu=None):
        r"""CreatePeriodElasticResourcePoolSpecChangeOrderRequestBody

        The model defined in huaweicloud sdk

        :param elastic_resource_pool_name: 弹性资源池名称，名称只能包含数字、小写英文字母和下划线，但不能是纯数字，且不能以下划线开头。长度限制：1~128个字符。
        :type elastic_resource_pool_name: str
        :param cloud_service_console_url: CBC订单跳转DLI console链接
        :type cloud_service_console_url: str
        :param promotion_info: 优惠信息
        :type promotion_info: str
        :param target_cu: 包周期目标CU大小
        :type target_cu: int
        """
        
        

        self._elastic_resource_pool_name = None
        self._cloud_service_console_url = None
        self._promotion_info = None
        self._target_cu = None
        self.discriminator = None

        self.elastic_resource_pool_name = elastic_resource_pool_name
        if cloud_service_console_url is not None:
            self.cloud_service_console_url = cloud_service_console_url
        if promotion_info is not None:
            self.promotion_info = promotion_info
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
    def cloud_service_console_url(self):
        r"""Gets the cloud_service_console_url of this CreatePeriodElasticResourcePoolSpecChangeOrderRequestBody.

        CBC订单跳转DLI console链接

        :return: The cloud_service_console_url of this CreatePeriodElasticResourcePoolSpecChangeOrderRequestBody.
        :rtype: str
        """
        return self._cloud_service_console_url

    @cloud_service_console_url.setter
    def cloud_service_console_url(self, cloud_service_console_url):
        r"""Sets the cloud_service_console_url of this CreatePeriodElasticResourcePoolSpecChangeOrderRequestBody.

        CBC订单跳转DLI console链接

        :param cloud_service_console_url: The cloud_service_console_url of this CreatePeriodElasticResourcePoolSpecChangeOrderRequestBody.
        :type cloud_service_console_url: str
        """
        self._cloud_service_console_url = cloud_service_console_url

    @property
    def promotion_info(self):
        r"""Gets the promotion_info of this CreatePeriodElasticResourcePoolSpecChangeOrderRequestBody.

        优惠信息

        :return: The promotion_info of this CreatePeriodElasticResourcePoolSpecChangeOrderRequestBody.
        :rtype: str
        """
        return self._promotion_info

    @promotion_info.setter
    def promotion_info(self, promotion_info):
        r"""Sets the promotion_info of this CreatePeriodElasticResourcePoolSpecChangeOrderRequestBody.

        优惠信息

        :param promotion_info: The promotion_info of this CreatePeriodElasticResourcePoolSpecChangeOrderRequestBody.
        :type promotion_info: str
        """
        self._promotion_info = promotion_info

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
