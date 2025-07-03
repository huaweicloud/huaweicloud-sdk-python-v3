# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModifyFlowSourcesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'flow_id': 'str',
        'source': 'FlowSource'
    }

    attribute_map = {
        'flow_id': 'flow_id',
        'source': 'source'
    }

    def __init__(self, flow_id=None, source=None):
        r"""ModifyFlowSourcesResponse

        The model defined in huaweicloud sdk

        :param flow_id: 流id
        :type flow_id: str
        :param source: 
        :type source: :class:`huaweicloudsdklive.v1.FlowSource`
        """
        
        super(ModifyFlowSourcesResponse, self).__init__()

        self._flow_id = None
        self._source = None
        self.discriminator = None

        if flow_id is not None:
            self.flow_id = flow_id
        if source is not None:
            self.source = source

    @property
    def flow_id(self):
        r"""Gets the flow_id of this ModifyFlowSourcesResponse.

        流id

        :return: The flow_id of this ModifyFlowSourcesResponse.
        :rtype: str
        """
        return self._flow_id

    @flow_id.setter
    def flow_id(self, flow_id):
        r"""Sets the flow_id of this ModifyFlowSourcesResponse.

        流id

        :param flow_id: The flow_id of this ModifyFlowSourcesResponse.
        :type flow_id: str
        """
        self._flow_id = flow_id

    @property
    def source(self):
        r"""Gets the source of this ModifyFlowSourcesResponse.

        :return: The source of this ModifyFlowSourcesResponse.
        :rtype: :class:`huaweicloudsdklive.v1.FlowSource`
        """
        return self._source

    @source.setter
    def source(self, source):
        r"""Sets the source of this ModifyFlowSourcesResponse.

        :param source: The source of this ModifyFlowSourcesResponse.
        :type source: :class:`huaweicloudsdklive.v1.FlowSource`
        """
        self._source = source

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
        if not isinstance(other, ModifyFlowSourcesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
