# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModifyElbVipOpenReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'group_id': 'str',
        'new_ip': 'str'
    }

    attribute_map = {
        'group_id': 'group_id',
        'new_ip': 'new_ip'
    }

    def __init__(self, group_id=None, new_ip=None):
        r"""ModifyElbVipOpenReq

        The model defined in huaweicloud sdk

        :param group_id: 组id。
        :type group_id: str
        :param new_ip: 新ip。
        :type new_ip: str
        """
        
        

        self._group_id = None
        self._new_ip = None
        self.discriminator = None

        if group_id is not None:
            self.group_id = group_id
        if new_ip is not None:
            self.new_ip = new_ip

    @property
    def group_id(self):
        r"""Gets the group_id of this ModifyElbVipOpenReq.

        组id。

        :return: The group_id of this ModifyElbVipOpenReq.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this ModifyElbVipOpenReq.

        组id。

        :param group_id: The group_id of this ModifyElbVipOpenReq.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def new_ip(self):
        r"""Gets the new_ip of this ModifyElbVipOpenReq.

        新ip。

        :return: The new_ip of this ModifyElbVipOpenReq.
        :rtype: str
        """
        return self._new_ip

    @new_ip.setter
    def new_ip(self, new_ip):
        r"""Sets the new_ip of this ModifyElbVipOpenReq.

        新ip。

        :param new_ip: The new_ip of this ModifyElbVipOpenReq.
        :type new_ip: str
        """
        self._new_ip = new_ip

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
        if not isinstance(other, ModifyElbVipOpenReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
