# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateTransferTaskReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'destination_type': 'str',
        'obs_destination_descriptor': 'OBSDestinationDescriptorRequest'
    }

    attribute_map = {
        'destination_type': 'destination_type',
        'obs_destination_descriptor': 'obs_destination_descriptor'
    }

    def __init__(self, destination_type=None, obs_destination_descriptor=None):
        r"""CreateTransferTaskReq

        The model defined in huaweicloud sdk

        :param destination_type: 转储任务类型。  - OBS：转储到OBS - MRS：转储到MRS - DLI：转储到DLI - CLOUDTABLE：转储到CloudTable - DWS：转储到DWS
        :type destination_type: str
        :param obs_destination_descriptor: 
        :type obs_destination_descriptor: :class:`huaweicloudsdkdis.v2.OBSDestinationDescriptorRequest`
        """
        
        

        self._destination_type = None
        self._obs_destination_descriptor = None
        self.discriminator = None

        self.destination_type = destination_type
        if obs_destination_descriptor is not None:
            self.obs_destination_descriptor = obs_destination_descriptor

    @property
    def destination_type(self):
        r"""Gets the destination_type of this CreateTransferTaskReq.

        转储任务类型。  - OBS：转储到OBS - MRS：转储到MRS - DLI：转储到DLI - CLOUDTABLE：转储到CloudTable - DWS：转储到DWS

        :return: The destination_type of this CreateTransferTaskReq.
        :rtype: str
        """
        return self._destination_type

    @destination_type.setter
    def destination_type(self, destination_type):
        r"""Sets the destination_type of this CreateTransferTaskReq.

        转储任务类型。  - OBS：转储到OBS - MRS：转储到MRS - DLI：转储到DLI - CLOUDTABLE：转储到CloudTable - DWS：转储到DWS

        :param destination_type: The destination_type of this CreateTransferTaskReq.
        :type destination_type: str
        """
        self._destination_type = destination_type

    @property
    def obs_destination_descriptor(self):
        r"""Gets the obs_destination_descriptor of this CreateTransferTaskReq.

        :return: The obs_destination_descriptor of this CreateTransferTaskReq.
        :rtype: :class:`huaweicloudsdkdis.v2.OBSDestinationDescriptorRequest`
        """
        return self._obs_destination_descriptor

    @obs_destination_descriptor.setter
    def obs_destination_descriptor(self, obs_destination_descriptor):
        r"""Sets the obs_destination_descriptor of this CreateTransferTaskReq.

        :param obs_destination_descriptor: The obs_destination_descriptor of this CreateTransferTaskReq.
        :type obs_destination_descriptor: :class:`huaweicloudsdkdis.v2.OBSDestinationDescriptorRequest`
        """
        self._obs_destination_descriptor = obs_destination_descriptor

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
        if not isinstance(other, CreateTransferTaskReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
