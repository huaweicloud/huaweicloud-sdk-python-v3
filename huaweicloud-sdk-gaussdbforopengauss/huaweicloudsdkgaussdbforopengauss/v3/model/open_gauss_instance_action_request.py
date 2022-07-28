# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OpenGaussInstanceActionRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'expand_cluster': 'OpenGaussExpandCluster',
        'enlarge_volume': 'OpenGaussEnlargeVolume',
        'is_auto_pay': 'str'
    }

    attribute_map = {
        'expand_cluster': 'expand_cluster',
        'enlarge_volume': 'enlarge_volume',
        'is_auto_pay': 'is_auto_pay'
    }

    def __init__(self, expand_cluster=None, enlarge_volume=None, is_auto_pay=None):
        """OpenGaussInstanceActionRequest

        The model defined in huaweicloud sdk

        :param expand_cluster: 
        :type expand_cluster: :class:`huaweicloudsdkgaussdbforopengauss.v3.OpenGaussExpandCluster`
        :param enlarge_volume: 
        :type enlarge_volume: :class:`huaweicloudsdkgaussdbforopengauss.v3.OpenGaussEnlargeVolume`
        :param is_auto_pay: 包周期实例时可指定，表示是否自动从账户中支付，此字段不影响自动续订的支付方式。  true，表示自动从账户中支付。 false，表示手动从账户中支付，默认为该方式。
        :type is_auto_pay: str
        """
        
        

        self._expand_cluster = None
        self._enlarge_volume = None
        self._is_auto_pay = None
        self.discriminator = None

        if expand_cluster is not None:
            self.expand_cluster = expand_cluster
        if enlarge_volume is not None:
            self.enlarge_volume = enlarge_volume
        if is_auto_pay is not None:
            self.is_auto_pay = is_auto_pay

    @property
    def expand_cluster(self):
        """Gets the expand_cluster of this OpenGaussInstanceActionRequest.


        :return: The expand_cluster of this OpenGaussInstanceActionRequest.
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.OpenGaussExpandCluster`
        """
        return self._expand_cluster

    @expand_cluster.setter
    def expand_cluster(self, expand_cluster):
        """Sets the expand_cluster of this OpenGaussInstanceActionRequest.


        :param expand_cluster: The expand_cluster of this OpenGaussInstanceActionRequest.
        :type expand_cluster: :class:`huaweicloudsdkgaussdbforopengauss.v3.OpenGaussExpandCluster`
        """
        self._expand_cluster = expand_cluster

    @property
    def enlarge_volume(self):
        """Gets the enlarge_volume of this OpenGaussInstanceActionRequest.


        :return: The enlarge_volume of this OpenGaussInstanceActionRequest.
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.OpenGaussEnlargeVolume`
        """
        return self._enlarge_volume

    @enlarge_volume.setter
    def enlarge_volume(self, enlarge_volume):
        """Sets the enlarge_volume of this OpenGaussInstanceActionRequest.


        :param enlarge_volume: The enlarge_volume of this OpenGaussInstanceActionRequest.
        :type enlarge_volume: :class:`huaweicloudsdkgaussdbforopengauss.v3.OpenGaussEnlargeVolume`
        """
        self._enlarge_volume = enlarge_volume

    @property
    def is_auto_pay(self):
        """Gets the is_auto_pay of this OpenGaussInstanceActionRequest.

        包周期实例时可指定，表示是否自动从账户中支付，此字段不影响自动续订的支付方式。  true，表示自动从账户中支付。 false，表示手动从账户中支付，默认为该方式。

        :return: The is_auto_pay of this OpenGaussInstanceActionRequest.
        :rtype: str
        """
        return self._is_auto_pay

    @is_auto_pay.setter
    def is_auto_pay(self, is_auto_pay):
        """Sets the is_auto_pay of this OpenGaussInstanceActionRequest.

        包周期实例时可指定，表示是否自动从账户中支付，此字段不影响自动续订的支付方式。  true，表示自动从账户中支付。 false，表示手动从账户中支付，默认为该方式。

        :param is_auto_pay: The is_auto_pay of this OpenGaussInstanceActionRequest.
        :type is_auto_pay: str
        """
        self._is_auto_pay = is_auto_pay

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
        if not isinstance(other, OpenGaussInstanceActionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
