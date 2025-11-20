# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MigrateDnInfoOpenResponse:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'dn_instance_id': 'str',
        'dn_instance_name': 'str'
    }

    attribute_map = {
        'dn_instance_id': 'dn_instance_id',
        'dn_instance_name': 'dn_instance_name'
    }

    def __init__(self, dn_instance_id=None, dn_instance_name=None):
        r"""MigrateDnInfoOpenResponse

        The model defined in huaweicloud sdk

        :param dn_instance_id: rds实例id。
        :type dn_instance_id: str
        :param dn_instance_name: rds实例名称。
        :type dn_instance_name: str
        """
        
        

        self._dn_instance_id = None
        self._dn_instance_name = None
        self.discriminator = None

        if dn_instance_id is not None:
            self.dn_instance_id = dn_instance_id
        if dn_instance_name is not None:
            self.dn_instance_name = dn_instance_name

    @property
    def dn_instance_id(self):
        r"""Gets the dn_instance_id of this MigrateDnInfoOpenResponse.

        rds实例id。

        :return: The dn_instance_id of this MigrateDnInfoOpenResponse.
        :rtype: str
        """
        return self._dn_instance_id

    @dn_instance_id.setter
    def dn_instance_id(self, dn_instance_id):
        r"""Sets the dn_instance_id of this MigrateDnInfoOpenResponse.

        rds实例id。

        :param dn_instance_id: The dn_instance_id of this MigrateDnInfoOpenResponse.
        :type dn_instance_id: str
        """
        self._dn_instance_id = dn_instance_id

    @property
    def dn_instance_name(self):
        r"""Gets the dn_instance_name of this MigrateDnInfoOpenResponse.

        rds实例名称。

        :return: The dn_instance_name of this MigrateDnInfoOpenResponse.
        :rtype: str
        """
        return self._dn_instance_name

    @dn_instance_name.setter
    def dn_instance_name(self, dn_instance_name):
        r"""Sets the dn_instance_name of this MigrateDnInfoOpenResponse.

        rds实例名称。

        :param dn_instance_name: The dn_instance_name of this MigrateDnInfoOpenResponse.
        :type dn_instance_name: str
        """
        self._dn_instance_name = dn_instance_name

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
        if not isinstance(other, MigrateDnInfoOpenResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
