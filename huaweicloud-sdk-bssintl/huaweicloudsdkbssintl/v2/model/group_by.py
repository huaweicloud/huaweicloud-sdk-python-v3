# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GroupBy:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'key': 'str'
    }

    attribute_map = {
        'type': 'type',
        'key': 'key'
    }

    def __init__(self, type=None, key=None):
        """GroupBy

        The model defined in huaweicloud sdk

        :param type: tag：按照成本标签过滤cost_unit：按照成本单元过滤dimension：默认取值
        :type type: str
        :param key: 如果type为tag，此处取值为tag的key。如果type为cost_unit，此处取值为cost_unit的key。如果type为dimension，此处取值如下：CLOUD_SERVICE_TYPE 产品类型RESOURCE_TYPE 产品ASSOCIATED_ACCOUNT 关联账号（企业主名下的所有企业子账号）REGION_CODE 区域AZ_CODE 可用区ENTERPRISE_PROJECT_ID 企业项目RES_SPEC_CODE 产品规格CHARGING_MODE 计费模式USAGE_TYPE 使用量类型BILL_TYPE 账单大类（billtype，前台需转换billdetailtype）BE_ID 运营实体（beid）PAYER_ACCOUNT_ID 支付账号RESOURCE_ID 资源
        :type key: str
        """
        
        

        self._type = None
        self._key = None
        self.discriminator = None

        self.type = type
        self.key = key

    @property
    def type(self):
        """Gets the type of this GroupBy.

        tag：按照成本标签过滤cost_unit：按照成本单元过滤dimension：默认取值

        :return: The type of this GroupBy.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this GroupBy.

        tag：按照成本标签过滤cost_unit：按照成本单元过滤dimension：默认取值

        :param type: The type of this GroupBy.
        :type type: str
        """
        self._type = type

    @property
    def key(self):
        """Gets the key of this GroupBy.

        如果type为tag，此处取值为tag的key。如果type为cost_unit，此处取值为cost_unit的key。如果type为dimension，此处取值如下：CLOUD_SERVICE_TYPE 产品类型RESOURCE_TYPE 产品ASSOCIATED_ACCOUNT 关联账号（企业主名下的所有企业子账号）REGION_CODE 区域AZ_CODE 可用区ENTERPRISE_PROJECT_ID 企业项目RES_SPEC_CODE 产品规格CHARGING_MODE 计费模式USAGE_TYPE 使用量类型BILL_TYPE 账单大类（billtype，前台需转换billdetailtype）BE_ID 运营实体（beid）PAYER_ACCOUNT_ID 支付账号RESOURCE_ID 资源

        :return: The key of this GroupBy.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this GroupBy.

        如果type为tag，此处取值为tag的key。如果type为cost_unit，此处取值为cost_unit的key。如果type为dimension，此处取值如下：CLOUD_SERVICE_TYPE 产品类型RESOURCE_TYPE 产品ASSOCIATED_ACCOUNT 关联账号（企业主名下的所有企业子账号）REGION_CODE 区域AZ_CODE 可用区ENTERPRISE_PROJECT_ID 企业项目RES_SPEC_CODE 产品规格CHARGING_MODE 计费模式USAGE_TYPE 使用量类型BILL_TYPE 账单大类（billtype，前台需转换billdetailtype）BE_ID 运营实体（beid）PAYER_ACCOUNT_ID 支付账号RESOURCE_ID 资源

        :param key: The key of this GroupBy.
        :type key: str
        """
        self._key = key

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
        if not isinstance(other, GroupBy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
