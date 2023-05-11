# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModifyIpWhitelistBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'enable_whitelist': 'bool',
        'whitelist': 'list[Whitelist]'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'enable_whitelist': 'enable_whitelist',
        'whitelist': 'whitelist'
    }

    def __init__(self, instance_id=None, enable_whitelist=None, whitelist=None):
        """ModifyIpWhitelistBody

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID
        :type instance_id: str
        :param enable_whitelist: 是否启用白名单（true/false）。
        :type enable_whitelist: bool
        :param whitelist: IP白名单分组列表。
        :type whitelist: list[:class:`huaweicloudsdkdcs.v2.Whitelist`]
        """
        
        

        self._instance_id = None
        self._enable_whitelist = None
        self._whitelist = None
        self.discriminator = None

        if instance_id is not None:
            self.instance_id = instance_id
        self.enable_whitelist = enable_whitelist
        self.whitelist = whitelist

    @property
    def instance_id(self):
        """Gets the instance_id of this ModifyIpWhitelistBody.

        实例ID

        :return: The instance_id of this ModifyIpWhitelistBody.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ModifyIpWhitelistBody.

        实例ID

        :param instance_id: The instance_id of this ModifyIpWhitelistBody.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def enable_whitelist(self):
        """Gets the enable_whitelist of this ModifyIpWhitelistBody.

        是否启用白名单（true/false）。

        :return: The enable_whitelist of this ModifyIpWhitelistBody.
        :rtype: bool
        """
        return self._enable_whitelist

    @enable_whitelist.setter
    def enable_whitelist(self, enable_whitelist):
        """Sets the enable_whitelist of this ModifyIpWhitelistBody.

        是否启用白名单（true/false）。

        :param enable_whitelist: The enable_whitelist of this ModifyIpWhitelistBody.
        :type enable_whitelist: bool
        """
        self._enable_whitelist = enable_whitelist

    @property
    def whitelist(self):
        """Gets the whitelist of this ModifyIpWhitelistBody.

        IP白名单分组列表。

        :return: The whitelist of this ModifyIpWhitelistBody.
        :rtype: list[:class:`huaweicloudsdkdcs.v2.Whitelist`]
        """
        return self._whitelist

    @whitelist.setter
    def whitelist(self, whitelist):
        """Sets the whitelist of this ModifyIpWhitelistBody.

        IP白名单分组列表。

        :param whitelist: The whitelist of this ModifyIpWhitelistBody.
        :type whitelist: list[:class:`huaweicloudsdkdcs.v2.Whitelist`]
        """
        self._whitelist = whitelist

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
        if not isinstance(other, ModifyIpWhitelistBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
