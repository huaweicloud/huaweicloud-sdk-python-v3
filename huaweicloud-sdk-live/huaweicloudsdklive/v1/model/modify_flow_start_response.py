# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModifyFlowStartResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'str',
        'flow_id': 'str'
    }

    attribute_map = {
        'status': 'status',
        'flow_id': 'flow_id'
    }

    def __init__(self, status=None, flow_id=None):
        r"""ModifyFlowStartResponse

        The model defined in huaweicloud sdk

        :param status: 状态，ACTIVE状态为运行状态,STANDBY状态为未启动状态
        :type status: str
        :param flow_id: 流id
        :type flow_id: str
        """
        
        super(ModifyFlowStartResponse, self).__init__()

        self._status = None
        self._flow_id = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if flow_id is not None:
            self.flow_id = flow_id

    @property
    def status(self):
        r"""Gets the status of this ModifyFlowStartResponse.

        状态，ACTIVE状态为运行状态,STANDBY状态为未启动状态

        :return: The status of this ModifyFlowStartResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ModifyFlowStartResponse.

        状态，ACTIVE状态为运行状态,STANDBY状态为未启动状态

        :param status: The status of this ModifyFlowStartResponse.
        :type status: str
        """
        self._status = status

    @property
    def flow_id(self):
        r"""Gets the flow_id of this ModifyFlowStartResponse.

        流id

        :return: The flow_id of this ModifyFlowStartResponse.
        :rtype: str
        """
        return self._flow_id

    @flow_id.setter
    def flow_id(self, flow_id):
        r"""Sets the flow_id of this ModifyFlowStartResponse.

        流id

        :param flow_id: The flow_id of this ModifyFlowStartResponse.
        :type flow_id: str
        """
        self._flow_id = flow_id

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
        if not isinstance(other, ModifyFlowStartResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
