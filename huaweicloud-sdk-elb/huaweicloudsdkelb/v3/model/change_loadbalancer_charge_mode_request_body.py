# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChangeLoadbalancerChargeModeRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'loadbalancer_ids': 'list[str]',
        'charge_mode': 'str',
        'prepaid_options': 'PrepaidChangeChargeModeOption'
    }

    attribute_map = {
        'loadbalancer_ids': 'loadbalancer_ids',
        'charge_mode': 'charge_mode',
        'prepaid_options': 'prepaid_options'
    }

    def __init__(self, loadbalancer_ids=None, charge_mode=None, prepaid_options=None):
        """ChangeLoadbalancerChargeModeRequestBody

        The model defined in huaweicloud sdk

        :param loadbalancer_ids: 需要修改计费类型的负载均衡器ID列表。
        :type loadbalancer_ids: list[str]
        :param charge_mode: 计费模式。  取值： - prepaid：包周期计费。
        :type charge_mode: str
        :param prepaid_options: 
        :type prepaid_options: :class:`huaweicloudsdkelb.v3.PrepaidChangeChargeModeOption`
        """
        
        

        self._loadbalancer_ids = None
        self._charge_mode = None
        self._prepaid_options = None
        self.discriminator = None

        self.loadbalancer_ids = loadbalancer_ids
        self.charge_mode = charge_mode
        if prepaid_options is not None:
            self.prepaid_options = prepaid_options

    @property
    def loadbalancer_ids(self):
        """Gets the loadbalancer_ids of this ChangeLoadbalancerChargeModeRequestBody.

        需要修改计费类型的负载均衡器ID列表。

        :return: The loadbalancer_ids of this ChangeLoadbalancerChargeModeRequestBody.
        :rtype: list[str]
        """
        return self._loadbalancer_ids

    @loadbalancer_ids.setter
    def loadbalancer_ids(self, loadbalancer_ids):
        """Sets the loadbalancer_ids of this ChangeLoadbalancerChargeModeRequestBody.

        需要修改计费类型的负载均衡器ID列表。

        :param loadbalancer_ids: The loadbalancer_ids of this ChangeLoadbalancerChargeModeRequestBody.
        :type loadbalancer_ids: list[str]
        """
        self._loadbalancer_ids = loadbalancer_ids

    @property
    def charge_mode(self):
        """Gets the charge_mode of this ChangeLoadbalancerChargeModeRequestBody.

        计费模式。  取值： - prepaid：包周期计费。

        :return: The charge_mode of this ChangeLoadbalancerChargeModeRequestBody.
        :rtype: str
        """
        return self._charge_mode

    @charge_mode.setter
    def charge_mode(self, charge_mode):
        """Sets the charge_mode of this ChangeLoadbalancerChargeModeRequestBody.

        计费模式。  取值： - prepaid：包周期计费。

        :param charge_mode: The charge_mode of this ChangeLoadbalancerChargeModeRequestBody.
        :type charge_mode: str
        """
        self._charge_mode = charge_mode

    @property
    def prepaid_options(self):
        """Gets the prepaid_options of this ChangeLoadbalancerChargeModeRequestBody.

        :return: The prepaid_options of this ChangeLoadbalancerChargeModeRequestBody.
        :rtype: :class:`huaweicloudsdkelb.v3.PrepaidChangeChargeModeOption`
        """
        return self._prepaid_options

    @prepaid_options.setter
    def prepaid_options(self, prepaid_options):
        """Sets the prepaid_options of this ChangeLoadbalancerChargeModeRequestBody.

        :param prepaid_options: The prepaid_options of this ChangeLoadbalancerChargeModeRequestBody.
        :type prepaid_options: :class:`huaweicloudsdkelb.v3.PrepaidChangeChargeModeOption`
        """
        self._prepaid_options = prepaid_options

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
        if not isinstance(other, ChangeLoadbalancerChargeModeRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
