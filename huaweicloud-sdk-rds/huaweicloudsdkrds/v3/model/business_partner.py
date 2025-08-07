# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BusinessPartner:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'bp_domain_id': 'str',
        'bp_name': 'str',
        'order': 'int',
        'international': 'bool'
    }

    attribute_map = {
        'bp_domain_id': 'bp_domain_id',
        'bp_name': 'bp_name',
        'order': 'order',
        'international': 'international'
    }

    def __init__(self, bp_domain_id=None, bp_name=None, order=None, international=None):
        r"""BusinessPartner

        The model defined in huaweicloud sdk

        :param bp_domain_id: 服务商ID。
        :type bp_domain_id: str
        :param bp_name: 服务商名称。
        :type bp_name: str
        :param order: 优先级，整数取值范围1-100，数值越小优先级越高。
        :type order: int
        :param international: 是否是国际站服务商。
        :type international: bool
        """
        
        

        self._bp_domain_id = None
        self._bp_name = None
        self._order = None
        self._international = None
        self.discriminator = None

        if bp_domain_id is not None:
            self.bp_domain_id = bp_domain_id
        if bp_name is not None:
            self.bp_name = bp_name
        if order is not None:
            self.order = order
        if international is not None:
            self.international = international

    @property
    def bp_domain_id(self):
        r"""Gets the bp_domain_id of this BusinessPartner.

        服务商ID。

        :return: The bp_domain_id of this BusinessPartner.
        :rtype: str
        """
        return self._bp_domain_id

    @bp_domain_id.setter
    def bp_domain_id(self, bp_domain_id):
        r"""Sets the bp_domain_id of this BusinessPartner.

        服务商ID。

        :param bp_domain_id: The bp_domain_id of this BusinessPartner.
        :type bp_domain_id: str
        """
        self._bp_domain_id = bp_domain_id

    @property
    def bp_name(self):
        r"""Gets the bp_name of this BusinessPartner.

        服务商名称。

        :return: The bp_name of this BusinessPartner.
        :rtype: str
        """
        return self._bp_name

    @bp_name.setter
    def bp_name(self, bp_name):
        r"""Sets the bp_name of this BusinessPartner.

        服务商名称。

        :param bp_name: The bp_name of this BusinessPartner.
        :type bp_name: str
        """
        self._bp_name = bp_name

    @property
    def order(self):
        r"""Gets the order of this BusinessPartner.

        优先级，整数取值范围1-100，数值越小优先级越高。

        :return: The order of this BusinessPartner.
        :rtype: int
        """
        return self._order

    @order.setter
    def order(self, order):
        r"""Sets the order of this BusinessPartner.

        优先级，整数取值范围1-100，数值越小优先级越高。

        :param order: The order of this BusinessPartner.
        :type order: int
        """
        self._order = order

    @property
    def international(self):
        r"""Gets the international of this BusinessPartner.

        是否是国际站服务商。

        :return: The international of this BusinessPartner.
        :rtype: bool
        """
        return self._international

    @international.setter
    def international(self, international):
        r"""Sets the international of this BusinessPartner.

        是否是国际站服务商。

        :param international: The international of this BusinessPartner.
        :type international: bool
        """
        self._international = international

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
        if not isinstance(other, BusinessPartner):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
