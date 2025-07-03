# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CustomerUpgradeMajorVersionReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'delay': 'bool',
        'configuration_id': 'str'
    }

    attribute_map = {
        'delay': 'delay',
        'configuration_id': 'configuration_id'
    }

    def __init__(self, delay=None, configuration_id=None):
        r"""CustomerUpgradeMajorVersionReq

        The model defined in huaweicloud sdk

        :param delay: 是否在运维时间窗内切换版本,默认为否。
        :type delay: bool
        :param configuration_id: 指定新版本的参数模板，若不填则默认会最大限度继承原实例的参数。
        :type configuration_id: str
        """
        
        

        self._delay = None
        self._configuration_id = None
        self.discriminator = None

        if delay is not None:
            self.delay = delay
        if configuration_id is not None:
            self.configuration_id = configuration_id

    @property
    def delay(self):
        r"""Gets the delay of this CustomerUpgradeMajorVersionReq.

        是否在运维时间窗内切换版本,默认为否。

        :return: The delay of this CustomerUpgradeMajorVersionReq.
        :rtype: bool
        """
        return self._delay

    @delay.setter
    def delay(self, delay):
        r"""Sets the delay of this CustomerUpgradeMajorVersionReq.

        是否在运维时间窗内切换版本,默认为否。

        :param delay: The delay of this CustomerUpgradeMajorVersionReq.
        :type delay: bool
        """
        self._delay = delay

    @property
    def configuration_id(self):
        r"""Gets the configuration_id of this CustomerUpgradeMajorVersionReq.

        指定新版本的参数模板，若不填则默认会最大限度继承原实例的参数。

        :return: The configuration_id of this CustomerUpgradeMajorVersionReq.
        :rtype: str
        """
        return self._configuration_id

    @configuration_id.setter
    def configuration_id(self, configuration_id):
        r"""Sets the configuration_id of this CustomerUpgradeMajorVersionReq.

        指定新版本的参数模板，若不填则默认会最大限度继承原实例的参数。

        :param configuration_id: The configuration_id of this CustomerUpgradeMajorVersionReq.
        :type configuration_id: str
        """
        self._configuration_id = configuration_id

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
        if not isinstance(other, CustomerUpgradeMajorVersionReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
