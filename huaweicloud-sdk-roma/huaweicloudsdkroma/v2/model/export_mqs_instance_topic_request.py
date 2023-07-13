# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExportMqsInstanceTopicRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'name': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'name': 'name'
    }

    def __init__(self, instance_id=None, name=None):
        """ExportMqsInstanceTopicRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID。
        :type instance_id: str
        :param name: 待导出的topic。多个topic以“,”分隔。默认导出所有的topic。
        :type name: str
        """
        
        

        self._instance_id = None
        self._name = None
        self.discriminator = None

        self.instance_id = instance_id
        if name is not None:
            self.name = name

    @property
    def instance_id(self):
        """Gets the instance_id of this ExportMqsInstanceTopicRequest.

        实例ID。

        :return: The instance_id of this ExportMqsInstanceTopicRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ExportMqsInstanceTopicRequest.

        实例ID。

        :param instance_id: The instance_id of this ExportMqsInstanceTopicRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def name(self):
        """Gets the name of this ExportMqsInstanceTopicRequest.

        待导出的topic。多个topic以“,”分隔。默认导出所有的topic。

        :return: The name of this ExportMqsInstanceTopicRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ExportMqsInstanceTopicRequest.

        待导出的topic。多个topic以“,”分隔。默认导出所有的topic。

        :param name: The name of this ExportMqsInstanceTopicRequest.
        :type name: str
        """
        self._name = name

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
        if not isinstance(other, ExportMqsInstanceTopicRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
