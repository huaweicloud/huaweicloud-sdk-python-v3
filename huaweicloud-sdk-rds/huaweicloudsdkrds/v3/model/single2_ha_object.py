# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Single2HaObject:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'az_code_new_node': 'str',
        'dsspool_id': 'str',
        'is_auto_pay': 'bool',
        'ad_domain_info': 'ADDomainInfo'
    }

    attribute_map = {
        'az_code_new_node': 'az_code_new_node',
        'dsspool_id': 'dsspool_id',
        'is_auto_pay': 'is_auto_pay',
        'ad_domain_info': 'ad_domain_info'
    }

    def __init__(self, az_code_new_node=None, dsspool_id=None, is_auto_pay=None, ad_domain_info=None):
        """Single2HaObject

        The model defined in huaweicloud sdk

        :param az_code_new_node: 实例节点可用区码（AZ）。
        :type az_code_new_node: str
        :param dsspool_id: Dec用户专属存储ID，每个az配置的专属存储不同，实例节点所在专属存储ID，仅支持DEC用户创建时使用。
        :type dsspool_id: str
        :param is_auto_pay: 仅包周期实例进行单机转主备时可指定，表示是否自动从客户的账户中支付。 - true，为自动支付。 - false，为手动支付，默认该方式。
        :type is_auto_pay: bool
        :param ad_domain_info: 
        :type ad_domain_info: :class:`huaweicloudsdkrds.v3.ADDomainInfo`
        """
        
        

        self._az_code_new_node = None
        self._dsspool_id = None
        self._is_auto_pay = None
        self._ad_domain_info = None
        self.discriminator = None

        self.az_code_new_node = az_code_new_node
        if dsspool_id is not None:
            self.dsspool_id = dsspool_id
        if is_auto_pay is not None:
            self.is_auto_pay = is_auto_pay
        if ad_domain_info is not None:
            self.ad_domain_info = ad_domain_info

    @property
    def az_code_new_node(self):
        """Gets the az_code_new_node of this Single2HaObject.

        实例节点可用区码（AZ）。

        :return: The az_code_new_node of this Single2HaObject.
        :rtype: str
        """
        return self._az_code_new_node

    @az_code_new_node.setter
    def az_code_new_node(self, az_code_new_node):
        """Sets the az_code_new_node of this Single2HaObject.

        实例节点可用区码（AZ）。

        :param az_code_new_node: The az_code_new_node of this Single2HaObject.
        :type az_code_new_node: str
        """
        self._az_code_new_node = az_code_new_node

    @property
    def dsspool_id(self):
        """Gets the dsspool_id of this Single2HaObject.

        Dec用户专属存储ID，每个az配置的专属存储不同，实例节点所在专属存储ID，仅支持DEC用户创建时使用。

        :return: The dsspool_id of this Single2HaObject.
        :rtype: str
        """
        return self._dsspool_id

    @dsspool_id.setter
    def dsspool_id(self, dsspool_id):
        """Sets the dsspool_id of this Single2HaObject.

        Dec用户专属存储ID，每个az配置的专属存储不同，实例节点所在专属存储ID，仅支持DEC用户创建时使用。

        :param dsspool_id: The dsspool_id of this Single2HaObject.
        :type dsspool_id: str
        """
        self._dsspool_id = dsspool_id

    @property
    def is_auto_pay(self):
        """Gets the is_auto_pay of this Single2HaObject.

        仅包周期实例进行单机转主备时可指定，表示是否自动从客户的账户中支付。 - true，为自动支付。 - false，为手动支付，默认该方式。

        :return: The is_auto_pay of this Single2HaObject.
        :rtype: bool
        """
        return self._is_auto_pay

    @is_auto_pay.setter
    def is_auto_pay(self, is_auto_pay):
        """Sets the is_auto_pay of this Single2HaObject.

        仅包周期实例进行单机转主备时可指定，表示是否自动从客户的账户中支付。 - true，为自动支付。 - false，为手动支付，默认该方式。

        :param is_auto_pay: The is_auto_pay of this Single2HaObject.
        :type is_auto_pay: bool
        """
        self._is_auto_pay = is_auto_pay

    @property
    def ad_domain_info(self):
        """Gets the ad_domain_info of this Single2HaObject.

        :return: The ad_domain_info of this Single2HaObject.
        :rtype: :class:`huaweicloudsdkrds.v3.ADDomainInfo`
        """
        return self._ad_domain_info

    @ad_domain_info.setter
    def ad_domain_info(self, ad_domain_info):
        """Sets the ad_domain_info of this Single2HaObject.

        :param ad_domain_info: The ad_domain_info of this Single2HaObject.
        :type ad_domain_info: :class:`huaweicloudsdkrds.v3.ADDomainInfo`
        """
        self._ad_domain_info = ad_domain_info

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
        if not isinstance(other, Single2HaObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
