# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchAttachSharebwDict:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'bandwidth_id': 'str',
        'publicip_id': 'str'
    }

    attribute_map = {
        'bandwidth_id': 'bandwidth_id',
        'publicip_id': 'publicip_id'
    }

    def __init__(self, bandwidth_id=None, publicip_id=None):
        """BatchAttachSharebwDict

        The model defined in huaweicloud sdk

        :param bandwidth_id: - 共享带宽的id
        :type bandwidth_id: str
        :param publicip_id: - 弹性公网IP ID
        :type publicip_id: str
        """
        
        

        self._bandwidth_id = None
        self._publicip_id = None
        self.discriminator = None

        if bandwidth_id is not None:
            self.bandwidth_id = bandwidth_id
        if publicip_id is not None:
            self.publicip_id = publicip_id

    @property
    def bandwidth_id(self):
        """Gets the bandwidth_id of this BatchAttachSharebwDict.

        - 共享带宽的id

        :return: The bandwidth_id of this BatchAttachSharebwDict.
        :rtype: str
        """
        return self._bandwidth_id

    @bandwidth_id.setter
    def bandwidth_id(self, bandwidth_id):
        """Sets the bandwidth_id of this BatchAttachSharebwDict.

        - 共享带宽的id

        :param bandwidth_id: The bandwidth_id of this BatchAttachSharebwDict.
        :type bandwidth_id: str
        """
        self._bandwidth_id = bandwidth_id

    @property
    def publicip_id(self):
        """Gets the publicip_id of this BatchAttachSharebwDict.

        - 弹性公网IP ID

        :return: The publicip_id of this BatchAttachSharebwDict.
        :rtype: str
        """
        return self._publicip_id

    @publicip_id.setter
    def publicip_id(self, publicip_id):
        """Sets the publicip_id of this BatchAttachSharebwDict.

        - 弹性公网IP ID

        :param publicip_id: The publicip_id of this BatchAttachSharebwDict.
        :type publicip_id: str
        """
        self._publicip_id = publicip_id

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
        if not isinstance(other, BatchAttachSharebwDict):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
