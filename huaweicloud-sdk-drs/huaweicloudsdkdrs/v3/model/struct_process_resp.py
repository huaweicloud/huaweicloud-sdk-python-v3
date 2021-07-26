# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StructProcessResp:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'create_time': 'str',
        'result': 'list[StructProcessVO]'
    }

    attribute_map = {
        'create_time': 'create_time',
        'result': 'result'
    }

    def __init__(self, create_time=None, result=None):
        """StructProcessResp - a model defined in huaweicloud sdk"""
        
        

        self._create_time = None
        self._result = None
        self.discriminator = None

        if create_time is not None:
            self.create_time = create_time
        if result is not None:
            self.result = result

    @property
    def create_time(self):
        """Gets the create_time of this StructProcessResp.

        数据生成时间

        :return: The create_time of this StructProcessResp.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this StructProcessResp.

        数据生成时间

        :param create_time: The create_time of this StructProcessResp.
        :type: str
        """
        self._create_time = create_time

    @property
    def result(self):
        """Gets the result of this StructProcessResp.

        对比结果

        :return: The result of this StructProcessResp.
        :rtype: list[StructProcessVO]
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this StructProcessResp.

        对比结果

        :param result: The result of this StructProcessResp.
        :type: list[StructProcessVO]
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
        import simplejson as json
        return json.dumps(sanitize_for_serialization(self))

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, StructProcessResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
