# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StartPipelineResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'result': 'str'
    }

    attribute_map = {
        'id': 'id',
        'result': 'result'
    }

    def __init__(self, id=None, result=None):
        """StartPipelineResponse

        The model defined in huaweicloud sdk

        :param id: 流水线id
        :type id: str
        :param result: 流水线操作成功
        :type result: str
        """
        
        super(StartPipelineResponse, self).__init__()

        self._id = None
        self._result = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if result is not None:
            self.result = result

    @property
    def id(self):
        """Gets the id of this StartPipelineResponse.

        流水线id

        :return: The id of this StartPipelineResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this StartPipelineResponse.

        流水线id

        :param id: The id of this StartPipelineResponse.
        :type id: str
        """
        self._id = id

    @property
    def result(self):
        """Gets the result of this StartPipelineResponse.

        流水线操作成功

        :return: The result of this StartPipelineResponse.
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this StartPipelineResponse.

        流水线操作成功

        :param result: The result of this StartPipelineResponse.
        :type result: str
        """
        self._result = result

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
        if not isinstance(other, StartPipelineResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
