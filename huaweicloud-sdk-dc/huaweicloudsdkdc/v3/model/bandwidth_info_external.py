# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BandwidthInfoExternal:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'bandwidth_size': 'int',
        'gcb_id': 'str',
        'freeze_status': 'str'
    }

    attribute_map = {
        'bandwidth_size': 'bandwidth_size',
        'gcb_id': 'gcb_id',
        'freeze_status': 'freeze_status'
    }

    def __init__(self, bandwidth_size=None, gcb_id=None, freeze_status=None):
        """BandwidthInfoExternal

        The model defined in huaweicloud sdk

        :param bandwidth_size: 带宽值
        :type bandwidth_size: int
        :param gcb_id: 带宽包ID
        :type gcb_id: str
        :param freeze_status: 冻结状态
        :type freeze_status: str
        """
        
        

        self._bandwidth_size = None
        self._gcb_id = None
        self._freeze_status = None
        self.discriminator = None

        if bandwidth_size is not None:
            self.bandwidth_size = bandwidth_size
        if gcb_id is not None:
            self.gcb_id = gcb_id
        if freeze_status is not None:
            self.freeze_status = freeze_status

    @property
    def bandwidth_size(self):
        """Gets the bandwidth_size of this BandwidthInfoExternal.

        带宽值

        :return: The bandwidth_size of this BandwidthInfoExternal.
        :rtype: int
        """
        return self._bandwidth_size

    @bandwidth_size.setter
    def bandwidth_size(self, bandwidth_size):
        """Sets the bandwidth_size of this BandwidthInfoExternal.

        带宽值

        :param bandwidth_size: The bandwidth_size of this BandwidthInfoExternal.
        :type bandwidth_size: int
        """
        self._bandwidth_size = bandwidth_size

    @property
    def gcb_id(self):
        """Gets the gcb_id of this BandwidthInfoExternal.

        带宽包ID

        :return: The gcb_id of this BandwidthInfoExternal.
        :rtype: str
        """
        return self._gcb_id

    @gcb_id.setter
    def gcb_id(self, gcb_id):
        """Sets the gcb_id of this BandwidthInfoExternal.

        带宽包ID

        :param gcb_id: The gcb_id of this BandwidthInfoExternal.
        :type gcb_id: str
        """
        self._gcb_id = gcb_id

    @property
    def freeze_status(self):
        """Gets the freeze_status of this BandwidthInfoExternal.

        冻结状态

        :return: The freeze_status of this BandwidthInfoExternal.
        :rtype: str
        """
        return self._freeze_status

    @freeze_status.setter
    def freeze_status(self, freeze_status):
        """Sets the freeze_status of this BandwidthInfoExternal.

        冻结状态

        :param freeze_status: The freeze_status of this BandwidthInfoExternal.
        :type freeze_status: str
        """
        self._freeze_status = freeze_status

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
        if not isinstance(other, BandwidthInfoExternal):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
