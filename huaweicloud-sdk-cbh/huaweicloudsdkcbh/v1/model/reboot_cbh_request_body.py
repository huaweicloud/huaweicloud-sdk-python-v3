# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RebootCbhRequestBody:

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
        'reboot': 'RebootType'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'reboot': 'reboot'
    }

    def __init__(self, instance_id=None, reboot=None):
        r"""RebootCbhRequestBody

        The model defined in huaweicloud sdk

        :param instance_id: 云堡垒机实例ID，使用UUID格式。
        :type instance_id: str
        :param reboot: 
        :type reboot: :class:`huaweicloudsdkcbh.v1.RebootType`
        """
        
        

        self._instance_id = None
        self._reboot = None
        self.discriminator = None

        self.instance_id = instance_id
        self.reboot = reboot

    @property
    def instance_id(self):
        r"""Gets the instance_id of this RebootCbhRequestBody.

        云堡垒机实例ID，使用UUID格式。

        :return: The instance_id of this RebootCbhRequestBody.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this RebootCbhRequestBody.

        云堡垒机实例ID，使用UUID格式。

        :param instance_id: The instance_id of this RebootCbhRequestBody.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def reboot(self):
        r"""Gets the reboot of this RebootCbhRequestBody.

        :return: The reboot of this RebootCbhRequestBody.
        :rtype: :class:`huaweicloudsdkcbh.v1.RebootType`
        """
        return self._reboot

    @reboot.setter
    def reboot(self, reboot):
        r"""Sets the reboot of this RebootCbhRequestBody.

        :param reboot: The reboot of this RebootCbhRequestBody.
        :type reboot: :class:`huaweicloudsdkcbh.v1.RebootType`
        """
        self._reboot = reboot

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
        if not isinstance(other, RebootCbhRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
