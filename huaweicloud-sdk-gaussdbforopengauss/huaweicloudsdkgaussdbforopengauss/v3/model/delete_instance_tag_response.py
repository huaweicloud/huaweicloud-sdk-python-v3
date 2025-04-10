# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteInstanceTagResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'result': 'str',
        'instance_id': 'str',
        'instance_name': 'str'
    }

    attribute_map = {
        'result': 'result',
        'instance_id': 'instance_id',
        'instance_name': 'instance_name'
    }

    def __init__(self, result=None, instance_id=None, instance_name=None):
        r"""DeleteInstanceTagResponse

        The model defined in huaweicloud sdk

        :param result: 处理结果
        :type result: str
        :param instance_id: 实例ID
        :type instance_id: str
        :param instance_name: 实例名称
        :type instance_name: str
        """
        
        super(DeleteInstanceTagResponse, self).__init__()

        self._result = None
        self._instance_id = None
        self._instance_name = None
        self.discriminator = None

        if result is not None:
            self.result = result
        if instance_id is not None:
            self.instance_id = instance_id
        if instance_name is not None:
            self.instance_name = instance_name

    @property
    def result(self):
        r"""Gets the result of this DeleteInstanceTagResponse.

        处理结果

        :return: The result of this DeleteInstanceTagResponse.
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        r"""Sets the result of this DeleteInstanceTagResponse.

        处理结果

        :param result: The result of this DeleteInstanceTagResponse.
        :type result: str
        """
        self._result = result

    @property
    def instance_id(self):
        r"""Gets the instance_id of this DeleteInstanceTagResponse.

        实例ID

        :return: The instance_id of this DeleteInstanceTagResponse.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this DeleteInstanceTagResponse.

        实例ID

        :param instance_id: The instance_id of this DeleteInstanceTagResponse.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def instance_name(self):
        r"""Gets the instance_name of this DeleteInstanceTagResponse.

        实例名称

        :return: The instance_name of this DeleteInstanceTagResponse.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        r"""Sets the instance_name of this DeleteInstanceTagResponse.

        实例名称

        :param instance_name: The instance_name of this DeleteInstanceTagResponse.
        :type instance_name: str
        """
        self._instance_name = instance_name

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
        if not isinstance(other, DeleteInstanceTagResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
