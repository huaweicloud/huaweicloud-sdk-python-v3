# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BussinessGroupTransferBodyDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'owner_id': 'int'
    }

    attribute_map = {
        'owner_id': 'owner_id'
    }

    def __init__(self, owner_id=None):
        r"""BussinessGroupTransferBodyDto

        The model defined in huaweicloud sdk

        :param owner_id: 移交目标用户id
        :type owner_id: int
        """
        
        

        self._owner_id = None
        self.discriminator = None

        if owner_id is not None:
            self.owner_id = owner_id

    @property
    def owner_id(self):
        r"""Gets the owner_id of this BussinessGroupTransferBodyDto.

        移交目标用户id

        :return: The owner_id of this BussinessGroupTransferBodyDto.
        :rtype: int
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        r"""Sets the owner_id of this BussinessGroupTransferBodyDto.

        移交目标用户id

        :param owner_id: The owner_id of this BussinessGroupTransferBodyDto.
        :type owner_id: int
        """
        self._owner_id = owner_id

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
        if not isinstance(other, BussinessGroupTransferBodyDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
