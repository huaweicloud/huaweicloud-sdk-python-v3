# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RunTaskResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'exec_id': 'str'
    }

    attribute_map = {
        'exec_id': 'exec_id'
    }

    def __init__(self, exec_id=None):
        r"""RunTaskResponse

        The model defined in huaweicloud sdk

        :param exec_id: 执行id
        :type exec_id: str
        """
        
        super(RunTaskResponse, self).__init__()

        self._exec_id = None
        self.discriminator = None

        if exec_id is not None:
            self.exec_id = exec_id

    @property
    def exec_id(self):
        r"""Gets the exec_id of this RunTaskResponse.

        执行id

        :return: The exec_id of this RunTaskResponse.
        :rtype: str
        """
        return self._exec_id

    @exec_id.setter
    def exec_id(self, exec_id):
        r"""Sets the exec_id of this RunTaskResponse.

        执行id

        :param exec_id: The exec_id of this RunTaskResponse.
        :type exec_id: str
        """
        self._exec_id = exec_id

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
        if not isinstance(other, RunTaskResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
