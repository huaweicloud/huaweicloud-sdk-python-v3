# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChangePrepaidCloudWafRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_id': 'str',
        'is_auto_pay': 'bool',
        'waf_product_info': 'AlterWafProductInfo',
        'domain_expack_product_info': 'ExpackProductInfo',
        'bandwidth_expack_product_info': 'ExpackProductInfo',
        'rule_expack_product_info': 'ExpackProductInfo'
    }

    attribute_map = {
        'project_id': 'project_id',
        'is_auto_pay': 'is_auto_pay',
        'waf_product_info': 'waf_product_info',
        'domain_expack_product_info': 'domain_expack_product_info',
        'bandwidth_expack_product_info': 'bandwidth_expack_product_info',
        'rule_expack_product_info': 'rule_expack_product_info'
    }

    def __init__(self, project_id=None, is_auto_pay=None, waf_product_info=None, domain_expack_product_info=None, bandwidth_expack_product_info=None, rule_expack_product_info=None):
        """ChangePrepaidCloudWafRequestBody

        The model defined in huaweicloud sdk

        :param project_id: 项目id
        :type project_id: str
        :param is_auto_pay: 是否自动支付    - false: 否（需要客户手动去支付）    - true：是（自动支付）
        :type is_auto_pay: bool
        :param waf_product_info: 
        :type waf_product_info: :class:`huaweicloudsdkwaf.v1.AlterWafProductInfo`
        :param domain_expack_product_info: 
        :type domain_expack_product_info: :class:`huaweicloudsdkwaf.v1.ExpackProductInfo`
        :param bandwidth_expack_product_info: 
        :type bandwidth_expack_product_info: :class:`huaweicloudsdkwaf.v1.ExpackProductInfo`
        :param rule_expack_product_info: 
        :type rule_expack_product_info: :class:`huaweicloudsdkwaf.v1.ExpackProductInfo`
        """
        
        

        self._project_id = None
        self._is_auto_pay = None
        self._waf_product_info = None
        self._domain_expack_product_info = None
        self._bandwidth_expack_product_info = None
        self._rule_expack_product_info = None
        self.discriminator = None

        self.project_id = project_id
        self.is_auto_pay = is_auto_pay
        if waf_product_info is not None:
            self.waf_product_info = waf_product_info
        if domain_expack_product_info is not None:
            self.domain_expack_product_info = domain_expack_product_info
        if bandwidth_expack_product_info is not None:
            self.bandwidth_expack_product_info = bandwidth_expack_product_info
        if rule_expack_product_info is not None:
            self.rule_expack_product_info = rule_expack_product_info

    @property
    def project_id(self):
        """Gets the project_id of this ChangePrepaidCloudWafRequestBody.

        项目id

        :return: The project_id of this ChangePrepaidCloudWafRequestBody.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this ChangePrepaidCloudWafRequestBody.

        项目id

        :param project_id: The project_id of this ChangePrepaidCloudWafRequestBody.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def is_auto_pay(self):
        """Gets the is_auto_pay of this ChangePrepaidCloudWafRequestBody.

        是否自动支付    - false: 否（需要客户手动去支付）    - true：是（自动支付）

        :return: The is_auto_pay of this ChangePrepaidCloudWafRequestBody.
        :rtype: bool
        """
        return self._is_auto_pay

    @is_auto_pay.setter
    def is_auto_pay(self, is_auto_pay):
        """Sets the is_auto_pay of this ChangePrepaidCloudWafRequestBody.

        是否自动支付    - false: 否（需要客户手动去支付）    - true：是（自动支付）

        :param is_auto_pay: The is_auto_pay of this ChangePrepaidCloudWafRequestBody.
        :type is_auto_pay: bool
        """
        self._is_auto_pay = is_auto_pay

    @property
    def waf_product_info(self):
        """Gets the waf_product_info of this ChangePrepaidCloudWafRequestBody.

        :return: The waf_product_info of this ChangePrepaidCloudWafRequestBody.
        :rtype: :class:`huaweicloudsdkwaf.v1.AlterWafProductInfo`
        """
        return self._waf_product_info

    @waf_product_info.setter
    def waf_product_info(self, waf_product_info):
        """Sets the waf_product_info of this ChangePrepaidCloudWafRequestBody.

        :param waf_product_info: The waf_product_info of this ChangePrepaidCloudWafRequestBody.
        :type waf_product_info: :class:`huaweicloudsdkwaf.v1.AlterWafProductInfo`
        """
        self._waf_product_info = waf_product_info

    @property
    def domain_expack_product_info(self):
        """Gets the domain_expack_product_info of this ChangePrepaidCloudWafRequestBody.

        :return: The domain_expack_product_info of this ChangePrepaidCloudWafRequestBody.
        :rtype: :class:`huaweicloudsdkwaf.v1.ExpackProductInfo`
        """
        return self._domain_expack_product_info

    @domain_expack_product_info.setter
    def domain_expack_product_info(self, domain_expack_product_info):
        """Sets the domain_expack_product_info of this ChangePrepaidCloudWafRequestBody.

        :param domain_expack_product_info: The domain_expack_product_info of this ChangePrepaidCloudWafRequestBody.
        :type domain_expack_product_info: :class:`huaweicloudsdkwaf.v1.ExpackProductInfo`
        """
        self._domain_expack_product_info = domain_expack_product_info

    @property
    def bandwidth_expack_product_info(self):
        """Gets the bandwidth_expack_product_info of this ChangePrepaidCloudWafRequestBody.

        :return: The bandwidth_expack_product_info of this ChangePrepaidCloudWafRequestBody.
        :rtype: :class:`huaweicloudsdkwaf.v1.ExpackProductInfo`
        """
        return self._bandwidth_expack_product_info

    @bandwidth_expack_product_info.setter
    def bandwidth_expack_product_info(self, bandwidth_expack_product_info):
        """Sets the bandwidth_expack_product_info of this ChangePrepaidCloudWafRequestBody.

        :param bandwidth_expack_product_info: The bandwidth_expack_product_info of this ChangePrepaidCloudWafRequestBody.
        :type bandwidth_expack_product_info: :class:`huaweicloudsdkwaf.v1.ExpackProductInfo`
        """
        self._bandwidth_expack_product_info = bandwidth_expack_product_info

    @property
    def rule_expack_product_info(self):
        """Gets the rule_expack_product_info of this ChangePrepaidCloudWafRequestBody.

        :return: The rule_expack_product_info of this ChangePrepaidCloudWafRequestBody.
        :rtype: :class:`huaweicloudsdkwaf.v1.ExpackProductInfo`
        """
        return self._rule_expack_product_info

    @rule_expack_product_info.setter
    def rule_expack_product_info(self, rule_expack_product_info):
        """Sets the rule_expack_product_info of this ChangePrepaidCloudWafRequestBody.

        :param rule_expack_product_info: The rule_expack_product_info of this ChangePrepaidCloudWafRequestBody.
        :type rule_expack_product_info: :class:`huaweicloudsdkwaf.v1.ExpackProductInfo`
        """
        self._rule_expack_product_info = rule_expack_product_info

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
        if not isinstance(other, ChangePrepaidCloudWafRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
