# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BeneficiaryItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'beneficiary_name': 'InsurancePolicyDetail',
        'beneficiary_type': 'InsurancePolicyDetail',
        'beneficiary_order': 'InsurancePolicyDetail',
        'beneficiary_share': 'InsurancePolicyDetail'
    }

    attribute_map = {
        'beneficiary_name': 'beneficiary_name',
        'beneficiary_type': 'beneficiary_type',
        'beneficiary_order': 'beneficiary_order',
        'beneficiary_share': 'beneficiary_share'
    }

    def __init__(self, beneficiary_name=None, beneficiary_type=None, beneficiary_order=None, beneficiary_share=None):
        """BeneficiaryItem

        The model defined in huaweicloud sdk

        :param beneficiary_name: 
        :type beneficiary_name: :class:`huaweicloudsdkocr.v1.InsurancePolicyDetail`
        :param beneficiary_type: 
        :type beneficiary_type: :class:`huaweicloudsdkocr.v1.InsurancePolicyDetail`
        :param beneficiary_order: 
        :type beneficiary_order: :class:`huaweicloudsdkocr.v1.InsurancePolicyDetail`
        :param beneficiary_share: 
        :type beneficiary_share: :class:`huaweicloudsdkocr.v1.InsurancePolicyDetail`
        """
        
        

        self._beneficiary_name = None
        self._beneficiary_type = None
        self._beneficiary_order = None
        self._beneficiary_share = None
        self.discriminator = None

        if beneficiary_name is not None:
            self.beneficiary_name = beneficiary_name
        if beneficiary_type is not None:
            self.beneficiary_type = beneficiary_type
        if beneficiary_order is not None:
            self.beneficiary_order = beneficiary_order
        if beneficiary_share is not None:
            self.beneficiary_share = beneficiary_share

    @property
    def beneficiary_name(self):
        """Gets the beneficiary_name of this BeneficiaryItem.

        :return: The beneficiary_name of this BeneficiaryItem.
        :rtype: :class:`huaweicloudsdkocr.v1.InsurancePolicyDetail`
        """
        return self._beneficiary_name

    @beneficiary_name.setter
    def beneficiary_name(self, beneficiary_name):
        """Sets the beneficiary_name of this BeneficiaryItem.

        :param beneficiary_name: The beneficiary_name of this BeneficiaryItem.
        :type beneficiary_name: :class:`huaweicloudsdkocr.v1.InsurancePolicyDetail`
        """
        self._beneficiary_name = beneficiary_name

    @property
    def beneficiary_type(self):
        """Gets the beneficiary_type of this BeneficiaryItem.

        :return: The beneficiary_type of this BeneficiaryItem.
        :rtype: :class:`huaweicloudsdkocr.v1.InsurancePolicyDetail`
        """
        return self._beneficiary_type

    @beneficiary_type.setter
    def beneficiary_type(self, beneficiary_type):
        """Sets the beneficiary_type of this BeneficiaryItem.

        :param beneficiary_type: The beneficiary_type of this BeneficiaryItem.
        :type beneficiary_type: :class:`huaweicloudsdkocr.v1.InsurancePolicyDetail`
        """
        self._beneficiary_type = beneficiary_type

    @property
    def beneficiary_order(self):
        """Gets the beneficiary_order of this BeneficiaryItem.

        :return: The beneficiary_order of this BeneficiaryItem.
        :rtype: :class:`huaweicloudsdkocr.v1.InsurancePolicyDetail`
        """
        return self._beneficiary_order

    @beneficiary_order.setter
    def beneficiary_order(self, beneficiary_order):
        """Sets the beneficiary_order of this BeneficiaryItem.

        :param beneficiary_order: The beneficiary_order of this BeneficiaryItem.
        :type beneficiary_order: :class:`huaweicloudsdkocr.v1.InsurancePolicyDetail`
        """
        self._beneficiary_order = beneficiary_order

    @property
    def beneficiary_share(self):
        """Gets the beneficiary_share of this BeneficiaryItem.

        :return: The beneficiary_share of this BeneficiaryItem.
        :rtype: :class:`huaweicloudsdkocr.v1.InsurancePolicyDetail`
        """
        return self._beneficiary_share

    @beneficiary_share.setter
    def beneficiary_share(self, beneficiary_share):
        """Sets the beneficiary_share of this BeneficiaryItem.

        :param beneficiary_share: The beneficiary_share of this BeneficiaryItem.
        :type beneficiary_share: :class:`huaweicloudsdkocr.v1.InsurancePolicyDetail`
        """
        self._beneficiary_share = beneficiary_share

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
        if not isinstance(other, BeneficiaryItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
