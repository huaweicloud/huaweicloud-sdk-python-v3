# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTdeStatusResponse(SdkResponse):

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
        'tde_status': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'tde_status': 'tde_status'
    }

    def __init__(self, instance_id=None, tde_status=None):
        r"""ShowTdeStatusResponse

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID
        :type instance_id: str
        :param tde_status: TDE状态
        :type tde_status: str
        """
        
        super(ShowTdeStatusResponse, self).__init__()

        self._instance_id = None
        self._tde_status = None
        self.discriminator = None

        if instance_id is not None:
            self.instance_id = instance_id
        if tde_status is not None:
            self.tde_status = tde_status

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ShowTdeStatusResponse.

        实例ID

        :return: The instance_id of this ShowTdeStatusResponse.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ShowTdeStatusResponse.

        实例ID

        :param instance_id: The instance_id of this ShowTdeStatusResponse.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def tde_status(self):
        r"""Gets the tde_status of this ShowTdeStatusResponse.

        TDE状态

        :return: The tde_status of this ShowTdeStatusResponse.
        :rtype: str
        """
        return self._tde_status

    @tde_status.setter
    def tde_status(self, tde_status):
        r"""Sets the tde_status of this ShowTdeStatusResponse.

        TDE状态

        :param tde_status: The tde_status of this ShowTdeStatusResponse.
        :type tde_status: str
        """
        self._tde_status = tde_status

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
        if not isinstance(other, ShowTdeStatusResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
