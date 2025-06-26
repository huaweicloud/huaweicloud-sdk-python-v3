# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ReconfigureExtDataSourceAction:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'reboot': 'bool',
        'agency': 'str'
    }

    attribute_map = {
        'reboot': 'reboot',
        'agency': 'agency'
    }

    def __init__(self, reboot=None, agency=None):
        r"""ReconfigureExtDataSourceAction

        The model defined in huaweicloud sdk

        :param reboot: **参数解释**： 重启。 **取值范围**： 不涉及。
        :type reboot: bool
        :param agency: **参数解释**： 委托。 **取值范围**： 不涉及。
        :type agency: str
        """
        
        

        self._reboot = None
        self._agency = None
        self.discriminator = None

        if reboot is not None:
            self.reboot = reboot
        if agency is not None:
            self.agency = agency

    @property
    def reboot(self):
        r"""Gets the reboot of this ReconfigureExtDataSourceAction.

        **参数解释**： 重启。 **取值范围**： 不涉及。

        :return: The reboot of this ReconfigureExtDataSourceAction.
        :rtype: bool
        """
        return self._reboot

    @reboot.setter
    def reboot(self, reboot):
        r"""Sets the reboot of this ReconfigureExtDataSourceAction.

        **参数解释**： 重启。 **取值范围**： 不涉及。

        :param reboot: The reboot of this ReconfigureExtDataSourceAction.
        :type reboot: bool
        """
        self._reboot = reboot

    @property
    def agency(self):
        r"""Gets the agency of this ReconfigureExtDataSourceAction.

        **参数解释**： 委托。 **取值范围**： 不涉及。

        :return: The agency of this ReconfigureExtDataSourceAction.
        :rtype: str
        """
        return self._agency

    @agency.setter
    def agency(self, agency):
        r"""Sets the agency of this ReconfigureExtDataSourceAction.

        **参数解释**： 委托。 **取值范围**： 不涉及。

        :param agency: The agency of this ReconfigureExtDataSourceAction.
        :type agency: str
        """
        self._agency = agency

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
        if not isinstance(other, ReconfigureExtDataSourceAction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
