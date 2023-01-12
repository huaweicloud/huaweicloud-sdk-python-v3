# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateGraphReqGraphPublicIp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'public_bind_type': 'str',
        'eip_id': 'str'
    }

    attribute_map = {
        'public_bind_type': 'public_bind_type',
        'eip_id': 'eip_id'
    }

    def __init__(self, public_bind_type=None, eip_id=None):
        """CreateGraphReqGraphPublicIp

        The model defined in huaweicloud sdk

        :param public_bind_type: 弹性IP绑定类型，取值如下。  - auto_assign：自动绑定。 - bind_existing：使用已有。
        :type public_bind_type: str
        :param eip_id: 弹性IP的id，当publicBindType设置为bind_existing时，该值为用户某个已创建但尚未绑定的EIP的ID；当publicBindType设置为auto_assign时，该值设置为空。
        :type eip_id: str
        """
        
        

        self._public_bind_type = None
        self._eip_id = None
        self.discriminator = None

        if public_bind_type is not None:
            self.public_bind_type = public_bind_type
        if eip_id is not None:
            self.eip_id = eip_id

    @property
    def public_bind_type(self):
        """Gets the public_bind_type of this CreateGraphReqGraphPublicIp.

        弹性IP绑定类型，取值如下。  - auto_assign：自动绑定。 - bind_existing：使用已有。

        :return: The public_bind_type of this CreateGraphReqGraphPublicIp.
        :rtype: str
        """
        return self._public_bind_type

    @public_bind_type.setter
    def public_bind_type(self, public_bind_type):
        """Sets the public_bind_type of this CreateGraphReqGraphPublicIp.

        弹性IP绑定类型，取值如下。  - auto_assign：自动绑定。 - bind_existing：使用已有。

        :param public_bind_type: The public_bind_type of this CreateGraphReqGraphPublicIp.
        :type public_bind_type: str
        """
        self._public_bind_type = public_bind_type

    @property
    def eip_id(self):
        """Gets the eip_id of this CreateGraphReqGraphPublicIp.

        弹性IP的id，当publicBindType设置为bind_existing时，该值为用户某个已创建但尚未绑定的EIP的ID；当publicBindType设置为auto_assign时，该值设置为空。

        :return: The eip_id of this CreateGraphReqGraphPublicIp.
        :rtype: str
        """
        return self._eip_id

    @eip_id.setter
    def eip_id(self, eip_id):
        """Sets the eip_id of this CreateGraphReqGraphPublicIp.

        弹性IP的id，当publicBindType设置为bind_existing时，该值为用户某个已创建但尚未绑定的EIP的ID；当publicBindType设置为auto_assign时，该值设置为空。

        :param eip_id: The eip_id of this CreateGraphReqGraphPublicIp.
        :type eip_id: str
        """
        self._eip_id = eip_id

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
        if not isinstance(other, CreateGraphReqGraphPublicIp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
