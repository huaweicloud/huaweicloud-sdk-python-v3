# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NovaServerSchedulerHints:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tenancy': 'list[str]',
        'dedicated_host_id': 'list[str]'
    }

    attribute_map = {
        'tenancy': 'tenancy',
        'dedicated_host_id': 'dedicated_host_id'
    }

    def __init__(self, tenancy=None, dedicated_host_id=None):
        r"""NovaServerSchedulerHints

        The model defined in huaweicloud sdk

        :param tenancy: 在指定的专属主机或者共享主机上创建弹性云服务器。 参数值为shared或者dedicated。
        :type tenancy: list[str]
        :param dedicated_host_id: 专属主机ID。 此属性仅在tenancy值为dedicated时有效。
        :type dedicated_host_id: list[str]
        """
        
        

        self._tenancy = None
        self._dedicated_host_id = None
        self.discriminator = None

        if tenancy is not None:
            self.tenancy = tenancy
        if dedicated_host_id is not None:
            self.dedicated_host_id = dedicated_host_id

    @property
    def tenancy(self):
        r"""Gets the tenancy of this NovaServerSchedulerHints.

        在指定的专属主机或者共享主机上创建弹性云服务器。 参数值为shared或者dedicated。

        :return: The tenancy of this NovaServerSchedulerHints.
        :rtype: list[str]
        """
        return self._tenancy

    @tenancy.setter
    def tenancy(self, tenancy):
        r"""Sets the tenancy of this NovaServerSchedulerHints.

        在指定的专属主机或者共享主机上创建弹性云服务器。 参数值为shared或者dedicated。

        :param tenancy: The tenancy of this NovaServerSchedulerHints.
        :type tenancy: list[str]
        """
        self._tenancy = tenancy

    @property
    def dedicated_host_id(self):
        r"""Gets the dedicated_host_id of this NovaServerSchedulerHints.

        专属主机ID。 此属性仅在tenancy值为dedicated时有效。

        :return: The dedicated_host_id of this NovaServerSchedulerHints.
        :rtype: list[str]
        """
        return self._dedicated_host_id

    @dedicated_host_id.setter
    def dedicated_host_id(self, dedicated_host_id):
        r"""Sets the dedicated_host_id of this NovaServerSchedulerHints.

        专属主机ID。 此属性仅在tenancy值为dedicated时有效。

        :param dedicated_host_id: The dedicated_host_id of this NovaServerSchedulerHints.
        :type dedicated_host_id: list[str]
        """
        self._dedicated_host_id = dedicated_host_id

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
        if not isinstance(other, NovaServerSchedulerHints):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
