# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowContainerProtectionStatusResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'no_risk': 'int',
        'risk': 'int',
        'no_protect': 'int',
        'total_num': 'int'
    }

    attribute_map = {
        'no_risk': 'no_risk',
        'risk': 'risk',
        'no_protect': 'no_protect',
        'total_num': 'total_num'
    }

    def __init__(self, no_risk=None, risk=None, no_protect=None, total_num=None):
        r"""ShowContainerProtectionStatusResponse

        The model defined in huaweicloud sdk

        :param no_risk: 无风险的容器数
        :type no_risk: int
        :param risk: 有风险的容器数
        :type risk: int
        :param no_protect: 未防护的容器数
        :type no_protect: int
        :param total_num: 容器总数
        :type total_num: int
        """
        
        super(ShowContainerProtectionStatusResponse, self).__init__()

        self._no_risk = None
        self._risk = None
        self._no_protect = None
        self._total_num = None
        self.discriminator = None

        if no_risk is not None:
            self.no_risk = no_risk
        if risk is not None:
            self.risk = risk
        if no_protect is not None:
            self.no_protect = no_protect
        if total_num is not None:
            self.total_num = total_num

    @property
    def no_risk(self):
        r"""Gets the no_risk of this ShowContainerProtectionStatusResponse.

        无风险的容器数

        :return: The no_risk of this ShowContainerProtectionStatusResponse.
        :rtype: int
        """
        return self._no_risk

    @no_risk.setter
    def no_risk(self, no_risk):
        r"""Sets the no_risk of this ShowContainerProtectionStatusResponse.

        无风险的容器数

        :param no_risk: The no_risk of this ShowContainerProtectionStatusResponse.
        :type no_risk: int
        """
        self._no_risk = no_risk

    @property
    def risk(self):
        r"""Gets the risk of this ShowContainerProtectionStatusResponse.

        有风险的容器数

        :return: The risk of this ShowContainerProtectionStatusResponse.
        :rtype: int
        """
        return self._risk

    @risk.setter
    def risk(self, risk):
        r"""Sets the risk of this ShowContainerProtectionStatusResponse.

        有风险的容器数

        :param risk: The risk of this ShowContainerProtectionStatusResponse.
        :type risk: int
        """
        self._risk = risk

    @property
    def no_protect(self):
        r"""Gets the no_protect of this ShowContainerProtectionStatusResponse.

        未防护的容器数

        :return: The no_protect of this ShowContainerProtectionStatusResponse.
        :rtype: int
        """
        return self._no_protect

    @no_protect.setter
    def no_protect(self, no_protect):
        r"""Sets the no_protect of this ShowContainerProtectionStatusResponse.

        未防护的容器数

        :param no_protect: The no_protect of this ShowContainerProtectionStatusResponse.
        :type no_protect: int
        """
        self._no_protect = no_protect

    @property
    def total_num(self):
        r"""Gets the total_num of this ShowContainerProtectionStatusResponse.

        容器总数

        :return: The total_num of this ShowContainerProtectionStatusResponse.
        :rtype: int
        """
        return self._total_num

    @total_num.setter
    def total_num(self, total_num):
        r"""Sets the total_num of this ShowContainerProtectionStatusResponse.

        容器总数

        :param total_num: The total_num of this ShowContainerProtectionStatusResponse.
        :type total_num: int
        """
        self._total_num = total_num

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
        if not isinstance(other, ShowContainerProtectionStatusResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
