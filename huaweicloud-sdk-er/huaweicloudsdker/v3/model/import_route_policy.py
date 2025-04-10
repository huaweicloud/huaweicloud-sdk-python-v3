# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImportRoutePolicy:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'import_policy_id': 'str'
    }

    attribute_map = {
        'import_policy_id': 'import_policy_id'
    }

    def __init__(self, import_policy_id=None):
        r"""ImportRoutePolicy

        The model defined in huaweicloud sdk

        :param import_policy_id: 入方向Ipv4协议路由策略id
        :type import_policy_id: str
        """
        
        

        self._import_policy_id = None
        self.discriminator = None

        if import_policy_id is not None:
            self.import_policy_id = import_policy_id

    @property
    def import_policy_id(self):
        r"""Gets the import_policy_id of this ImportRoutePolicy.

        入方向Ipv4协议路由策略id

        :return: The import_policy_id of this ImportRoutePolicy.
        :rtype: str
        """
        return self._import_policy_id

    @import_policy_id.setter
    def import_policy_id(self, import_policy_id):
        r"""Sets the import_policy_id of this ImportRoutePolicy.

        入方向Ipv4协议路由策略id

        :param import_policy_id: The import_policy_id of this ImportRoutePolicy.
        :type import_policy_id: str
        """
        self._import_policy_id = import_policy_id

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
        if not isinstance(other, ImportRoutePolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
