# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CustomerUpgradeDatabaseVersionReqNew:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'is_delayed': 'bool',
        'second_switch': 'bool'
    }

    attribute_map = {
        'is_delayed': 'is_delayed',
        'second_switch': 'second_switch'
    }

    def __init__(self, is_delayed=None, second_switch=None):
        r"""CustomerUpgradeDatabaseVersionReqNew

        The model defined in huaweicloud sdk

        :param is_delayed: 是否延迟至可维护时间段内升级。 取值范围： - true：延迟升级。表示实例将在设置的可维护时间段内升级。 - false：立即升级，默认该方式。
        :type is_delayed: bool
        :param second_switch: 设置仅对RDS for MySQL数据库实例（主备）生效。主备实例升级过程中，备机升级成功后，会触发主备倒换继续升级主机，主机升级完成后，若主备可用区不同则触发第二次倒换，保证可用区不变。若主备可用区相同，该选项无效。 取值范围： - true：默认该方式。表示升级过程中会进行二次倒换保证主备实例可用区不变。 - false：升级过程中不进行第二次主备倒换，适合对主备所在可用区不敏感，对业务连续性敏感的客户。
        :type second_switch: bool
        """
        
        

        self._is_delayed = None
        self._second_switch = None
        self.discriminator = None

        if is_delayed is not None:
            self.is_delayed = is_delayed
        if second_switch is not None:
            self.second_switch = second_switch

    @property
    def is_delayed(self):
        r"""Gets the is_delayed of this CustomerUpgradeDatabaseVersionReqNew.

        是否延迟至可维护时间段内升级。 取值范围： - true：延迟升级。表示实例将在设置的可维护时间段内升级。 - false：立即升级，默认该方式。

        :return: The is_delayed of this CustomerUpgradeDatabaseVersionReqNew.
        :rtype: bool
        """
        return self._is_delayed

    @is_delayed.setter
    def is_delayed(self, is_delayed):
        r"""Sets the is_delayed of this CustomerUpgradeDatabaseVersionReqNew.

        是否延迟至可维护时间段内升级。 取值范围： - true：延迟升级。表示实例将在设置的可维护时间段内升级。 - false：立即升级，默认该方式。

        :param is_delayed: The is_delayed of this CustomerUpgradeDatabaseVersionReqNew.
        :type is_delayed: bool
        """
        self._is_delayed = is_delayed

    @property
    def second_switch(self):
        r"""Gets the second_switch of this CustomerUpgradeDatabaseVersionReqNew.

        设置仅对RDS for MySQL数据库实例（主备）生效。主备实例升级过程中，备机升级成功后，会触发主备倒换继续升级主机，主机升级完成后，若主备可用区不同则触发第二次倒换，保证可用区不变。若主备可用区相同，该选项无效。 取值范围： - true：默认该方式。表示升级过程中会进行二次倒换保证主备实例可用区不变。 - false：升级过程中不进行第二次主备倒换，适合对主备所在可用区不敏感，对业务连续性敏感的客户。

        :return: The second_switch of this CustomerUpgradeDatabaseVersionReqNew.
        :rtype: bool
        """
        return self._second_switch

    @second_switch.setter
    def second_switch(self, second_switch):
        r"""Sets the second_switch of this CustomerUpgradeDatabaseVersionReqNew.

        设置仅对RDS for MySQL数据库实例（主备）生效。主备实例升级过程中，备机升级成功后，会触发主备倒换继续升级主机，主机升级完成后，若主备可用区不同则触发第二次倒换，保证可用区不变。若主备可用区相同，该选项无效。 取值范围： - true：默认该方式。表示升级过程中会进行二次倒换保证主备实例可用区不变。 - false：升级过程中不进行第二次主备倒换，适合对主备所在可用区不敏感，对业务连续性敏感的客户。

        :param second_switch: The second_switch of this CustomerUpgradeDatabaseVersionReqNew.
        :type second_switch: bool
        """
        self._second_switch = second_switch

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CustomerUpgradeDatabaseVersionReqNew):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
