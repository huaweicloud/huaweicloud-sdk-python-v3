# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowFlowGraphRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'build_flow_record_id': 'str'
    }

    attribute_map = {
        'build_flow_record_id': 'build_flow_record_id'
    }

    def __init__(self, build_flow_record_id=None):
        r"""ShowFlowGraphRequest

        The model defined in huaweicloud sdk

        :param build_flow_record_id: 父任务构建记录ID
        :type build_flow_record_id: str
        """
        
        

        self._build_flow_record_id = None
        self.discriminator = None

        self.build_flow_record_id = build_flow_record_id

    @property
    def build_flow_record_id(self):
        r"""Gets the build_flow_record_id of this ShowFlowGraphRequest.

        父任务构建记录ID

        :return: The build_flow_record_id of this ShowFlowGraphRequest.
        :rtype: str
        """
        return self._build_flow_record_id

    @build_flow_record_id.setter
    def build_flow_record_id(self, build_flow_record_id):
        r"""Sets the build_flow_record_id of this ShowFlowGraphRequest.

        父任务构建记录ID

        :param build_flow_record_id: The build_flow_record_id of this ShowFlowGraphRequest.
        :type build_flow_record_id: str
        """
        self._build_flow_record_id = build_flow_record_id

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
        if not isinstance(other, ShowFlowGraphRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
