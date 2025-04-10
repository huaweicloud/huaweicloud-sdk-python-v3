# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpgradeInstanceSpecV2RequestBody:

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
        'upgrade_data': 'UpgradeInstanceData'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'upgrade_data': 'upgrade_data'
    }

    def __init__(self, instance_id=None, upgrade_data=None):
        r"""UpgradeInstanceSpecV2RequestBody

        The model defined in huaweicloud sdk

        :param instance_id: 实例id
        :type instance_id: str
        :param upgrade_data: 
        :type upgrade_data: :class:`huaweicloudsdkaad.v2.UpgradeInstanceData`
        """
        
        

        self._instance_id = None
        self._upgrade_data = None
        self.discriminator = None

        self.instance_id = instance_id
        self.upgrade_data = upgrade_data

    @property
    def instance_id(self):
        r"""Gets the instance_id of this UpgradeInstanceSpecV2RequestBody.

        实例id

        :return: The instance_id of this UpgradeInstanceSpecV2RequestBody.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this UpgradeInstanceSpecV2RequestBody.

        实例id

        :param instance_id: The instance_id of this UpgradeInstanceSpecV2RequestBody.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def upgrade_data(self):
        r"""Gets the upgrade_data of this UpgradeInstanceSpecV2RequestBody.

        :return: The upgrade_data of this UpgradeInstanceSpecV2RequestBody.
        :rtype: :class:`huaweicloudsdkaad.v2.UpgradeInstanceData`
        """
        return self._upgrade_data

    @upgrade_data.setter
    def upgrade_data(self, upgrade_data):
        r"""Sets the upgrade_data of this UpgradeInstanceSpecV2RequestBody.

        :param upgrade_data: The upgrade_data of this UpgradeInstanceSpecV2RequestBody.
        :type upgrade_data: :class:`huaweicloudsdkaad.v2.UpgradeInstanceData`
        """
        self._upgrade_data = upgrade_data

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
        if not isinstance(other, UpgradeInstanceSpecV2RequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
